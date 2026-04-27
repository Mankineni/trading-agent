# Learnings

Agent-appended reflections and observations across runs.

## 2025-04-17

- Starting fresh — no prior signal history, no track record to grade yet
- German investor context: UCITS-preferred, EUR/USD exposure matters, IE domicile for US equity funds
- Manual execution via Scalable Capital PRIME+; orders must be ≥€250 for free gettex execution

<!-- The agent appends to this file after each run. Do not edit manually. -->

## 2026-04-21

- Portfolio file is still seeded with placeholder values; the agent cannot size positions or check cash-reserve gates until real holdings and a real cash balance land in `memory/portfolio.md`. Treating this as a hard blocker rather than estimating around it.
- FRED macro block returned ERROR across every series this week — the Yahoo snapshot alone still gave enough to read the regime (^TNX 4.25%, VIX 18.9, EUR/USD 1.18), but a second consecutive FRED failure would materially degrade the macro read. Worth flagging to the human before it becomes chronic.
- Broad equities (VWCE.DE, SXR8.DE) pressing 52-week highs at the same moment vol is compressing; historically a risk-on tape but also where forced activity tends to age badly. The "do nothing when in doubt" default is the right one this week regardless of the portfolio-state issue.

## 2026-04-21

- With real portfolio data loaded, the no-pick conclusion still holds on its own merits: IWDA.AS is Sparplan-blocked, SPYI.DE has an unresolved cost-basis anomaly (€98.01 avg vs €10.59 current price), VWCE.DE duplicates existing global equity exposure, and AGGH.DE data is unavailable. No single gate failed alone — the whole watchlist cleared out.
- BBAI moved +14.6% in one week while IWDA.AS and SPYI.DE moved +2.3% — the contrast is sharp and instructive. Single-stock vol is not a feature; it is the point. Tracking this divergence each week builds intuition faster than any abstract lesson.
- Cost-basis data quality matters as much as price data. An incorrect avg cost in portfolio.md makes it impossible to evaluate position P&L, decide on adds, or set sell targets. Data hygiene in the portfolio file is a prerequisite for the agent to function correctly.

## 2026-04-24

- The SPYI.DE cost-basis anomaly (avg €93.89 vs current €10.58) has now persisted across two consecutive runs. The right lesson: a data-quality blocker that recurs without human action is not a passive note — it is a hard blocker that should be escalated explicitly each week until resolved.
- FRED macro data has failed for two consecutive weeks; Brent crude has no price at all. The Yahoo snapshot alone is functional for a regime read but leaves macro coverage structurally incomplete. A fallback ticker (e.g., BZ=F for Brent) in the snapshot script would close the gap.
- BBAI reversed its prior-week +14.6% gain, falling -4.0% this week to $3.70 (≈€3.16), now -36.7% YTD and -19% from EUR cost basis. The round-trip illustrates that single-stock bounces in a downtrend are noise, not trend changes — a useful data point for the learning phase.

## 2026-04-27

- The portfolio rules create a structural deadlock at ~€1,038 active: the 40% ETF cap blocks adding to IUSQ.DE at minimum order size (€250 would push it to 52.5%), IWDA.AS is Sparplan-blocked, and the tactical sleeve ceiling (~€52) is permanently below the €250 minimum order. No picks is the only rule-compliant outcome. This is not a data problem — it is a rules-calibration problem the human needs to resolve.
- FRED macro data has now failed for at least three consecutive weeks. Passive noting in learnings is insufficient; this is a live infrastructure gap that needs an active fix (e.g. adding BZ=F for Brent and verifying the FRED API key). Until it is fixed, the macro section of every report is structurally incomplete.
- BBAI at $3.70 (~€131.71) is -20.1% below EUR cost basis and -36.6% YTD. The ring-fence holds, but the position now represents 11.3% of total portfolio value (including BBAI). The human should consciously decide when and whether to review the ring-fence status — deferring indefinitely is a choice, not a neutral default.
