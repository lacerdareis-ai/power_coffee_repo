# "The Operator" — Newsletter Playbook

Started 2026-10-01, inspired by Justin Welsh's content system (reference:
a 6-slide LinkedIn carousel from Blank Partners analyzing his model — see
"The source → the expansion → the asset" below). Leo's goal: use a
LinkedIn newsletter to engage the maximum number of people and grow
Power Coffee, cross-posted to his **personal** LinkedIn and **personal**
Instagram (not the `@powercoffee.ofc` brand account).

## The system this is built on (Justin Welsh's model, not invented here)

1. **A source** — the newsletter is the center of everything. One edition
   a week, written first. The logic: if you can't explain an idea in
   writing with real depth, you don't understand it well enough yet to
   publish it anywhere else.
2. **An expansion** — one newsletter idea becomes 6–12 platform posts,
   each adapted to how that platform is actually consumed, so the same
   idea reaches people who give it very different amounts of attention.
3. **An asset** — the content keeps leading people back to the product,
   because the product teaches exactly what the content teaches. Reading
   the posts over time **is** seeing how the system works.
4. **The content Pareto** — 80% of results come from 20% of posts. Track
   what actually resonates, and let that steer what gets written next,
   not a content calendar decided in advance.

Four hours a week, total, is the whole claimed production budget for this
system at Justin Welsh's scale. That's the discipline worth protecting:
**the newsletter is cheap to produce content FROM, not another thing to
produce.**

## Name, cadence, platforms

- **Name:** The Operator.
- **Cadence, locked 2026-10-01:** 1 newsletter edition/week + **5**
  expansion posts/week, every post going to **both** LinkedIn and
  Instagram (not a LinkedIn-only post occasionally adapted — every
  scheduled post gets an IG treatment by design now).
- **Primary platform:** LinkedIn Newsletter, published under **Leo's
  personal profile** (LinkedIn newsletters are a personal-profile feature,
  not something `@powercoffee.ofc` — a company page — can run the same
  way). This is deliberate: Justin Welsh's whole model is a *person*
  people choose to follow, not a brand feed.
- **Expansion posts:** 5 scheduled/week, LinkedIn feed posts under Leo's
  personal profile, each one a single angle pulled from that week's
  edition — not a summary of it. Issues can write more than 5 (banked for
  a future week) but only 5 go out per cycle.
- **Cross-post:** every scheduled post gets its own Instagram treatment —
  **@leolacerdaofc** — scoped per-post (quote card, carousel, caption-led
  photo), never a screenshot of the LinkedIn text.
- **Weekly rhythm:** Monday = newsletter edition. Tuesday–Saturday = the 5
  expansion posts, one/day. Sunday = no Operator content.
- **2026-10-01 — merged into the daily pipeline, by Leo's direct call.**
  The Operator is now THE model for Power Coffee's LinkedIn content, not a
  separate stream. `generate_content.py` is patched
  (`_apply_operator_linkedin_override`, called right after the LLM
  generation + sanitizer step): for any date with an entry in
  `the_operator/schedule.json`, it replaces that day's generated
  `## LINKEDIN` section with the scheduled Operator content before the
  file is saved. A date with no schedule entry falls through to the old
  pillar-rotation behavior untouched — this only ever touches dates
  explicitly scheduled into The Operator.
  **Maintenance requirement**: `schedule.json` has to be kept extended
  (currently populated through Oct 17) as new issues/posts are written,
  or LinkedIn silently reverts to the old pillar-rotation content past
  that date. Not self-sustaining yet — there's no automatic "write next
  week's Operator content" step, only the override mechanism.

### First five cycles, scheduled

| Week | Mon (newsletter) | Tue | Wed | Thu | Fri | Sat |
|---|---|---|---|---|---|---|
| 1 (operator) | **Oct 5** — Issue 1 | Oct 6 — Post 2 | Oct 7 — Post 4 | Oct 8 — Post 6 | Oct 9 — Post 1 | Oct 10 — Post 7 |
| 2 (performance) | **Oct 12** — Issue 2 | Oct 13 — Post 2 | Oct 14 — Post 3 | Oct 15 — Post 4 | Oct 16 — Post 5 | Oct 17 — Post 6 |
| 3 (operator) | **Oct 19** — Issue 3 | Oct 20 — Post 1 | Oct 21 — Post 2 | Oct 22 — Post 3 | Oct 23 — Post 4 | Oct 24 — Post 5 |
| 4 (performance) | **Oct 26** — Issue 4 | Oct 27 — Post 1 | Oct 28 — Post 2 | Oct 29 — Post 3 | Oct 30 — Post 4 | Oct 31 — Post 5 |
| 5 (operator) | **Nov 2** — Issue 5 | Nov 3 — Post 1 | Nov 4 — Post 2 | Nov 5 — Post 3 | Nov 6 — Post 4 | Nov 7 — Post 5 |

