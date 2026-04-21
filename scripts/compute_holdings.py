#!/usr/bin/env python3
"""Compute current holdings + cash from memory/transactions.csv.

Reads the Scalable broker CSV export (European number format, semicolon-
delimited), computes weighted-average EUR cost basis per ISIN, sums cash,
and writes memory/holdings.md — the agent's authoritative view of what
you own and how much it cost.

ISIN -> ticker mapping comes from memory/watchlist.md.
Status overrides (e.g. ring-fenced) come from memory/portfolio.md.
"""

import csv
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEMORY = ROOT / "memory"

TRANSACTIONS_CSV = MEMORY / "transactions.csv"
WATCHLIST_MD = MEMORY / "watchlist.md"
PORTFOLIO_MD = MEMORY / "portfolio.md"
HOLDINGS_MD = MEMORY / "holdings.md"

# Treat qty smaller than this as "closed" — avoids floating-point dust rows
CLOSED_QTY_EPSILON = 1e-6


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------

def parse_eu_number(s: str) -> float:
    """European format: '1.234,56' -> 1234.56, '3,706' -> 3.706, '' -> 0.0."""
    if s is None:
        return 0.0
    s = s.strip()
    if not s:
        return 0.0
    s = s.replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return 0.0


def parse_markdown_table(block: str) -> list[dict]:
    lines = [l.strip() for l in block.splitlines() if l.strip().startswith("|")]
    if len(lines) < 2:
        return []

    def cells(line: str) -> list[str]:
        return [c.strip() for c in line.strip().strip("|").split("|")]

    header = cells(lines[0])
    out: list[dict] = []
    for line in lines[1:]:
        c = cells(line)
        if all(set(x).issubset({"-", ":", " "}) for x in c):
            continue
        if len(c) != len(header):
            continue
        out.append(dict(zip(header, c)))
    return out


def parse_all_tables(text: str) -> list[list[dict]]:
    tables: list[list[dict]] = []
    buf: list[str] = []
    for line in text.splitlines():
        if line.strip().startswith("|"):
            buf.append(line)
        else:
            if buf:
                t = parse_markdown_table("\n".join(buf))
                if t:
                    tables.append(t)
                buf = []
    if buf:
        t = parse_markdown_table("\n".join(buf))
        if t:
            tables.append(t)
    return tables


def load_isin_ticker_map(path: Path) -> dict[str, str]:
    """Scan watchlist.md for every {ISIN: ticker} pair in any table."""
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    mapping: dict[str, str] = {}
    for table in parse_all_tables(text):
        for row in table:
            isin = row.get("ISIN", "").strip()
            ticker = row.get("Ticker", "").strip()
            if isin and ticker and re.match(r"^[A-Z]{2}[A-Z0-9]{9}\d$", isin):
                mapping[isin] = ticker
    return mapping


def load_status_overrides(path: Path) -> dict[str, str]:
    """Read `## Position overrides` table from portfolio.md (ISIN -> status)."""
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    after = text.split("## Position overrides", 1)
    if len(after) != 2:
        return {}
    section = re.split(r"^##\s", after[1], maxsplit=1, flags=re.MULTILINE)[0]
    tables = parse_all_tables(section)
    if not tables:
        return {}
    out: dict[str, str] = {}
    for row in tables[0]:
        isin = row.get("ISIN", "").strip()
        status = row.get("Status", "").strip()
        if isin and status:
            out[isin] = status
    return out


def parse_transactions(path: Path) -> list[dict]:
    """Return all executed rows sorted oldest -> newest."""
    rows: list[dict] = []
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter=";", quotechar='"')
        for r in reader:
            rows.append({
                "date": r.get("date", "").strip(),
                "time": r.get("time", "").strip(),
                "status": r.get("status", "").strip(),
                "description": r.get("description", "").strip(),
                "asset_type": r.get("assetType", "").strip(),
                "type": r.get("type", "").strip(),
                "isin": r.get("isin", "").strip(),
                "shares": parse_eu_number(r.get("shares", "")),
                "price": parse_eu_number(r.get("price", "")),
                "amount": parse_eu_number(r.get("amount", "")),
                "fee": parse_eu_number(r.get("fee", "")),
                "tax": parse_eu_number(r.get("tax", "")),
            })
    # Skip anything that isn't a completed transaction
    rows = [r for r in rows if r["status"] == "Executed"]
    rows.sort(key=lambda r: (r["date"], r["time"]))
    return rows


