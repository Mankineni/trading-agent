# Research Output Template

Write `docs/latest.md` using exactly this structure.
Do not add sections. Do not skip sections. If a section has nothing, say so in one line.

---

## Required Structure

```markdown
# Weekly Research - YYYY-MM-DD

## TL;DR

Three sentences max. What matters this week, what you recommend, and why.
Explicitly say whether there is a core buy, tactical buy, sell, or no action.

## Macro Backdrop

4-6 bullets. Reference concrete numbers from market_snapshot.md.

- US 10Y: X.XX%
- EUR/USD: X.XXXX
- VIX: XX.X
- Gold: $XX.XX
- Market regime: risk-on / risk-off / mixed / no change
- One-line impact on the 80% core and 20% tactical sleeve

## Opportunity Screen

Summarize the top scored candidates from `market_snapshot.md`.
Do not recommend them automatically. Explain what the score says and what it does not say.

| Ticker | Score | Signal read | Action |
|--------|------:|-------------|--------|
| TICKER | 72 | momentum/fundamental/news read in one line | BUY / WATCH / SKIP |

## Actions

### CORE BUY: TICKER - Name

- **Price:** EUR XX.XX (or $XX.XX ~= EUR XX.XX at EUR/USD X.XXXX)
- **Size:** EUR XXX on gettex
- **Portfolio role:** core
- **TFS:** equity 30% / mixed 15% / none
- **Domicile:** IE / LU / DE / US / -

**Thesis (3 bullets):**
1. What is happening
2. Why it matters for this position
3. What the expected outcome is

**Why I could be wrong (2 scenarios):**
1. Scenario A that would invalidate this thesis
2. Scenario B that would invalidate this thesis

(Omit this section entirely if there is no core buy.)

### TACTICAL BUY: TICKER - Name

- **Price:** EUR XX.XX (or $XX.XX ~= EUR XX.XX at EUR/USD X.XXXX)
- **Size:** EUR XXX; must fit inside the 20% tactical sleeve
- **Portfolio role:** tactical
- **Time window:** days to 12 weeks
- **TFS:** equity 30% / mixed 15% / none
- **Domicile:** IE / LU / DE / US / -

**Thesis (3 bullets):**
1. What is happening now
2. Why the signal can matter over the tactical window
3. What the expected outcome is

**Exit plan:**
- **Profit-taking zone:** price or percentage move
- **Invalidation trigger:** price, trend, earnings, news, or macro condition
- **Maximum acceptable loss:** EUR and percentage
- **Review date:** date or maximum holding window

**Why I could be wrong (2 scenarios):**
1. Scenario A
2. Scenario B

(Omit this section entirely if there is no tactical buy.)

### SELL: TICKER - Name

- **Current price:** EUR XX.XX
- **Size:** full / partial EUR XXX
- **Portfolio role:** core / tactical
- **TFS:** category

**Thesis (3 bullets):**
1. What changed
2. Why holding no longer makes sense
3. What you would rotate into, or "cash"

**Why I could be wrong (2 scenarios):**
1. Scenario A
2. Scenario B

(Repeat for each SELL, max 3. Omit section entirely if zero sells.)

### HOLD positions

For each holding not mentioned above:

- **TICKER - Name:** HOLD - one-line rationale

If portfolio is empty, write: "No holdings to review."

## Portfolio Plan

Show how the recommendation affects the 80% core / 20% tactical split.
If the split cannot be calculated from available data, say what data is missing.

## Retro on Last Week

**Grade: A / B / C / D / F** - one sentence explaining the grade.

Compare last week's picks from trade_log.md against this week's prices.
If this is the first run or no prior picks exist, write:
"First run - no prior picks to grade."

## What I'd Change If I Ran It Back

1-3 bullets. Honest self-assessment of last week's reasoning.
If first run: "N/A - first run."

## Open Questions

2-4 bullets. Things the agent is uncertain about, would investigate further,
or wants the human to weigh in on.
```

---

## Internal Reasoning Checklist

Run this before writing the output. Do not include it in `docs/latest.md`.

1. **Drift check:** does the portfolio still match the goals in portfolio.md?
2. **Core vs tactical:** is this a boring core allocation or a risk-sleeve trade?
3. **Is anything actually new?** If nothing material changed, no picks is correct.
4. **Opportunity score sanity:** high score is only a prompt to investigate, not a trade.
5. **Risk rules checked:** run every pick through all 12 gates in skills/risk_check.md.
6. **Exit plan:** every tactical idea needs a clean exit before it can be recommended.
7. **Real edge vs activity:** if the best reason is "this looks interesting", drop it.
