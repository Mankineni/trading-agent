# Weekly Research — 2026-04-21

## TL;DR

The tape is risk-on — VIX compressed to 18.8, broad equities pressing 52-week highs — but nothing on the watchlist clears all risk gates. The SPYI.DE cost-basis entry in portfolio.md is a data anomaly that needs human clarification before any action on that position. No new buys or sells this week.

## Macro Backdrop

- **US 10Y:** 4.27% (^TNX via Yahoo; FRED data returned ERROR across all series again this week)
- **EUR/USD:** 1.1800 — near a 12-month high; dollar weakness continues
- **VIX:** 18.81 — down 29.8% over the past month; the fear spike from earlier this quarter has fully unwound
- **Gold:** $4,801.50 (GC=F) — YTD +11.3%; gold and equities rising together signals residual hedging demand despite the risk-on surface
- **VWCE.DE:** €153.54 — 0.1% below its 52-week high of €153.70; broad equities at the top of the range
- **Regime read:** Risk-on. Vol compressing, equities recovering. The concurrent gold bid is a caution flag — this is not a clean "all-clear" environment.

## Actions

No buys. No sells.

### HOLD positions

- **IWDA.AS — iShares Core MSCI World Acc:** HOLD — Sparplan auto-invests €150/month into this ticker; no manual add is permitted by Rule 4. Price €116.82 (+2.3% 1w, +4.9% YTD) vs avg cost €116.25. Thesis intact.
- **SPYI.DE — SPDR MSCI ACWI IMI Acc:** HOLD — The fund has recovered +6.7% over the past month to €10.59. However, the avg cost in portfolio.md is recorded as €98.01, which conflicts with the fund's entire 52-week range of €9.01–€12.24. This data anomaly must be resolved before any add or sell decision. See Open Questions.
- **BBAI — BigBear.ai Holdings:** Ring-fenced; no recommendation. Moved +14.6% this week to $3.84 (≈ €3.25 at EUR/USD 1.1800), putting it +15.0% above avg cost of $3.34 in USD terms. A 14.6% weekly move in one stock vs. the ETFs' +2.3% is a clean illustration of single-stock vol — useful data point at this stage of learning.

## Retro on Last Week

**Grade: B** — "No picks" was the right call. The prior run cited an incomplete portfolio file as the primary blocker. Now with real holdings and real cash loaded, the no-pick conclusion holds on its own merits: IWDA.AS is Sparplan-blocked, SPYI.DE has a cost-basis anomaly, VWCE.DE duplicates existing exposure (Gate 4), and AGGH.DE data is unavailable. Right answer, incomplete reasoning.

## What I'd Change If I Ran It Back

1. The SPYI.DE cost-basis conflict (€98.01 avg vs €10.59 current price) was visible in portfolio.md from the first run and should have been flagged immediately rather than deferred.
2. BBAI's >10% weekly move threshold for ring-fenced positions should have been explicitly modelled from the first run so the habit of tracking it is built earlier.

## Open Questions

1. **SPYI.DE cost basis anomaly:** Avg cost recorded is €98.01 per share, but the fund's 52-week range is €9.01–€12.24. A cost basis ~9× the current price cannot be correct unless the fund underwent a reverse split or major restructuring. Clarify the actual avg cost before any SPYI.DE trade is evaluated — position sizing, P&L, and the sell case all depend on this number.
2. **AGGH.DE data missing:** Bond ETF price data was unavailable again this week. If you are considering bonds for portfolio ballast, check the price manually on Scalable Capital — the agent cannot evaluate AGGH.DE without a price.
3. **FRED data outage:** All FRED macro series returned ERROR for the second consecutive week. The Yahoo prices cover the essentials, but the data-fetch pipeline appears broken. Worth investigating before the next run.
4. **BBAI ring-fence review timing:** BBAI is +15% above avg cost in USD but -34.2% YTD — it bounced hard this week but remains well below its year-open level. Consider setting a personal price threshold (e.g., "I will decide when it hits $X") so the exit decision is made deliberately, not reactively.
