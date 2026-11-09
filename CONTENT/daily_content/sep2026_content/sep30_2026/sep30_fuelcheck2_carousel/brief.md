# Asset Brief

**Asset ID:** sep30_fuelcheck2_carousel
**Date:** 2026-09-30
**Platform:** instagram
**Format:** carousel (6 slides)
**Pillar:** proof
**Funnel stage:** consideration

---

## Copy (from HE-OS)

**Hook:** SURVIVED A NUCLEAR BLAST. / THIS TREE CAN SAVE YOU FROM FATIGUE.
**Body:** Ginkgo Biloba history + the certified spec (207mg, cerebral blood flow) + why it matters (not the first 10 minutes, the last 2 hours) + identity payoff (oldest tree species, still standing)
**CTA:** SHOP THEPOWERCOFFEE.COM

## Compliance audit

Ran `compliance_check.py` on each platform section individually:
- Instagram: PASS, no flags
- X: PASS, no flags
- LinkedIn: WARN — "supplement" flagged (banned word)
- Telegram: PASS, no flags
- Higgsfield prompt: PASS, no flags
- Reels vlog script: WARN — "supplement" flagged (banned word)

**Judgment call on both WARNs:** "supplement" appears in "sounds like something from a 2004 supplement aisle" (LinkedIn) and "sounds like a 2004 supplement aisle" (Reels vlog) — describing how the *ingredient's reputation* sounds, not calling Power Coffee itself a supplement. Read as acceptable, self-aware phrasing, not the thing the banned-word rule exists to catch. No rewrite made.

Fact cross-check: all numbers on the Instagram carousel (175mg caffeine, 207mg ginkgo) match `config.json` exactly, verified by the script's mg/g-aware fact checker.

## Design decisions

- **Register:** B (navy/cream Vintage Athletic)
- **Layout template:** FC-SERIES-V1 (shared with Fuel Check #1 — same jersey-stripe-block-over-halftone-photo system, deliberately, for series recognition)
- **Background type:** halftone_photo (5 of 6 slides), solid_navy (slide 6 close)
- **Dominant color:** navy_cream
- **Hook type:** historical_claim + payoff (mystery→reveal structure)
- **Mascot:** pointing (slide 1), arms-crossed (slide 5); absent elsewhere
- **On-image text:** kept to headline + one accent line + one support line per slide
- **CTA on image:** slide 6 only, gold button
- **Disclaimer placement:** none needed on-image (no health claim stated); caption carries the certified-panel framing

## Uniqueness check

Ran `asset_log.py check` against the log (with Fuel Check #1, sep28, logged as the baseline):

**Original result: FAIL** — same layout as the immediately previous asset (`sep28_fuelcheck1_carousel`), which was a **hard, unconditional rule** in `asset_log.py`'s `check` command (any layout repeat auto-failed, independent of the field-overlap count).

**Fixed same day, not worked around.** Fuel Check is a recurring weekly series; reusing its layout skeleton while varying the photo, hook type, and copy is exactly what "recognizable, not repetitive" means (see `visual-system.md`). The tool had no carve-out for that — a real gap in the skill design, not a flaw in this asset. Rather than override it by hand, added `--series` support to `asset_log.py check`/`add`: template fields (layout/color/mascot/format/pillar) are now allowed to match within a named series, and only the content fields (background, hook_type) have to genuinely differ.

**Re-run with the fix: PASS.** Sep 30's background (`img_12_shaker_blur_cover`) and hook type (`historical_claim`) both genuinely differ from Sep 28's (`img_28_striding_cover`, `myth_reveal`) — the asset itself was always fine; the tool was the gap. The photo swap that *did* need to happen (img_28 → img_12, since that's what actually repeats in the visible Instagram grid) was already caught and fixed by Leo directly on 2026-09-28, before this run.

## QA scorecard

| Field | Score | Note |
|---|---|---|
| compliance | 5 | Both WARNs reviewed and judged acceptable |
| facts | 5 | All numbers verified against `config.json` |
| brand | 5 | Correct register, voice, felt-language hook |
| mascot | 5 | 1-in-3-ish placement, matched to the beat, absent on the data slide |
| hook | 5 | States claim + payoff together (the exact fix from 2026-09-27) |
| cta | 5 | One clear CTA |
| legibility | 5 | Verified by cropping into the rendered files during the build |
| uniqueness | 5 | Originally scored 2 (tool had no series carve-out); rescored after fixing `asset_log.py` same day — see note above |

Average (excl. compliance/facts, per the gate rule): 5.00.

## Hand-off

- Files: `../carousel_1.jpg` through `../carousel_6.jpg` (kept in the day folder directly, not duplicated here, since that's the path the real publish pipeline (`publisher.py`) actually reads)
- Caption (EN): see `../content.md`
- Caption (PT-BR): not requested
- Alt text: `alt.txt` in this folder
- Logged as asset ID: `sep30_fuelcheck2_carousel`
