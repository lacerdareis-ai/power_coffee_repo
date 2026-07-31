# August 2026 — Plan to 100 Sales (Amazon + DTC)

**Created:** 2026-07-31 · **Baseline:** ~0 tracked sales in July · **Target:** 100 sales in August (~3.2/day) · **AOV:** ~$32 → ~$3,200 revenue

---

## PART 1 — LENS diagnosis: why July was 0 sales

Drawn from the LENS reports (jun–jul) + the analytics/revenue CSVs. The content is NOT the problem. The **commercial engine** is. Five root causes:

1. **No distribution.** Instagram reach collapsed: July posts reached **8–224 people (avg ~84)**, 1–5 likes each, on a 972-follower base. The Jul 20–24 LENS report says it plainly: *"At 84 average reach… the current Instagram funnel is a brand-building vehicle, not a primary revenue driver — that shifts only when reach crosses into the low thousands."* You cannot produce 100 sales from ~84 reach/day.
2. **Only one channel is actually selling.** LENS: *"Only Instagram was live this week. X, LinkedIn, Blog, and Email were written and confirmed ready but not published."* And none of these are purchase channels anyway.
3. **No paid acquisition running.** Amazon PPC keywords were fully planned (Jun 23) but there's no evidence of live ad spend. DTC has zero paid traffic. Organic-only at dead reach = near-zero volume by math.
4. **The conversion levers are built but not deployed.** The **Power Starter Kit** ($31.90 bundle — the AOV + gift + habit lever) is flagged *"Not yet live."* The avatar landing pages were designed but adoption is unclear. No live offer, urgency, or bundle.
5. **Flying blind — no attribution.** `shopify-revenue.csv` is an empty header. No UTM tags, no per-channel discount codes. "0 sales" is partly "0 *tracked* sales." We literally cannot see which channel converts.

### The funnel, in hard numbers (IG Insights, ~30-day, pulled 2026-07-31)
| Stage | Count | Conversion |
|-------|-------|-----------|
| Views | 3,825 (by only 932 accounts — repeat views) | — |
| Accounts reached | 932 | ≈ your 973 followers → **almost zero cold reach** |
| Interactions | 184 (only **40 accounts engaged** all month) | 4.8% of views |
| Profile visits | 330 | 8.6% of views |
| **External link taps** | **15** | 4.5% of profile visits |
| **Sales** | **0** | **0% of link taps** |

Two things this proves:
1. **The top of the funnel is microscopic.** 15 link taps in a month means ~15 people even *reached* the store from social. No funnel converts 0 → 100 from 15 clicks. Volume is the primary constraint → must add paid (Amazon PPC + Meta).
2. **The store itself is fine — so the constraint is VOLUME, not conversion.** Verified the landing page (`/pages/betterday`, 2026-07-31): loads clean, clear price ($18.90/bag), "Buy 2 Get 1 Free," 4.9★/112 reviews, 30-day guarantee, working CTAs. 15 clicks *should* yield ~0–1 sale, so 0 is a volume problem, not a broken funnel. Good news: we don't have to fix the store, we have to fill it. **BUT** the live promo (code FOURTH, "Buy 2 Get 1") **expires July 31** — August needs a fresh offer on day one (launch the Starter Kit + a new August code), or paid traffic lands on an expired deal.

**Assets we DO have (the foundation to build on):**
- **Amazon: 4.9★ from 112 verified organic reviews.** This is real and valuable — it means Amazon ads will convert.
- Proven content patterns: founder-defense Reels (28.6% ER) and present-tense problem hooks (best reach). Good creative for *paid* amplification.
- A finished (unlaunched) Starter Kit offer + subscription upsell.
- A daily content engine that reliably ships.

**⚠️ The "8,000 email list" is NOT a lever — it's a liability.** `email_list.txt` (8,006 addresses) was built by `fetch_gmail_contacts.py` = the founder's personal **Gmail contacts, not opted-in subscribers.** Mass-blasting it is a CAN-SPAM / deliverability / domain-reputation risk and explains ~0 email conversion. **Do not scale email to this list.** (Build a real opt-in list for Sept — see Part 4.)

---

## PART 2 — The honest precondition

**100 sales from a standing start of 0, in 31 days, is achievable but NOT with organic content alone.** It requires a modest paid budget. Realistic ask: **~$1,000–1,300 in ad spend for August** (~$35–45/day split Amazon + Meta). With that budget + the offer live + attribution on, 100 is realistic. With **$0 budget**, the honest organic ceiling is ~10–25 sales (Amazon organic halo + tiny DTC), not 100 — say so up front rather than promise it.

Channel split target: **Amazon ~60 · DTC ~40.**

---

## PART 3 — The plan

### Channel A — Amazon (target ~60 sales) — *fastest path, highest intent*
Amazon is a search/intent channel and we already have 112 reviews at 4.9★. This is the single strongest lever.

