# Weekly Research - 2026-04-27

## TL;DR

No new buys this week. The portfolio's risk rules collectively create a structural deadlock at its current size: the 40% ETF cap, the €250 minimum order, and the Sparplan block on IWDA.AS leave no viable core add, and the tactical sleeve maximum (~€52) is permanently below the minimum order threshold. Discipline holds; the open questions section flags the rule tension that needs human attention.

## Macro Backdrop

- **US 10Y (^TNX):** 4.32% — up +1.6% weekly; FRED data still returning ERROR for the third consecutive run.
- **EUR/USD:** 1.18 — near 52-week high of 1.20; strong euro mutes USD-asset returns in EUR terms.
- **VIX:** 19.05 — well off the 52-week high of 35.30; vol compression is consistent with risk-on recovery, but still elevated vs. the 52-week low of 13.38.
- **Gold (GC=F):** $4,716.30 — off the recent peak, -1.9% weekly, +9.3% YTD; still elevated in an absolute sense.
- **Market regime:** Mixed — global equity 1-month momentum is strong (+5–6% for IWDA/IUSQ), but EUR strength, FRED data gaps, and extended single-stock moves introduce meaningful uncertainty.
- **Impact on portfolio:** Core sleeve benefits from the equity recovery but is structurally underweight (59% vs. 80% target). Tactical sleeve is empty. No regime signal is sharp enough to override the gate failures this week.

## Opportunity Screen

MSFT ($424.62 = ~€360/share), GOOGL ($344.40 = ~€292/share), AMD ($347.81 = ~€295/share), and AVGO ($422.76 = ~€358/share) are omitted — each share costs more than 25% of total active portfolio value (€1,038).

| Ticker | Score | Signal read | Action |
|--------|------:|-------------|--------|
| NVDA | 87 | Positive 3m trend (+11%), revenue +73% YTD, 55.6% profit margin, rel. volume 1.49 above average, analyst consensus constructive; extended but not parabolic. $208.27 = ~€176.50/share. | WATCH — single-share cost passes affordability gate, but max tactical position (~€52) is below €250 minimum order. No trade possible until portfolio grows. |
| IUSQ.DE | 62 | +6.2% 1m, +3.9% 3m; near 52-week high (€98.71); constructive momentum but no standalone catalyst beyond steady global equity recovery. | WATCH — adding €250 would push IUSQ.DE to 52.5% of active portfolio, breaching the 40% ETF cap. |
| IWDA.AS | 62 | +5.9% 1m, +0.3% weekly; at 52-week high range (€117.10); Sparplan already buys this monthly. | HOLD — Sparplan-blocked for discretionary buys per portfolio rules. |

## Actions

### HOLD positions

- **IWDA.AS — iShares Core MSCI World (Acc):** HOLD — 2.696 shares at €116.60; cost basis €300.25, current value €314.33 (+4.7%). Sparplan continues monthly. Near 52-week high; no action needed.
- **IUSQ.DE — iShares MSCI ACWI (Acc):** HOLD — 3 shares at €98.31; cost basis €281.67, current value €294.93 (+4.7%). Near 52-week high. A discretionary add would breach the 40% ETF cap at minimum order size.
- **BBAI — BigBear.ai Holdings (ring-fenced):** HOLD — 42 shares at $3.70 (~€3.14 at EUR/USD 1.18); cost basis €164.73, current value ~€131.71 (-20.1% unrealized). Down -3.9% this week, -36.6% YTD. Ring-fenced per portfolio.md — no action recommended; included for observational context only.

## Portfolio Plan

Active portfolio (BBAI excluded from math per portfolio.md):

| Component | Value | % of Active |
|-----------|------:|------------:|
| Core equity (IWDA.AS + IUSQ.DE) | €609.26 | 58.7% |
| Tactical sleeve | €0 | 0.0% |
| Cash | €429.08 | 41.3% |
| **Active total** | **€1,038.34** | **100%** |

Target is 80% core / 20% tactical. Current core is 21 percentage points below target. The gap cannot be closed this week because:

1. IWDA.AS is Sparplan-blocked.
2. Adding €250 to IUSQ.DE pushes it to 52.5% of active portfolio — above the 40% ETF cap.
3. A new all-country ETF (VWCE.DE) duplicates IUSQ.DE; Gate 5 routes back to adding to IUSQ.DE, which breaches the cap.
4. EUNA.DE (bonds, score 46) lacks a compelling thesis and has a negative 3-month trend.
5. Tactical sleeve ceiling (~€52) is permanently below the €250 minimum order at this portfolio size.

The portfolio is mechanically stuck until cash accumulates further or the ETF cap is reviewed. No picks is the only rule-compliant outcome.

## Retro on Last Week

**Grade: B** — No picks on 2026-04-24 was the right call; IWDA.AS and IUSQ.DE each moved +0.3–0.4% in the week that followed, and the gate failures that blocked buys then still hold now. Missing a sub-0.5% weekly move by sitting on hands is not a mistake.

The SPYI.DE cost-basis anomaly flagged over two prior runs has been resolved — the correct ticker for ISIN IE00B6R52259 is IUSQ.DE at €98.31, which looks correct against the €93.89 average cost. That data blocker is cleared.

## What I'd Change If I Ran It Back

- The structural deadlock (ETF cap + minimum order + Sparplan block) was present last week too; it should have been framed as an explicit human decision point sooner, not just noted as an aside.
- FRED data has returned ERROR for three consecutive weeks. Flagging it in learnings is not enough — escalating it as a live data gap that needs a fix is the right move now.

## Open Questions

- **Rule tension:** The 40% ETF cap and the €250 minimum order together prevent adding to the largest core holding (IUSQ.DE would reach 52.5%). As the Sparplan grows IWDA.AS monthly, this deadlock may persist for a long time. Should the ETF cap be raised to 55–60% for the learning phase, or should a second non-duplicate core ETF be added to the watchlist to give the portfolio a legal deployment target?
- **Tactical sleeve math:** At ~€1,038 active portfolio, the maximum tactical position (5% of total or 25% of sleeve, whichever is smaller) is ~€52 — permanently below the €250 minimum order. Tactical buys are structurally impossible until the active portfolio grows to at least €5,000. Is this intentional? If so, the agent should suspend tactical screening until that threshold is met.
- **FRED failure:** Macro FRED data has returned ERROR every week since the agent launched. The Yahoo snapshot is sufficient for a basic regime read, but yield-curve data (2Y vs 10Y spread) and Brent crude are unavailable. Adding BZ=F and a fallback to ^TNX for the 10Y in the snapshot script would restore full macro coverage.
- **BBAI:** At $3.70 (~€131.71), the ring-fenced position is -20.1% below EUR cost basis and -36.6% YTD. No action required per rules, but at what point would you want to revisit the ring-fence and decide whether to hold through the drawdown or cut the loss?
