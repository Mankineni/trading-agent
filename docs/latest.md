# Weekly Research - 2026-04-27

## TL;DR

The SPYI.DE issue was a ticker mapping error, not a transaction problem: ISIN IE00B6R52259 maps to IUSQ.DE, now priced at EUR 98.46 versus EUR 93.89 average cost. No immediate trade is forced by this fix; the portfolio now shows IWDA.AS and IUSQ.DE both modestly positive, while BBAI remains ring-fenced and negative. Tactical scores highlight MSFT, NVDA, and GOOGL as names to watch, but any tactical buy still needs sizing inside the 20% risk sleeve and a clear exit plan.

## Macro Backdrop

- US 10Y proxy (^TNX): 4.31, up +1.5% over 1w.
- EUR/USD: 1.18, up +0.1% over 1w.
- VIX: 18.97, up +0.5% over 1w and still below the 20 caution threshold.
- Gold (GC=F): $4,720.60, down -1.8% over 1w but up +9.4% YTD.
- FRED values timed out in this local run, so Yahoo macro tickers are the usable macro source this week.
- Market regime: mixed-to-risk-on for equities; core can stay invested, tactical sleeve should avoid chasing extended one-week moves.

## Opportunity Screen

The score is a research triage signal, not a buy instruction. It helps decide what deserves deeper work.

| Ticker | Score | Signal read | Action |
|--------|------:|-------------|--------|
| MSFT | 89 | Strong 1m momentum, revenue growth, high margin, constructive analysts, positive headline tone | WATCH |
| NVDA | 87 | Strong growth and margin, positive 3m trend, but already close to 52w high | WATCH |
| GOOGL | 82 | Positive 1m/3m trend, profitable, revenue growing, neutral headline tone | WATCH |
| IUSQ.DE | 72 | Held core ETF, price now matches the transaction scale after ticker fix | HOLD |
| VWCE.DE | 72 | Core ETF still attractive structurally, but duplicates existing global equity exposure | SKIP |

## Actions

### HOLD positions

- **IWDA.AS - iShares Core MSCI World (Acc):** HOLD - current EUR 116.78 versus EUR 111.38 average cost; Sparplan already handles regular buying.
- **IUSQ.DE - iShares MSCI ACWI (Acc):** HOLD - current EUR 98.46 versus EUR 93.89 average cost; prior SPYI.DE anomaly is fixed by correcting the ticker mapping.
- **BBAI - BigBear.ai Holdings:** HOLD (ring-fenced) - current $3.70, negative versus EUR cost basis; agent still does not buy or sell this position.

## Portfolio Plan

Current priced portfolio is about EUR 1,170.97 including cash. Active core ETFs are roughly EUR 610.19, BBAI is roughly EUR 131.69 and ring-fenced, and cash is EUR 429.08. The 20% tactical sleeve should be treated as a cap, not a target; with BBAI already consuming speculative risk, any new tactical buy should be small and should not be opened without a written exit plan.

## Retro on Last Week

**Grade: B** - "No picks" was still conservative and acceptable, but the SPYI.DE issue should have been identified as a wrong ticker mapping to IUSQ.DE sooner.

## What I'd Change If I Ran It Back

1. Check ISIN-to-ticker mappings before treating a cost-basis mismatch as a broker CSV problem.
2. Keep the opportunity score table separate from recommendations so high-scoring stocks do not become automatic buys.
3. Replace stale or failing tickers quickly, as with AGGH.DE to EUNA.DE.

## Open Questions

- Should BBAI remain ring-fenced, or should you define a personal review price/date for it?
- Do you want the tactical sleeve to allow only mega-cap profitable stocks, or also smaller high-volatility names?
- Should the weekly report include a suggested maximum EUR amount for the tactical sleeve based on current portfolio value?
