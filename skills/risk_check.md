# Risk Check - 12 Hard Gates

Every pick must pass all 12 gates or be dropped silently from the output.
Do not list failed candidates. Do not explain why they failed.

Read position limits and rules from `memory/portfolio.md` each run.
Do not hardcode portfolio values here. `portfolio.md` is the single source of truth.

---

## Gate 1 - Position Size

- Non-ETF single position above the portfolio cap in `portfolio.md` -> fail.
- ETF single position above the portfolio cap in `portfolio.md` -> fail.
- Order size below the configured broker threshold -> warn in the pick.

## Gate 2 - Core vs Tactical Sleeve

- Classify every BUY as `core` or `tactical`.
- Core buys must fit the long-term allocation plan.
- Tactical buys must fit inside the 20% tactical sleeve.
- A new tactical position must not exceed 5% of total portfolio or 25% of the tactical sleeve, whichever is smaller.

## Gate 3 - Concentration

- Total equity allocation above the cap in `portfolio.md` -> fail the new equity buy.
- Single sector above the cap in `portfolio.md` -> warn in the pick.
- Check both current holdings and the proposed addition.

## Gate 4 - Cash Reserve

- If the buy would leave cash below the minimum reserve in `portfolio.md` -> fail.
- Calculate using: current cash - proposed buy size >= min reserve.

## Gate 5 - Duplicate Exposure

- If the same underlying index is already held through another instrument, recommend adding to the existing position rather than buying a new ticker.
- Example: already hold SXR8.DE for S&P 500 exposure -> do not also buy VOO.

## Gate 6 - FX Sanity

- If a UCITS-listed version exists with TER within 0.30% of the US-listed version, prefer the UCITS version for core allocation.
- Tactical single stocks may be USD-listed, but the pick must show the USD price and EUR equivalent using EUR/USD from `market_snapshot.md`.

## Gate 7 - Freshness

- Ticker sold in the last 4 weeks -> must include explicit justification for re-entry.
- Ticker bought in the last 2 weeks without a subsequent >5% move -> fail.
- Avoid churning the same name.

## Gate 8 - No-Fly List

- Check the no-fly list in `portfolio.md`.
- If the ticker appears on the list or clearly violates it -> fail.

## Gate 9 - Asset Class

- Options -> fail.
- Leveraged products -> fail.
- Inverse products -> fail.
- CFDs -> fail.
- Crypto spot or crypto ETPs -> fail while `portfolio.md` says they are disallowed.
- Plain cash equities and plain UCITS funds are allowed if the other gates pass.

## Gate 10 - Tax Awareness

- Prefer accumulating UCITS funds over distributing funds for core holdings.
- Flag Teilfreistellung category on every fund pick: equity 30%, mixed 15%, or none.
- Prefer Irish domicile for funds holding US equities when comparable choices exist.
- If a tax edge case arises, note: "Check with your Steuerberater."

## Gate 11 - Tactical Evidence

Tactical BUYs need at least three of these five:

- Opportunity Score >= 65 in `market_snapshot.md`.
- Positive 1m or 3m trend.
- Revenue growth or profit margin is positive.
- News tone is positive or neutral.
- Relative volume is above 1.0 or analyst mean is constructive.

If fewer than three are present -> fail.

## Gate 12 - Reason and Exit Plan Good Enough

- The thesis must have exactly 3 concrete bullets without hedging.
- "Looks interesting" or "might go up" is not a bullet. Cite data.
- The "Why I could be wrong" section must have 2 credible scenarios.
- Every tactical pick must include:
  - profit-taking zone,
  - invalidation trigger,
  - maximum acceptable loss,
  - review date or maximum holding window.
- If you cannot fill these convincingly -> fail.

---

## Processing Rule

Run all 12 gates on every candidate before writing the output.
Failed candidates are dropped silently. The reader sees only picks that passed.
Do not mention the gates, failures, or filtering process in `docs/latest.md`.
