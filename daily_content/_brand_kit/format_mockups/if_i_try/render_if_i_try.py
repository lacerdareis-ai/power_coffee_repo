#!/usr/bin/env python3
"""
"If I Try" — renamed 2026-09-29 from "If You Try" (Leo's call — first
person invites the reader to complete the thought themselves, rather than
being told "you"). Structure unchanged: a relatable everyday scenario posed
as a question/invitation, answered by a real payoff photo — never a hard
guarantee. Compliance-safe by construction: an invitation to find out, not
an assertion of a result. See growth_playbooks/if_i_try_campaign.md.

Single-image posts (the photo IS the answer), not carousels — different
register from Fuel Check but same brand frame (cream border, navy header
card) for account-level consistency. Mascot left OUT of most of these
deliberately: this is closer to real-life/proof content than a hook/
mascot-led format (see mascot.md's "absent on proof posts" rule).

**2026-09-29 revision — real photo color, not the Fuel Check duotone.**
Leo's call: "If I Try" is meant to read as a real moment from a real life,
so the background is now the photo's actual color, full-bleed — not the
navy/cream halftone treatment Fuel Check uses for its poster-reference
aesthetic. That treatment stays exactly as-is on Fuel Check; this is a
deliberate divergence for this series only, not a system-wide change.
Added a bottom gradient scrim (`bottom_scrim()`) so the handle stays
legible regardless of what color the specific photo happens to be at that
edge — real photos vary in a way a flat navy/cream canvas never did.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "fuel_check"))
from render_fuel_check import (
    W, H, MARGIN, BORDER_INSET, NAVY, NAVY_DEEP, BORDER_BLUE, CREAM,
    CREAM_DIM, GOLD, anton, inter, tracked_text, cover_fit,
    measure_stack, draw_stack,
)
from PIL import Image, ImageDraw

IMGS = "/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/images"
OUT = HERE

EYEBROW = "IF I TRY:"


def bottom_scrim(img, w, h, start_frac=0.80, max_alpha=190, color=NAVY_DEEP):
    """Soft dark-navy gradient rising from the bottom edge, transparent at
    start_frac*h and near-opaque at the very bottom — keeps bottom text
    legible over a real (uncontrolled-color) photo without flattening the
    whole image the way a full-frame tint would."""
    grad = Image.new("L", (1, h), 0)
    start_y = int(h * start_frac)
    for y in range(start_y, h):
        t = (y - start_y) / max(1, (h - start_y))
        grad.putpixel((0, y), int(max_alpha * t))
    alpha = grad.resize((w, h))
    overlay = Image.new("RGBA", (w, h), color + (255,))
    overlay.putalpha(alpha)
    base = img.convert("RGBA")
    base.alpha_composite(overlay)
    return base.convert("RGB")


def make_post(name, photo_file, headline_lines, payoff_line, eyebrow=EYEBROW):
    photo = Image.open(f"{IMGS}/{photo_file}").convert("RGB")
    photo = cover_fit(photo, W, H)
    img = bottom_scrim(photo, W, H)
    d = ImageDraw.Draw(img)

    d.rectangle([BORDER_INSET, BORDER_INSET, W - BORDER_INSET, H - BORDER_INSET], outline=CREAM, width=4)

    # ── header scrim block: eyebrow + headline + payoff line, measured
    # stacking so it can never collide (the discipline every Fuel Check bug
    # traced back to) ──
    block_x0, block_y0, block_x1 = 0, 44, 848
    ef = inter(30, "Bold")
    eyebrow_bbox = ef.getbbox(eyebrow)
    eyebrow_h = eyebrow_bbox[3] - eyebrow_bbox[1]

    lines = list(headline_lines) + [(payoff_line, inter(28, "SemiBold"), CREAM_DIM, 0)]
    block_h = 44 + eyebrow_h + 24 + measure_stack([(t, f, g) for t, f, _, g in lines]) + 44
    d.rectangle([block_x0, block_y0, block_x1, block_y0 + block_h], fill=NAVY_DEEP)
    d.rectangle([block_x0, block_y0, block_x1, block_y0 + block_h], outline=BORDER_BLUE, width=3)

    ey = block_y0 + 40
    tracked_text(d, (MARGIN, ey), eyebrow, ef, GOLD, tracking=4)
    cursor_y = ey + eyebrow_h + 24
    cursor_y = draw_stack(d, MARGIN, cursor_y, lines)

    hf2 = inter(28, "SemiBold")
    handle = "@POWERCOFFEE.OFC"
    hw = d.textlength(handle, font=hf2)
    d.text(((W - hw) / 2, H - BORDER_INSET - 46), handle, font=hf2, fill=CREAM_DIM)

    img.save(f"{OUT}/{name}.jpg", quality=95)
    print(f"{name} saved, block_h={block_h} block_bottom={block_y0 + block_h}")


if __name__ == "__main__":
    make_post(
        "post_dunkin",
        "img_13_power.png",
        [("ONE SCOOP IN MY", anton(78), CREAM, 12),
         ("DUNKIN' RUN.", anton(78), CREAM, 20)],
        "This is what 3pm can look like instead.",
    )
    make_post(
        "post_gym",
        "img_14_power.png",
        [("ONE SCOOP BEFORE MY", anton(66), CREAM, 12),
         ("GYM BAG'S EVEN PACKED.", anton(66), CREAM, 20)],
        "This is what showing up early can look like.",
    )
    make_post(
        "post_secondcup",
        "img_16_power.png",
        [("ONE SCOOP INSTEAD OF", anton(70), CREAM, 12),
         ("MY SECOND CUP.", anton(70), CREAM, 20)],
        "This is what a calm afternoon can look like.",
    )
    # ── 2026-10 batch: the last 5 unused photos in the verified-clean pool.
    # After this, the pool is spent — see if_i_try_campaign.md's October
    # section for what that means for the rest of the month. ──
    make_post(
        "post_schoolmorning",
        "img_24_power.png",
        [("ONE SCOOP BEFORE THE", anton(64), CREAM, 12),
         ("SCHOOL-DAY SCRAMBLE.", anton(64), CREAM, 20)],
        "This is what keeping up before 8am can look like.",
    )
    make_post(
        "post_outthedoor",
        "img_12_power.png",
        [("ONE SCOOP, SHAKEN", anton(74), CREAM, 12),
         ("ON MY WAY OUT.", anton(74), CREAM, 20)],
        "This is what not skipping breakfast can look like.",
    )
    make_post(
        "post_bigmeeting",
        "img_28_power.png",
        [("ONE SCOOP BEFORE I", anton(70), CREAM, 12),
         ("WALK INTO THAT ROOM.", anton(70), CREAM, 20)],
        "This is what walking in like I mean it can look like.",
    )
    # Format variant: the "before" counterpoint, not a payoff shot. No answer
    # photo exists for "still losing the afternoon" in the verified pool (and
    # shouldn't — that's the problem, not the fix) so the invitation itself
    # carries the payoff instead of a photo. Different eyebrow marks it as
    # the set-up, not another "IF I TRY:" answer.
    make_post(
        "post_stilllosing",
        "img_09_power.png",
        [("THREE COFFEES IN.", anton(74), CREAM, 12),
         ("STILL LOSING 2PM.", anton(74), CREAM, 20)],
        "Tomorrow, one scoop. Let's see what changes.",
        eyebrow="SOUND FAMILIAR?",
    )
    # Format variant: simplicity beat — a tactile macro shot, not a life
    # scene, so the copy leans into what's actually shown (the scoop itself)
    # instead of forcing a scenario onto a product close-up.
    make_post(
        "post_simplicity",
        "img_04_power.png",
        [("ONE SCOOP.", anton(84), CREAM, 12),
         ("THAT'S REALLY IT.", anton(84), CREAM, 20)],
        "This is what keeping it simple can look like.",
    )
