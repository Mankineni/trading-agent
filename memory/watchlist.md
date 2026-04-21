# Watchlist

> **You (the user) edit this file.** These are the tickers the agent actively considers each week.
>
> **Yahoo Finance tickers.** Exchange suffixes: `.DE` = Xetra, `.L` = London, `.AS` = Amsterdam, no suffix = US. Check any ticker at `https://finance.yahoo.com/quote/TICKER`.
>
> **UCITS column:** `yes` = EU-regulated fund (tax-efficient for Germany), `no` = not UCITS, `—` = not a fund (macro indicators, individual stocks).
>
> **Phase:** Learning phase (first 6 months). Watchlist is deliberately small — I only track things I actually understand or might plausibly buy.

---

## Already held (agent reviews these every week)

These are in my portfolio. The agent re-evaluates them weekly for HOLD/SELL.

| Ticker  | ISIN         | Name                                  | UCITS | TER    | Notes |
|---------|--------------|---------------------------------------|-------|--------|-------|
| IWDA.AS | IE00B4L5Y983 | iShares Core MSCI World UCITS Acc     | yes   | 0.20%  | Developed markets only (~1,500 stocks) |
| SPYI.DE | IE00B6R52259 | SPDR MSCI ACWI IMI UCITS Acc          | yes   | 0.17%  | All global markets incl. EM + small caps (~9,000 stocks) |
| BBAI    | US08975B1098 | BigBear.ai Holdings                   | no    | —      | Ring-fenced — see portfolio.md. Agent does not trade. |

## Candidates I'd consider buying

Short list of things the agent can recommend as BUY. Kept tight on purpose — I'd rather understand 4 funds well than track 20.

| Ticker  | ISIN         | Name                                   | UCITS | TER    | Why it's on the list |
|---------|--------------|----------------------------------------|-------|--------|----------------------|
| VWCE.DE | IE00BK5BQT80 | Vanguard FTSE All-World UCITS Acc      | yes   | 0.22%  | The classic "one ETF for everything" pick. Alternative to SPYI. |
| AGGH.DE | IE00BDBRDM35 | iShares Core Global Agg Bond UCITS EUR-H | yes | 0.10% | Bonds to reduce portfolio volatility — consider adding later. |
| 4GLD.DE | DE000A0S9GB0 | Xetra-Gold ETC                         | no    | 0.025% | German tax-free after 1yr hold. Future option, not during learning phase. |

## Macro indicators — context only, do NOT trade these

These tell the agent about the market environment. The agent reads these to reason about timing but never recommends buying them.

| Ticker     | Name                               | UCITS | Notes |
|------------|------------------------------------|-------|-------|
| ^VIX       | CBOE Volatility Index              | —     | "Fear gauge" — spikes during selloffs. |
| ^TNX       | US 10-Year Treasury yield (×10)    | —     | Higher yields pressure stock valuations. |
| EURUSD=X   | EUR/USD exchange rate              | —     | Matters for USD-denominated positions (BBAI). |
| GC=F       | Gold futures (USD/oz)              | —     | Reference price for Xetra-Gold. |

---

## Why this watchlist is short

A beginner with €500 in capital does not need to track 20 tickers.

- My three current holdings cover most of global equity already (IWDA + SPYI = heavy overlap).
- My Sparplan auto-invests €150/month, so most of my capital deployment decisions are already automated — the weekly agent is for **thinking**, not frantic activity.
- Adding more tickers would just give the agent more ways to suggest buys I don't need.

## When to expand this watchlist

Add a ticker ONLY when I can answer: **"Why specifically this one, and what does it add that I don't already have?"**

Examples of valid reasons:
- "I want exposure to bonds" → add AGGH.DE ✓ (already there, just not purchased yet)
- "I want a gold hedge" → add 4GLD.DE ✓ (already there, future option)
- "I think European small-caps are interesting" → this is a view, not a shopping list. Research first, then maybe add.

Examples of INVALID reasons to add a ticker:
- "I saw it on YouTube"
- "It's going up lately"
- "The agent might like it"
- "Just in case"

## Deliberately NOT in this list

- **Individual stocks** (except ring-fenced BBAI) — rule 5, no single-stock bets for 6 months.
- **Sector/thematic ETFs** (tech, healthcare, clean energy, etc.) — too specific for learning phase. Broad diversification first.
- **Crypto and crypto ETPs** — rule 8, off-limits for 6 months.
- **Leveraged/inverse ETFs** — gambling tools, never for long-term.
- **US-domiciled ETFs (VOO, QQQ, etc.)** — worse tax treatment than UCITS equivalents for a German investor.
- **Distributing ETFs** — accumulating is more tax-efficient for me during wealth-building (rule 9).