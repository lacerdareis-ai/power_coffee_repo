#!/usr/bin/env python3
"""
Problem-hook still — the single feed image used when a P1 Monday Reel can't
be generated (Higgsfield not_enough_credits). First used Oct 12 ("THE PLAN
DIED AT 11AM."), whose script was never saved; rebuilt here 2026-10-17 for
Oct 19 so the layout stays reproducible.

Layout: navy canvas + cream inset border, gold eyebrow, two-line Anton
headline (cream, then blue), Inter sub line, rounded inset photo with a
cream frame, footer www.thepowercoffee.com | Amazon logo. No black anywhere.

Usage:
  python3 render_problem_still.py PHOTO OUT.jpg "EYEBROW" "LINE 1" "LINE 2" "Sub line."
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "fuel_check"))
from render_fuel_check import (
    W, H, MARGIN, BORDER_INSET, NAVY, NAVY_DEEP, BORDER_BLUE, CREAM,
    CREAM_DIM, GOLD, anton, inter, tracked_text, cover_fit,
)
from PIL import Image, ImageDraw

LOGOS = os.path.join(HERE, "..", "..", "logos")


def fit_font(d, text, max_w, start):
    size = start
    while size > 40 and d.textlength(text, font=anton(size)) > max_w:
        size -= 2
    return anton(size)


def render(photo_path, out_path, eyebrow, line1, line2, sub):
    img = Image.new("RGB", (W, H), NAVY_DEEP)
    d = ImageDraw.Draw(img)

    # faint dot grid for texture (navy on navy, never black)
    for y in range(0, H, 14):
        for x in range(0, W, 14):
            d.point((x, y), fill=NAVY)

    d.rectangle([BORDER_INSET, BORDER_INSET, W - BORDER_INSET, H - BORDER_INSET],
                outline=CREAM_DIM, width=2)

    # eyebrow: gold rule + tracked caps
    ey = 112
    d.line([(MARGIN, ey + 16), (MARGIN + 44, ey + 16)], fill=GOLD, width=3)
    tracked_text(d, (MARGIN + 62, ey), eyebrow, inter(30, "Bold"), GOLD, tracking=4)

    max_w = W - 2 * MARGIN
    size = min(fit_font(d, line1, max_w, 150).size, fit_font(d, line2, max_w, 150).size)
    hf = anton(size)
    y = ey + 70
    for text, color in ((line1, CREAM), (line2, BORDER_BLUE)):
        bbox = hf.getbbox(text)
        d.text((MARGIN, y - bbox[1]), text, font=hf, fill=color)
        y += (bbox[3] - bbox[1]) + 22

    sf = inter(36, "Medium")
    sb = sf.getbbox(sub)
    d.text((MARGIN, y + 18 - sb[1]), sub, font=sf, fill=CREAM)
    y += 18 + (sb[3] - sb[1]) + 44

    # inset photo with rounded cream frame, sized to the room left above the footer
    footer_top = H - BORDER_INSET - 150
    px0, px1 = 88, W - 88
    py0, py1 = y, footer_top
    photo = cover_fit(Image.open(photo_path).convert("RGB"), px1 - px0, py1 - py0)
    mask = Image.new("L", photo.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, *photo.size], radius=22, fill=255)
    img.paste(photo, (px0, py0), mask)
    d.rounded_rectangle([px0 - 2, py0 - 2, px1 + 2, py1 + 2], radius=24, outline=CREAM, width=4)

    # footer: www | amazon
    ff = inter(34, "Bold")
    url = "www.thepowercoffee.com"
    uw = d.textlength(url, font=ff)
    logo = Image.open(os.path.join(LOGOS, "amazon_logo_cream.png")).convert("RGBA")
    lh = 52
    logo = logo.resize((int(logo.width * lh / logo.height), lh), Image.LANCZOS)
    gap = 36
    total = uw + gap * 2 + 2 + logo.width
    fx = (W - total) / 2
    fy = footer_top + 62
    ub = ff.getbbox(url)
    d.text((fx, fy - ub[1]), url, font=ff, fill=CREAM)
    div_x = fx + uw + gap
    d.line([(div_x, fy - 8), (div_x, fy + 44)], fill=CREAM_DIM, width=2)
    img.paste(logo, (int(div_x + 2 + gap), int(fy - 6)), logo)

    img.save(out_path, quality=95)
    print(f"saved {out_path} (headline {size}px, photo {px1 - px0}x{py1 - py0})")


if __name__ == "__main__":
    render(*sys.argv[1:7])
