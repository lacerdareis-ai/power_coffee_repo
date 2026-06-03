# Sales Motor — Session Report
**Date:** May 23, 2026
**Period Covered:** May 11 – May 23, 2026
**Prepared by:** Claude (AI operator)

---

## What Was Done This Session

### 1. Fixed and Retried the May 22 Instagram Carousel

The carousel published at 4am on May 22 failed because the GitHub remote had diverged — another process had pushed to the repo after the last pull, so `git push` was rejected silently. The publisher proceeded without raising an error, and Meta's CDN couldn't fetch the images.

**Fix applied:**
- Ran `git pull --rebase origin main` to sync the remote state
- Confirmed CDN propagation via `curl` loop before re-running
- Re-published the carousel successfully (`post_id=18557953942065795`)

**Root cause note:** This is the same failure pattern as May 12. The `push_jpegs_to_github()` function does not verify whether the push actually succeeded before continuing. It fails silently. This needs a permanent fix — add push exit-code verification to the function.

---

### 2. Built the CTA Stories System

Created a full conversion-focused Instagram Story system from scratch.

**Files created:**
- `/daily_content/cta_stories/figma_cta_stories.js` — Figma Scripter script generating 10 story frames (1080×1920px) with brand colors, bottom CTA bar with `thepowercoffee.com` on every slide
- `/daily_content/cta_stories/README.md` — instructions for export, music setup, and link behavior
- `story1.jpg` through `story10.jpg` — exported from Figma (story9.jpg was a Pillow-generated placeholder for the missing slide)

**Funnel arc:**
| Story | Theme |
|-------|-------|
| 1 | Hook — "Still crashing by 10am?" |
| 2 | Problem — coffee peaks in 45 min |
| 3 | Cost — the 10am fog is not normal |
| 4 | Solution — same ritual, better formula |
| 5 | Ingredients — 11, zero fillers |
| 6 | Math — $1.19 a morning |
| 7 | Comparison — $6 latte vs $1.19 scoop |
| 8 | Proof — day 3 / day 5 experience |
| 9 | Simplicity — scoop, stir, done, win |
| 10 | Final CTA — "Try it today" |

**Publisher integration:**
Added `publish_cta_story()` function to `publisher.py` that:
- Picks 1 random story from `cta_stories/` at 4am daily
- Tries to post with music (via `INSTAGRAM_STORY_MUSIC` env var)
- Retries without music if the Meta container creation fails (music unavailable)
- Respects the `already_ok` deduplication logic
- Supports `--platform=ctastory` filter

**Important limitation:** Instagram Graph API does not support link stickers via the Content Publishing API. The `thepowercoffee.com` URL is baked into the story image design — it is visible text, not a tappable link. This is the only method available through the API.

**First live test:** May 22 — `story7.jpg` ("$6 LATTE: 45 MINUTES. / $1.19 SCOOP: 5 HOURS.") posted successfully (`post_id=18115477948825548`).

---

### 3. Publication Performance Report (May 11–22)

Built a full delivery report covering all platforms for the first 10 days of the Sales Motor.

**Key findings:**

| Platform | Success Rate | Status |
|----------|-------------|--------|
| Email | 100% | ✅ Stable — 359 contacts, 0 failed |
| Instagram | 89% | ✅ Stable (CDN push fix applied) |
| LinkedIn | 86% | ✅ Stable |
| Telegram | 86% | ✅ Stable |
| Shopify Blog | 75% | ✅ Stable |
| X | 71% | ✅ Stable (early auth failures only) |
| WhatsApp | 60% | ⚠️ Session expired — needs re-auth |
| Threads | 0% | ❌ Credentials never added |
| CTA Story | 100% | ✅ New — 1 test passed |

**Content gap:** The May 20 P3 Founder Story (Ironman / "I can't buy back a wasted morning.") was only ever a dry run. It was generated but never published to any platform. This is the highest-trust pillar and it was missed for the entire week of May 18–22.

Report saved to: `04-Analytics/publish-report-may11-may22.md`

---

### 4. Instagram Performance Analysis

Pulled live data from Instagram Graph API. Analyzed 30 posts (API default) and the full Sales Motor period.

**Account state:**
- 942 followers, 313 following, 141 total posts (all time)
- Follower/following ratio: 3.0x

**Format performance (all time, 30 posts sampled):**

| Format | Posts | Avg interactions | Best post |
|--------|-------|-----------------|-----------|
| Reel | 9 | **8.3** | 18 (Mar 5, 2026) |
| Carousel | 16 | **5.1** | 16 (Feb 3, 2026) |
| Image | 5 | **3.0** | 5 (Jan 1, 2026) |

**Sales Motor period (May 11–22):**
- 6 posts published: 5 carousels, 1 Reel
- Reel (May 20): **11 interactions, 1.17% ER, 3.7 ix/day → #4 all-time**
- Carousels: declining week-over-week (0.64% → 0.11%)
- Below industry benchmark for accounts under 10K (benchmark: 3.5–6% ER)

**Critical gap — missing API permission:**
`instagram_manage_insights` is not granted. This means reach, impressions, saves, shares, profile visits, and story metrics are all invisible. Saves especially are likely the most valuable metric for educational carousels — the true engagement may be much higher than like/comment counts suggest.

