# "If I Try" — Campaign Playbook

Started 2026-09-29, Leo's concept, renamed same day (Leo's call: first person —
"If I Try" — invites the reader to complete the thought themselves, rather than
being told "you"). Companion to the Fuel Check reference-carousel series
(`_brand_kit/format_mockups/fuel_check/`) — same navy/cream Vintage Athletic
brand system, different register: Fuel Check proves a claim with data;
**If I Try makes the reader imagine their own life changing**, one small,
specific, relatable action at a time.

## The idea

Every post poses a small, concrete "what if" — not "try our coffee," but
"what if I added one scoop to the thing I'm already doing today" — and answers
it with a real photo of the payoff: someone in the energized/focused state
that small change made possible. The reader isn't sold a product; they're
shown a version of their own day.

**Why this is compliant by construction, not despite the compliance rules**:
framing every post as a question/invitation ("if I try...") rather than an
assertion ("you will feel...") means the claim is never stated as fact — run
through `compliance_check.py` and it passes clean, including the payoff
line's "can look like" (hedged, not "will look like"). Keep every future
execution in this format: **pose the scenario, hedge the payoff, let the
photo do the emotional work.**

## Template (`render_if_i_try.py`)

- Full-bleed real photo, **real color** (not Fuel Check's navy/cream
  halftone-duotone — Leo's call, 2026-09-29: this series is meant to read
  as an actual moment from an actual life, and the duotone treatment was
  hiding that). A bottom gradient scrim (`bottom_scrim()`) keeps the handle
  legible over whatever color the specific photo happens to be. Still uses
  `measure_stack()`/`draw_stack()` from `render_fuel_check.py` for the
  header card — same "measure, don't guess" text-stacking discipline.
- Fixed eyebrow tag: **"IF I TRY:"** in gold — this is the series identity,
  keep it on every post, unchanged.
- Headline: the specific scenario, 2 short lines, first person, e.g. "ONE
  SCOOP IN MY DUNKIN' RUN."
- Payoff line: one hedged sentence naming what the photo shows, e.g. "This
  is what 3pm can look like instead." Never drop the hedge ("can," not
  "will").
- No mascot on most executions — this is closer to real-life/proof content
  than a hook/mascot-led format (see `mascot.md`'s "absent on proof posts"
  rule). Reserve the mascot for maybe 1 in 4-5 of these, if at all.
- Single image, not a carousel — the whole point is one relatable moment,
  answered immediately, not a multi-slide build-up.

## Built so far

| Scenario | Photo | Persona |
|---|---|---|
| One scoop in my Dunkin' run | img_13 (focused at work) | professional/office |
| One scoop before my gym bag's even packed | img_14 (gym bag, dawn) | fitness |
| One scoop instead of my second cup | img_16 (calm morning ritual) | general/ritual |

