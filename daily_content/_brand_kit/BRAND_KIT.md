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

## 2. Fonts  → drop files in `fonts/`
| Use | Font file | Weight |
|-----|-----------|--------|
| Headlines | … | … |
| Body | … | … |
| Accent/labels (optional) | … | … |

## 3. Cutouts (transparent PNGs)  → drop files in `cutouts/`
List each image + how to use it:
- `…png` — what it is — where it goes (e.g. product can → bottom-right of CTA slide)
- …

## 4. Design direction
Drop 1+ reference screenshots in `references/`, and/or describe:
- Headline placement: top / centered / bottom — …
- Product image on every slide, or only hook/CTA? — …
- Background: solid Deep Espresso / texture / photo — …
- Light slides, dark slides, or alternating? — …
- Logo placement: …
- Slide counter (01/07) yes/no: …
- Overall vibe (3 words): …

## 5. Format
- Size: 1080 × 1350 (4:5 portrait) unless you want square 1080×1080 — …
- Slide count: follows `content.md` "Carousel Copy" (7 for jun02)

---

*Once fonts + cutouts + a reference are in, I rebuild `make_carousel.py` to match, regenerate `carousel_1…7.jpg` in the day's folder, show you slides 1/4/7 for approval, then post. This kit also gets mirrored into `brain/references/brand.md` so it's permanent.*
