# Weekly UGC Reel — SOP + cadence

**Created:** 2026-07-31 · **Cadence:** 1 UGC reel per week · **Publish day:** Wednesday (Instagram Reel 2 slot) · **Best time:** ~11:00-12:00 local.

## Why Wednesday, ~late morning
- **Wednesday** is already the mid-week Reel slot (Reel 2 in the rotation), so UGC drops in without disrupting the Mon founder / Fri ritual+offer reels. Mid-week reach is the strongest window for this niche, and a Wednesday UGC seeds the problem-reframe two days before the Friday offer close, warming cold viewers before the CTA.
- **~11:00-12:00** so the "2pm crash" message lands right before the audience's actual afternoon slump. It is thematically and behaviorally timed, and lunch is a natural IG peak.
- Tune with data: once attribution is live, check IG Insights day/time and shift if a different window converts better.

## Scheduling
- **Reminder:** `run_ugc_reminder.sh` fires every **Sunday 17:00** (cron `0 17 * * 0`) → Telegram nudge to make that week's reel, ready for Wednesday. It aligns with the Sunday film session.
- **Why a reminder, not full autonomy:** creation uses Higgsfield credits + judgment (the ugc-flow with Claude), so it is human-triggered, not an unattended cron. Check the Higgsfield balance first (2 videos ran ~292 credits; 1 ~146).

## Available UGC pool (all captioned 2026-08-03) — rotate creators, never repeat a video two days running
All four captioned versions live in `daily_content/_brand_kit/ugc_august2026/` (`*_captioned.mp4`). Raw originals of the July three are in `daily_content/_brand_kit/videos/`.
- **Julia** (`ugc_julia_2pm_crash_9x16_captioned.mp4`) — woman ~35, home office, "2pm crash" (AI, known script).
- **green-haired creator** (`ugc_liam_captioned.mp4` + `ugc_yuna_captioned.mp4`) — **same person**, two clips (pink room / disco room + glass-and-scoop). Script: "dangerously good at waking you up. One scoop, water or milk... eight ingredients, real caffeine, matcha, taurine, nothing fake."
- **malik** (`ugc_malik_captioned.mp4`) — male creator, London street + tumbler. Taste-angle review.
- Filenames don't match the person ("liam" is a woman) — go by descriptions, not names.

**Captioning method (2026-08-03):** transcribe with `faster_whisper` (word timestamps) then burn Inter captions — script `caption_ugc.py` in scratchpad (transcribe → chunk → PIL overlay → ffmpeg). Includes a CORRECT dict for STT mishearings (whisper hears "taurine" as "torian"/"tore"; fix before rendering). No Higgsfield credits needed.

**W32 usage:** Tue (aug04) = Julia (captioned). Wed (aug05) = malik (captioned). Consecutive reels use different creators. ~3 distinct faces = ~3 weeks unique before repeating.

## The repeatable process (what worked 2026-07-31)
Run the Higgsfield **ugc-flow** with Claude. Settings that produced the Julia reel:
1. **Product intake** — import the pouch cutout (`frente.png`) as the product image.
2. **Creator** — soul_2, 3:4, an attractive natural person ~35, home office, NO product in this shot. Verify face is good before continuing.
3. **8-slot board** — gpt_image_2, 16:9: consistent creator, correct product label, scoop + mix-into-a-glass-of-water beats, NO coffee mug.
4. **De-slop pass** — seedream_v5_pro on the board.
5. **Video** — seedance_2_0, **9:16, 1080p, 15s**, medias = [board, character, product]. 8 hard cuts mapped to the monologue. Render takes a few minutes.
6. **Captions** — burn word-chunked captions with the brand **Inter** font (script: the ffmpeg + PIL overlay approach in scratchpad; white text, dark stroke + shadow, ~66% vertical). Most paid/social plays muted, so captions are mandatory.
7. **QA (frozen-frame)** — one hero product, correct legible label, glass-not-coffee, one clean hand per beat, no baked text/watermark, face consistent across cuts.
8. **Deliver** — save both plain + captioned 9:16 mp4 to `daily_content/_brand_kit/ugc_august2026/` (or that month's folder).

## Publish it as the Wednesday reel
- Copy the **captioned** mp4 to that week's Wednesday content folder as `instagram.mp4`. The publisher uploads `instagram.mp4` as a Reel (publisher.py). Content generation writes `content.md`/`story.jpg` only, so the dropped video is not overwritten.
- The weekly plan's Wednesday IG item should reference the UGC (see `weekly_plans/…/plan.json`).

## Compliance (every UGC)
- **Illustrative ad, not a testimonial.** The creator never claims to be a real customer (FTC). Frame captions/landing copy as a demo, not a customer review.
- Persona-first (the 2pm crash), product is the receipt. No coffee mug as subject. No protein-gram figure, no mg counts, no vanilla. Certification stated factually.

## Optional: refresh the landing video
The betterday landing page (`templates/page.betterday.liquid`, Dawn theme) has a UGC video block between the founder and reviews sections (marker `UGC-VIDEO-START`). To swap it: upload the new captioned mp4 to Shopify Files (staged upload → fileCreate, see scratchpad `shopify_upload_ugc.py`), then replace the `src`/`poster` in that block.
