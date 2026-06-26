# The Power Coffee — Website

**URL:** thepowercoffee.com  
**Platform:** Shopify  
**Last audited:** 2026-06-08

---

## Hero Section — Current vs Rewritten

### Current (broken / off-brand)
| Element | Current text |
|---|---|
| Headline | YOUR COFFEE SUPERCHARGED! |
| Subheadline | Add one scoop. Get all-day energy and focus, no crash, no jitters. |
| CTA | 👉 BREAK MY FATIGUE CYCLE |
| Badge 1 | AI science-Backed Formula |
| Badge 2 | Zero Sugar / Zero Lactose |
| Badge 3 | 4.5★ Customer Rating |
| Badge 4 | Made in USA |

### Rewritten (ready to paste)

**Main Headline**
```
Your coffee isn't the problem.
It's under-built.
```

**Subheadline**
```
One scoop. 11 ingredients. Same morning ritual — without the crash.
```

**Body text**
```
Regular coffee was built for a 45-minute lift. Power Coffee adds taurine,
matcha L-theanine, pea protein, and 8 more ingredients that turn your
existing brew into something that holds — through the meetings, the
afternoon, and everything after. $1.19 a morning.
```

**CTA button text**
```
Try it for 7 days — $17.90
```

**CTA button URL**
```
/collections/all
```

**Secondary link (below button)**
```
See what buyers say after Day 3 ↓
```

**Updated trust badges**
| Badge | Updated |
|---|---|
| ~~AI science-Backed Formula~~ | 4.9★ · 112 verified buyers |
| Zero Sugar / Zero Lactose | Zero Sugar · Zero Lactose |
| ~~4.5★ Customer Rating~~ | 30-day money-back guarantee |
| Made in USA | Made in USA |

---

## HTML Block (paste into Shopify → Customize → Add section → Custom HTML)

```html
<section style="background:#171412; padding:80px 24px 64px; text-align:center; font-family:'Georgia', serif;">

  <!-- Pre-headline -->
  <p style="font-size:13px; font-family:'Arial', sans-serif; letter-spacing:0.15em; color:#D9A633; text-transform:uppercase; margin:0 0 20px;">
    The first win of your day.
  </p>

  <!-- Main headline -->
  <h1 style="font-size:clamp(36px,5vw,64px); font-style:italic; font-weight:700; color:#F7F0E0; line-height:1.05; margin:0 auto 24px; max-width:760px;">
    Your coffee isn't the problem.<br>It's under-built.
  </h1>

  <!-- Subheadline -->
  <p style="font-size:clamp(16px,2vw,20px); color:#C07A47; font-family:'Arial', sans-serif; font-weight:600; margin:0 auto 20px; max-width:600px; line-height:1.5;">
    One scoop. 11 ingredients. Same morning ritual — without the crash.
  </p>

  <!-- Body copy -->
  <p style="font-size:16px; color:#c0b8ad; font-family:'Georgia', serif; line-height:1.7; margin:0 auto 36px; max-width:540px;">
    Regular coffee was built for a 45-minute lift. Power Coffee adds taurine, matcha L-theanine, pea protein, and 8 more functional ingredients to the cup you're already making. No new routine. No second cup by 10am. <strong style="color:#F7F0E0;">$1.19 a morning.</strong>
  </p>

  <!-- CTA Button -->
  <a href="/collections/all"
     style="display:inline-block; background:#D9A633; color:#171412; font-family:'Arial', sans-serif; font-size:15px; font-weight:700; letter-spacing:0.08em; text-decoration:none; padding:18px 44px; text-transform:uppercase; margin-bottom:16px;">
    TRY IT FOR 7 DAYS — $17.90
  </a>

  <!-- Secondary link -->
  <p style="margin:0 0 48px;">
    <a href="#reviews" style="font-size:13px; font-family:'Arial', sans-serif; color:#D9A633; text-decoration:none; letter-spacing:0.05em;">
      See what buyers say after Day 3 ↓
    </a>
  </p>

  <!-- Trust bar -->
  <div style="display:flex; flex-wrap:wrap; justify-content:center; gap:24px 40px; border-top:1px solid rgba(217,166,51,0.25); padding-top:28px; max-width:720px; margin:0 auto;">
    <span style="font-size:13px; font-family:'Arial', sans-serif; color:#D9A633; font-weight:700;">
      ★★★★★ &nbsp;4.9 · 112 verified buyers
    </span>
    <span style="font-size:13px; font-family:'Arial', sans-serif; color:#c0b8ad;">
      Zero Sugar · Zero Lactose
    </span>
    <span style="font-size:13px; font-family:'Arial', sans-serif; color:#c0b8ad;">
      30-day money-back guarantee
    </span>
    <span style="font-size:13px; font-family:'Arial', sans-serif; color:#c0b8ad;">
      Made in USA
    </span>
  </div>

</section>
```

