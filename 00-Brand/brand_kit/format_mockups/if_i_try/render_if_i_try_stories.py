#!/usr/bin/env python3
"""
"If I Try" — Instagram Stories versions of the 3 feed posts (2026-09-29).
Reformatted for the 9:16 Stories canvas instead of just letterboxing the
4:5 feed image.

Safe-zone numbers per social-media-design/references/platform-specs.md
(Meta's unified Stories/Reels safe zone): keep essential content out of the
top ~14% (~270px of 1920) and bottom ~20-35% (~400-670px) and ~6% each side
(~65px). Used conservative bottom clearance (650px) since these are static
posts with no way to know exactly where a given viewer's UI chrome sits.

**2026-09-29 revision — real photo color, not the Fuel Check duotone.**
Same call as the feed version (`render_if_i_try.py`): background is the
real photo, full-bleed, no navy/cream tint. Replaced the halftone-duotone
pass with a bottom gradient scrim (`bottom_scrim()`) sized to the fixed
pixel anchors this layout already uses (accent line / CTA / handle), so
that block stays legible over whatever color the photo actually is there.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "fuel_check"))
from render_fuel_check import (
    MARGIN, NAVY_DEEP, BORDER_BLUE, CREAM, CREAM_DIM, GOLD,
    anton, inter, tracked_text, cover_fit, measure_stack, draw_stack,
)
from PIL import Image, ImageDraw

IMGS = "/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/images"
OUT = HERE

SW, SH = 1080, 1920
BORDER_INSET = 44
TOP_SAFE = 270
BOTTOM_SAFE = SH - 650  # content must stay above this y
SIDE_SAFE = 64

EYEBROW = "IF I TRY:"


def bottom_scrim(img, w, h, start_y, max_alpha=210, color=NAVY_DEEP):
    """Soft dark-navy gradient rising from the bottom edge, transparent at
    start_y and near-opaque at the very bottom — same technique as the feed
    script's bottom_scrim(), here sized against this layout's fixed pixel
    anchors (accent line / CTA / handle) rather than a height fraction."""
    grad = Image.new("L", (1, h), 0)
    for y in range(start_y, h):
        t = (y - start_y) / max(1, (h - start_y))
        grad.putpixel((0, y), int(max_alpha * t))
    alpha = grad.resize((w, h))
    overlay = Image.new("RGBA", (w, h), color + (255,))
    overlay.putalpha(alpha)
    base = img.convert("RGBA")
    base.alpha_composite(overlay)
    return base.convert("RGB")


def make_story(name, photo_file, headline_lines, payoff_line, eyebrow=EYEBROW):
    photo = Image.open(f"{IMGS}/{photo_file}").convert("RGB")
    photo = cover_fit(photo, SW, SH)
    # scrim starts ~80px above the accent line (cta_y - 30) so the fade is
    # gentle rather than a hard edge
    img = bottom_scrim(photo, SW, SH, start_y=(BOTTOM_SAFE - 130) - 110)
    d = ImageDraw.Draw(img)

    d.rectangle([BORDER_INSET, BORDER_INSET, SW - BORDER_INSET, SH - BORDER_INSET], outline=CREAM, width=4)

    # header card — same eyebrow/headline/payoff stack as feed, boxed with a
    # real side margin (not full-bleed) since Stories' side safe zone is
    # tighter than feed's
    block_x0, block_y0, block_x1 = SIDE_SAFE, TOP_SAFE + 40, SW - SIDE_SAFE
    ef = inter(30, "Bold")
    eyebrow_bbox = ef.getbbox(eyebrow)
    eyebrow_h = eyebrow_bbox[3] - eyebrow_bbox[1]

    lines = list(headline_lines) + [(payoff_line, inter(28, "SemiBold"), CREAM_DIM, 0)]
    block_h = 44 + eyebrow_h + 24 + measure_stack([(t, f, g) for t, f, _, g in lines]) + 44
    d.rectangle([block_x0, block_y0, block_x1, block_y0 + block_h], fill=NAVY_DEEP)
    d.rectangle([block_x0, block_y0, block_x1, block_y0 + block_h], outline=BORDER_BLUE, width=3)

    text_x = block_x0 + (MARGIN - SIDE_SAFE) if MARGIN > SIDE_SAFE else block_x0 + 44
    ey = block_y0 + 40
    tracked_text(d, (text_x, ey), eyebrow, ef, GOLD, tracking=4)
    cursor_y = ey + eyebrow_h + 24
    cursor_y = draw_stack(d, text_x, cursor_y, lines)
    block_bottom = block_y0 + block_h

    # bottom CTA + handle — both well clear of BOTTOM_SAFE
    cta_f = inter(32, "Bold")
    cta_text = "SHOP THEPOWERCOFFEE.COM"
    cta_w = d.textlength(cta_text, font=cta_f)
    cta_y = BOTTOM_SAFE - 130
    d.line([(SW / 2 - 120, cta_y - 30), (SW / 2 + 120, cta_y - 30)], fill=BORDER_BLUE, width=2)
    d.text(((SW - cta_w) / 2, cta_y), cta_text, font=cta_f, fill=GOLD)

    hf2 = inter(28, "SemiBold")
    handle = "@POWERCOFFEE.OFC"
    hw = d.textlength(handle, font=hf2)
    d.text(((SW - hw) / 2, cta_y + 52), handle, font=hf2, fill=CREAM_DIM)

    img.save(f"{OUT}/{name}.jpg", quality=95)
    print(f"{name} saved, block_bottom={block_bottom} (limit {BOTTOM_SAFE - 160}), "
          f"cta_bottom={cta_y + 52 + 34} (limit {BOTTOM_SAFE})")


if __name__ == "__main__":
    make_story(
        "story_dunkin",
        "img_13_power.png",
        [("ONE SCOOP IN MY", anton(78), CREAM, 12),
         ("DUNKIN' RUN.", anton(78), CREAM, 20)],
        "This is what 3pm can look like instead.",
    )
    make_story(
        "story_gym",
        "img_14_power.png",
        [("ONE SCOOP BEFORE MY", anton(66), CREAM, 12),
         ("GYM BAG'S EVEN PACKED.", anton(66), CREAM, 20)],
        "This is what showing up early can look like.",
    )
    make_story(
        "story_secondcup",
        "img_16_power.png",
        [("ONE SCOOP INSTEAD OF", anton(70), CREAM, 12),
         ("MY SECOND CUP.", anton(70), CREAM, 20)],
        "This is what a calm afternoon can look like.",
    )
    make_story(
        "story_schoolmorning",
        "img_24_power.png",
        [("ONE SCOOP BEFORE THE", anton(64), CREAM, 12),
         ("SCHOOL-DAY SCRAMBLE.", anton(64), CREAM, 20)],
        "This is what keeping up before 8am can look like.",
    )
    make_story(
        "story_outthedoor",
        "img_12_power.png",
        [("ONE SCOOP, SHAKEN", anton(74), CREAM, 12),
         ("ON MY WAY OUT.", anton(74), CREAM, 20)],
        "This is what not skipping breakfast can look like.",
    )
    make_story(
        "story_bigmeeting",
        "img_28_power.png",
        [("ONE SCOOP BEFORE I", anton(70), CREAM, 12),
         ("WALK INTO THAT ROOM.", anton(70), CREAM, 20)],
        "This is what walking in like I mean it can look like.",
    )
    make_story(
        "story_stilllosing",
        "img_09_power.png",
        [("THREE COFFEES IN.", anton(74), CREAM, 12),
         ("STILL LOSING 2PM.", anton(74), CREAM, 20)],
        "Tomorrow, one scoop. Let's see what changes.",
        eyebrow="SOUND FAMILIAR?",
    )
    make_story(
        "story_simplicity",
        "img_04_power.png",
        [("ONE SCOOP.", anton(84), CREAM, 12),
         ("THAT'S REALLY IT.", anton(84), CREAM, 20)],
        "This is what keeping it simple can look like.",
    )
