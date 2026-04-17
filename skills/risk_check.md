# Risk Check — 10 Hard Gates

Every pick must pass all 10 gates or be dropped silently from the output.
Do not list failed candidates. Do not explain why they failed.

Read position limits and rules from `memory/portfolio.md` each run.
Do not hardcode values here — portfolio.md is the single source of truth.

---

## Gate 1 — Position Size

- Non-ETF single position > 15% of portfolio → **fail**
- ETF single position > 60% of portfolio → **fail**
- Order size < €250 → **warn** in the pick: "Below €250 gettex threshold — broker fee applies"
  (do not auto-upsize; flag and let the human decide)

## Gate 2 — Concentration

- Total equity allocation > 90% of portfolio → **fail** the new equity buy
- Single sector > 40% of portfolio → **warn** in the pick
- Check against both current holdings and the proposed addition combined

## Gate 3 — Cash Reserve

- If the buy would leave cash below the minimum reserve in portfolio.md (default €500) → **fail**
- Calculate using: current cash − proposed buy size ≥ min reserve

## Gate 4 — Duplicate Exposure

- If the same underlying index is already held through another instrument,
  recommend adding to the existing position rather than buying a new ticker.
- Example: already hold SXR8.DE (S&P 500) → do not also buy VOO. Add to SXR8.DE.

## Gate 5 — FX Sanity

- If a UCITS-listed version exists with TER within 0.30% of the US-listed version,
  prefer the UCITS version (tax efficiency, EUR settlement, no W-8BEN).
- Note the TER difference in the pick if you choose UCITS over a cheaper US-listed alternative.

## Gate 6 — Freshness

- Ticker sold in the last 4 weeks (check trade_log.md) → must include explicit
  justification for re-entry. What changed since the sell?
- Ticker bought in the last 2 weeks without a subsequent > 5% move → **fail**.
  Avoid churning the same name. Let positions develop.

## Gate 7 — No-Fly List

- Check the no-fly list in portfolio.md.
- If the ticker appears on the list → **fail**. No exceptions, no justifications.

## Gate 8 — Asset Class

- Options → **fail**
- Leveraged products (2x, 3x, inverse) → **fail**
- CFDs → **fail**
- Crypto spot / direct crypto holdings → **fail**
- Crypto ETPs → allowed, but total crypto ETP allocation must stay ≤ 5% of portfolio

## Gate 9 — Tax Awareness

- Prefer accumulating (Acc) share classes over distributing — avoids annual
  Vorabpauschale complexity and reinvestment friction.
- Flag Teilfreistellung category on every pick:
  (TFS: equity 30%), (TFS: mixed 15%), (TFS: none)
- Prefer Irish (IE) domicile over Luxembourg (LU) for funds holding US equities
  (15% vs 30% US withholding tax under the IE-US treaty).
- If a tax edge case arises, note: "Check with your Steuerberater."

## Gate 10 — Reason Good Enough

- The thesis must have exactly 3 concrete bullets without hedging.
  "Looks interesting" or "might go up" is not a bullet. Cite data.
- The "Why I could be wrong" section must have 2 credible scenarios.
  "Black swan event" is not credible — it's a cop-out.
- If you cannot fill both sections convincingly → **fail**. Move the ticker
  to "Open Questions" in the report instead.

---

## Processing rule

Run all 10 gates on every candidate before writing the output.
Failed candidates are dropped silently. The reader sees only picks that passed.
Do not mention the gates, the failures, or the filtering process in docs/latest.md.
