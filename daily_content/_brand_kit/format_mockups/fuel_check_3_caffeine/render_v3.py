#!/usr/bin/env python3
"""
Fuel Check #3 — topic: caffeine/adenosine. This is the account's single
best-measured hook ("Caffeine doesn't give you energy" — 122.22% ER on day
1, brand.md's own Growth Report data), reframed per the standing hook rule:
state the claim and its payoff together (see the Ginkgo correction,
2026-09-27). Photo pool is down to 8 verified-clean images total after the
completed audit (img_04, 09, 12, 13, 14, 16, 24, 28) — img_04 is genuinely
new here; the rest are necessarily reused from Fuel Check #1/#2 on
non-cover slides, which is the real production constraint already flagged
in memory (needs new photography, not more AI-generated packs).
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
OUT = "/private/tmp/claude-501/-Users-lacerdareis-Documents-Claude-ClaudeAI/f98d6e2e-f544-4fa9-bed1-641be79c6a41/scratchpad/fuel_check_3"


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 1 — HOOK, bleed technique (photo: img_04, scoop macro texture)
# ══════════════════════════════════════════════════════════════════════════
def slide1():
    img = Image.new("RGB", (W, H), NAVY_DEEP)
    d = ImageDraw.Draw(img)

    photo = Image.open(f"{IMGS}/img_04_power.png").convert("RGB")
    photo_h = int(H * 0.50)
    photo = cover_fit(photo, W, photo_h)
    bg = halftone_duotone(photo, cell=5)
    seam_y = H - photo_h
    img.paste(bg, (0, seam_y))

    hf = anton(112)
    lines = ["CAFFEINE DOESN'T", "GIVE YOU ENERGY."]
    y = -26
    line_h = 104
    headline_bottom = y
    for line in lines:
        bbox = d.textbbox((0, 0), line, font=hf)
        tw = bbox[2] - bbox[0]
        x = (W - tw) / 2 - bbox[0]
        d.text((x, y), line, font=hf, fill=CREAM)
        y += line_h
        headline_bottom = y - line_h + bbox[3]

    payoff_f = anton(56)
    payoff_lines = ["IT JUST DELAYS", "YOUR CRASH."]
    py_y = seam_y - 240
    for pline in payoff_lines:
        bbox = d.textbbox((0, 0), pline, font=payoff_f)
        pw = bbox[2] - bbox[0]
        d.text(((W - pw) / 2 - bbox[0], py_y), pline, font=payoff_f, fill=BORDER_BLUE)
        py_y += 92

    badge_f = inter(26, "Bold")
    bw = tracked_text(d, (0, -1000), "TPC", badge_f, CREAM, tracking=2)
    d.rectangle([W - MARGIN - bw - 28, 50, W - MARGIN, 100], outline=GOLD, width=2)
    tracked_text(d, (W - MARGIN - bw - 14, 62), "TPC", badge_f, GOLD, tracking=2)

    # save-cue sits right under the payoff, inside the navy area — matches
    # Fuel Check #1/#2's proven slide-1 pattern. A first pass here shared
    # the bottom row with the handle instead and the two ran into each
    # other; this is the same fix, put in the right place this time.
    hf2 = inter(28, "SemiBold")
    save_text = "SAVE THIS — PART 1 OF 6"
    stw = d.textlength(save_text, font=hf2)
    d.text(((W - stw) / 2, py_y + 16), save_text, font=hf2, fill=CREAM_DIM)

    # Handle sits over the photo here (unlike every other slide's opaque
    # bottom band) — the bottom of img_04 is a light patch, so bare
    # CREAM_DIM text nearly disappears into it. A small scrim pill fixes
    # the contrast instead of just hoping the photo is dark enough there.
    save_f = inter(26, "Bold")
    handle_text = "@POWERCOFFEE.OFC"
    htw = d.textlength(handle_text, font=save_f)
    pill_cx = W / 2
    pill_y0, pill_y1 = H - BORDER_INSET - 58, H - BORDER_INSET - 16
    d.rectangle([pill_cx - htw / 2 - 20, pill_y0, pill_cx + htw / 2 + 20, pill_y1], fill=NAVY_DEEP)
    d.text((pill_cx - htw / 2, H - BORDER_INSET - 46), handle_text, font=save_f, fill=CREAM_DIM)

    img.save(f"{OUT}/v3_slide1.jpg", quality=95)
    print("v3_slide1 saved, seam_y=", seam_y, "headline_bottom=", headline_bottom,
          "payoff_y_end=", py_y, "save_cue_y=", py_y + 16)


def photo_slide(num, total, photo_file, lines, mascot=None, spec=None):
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
    img.save(f"{OUT}/v3_slide{num}.jpg", quality=95)
    print(f"v3_slide{num} saved, block_bottom=", block_y0 + block_h)


if __name__ == "__main__":
    slide1()

    # SLIDE 2 — the mechanism (photo: img_16, calm ritual)
    photo_slide(2, 6, "img_16_power.png", [
        ("IT BLOCKS THE SIGNAL", anton(64), CREAM, 14),
        ("THAT SAYS YOU'RE TIRED.", anton(64), CREAM, 30),
        ("THE TIREDNESS DOESN'T GO AWAY.", anton(38), BORDER_BLUE, 10),
        ("IT WAITS.", anton(38), BORDER_BLUE, 20),
        ("Caffeine blocks the adenosine receptors that build sleep", inter(24, "Regular"), CREAM_DIM, 4),
        ("pressure. It doesn't stop the buildup — just the feeling.", inter(24, "Regular"), CREAM_DIM, 0),
    ])

    # SLIDE 3 — the spec (photo: img_12, motion blur)
    photo_slide(3, 6, "img_12_power.png", [
        ("THE SPEC.", anton(78), CREAM, 24),
    ], spec={"dose": "NATURAL CAFFEINE · 175mg", "desc_lines": [
        "Under EFSA's 200mg single-dose safety threshold.",
        "~5 hour half-life — then the adenosine floods back.",
    ]})

    # SLIDE 4 — why it matters (photo: img_09, drained at desk) — the
    # already-proven brand.md content hook, near-verbatim.
    photo_slide(4, 6, "img_09_power.png", [
        ("YOUR SECOND CUP", anton(80), CREAM, 14),
        ("DOESN'T HIT LIKE", anton(80), CREAM, 14),
        ("THE FIRST.", anton(80), CREAM, 30),
        ("THAT'S NOT TOLERANCE.", anton(44), BORDER_BLUE, 10),
        ("THAT'S ADENOSINE.", anton(44), BORDER_BLUE, 0),
    ])

    # SLIDE 5 — identity payoff, mascot armscrossed (photo: img_14, dawn)
    photo_slide(5, 6, "img_14_power.png", [
        ("WE DON'T FIGHT", anton(80), CREAM, 14),
        ("THE CRASH.", anton(80), CREAM, 30),
        ("WE PAIR CAFFEINE WITH", anton(42), BORDER_BLUE, 8),
        ("WHAT SMOOTHS IT.", anton(42), BORDER_BLUE, 20),
        ("Matcha. L-theanine. Stable blood sugar. One scoop.", inter(24, "Regular"), CREAM_DIM, 0),
    ], mascot="pose_armscrossed_cutout.png")

    # SLIDE 6 — CTA close (solid navy, matches the series pattern)
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
    save_text6 = "SAVE THIS. SEND IT TO SOMEONE"
    save_text6b = "WHO BLAMES TOLERANCE FOR THE CRASH."
    d.text((MARGIN + 52, save_y), save_text6, font=bf, fill=CREAM)
    d.text((MARGIN + 52, save_y + 40), save_text6b, font=bf, fill=CREAM)
    tag_y = H - BORDER_INSET - 220
    d.line([(MARGIN, tag_y), (W - MARGIN, tag_y)], fill=BORDER_BLUE, width=2)
    tag_f = anton(46)
    tag_text = "THE FIRST WIN OF YOUR DAY."
    tw6 = d.textlength(tag_text, font=tag_f)
    d.text(((W - tw6) / 2, tag_y + 36), tag_text, font=tag_f, fill=CREAM_DIM)
    bottom_handle(d, deep_band=False)
    img.save(f"{OUT}/v3_slide6.jpg", quality=95)
    print("slide6 saved")
