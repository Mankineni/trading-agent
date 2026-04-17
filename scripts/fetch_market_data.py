#!/usr/bin/env python3
"""Fetch market data from yfinance and FRED, write memory/market_snapshot.md.

Data sources:
  - yfinance: price history for tickers listed in memory/watchlist.md
  - FRED public CSV endpoint (no API key): macro indicators

Output: memory/market_snapshot.md (overwritten each run)
"""

import csv
import io
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import yfinance as yf

ROOT = Path(__file__).resolve().parent.parent
MEMORY = ROOT / "memory"

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


# ---------------------------------------------------------------------------
# Ticker parsing
# ---------------------------------------------------------------------------

def parse_tickers(filepath: Path) -> list[str]:
    """Extract tickers from the first column of markdown tables in a file.

    Skips header rows (cell == 'Ticker') and separator rows (all dashes/spaces).
    """
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
# yfinance
# ---------------------------------------------------------------------------

def compute_returns(closes, today: datetime) -> dict[str, str | None]:
    """Compute 1d/1w/1m/3m/YTD returns from a Close series."""
    if closes.empty:
        return {k: None for k in list(RETURN_WINDOWS) + ["YTD"]}

    latest = closes.iloc[-1]
    results: dict[str, str | None] = {}

    for label, days in RETURN_WINDOWS.items():
        if len(closes) > days:
            prev = closes.iloc[-(days + 1)]
            results[label] = f"{((latest / prev) - 1) * 100:+.1f}%"
        else:
            results[label] = None

    # YTD: first trading day of current year
    year_data = closes.loc[closes.index.year == today.year]
    if len(year_data) >= 2:
        results["YTD"] = f"{((latest / year_data.iloc[0]) - 1) * 100:+.1f}%"
    else:
        results["YTD"] = None

    return results


def fetch_watchlist_data(tickers: list[str]) -> tuple[str, list[str]]:
    """Fetch price data for each ticker. Returns (markdown_table, missing_tickers)."""
    if not tickers:
        return "*No tickers in watchlist.*\n", []

    header = (
        "| Ticker | Currency | Close | 1d | 1w | 1m | 3m | YTD "
        "| 52w Low | 52w High | P/E | Mkt Cap |"
    )
    sep = "|--------|----------|-------|-----|-----|------|------|-----" \
          "|---------|----------|-----|---------|"
    rows: list[str] = []
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
            returns = compute_returns(closes, today)

            # Metadata via fast_info (cheaper than .info)
            fi = t.fast_info
            currency = getattr(fi, "currency", "—")
            low52 = getattr(fi, "year_low", None)
            high52 = getattr(fi, "year_high", None)
            mcap = getattr(fi, "market_cap", None)

            # P/E needs .info — only fetch what we need
            info = t.info
            pe = info.get("trailingPE")

            price_str = f"{latest_price:.2f}"
            low52_str = f"{low52:.2f}" if low52 else "—"
            high52_str = f"{high52:.2f}" if high52 else "—"
            pe_str = f"{pe:.1f}" if pe else "—"

            if mcap and mcap >= 1e12:
                mcap_str = f"{mcap / 1e12:.1f}T"
            elif mcap and mcap >= 1e9:
                mcap_str = f"{mcap / 1e9:.1f}B"
            elif mcap and mcap >= 1e6:
                mcap_str = f"{mcap / 1e6:.0f}M"
            else:
                mcap_str = "—"

            r = returns
            rows.append(
                f"| {ticker} | {currency} | {price_str} "
                f"| {r['1d'] or '—'} | {r['1w'] or '—'} | {r['1m'] or '—'} "
                f"| {r['3m'] or '—'} | {r['YTD'] or '—'} "
                f"| {low52_str} | {high52_str} | {pe_str} | {mcap_str} |"
            )
        except Exception as e:
            print(f"  WARN: {ticker}: {e}")
            missing.append(ticker)

    lines = [header, sep] + rows
    return "\n".join(lines) + "\n", missing


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
            next(reader)  # skip header
            last_date, last_val = None, None
            for row in reader:
                if len(row) >= 2 and row[1].strip() != ".":
                    last_date, last_val = row[0], row[1]

            if last_val:
                rows.append(f"| {series_id} | {name} | {last_val} | {last_date} |")
            else:
                rows.append(f"| {series_id} | {name} | — | — |")
        except Exception as e:
            print(f"  WARN: FRED {series_id}: {e}")
            rows.append(f"| {series_id} | {name} | ERROR | — |")

    return "\n".join([header, sep] + rows) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    berlin = ZoneInfo("Europe/Berlin")
    now_berlin = datetime.now(berlin).strftime("%Y-%m-%d %H:%M %Z")
    now_utc = datetime.now(ZoneInfo("UTC")).strftime("%Y-%m-%d %H:%M UTC")

    tickers = parse_tickers(MEMORY / "watchlist.md")
    print(f"Fetching {len(tickers)} tickers from watchlist.md …")

    watchlist_table, missing = fetch_watchlist_data(tickers)
    macro_table = fetch_fred_series()

    sections = [
        f"# Market Snapshot",
        f"",
        f"Generated: {now_berlin} ({now_utc})",
        f"",
        f"> **Agent note:** treat all prices and macro values below as authoritative.",
        f"> Do not re-fetch or estimate — if a value is missing, say so.",
        f"",
        f"## Watchlist ({len(tickers) - len(missing)}/{len(tickers)} tickers)",
        f"",
        watchlist_table,
        f"",
        f"## Macro Indicators (FRED)",
        f"",
        macro_table,
    ]

    if missing:
        sections += [
            f"",
            f"## Missing",
            f"",
            f"The following tickers returned no data and were skipped:",
            f"",
        ]
        for t in missing:
            sections.append(f"- `{t}`")
        sections.append("")

    snapshot = "\n".join(sections)
    out = MEMORY / "market_snapshot.md"
    out.write_text(snapshot, encoding="utf-8")
    print(f"Wrote {out} — {len(tickers) - len(missing)} tickers, {len(FRED_SERIES)} FRED series")
    if missing:
        print(f"  Missing: {', '.join(missing)}")


if __name__ == "__main__":
    main()
