#!/usr/bin/env python3
"""
Profile grid-mix mockup: demonstrates "one palette, varied content" — the
actual working principle behind the Everyday Dose reference, applied with
Power Coffee's own already-built assets. 6 real tiles (mixing hook/spec/
identity/CTA slide types, not the same template 9 times) + 3 clearly-marked
placeholders for real event/founder photography, which this session does
NOT fabricate — see the fabricated-label-images project memory for why
that's a hard rule, not a style choice.
"""
import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-lacerdareis-Documents-Claude-ClaudeAI/f98d6e2e-f544-4fa9-bed1-641be79c6a41/scratchpad/fuel_check")
from render_fuel_check import NAVY_DEEP, BORDER_BLUE, CREAM, CREAM_DIM, anton, inter
from PIL import Image, ImageDraw

BK = "/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/format_mockups"
OUT = "/private/tmp/claude-501/-Users-lacerdareis-Documents-Claude-ClaudeAI/f98d6e2e-f544-4fa9-bed1-641be79c6a41/scratchpad/grid_mockup"

TILE = 1080
GAP = 6  # IG's own grid gap is ~3px at typical display scale; a little
         # breathing room here makes the 3x3 read clearly as a grid, not
         # one stitched image


def cover_crop(path, size=TILE):
    im = Image.open(path).convert("RGB")
    # IG's grid preview crops a 4:5 post to a centered square, weighted
    # slightly toward the top third (where the safe-zone content already
    # lives) rather than dead-center — matches how these slides were
    # actually designed (headline block near the top).
    w, h = im.size
    if w / h > 1:
        new_h = size
        new_w = int(w * (size / h))
    else:
        new_w = size
        new_h = int(h * (size / w))
    im = im.resize((new_w, new_h), Image.LANCZOS)
    x0 = (new_w - size) // 2
    y0 = int((new_h - size) * 0.16)  # top-weighted crop, not dead-center
    return im.crop((x0, y0, x0 + size, y0 + size))


def placeholder_tile(label, sublabel):
    img = Image.new("RGB", (TILE, TILE), NAVY_DEEP)
    d = ImageDraw.Draw(img)
    # dashed border — unmistakably "not a finished asset"
    dash, gap_len = 26, 18
    x0, y0, x1, y1 = 24, 24, TILE - 24, TILE - 24
    x = x0
    while x < x1:
        d.line([(x, y0), (min(x + dash, x1), y0)], fill=CREAM_DIM, width=4)
        d.line([(x, y1), (min(x + dash, x1), y1)], fill=CREAM_DIM, width=4)
        x += dash + gap_len
    y = y0
    while y < y1:
        d.line([(x0, y), (x0, min(y + dash, y1))], fill=CREAM_DIM, width=4)
        d.line([(x1, y), (x1, min(y + dash, y1))], fill=CREAM_DIM, width=4)
        y += dash + gap_len

    icon_f = anton(120)
    iw = d.textlength("+", font=icon_f)
    d.text((TILE / 2 - iw / 2, TILE / 2 - 220), "+", font=icon_f, fill=BORDER_BLUE)

    label_f = anton(56)
    lw = d.textlength(label, font=label_f)
    d.text((TILE / 2 - lw / 2, TILE / 2 - 40), label, font=label_f, fill=CREAM)

    sub_f = inter(28, "Regular")
    # wrap sublabel to two lines if needed
    words = sublabel.split()
    l1, l2 = "", ""
    for w in words:
        trial = (l1 + " " + w).strip()
        if d.textlength(trial, font=sub_f) <= TILE - 140:
            l1 = trial
        else:
            l2 = (l2 + " " + w).strip()
    sw1 = d.textlength(l1, font=sub_f)
    d.text((TILE / 2 - sw1 / 2, TILE / 2 + 40), l1, font=sub_f, fill=CREAM_DIM)
    if l2:
        sw2 = d.textlength(l2, font=sub_f)
        d.text((TILE / 2 - sw2 / 2, TILE / 2 + 76), l2, font=sub_f, fill=CREAM_DIM)
    return img


TILES = [
    ("cover", f"{BK}/fuel_check/slide1_v2_mockup.jpg"),
    ("placeholder", "REAL PHOTO", "Leo at a retail/market activation, posted within 24h"),
    ("cover", f"{BK}/fuel_check_2_ginkgo/slide_3.jpg"),
    ("cover", f"{BK}/fuel_check_3_caffeine/slide_5.jpg"),
    ("placeholder", "REAL PHOTO", "Founder-to-camera, unscripted — the account's proven #1 format"),
    ("cover", f"{BK}/fuel_check/slide6_mockup.jpg"),
    ("cover", f"{BK}/fuel_check_2_ginkgo/slide_1.jpg"),
    ("cover", f"{BK}/fuel_check_3_caffeine/slide_3.jpg"),
    ("placeholder", "REAL PHOTO", "A local store/cafe stocking Power Coffee"),
]

cols, rows = 3, 3
sheet_w = cols * TILE + (cols - 1) * GAP
sheet_h = rows * TILE + (rows - 1) * GAP
sheet = Image.new("RGB", (sheet_w, sheet_h), (20, 20, 20))

for i, entry in enumerate(TILES):
    if entry[0] == "cover":
        tile = cover_crop(entry[1])
    else:
        tile = placeholder_tile(entry[1], entry[2])
    r, c = divmod(i, cols)
    sheet.paste(tile, (c * (TILE + GAP), r * (TILE + GAP)))

sheet.save(f"{OUT}/grid_mockup.jpg", quality=92)
print("grid_mockup saved", sheet.size)
