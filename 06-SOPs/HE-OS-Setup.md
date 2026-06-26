# HE-OS Setup SOP
**v2.1 · June 2026 · Claude Stack**

---

## To deploy HE-OS for a new brand

Open Claude Code and type:

```
/heos-setup
```

The agent will ask 5 questions about the brand and then build everything automatically:
directory scaffold → brain reference files → .env → git repo → cron jobs → skills → first content generation test.

**Time to first post: ~30 minutes** (mostly waiting on you to paste API credentials).

---

## What gets installed

- Full bot scripts (publisher, generator, analytics, campaign, briefs, alerts)
- 11 cron jobs (4am publish, 5am generate, 6am analytics, 7am brief, 8am report, 10am campaign, weekly LENS, etc.)
- 5 Claude skills: `/brain` `/lens` `/pulse` `/studio` `/ads`
- Brand-specific knowledge base (brand.md, content-system.md, market.md)
- Git content repo (GitHub, nested monthly path)
- Mac wake guard (3:50am daily)

---

## Credentials you'll need before setup

| Credential | Where to get it |
|---|---|
| `ANTHROPIC_API_KEY` | console.anthropic.com |
| `TELEGRAM_BOT_TOKEN` | @BotFather on Telegram → /newbot |
| `INSTAGRAM_ACCESS_TOKEN` | Meta for Developers → Graph API → long-lived token |
| `LINKEDIN_ACCESS_TOKEN` | LinkedIn Developer Portal → OAuth 2.0 |
| `SHOPIFY_ACCESS_TOKEN` | Shopify Admin → Settings → Apps → Develop apps |
| `RESEND_API_KEY` | resend.com → API Keys (add domain DNS records in GoDaddy) |
| `WHATSAPP_ACCESS_TOKEN` | Meta Business → WhatsApp → API Setup |

You don't need all of them upfront. The installer will flag what's missing and the system starts publishing to whatever is configured.

---

## Power Coffee reference

The Power Coffee is the v1 deployment. See:
- `/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/HE-OS.md` — full current-state doc
- `/Users/lacerdareis/power_coffee_bot/sales_motor/` — reference scripts

---

*Last updated: June 4, 2026*
