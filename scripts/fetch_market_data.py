#!/usr/bin/env python3
"""Fetch market data from yfinance and FRED, write memory/market_snapshot.md.

Data sources:
  - yfinance: price history, fundamentals, analyst metadata, and news headlines
  - FRED public CSV endpoint (no API key): macro indicators

Output: memory/market_snapshot.md (overwritten each run)
"""

import csv
import io
import math
import re
import urllib.request
import warnings
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import yfinance as yf

warnings.filterwarnings("ignore", category=FutureWarning, module="yfinance")

ROOT = Path(__file__).resolve().parent.parent
MEMORY = ROOT / "memory"
CACHE = ROOT / ".cache" / "yfinance"
CACHE.mkdir(parents=True, exist_ok=True)
if hasattr(yf, "set_tz_cache_location"):
    yf.set_tz_cache_location(str(CACHE))

FRED_SERIES = {
    "DGS10": "US 10Y Treasury Yield (%)",
    "DGS2": "US 2Y Treasury Yield (%)",
    "IRLTLT01DEM156N": "Germany Long-Term Govt Bond Yield (%)",
    "DEXUSEU": "EUR/USD",
    "VIXCLS": "CBOE VIX",
    "DCOILBRENTEU": "Brent Crude (USD/bbl)",
}

RETURN_WINDOWS = {
    "1d": 1,
    "1w": 5,
    "1m": 21,
    "3m": 63,
}

CONTEXT_ONLY_TICKERS = {"^VIX", "^TNX", "EURUSD=X", "GC=F"}

POSITIVE_NEWS_WORDS = {
    "beat", "beats", "upgrade", "upgraded", "raise", "raised", "growth",
    "profit", "profits", "surge", "surges", "rally", "record", "strong",
    "outperform", "bullish", "buyback", "guidance", "expands", "wins",
}

NEGATIVE_NEWS_WORDS = {
    "miss", "misses", "downgrade", "downgraded", "cut", "cuts", "loss",
    "losses", "falls", "fall", "plunge", "plunges", "weak", "lawsuit",
    "probe", "risk", "risks", "bearish", "layoff", "layoffs", "warning",
}


# ---------------------------------------------------------------------------
# Ticker parsing
# ---------------------------------------------------------------------------

def parse_tickers(filepath: Path) -> list[str]:
    """Extract tickers from the first column of markdown tables in a file."""
    tickers: list[str] = []
    if not filepath.exists():
        return tickers
    for line in filepath.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 2:
            continue
        cell = cells[1]
        if not cell or cell == "Ticker" or set(cell).issubset({"-", " ", ":"}):
            continue
        tickers.append(cell)
    return tickers


# ---------------------------------------------------------------------------
# Formatting and scoring helpers
# ---------------------------------------------------------------------------

def compute_return_values(closes, today: datetime) -> dict[str, float | None]:
    """Compute 1d/1w/1m/3m/YTD returns as percentage floats."""
    if closes.empty:
        return {k: None for k in list(RETURN_WINDOWS) + ["YTD"]}

    latest = closes.iloc[-1]
    results: dict[str, float | None] = {}

    for label, days in RETURN_WINDOWS.items():
        if len(closes) > days:
            prev = closes.iloc[-(days + 1)]
            results[label] = ((latest / prev) - 1) * 100
        else:
            results[label] = None

    year_data = closes.loc[closes.index.year == today.year]
    if len(year_data) >= 2:
        results["YTD"] = ((latest / year_data.iloc[0]) - 1) * 100
    else:
        results["YTD"] = None

    return results


def fmt_pct(v: float | None) -> str:
    return f"{v:+.1f}%" if v is not None else "-"


def fmt_number(v, digits: int = 1) -> str:
    if v is None:
        return "-"
    try:
        if math.isnan(v):
            return "-"
    except TypeError:
        return "-"
    return f"{v:.{digits}f}"


def fmt_large_number(v) -> str:
    if v is None:
        return "-"
    try:
        if math.isnan(v):
            return "-"
    except TypeError:
        return "-"
    sign = "-" if v < 0 else ""
    v = abs(v)
    if v >= 1e12:
        return f"{sign}{v / 1e12:.1f}T"
    if v >= 1e9:
        return f"{sign}{v / 1e9:.1f}B"
    if v >= 1e6:
        return f"{sign}{v / 1e6:.0f}M"
    return f"{sign}{v:,.0f}"


def score_news_titles(news_items) -> tuple[int | None, str]:
    """Score recent Yahoo headlines with a transparent keyword heuristic."""
    if not news_items:
        return None, "no headlines"

    score = 0
    count = 0
    for item in news_items[:8]:
        title = item.get("title") or item.get("content", {}).get("title") or ""
        if not title:
            continue
        count += 1
        words = set(re.findall(r"[a-z]+", title.lower()))
        score += len(words & POSITIVE_NEWS_WORDS)
        score -= len(words & NEGATIVE_NEWS_WORDS)

    if count == 0:
        return None, "no usable headlines"
    if score > 1:
        label = "positive"
    elif score < -1:
        label = "negative"
    else:
        label = "neutral"
    return score, f"{label} ({score:+d}/{count})"


