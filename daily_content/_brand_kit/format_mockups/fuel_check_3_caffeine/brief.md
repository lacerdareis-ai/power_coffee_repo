# Asset Brief

**Asset ID:** fuelcheck3_caffeine_carousel
**Date:** not yet staged to a specific day — see hand-off note
**Platform:** instagram
**Format:** carousel (6 slides)
**Pillar:** proof
**Funnel stage:** consideration

---

## Copy

**Hook:** CAFFEINE DOESN'T GIVE YOU ENERGY. / IT JUST DELAYS YOUR CRASH.
**Body:** The adenosine mechanism (blocks the tired-signal, doesn't stop the buildup) + the spec (175mg, ~5hr half-life) + the already-proven brand.md hook ("your second cup doesn't hit like the first — that's not tolerance, that's adenosine") + Power Coffee's actual answer (paired with matcha/L-theanine/blood-sugar-stable ingredients, not fighting the crash head-on)
**CTA:** SHOP THEPOWERCOFFEE.COM

**Why this topic:** "Caffeine doesn't give you energy" is the single best-measured hook in this account's history — 122.22% ER on day 1 (brand.md's Growth Report), ahead of even the Ginkgo/Hiroshima hook that drove Fuel Check #2. Grounded in a real citation: Fredholm et al., *Pharmacological Reviews*, 1999.

## Compliance audit

Ran `compliance_check.py` on the full slide copy: 1 WARN — "GIVE YOU ENERGY" flagged as an unsoftened outcome claim. **Reviewed: the phrase negates the claim** ("doesn't give you energy" — myth-busting, not asserting an energy benefit), which is exactly the kind of pattern-vs-meaning judgment call the tool is built to surface rather than resolve on its own. No rewrite needed.

Fact cross-check: 175mg caffeine confirmed against `config.json`. The ~5hr half-life figure is general pharmacology cited directly from brand.md's own vetted science section (Fredholm et al.), not a proprietary claim — kept as-is, no product-specific number attached to it.

## Design decisions

- **Register:** B (navy/cream Vintage Athletic), series template `FC-SERIES-V1`
- **Background:** halftone photo on 5 of 6 slides; solid navy CTA close
- **Cover photo:** `img_04_power.png` — genuinely new to the pool (never used in FC1 or FC2), found during this build's photo audit
- **Hook type:** science_counterclaim (new category — distinct from FC1's myth_reveal and FC2's historical_claim)
- **Mascot:** pointing (slide 1), arms-crossed (slide 5)

## Photo pool note

Full `_brand_kit/images/` audit is now complete (2026-09-28): 8 of 27 images verified clean (`img_04, 09, 12, 13, 14, 16, 24, 28`). This carousel's non-cover slides necessarily reuse photos already used in FC1/FC2 (img_16, img_12, img_09, img_14) — the pool is genuinely this small. Real production photography is still the actual fix, not more AI-generated packs (see the fabricated-label project memory).

## Uniqueness check

`asset_log.py check --series fuel_check`: **PASS** — 0/7 field overlap against non-series assets, and both content fields (background, hook_type) differ from every prior Fuel Check entry.

## QA scorecard

All 8 fields scored 5. Average (excl. compliance/facts): 5.00.

## Hand-off

- Files: `slide_1.jpg` through `slide_6.jpg` in this folder
- Logged as: `fuelcheck3_caffeine_carousel` (series: `fuel_check`)
- **Not yet staged to a specific `daily_content` day folder** — no date was given for this one; ready to copy into place as soon as a day is picked.
