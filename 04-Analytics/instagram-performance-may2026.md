# Instagram Performance Analysis — @powercoffee.ofc
**Date:** May 23, 2026
**Data source:** Instagram Graph API (likes + comments — reach/impressions require `instagram_manage_insights` permission, not yet active)

---

## Account Overview

| Metric | Value |
|--------|-------|
| Followers | **942** |
| Following | 313 |
| Total posts (all time) | 141 |
| Follower/following ratio | 3.0x |

---

## Sales Motor Period vs Before

| Period | Posts | Avg interactions | Avg ER | Posting frequency |
|--------|-------|-----------------|--------|-------------------|
| Pre-Sales Motor (Dec 20 – May 10) | 24 | **6.0** | **0.64%** | 1.2x / week |
| Sales Motor Live (May 11 – May 22) | 6 | **4.3** | **0.46%** | 3.8x / week |

**Context:** The lower SM-period average is partly explained by post age. The May 22 carousel is 1 day old, May 19 is 4 days old — both still accumulating. The May 20 Reel (3 days old) already has 11 interactions and is **#4 all-time**. Adjust the comparison in 2 weeks when posts have fully aged.

---

## Sales Motor Posts — Individual Performance

| Date | Format | Likes | Comments | ER | Days Live |
|------|--------|-------|----------|----|-----------|
| May 11 | Carousel | 6 | 0 | 0.64% | 12 |
| May 12 | Carousel | 4 | 0 | 0.42% | 11 |
| May 15 | Carousel | 2 | 0 | 0.21% | 8 |
| May 19 | Carousel | 1 | 0 | 0.11% | 4 |
| **May 20** | **Reel** | **10** | **1** | **1.17%** | 3 |
| May 22 | Carousel | 2 | 0 | 0.21% | 1 |

**Carousel engagement is declining across the period.** Even accounting for age, the May 11 carousel has 6 likes after 12 days while the May 12 carousel has 4 likes after 11 days. The algorithm may be distributing reach more thinly as posting frequency increases.

**The Reel is the clear outlier.** 11 interactions in 3 days vs an average of 3.0 interactions per carousel in the same period.

---

## Format Performance — All Time (30 posts sampled)

| Format | Posts | Avg interactions | Best post |
|--------|-------|-----------------|-----------|
| **Reel** | 9 | **8.3** | 18 (Mar 5, 2026) |
| **Carousel** | 16 | **5.1** | 16 (Feb 3, 2026) |
| **Image** | 5 | **3.0** | 5 (Jan 1, 2026) |

**Reels outperform carousels by 63% on average.** Despite this, 4 of 6 Sales Motor posts during this period were carousels and only 1 was a Reel (posted manually).

---

## All-Time Top 5 Posts

| Rank | Interactions | Date | Format | Notes |
|------|-------------|------|--------|-------|
| #1 | 18 | Mar 5, 2026 | Reel | Best ever — investigate hook/content |
| #2 | 16 | Feb 3, 2026 | Carousel | 2nd best — review the format/topic |
| #3 | 14 | Jan 21, 2026 | Reel | 10 likes + 4 comments |
| **#4** | **11** | **May 20, 2026** | **Reel** | **Sales Motor content, manual post** |
| #5 | 8 | Mar 3, 2026 | Reel |  |

3 of the top 5 are Reels. The #4 post is Sales Motor content, posted only 3 days ago. **This is the strongest signal in the dataset.**

---

## Engagement Rate vs Industry Benchmark

| Segment | Typical ER (likes+comments) |
|---------|---------------------------|
| Accounts under 10K followers (industry avg) | 3.5 – 6.0% |
| @powercoffee.ofc (pre-SM avg) | **0.64%** |
| @powercoffee.ofc (SM period avg) | **0.46%** |

**Power Coffee is significantly below the benchmark for accounts its size.** This is common for early-stage DTC brands with a mixed audience (many followers may be network/industry vs target buyers). The gap is the growth opportunity — content that generates saves and shares (not tracked by current API permissions) would be the real lever.

