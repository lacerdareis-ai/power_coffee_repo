# "Eisner Stories by Power Coffee" — Weekly Comic Series

**Series name:** Eisner Stories by Power Coffee (renamed 2026-07-28; individual episode titles like "The First Win" stay as episode titles, not the series name — same pattern as a TV show title vs. episode titles). Note: "Eisner" is an actively used trademark in the comics industry (the Eisner Awards) — flagged to Leo, he chose to proceed anyway.

**Format:** 4-slide Instagram carousel, 1080x1350 (4:5)
**Cadence:** Weekly, Sundays — new pillar (P7), doesn't replace P1-P6
**Style:** Black-and-white noir ink comic in the style of Will Eisner's *The Spirit* — heavy ink shadows, dramatic high-contrast lighting, bold expressive brush linework, monochrome only, 1940s urban atmosphere. No photorealism.
**Structure (every episode, 4 beats):** ordinary struggle → the wall/low point → the mascot bursts in → the first win.
**Continuity rule:** the human protagonist is a **different person every episode** (new description each time — don't reuse yesterday's character). The **only recurring character is the mascot**, always drawn in-style (never pasted as the flat vector logo — see rendering notes).

---

## Rendering pipeline (how Episode 1 was made)

1. **Panels 1, 2, 4** (and panel 3's human half): generate via `mcp__claude_ai_Higgsfield__generate_image`, model `recraft_v4_1`, `model_type: "standard"`, `aspect_ratio: "4:5"`, `resolution: "2k"`. Prompt must explicitly state: "Black and white noir comic book illustration in the style of Will Eisner's The Spirit... monochrome black and white only, no color. No text or lettering in the image." Always fully re-describe the protagonist's appearance in every panel's prompt (hair, clothing, build) since each generation is independent — this is what keeps them consistent panel-to-panel within one episode.
2. **Panel 3 (mascot entrance)**: do NOT paste the flat `high_energy_guy.png` logo — it clashes with the ink style. Instead, describe the mascot with enough specific detail to actually match the real brand asset, and let the model illustrate him in-style. As of 2026-07-28, the `mascot_prompt_fragment` in `comic_episodes.json` reads: "the Power Coffee mascot: a stout white ceramic coffee mug character with a curved handle on one side and 'THE POWER COFFEE' printed on its body in bold black block letters, black coffee visible at the rim with a jagged lightning bolt bursting straight up out of it like steam, thick bold black cartoon outline on every edge, an angry determined cartoon face on the front of the mug, two big round white boxing-glove-style mitten hands raised in a fighting stance, simple black tube legs ending in white cartoon sneakers with visible tread lines. Keep his flat bold-outline mascot-logo proportions recognizable, but render him with the same ink cross-hatching, brush texture and dramatic shadow as the rest of the panel..." — the first version was too generic ("anthropomorphic coffee mug with a determined face") and produced a recognizable-as-a-mug-hero but not recognizable-as-*our*-mascot result; naming the specific real features (white body, wordmark, handle, mitten hands, sneaker tread) is what actually got Recraft to reproduce the real logo's likeness. Generate 2 variants and pick the best — this step benefits from a second look before locking.
3. **Compositing**: Python/Pillow script (see `sales_motor/make_carousel.py` for the pattern — fonts from `daily_content/_brand_kit/fonts/`, Anton for display, Inter for body/captions). Each slide: full-bleed panel image, black bar top with series tag "EISNER STORIES · EP. N" + slide counter "N/4" in a gold badge top-right, cream Eisner-style narration caption box (black border, bold black text) top-left of the panel, black footer bar with "@POWERCOFFEE.OFC · SWIPE →" on slides 1-3 and "@POWERCOFFEE.OFC · THEPOWERCOFFEE.COM · NEW EPISODE EVERY WEEK" on slide 4.
4. Output as `carousel_1.jpg`...`carousel_4.jpg` in the day's content folder, same as any other carousel day — flows through the normal qa_critic/review_and_push/publish pipeline.

---

## Episode 1 — "The First Win" (produced 2026-07-28, prototype)

A weary office worker slogs through a rainy Monday, hits a wall at his desk by 2pm, the mascot kicks the door in, he ends the day standing tall on a fire escape at sunrise.

- Panel 1: rain-soaked brownstone steps at dawn, weary man in rumpled white shirt/tie, briefcase, streetlamp. Caption: "ANOTHER CITY. ANOTHER MONDAY. SAME TIRED EYES."
- Panel 2: same man slumped at desk, venetian-blind shadows, clock past 2, empty coffee cup. Caption: "BY TWO O'CLOCK, THE CITY ALREADY HAD HIM BEAT."
- Panel 3: mascot kicks the door open in a blaze of light, papers flying. Caption: "THEN SOMETHING KICKED THE DOOR IN."
- Panel 4: man standing tall on a fire escape at sunrise over the skyline. Caption: "THE FIRST WIN OF THE DAY. EVERY DAY."

Assets: `/private/tmp/.../scratchpad/eisner_strip_prototype/ig_carousel_slide_1-4.jpg` (prototype location, not yet in a dated content folder).

---

## Episode 2 — "The Commute"

Protagonist: a woman in her late 20s, hair in a messy bun, oversized cardigan over a blouse, driving.

- Panel 1: gridlocked traffic at rush hour, she grips the wheel, brake lights stretching to the horizon, rain on the windshield. Caption: "SIX MILES. FORTY MINUTES. STILL NOT MOVING."
- Panel 2: close-up inside the car, she checks her watch, meeting-start time flashing on her phone mounted on the dash, head dropped against the headrest. Caption: "THE MEETING STARTED WITHOUT HER."
- Panel 3: mascot bursts through/over the dashboard in a blaze of light and motion lines, radio-dial energy. Caption: "THEN SOMETHING CUT THROUGH THE NOISE."
- Panel 4: she strides into the office lobby, coat over one arm, chin up, unbothered by the lateness, coworkers glancing up. Caption: "THE FIRST WIN OF THE DAY. EVERY DAY."

## Episode 3 — "The Deadline"

Protagonist: a man in his 40s, glasses, cardigan sleeves pushed up, home office.

- Panel 1: cluttered desk at night, blank page glowing on the monitor, crumpled paper on the floor, a wall clock reading near midnight. Caption: "THE PAGE WAS STILL BLANK AT MIDNIGHT."
- Panel 2: he's slumped forward, head on folded arms next to a graveyard of empty coffee cups, moonlight through the blinds. Caption: "THE DEADLINE DIDN'T CARE HOW TIRED HE WAS."
- Panel 3: mascot bursts through the office door in a shaft of light, sending draft pages flying. Caption: "THEN SOMETHING SHOOK THE ROOM AWAKE."
- Panel 4: sunrise through the window, he leans back in his chair, hand hovering over the send button, exhausted but satisfied. Caption: "THE FIRST WIN OF THE DAY. EVERY DAY."

## Episode 4 — "The Gym"

Protagonist: a heavyset man in his 30s, gym shirt, gym bag, standing outside a gym door at dawn.

- Panel 1: he stands outside the gym entrance in the pre-dawn cold, hand on the door handle, hesitating, breath visible in the air. Caption: "FIVE A.M. THE DOOR NEVER GETS EASIER."
- Panel 2: inside, he sits on a bench, head down, staring at a loaded barbell like it's a mountain. Caption: "SOME MORNINGS THE WEIGHT WINS BEFORE YOU LIFT IT."
- Panel 3: mascot bursts through the gym's swinging door in a blaze of light, dumbbells rattling. Caption: "THEN SOMETHING WALKED IN READY TO WORK."
- Panel 4: he finishes a lift, chalk dust in the air, walking out of the gym into the sunrise, shoulders back. Caption: "THE FIRST WIN OF THE DAY. EVERY DAY."

## Episode 5 — "The Parent"

Protagonist: a woman in her early 30s, hair a mess, robe over pajamas, holding a bottle.

- Panel 1: she paces a dark nursery at 3am, rocking a crying baby, eyes half-closed with exhaustion. Caption: "THE THIRD TIME UP SINCE MIDNIGHT."
- Panel 2: dawn light through the kitchen window, she's slumped at the table, baby finally asleep in the next room, staring blankly at a full pot of coffee she doesn't have energy to pour. Caption: "THE BABY WAS ASLEEP. SHE WASN'T."
- Panel 3: mascot bursts through the kitchen door in a blaze of light, apron strings and dish towels flying. Caption: "THEN SOMETHING SHOWED UP LOUDER THAN THE EXHAUSTION."
- Panel 4: she walks out the front door into the morning sun, coffee in hand, diaper bag on her shoulder, standing a little taller. Caption: "THE FIRST WIN OF THE DAY. EVERY DAY."

## Episode 6 — "The Pitch"

Protagonist: a young man in his late 20s, slightly-too-big suit jacket, tie loosened, in an office hallway.

- Panel 1: he stands alone in a bathroom, rehearsing his pitch in the mirror, sweat on his brow, straightening his tie for the third time. Caption: "HE'D REHEARSED IT FIFTY TIMES. IT STILL DIDN'T FEEL READY."
- Panel 2: he sits in a waiting room chair outside the boardroom, knee bouncing, watching the second hand on the wall clock. Caption: "DOUBT ALWAYS SHOWS UP EARLY."
- Panel 3: mascot bursts through the waiting-room door in a blaze of light, scattering the receptionist's magazines. Caption: "THEN SOMETHING SHOWED UP CONFIDENT ENOUGH FOR BOTH OF THEM."
- Panel 4: he walks out of the boardroom shaking a hand, jacket unbuttoned, grin breaking through, city skyline through the hallway window behind him. Caption: "THE FIRST WIN OF THE DAY. EVERY DAY."

---

## Status: wired in (2026-07-28)

- **Sunday confirmed and live.** `generate_content.py`'s `main()` branches on `weekday == 6` straight to `make_comic_episode.prepare_comic_day()`, bypassing the standard LLM prompt/pillar path entirely. Doesn't touch P1-P6 or any other weekday.
- **Episode roster + rotation state:** `comic_episodes.json` (6 episodes, structured) + `_brand_kit/comic_episode_state.json` (`{"next_episode": N}`, advances after each successful `prepare_comic_day()` call, wraps around after episode 6).
- **`make_comic_episode.py`** does the rest: writes content.md (Instagram Carousel Copy from the episode's captions, cross-promo blurbs for X/LinkedIn/Telegram since those platforms publish every day regardless of pillar, resolved panel prompts embedded at the bottom for whoever generates the art), and composites `panel_1..4.png` → `carousel_1..4.jpg` if the raw panels are already sitting in the folder.
- **Image generation is still manual** — see the credentials note below. If `panel_1-4.png` aren't in the day's folder yet, `compose_slides()` just skips (logs it, doesn't error) and qa_critic's existing hard-check on missing carousel media escalates it via Telegram same as any other day. No silent fallback to something wrong (that's the exact failure mode that caused the July 29 story bug, and this pipeline deliberately doesn't repeat it).
- Standalone re-run: `python3 make_comic_episode.py <day_folder_name> --compose-only` once panels are dropped in.

## Known blocker: Higgsfield direct API is broken

`generate_media.py`'s `hf_generate()` (used for every other day's story/carousel art) hits `platform.higgsfield.ai/v1` and has been returning `401 Invalid credentials` on every credential tried (confirmed 2026-07-28: 3 different key/secret values, all identical 401). This is **also the root cause of the July 29 "jar in the fridge" story bug** — that day's real Higgsfield prompt was never actually used; it silently fell back to a random unrelated stock photo from the Pillow fallback pool. That failure mode is silent and will keep recurring on other days (not just the comic) until this is fixed.

Panels for "The First Win" are generated interactively instead, via the Higgsfield MCP tool available in a Claude session (model `recraft_v4_1`, `model_type: standard`, verified working 2026-07-28 — see Episode 1). Until the direct API is fixed, generating each week's panels is a manual step: open a Claude session, use the resolved prompts embedded in that Sunday's content.md, save as `panel_1.png`..`panel_4.png`, run `--compose-only`.

## First real run (2026-07-28)

Episode 1 fully generated and placed in `daily_content/aug2026_content/aug02_2026/` — panels generated fresh via the actual `resolved_prompts()` output (not reused prototype images), composited via `--compose-only`, committed and pushed. Episode rotation state advanced to `next_episode: 2`. Not yet approved/reviewed through the normal QA gate (that happens naturally the Saturday before, when Aug 2 becomes "tomorrow").

## Still open

- Whether qa_critic's rubric (hook/body/CTA/brand-voice scoring) needs a comic-specific check, or the generic rubric scoring the Caption/Hashtags text is good enough. Untested against a real comic day yet.
- Fixing the underlying Higgsfield REST API credentials (see memory `project_shopify_token`-style — this needs Leo digging into Higgsfield's actual current API docs/support, not more guessing).
