# Watchlist

> **You (the user) edit this file.** These are the tickers the agent actively considers each week.
>
> **Yahoo Finance tickers.** Exchange suffixes: `.DE` = Xetra, `.L` = London, `.AS` = Amsterdam, no suffix = US.
>
> **UCITS column:** `yes` = EU-regulated fund, `no` = not UCITS, `-` = not a fund or not relevant.
>
> **Plan:** core portfolio first, tactical ideas second. Tactical stock ideas must stay inside the 20% risk sleeve from `portfolio.md`.

---

## Already held (agent reviews these every week)

| Ticker  | ISIN         | Name                                  | UCITS | TER   | Notes |
|---------|--------------|---------------------------------------|-------|-------|-------|
| IWDA.AS | IE00B4L5Y983 | iShares Core MSCI World UCITS Acc     | yes   | 0.20% | Developed markets only, around 1,500 stocks |
| IUSQ.DE | IE00B6R52259 | iShares MSCI ACWI UCITS ETF USD Acc   | yes   | 0.20% | Held global all-country equity ETF. Correct ticker for ISIN IE00B6R52259. |
| BBAI    | US08975B1098 | BigBear.ai Holdings                   | no    | -     | Ring-fenced. Agent does not trade. |

## Candidates I'd consider buying

Core ideas are for the 80% long-term sleeve. Tactical stocks are for the 20% risk sleeve only and need a clear catalyst, invalidation level, and sizing discipline.

| Ticker  | ISIN         | Name                                     | UCITS | TER    | Why it's on the list |
|---------|--------------|------------------------------------------|-------|--------|----------------------|
| VWCE.DE | IE00BK5BQT80 | Vanguard FTSE All-World UCITS Acc        | yes   | 0.22%  | Core: classic one-ETF global equity benchmark. |
| EUNA.DE | IE00BDBRDM35 | iShares Core Global Agg Bond UCITS EUR-H | yes   | 0.10%  | Core: bonds to reduce portfolio volatility. |
| 4GLD.DE | DE000A0S9GB0 | Xetra-Gold ETC                           | no    | 0.025% | Defensive diversifier; only if portfolio rules allow. |
| MSFT    | US5949181045 | Microsoft                                | no    | -      | Tactical stock: profitable mega-cap AI/cloud exposure. |
| NVDA    | US67066G1040 | NVIDIA                                   | no    | -      | Tactical stock: AI semiconductor leader; high volatility. |
| GOOGL   | US02079K3059 | Alphabet Class A                         | no    | -      | Tactical stock: profitable digital ads/cloud/AI exposure. |
| AMD     | US0079031078 | Advanced Micro Devices                   | no    | -      | Tactical stock: cyclical AI/CPU/GPU candidate. |
| AVGO    | US11135F1012 | Broadcom                                 | no    | -      | Tactical stock: semiconductor and infrastructure software exposure. |

## Macro indicators - context only, do NOT trade these

These tell the agent about the market environment. The agent reads these to reason about timing but never recommends buying them.

| Ticker   | Name                            | UCITS | Notes |
|----------|---------------------------------|-------|-------|
| ^VIX     | CBOE Volatility Index           | -     | Fear gauge; spikes during selloffs. |
| ^TNX     | US 10-Year Treasury yield x10   | -     | Higher yields pressure stock valuations. |
| EURUSD=X | EUR/USD exchange rate           | -     | Matters for USD-denominated positions. |
| GC=F     | Gold futures USD/oz             | -     | Reference price for Xetra-Gold. |

---

## Watchlist rules

- Keep the list small enough to understand. More tickers are not automatically better.
- Add a ticker only when it has a role: core allocation, defensive diversifier, or tactical stock candidate.
- Tactical stocks must be scored with current data from `market_snapshot.md`; the ticker being famous is not enough.
- Do not add leverage, inverse products, options, crypto, tobacco, weapons, or fossil fuel majors.
- Prefer accumulating UCITS funds for core holdings when a fund version exists.
