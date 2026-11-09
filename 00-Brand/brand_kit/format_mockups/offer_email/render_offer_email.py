#!/usr/bin/env python3
"""
Offer email images — first-order discount emails (browse abandonment + the
Oct 31 2026 Saturday newsletter). Modeled on the Lineage Provisions offer email
Leo forwarded 2026-10-27: one big offer, one code, one button, brand sign-off.

Images only carry the visuals; every word that matters (offer, code, terms) is
also live text in the HTML so the email still works with images blocked.

  python3 render_offer_email.py OUT_DIR "EYEBROW" "BIG LINE" "SMALL LINE"

Writes OUT_DIR/hero_offer.jpg (1200x1400), morning.jpg (1200x760),
brand_footer.jpg (1200x600). 2x the 600px email width for retina screens.
Real pack only (cutouts/frente.png) — never the AI pack images with fabricated
label text (make_carousel.py audit, 2026-09-27). Navy/cream, no black.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "fuel_check"))
from render_fuel_check import NAVY, NAVY_DEEP, CREAM, CREAM_DIM, GOLD, anton, inter, tracked_text, cover_fit
from PIL import Image, ImageDraw, ImageFilter

KIT = os.path.abspath(os.path.join(HERE, "..", ".."))
PACK = os.path.join(KIT, "cutouts", "frente.png")
MORNING = os.path.join(KIT, "images", "img_16_power.png")
AMAZON = os.path.join(KIT, "logos", "amazon_logo_cream.png")
W = 1200


def glow(size, center, radius, color):
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    cx, cy = center
    d.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=color + (150,))
    return layer.filter(ImageFilter.GaussianBlur(radius // 2))


def centered(d, y, text, font, fill, tracking=0):
    if tracking:
        w = sum(d.textlength(c, font=font) + tracking for c in text) - tracking
        tracked_text(d, ((W - w) / 2, y), text, font, fill, tracking=tracking)
        return
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)


def fit(d, text, max_w, start):
    s = start
    while s > 40 and d.textlength(text, font=anton(s)) > max_w:
        s -= 4
    return anton(s)


def edge_fade(im, side=0.16, bottom=0.12):
    """Fade the crop edges so the cutout's soft floor shadow never shows as a box."""
    w, h = im.size
    mask = Image.new("L", (w, h), 255)
    md = ImageDraw.Draw(mask)
    sw, bh = int(w * side), int(h * bottom)
    for i in range(sw):
        v = int(255 * i / sw)
        md.line([(i, 0), (i, h)], fill=v)
        md.line([(w - 1 - i, 0), (w - 1 - i, h)], fill=v)
    from PIL import ImageChops
    vert = Image.new("L", (w, h), 255)
    vd = ImageDraw.Draw(vert)
    for j in range(bh):
        vd.line([(0, h - 1 - j), (w, h - 1 - j)], fill=int(255 * j / bh))
    mask = ImageChops.multiply(mask, vert)
    im.putalpha(ImageChops.multiply(im.split()[3], mask))
    return im


def hero(out, eyebrow, big, small):
    H = 1400
    img = Image.new("RGBA", (W, H), NAVY_DEEP + (255,))
    img.alpha_composite(glow((W, H), (W // 2, 860), 420, NAVY))
    d = ImageDraw.Draw(img)
    # gold rule + eyebrow
    d.line([(W / 2 - 30, 92), (W / 2 + 30, 92)], fill=GOLD, width=4)
    centered(d, 118, eyebrow, inter(34, "Bold"), GOLD, tracking=5)
    f = fit(d, big, W - 160, 230)
    centered(d, 176, big, f, CREAM)
    bb = d.textbbox((0, 176), big, font=f)
    small_y = bb[3] + 34
    centered(d, small_y, small, inter(40, "SemiBold"), CREAM_DIM)
    text_bottom = small_y + 60
    # real pack, cropped to the bag + its soft shadow
    pack = Image.open(PACK).convert("RGBA").crop((1150, 380, 2690, 2700))
    ph = min(860, H - text_bottom - 30)
    pack = edge_fade(pack.resize((int(pack.width * ph / pack.height), ph), Image.LANCZOS))
    img.alpha_composite(pack, ((W - pack.width) // 2, H - ph))
    img.convert("RGB").save(os.path.join(out, "hero_offer.jpg"), quality=88)


def morning(out):
    im = cover_fit(Image.open(MORNING).convert("RGB"), W, 760)
    # a light navy grade so the photo sits in the palette
    tint = Image.new("RGB", im.size, NAVY_DEEP)
    Image.blend(im, tint, 0.12).save(os.path.join(out, "morning.jpg"), quality=86)


def brand_footer(out):
    H = 600
    img = Image.new("RGBA", (W, H), NAVY_DEEP + (255,))
    d = ImageDraw.Draw(img)
    f = fit(d, "THE POWER", W - 160, 200)
    y = 50
    for line in ("THE POWER", "COFFEE"):
        top = d.textbbox((0, 0), line, font=f)
        centered(d, y - top[1], line, f, CREAM)
        y += (top[3] - top[1]) + 26
    # footer: www + divider + Amazon logo
    url = "www.thepowercoffee.com"
    uf = inter(36, "SemiBold")
    uw = d.textlength(url, font=uf)
    logo = Image.open(AMAZON).convert("RGBA")
    lh = 44
    logo = logo.resize((int(logo.width * lh / logo.height), lh), Image.LANCZOS)
    gap = 36
    total = uw + gap * 2 + 2 + logo.width
    x = (W - total) / 2
    y = max(y + 40, 500)
    d.text((x, y), url, font=uf, fill=CREAM)
    dx = x + uw + gap
    d.line([(dx, y - 4), (dx, y + 46)], fill=CREAM_DIM, width=2)
    img.alpha_composite(logo, (int(dx + 2 + gap), y + 2))
    img.convert("RGB").save(os.path.join(out, "brand_footer.jpg"), quality=88)


if __name__ == "__main__":
    out, eyebrow, big, small = sys.argv[1:5]
    os.makedirs(out, exist_ok=True)
    hero(out, eyebrow, big, small)
    morning(out)
    brand_footer(out)
    print("wrote", out)
