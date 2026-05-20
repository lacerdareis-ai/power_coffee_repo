# Phase 0 Sales Motor — Setup Complete

**Date:** 2025-05-08  
**Status:** ✅ All core automations running

---

## 📦 Contents

- `00-Brand/Brand-Bible.md` — Product specs, brand voice, ICP, competitors, visual direction
- `01-Prompts/Master-Prompts.md` — 8 ready-to-use Claude prompts (ad copy, emails, landing pages, weekly analyst, social content, competitor monitor, Higgsfield brief, landing page writer)
- `02-Campaigns/Meta-Ads-Launch-Playbook.md` — Full campaign structure with 5 ad angles, testing protocol, kill/scale criteria, budget ramp
- `03-Creatives/Higgsfield-Prompt-Library.md` — 12 Higgsfield prompts for product shots, lifestyle images, video ads, UGC
- `04-Analytics/` — Weekly report template (`Week-Template.md`) and `Winning-Patterns.md` logging
- `05-Emails/Email-Sequences.md` — 12 emails across 3 sequences (welcome, abandoned cart, post-purchase)
- `06-SOPs/` — `Weekly-Rhythm.md` (8.5h/week mapped per day) and `HE-OS-Setup.md`

---

## 🚀 What's Configured

### HE-OS
- Installed: v0.11.0 (Nous Portal backend)
- Model: `stepfun/step-3.5-flash`
- Gateway: Running (Telegram: `@thepowercoffee`, WhatsApp, Slack connected)
- Scheduled cron jobs: 5 active

### Cron Jobs (Eastern Time)

| Job | Schedule | Purpose |
|-----|----------|---------|
| `morning-brief` | 7:00 AM daily | Telegram motivational brief + daily focus reminder (Mon=Analyze, Tue=Create, Wed=Launch, Thu=Content, Fri=Optimize) |
| `competitor-monitor` | 10:00 AM daily | Web + Instagram monitoring of mudwtr.com, ryze.com, foursigmatic.com; sends Telegram report |
| `review-scanner` | 9:00 AM every 2 days | Amazon 1–2 star review scraping; suggests ad angles; Telegram |
| `morning-motivation-x` | 8:30 AM daily | Posts inspirational quote to X/Twitter (@boosteddays) |
| `bidnetdaily-scraper` | 1:00 PM daily | Government bid scraper (Barnstable, Dukes, Plymouth counties) |
| `status-updater` | Every 5 minutes | Generates `status.json` for dashboard |

**Note:** The 5 daily X posts were paused; replaced with morning motivation only.

### X/Twitter Automation
- Authenticated via `xurl` (powercoffee app → boosteddays user)
- Script: `/Users/lacerdareis/power_coffee_bot/morning_motivation.py`
- State: `morning_post_state.json` tracks today's post
- Logs: cron job output → can view via `cronjob logs <job_id>`

### Local Dashboard
- File: `Phase0_sales_motor/dashboard.html`
- Features:
  - Shows automation status (next runs, last status)
  - Displays today's morning motivation tweet (content + link)
  - Quick links to all Phase 0 documents
  - Daily metrics entry form (followers, visits, sales, revenue, ad spend, notes)
  - Cron log tail view
  - One-click test triggers
- Usage: Open `dashboard.html` in any browser. Auto-refreshes every 5 min.

### Status Generation
- Script: `/Users/lacerdareis/power_coffee_bot/generate_status.py`
- Output: `power_coffee_bot/status.json` (read by dashboard)
- Cron: `status-updater` runs every 5 minutes

---

## 📊 Quick Start

1. **Open Dashboard**
   - Navigate to: `~/Documents/Claude/ClaudeAI/Phase0_sales_motor/dashboard.html`
   - Or open via Obsidian: `[[dashboard.html]]`

2. **Check Telegram** — you should receive:
   - Morning brief at 7:00 AM
   - Competitor monitor at 10:00 AM
   - Review scanner every 2 days at 9:00 AM

3. **Enter daily metrics** in the dashboard form; they're saved to `localStorage` (could later be exported to Google Sheets)

4. **Manual content creation**: Use the Master Prompts (`01-Prompts/Master-Prompts.md`) with Hermes or Claude. The dashboard future plan includes buttons to trigger these.

---

## 🛠️ Customization

### Adjust X Morning Quotes
Edit: `/Users/lacerdareis/power_coffee_bot/morning_motivation.py` → `MOTIVATIONAL_QUOTES` list.

### Change Schedules
Use `cronjob` commands:
```bash
cronjob list
cronjob update <job_id> --schedule "NEW SCHEDULE"
```

### Add New Automations
Create a script + cron job. Follow the pattern: script writes output to a log file or Telegram message.

---

## 🔐 Security Notes

- Amazon SP-API not configured (awaiting production approval). Competitor reviews are scraped via web.
- No credentials stored in plain text; xurl uses `~/.xurl` (OAuth tokens)
- Telegram bot token stored in Hermes config (not in repo)

---

## 📈 Next Steps (Phase 0 Execution)

1. **Daily (5–10 min)**
   - Review morning brief (Telegram)
   - Check dashboard metrics
   - Enter yesterday's metrics if not auto-tracked

2. **Weekly (1–2 hours, per SOP)**
   - Monday: ANALYZE — review Weekly Report template, Winning Patterns log
   - Tuesday: CREATE — use Master Prompts to generate ad copy, emails, landing pages
   - Wednesday: LAUNCH — deploy new campaigns (Meta Ads) per Playbook
   - Thursday: CONTENT — schedule social posts, generate creatives with Higgsfield prompts
   - Friday: OPTIMIZE — review metrics, adjust ads, double down on winners, kill losers

3. **Monthly**
   - Expand competitor list if needed
   - Update Brand Bible with refined positioning
   - Review Hermes skills; teach automation skills (Ad Angle Generator, Weekly Data Formatter, Content Idea Scanner)

---

## 📞 Support

- Hermes docs: Run `hermes doctor`, `hermes status`
- Cron management: `cronjob list`, `cronjob logs <id>`
- X posting logs: `tail -f ~/power_coffee_bot/morning_motivation.log` (if configured)

---

*This note auto-generated on setup completion. Update as you iterate.*
