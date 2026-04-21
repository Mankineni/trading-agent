# Portfolio

## Who I am (context for the agent)

- I am **new to investing** and intentionally starting small to learn.
- I am using this agent to **understand reasoning**, not to get rich fast.
- I will execute every trade manually in Scalable Capital on Saturdays.
- I expect to hold positions for **years, not weeks**.
- If the agent recommends something I don't understand, I will NOT act on it — I'll ask for clarification instead.

## Goals

- **Primary benchmark:** VWCE.DE (Vanguard FTSE All-World) — if I can't beat this over 5+ years, I should just hold it and stop picking.
- **Horizon:** 10+ years. I don't need this money back anytime soon.
- **Risk appetite:** I can probably stomach a 20–30% drawdown without panic-selling, but I haven't been tested yet. Respect this — don't push me into aggressive positions until I've seen a real drawdown.
- **Phase:** Learning phase. First 6 months are about building intuition, not maximising return.

## Cash balance (EUR)

- Free cash available for new investments: **€428.72**
- Monthly Sparplan amount: **€150.00**
- Sparplan target: **iShares Core MSCI World (Acc)**
- Total new capital I'm comfortable deploying in the next 3 months: **€500**

## Current holdings

| Ticker  | ISIN         | Name                            | Quantity  | Avg. cost | Currency | Purchased  | Status       |
|---------|--------------|---------------------------------|----------:|----------:|:--------:|------------|--------------|
| BBAI    | US08975B1098 | BigBear.ai Holdings             | 42        |      3.34 | USD      | 2025-03-06 | ring-fenced  |
| IWDA.AS | IE00B4L5Y983 | iShares Core MSCI World Acc     |  2.695764 |    116.25 | EUR      | 2025-03-06 | active       |
| SPYI.DE | IE00B6R52259 | SPDR MSCI ACWI IMI Acc          | 3         |     98.01 | EUR      | 2025-03-06 | active       |

### Important context for the agent about BBAI

BigBear.ai (BBAI) is a speculative single-stock position I bought before defining these rules. It violates rule 5 ("no single-stock bets in first 6 months") and potentially rule 1 (15% single-stock cap) depending on current market value.

**Instruction to the agent:** treat BBAI as **ring-fenced / out of scope**. Don't recommend buying more of it. Don't recommend selling it either — I'll make that decision myself separately. Don't factor it into portfolio diversification math for new buys. Pretend, for the purposes of weekly thesis generation, that it doesn't exist — but DO include it in the retro/grading if it moves significantly, so I can learn from how a single-stock position behaves vs. my ETFs.

If/when I decide to sell or reduce BBAI, I'll edit this file to change its status from `ring-fenced` to `active` or remove it entirely.

## Risk rules (the agent must respect these)

These are tuned for someone just starting out. Tighter than the default template. I'll relax them as I gain experience.

1. **Max position size:** 40% of total portfolio in any single ETF, 15% in any single stock. (Applies to `active` positions only; `ring-fenced` is excluded.)
2. **Max new buys per week:** 1. (Yes, one. I'm learning — I don't need the agent throwing multiple picks at me.)
3. **Min cash reserve:** €50 always stays in cash.
4. **Sparplan is sacred:** the agent must NEVER recommend selling something I'm actively Sparplan-ing, and must NEVER recommend buying the same ticker my Sparplan already buys (that would just double up).
5. **No NEW single-stock positions in my first 6 months.** (Existing ring-fenced positions are grandfathered.)
6. **No-fly list:** no tobacco, no weapons, no fossil fuel majors.
7. **Minimum order size:** **€250+**
8. **No leverage, no options, no single-stock derivatives, no crypto spot, no crypto ETPs** during the first 6 months. Reconsider after.
9. **Prefer accumulating UCITS ETFs** over distributing ones.
10. **Prefer Ireland-domiciled (IE…) UCITS** for US exposure — better tax treatment on US dividends.

### Minimum order size rule — customize based on your Scalable plan

**Pick ONE of these and delete the other:**

- **If Scalable FREE:** "No minimum order size. I pay €0.99 per trade on gettex regardless of size. Size orders based on conviction and thesis, not venue fees."
- **If Scalable PRIME+:** "Prefer €250+ orders on gettex for free execution. Below €250, flag the €0.99 fee but proceed if thesis is strong."

## German-specific notes for the agent

- I am tax-resident in Germany.
- My **Freibetrag** is €1,000/year tax-free capital gains + dividends. This resets every January.
- **Teilfreistellung**: equity funds get 30% tax exemption on gains, mixed funds get 15%, bond funds get 0%. Prefer equity funds for tax efficiency when the investment thesis allows.
- **Xetra-Gold (4GLD.DE)**: physical-gold ETCs are tax-free after 1-year holding in Germany. (Not allowed during learning period, but worth the agent noting as a future option.)
- I trade via **Scalable Capital PRIME+**.

## What "success" looks like for me in year 1

Not "beat the S&P." Success in year 1 is:

1. I can read the agent's weekly thesis and **understand every word of the reasoning**. If I can't, I ask.
2. I've held through at least one 5%+ drawdown without panic-selling.
3. My portfolio is more diversified than "all in one stock."
4. I've built the muscle memory of the Saturday review + manual execution habit.
5. I haven't over-traded — if the agent recommended fewer than ~20 trades across the whole year, that's a feature, not a bug.

**What success is NOT:** beating the index in year 1. One year is statistical noise. Don't let the agent (or me) pretend otherwise.

## Explicit instructions for the agent

- When in doubt, **hold**. "No new buys this week" is always a valid answer.
- If a recommendation would violate any rule above, silently drop it — don't bargain with the rules.
- If you detect me violating my own rules (e.g. trying to over-concentrate), flag it explicitly in the "Open questions" section of the thesis.
- Remember I'm learning. When you recommend something, **explain WHY in plain language a beginner can follow**, not in jargon.
- My Sparplan runs automatically on Scalable. Don't suggest buys that duplicate it.
- Treat any position marked `ring-fenced` as out of scope: don't recommend buying or selling, but include in retro/observations if it moves materially (>10% in a week or >25% in a month).