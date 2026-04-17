# Research Output Template

Write `docs/latest.md` using exactly this structure.
Do not add sections. Do not skip sections. If a section has nothing, say so in one line.

---

## Required structure

```markdown
# Weekly Research — YYYY-MM-DD

## TL;DR

Three sentences max. What matters this week, what you recommend, and why.

## Macro Backdrop

4-6 bullets. Reference concrete numbers from market_snapshot.md.

- US 10Y: X.XX% (Δ from last week if trade_log.md has a prior run)
- EUR/USD: X.XXXX
- VIX: XX.X
- Brent: $XX.XX
- Any notable regime change or trend continuation
- One-line read: risk-on / risk-off / mixed / no change

## Actions

### BUY: TICKER — Name

- **Price:** €XX.XX (or $XX.XX ≈ €XX.XX at EUR/USD X.XXXX)
- **Size:** €XXX on gettex (must be ≥€250, or flag: "below gettex threshold")
- **Venue:** gettex via Scalable Capital
- **TFS:** (TFS: equity 30%) / (TFS: mixed 15%) / (TFS: none)
- **Domicile:** IE / LU / DE / US / —

**Thesis (3 bullets):**
1. What is happening
2. Why it matters for this position
3. What the expected outcome is

**Why I could be wrong (2 scenarios):**
1. Scenario A that would invalidate this thesis
2. Scenario B that would invalidate this thesis

(Repeat for each BUY, max 3. Omit section entirely if zero buys.)

### SELL: TICKER — Name

- **Current price:** €XX.XX
- **Size:** full / partial €XXX
- **TFS:** category

**Thesis (3 bullets):**
1. What changed
2. Why holding no longer makes sense
3. What you'd rotate into (or "cash")

**Why I could be wrong (2 scenarios):**
1. Scenario A
2. Scenario B

(Repeat for each SELL, max 3. Omit section entirely if zero sells.)

### HOLD positions

For each holding in portfolio.md not mentioned above:

- **TICKER — Name:** HOLD — one-line rationale

(If portfolio is empty, write: "No holdings to review.")

## Retro on Last Week

**Grade: A / B / C / D / F** — one sentence explaining the grade.

Compare last week's picks (from trade_log.md) against this week's prices.
If this is the first run or no prior picks exist, write:
"First run — no prior picks to grade."

## What I'd Change If I Ran It Back

1-3 bullets. Honest self-assessment of last week's reasoning.
What signal did you miss? What weight was wrong?
If first run: "N/A — first run."

## Open Questions

2-4 bullets. Things the agent is uncertain about, would investigate
further, or wants the human to weigh in on.
```

---

## Internal reasoning checklist

Run this before writing the output. Do not include it in `docs/latest.md`.

1. **Drift check:** does the portfolio still match the goals in portfolio.md?
   If it drifts >10% from benchmark allocation, flag it.
2. **Is anything actually new?** If nothing material changed in macro or
   holdings, "no picks this week" is correct. Do not manufacture activity.
3. **Honest confidence:** would you stake your reputation on this pick?
   If the answer is "maybe", drop it.
4. **Risk rules checked:** run every pick through all 10 gates in
   skills/risk_check.md. Failed picks are dropped silently.
5. **Real edge vs manufactured activity:** if the best you can say is
   "this looks interesting", that is not a pick. That is a watchlist note.