# ---------------------------------------------------------------------------
# Computation
# ---------------------------------------------------------------------------

def compute_holdings(transactions: list[dict]) -> dict[str, dict]:
    """Walk transactions chronologically, maintain per-ISIN qty + EUR cost basis."""
    positions: dict[str, dict] = {}

    for t in transactions:
        if t["asset_type"] != "Security" or not t["isin"]:
            continue
        isin = t["isin"]
        pos = positions.setdefault(isin, {
            "qty": 0.0,
            "cost_eur": 0.0,
            "name": t["description"] or isin,
            "realized_pnl_eur": 0.0,
            "last_tx_date": t["date"],
        })
        if t["description"]:
            pos["name"] = t["description"]
        pos["last_tx_date"] = t["date"]

        ttype = t["type"]
        shares = t["shares"]

        if ttype in ("Buy", "Savings plan"):
            # amount is negative (cash out), add its abs value + fee + tax as cost
            cost_added = abs(t["amount"]) + t["fee"] + t["tax"]
            pos["qty"] += shares
            pos["cost_eur"] += cost_added

        elif ttype == "Sell":
            if pos["qty"] > CLOSED_QTY_EPSILON and shares > 0:
                proceeds = t["amount"] - t["fee"] - t["tax"]  # net cash received
                cost_removed = (min(shares, pos["qty"]) / pos["qty"]) * pos["cost_eur"]
                pos["realized_pnl_eur"] += proceeds - cost_removed
                pos["qty"] -= shares
                pos["cost_eur"] -= cost_removed

        elif ttype == "Security transfer":
            # shares can be positive (transfer in) or negative (transfer out)
            if shares > 0:
                # Inflow — treat like a buy; use amount if present, else shares*price
                cost_added = abs(t["amount"]) if t["amount"] else shares * t["price"]
                pos["qty"] += shares
                pos["cost_eur"] += cost_added
            elif shares < 0:
                # Outflow — treat like a sell without a realized P&L event
                shares_out = abs(shares)
                if pos["qty"] > CLOSED_QTY_EPSILON:
                    cost_removed = (min(shares_out, pos["qty"]) / pos["qty"]) * pos["cost_eur"]
                    pos["qty"] -= shares_out
                    pos["cost_eur"] -= cost_removed

        elif ttype == "Corporate action":
            # Typically a delisting: shares is the adjustment (often negative)
            if shares < 0 and pos["qty"] > CLOSED_QTY_EPSILON:
                shares_lost = min(abs(shares), pos["qty"])
                frac = shares_lost / pos["qty"]
                cost_lost = frac * pos["cost_eur"]
                pos["realized_pnl_eur"] -= cost_lost  # capital loss on delisting
                pos["qty"] -= shares_lost
                pos["cost_eur"] -= cost_lost

        # Distributions/dividends don't affect cost basis — handled in cash total

        # Clamp drift near zero
        if pos["qty"] < CLOSED_QTY_EPSILON:
            pos["qty"] = 0.0
            pos["cost_eur"] = 0.0

    return positions


