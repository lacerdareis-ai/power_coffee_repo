# Power Coffee — Content for October 2, 2026
**Pillar:** consideration — first AI-generated UGC video, "If I Try" voice | **Day:** Friday | **Format:** Reel

---
## APPROVAL
- [x] APPROVED
<!-- Checked per Leo's direct instruction 2026-09-29: "add captions and schedule to be posted."
     This is the account's FIRST AI-generated UGC video — a new content type, not the existing
     photo-based daily pipeline. Flagging that plainly here in case it needs a second look before
     the 4am job picks it up. -->

---

## INSTAGRAM — Reel (`instagram.mp4`)

30s vertical UGC-style video. AI-generated creator (not a real customer), brand-produced —
demonstrates making Power Coffee on camera, delivering the "If I Try" hook in her own words.
Captions burned in (word-synced, bottom-third). Native audio/voice, generated via the
`ugc-review-video` pipeline (Higgsfield/Seedance 2.5), product pack rendered from the real
product photo as an angle-locked reference.

**Compliance note**: framed throughout as an invitation/curiosity ("I'm finding out," "let's
see"), never a completed positive-outcome claim — no "it worked," no "I felt amazing." This
is brand-produced creative posted from the brand's own account, not passed off as an
independent third-party review.

### Caption
Some days you just have to try the thing you've been wondering about.

One scoop. My regular coffee. Let's see what happens.

Shop: thepowercoffee.com/pages/betterday?utm_source=instagram&utm_medium=organic&utm_campaign=ugc_video_oct26&utm_content=hookvideo_v1

### Hashtags
#powercoffee #ifitry #functionalcoffee #morningroutine #cleanenergy #realtalk

---

## Notes
First execution of a new format for this account: AI-generated UGC talking-head video (built
via the `ugc-review-video` workflow — 2-board/2-clip pipeline, Seedance 2.5, real product photo
as angle-lock reference so the pack renders correctly). Known limitation Leo flagged and
accepted: the on-screen pack isn't a pixel-perfect match to the real product (accepted as
good-enough for this format, unlike the earlier "If I Try" static-photo standard which required
an exact match). Captions added via the workflow's `subtitles.md` step, word-level timed from
the actual rendered audio — verified by viewing sample frames before staging, not just trusting
the pipeline.