---

## What's Not Being Tracked (Critical Gap)

The app token is missing `instagram_manage_insights`. This means:

| Missing metric | Why it matters |
|----------------|---------------|
| **Impressions** | Total views, including non-followers — measures reach beyond existing audience |
| **Reach** | Unique accounts that saw the post — key for growth |
| **Saves** | Most powerful Instagram signal — indicates evergreen content value |
| **Shares** | Viral coefficient |
| **Profile visits** | Post → profile → follow funnel |
| **Story metrics** | Exits, taps forward/back, replies — stories expire from API after 24h |

**Saves are likely the most important missing metric.** Educational carousels (ingredient science, formula breakdowns) typically generate 3–5x more saves than likes. Power Coffee's carousels are highly saveable content — the actual engagement may be much higher than the like/comment count suggests.

### How to fix
Add `instagram_manage_insights` in the Facebook Developer app → App Review → request permission. Once granted, the publisher can start logging impressions, reach, and saves per post automatically.

---

## Format Strategy — What the Data Says

### Reels: under-used, over-performing
- **4 of top 5 all-time posts are Reels or include video**
- Sales Motor currently produces 1 Reel/week (Monday) — automated route is broken (manual only)
- **Fixing the Reel upload pipeline is the single highest-ROI infrastructure task**

### Carousels: solid base, engagement declining
- Carousels are working well for educational content (ingredients, formula science)
- Best carousel all-time: 16 interactions (Feb 3) — investigate that content hook
- Recent carousels (May 15, 19, 22) showing lower engagement — may need stronger opening slides

### Stories: blind spot
- Stories are posted (May 13, 14, 21) but expire from the API within 24h — zero performance data
- CTA Story system now live as of May 22 — still no insights without `instagram_manage_insights`
- No way to measure story exit rate, reply rate, or link taps without the permission

---

## Posting Frequency Effect

Frequency went from **1.2x/week → 3.8x/week** with the Sales Motor. This is a positive infrastructure change, but early data suggests per-post engagement may dilute slightly at higher volume. This is normal and expected — reach typically grows with frequency even if per-post ER dips. Watch the follower count trajectory over the next 30 days as the real signal.

---

## Recommendations — Prioritized

### Immediate
1. **Fix the Reel API upload** — switch from URL-based to direct multipart upload. Reels are the #1 format by data and the automation is currently broken (manual fallback).
2. **Request `instagram_manage_insights` permission** — without it, half the analysis is invisible. This is a 1-click App Review request.

### This Week
3. **Audit the Mar 5 Reel (#1 all-time, 18 interactions)** — review the hook, audio, and content structure. Whatever worked there should be replicated in the Sales Motor Reel format.
4. **Audit the Feb 3 Carousel (#2 all-time, 16 interactions)** — identify what made the opening slide work. Apply to current carousel hooks.
5. **Strengthen carousel Slide 1 hooks** — the May 11–22 carousels show a clear engagement decline. The hook slide is the lever.

### Next 30 Days
6. **Shift content mix toward more Reels** — data supports 2–3 Reels/week instead of 1. The Monday Reel should become fully automated.
7. **Track follower growth weekly** — the 942 baseline is set. Daily posting should move this number. If it doesn't in 30 days, content or hashtag strategy needs review.
8. **Set up a story analytics log** — capture story post IDs immediately after publish (within 24h) and query metrics before they expire. Add this to the 4am or 5am scripts.

---

## Data Limitations

- Like/comment counts only — no impressions, reach, saves, shares, or story metrics
- 30 posts sampled (API default) — posts before Dec 2025 not included
- Stories are not returned in the media endpoint (separate stories endpoint, 24h expiry)
- Engagement rates will shift as newer posts age (particularly May 19–22)

---

*Generated from Instagram Graph API — endpoint: `/{account_id}/media` with fields `like_count,comments_count,media_type,timestamp`*
*For full analytics, add `instagram_manage_insights` to the app permissions.*
