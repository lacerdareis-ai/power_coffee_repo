#!/usr/bin/env python3
"""
nov20_one_scoop.py: a one-off graphic carousel for Nov 20, 2026 ("One scoop. That's the whole change.").

Design: a recipe-card look with no stock photos. Espresso and cream slides alternate, with big step
numerals, the brand line icons, the real pack render (cutouts/frente.png) and a gold coupon slide for
MORNING15. Copy matches the day's content.md word for word.

Usage: python3 nov20_one_scoop.py <day_folder>
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

BK = Path.home() / "Documents/Claude/The_Power_Coffee/Sales_motor/00-Brand/brand_kit"
FONTS = BK / "fonts"
CUT = BK / "cutouts"

W, H = 1080, 1350
M = 90
ESPRESSO = (23, 20, 18)
CHARCOAL = (46, 40, 36)
CREAM = (247, 240, 224)
CREAM_DIM = (200, 191, 172)
INK = (24, 21, 19)
GRAY = (96, 86, 76)
GOLD = (217, 166, 51)
GOLD_DEEP = (191, 146, 42)
MATCHA = (56, 114, 77)
TOTAL = 7


def anton(s):
    return ImageFont.truetype(str(FONTS / "Anton-Regular.ttf"), s)


def inter(s, w="Regular"):
    f = ImageFont.truetype(str(FONTS / "Inter-Variable.ttf"), s)
    try:
        f.set_variation_by_name(w)
    except Exception:
        pass
    return f


def wrap(d, text, f, mw):
    out, line = [], ""
    for w in text.split():
        t = (line + " " + w).strip()
        if d.textlength(t, font=f) <= mw:
            line = t
        else:
            out.append(line)
            line = w
    if line:
        out.append(line)
    return out


def icon(name, color, size):
    """Black-on-white RGB icon -> tinted RGBA, cropped to its ink."""
    g = Image.open(CUT / name).convert("L")
    mask = ImageOps.invert(g).point(lambda v: 255 if v > 110 else int(v * 2.2))
    bbox = mask.getbbox()
    mask = mask.crop(bbox)
    mask.thumbnail((size, size), Image.LANCZOS)
    out = Image.new("RGBA", mask.size, color + (0,))
    out.putalpha(mask)
    return out


def pack(width, angle=0):
    p = Image.open(CUT / "frente.png").convert("RGBA")
    p = p.crop(p.split()[3].point(lambda v: 255 if v > 200 else 0).getbbox())
    p = p.resize((width, int(p.height * width / p.width)), Image.LANCZOS)
    if angle:
        p = p.rotate(angle, expand=True, resample=Image.BICUBIC)
    return p


def shadow(img, base, xy, blur=28, alpha=110):
    from PIL import ImageFilter
    a = img.split()[3].point(lambda v: alpha if v > 10 else 0)
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sh.putalpha(a)
    pad = blur * 3
    big = Image.new("RGBA", (img.width + pad * 2, img.height + pad * 2), (0, 0, 0, 0))
    big.paste(sh, (pad, pad), sh)
    big = big.filter(ImageFilter.GaussianBlur(blur))
    base.alpha_composite(big, (xy[0] - pad + 14, xy[1] - pad + 24))


def chrome(img, n, dark):
    """Slide counter, handle, and the HE mug sticker: the same on every slide."""
    d = ImageDraw.Draw(img)
    f = inter(28, "Bold")
    lab = f"{n:02d}/{TOTAL:02d}"
    tw = d.textlength(lab, font=f)
    d.rounded_rectangle([W - 40 - tw - 44, 40, W - 40, 40 + 54], radius=27,
                        outline=GOLD if dark else INK, width=3)
    d.text((W - 40 - tw - 22, 50), lab, font=f, fill=GOLD if dark else INK)
    d.text((M, 52), "THE POWER COFFEE", font=inter(26, "Bold"), fill=CREAM_DIM if dark else GRAY)
    d.text((M, H - 74), "@POWERCOFFEE.OFC", font=inter(28, "SemiBold"), fill=CREAM_DIM if dark else GRAY)


def sticker(img, dark, size=170):
    s = Image.open(BK / ("high_energy_guy_whitecolor.png" if dark else "high_energy_guy.png")).convert("RGBA")
    s = s.resize((size, size), Image.LANCZOS).rotate(10, expand=True, resample=Image.BICUBIC)
    img.alpha_composite(s, (W - s.width - 34, H - s.height - 24))


def text_block(d, x, y, lines, f, fill, lh):
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill)
        y += lh
    return y


def base(dark):
    return Image.new("RGBA", (W, H), (ESPRESSO if dark else CREAM) + (255,))


# ── slides ──────────────────────────────────────────────────────────────────

def s1():
    img = base(True)
    d = ImageDraw.Draw(img)
    # warm glow behind the pack
    from PIL import ImageFilter
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([430, 640, 1180, 1390], fill=GOLD + (90,))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(120)))
    p = pack(400, angle=-8)
    shadow(p, img, (610, 660))
    img.alpha_composite(p, (610, 660))
    y = 200
    d.text((M, y), "ONE SCOOP.", font=anton(190), fill=GOLD)
    y += 215
    for ln in ["THAT'S THE", "WHOLE CHANGE."]:
        d.text((M, y), ln, font=anton(104), fill=CREAM)
        y += 112
    y += 34
    f = inter(36)
    text_block(d, M, y, wrap(d, "How Power Coffee fits into the morning you already have.", f, 430), f, CREAM_DIM, 52)
    chrome(img, 1, True)
    return img


def step(n, num, head, body, ic, dark):
    img = base(dark)
    d = ImageDraw.Draw(img)
    fg, dim = (CREAM, CREAM_DIM) if dark else (INK, GRAY)
    # giant outlined step numeral
    d.text((M - 12, 150), num, font=anton(500), fill=ESPRESSO if dark else CREAM, stroke_width=5, stroke_fill=GOLD)
    d.text((M, 800), f"STEP {num.lstrip('0')}", font=inter(36, "Bold"), fill=GOLD_DEEP if not dark else GOLD)
    y = 860
    for ln in wrap(d, head, anton(116), W - 2 * M):
        d.text((M, y), ln, font=anton(116), fill=fg)
        y += 124
    d.rectangle([M, y + 18, M + 90, y + 26], fill=GOLD)
    f = inter(38)
    text_block(d, M, y + 66, wrap(d, body, f, 760), f, dim, 56)
    img.alpha_composite(ic, (W - M - ic.width, 230))
    chrome(img, n, dark)
    sticker(img, dark)
    return img


def mug_icon(color, size=330):
    """Plain coffee mug with steam, drawn to match the line icons."""
    S = 4
    c = Image.new("RGBA", (size * S, size * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    lw = 15 * S
    x0, y0, x1, y1 = 40 * S, 120 * S, 230 * S, 310 * S
    d.rounded_rectangle([x0, y0, x1, y1], radius=34 * S, outline=color, width=lw)
    d.arc([200 * S, 160 * S, 300 * S, 260 * S], 270, 90, fill=color, width=lw)
    for sx in (85, 135, 185):
        d.arc([(sx - 18) * S, 20 * S, (sx + 18) * S, 62 * S], 90, 270, fill=color, width=11 * S)
        d.arc([(sx - 18) * S, 58 * S, (sx + 18) * S, 100 * S], 270, 90, fill=color, width=11 * S)
    return c.resize((size, size), Image.LANCZOS)


def s4():
    img = base(False)
    d = ImageDraw.Draw(img)
    leaf = icon("preto.png", MATCHA, 150)
    img.alpha_composite(leaf, (W - M - leaf.width, 200))
    y = 220
    for ln in ["WHAT'S IN", "THE SCOOP."]:
        d.text((M, y), ln, font=anton(150), fill=INK)
        y += 160
    d.rectangle([M, y + 16, M + 90, y + 24], fill=GOLD)
    y += 70
    d.text((M, y), "11 INGREDIENTS, INCLUDING", font=inter(30, "Bold"), fill=GRAY)
    y += 64
    pills = ["MATCHA", "TAURINE", "GINKGO BILOBA", "CEYLON CINNAMON", "GINGER"]
    f = inter(40, "SemiBold")
    x = M
    for p in pills:
        tw = d.textlength(p, font=f)
        wpill = tw + 64
        if x + wpill > W - M:
            x = M
            y += 104
        d.rounded_rectangle([x, y, x + wpill, y + 84], radius=42, fill=MATCHA)
        d.text((x + 32, y + 19), p, font=f, fill=CREAM)
        x += wpill + 18
    y = max(y + 150, 1000)
    # three-stat row
    stats = [("11", "INGREDIENTS"), ("0g", "SUGAR"), ("USA", "MADE IN THE USA")]
    colw = (W - 2 * M) / 3
    d.line([M, y - 30, W - M, y - 30], fill=(214, 204, 184), width=3)
    for i, (big, small) in enumerate(stats):
        cx = M + i * colw
        d.text((cx, y - 20), big, font=anton(110), fill=INK)
        d.text((cx, y + 140), small, font=inter(24, "Bold"), fill=GRAY)
    chrome(img, 4, False)
    return img


def s5():
    img = base(True)
    d = ImageDraw.Draw(img)
    p = pack(340, angle=6)
    shadow(p, img, (620, 760))
    img.alpha_composite(p, (620, 760))
    d.text((M - 6, 170), "$1.26", font=anton(330), fill=GOLD)
    d.text((M, 590), "A CUP.", font=anton(140), fill=CREAM)
    d.rectangle([M, 770, M + 90, 778], fill=GOLD)
    f = inter(40)
    text_block(d, M, 820, wrap(d, "15 servings in every $18.90 pack.", f, 460), f, CREAM_DIM, 58)
    chrome(img, 5, True)
    return img


def s6():
    img = Image.new("RGBA", (W, H), GOLD + (255,))
    d = ImageDraw.Draw(img)
    d.text((M, 190), "FIRST ORDER?", font=anton(110), fill=ESPRESSO)
    d.text((M - 6, 300), "15% OFF.", font=anton(240), fill=ESPRESSO)
    # coupon ticket
    tx0, ty0, tx1, ty1 = M, 680, W - M, 1010
    d.rounded_rectangle([tx0, ty0, tx1, ty1], radius=26, fill=ESPRESSO)
    for cy in (ty0 + (ty1 - ty0) // 2,):
        d.ellipse([tx0 - 34, cy - 34, tx0 + 34, cy + 34], fill=GOLD)
        d.ellipse([tx1 - 34, cy - 34, tx1 + 34, cy + 34], fill=GOLD)
    for xx in range(tx0 + 60, tx1 - 60, 34):
        d.line([xx, ty0 + 26, xx + 16, ty0 + 26], fill=GOLD, width=3)
        d.line([xx, ty1 - 26, xx + 16, ty1 - 26], fill=GOLD, width=3)
    lab = "USE CODE AT CHECKOUT"
    f = inter(28, "Bold")
    d.text(((W - d.textlength(lab, font=f)) / 2, ty0 + 50), lab, font=f, fill=CREAM_DIM)
    code = "MORNING15"
    fc = anton(130)
    bb = d.textbbox((0, 0), code, font=fc)
    d.text(((W - (bb[2] - bb[0])) / 2 - bb[0], ty0 + 105 - bb[1]), code, font=fc, fill=GOLD)
    f2 = inter(32, "SemiBold")
    d.text((M, 1050), "First order only, one use per customer.", font=f2, fill=ESPRESSO)
    chrome(img, 6, False)
    sticker(img, False)
    return img


def s7():
    img = base(True)
    d = ImageDraw.Draw(img)
    from PIL import ImageFilter
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([240, 520, 840, 1120], fill=GOLD + (80,))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(110)))
    y = 170
    for ln in ["THE FIRST WIN", "OF YOUR DAY."]:
        d.text((M, y), ln, font=anton(136), fill=CREAM)
        y += 146
    d.rectangle([M, y + 16, M + 90, y + 24], fill=GOLD)
    mascot = Image.open(BK / "high_energy_guy_whitecolor.png").convert("RGBA").resize((440, 440), Image.LANCZOS)
    p = pack(300, angle=-6)
    shadow(p, img, (610, 540))
    img.alpha_composite(p, (610, 540))
    img.alpha_composite(mascot.rotate(8, expand=True, resample=Image.BICUBIC), (110, 560))
    # CTA bar
    bx0, by0, bx1, by1 = M, 1080, W - M, 1200
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=60, fill=GOLD)
    url = "thepowercoffee.com/pages/betterday"
    fu = inter(38, "Bold")
    d.text(((W - d.textlength(url, font=fu)) / 2, by0 + 37), url, font=fu, fill=ESPRESSO)
    chrome(img, 7, True)
    return img


def main():
    out = Path(sys.argv[1])
    slides = [
        s1(),
        step(2, "01", "MAKE YOUR COFFEE.", "The one you already love. Same mug, same machine, same time.",
             mug_icon(INK, 300), False),
        step(3, "02", "ADD ONE SCOOP.", "Stir it in and drink it the way you always do. No new routine to learn.",
             icon("ícones.png", CREAM, 300), True),
        s4(), s5(), s6(), s7(),
    ]
    for i, s in enumerate(slides, 1):
        s.convert("RGB").save(out / f"carousel_{i}.jpg", quality=92)
        print("saved", out / f"carousel_{i}.jpg")


if __name__ == "__main__":
    main()