Issue 5 is grounded in the real 2026-09-30 auto-pipeline overwrite
incident (see [[project_power_coffee_publish_pipeline_notes]] /
`generate_content.py`'s approval/staged-media guard) — genuinely new
material again, an internal-tooling story rather than a repeat of Issue
1's photo audit or Issue 3's email-list decision. **This is the first
Issue scheduled into a month that doesn't have day folders yet** — Nov
2-7 haven't been generated by `generate_content.py` at all, so there was
nothing to retroactively patch. This will be the first real live test of
the forward-looking override: when the 5am job eventually generates
these days fresh, `_apply_operator_linkedin_override()` should apply
automatically with no manual intervention — worth spot-checking once
those days actually get generated, to confirm the live path works as
designed and not just in the isolated test calls run so far.

Post numbers refer to each issue's own expansion-posts file. Issue 3 is
grounded in the real email-list deliverability decision (490 new
addresses, 488 added after flagging the aggregate-reputation risk, list
now 8,498 — see `email_list.txt` / the memory file on it) — genuinely
new, unused material, not a rehash of Issue 1's photo-audit incident.
Issue 4 is grounded in the certified L-theanine + caffeine mechanism
(brand.md's real citation — Haskell et al. 2008 — on the combination
producing a steadier, longer-held, less-crashy curve than caffeine
alone), applied as an operator pacing lesson via an illustrative
three-launches-in-one-week scenario — same device Issue 2 used (a
representative founder scenario carrying a real, certified mechanism),
not a claim that this specific incident is independently logged
elsewhere the way Issue 1/3's operational incidents are.

**LinkedIn posting mechanism, resolved**: as of the 2026-10-01 merge (see
above), all scheduled entries ride `publisher.py`'s existing automated
daily LinkedIn post via `schedule.json` + `generate_content.py`'s
override — no separate trigger needed for expansion posts. Newsletter
*editions* still need manual publish through LinkedIn's own composer (no
API for Newsletter articles). Instagram side (`@leolacerdaofc`) has no
automated posting path confirmed at all — moot for now since Leo is
posting personal Instagram manually.

`schedule.json` needs manual extension for Issue 6 onward (next:
performance week, Nov 9 edition) or LinkedIn reverts to the old
pillar-rotation content past Nov 7.