1. **Turn on Sponsored Products PPC** on the Tier-1 keywords already researched (`amazon_keywords.md`): *no crash coffee, functional coffee no crash, afternoon energy boost, energy coffee no jitters, clean energy coffee*. Start ~$20–25/day, exact + phrase match, harvest search terms weekly, kill >40% ACOS losers, scale <25% ACOS winners.
2. **Refresh the listing:** title front-loads the problem ("No-Crash Functional Coffee Booster…"), add A+ / brand content, and put the **Illuminate Labs Certified badge** + "Reviewed by an MD" in the image stack and A+ (the certification we just earned — a conversion asset). Load the backend keywords from `amazon_backend_keywords.md`.
3. **Launch coupon + Subscribe & Save:** a 10–15% clippable coupon (green badge lifts CTR) and enable S&S for repeat revenue and BSR momentum. Do NOT deep-discount — protect margin.
4. **Review velocity:** hit "Request a Review" on every order, add a product insert card (QR to a how-to + review ask), and enroll in Vine if eligible. More reviews → better rank → cheaper organic sales.
5. **Math:** ~$22/day at ~$0.60 CPC ≈ 35 clicks/day; at ~8–12% CVR (justified by 4.9★) ≈ 3–4 ad orders/day, plus organic halo as BSR climbs → ~60/month is credible.

### Channel B — DTC / Shopify (target ~40 sales) — *ebook-led funnel*
Organic reach is dead and a cold micro-audience won't buy on first click (15 taps → 0 sales). So lead with a **free lead magnet**, capture a real opt-in, and let email nurture convert. Full copy: `august_landing_offer_copy.md`.

**Funnel:** cold traffic → **free ebook `/pages/10shakes`** → real opt-in email → 5-email nurture → purchase (First Win Bundle) → non-buyers retargeted on Meta. This also builds the permissioned list we don't currently have.

1. **Free ebook as the entry offer** ("10 Power Coffee Shakes"). Near-zero friction; every download is a permissioned lead (unlike the cold Gmail-contacts file).
2. **5-email nurture sequence** is the actual sales engine — deliver → problem → trust/cert → proof+offer → urgency. The Starter Kit / First Win Bundle is the conversion offer inside the nurture, not the cold ask.
3. **Meta/IG paid ads** ($15–20/day) drive to the **free ebook** (much higher cold CVR than a $18.90 ask), using the **proven organic winners as creative** — the founder-defense Reel (28.6% ER) and the present-tense 2pm-crash hook. Retarget opt-ins/visitors with the buy offer.
3. **Attribution — non-negotiable, do this first:** append `?utm_source=…` to every link (IG bio, story, ads, Amazon-vs-DTC) and issue **per-channel discount codes** (e.g. AUGIG, AUGX, AUGEMAIL) so every order is traceable. Fixes the flying-blind problem and lets us see the real converting channel by week 1.
4. **Organic assist (free):** the daily content stays problem-led (persona-first rule), the certification story runs as the trust closer, and a coordinated "August launch" push in the first week. Pin the Starter Kit. Add the referral program (`referral_program.md`, "give $10 get $10") to squeeze word-of-mouth from early-August buyers.
5. **Math:** ~$500 Meta spend + a live bundled offer at even a 1.5–2.5% landing-page CVR on paid clicks → ~40 orders is plausible; the Starter Kit's higher AOV also lifts revenue per order.

---

## PART 4 — Fix the system (so Sept compounds)
- **Build a REAL opt-in email list:** use the existing ebooks (`PC — 09 Ebooks`) as a lead magnet with a proper signup form. Stop treating the Gmail-contacts file as a marketing list. A permissioned list is the highest-ROI channel — but it has to be built, not scraped.
- **Weekly LENS now includes a revenue row** pulled from Shopify + Amazon (currently absent). Decisions on CTA content should never be blind again.
- **Actually publish the other channels** if the automation says they're "ready but not live" — but treat them as awareness, not the sales plan.

---

## PART 5 — Weekly cadence & scoreboard (target 100)

| Week | Focus | Sales target (cumulative) |
|------|-------|---------------------------|
| Aug 1–3 (setup) | Attribution live, Starter Kit live, Amazon PPC + coupon on, Meta ads live, launch push | 8 |
| Aug 4–10 | Scale Amazon winners, retarget on Meta, review velocity | 30 |
| Aug 11–17 | Kill losing keywords/ads, double winners, referral push | 55 |
| Aug 18–24 | Subscribe & Save + kit upsell emphasis, mid-month offer refresh | 80 |
| Aug 25–31 | Month-end urgency ("first 100 kits" close), retarget abandoners | 100 |

**Track daily:** Amazon orders, Shopify orders (by code/UTM), ad spend, ACOS/ROAS, BSR. If by Aug 10 we're under ~25 cumulative, the constraint is almost certainly CVR or creative, not spend — diagnose before adding budget.

---

## Owner actions that only Leo can do (blockers)
1. Approve the **~$1–1.3k August ad budget** (or tell me the real number so I can resize the target honestly).
2. Set up **Amazon Sponsored Products** campaign + clippable coupon in Seller Central (I can't access it).
3. Publish the **Starter Kit** product/bundle in Shopify + turn on the subscription app.
4. Create the **Meta ads** (or grant access) — I can supply the creative/copy from proven winners.
5. Confirm the **Amazon listing** is live and eligible for ads/coupons.
