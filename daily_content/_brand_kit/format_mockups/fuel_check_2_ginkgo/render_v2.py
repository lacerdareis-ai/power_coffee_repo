#!/usr/bin/env python3
"""
Fuel Check #2 (Ginkgo Biloba) — REBUILD per Leo's direct feedback:
  - Hook needs the payoff built in: "the tree that survived a nuclear blast
    CAN SAVE YOU FROM FATIGUE" — not just an interesting fact on its own.
  - Real photo backgrounds throughout, not flat solid cards — lean back into
    the 24-poster reference batch (swipe_file/README.md section 3),
    specifically the "bleed" technique (oversized type over a photo seam)
    for the hook, which already proved out well on the taurine carousel.
No literal nuclear-blast/Hiroshima imagery — the copy carries that fact as
text; backgrounds are real verified-clean lifestyle photos of the fatigue/
focus payoff, the same substitution used in Fuel Check #1.
"""
import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-lacerdareis-Documents-Claude-ClaudeAI/f98d6e2e-f544-4fa9-bed1-641be79c6a41/scratchpad/fuel_check")
from render_fuel_check import (
    W, H, MARGIN, BORDER_INSET, NAVY, NAVY_DEEP, BORDER_BLUE, CREAM,
    CREAM_DIM, GOLD, anton, inter, tracked_text, cover_fit, halftone_duotone,
    measure_stack, draw_stack, place_mascot, base_canvas, eyebrow_row, bottom_handle,
)
from PIL import Image, ImageDraw

IMGS = "/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/images"
OUT = "/private/tmp/claude-501/-Users-lacerdareis-Documents-Claude-ClaudeAI/f98d6e2e-f544-4fa9-bed1-641be79c6a41/scratchpad/fuel_check_2"


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 1 — HOOK, bleed technique (photo: img_28, striding/energy)
# ══════════════════════════════════════════════════════════════════════════
def slide1():
    img = Image.new("RGB", (W, H), NAVY_DEEP)
    d = ImageDraw.Draw(img)

    # img_28 was already used on Fuel Check #1's slide 1 (staged as tomorrow's
    # content) — switched to img_12 (motion-blurred shaker) so the two
    # carousels' cover slides don't share a background photo.
    photo = Image.open(f"{IMGS}/img_12_power.png").convert("RGB")
    photo_h = int(H * 0.50)
    photo = cover_fit(photo, W, photo_h)
    bg = halftone_duotone(photo, cell=5)
    seam_y = H - photo_h
    img.paste(bg, (0, seam_y))

    # bleed headline — bigger than the canvas, bleeding off the top edge
    hf = anton(118)
    lines = ["SURVIVED A", "NUCLEAR BLAST."]
    y = -30
    line_h = 108
    headline_bottom = y
    for line in lines:
        bbox = d.textbbox((0, 0), line, font=hf)
        tw = bbox[2] - bbox[0]
        x = (W - tw) / 2 - bbox[0]
        d.text((x, y), line, font=hf, fill=CREAM)
        y += line_h
        headline_bottom = y - line_h + bbox[3]

    # payoff line — the mystery (huge type, above) resolves here: WHAT
    # survived + WHY it matters to the reader, together, in the clear navy
    # strip between the headline and the photo seam. (First pass put "THIS
    # TREE" as a separate label crowding the same rows as the huge type —
    # removed; folding it into the reveal line fixes the collision and
    # reads better as a mystery-then-reveal structure anyway.)
    payoff_f = anton(56)
    payoff_lines = ["THIS TREE CAN SAVE", "YOU FROM FATIGUE."]
    py_y = seam_y - 210
    for pline in payoff_lines:
        bbox = d.textbbox((0, 0), pline, font=payoff_f)
        pw = bbox[2] - bbox[0]
        d.text(((W - pw) / 2 - bbox[0], py_y), pline, font=payoff_f, fill=BORDER_BLUE)
        py_y += 92

    # corner mark
    badge_f = inter(26, "Bold")
    bw = tracked_text(d, (0, -1000), "TPC", badge_f, CREAM, tracking=2)
    d.rectangle([W - MARGIN - bw - 28, 50, W - MARGIN, 100], outline=GOLD, width=2)
    tracked_text(d, (W - MARGIN - bw - 14, 62), "TPC", badge_f, GOLD, tracking=2)

    save_f = inter(26, "Bold")
    tracked_text(d, (MARGIN, H - BORDER_INSET - 46), "@POWERCOFFEE.OFC", save_f, CREAM_DIM, tracking=1)
    hf2 = inter(28, "SemiBold")
    save_text = "SAVE THIS — PART 1 OF 6"
    d.text((W - MARGIN - d.textlength(save_text, font=hf2), H - BORDER_INSET - 46), save_text, font=hf2, fill=CREAM_DIM)

    img.save(f"{OUT}/v2_slide1.jpg", quality=95)
    print("v2_slide1 saved, seam_y=", seam_y, "payoff_y=", py_y, "headline_bottom=", headline_bottom)