**2026-10-01 — performance-tracking process reviewed.** `asset_log.py`
already has the full mechanism built (`perf` to record saves/shares/
clicks/sales against a logged asset, `winners` to surface the
best-performing hook types/layouts/mascot poses over the last N days) —
this is the actual "content Pareto" infrastructure the playbook's
Tracking section calls for. It is not broken, but it has **zero real
data points recorded** as of this review: every one of the 41 logged
assets (including all 20 Operator entries) shows `performance: null`.
Checked why — there's real Instagram analytics flowing into
`04-Analytics/instagram-analytics-may2026.csv` (actively updated,
168 rows through 2026-09-25), but asset-level logging into
`asset_log.json` only started 2026-09-28, three days after that CSV's
latest row — so there is currently **no date overlap at all** between
"posts with real engagement data" and "posts logged in the system that's
supposed to track them." This isn't a pipeline bug, it's a timing gap:
real numbers need to be recorded via `perf` once the Sep 28+ assets have
had time to accumulate engagement, and nobody has done that yet because
the discipline is brand new. **Separately confirmed**: no LinkedIn scope
anywhere in `power_coffee_bot`'s code grants analytics access, and
LinkedIn's public API has no engagement-read endpoint for personal-profile
posts at all (only Organization-page analytics exist, via the Marketing
Developer Platform, which doesn't apply here) — so LinkedIn-side Pareto
tracking will always be a manual step: Leo reading his own post analytics
panel and reporting numbers back, there's no automatable path. **Action,
not yet taken**: once the earliest Oct assets have been live ~1-2 weeks,
record real `perf` numbers against them and run `winners` for the first
time — that's the step that turns this from "built but empty" into an
actual feedback loop.

## The alternating-week structure, and why it won't feel like two newsletters

Leo's call: alternate between two territories —

- **Operator weeks (odd — starts Week 1):** Building Power Coffee in
  public. Supply chain, formula decisions, manufacturing reality, real
  numbers, real mistakes. Power Coffee is the case study, not the ad —
  this is the deeper written version of the same voice already running in
  the Founder Vlog Reels (Ep. 13, Ep. 14...). Reuse real stories from
  actually operating the account; don't invent generic "founder journey"
  content when true, specific incidents exist.
- **Performance weeks (even):** High-performance focus/energy content for
  operators and founders, in the brand's own established "high-performance
  mentor" archetype (`config.json`'s `brand_voice`). Power Coffee shows up
  as the tool that supports the lesson, not the subject of the lesson.
  Broader audience than operator weeks; less direct brand tie-in, more
  top-of-funnel reach.

**The real risk with alternating topics**: it can read as two different
newsletters sharing a name. Fixed with a skeleton that stays fixed
regardless of which week's topic runs:

1. **Same hook discipline every week** — a specific scene, number, or
   named problem in the first two lines. Never a generic claim. (Same
   rule this account already applies everywhere else — see
   `social-media-design/SKILL.md`'s "genericness is the single most common
   reason a strong idea underperforms.")
2. **Same closing structure** — every edition ends with an explicit
   **"Expansion seeds"** section: 2–4 single-sentence angles pulled from
   that edition, each one the literal seed for one of that week's LinkedIn
   posts. This is what makes the "6–12 posts from one idea" step
   systematic instead of improvised after the fact.
3. **Same sign-off** — one fixed line that's always "The Operator,"
   regardless of topic, so the identity anchors even when the territory
   shifts. Draft: *"— Leo, building Power Coffee one real decision at a
   time."*
4. **Same day of week** — pick one and hold it, so following it becomes a
   habit, not a surprise.

## Expansion pipeline (the actual production step)

After an edition is written:

1. Pull its "Expansion seeds" section — 2–4 named angles.
2. For each seed, write 2–4 standalone LinkedIn posts developing that one
   angle on its own (a post should never require having read the
   newsletter to land — same "cold open every piece" rule as the rest of
   this account's content). Target 6–12 total posts for the week.
3. For each post, decide separately whether it's worth adapting for
   Instagram (not every LinkedIn post needs an Instagram twin) — if yes,
   give it its own visual treatment, not a screenshot of the text post.
4. Log each edition + its expansion posts (see Tracking below) so the
   content Pareto can actually be measured, not guessed at.

## Tracking — so the content Pareto is real, not a vibe

Extend `asset_log.py`'s pattern to this content type: log each newsletter
edition and each expansion post with a `series: the_operator` tag and a
`week_type: operator | performance` field, so engagement can later be
compared within and across week-types once real performance data exists.
No analytics baseline exists yet for LinkedIn specifically in this
account's tooling (same caveat as the October UTM-tracking note) — this
needs a real check of what LinkedIn analytics access actually exists
before the Pareto-tracking step can run on real numbers instead of
impressions eyeballed by hand.

## Compliance note

Same rules as everywhere else in this account: `compliance_check.py`
applies to every mention of Power Coffee in any edition or expansion
post, hedged claims only, every product fact sourced from `config.json`/
`brand.md`, never a disease or guarantee claim. Operator-week stories
about real mistakes (a fabricated AI image, a pipeline bug) are
compliance-safe by nature — they're operational transparency, not product
claims — but still get the same fact-check pass on anything that touches
the product itself.

## Issue #1 — status

Built 2026-10-01 as the first Operator-week edition, grounded in real,
verified incidents from this account's own recent operations (the
fabricated-label-image audit, the wrong-pack catch-and-fix, the
auto-pipeline overwrite bug) rather than invented founder-journey content.
See `the_operator/issue_01.md`. Expansion posts built alongside it — see
`the_operator/issue_01_expansion_posts.md`.

## Issue #3 — status

Built 2026-10-01, same day as the schedule.json extension past Issue 2.
Operator week, grounded in the real email-list deliverability decision
(2026-09-29: ~490 new addresses offered, flagged the aggregate-reputation
risk before adding anything, Leo confirmed, 488 added after excluding 2
unambiguous technical errors, list now 8,498). See `the_operator/issue_03.md`
and `the_operator/issue_03_expansion_posts.md`. Compliance-checked PASS —
no product claims at all in this issue, purely an operations story.
Scheduled live Oct 19–24 in `schedule.json` and directly patched into the
6 already-existing October day files (1 insert for `oct20_2026`, which had
no prior `## LINKEDIN` section; 5 replaces for the rest) — every file
independently verified by reading it, not just trusting the patch
script's own output, after the Issue 1/2 retroactive-patch date-slicing
bug made that the standing verification bar for this kind of edit.
