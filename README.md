# Trading Research Agent

A weekly trading research agent that runs on GitHub Actions, analyses your
watchlist and portfolio, scores short-term opportunities, and publishes a
dashboard to GitHub Pages.

**It does not execute trades.** It produces a weekly report with core and
tactical recommendations. You read the report, decide, and place orders
manually on Scalable Capital (or wherever you trade).

## How it works

Every Friday at 19:00 UTC (20:00 CET / 21:00 CEST):

1. A Python script fetches fresh price data (yfinance) and macro indicators (FRED).
2. Claude reads your portfolio, watchlist, prior picks, market data, opportunity scores, and risk rules.
3. Claude grades last week's recommendations against current prices.
4. Claude writes a new research report with buy/sell/hold verdicts.
5. A render script converts the report to a static HTML dashboard.
6. Everything is committed to `main` and published via GitHub Pages.

You maintain two files (`portfolio.md` and `watchlist.md`). The agent
maintains the rest. Zero picks is a valid and common output.

## Dashboard layout

`docs/index.html` is a single self-contained page (no external JS/CSS,
dark-mode aware) split into eight scannable sections:

1. **Decision banner** — large colour-coded verdict for the week (BUY / SELL /
   HOLD) pulled from the latest `trade_log.md` entry.
2. **Macro backdrop** — regime pill (risk-on / neutral / caution / risk-off)
   plus four KPI tiles: VIX, US 10Y, EUR/USD, Gold. Each tile shows the
   latest value and the 1-week change.
3. **Allocation** — hand-rolled SVG donut of current EUR value per position,
   with cash as its own slice and a legend listing % and EUR per position.
   USD holdings are converted at the snapshot's EUR/USD rate.
4. **Holdings table** — position, quantity, avg cost, current price, EUR
   value, a centred P&L bar (green right / red left, globally scaled), the
   week's move, and a `ring-fenced` badge where applicable.
5. **Opportunity scores** — ranked short-term triage table blending momentum,
   fundamentals, analyst tone, liquidity, and recent headline tone.
6. **Watchlist candidates** — one card per candidate with price, 1w, YTD,
   UCITS badge, TER, and a dot on the 52-week range.
7. **Decision timeline** — the last 12 weeks as horizontal dots, coloured
   green (BUY) / red (SELL) / grey (HOLD), with the date and picks on hover.
8. **Flags & open issues** — auto-generated from the data: FRED fetch
   errors, stale snapshot, held positions missing from the snapshot,
   cost-basis outside 52w range, low cash, and >10% weekly moves on
   ring-fenced positions.
9. **Full prose report** — the week's `latest.md` rendered as HTML inside a
   collapsed `<details>` block for when you want the agent's full reasoning.

Graceful placeholders kick in when data is missing (FRED errors, stale or
empty snapshot, tickers yfinance couldn't fetch) — the page still renders.

## Setup (8 steps)

1. **Create a private GitHub repo** and push this code to `main`.

2. **Get an Anthropic API key** from [console.anthropic.com](https://console.anthropic.com).

3. **Add the secret** — go to repo Settings → Secrets and variables → Actions →
   New repository secret → name: `ANTHROPIC_API_KEY`, value: your key.

4. **Enable GitHub Pages** — go to repo Settings → Pages → Source: "Deploy from
   a branch" → Branch: `main`, folder: `/docs` → Save.

5. **Edit `memory/portfolio.md`** — fill in your actual holdings, cash balance,
   and adjust the risk rules to match your situation.

6. **Edit `memory/watchlist.md`** — add or remove tickers. The starter list
   has common UCITS ETFs and a few US names. Make it yours.

7. **Trigger the first run** — go to Actions → "Weekly Review" → Run workflow.
   Watch the logs. The first run takes 2-3 minutes.

8. **Bookmark the Pages URL** on your phone —
   `https://<username>.github.io/<repo>/`

## File map

| File | Owner | Purpose |
|------|-------|---------|
| `CLAUDE.md` | repo | Agent system prompt — identity, workflow, constraints |
| `memory/portfolio.md` | you | Holdings, cash, risk rules, goals |
| `memory/watchlist.md` | you | Tickers to consider + macro indicators |
| `memory/trade_log.md` | agent | Appended record of weekly picks |
| `memory/learnings.md` | agent | Appended reflections across runs |
| `memory/market_snapshot.md` | script | Fresh price + macro data (overwritten each run) |
| `skills/research.md` | repo | Output template the agent must follow |
| `skills/risk_check.md` | repo | 12 hard gates every pick must pass |
| `scripts/fetch_market_data.py` | repo | Fetches yfinance + FRED data, fundamentals, analyst metadata, and headline tone |
| `scripts/render_dashboard.py` | repo | Renders latest.md → index.html |
| `docs/latest.md` | agent | Most recent weekly report (markdown) |
| `docs/index.html` | script | Rendered dashboard for GitHub Pages |
| `docs/style.css` | repo | Dashboard styles (unused — CSS is inlined in index.html) |
| `.github/workflows/weekly-review.yml` | repo | Cron schedule + CI pipeline |

## Cost estimate

| Service | Cost |
|---------|------|
| GitHub Actions | Free (runs ~3 min/week, well within free-tier limits) |
| GitHub Pages | Free for public or private repos on Pro/Team plans |
| Anthropic API | ~€1–5/month depending on output length and model |
| yfinance + FRED | Free (public data, no API keys required) |

## What this is NOT

- **Not financial advice.** This is a personal research tool. It has no
  licence, no fiduciary duty, and no accountability. You make every
  trading decision yourself.
- **Not autonomous.** The agent cannot access your broker, place orders,
  or move money. It writes a markdown file. That's it.
- **Not tax-optimized.** It flags Teilfreistellung categories and domicile,
  but it is not a Steuerberater. German tax law is complex and changes.
  Consult a professional for tax decisions.
- **Not a backtested strategy.** There is no historical simulation behind
  these picks. The agent reasons from current data each week.
- **Not real-time.** It runs once per week on Friday evening. It knows
  nothing about intraday moves, earnings surprises, or breaking news
  between runs.