def photo_slide(num, total, photo_file, lines, tag_lines=None, mascot=None, spec=None):
    """Generic photo-backed slide: halftone photo + opaque headline block,
    matching Fuel Check #1's proven 'jersey stripe' pattern."""
    img = base_canvas("photo", photo_file, None)
    d = ImageDraw.Draw(img)
    d.rectangle([BORDER_INSET, BORDER_INSET, W - BORDER_INSET, H - BORDER_INSET], outline=CREAM, width=4)
    eyebrow_row(d, f"{num:02d} / {total:02d}")

    block_x0, block_y0, block_x1 = 0, 280, 848
    all_lines = list(lines)
    if spec:
        all_lines = all_lines + [(spec["dose"], inter(34, "Bold"), GOLD, 8)]
        for i, dline in enumerate(spec["desc_lines"]):
            all_lines.append((dline, inter(24, "Regular"), CREAM_DIM, 6 if i == 0 else 0))
    block_h = measure_stack([(t, f, g) for t, f, _, g in all_lines]) + 88
    d.rectangle([block_x0, block_y0, block_x1, block_y0 + block_h], fill=NAVY_DEEP)
    d.rectangle([block_x0, block_y0, block_x1, block_y0 + block_h], outline=BORDER_BLUE, width=3)
    draw_stack(d, MARGIN, block_y0 + 44, all_lines)

    band_h = bottom_handle(d)
    if mascot:
        place_mascot(img, mascot, block_y0 + block_h + 24, H - BORDER_INSET - band_h - 24)
    img.save(f"{OUT}/v2_slide{num}.jpg", quality=95)
    print(f"v2_slide{num} saved, block_bottom=", block_y0 + block_h)


if __name__ == "__main__":
    slide1()

    # SLIDE 2 — the real history fact (photo: img_16, calm ritual)
    photo_slide(2, 6, "img_16_power.png", [
        ("SIX GINKGO TREES", anton(78), CREAM, 14),
        ("SURVIVED HIROSHIMA.", anton(78), CREAM, 30),
        ("THEY'RE STILL ALIVE TODAY.", anton(46), BORDER_BLUE, 24),
        ("One of the same species is in your morning scoop.", inter(26, "Regular"), CREAM_DIM, 0),
    ])

    # SLIDE 3 — the spec, over the "drained/fatigue" persona photo (thematic fit)
    photo_slide(3, 6, "img_09_power.png", [
        ("THE SPEC.", anton(78), CREAM, 24),
    ], spec={"dose": "GINKGO BILOBA (EGb 761) · 207mg", "desc_lines": [
        "Supports cerebral blood flow. Used for centuries.",
        "Now backed by research.",
    ]})

    # SLIDE 4 — why it matters (photo: img_13, focused outcome)
    photo_slide(4, 6, "img_13_power.png", [
        ("NOT FOR THE", anton(88), CREAM, 14),
        ("FIRST 10 MINUTES.", anton(88), CREAM, 30),
        ("FOR THE LAST TWO HOURS.", anton(52), BORDER_BLUE, 24),
        ("Paired with caffeine, not replacing it.", inter(26, "Regular"), CREAM_DIM, 0),
    ])

    # SLIDE 5 — identity payoff, mascot armscrossed (photo: img_14, dawn/determination)
    photo_slide(5, 6, "img_14_power.png", [
        ("ONE OF THE OLDEST", anton(72), CREAM, 14),
        ("TREE SPECIES ON EARTH.", anton(58), CREAM, 30),
        ("STILL STANDING.", anton(50), BORDER_BLUE, 10),
        ("STILL SHOWING UP.", anton(50), BORDER_BLUE, 0),
    ], mascot="pose_armscrossed_cutout.png")

    # SLIDE 6 — CTA close (solid navy, matches Fuel Check #1's proven pattern)
    img = base_canvas("solid", None, NAVY_DEEP)
    d = ImageDraw.Draw(img)
    d.rectangle([BORDER_INSET, BORDER_INSET, W - BORDER_INSET, H - BORDER_INSET], outline=CREAM, width=4)
    eyebrow_row(d, "06 / 06")
    hf = anton(100)
    lines6 = [("YOUR FIRST WIN", hf, CREAM, 22), ("STARTS HERE.", hf, CREAM, 56)]
    cursor_y = draw_stack(d, MARGIN, 340, lines6)
    btn_f = inter(32, "Bold")
    btn_text = "SHOP THEPOWERCOFFEE.COM  →"
    btn_pad_x, btn_pad_y = 40, 26
    btn_w = d.textlength(btn_text, font=btn_f) + btn_pad_x * 2
    btn_h = 32 + btn_pad_y * 2
    btn_y0 = cursor_y + 26
    d.rectangle([MARGIN, btn_y0, MARGIN + btn_w, btn_y0 + btn_h], fill=GOLD)
    d.text((MARGIN + btn_pad_x, btn_y0 + btn_pad_y), btn_text, font=btn_f, fill=NAVY_DEEP)
    save_y = btn_y0 + btn_h + 54
    bf = inter(28, "Bold")
    d.ellipse([MARGIN, save_y - 4, MARGIN + 38, save_y + 32], outline=CREAM, width=3)
    d.polygon([(MARGIN + 13, save_y + 2), (MARGIN + 25, save_y + 2), (MARGIN + 25, save_y + 21), (MARGIN + 19, save_y + 16), (MARGIN + 13, save_y + 21)], fill=CREAM)
    save_text6 = "SAVE THIS. SEND IT TO SOMEONE WHO"
    save_text6b = "ASSUMES GINKGO IS A SUPPLEMENT-AISLE WORD."
    d.text((MARGIN + 52, save_y), save_text6, font=bf, fill=CREAM)
    d.text((MARGIN + 52, save_y + 40), save_text6b, font=bf, fill=CREAM)
    tag_y = H - BORDER_INSET - 220
    d.line([(MARGIN, tag_y), (W - MARGIN, tag_y)], fill=BORDER_BLUE, width=2)
    tag_f = anton(46)
    tag_text = "THE FIRST WIN OF YOUR DAY."
    tw6 = d.textlength(tag_text, font=tag_f)
    d.text(((W - tw6) / 2, tag_y + 36), tag_text, font=tag_f, fill=CREAM_DIM)
    bottom_handle(d, deep_band=False)
    img.save(f"{OUT}/v2_slide6.jpg", quality=95)
    print("slide6 saved")
