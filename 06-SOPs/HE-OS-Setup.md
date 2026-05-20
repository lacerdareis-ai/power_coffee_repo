# HE-OS Setup — Power Coffee Phase 0

> HE-OS (High Energy Operational System) runs on your MacBook M2. It's your autonomous assistant that monitors, alerts, and handles repetitive tasks while you focus on strategy.

---

## Installation (5 minutes)

Open Terminal on your MacBook and run:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Then run the setup wizard:

```bash
hermes setup
```

---

## Configuration

### 1. Choose your LLM provider

For Phase 0 budget, use **OpenRouter** with **DeepSeek V4**:
- Sign up at openrouter.ai
- Add $10 credit
- Copy your API key

In HE-OS:
```bash
hermes model
# Select: OpenRouter
# Paste your API key
# Choose: deepseek/deepseek-chat (DeepSeek V4)
```

**Cost:** ~$0.30 per million input tokens. $10 will last 1-2 months of normal use.

For higher quality tasks, you can switch to Claude:
```bash
hermes model
# Select: Anthropic
# Use your Claude API key (separate from Pro subscription)
# Choose: claude-sonnet-4-6
```

### 2. Connect Telegram (recommended)

1. Open Telegram, search for @BotFather
2. Send `/newbot` and follow the prompts
3. Name it "Power Coffee Agent" or similar
4. Copy the bot token

In HE-OS:
```bash
hermes gateway
# Select: Telegram
# Paste your bot token
```

Now HE-OS can send you alerts directly on your phone.

### 3. Start the gateway

```bash
hermes gateway
```

Leave this running (or set it as a startup process).

---

## Daily Automated Tasks

Configure these tasks in HE-OS by chatting with it:

### Morning Brief (7am daily)
Tell HE-OS:
```
Set up a daily cron job at 7am Eastern time. Every morning, send me a Telegram message with:
1. A motivational one-liner for the day
2. Reminder of today's Power Coffee sales motor focus (Monday=Analyze, Tuesday=Create, Wednesday=Launch, Thursday=Content, Friday=Optimize)
3. Any alerts from overnight
```

### Competitor Monitor (daily)
Tell HE-OS:
```
Every day at 10am, check these websites and report any changes:
- mudwtr.com (pricing, new products)
- rfrize.com (pricing, new products)  
- foursigmatic.com (pricing, new products)

Also check their Instagram accounts for any posts with unusually high engagement. Send findings to me on Telegram.
```

### Review Scanner (every 2 days)
Tell HE-OS:
```
Every 2 days, search Amazon for recent 1-star and 2-star reviews on:
- Mud/Wtr
- Ryze mushroom coffee
- Four Sigmatic

Summarize the top complaints. These are potential ad angles for Power Coffee. Send via Telegram.
```

---

## Skills to Teach HE-OS

Over time, HE-OS learns skills. Here are the first ones to teach:

### Skill 1: Ad Angle Generator
After a few weeks of data, tell Hermes:
```
Here are our top-performing ad angles so far: [paste from Winning-Patterns.md]. 
When I ask you to generate new angles, combine elements from these winners with new competitor complaints or trending topics. Save this as a skill.
```

### Skill 2: Weekly Data Formatter
Tell HE-OS:
```
When I paste raw Meta Ads data, format it into this template: [paste Week-Template.md structure]. Save this as a skill so I can just paste data and you format it automatically.
```

### Skill 3: Content Idea Scanner
Tell HE-OS:
```
Every Monday morning, search Reddit for posts in r/coffee, r/nootropics, r/productivity, and r/biohacking that mention functional coffee, coffee alternatives, or energy without crash. Summarize the top 5 most engaged posts and suggest how Power Coffee could address those conversations. Send via Telegram.
```

---

## HE-OS Budget Tracker

| Month | OpenRouter Credit | Usage | Remaining |
|---|---|---|---|
| Month 1 | $10 | | |
| Month 2 | $10 | | |
| Month 3 | $10 | | |

**Expected cost: ~$5-10/month** for the tasks above using DeepSeek V4.

---

## Troubleshooting

**HE-OS not responding?**
```bash
hermes doctor
```

**Switch models on the fly:**
```bash
hermes model
```

**Check what skills HE-OS has learned:**
```bash
hermes tools
```

**Update HE-OS:**
```bash
hermes update
```

---

*Save this in `06-SOPs/HE-OS-Setup.md`. Update as you teach HE-OS new skills.*