---

## Full Site Audit — Issues & Priority

### Critical (fix this week)
1. **Hero CTA goes to partner page** — replace with direct `/collections/all`
2. **112 Google reviews at 4.9★ not embedded** — add Google Reviews widget to homepage above fold. Invisible social proof = zero social proof.
3. **Testimonials section is placeholder** — email last 90 days of buyers: *"What changed about your mornings after Week 3?"* Publish their exact words.

### Copy fixes
4. **"Supercharged" in headline** — brand rule: never use. Fixed in rewrite above.
5. **"AI science-backed formula" badge** — confusing, removes trust. Replaced with 4.9★ / 112 reviews.
6. **"BREAK MY FATIGUE CYCLE" CTA** — aggressive, emoji, off-brand. Fixed above.
7. **"Sustained energy" site-wide** — replace with "smooth energy" (buyer word, confirmed by PULSE).
8. **Triple-action #3: "calorie burn"** — supplement language, wrong buyer. Replace: *"Cinnamon + ginger stabilize blood sugar so energy stays level, not spiked."*
9. **Pricing math missing** — $1.19/serving not visible on homepage. Add to hero body copy and product section.
10. **Day 3 proof missing from homepage** — biggest objection: "what if it doesn't work Day 1?" Add a section: *"Day 1: skeptical. Day 2: noticed something. Day 3: stopped reaching for a second cup."*
11. **Founder days stale** — "430 days" in founder story → update to "550+ days"

### What's working (keep)
- "You're Not 'Tired.' You're Under-Fueled" section — strong, keep
- FAQ accordion — covers real objections
- Blog content — 6 articles, strong titles, SEO-friendly
- Money-back guarantee mention
- Ingredient carousel
- Founder story section (just needs days updated)

---

## Conversion Triggers to Add (from buyer data)

See `04-Analytics/Winning-Patterns.md` → Purchase Triggers section for full framework.

Key triggers missing from current site:
- **Second cup test CTA:** "Tomorrow morning: one scoop. See if you reach for a second cup by 10am."
- **Day 3 specificity:** buyer language that removes the vagueness objection
- **$1.19 math:** visible in hero, not just product page
- **112 reviews:** embedded, not referenced
- **"Smooth" word:** replace "sustained" everywhere
- **Red Bull taurine reframe:** good for P2 blog/product page, not necessarily hero
- **550 days founder use:** update the founder section number

---

## Products

| Product | Regular | Sale | Notes |
|---|---|---|---|
| 10-day pack | $21.90 | $17.90 | Clarify serving count (says "10 servings" — confirm vs brand.md "15 servings") |
| 30-day pack | $90.99 | $45.90 | 50% discount — confirm serving count |

**Serving count discrepancy:** website says "10 servings (15-day supply)" — 10 ≠ 15. Clarify and correct. Brand.md states 15 servings at $17.90 = $1.19/serving.

---

*Last updated: Jun 8, 2026*