**2026-09-29 edit note**: Leo asked for two scenario tweaks alongside the
rename. "Before school" → "before work" — noted below, not yet built (no
clean unused photo; img_13 is already spoken for by the Dunkin' scenario).
"After workout" → "before workout" — this collapses onto the *already-built*
gym post above (both become a before-workout scenario), so it's folded in
here rather than built as a near-duplicate fourth post. Flagged to Leo;
revisit if he wants it as its own distinct post instead.

## Queued, needs real photography before building

Leo's own example — **"a mom with energy after leaving kids at school"** —
doesn't have a match in the verified-clean photo pool (`img_04, 09, 12, 13,
14, 16, 24, 28` — see the fabricated-label-images project memory for why
that pool is this small). Forcing a mismatched stock-ish photo onto this
scenario would undercut the whole format's promise of showing something
real. **This needs an actual photo** — a parent, kids, a school drop-off (or
now: a commute/desk "before work") moment — before it can be built, not an
AI-generated substitute (same rule as everywhere else in this project's
photo pipeline).

Other scenarios worth planning once more real photography exists: before a
big presentation, on a road trip, the first hour of a new job, studying for
an exam.

## Distribution note

Single-image format fits Instagram feed, Threads/X, and — per the funnel-
and-hooks.md platform note — likely needs its OWN framing for LinkedIn (a
"what if" invitation reads differently to a founder/operator audience than
a consumer one; don't just resize this straight onto LinkedIn without
rethinking the scenario for that audience).

## Feed + Stories, staged (2026-09-29)

All 3 posts now have a matching Instagram Story (`render_if_i_try_stories.py`,
same folder) — same copy and photo, reformatted for the 9:16 canvas rather
than just letterboxing the 4:5 feed image. Header card clear of the top
~270px, CTA + handle clear of the bottom ~650px (Meta's unified Stories/
Reels safe zone, see `social-media-design/references/platform-specs.md`).

**Real bug caught building these**: `render_fuel_check.py`'s
`halftone_duotone()` reads the module-level `W, H` globals internally
instead of taking them as parameters, so it can't be reused as-is against
a taller canvas — it would silently sample the dot pattern at the wrong
size. Re-implemented as `halftone_duotone_wh(im, w, h, ...)` with identical
logic, parameterized. Worth fixing at the source in `render_fuel_check.py`
itself if a third format ever needs this treatment.

Staged into real day folders as the actual publish pipeline expects it —
`instagram.jpg` (feed) + `story.jpg` (Story) dropped directly into each day
folder, which `publisher.py` posts together automatically (it explicitly
posts a standalone `story.jpg` alongside the main post, not just the
carousel/feed asset):

| Date | Day folder | Scenario |
|---|---|---|
| 2026-10-01 | `oct2026_content/oct01_2026/` | Dunkin' run — **approved by Leo directly in content.md** |
| 2026-10-03 | `oct2026_content/oct03_2026/` | Gym bag — **approved** |
| 2026-10-06 | `oct2026_content/oct06_2026/` | Second cup — **approved** |
| 2026-10-08 | `oct2026_content/oct08_2026/` | School-day scramble — **rebuilt with img_29 (new, no-pack-in-frame), approved** |
| 2026-10-13 | `oct2026_content/oct13_2026/` | Out the door (img_12) |
| 2026-10-15 | `oct2026_content/oct15_2026/` | Before that meeting (img_28) |
| 2026-10-20 | `oct2026_content/oct20_2026/` | "Sound familiar?" — problem-variant, img_09, no answer photo |
| 2026-10-27 | `oct2026_content/oct27_2026/` | Simplicity beat (img_04) — last unused photo in the pool |

## 2026-09-29 — October build, goal-tied, photo pool exhausted

Leo: "Create all content for october/26 using this idea. Set your goal in
100 sales." Built the remaining 5 executions the verified-clean photo pool
allows (img_24, img_12, img_28, img_09, img_04) — bringing the series to
all 8 photos used, 8 posts total. Every CTA link now carries UTM tracking
(`utm_campaign=ifitry_oct26`) so the 100-sale goal is actually measurable
against real analytics, not eyeballed. Full calendar, sales-goal math, and
what's still open written up as a living doc:
https://claude.ai/artifact/Hce9Ks4qaq9tHCrywzfnR9

**Real ceiling reached**: all 8 verified-clean photos are now spent. The
account's own uniqueness rule (`asset_log.py`) blocks reusing any of them
again within this series — so this format cannot cover the rest of October
without either falling back to the account's other pillars (Fuel Check,
founder Reels — both pre-existing, not rebuilt here) or new lifestyle
photography. Flagged in the doc rather than silently padding the calendar
with weaker content.

**2026-09-29, same day, later — Oct 8 pulled, then rebuilt and reapproved.**
Leo caught it after approving: `img_24`'s on-pack design doesn't match the
real product (wrong pouch, wrong layout — legible but wrong, a defect
class the original 27-image audit's "is the text garbled" method never
checked for). Two crop attempts to frame the bad pack out of the shot both
failed. Pulled the post, demoted `img_24` from the verified-clean pool.

Leo then asked for a new image. Generated one (`img_29_power.png`) with
the packaging problem designed out from the start — same scenario, prompt
explicitly excluded any coffee bag/label/logo from frame, so there was
nothing left to render wrong. Verified the actual rendered feed + Story
pixels before staging (not just the raw generation). Rebuilt Oct 8 with
it, restaged the day folder, re-approved. **Pool is now 8 again**
(`img_04, 09, 12, 13, 14, 16, 28, 29`), with `img_29` in the same
"no product visible" category as the other persona shots this pool
already keeps for exactly this reason.

Two deliberate format variants introduced to make honest use of photos
that don't fit the standard scenario template: `post_stilllosing` (img_09,
a stressed "before" photo — different eyebrow "SOUND FAMILIAR?", the
invitation carries the payoff since no answer photo exists) and
`post_simplicity` (img_04, a macro product shot — leans into the object
itself rather than forcing a life scene onto a close-up).

Each day's `content.md` follows the real pipeline format (`- [ ] APPROVED`
gate, checked by `check_approval.py` before the 4am job) — Instagram-only
for these three, no X/LinkedIn/Telegram/Reels content, consistent with this
campaign's own distribution note above.