def compute_cash(transactions: list[dict]) -> float:
    """Cash delta for each row is amount - fee - tax; sum across all executed rows."""
    total = 0.0
    for t in transactions:
        total += t["amount"] - t["fee"] - t["tax"]
    return total


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def render_holdings_md(
    positions: dict[str, dict],
    cash: float,
    isin_map: dict[str, str],
    status_map: dict[str, str],
    generated_at: datetime,
    tx_count: int,
) -> str:
    open_positions = [
        (isin, p) for isin, p in positions.items() if p["qty"] > CLOSED_QTY_EPSILON
    ]
    closed_positions = [
        (isin, p) for isin, p in positions.items() if p["qty"] <= CLOSED_QTY_EPSILON
    ]

    open_positions.sort(key=lambda ip: ip[1]["cost_eur"], reverse=True)

    lines: list[str] = []
    lines.append("# Holdings")
    lines.append("")
    lines.append(f"Generated: {generated_at.strftime('%Y-%m-%d %H:%M')} "
                 f"from `memory/transactions.csv` ({tx_count} executed rows)")
    lines.append("")
    lines.append("> Auto-generated by `scripts/compute_holdings.py`. Do not edit.")
    lines.append("> Re-run the script after updating `memory/transactions.csv`.")
    lines.append("> Source of truth for current qty, avg cost (EUR), and cash balance.")
    lines.append("")

    # Current positions
    lines.append("## Current positions")
    lines.append("")
    if not open_positions:
        lines.append("*No open positions.*")
    else:
        lines.append("| Ticker | ISIN | Name | Quantity | Avg cost EUR | Cost basis EUR | Status |")
        lines.append("|--------|------|------|---------:|-------------:|---------------:|--------|")
        for isin, p in open_positions:
            ticker = isin_map.get(isin, "—")
            status = status_map.get(isin, "active")
            qty_str = f"{p['qty']:.6f}".rstrip("0").rstrip(".")
            avg_cost = p["cost_eur"] / p["qty"] if p["qty"] > 0 else 0.0
            lines.append(
                f"| {ticker} | {isin} | {p['name']} | {qty_str} "
                f"| {avg_cost:.4f} | {p['cost_eur']:.2f} | {status} |"
            )
    lines.append("")

    # Cash
    lines.append("## Cash")
    lines.append("")
    lines.append(f"- **Free cash (computed from transactions):** €{cash:,.2f}")
    lines.append("")

    # Realized P&L (all-time, closed + partially-closed)
    realized_rows = [
        (isin, p) for isin, p in positions.items()
        if abs(p["realized_pnl_eur"]) > 0.01
    ]
    realized_rows.sort(key=lambda ip: ip[1]["realized_pnl_eur"], reverse=True)
    if realized_rows:
        total_realized = sum(p["realized_pnl_eur"] for _, p in realized_rows)
        lines.append("## Realized P&L (all-time)")
        lines.append("")
        lines.append(f"- **Total:** €{total_realized:,.2f}")
        lines.append("")
        lines.append("| Ticker | ISIN | Name | Realized EUR |")
        lines.append("|--------|------|------|-------------:|")
        for isin, p in realized_rows:
            ticker = isin_map.get(isin, "—")
            lines.append(f"| {ticker} | {isin} | {p['name']} | {p['realized_pnl_eur']:,.2f} |")
        lines.append("")

    # Closed positions (informational)
    fully_closed = [ip for ip in closed_positions if ip[1]["qty"] <= CLOSED_QTY_EPSILON]
    if fully_closed:
        lines.append("## Closed positions (no current holding)")
        lines.append("")
        for isin, p in fully_closed:
            ticker = isin_map.get(isin, "—")
            lines.append(f"- {ticker} ({isin}) — {p['name']} — last tx {p['last_tx_date']}")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    if not TRANSACTIONS_CSV.exists():
        print(f"No {TRANSACTIONS_CSV} — skipping holdings computation")
        return

    transactions = parse_transactions(TRANSACTIONS_CSV)
    isin_map = load_isin_ticker_map(WATCHLIST_MD)
    status_map = load_status_overrides(PORTFOLIO_MD)

    positions = compute_holdings(transactions)
    cash = compute_cash(transactions)

    out = render_holdings_md(
        positions=positions,
        cash=cash,
        isin_map=isin_map,
        status_map=status_map,
        generated_at=datetime.now(),
        tx_count=len(transactions),
    )
    HOLDINGS_MD.write_text(out, encoding="utf-8")

    # Console summary
    open_n = sum(1 for p in positions.values() if p["qty"] > CLOSED_QTY_EPSILON)
    print(f"Wrote {HOLDINGS_MD}")
    print(f"  {len(transactions)} executed transactions")
    print(f"  {open_n} open positions, {len(positions) - open_n} closed")
    print(f"  Free cash: €{cash:,.2f}")
    for isin, p in sorted(positions.items(), key=lambda i: i[1]["cost_eur"], reverse=True):
        if p["qty"] <= CLOSED_QTY_EPSILON:
            continue
        avg = p["cost_eur"] / p["qty"] if p["qty"] > 0 else 0
        ticker = isin_map.get(isin, isin)
        print(f"  {ticker}: {p['qty']:.4f} @ €{avg:.4f} avg, cost €{p['cost_eur']:.2f}")


if __name__ == "__main__":
    main()
