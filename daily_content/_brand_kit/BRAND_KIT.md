# The Power Coffee — Brand Kit (Content Creation)

Everything the carousel/visual generator needs. Drop files in the subfolders, fill the blanks (or just tell me and I'll fill them). This is the single source of truth for how visuals get made.

```
_brand_kit/
├── fonts/         ← brand font files (.ttf / .otf)
├── cutouts/       ← transparent PNGs (product can, scoop, ingredients…)
├── backgrounds/   ← optional background textures/photos
├── references/    ← screenshots of carousel styles to match
└── BRAND_KIT.md   ← this file
```

---

## 1. Colors  (from brand.md — confirm or correct)
| Role | Hex |
|------|-----|
| Deep Espresso (primary bg) | `#171412` |
| Warm Cream (text on dark) | `#F7F0E0` |
| Golden Energy (accent / CTA) | `#D9A633` |
| Matcha Green (ingredient accent) | `#38724D` |
| Dark Charcoal (secondary bg) | `#2E2824` |

_Add any missing (gradients, lighter cream, etc.):_ …

## 2. Fonts

**Current standard (Leo, 2026-06-26): Anton for headlines, Inter for everything else.** This replaces the old Georgia/Arial system.

| Use | Font | Weight | Notes |
|-----|------|--------|-------|
| Headlines (carousel / story / CTA) | **Anton** | Regular | ALL CAPS display; Anton ships heavy/condensed so one weight is enough |
| Sub-headlines / CTA block | **Inter** | SemiBold | Story heads, CTA text |
| Body copy | **Inter** | Regular | Slide body, supporting text |
| Labels / Overlines | **Inter** | Bold | ALL CAPS overlines, slide counter |
| Footer brand name | **Inter** | Bold | "THE POWER COFFEE" |
| Ingredient pills | **Inter** | SemiBold | Letter-spacing +20% |

**Font files (installed in `_brand_kit/fonts/`):**
`Anton-Regular.ttf` · `Inter-Variable.ttf` (variable — pick weight in PIL via `set_variation_by_name("Regular"|"SemiBold"|"Bold")`)

**Renderers use these:** `make_cta_story.py` (done). Any new carousel/story renderer must load Anton + Inter from `_brand_kit/fonts/`, not the old system Georgia/Arial.

**Figma:** Anton + Inter are both free Google Fonts — add them to the Figma file's fonts if not present.

## 3. Cutouts (transparent PNGs)  → drop files in `cutouts/`
| File | What it is | Suggested use |
|------|-----------|---------------|
| `mascot_logo.png` | Animated coffee cup mascot — lightning bolt on top, arms + legs, "THE POWER COFFEE" on cup body. 1560×1560px, RGBA transparent. Sourced from Figma Brand_kit node 14:21. | CTA slides, story covers, hook slide accent. Bottom-right or centered over dark bg. |
| `high_energy_guy.png` | — | — |
| `logo.png` | — | — |

## 4. Design direction
Drop 1+ reference screenshots in `references/`, and/or describe:
- Headline placement: top / centered / bottom — Left
- Product image on every slide, or only hook/CTA? — Both
- Background: solid Deep Espresso / texture / photo — all of them
- Light slides, dark slides, or alternating? — alternating
- Logo placement: use HE (our energy mug) on bottom right
- Slide counter (01/07) yes/no: yes
- Overall vibe (3 words): Energy/ real regular person/ Focus

## 5. Welcome Screens (Video Title Cards)

Created Jun 10, 2026 — Figma file Brand_kit, nodes `17:2` and `17:43`.

| File | Text | Tagline |
|------|------|---------|
| `☕ Welcome — GOOD MORNING.png` | GOOD MORNING | Let's win today. |
| `☕ Welcome — HELLO THERE.png` | HELLO THERE | Ready to fuel up? |

Format: 1080 × 1920 (9:16). Deep Espresso bg, mascot + gold glow, Lora Bold Italic headlines, gold accents, THE POWER COFFEE footer. Use as video intro title cards.

Figma Scripter source: `figma_welcome_screen.js`

---

## 6. Format
- Size: 1080 × 1350 (4:5 portrait) unless you want square 1080×1080 — …
- Slide count: follows `content.md` "Carousel Copy" (7 for jun02)

---

*Once fonts + cutouts + a reference are in, I rebuild `make_carousel.py` to match, regenerate `carousel_1…7.jpg` in the day's folder, show you slides 1/4/7 for approval, then post. This kit also gets mirrored into `brain/references/brand.md` so it's permanent.*
