#!/usr/bin/env python3
"""
Two new post formats applying techniques from the 24-poster reference batch
Leo shared 2026-09-27 (see swipe_file/README.md section 3):

  Post A — "Bleed" poster: massive type bleeding off-canvas, overlapping a
  photo seam. Technique from Georgia "G-Day" / USC "Season Opener."
  Post B — "Annotated Spec": leader-line callouts on a clean product photo,
  near-zero headline copy. Technique from the Amino Innovations grid.

Both reuse the established navy/cream Vintage Athletic system and only
verified-clean images from the fabricated-label audit (img_16, img_24,
img_28) — no new AI photo generation, given that risk is already documented.
"""
import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-lacerdareis-Documents-Claude-ClaudeAI/f98d6e2e-f544-4fa9-bed1-641be79c6a41/scratchpad/fuel_check")
from render_fuel_check import (
    W, H, MARGIN, BORDER_INSET, NAVY, NAVY_DEEP, BORDER_BLUE, CREAM,
    CREAM_DIM, GOLD, anton, inter, tracked_text, cover_fit, halftone_duotone,
)
from PIL import Image, ImageDraw, ImageFont

IMGS = "/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/images"
OUT = "/private/tmp/claude-501/-Users-lacerdareis-Documents-Claude-ClaudeAI/f98d6e2e-f544-4fa9-bed1-641be79c6a41/scratchpad/swipe_inspired"


# ══════════════════════════════════════════════════════════════════════════
# POST A — "BLEED" — oversized type overlapping a photo seam
# (Georgia G-Day / USC Season Opener technique)
# ══════════════════════════════════════════════════════════════════════════
def post_bleed():
    img = Image.new("RGB", (W, H), NAVY_DEEP)
    d = ImageDraw.Draw(img)

    # Photo occupies the bottom ~56% — halftone-duotone treated, matching
    # the mascot's own line art (same technique as the Fuel Check series).
    photo = Image.open(f"{IMGS}/img_28_power.png").convert("RGB")
    photo_h = int(H * 0.62)
    photo = cover_fit(photo, W, photo_h)
    bg = halftone_duotone(photo, cell=5)
    seam_y = H - photo_h
    img.paste(bg, (0, seam_y))

    # ── the bleed headline — huge, bleeding off the top edge, overlapping
    # down into the photo seam, exactly the USC/Georgia device ──────────
    hf = anton(168)
    lines = ["THE", "FIRST WIN", "OF YOUR DAY."]
    # Start above the canvas top so line 1 is cropped/bled off.
    y = -46
    line_h = 152
    headline_bottom = y
    for i, line in enumerate(lines):
        fill = GOLD if i == 1 else CREAM
        bbox = d.textbbox((0, 0), line, font=hf)
        tw = bbox[2] - bbox[0]
        x = (W - tw) / 2 - bbox[0]
        d.text((x, y), line, font=hf, fill=fill)
        y += line_h
        headline_bottom = y - line_h + bbox[3]

    # Tiny technical/spec meta line — the detail USC's poster opens with
    # (coordinates, engineering copy), translated to our own real facts.
    # Placed in the clear navy strip *below* the headline and *above* the
    # photo seam (not at the top, which the giant type already owns —
    # a first pass put it there and "CAFFEINE" ended up cut by the "R").
    meta_f = inter(22, "SemiBold")
    meta_y = seam_y - 44
    tracked_text(d, (MARGIN, meta_y), "BOSTON, MASSACHUSETTS · 11 INGREDIENTS · 175MG CAFFEINE", meta_f, CREAM_DIM, tracking=2)

    # Small mark, top-right (USC's corner badge equivalent) — clear of the
    # centered headline since it's short and stays near canvas center.
    badge_f = inter(26, "Bold")
    bw = tracked_text(d, (0, -1000), "TPC", badge_f, CREAM, tracking=2)  # measure off-canvas
    d.rectangle([W - MARGIN - bw - 28, 50, W - MARGIN, 100], outline=GOLD, width=2)
    tracked_text(d, (W - MARGIN - bw - 14, 62), "TPC", badge_f, GOLD, tracking=2)

    # Handle, bottom
    hf2 = inter(28, "SemiBold")
    handle = "@POWERCOFFEE.OFC"
    hw = d.textlength(handle, font=hf2)
    d.text(((W - hw) / 2, H - 64), handle, font=hf2, fill=CREAM_DIM)

    img.save(f"{OUT}/post_bleed.jpg", quality=95)
    print("post_bleed saved, seam_y=", seam_y)