def score_opportunity(returns: dict[str, float | None], info: dict, rel_volume: float | None,
                      news_score: int | None) -> tuple[int, str]:
    """0-100 short-term research triage score. It is not a buy signal."""
    score = 50
    reasons: list[str] = []

    one_w = returns.get("1w")
    one_m = returns.get("1m")
    three_m = returns.get("3m")

    if one_m is not None:
        if 2 <= one_m <= 15:
            score += 12
            reasons.append("constructive 1m momentum")
        elif one_m > 25:
            score -= 8
            reasons.append("extended 1m move")
        elif one_m < -10:
            score -= 10
            reasons.append("weak 1m momentum")

    if three_m is not None:
        if 4 <= three_m <= 30:
            score += 10
            reasons.append("positive 3m trend")
        elif three_m < -15:
            score -= 8
            reasons.append("negative 3m trend")

    if one_w is not None and abs(one_w) > 12:
        score -= 8
        reasons.append("high 1w volatility")

    revenue_growth = info.get("revenueGrowth")
    profit_margin = info.get("profitMargins")
    debt_to_equity = info.get("debtToEquity")
    recommendation = info.get("recommendationMean")

    if revenue_growth is not None:
        if revenue_growth > 0.08:
            score += 8
            reasons.append("revenue growing")
        elif revenue_growth < -0.05:
            score -= 8
            reasons.append("revenue shrinking")

    if profit_margin is not None:
        if profit_margin > 0.08:
            score += 8
            reasons.append("profitable")
        elif profit_margin < 0:
            score -= 10
            reasons.append("loss-making")

    if debt_to_equity is not None and debt_to_equity > 250:
        score -= 6
        reasons.append("high leverage")

    if recommendation is not None:
        if recommendation <= 2.2:
            score += 6
            reasons.append("analysts constructive")
        elif recommendation >= 3.2:
            score -= 6
            reasons.append("analysts cautious")

    if rel_volume is not None:
        if rel_volume >= 1.5:
            score += 6
            reasons.append("volume above average")
        elif rel_volume < 0.5:
            score -= 4
            reasons.append("thin current volume")

    if news_score is not None:
        if news_score > 1:
            score += 5
            reasons.append("news tone positive")
        elif news_score < -1:
            score -= 5
            reasons.append("news tone negative")

    return max(0, min(100, score)), "; ".join(reasons[:4]) or "mixed signal set"


# ---------------------------------------------------------------------------
# yfinance
# ---------------------------------------------------------------------------

def fetch_watchlist_data(tickers: list[str]) -> tuple[str, str, list[str]]:
    """Fetch price, fundamental, and sentiment data for each ticker."""
    if not tickers:
        no_data = "*No tickers in watchlist.*\n"
        return no_data, no_data, []

    price_header = (
        "| Ticker | Currency | Close | 1d | 1w | 1m | 3m | YTD "
        "| 52w Low | 52w High | P/E | Mkt Cap |"
    )
    price_sep = "|--------|----------|-------|-----|-----|------|------|-----" \
                "|---------|----------|-----|---------|"

    score_header = (
        "| Ticker | Score | 1m trend | 3m trend | Revenue | Revenue growth "
        "| Profit margin | Debt/Equity | Rel volume | Analyst mean | Target upside "
        "| News tone | Score notes |"
    )
    score_sep = (
        "|--------|------:|---------:|---------:|--------:|---------------:|"
        "--------------:|------------:|-----------:|-------------:|--------------:|"
        "-----------|-------------|"
    )

    price_rows: list[str] = []
    score_rows: list[str] = []
    missing: list[str] = []
    today = datetime.now()

    for ticker in tickers:
        try:
            t = yf.Ticker(ticker)
            hist = t.history(period="1y")

            if hist.empty:
                missing.append(ticker)
                continue

            closes = hist["Close"]
            latest_price = closes.iloc[-1]
            returns = compute_return_values(closes, today)

            fi = t.fast_info
            currency = getattr(fi, "currency", "-")
            low52 = getattr(fi, "year_low", None)
            high52 = getattr(fi, "year_high", None)
            mcap = getattr(fi, "market_cap", None)
            avg_volume = (
                getattr(fi, "ten_day_average_volume", None)
                or getattr(fi, "three_month_average_volume", None)
            )
            current_volume = hist["Volume"].iloc[-1] if "Volume" in hist and not hist["Volume"].empty else None
            rel_volume = (current_volume / avg_volume) if current_volume and avg_volume else None

            info = t.info
            pe = info.get("trailingPE")
            revenue = info.get("totalRevenue")
            revenue_growth = info.get("revenueGrowth")
            profit_margin = info.get("profitMargins")
            debt_to_equity = info.get("debtToEquity")
            recommendation = info.get("recommendationMean")
            target_mean = info.get("targetMeanPrice")
            target_upside = (target_mean / latest_price - 1) * 100 if target_mean and latest_price else None

            try:
                news_score, news_label = score_news_titles(t.news)
            except Exception:
                news_score, news_label = None, "Yahoo news unavailable"

            opportunity_score, score_notes = score_opportunity(
                returns=returns,
                info=info,
                rel_volume=rel_volume,
                news_score=news_score,
            )

            price_rows.append(
                f"| {ticker} | {currency} | {latest_price:.2f} "
                f"| {fmt_pct(returns['1d'])} | {fmt_pct(returns['1w'])} "
                f"| {fmt_pct(returns['1m'])} | {fmt_pct(returns['3m'])} "
                f"| {fmt_pct(returns['YTD'])} "
                f"| {fmt_number(low52, 2)} | {fmt_number(high52, 2)} "
                f"| {fmt_number(pe, 1)} | {fmt_large_number(mcap)} |"
            )
            if ticker not in CONTEXT_ONLY_TICKERS:
                score_rows.append(
                    f"| {ticker} | {opportunity_score} | {fmt_pct(returns['1m'])} "
                    f"| {fmt_pct(returns['3m'])} | {fmt_large_number(revenue)} "
                    f"| {fmt_pct(revenue_growth * 100 if revenue_growth is not None else None)} "
                    f"| {fmt_pct(profit_margin * 100 if profit_margin is not None else None)} "
                    f"| {fmt_number(debt_to_equity)} | {fmt_number(rel_volume, 2)} "
                    f"| {fmt_number(recommendation, 2)} | {fmt_pct(target_upside)} "
                    f"| {news_label} | {score_notes} |"
                )
        except Exception as e:
            print(f"  WARN: {ticker}: {e}")
            missing.append(ticker)

    price_table = "\n".join([price_header, price_sep] + price_rows) + "\n"
    score_table = "\n".join([score_header, score_sep] + score_rows) + "\n"
    return price_table, score_table, missing


