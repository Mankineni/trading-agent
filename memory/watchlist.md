# Watchlist

Last updated: YYYY-MM-DD

## Yahoo Finance Exchange Suffixes

- `.DE` — XETRA (Germany)
- `.AS` — Euronext Amsterdam
- `.L` — London Stock Exchange
- No suffix — US exchanges (NYSE, NASDAQ)
- `=X` — forex pairs
- `^` prefix — indices (not tradeable, used for macro context)
- `=F` — futures (not tradeable, used for macro context)

---

## Core ETFs

| Ticker | Name | UCITS | Domicile | Sector | Notes |
|--------|------|-------|----------|--------|-------|
| VWCE.DE | Vanguard FTSE All-World (Acc) | yes | IE | Global Equity | Benchmark, broadest single-ETF allocation |
| IWDA.AS | iShares Core MSCI World (Acc) | yes | IE | Developed Markets | DM-only complement to VWCE |
| EIMI.DE | iShares Core MSCI EM IMI (Acc) | yes | IE | Emerging Markets | EM exposure |
| SXR8.DE | iShares Core S&P 500 (Acc) | yes | IE | US Large Cap | US core, IE domicile |
| EXSA.DE | iShares STOXX Europe 600 (Acc) | yes | DE | Europe Equity | Broad European exposure |
| EXXT.DE | iShares NASDAQ-100 (Acc) | yes | DE | US Tech | Tech/growth tilt |
| IS3N.DE | iShares Core MSCI World (Acc) EUR | yes | IE | Developed Markets | EUR-hedged variant |
| IBCI.DE | iShares Euro Inflation-Linked Govt Bond | yes | IE | EUR Bonds | Inflation protection |
| IGLT.DE | iShares Core UK Gilts | yes | IE | GBP Bonds | UK govt bond exposure |

## Thematic Satellites

| Ticker | Name | UCITS | Domicile | Sector | Notes |
|--------|------|-------|----------|--------|-------|
| IUIT.DE | iShares S&P 500 IT Sector (Acc) | yes | IE | US Tech | Concentrated IT bet |
| EXV6.DE | iShares STOXX Europe 600 Health Care | yes | DE | Healthcare | European healthcare |
| XDWH.DE | Xtrackers MSCI World Health Care | yes | IE | Healthcare | Global healthcare |

## US Stocks

| Ticker | Name | UCITS | Domicile | Sector | Notes |
|--------|------|-------|----------|--------|-------|
| VOO | Vanguard S&P 500 ETF | no | US | US Large Cap | US-domiciled, no TFS |
| QQQ | Invesco NASDAQ-100 ETF | no | US | US Tech | US-domiciled, no TFS |

## Macro Indicators

These are not tradeable — used by the agent for context only.

| Ticker | Name | UCITS | Domicile | Sector | Notes |
|--------|------|-------|----------|--------|-------|
| ^VIX | CBOE Volatility Index | — | — | Volatility | Fear gauge |
| ^TNX | US 10Y Treasury Yield | — | — | Rates | Rate environment |
| EURUSD=X | EUR/USD | — | — | FX | Currency risk for US positions |
| DX-Y.NYB | US Dollar Index | — | — | FX | Broad USD strength |
| GC=F | Gold Futures | — | — | Commodities | Safe haven signal |

<!--
UCITS column: yes / no / — (for non-tradeable indicators)
Edit this file manually. The agent reads it but NEVER modifies it.
-->