# ══════════════════════════════════════════════════════════════════════════
# POST B — "ANNOTATED SPEC" — leader-line callouts, minimal headline
# (Amino Innovations technique)
# ══════════════════════════════════════════════════════════════════════════
def leader_line(d, from_xy, to_xy, elbow_x, color):
    fx, fy = from_xy
    tx, ty = to_xy
    d.line([(fx, fy), (elbow_x, fy)], fill=color, width=2)
    d.line([(elbow_x, fy), (elbow_x, ty)], fill=color, width=2)
    d.line([(elbow_x, ty), (tx, ty)], fill=color, width=2)
    r = 4
    d.ellipse([fx - r, fy - r, fx + r, fy + r], fill=color)

def annotation(d, xy, label, value, font_l, font_v, color, align="left"):
    x, y = xy
    if align == "left":
        d.text((x, y), label, font=font_l, fill=CREAM_DIM)
        d.text((x, y + 26), value, font=font_v, fill=color)
    else:
        lw = d.textlength(label, font=font_l)
        vw = d.textlength(value, font=font_v)
        d.text((x - lw, y), label, font=font_l, fill=CREAM_DIM)
        d.text((x - vw, y + 26), value, font=font_v, fill=color)

def post_annotated():
    img = Image.new("RGB", (W, H), NAVY_DEEP)
    d = ImageDraw.Draw(img)
    d.rectangle([BORDER_INSET, BORDER_INSET, W - BORDER_INSET, H - BORDER_INSET], outline=BORDER_BLUE, width=3)

    # Clean, in-focus product photo — img_24 (verified clean: simple black
    # pouch label, no fabricated subtext) — centered, generous negative
    # space around it for the leader lines to land in, same restraint as
    # the reference batch's near-zero-headline product shots.
    photo = Image.open(f"{IMGS}/img_24_power.png").convert("RGB")
    pw, ph = 620, 620
    photo = cover_fit(photo, pw, ph)
    px, py = (W - pw) // 2, 330
    img.paste(photo, (px, py))
    d.rectangle([px, py, px + pw, py + ph], outline=CREAM_DIM, width=1)

    ef = inter(28, "Bold")
    tracked_text(d, (MARGIN, 100), "THE FORMULA, ANNOTATED", ef, GOLD, tracking=3)
    sf = inter(20, "Regular")
    d.text((MARGIN, 138), "Every claim on this label is on the Illuminate Labs certified panel.",
            font=sf, fill=CREAM_DIM)

    label_f = inter(18, "SemiBold")
    value_f = inter(30, "Bold")

    # Four leader-line callouts to real, already-vetted figures — labels
    # sit in the clear navy margin ABOVE or BELOW the photo, never on top
    # of it (a first pass let two overlap the photo itself, right across
    # the cereal bowl). Left/right pairs are also staggered vertically,
    # not just left/right-aligned on one shared row — a first pass had
    # both top values on the same row and, being real sentences rather
    # than short numbers, they ran into each other in the middle. Short,
    # number-first values with the context on the (smaller) label line
    # instead removes the failure mode rather than just hoping the
    # strings stay short enough.
    top_l_label_y, top_l_value_y = py - 150, py - 122
    top_r_label_y, top_r_value_y = py - 96, py - 68
    bot_l_label_y = py + ph + 34
    bot_r_label_y = py + ph + 88

    leader_line(d, (px + 90, py), (px + 90, top_l_value_y - 4), px + 90, BORDER_BLUE)
    annotation(d, (px, top_l_label_y), "CAFFEINE · UNDER EFSA'S LIMIT", "175mg", label_f, value_f, CREAM, "left")

    leader_line(d, (px + pw - 90, py), (px + pw - 90, top_r_value_y - 4), px + pw - 90, BORDER_BLUE)
    annotation(d, (px + pw, top_r_label_y), "TAURINE · NOT A STIMULANT", "2.1g", label_f, value_f, CREAM, "right")

    leader_line(d, (px + 90, py + ph), (px + 90, bot_l_label_y - 10), px + 90, GOLD)
    annotation(d, (px, bot_l_label_y), "SUGAR", "0g · zero, always", label_f, value_f, GOLD, "left")

    leader_line(d, (px + pw - 90, py + ph), (px + pw - 90, bot_r_label_y - 10), px + pw - 90, GOLD)
    annotation(d, (px + pw, bot_r_label_y), "SERVINGS", "15/bag · $1.26/morning", label_f, value_f, GOLD, "right")

    hf2 = inter(26, "SemiBold")
    handle = "@POWERCOFFEE.OFC"
    hw = d.textlength(handle, font=hf2)
    d.text(((W - hw) / 2, H - BORDER_INSET - 44), handle, font=hf2, fill=CREAM_DIM)

    img.save(f"{OUT}/post_annotated.jpg", quality=95)
    print("post_annotated saved")


if __name__ == "__main__":
    post_bleed()
    post_annotated()
