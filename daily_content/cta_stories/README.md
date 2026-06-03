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