# ---------------------------------------------------------------------------
# FRED
# ---------------------------------------------------------------------------

def fetch_fred_series() -> str:
    """Fetch latest values from FRED public CSV endpoint (no API key)."""
    header = "| Series | Name | Value | Date |"
    sep = "|--------|------|-------|------|"
    rows: list[str] = []

    end = datetime.now(ZoneInfo("UTC")).strftime("%Y-%m-%d")
    start = (datetime.now(ZoneInfo("UTC")) - timedelta(days=30)).strftime("%Y-%m-%d")

    for series_id, name in FRED_SERIES.items():
        try:
            url = (
                f"https://fred.stlouisfed.org/graph/fredgraph.csv"
                f"?id={series_id}&cosd={start}&coed={end}"
            )
            req = urllib.request.Request(url, headers={"User-Agent": "trading-agent/1.0"})
            with urllib.request.urlopen(req, timeout=8) as resp:
                text = resp.read().decode("utf-8")

            reader = csv.reader(io.StringIO(text))
            next(reader)
            last_date, last_val = None, None
            for row in reader:
                if len(row) >= 2 and row[1].strip() != ".":
                    last_date, last_val = row[0], row[1]

            if last_val:
                rows.append(f"| {series_id} | {name} | {last_val} | {last_date} |")
            else:
                rows.append(f"| {series_id} | {name} | - | - |")
        except Exception as e:
            print(f"  WARN: FRED {series_id}: {e}")
            rows.append(f"| {series_id} | {name} | ERROR | - |")

    return "\n".join([header, sep] + rows) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    berlin = ZoneInfo("Europe/Berlin")
    now_berlin = datetime.now(berlin).strftime("%Y-%m-%d %H:%M %Z")
    now_utc = datetime.now(ZoneInfo("UTC")).strftime("%Y-%m-%d %H:%M UTC")

    tickers = parse_tickers(MEMORY / "watchlist.md")
    print(f"Fetching {len(tickers)} tickers from watchlist.md ...")

    watchlist_table, opportunity_table, missing = fetch_watchlist_data(tickers)
    macro_table = fetch_fred_series()

    sections = [
        "# Market Snapshot",
        "",
        f"Generated: {now_berlin} ({now_utc})",
        "",
        "> **Agent note:** treat all prices and macro values below as authoritative.",
        "> Do not re-fetch or estimate. If a value is missing, say so.",
        "",
        f"## Watchlist ({len(tickers) - len(missing)}/{len(tickers)} tickers)",
        "",
        watchlist_table,
        "",
        "## Opportunity Scores",
        "",
        "> Score is a 0-100 research triage signal, not a buy/sell instruction.",
        "> It blends short-term momentum, fundamentals, analyst tone, liquidity, and recent headline tone.",
        "",
        opportunity_table,
        "",
        "## Macro Indicators (FRED)",
        "",
        macro_table,
    ]

    if missing:
        sections += [
            "",
            "## Missing",
            "",
            "The following tickers returned no data and were skipped:",
            "",
        ]
        for ticker in missing:
            sections.append(f"- `{ticker}`")
        sections.append("")

    snapshot = "\n".join(sections)
    out = MEMORY / "market_snapshot.md"
    out.write_text(snapshot, encoding="utf-8")
    print(f"Wrote {out} - {len(tickers) - len(missing)} tickers, {len(FRED_SERIES)} FRED series")
    if missing:
        print(f"  Missing: {', '.join(missing)}")


if __name__ == "__main__":
    main()
