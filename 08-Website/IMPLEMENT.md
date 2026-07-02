# Website Implementation Checklist

Files are ready. Paste in this order.

---

## 1. Kill the "AI science formula" line

On the product page in Shopify admin, find and delete every instance of:
- "A.I. science formula"
- "AI science formula"
- "AI-powered formula"

Replace with: **"11 real ingredients. Real doses. Nothing hidden."**

This is the highest-trust-damage item on the site. Do this first.

---

## 2. Fix the competing CTAs

Currently the product page has three different framings:
- "Try it for 7 days — $18.90"
- "BOOST MY DAY for $1.26/morning"
- "Start My 15-Day Supply"

Pick one and use it everywhere: **"Start for $1.26 a morning"**

The sub-line handles the context: "15 servings · $18.90 · free shipping"

---

## 3. Add the Hero section

File: `Section-Hero.liquid`

Online Store → Themes → Edit code → Sections → "Add a new section" → name it `pc-hero` → paste the file.

Then in the theme editor (Customize), drag it to the top of the homepage. Move the old hero below it or remove it.

The new headline: "Your 10am crash isn't caffeine wearing off."

---

## 4. Add the Ingredient Transparency section

File: `Section-Ingredients-Transparency.liquid`

**Before pasting:** Verify the caffeine display. The section now shows "175mg total caffeine per serving (from instant coffee and matcha combined)" — cross-check this against the physical label.

**Also before pasting:** Fill in ingredients 10 and 11. Look at the physical label. The two placeholders marked `{% comment %}` are where they go.

Same process: new section named `pc-ingredients`, add to homepage below the hero or product callout.

---

## 5. Add the Price Comparison section

File: `Section-Price-Comparison.liquid`

Add below the ingredient section. This turns the "$18.90 vs $30" content angle into a homepage conversion module.

The "11 active ingredients" number in the math bar matches the updated ingredient count.

---

## 6. Add the Reviews section

File: `Section-Reviews.liquid`

Add below price comparison or above the footer.

**Before pasting:** Pull 3 real buyer quotes from your Google reviews or recent DMs. The current quotes are from Luis D. (Go Global interview) and Lauriete M. (verified review). Replace the third quote with a newer real buyer.

Update the "112 reviews" count when it changes.

---

## 7. Enable Subscribe & Save

On the product page, make the subscription option visible and featured, not buried in FAQ.

Use Shopify Subscriptions or ReCharge. Show: "Subscribe & Save 15% — $15.21/bag, cancel anytime."

This is the single highest-LTV action available. One-time buyers who switch to subscription have materially higher lifetime value.

---

## Priority order

| # | Action | Time | Revenue impact |
|---|---|---|---|
| 1 | Kill "AI science formula" | 5 min | High (trust) |
| 2 | Fix competing CTAs to one | 10 min | High (conversion) |
| 3 | Add Hero section | 20 min | High (cold traffic) |
| 4 | Add Reviews section | 20 min | High (social proof) |
| 5 | Add Ingredients section | 30 min (after label check) | Medium (trust) |
| 6 | Add Price Comparison section | 20 min | Medium (objection) |
| 7 | Enable Subscribe & Save | 1 hour | Highest (LTV) |
