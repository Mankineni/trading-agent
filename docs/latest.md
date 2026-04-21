# Weekly Research — 2026-04-21

## TL;DR

Broad equities sit at or near 52-week highs with VIX at 18.9 and EUR/USD at 1.18. The portfolio file still holds only a placeholder row and an unspecified cash balance, so no position sizing is possible. No picks this week — fill in `memory/portfolio.md` with real holdings and cash before the next run.

## Macro Backdrop

- US 10Y (^TNX): 4.25% — rates stable, -1.1% on the week
- EUR/USD: 1.1800 — flat w/w, +0.1% YTD; USD weakness muted
- VIX: 18.92 — +3.1% w/w but -29.4% over 1 month; vol regime calming
- Brent: data unavailable (FRED series ERROR)
- VWCE.DE at 153.52 (52w high 153.70); SXR8.DE at 651.68 (52w high 649.90) — global equities printing new highs
- Gold (GC=F) $4,803, +11.3% YTD but flat recent; safe-haven bid present but not accelerating
- Read: risk-on, but extended. No regime change this week.

## Actions

No BUYs or SELLs this week.

Rationale: `memory/portfolio.md` contains a placeholder holding (`EXAMPLE.DE`) and a placeholder cash line (`€X,XXX`). Risk gates 1–3 (position size, concentration, cash reserve) cannot be evaluated without real numbers. Recommending a buy under these conditions would violate the "never invent numbers" constraint. Broad-market ETFs are also printing 52-week highs, which is not the moment to force activity on an undefined base.

### HOLD positions

No holdings to review. Portfolio file contains only a placeholder row flagged for deletion.

## Retro on Last Week

**Grade: N/A** — First run — no prior picks to grade.

## What I'd Change If I Ran It Back

- N/A — first run.

## Open Questions

- When will `memory/portfolio.md` be populated with real cash balance and holdings? All future gate checks depend on this.
- EIMI.DE, IGLT.DE, IUIT.DE returned no data in the snapshot — is the feed broken or are these being dropped from the watchlist?
- FRED macro block is fully ERROR this week. The agent is running blind on Brent and treasury series from that source; is the API key or network path healthy?
- Healthcare split is wide: EXV6.DE (Europe) +20.6% YTD vs XDWH.DE (global) -2.9% YTD. Worth the human deciding whether regional healthcare exposure deserves a dedicated slot once the portfolio is seeded.
