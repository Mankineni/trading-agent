# Weekly Research — 2026-04-24

## TL;DR

VIX spiked mid-week then partially recovered; US 10Y nudged up to 4.31%; all active equity ETFs finished the week roughly flat. No new buys — IWDA.AS is Sparplan-blocked, VWCE.DE duplicates existing global equity exposure, and AGGH.DE has no price data. The SPYI.DE cost-basis anomaly (avg cost €93.89 vs current €10.58) blocks evaluation of that position for a second consecutive week and requires human resolution.

## Macro Backdrop

- US 10Y: 4.31% (Δ +0.06pp from ~4.25% last week — mild upward pressure, no trend break)
- EUR/USD: 1.1700 (Δ -0.01 from 1.18 last week — EUR softened marginally)
- VIX: 18.68 (Δ -0.22 from ~18.9 last week; up 6.9% over the week but -3.3% on Friday — mid-week spike with partial reversal)
- Gold (GC=F): $4,732.60 (-2.6% this week after +9.7% YTD run — short-term pullback in a still-elevated trend)
- Brent Crude: data unavailable (FRED ERROR — second consecutive week; no price in snapshot)
- One-line read: mixed — vol elevated but retreating, rates stable, equity ETFs flat, EUR softening slightly; no regime change

## Actions

### HOLD positions

- **IWDA.AS — iShares Core MSCI World (Acc):** HOLD — Sparplan target at €116.73 (near 52w high of €117.00); 2.695764 shares at avg cost €111.38; unrealized gain ≈+€14.47 (+4.8%); monthly auto-invest already handles capital deployment here.
- **SPYI.DE — iShares MSCI ACWI (Acc):** HOLD — current €10.58; recorded avg cost €93.89 per share is an 89% discrepancy; no add or sell evaluated until transactions.csv is verified. See Open Questions.
- **BBAI — BigBear.ai Holdings:** HOLD (ring-fenced) — $3.70 ≈ €3.16 at EUR/USD 1.17; 42 shares, EUR cost basis €164.73, current EUR value ≈€132.82; down ≈19% from EUR cost basis and -36.7% YTD. Agent takes no action. Human to decide when to review the ring-fence.

## Retro on Last Week

**Grade: A** — "No picks" was the correct call. IWDA.AS finished +0.0% on the week, SPYI.DE -0.1%, VWCE.DE -0.0%. Sitting on hands cost nothing, and every data-quality blocker that drove the no-pick decision is still unresolved, confirming the call was right for the right reasons.

## What I'd Change If I Ran It Back

1. The SPYI.DE cost-basis anomaly has now been flagged in two consecutive runs without resolution. Flagging and waiting is not enough — the Open Questions section needs to ask for a concrete human action, not just note the problem.
2. FRED macro data has failed for two consecutive weeks. Brent crude has no price at all in the snapshot. Accepting a structurally degraded macro section passively is a recurring mistake; the question of a fallback data source should be escalated.

## Open Questions

1. **SPYI.DE cost basis (action required):** avg cost €93.89 per share vs current price €10.58 implies an 89% discrepancy on a fund whose 52-week range is €9.33–€12.24. Check transactions.csv for duplicate rows, wrong currency entries, or a stale lot from a different instrument. The agent cannot evaluate this position — add, sell, or P&L — until the data is clean.
2. **FRED data failure (week 2):** Brent crude, German bund yield, and formal yield-curve data are all ERROR for a second straight week. If the API key is expired or rate-limited, consider adding a Yahoo Finance fallback (e.g., BZ=F for Brent) to the snapshot script.
3. **AGGH.DE no price data (week 2):** bond ETF candidate has returned no data two weeks running. Confirm the ticker is still active and priced on Scalable Capital before the agent can consider it as a buy candidate.
4. **BBAI ring-fence review:** at $3.70 (avg cost $3.922), -36.7% YTD and -19% from EUR cost basis, this position drifts further negative each week it is deferred. Consider setting a personal price threshold so the exit decision is deliberate, not reactive.