Analysis saved to: `04-Analytics/instagram-performance-may2026.md`

---

### 5. LENS Analysis — May 18–22 Patterns

Ran a full patterns analysis on the week of May 18–22 and updated all three brain files.

**Patterns extracted and logged:**

| Pattern | Evidence |
|---------|----------|
| Present-tense problem scene | "Two cups in. Still foggy." → #4 all-time, 1.17% ER |
| Price math comparison | "$0.73 a morning. Real focus. No crash." → disarms price objection |
| Pain-first ingredient reveal | Lead with blood sugar problem → ingredient as solution in slide 2 |
| Nuclear/survival hook | "The tree that survived a nuclear blast..." → 4–6 likes vs 1 like for direct product hook |

**Files updated:**
- `04-Analytics/Winning-Patterns.md` — 4 copy patterns, 2 visual styles, Week 1–2 trend rows
- `PC Brain/Content Engine.md` — added "Performance Learnings" section with ranked hook formulas and format priority
- `PC Brain/Brand Identity.md` — added "Science Hooks That Resonate" table with live data

---

## My Considerations

### What's actually working

**The Reel on May 20 is the most important data point in the first two weeks.** It's not just the best Sales Motor post — it's #4 all-time on an account with 141 posts. And it was published manually because the API upload route is broken. That means the single best-performing content format is the one with zero automation. That's the most urgent fix in the entire system.

The present-tense problem hook ("Two cups in. Still foggy.") is doing something very specific: it puts the reader inside their own pain without any setup. No brand name, no product, no explanation — just a scene they recognize. That's why it outperforms ingredient hooks. The ingredient hooks lead with the answer; this one leads with the feeling.

**The CTA Stories system is a solid infrastructure addition.** 10 conversion-focused stories cycling daily at 4am, fully automated, with the URL visible in every frame. The limitation (no API link sticker) is real but not blocking — the image design carries the message. Over 30 days, this touchpoint compounds.

### What's not working and why

**Carousel engagement is declining.** This isn't the carousel format breaking — it's the hooks. The May 11 carousel had a strong hook and got 6 likes in 12 days. The May 19 carousel got 1 like in 4 days. The format is the same. The hook quality dropped. The fix is not to abandon carousels — it's to apply the pain-first hook formula to every carousel Slide 1.

**WhatsApp is the weakest platform by reliability.** Session management is a structural problem — WhatsApp Web sessions expire, and re-auth requires a manual QR scan. There's no clean programmatic solution. This will keep breaking unless it's handled proactively (e.g., a weekly health-check cron, or a Slack/Telegram alert when the session expires).

**Threads has never posted.** The credentials were never added to `.env`. This is a 5-minute fix, but it's been pending since day 1. Every day without Threads is a missed distribution channel that costs nothing to activate.

**P3 Founder content was skipped entirely May 18–22.** This is a strategic mistake, not a system failure. P3 (Founder Story) is the highest-trust pillar — it's the content that builds the relationship between Leo and the audience. The Ironman/morning ritual content is sitting in the archive unused. It should go out next week.

### What I think the priority order should be next week

1. **Fix the Reel API upload** — multipart direct upload instead of URL-based. This is the single action with the highest expected return. Every Monday Reel that posts manually is a risk that the post doesn't happen at all.

2. **Post the May 20 P3 content** — the Ironman founder story is already written and designed. It doesn't need new work. Post it.

3. **Add Threads credentials** — 5 minutes. Opens a new channel.

4. **Re-auth WhatsApp** — 5 minutes. Restores a channel that's been down since May 21.

5. **Request `instagram_manage_insights`** — without reach and saves data, the analysis is running on half the information. Saves are almost certainly the most important metric for educational carousels and this blind spot will compound.

### Longer-term consideration

The account is posting 3.8x/week and is still below the industry ER benchmark for its size (0.46% vs 3.5–6%). This gap is mostly explained by audience composition — early followers tend to be network, family, friends, and industry contacts, not buyers. That's normal at 942 followers.

The metric to watch over the next 30 days is not engagement rate — it's follower growth. Daily posting at 3.8x/week should move the follower count. If it doesn't move by June 22, the issue is reach (hashtag strategy, no Reels automation) not content quality.

The May 20 Reel reaching #4 all-time at 3 days old is the strongest early signal. If the format + hook formula is replicated consistently, the account should start growing. But it requires the Reel automation to actually work.

---

## Open Action Items

| Priority | Item | Owner | Est. Time |
|----------|------|-------|-----------|
| 🔴 | Fix Reel API upload (multipart) | Engineering | 2–4h |
| 🔴 | Post May 20 P3 content | Leo / System | 15 min |
| 🔴 | Re-auth WhatsApp | Leo | 5 min |
| 🟡 | Add Threads to `.env` | Leo | 5 min |
| 🟡 | Request `instagram_manage_insights` | Leo | 15 min (App Review) |
| 🟡 | Re-export story9.jpg from Figma | Leo | 10 min |
| 🟢 | Add `push_jpegs_to_github()` exit-code check | Engineering | 30 min |
| 🟢 | WhatsApp session health-check cron | Engineering | 1h |

---

*Report covers session of May 23, 2026.*
*Data sources: Instagram Graph API, publish_confirm.md logs (may11–may22), Winning-Patterns.md.*
