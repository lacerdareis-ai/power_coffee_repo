# Power Coffee — Content for October 9, 2026
**Pillar:** consideration — AI-generated UGC video, office/iced-latte scenario | **Day:** Friday | **Format:** Reel

---
## APPROVAL
- [x] APPROVED
<!-- Checked 2026-09-29 per Leo: "add both videos for october." -->

---

## INSTAGRAM — Reel (`instagram.mp4`)

30s vertical UGC-style video, second execution of the AI-generated UGC format (see Oct 2 for
the first). AI-generated male creator (not a real customer), brand-produced — office scenario:
sees the pack in his bag, opens it, scoops into an iced latte at his desk, drinks it, closes
with an invitation to try it. Product pack rendered from the real product photo as an
angle-locked reference (confirmed correct across every slot before rendering to video).
Captions burned in, word-synced against the authored script — verified via the pipeline's own
QA gate (word-for-word match against `script.txt`), not just visually spot-checked.

**Real issue caught and fixed during build**: the first render of the second half (scooping →
drinking → close) had a genuine audio glitch — repeated phrase + a stretch of garbled nonsense
speech mid-clip, caught by the caption pipeline's transcript-vs-script QA check, not by the
visual frame QA that caught the Oct 2 video's issues. Confirmed with Leo before spending
credits on a re-render. Regenerated, re-verified the transcript matched the script exactly
before proceeding to caption/assemble.

**Compliance note**: framed as an ongoing personal account, always hedged ("this is how it's
been going for me"), never a flat "it worked" claim — no medical/before-after language. Brand-
produced creative posted from the brand's own account, not passed off as an independent
third-party review.

### Caption
Some things you just have to try to know.

One scoop in the iced latte. Same drink, same order — this is what a few weeks of trying looks like.

Shop: thepowercoffee.com/pages/betterday?utm_source=instagram&utm_medium=organic&utm_campaign=ugc_video_oct26&utm_content=hookvideo_v2_office

### Hashtags
#powercoffee #ifitry #functionalcoffee #icedlatte #officelife #cleanenergy #realtalk

---

## Notes
Second AI-generated UGC video (`ugc-review-video` pipeline, Seedance 2.5, 2-board/2-clip). Same
real-product-photo angle-lock approach as Oct 2's video — pack reads correctly throughout,
verified by eye on both boards before proceeding to video. Unlike Oct 2, this one surfaced (and
required fixing) a real audio-generation defect — worth remembering as a pattern: sample-frame
QA alone doesn't catch audio glitches; the caption pipeline's transcript match is a genuine
second QA layer, not just a captioning step.
