# CTA Stories — Power Coffee

10 Instagram Stories focused on converting to thepowercoffee.com.
One random story is posted automatically every day at 4am alongside the daily content.

## How to generate the images

1. Open Figma → Plugins → Scripter
2. Paste the full content of `figma_cta_stories.js`
3. Click **Run**
4. 10 story frames appear (1080×1920 px each)
5. Select all frames → Export at 1x as **JPEG**
6. Save them here as: `story1.jpg`, `story2.jpg` ... `story10.jpg`

## Music (optional)

Set `INSTAGRAM_STORY_MUSIC` in `.env` to a song name from Meta's music catalog.
The publisher tries with music first, then retries without if the track is unavailable.

Example:
```
INSTAGRAM_STORY_MUSIC=Good Day Sunshine
```

## Link

`thepowercoffee.com` is baked into every story image at the bottom bar.
The Instagram Graph API does not support link stickers via publishing API —
the URL in the design is the visible reference for viewers.

## Story sequence (funnel arc)

| File | Theme |
|------|-------|
| story1.jpg | Hook — "Still crashing by 10am?" |
| story2.jpg | Problem — coffee peaks in 45 min |
| story3.jpg | Cost — the 10am fog is not normal |
| story4.jpg | Solution — same ritual, better formula |
| story5.jpg | Ingredients — 11, zero fillers |
| story6.jpg | Math — $1.19 a morning |
| story7.jpg | Comparison — $6 latte vs $1.19 scoop |
| story8.jpg | Proof — day 3 / day 5 experience |
| story9.jpg | Simplicity — scoop, stir, done, win |
| story10.jpg | Final CTA — "Try it today" |

## Update 2026-10-09 — rotation is story_NN.jpg, one per day (9am launchd `ctastory`)

`publish_cta_story()` cycles deterministically through every `story_<NN>.jpg` (underscore form only;
`story11.jpg` / `story_amazon.jpg` are not in the pool).

- **story_11 – story_20**: recipe series, one per recipe of the "10 Power Smart Energy Shakes" ebook
  (one scoop each; 12 Mocha and 18 Chocolate Espresso carry an "Extra caffeine" badge). CTA →
  thepowercoffee.com/pages/10shakes. Source: `_source_recipe_stories/build.py` + `recipes.json`
  (HTML → headless Chrome, navy/cream register). Logged in the social-design asset log as series `recipe_story`.
- **_retired/**: pulled from rotation because they state facts that no longer match the site —
  story_06 ($1.19 / $17.90), story_10 ($17.90), story_05 ("5g Pea Protein", unconfirmed),
  story_02 (cortisol / blood-sugar claims about regular coffee), story_08 (day-3/day-5 outcome promises).
  Rebuild with current facts ($18.90, $1.26/serving) before putting any back.
- **story_21 – story_25** (2026-10-10): photo CTA series in the same navy/cream design, using the website's lifestyle photos in original color (afternoon slump, desk focus, street walk, shaker, gym bag). Source: `_source_cta_v2/`. Logged as series `cta_story_v2`. story_25's gym-bag photo is AI-made; its pack label has a garbled "THE" up close, so it's kept small in frame.
