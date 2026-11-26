#!/usr/bin/env python3
"""
nov27_your_day.py: an 8-slide problem-first carousel for Nov 27, 2026, "You know this day."

The customer's regular day, hour by hour (5:30am alarm → lunch on the go → post-lunch slump →
second cup → home with nothing left), then the turn (one scoop in the first cup) and the CTA.
A battery drains across the day as a visual hook.

Same graphic system as nov20_one_scoop.py, but in NAVY and CREAM (brand rule: never a black
background). Every slide carries www.thepowercoffee.com plus the Amazon logo (brand rule) and no
/pages/ links. The copy matches the day's content.md.

Usage: python3 nov27_your_day.py <day_folder>
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BK = Path.home() / "Documents/Claude/The_Power_Coffee/Sales_motor/00-Brand/brand_kit"
FONTS, CUT = BK / "fonts", BK / "cutouts"
W, H, M = 1080, 1350, 90
NAVY_DEEP, NAVY, NAVY_LINE = (10, 34, 66), (17, 58, 110), (40, 74, 120)
CREAM, CREAM_DIM, GOLD, CORAL = (238, 230, 202), (196, 188, 158), (212, 163, 58), (217, 115, 78)
INK_NAVY, GRAY_NAVY = (10, 34, 66), (70, 86, 110)
TOTAL = 8
TIMES = ["5:30", "12:30", "2:00", "3:00", "6:30"]


def anton(s): return ImageFont.truetype(str(FONTS / "Anton-Regular.ttf"), s)


def inter(s, w="Regular"):
    f = ImageFont.truetype(str(FONTS / "Inter-Variable.ttf"), s)
    try: f.set_variation_by_name(w)
    except Exception: pass
    return f


def wrap(d, text, f, mw):
    out, line = [], ""
    for w in text.split():
        t = (line + " " + w).strip()
        if d.textlength(t, font=f) <= mw: line = t
        else: out.append(line); line = w
    if line: out.append(line)
    return out


def base(bg):
    img = Image.new("RGBA", (W, H), bg + (255,))
    if bg == NAVY_DEEP:  # soft lift so navy never reads flat/black
        g = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(g).ellipse([-200, -300, 1300, 900], fill=NAVY + (150,))
        img.alpha_composite(g.filter(ImageFilter.GaussianBlur(180)))
    return img


def pack(width, angle=0):
    p = Image.open(CUT / "frente.png").convert("RGBA")
    p = p.crop(p.split()[3].point(lambda v: 255 if v > 200 else 0).getbbox())
    p = p.resize((width, int(p.height * width / p.width)), Image.LANCZOS)
    return p.rotate(angle, expand=True, resample=Image.BICUBIC) if angle else p


def shadow(img, el, xy, blur=26, alpha=120):
    a = el.split()[3].point(lambda v: alpha if v > 10 else 0)
    pad = blur * 3
    big = Image.new("RGBA", (el.width + pad * 2, el.height + pad * 2), (0, 0, 0, 0))
    sh = Image.new("RGBA", el.size, (0, 0, 0, 255)); sh.putalpha(a)
    big.paste(sh, (pad, pad), sh)
    img.alpha_composite(big.filter(ImageFilter.GaussianBlur(blur)), (xy[0] - pad + 14, xy[1] - pad + 24))


def battery(d, x, y, w, h, level, outline, empty_fill):
    lw = max(4, w // 40)
    d.rounded_rectangle([x, y, x + w, y + h], radius=h // 5, outline=outline, width=lw)
    d.rounded_rectangle([x + w + lw, y + h * 0.3, x + w + lw + w // 18, y + h * 0.7], radius=4, fill=outline)
    inner = w - lw * 4
    fill_w = max(0, int(inner * level))
    color = GOLD if level > 0.3 else CORAL
    d.rounded_rectangle([x + lw * 2, y + lw * 2, x + lw * 2 + inner, y + h - lw * 2], radius=h // 8, fill=empty_fill)
    if fill_w:
        d.rounded_rectangle([x + lw * 2, y + lw * 2, x + lw * 2 + fill_w, y + h - lw * 2], radius=h // 8, fill=color)


def chrome(img, n, dark):
    d = ImageDraw.Draw(img)
    fg, dim = (CREAM, CREAM_DIM) if dark else (INK_NAVY, GRAY_NAVY)
    f = inter(28, "Bold"); lab = f"{n:02d}/{TOTAL:02d}"; tw = d.textlength(lab, font=f)
    d.rounded_rectangle([W - 40 - tw - 44, 40, W - 40, 94], radius=27, outline=GOLD if dark else INK_NAVY, width=3)
    d.text((W - 40 - tw - 22, 50), lab, font=f, fill=GOLD if dark else INK_NAVY)
    d.text((M, 52), "@POWERCOFFEE.OFC", font=inter(26, "Bold"), fill=dim)
    # footer: website + Amazon logo on every slide (brand rule)
    fu = inter(28, "SemiBold")
    d.text((M, H - 78), "www.thepowercoffee.com", font=fu, fill=fg)
    x = M + d.textlength("www.thepowercoffee.com", font=fu) + 24
    d.line([x, H - 76, x, H - 40], fill=dim, width=2)
    logo = Image.open(BK / "logos" / ("amazon_logo_cream.png" if dark else "amazon_logo_navy.png")).convert("RGBA")
    logo = logo.resize((int(logo.width * 34 / logo.height), 34), Image.LANCZOS)
    img.alpha_composite(logo, (int(x + 24), H - 74))


def sticker(img, dark, size=160):
    s = Image.open(BK / ("high_energy_guy_whitecolor.png" if dark else "high_energy_guy.png")).convert("RGBA")
    s = s.resize((size, size), Image.LANCZOS).rotate(10, expand=True, resample=Image.BICUBIC)
    img.alpha_composite(s, (W - s.width - 30, H - s.height - 20))


def timeline(d, active):
    """Five dots across the day, the current one highlighted."""
    y, x0, x1 = 1130, M, W - M - 190
    d.line([x0, y, x1, y], fill=NAVY_LINE, width=4)
    step = (x1 - x0) / (len(TIMES) - 1)
    f = inter(22, "Bold")
    for i, t in enumerate(TIMES):
        cx = x0 + i * step
        on = i == active
        r = 13 if on else 8
        d.ellipse([cx - r, y - r, cx + r, y + r], fill=GOLD if on else (CREAM_DIM if i < active else NAVY_LINE))
        tw = d.textlength(t, font=f)
        d.text((cx - tw / 2, y + 22), t, font=f, fill=GOLD if on else CREAM_DIM)


# ── slides ────────────────────────────────────────────────────────────────────

def s_cover():
    img = base(NAVY_DEEP); d = ImageDraw.Draw(img)
    d.text((M, 190), "YOU KNOW", font=anton(200), fill=CREAM)
    d.text((M, 410), "THIS DAY.", font=anton(200), fill=GOLD)
    f = inter(40, "SemiBold")
    d.text((M, 700), "Hour by hour. Swipe →", font=f, fill=CREAM_DIM)
    # five batteries draining left to right
    levels, bw, gap = [0.9, 0.6, 0.3, 0.2, 0.05], 150, 30
    by = 860
    for i, lv in enumerate(levels):
        x = M + i * (bw + gap)
        battery(d, x, by, bw, 84, lv, CREAM, NAVY)
        t = TIMES[i]; ft = inter(24, "Bold")
        d.text((x + (bw - d.textlength(t, font=ft)) / 2, by + 104), t, font=ft, fill=CREAM_DIM)
    chrome(img, 1, True); sticker(img, True)
    return img


def s_hour(n, idx, time, ampm, level, head, body):
    img = base(NAVY_DEEP); d = ImageDraw.Draw(img)
    size = 290  # shrink long times (12:30) so time + AM/PM never reach the battery
    while size > 180 and d.textlength(time, font=anton(size)) + 16 + d.textlength(ampm, font=anton(90)) > W - 2 * M - 270:
        size -= 10
    ft = anton(size)
    d.text((M - 6, 120 + (290 - size) * 0.9), time, font=ft, fill=GOLD)
    tw = d.textlength(time, font=ft)
    d.text((M + tw + 16, 330), ampm, font=anton(90), fill=GOLD)
    battery(d, W - M - 230, 210, 200, 96, level, CREAM, NAVY)
    pct = f"{int(round(level * 100))}%"
    fp = inter(30, "Bold")
    d.text((W - M - 230 + (200 - d.textlength(pct, font=fp)) / 2, 320), pct, font=fp,
           fill=CORAL if level <= 0.3 else CREAM_DIM)
    y = 560
    for ln in wrap(d, head, anton(124), W - 2 * M):
        d.text((M, y), ln, font=anton(124), fill=CREAM); y += 132
    d.rectangle([M, y + 18, M + 90, y + 26], fill=GOLD)
    fb = inter(40)
    y += 70
    for ln in wrap(d, body, fb, W - 2 * M - 40):
        d.text((M, y), ln, font=fb, fill=CREAM_DIM); y += 58
    timeline(d, idx)
    chrome(img, n, True); sticker(img, True, 140)
    return img


def s_turn():
    img = base(CREAM); d = ImageDraw.Draw(img)
    y = 170
    for ln in ["WHAT IF THE", "CHANGE STARTED", "WITH YOUR", "FIRST CUP?"]:
        d.text((M, y), ln, font=anton(118), fill=GOLD if ln == "FIRST CUP?" else INK_NAVY); y += 126
    d.rectangle([M, y + 16, M + 90, y + 24], fill=GOLD)
    fb = inter(36); y += 66
    body = ("One scoop of Power Coffee in the coffee you already make. Matcha, taurine, ginkgo biloba, "
            "Ceylon cinnamon and ginger, with 0g sugar. Designed to support steady energy and focus "
            "through the afternoon.*")
    for ln in wrap(d, body, fb, 560):
        d.text((M, y), ln, font=fb, fill=GRAY_NAVY); y += 52
    p = pack(330, angle=6)
    shadow(p, img, (W - M - p.width + 40, 690), alpha=70)
    img.alpha_composite(p, (W - M - p.width + 40, 690))
    chrome(img, 7, False)
    return img


def s_cta():
    img = base(NAVY_DEEP); d = ImageDraw.Draw(img)
    y = 160
    for ln in ["THE FIRST WIN", "OF YOUR DAY."]:
        d.text((M, y), ln, font=anton(140), fill=CREAM); y += 150
    d.rectangle([M, y + 16, M + 90, y + 24], fill=GOLD)
    battery(d, M, y + 70, 230, 100, 1.0, CREAM, NAVY)
    d.text((M, y + 190), "Start the day charged.", font=inter(36, "SemiBold"), fill=CREAM_DIM)
    p = pack(290, angle=-6)
    shadow(p, img, (W - M - p.width + 20, 525))
    img.alpha_composite(p, (W - M - p.width + 20, 525))
    # offer chip
    f = inter(34, "Bold"); t = "FIRST ORDER? 15% OFF · CODE MORNING15"
    tw = d.textlength(t, font=f)
    d.rounded_rectangle([(W - tw) / 2 - 36, 960, (W + tw) / 2 + 36, 1040], radius=40, fill=GOLD)
    d.text(((W - tw) / 2, 980), t, font=f, fill=NAVY_DEEP)
    f2 = inter(24)
    t2 = "First order only, one use per customer, at www.thepowercoffee.com."
    d.text(((W - d.textlength(t2, font=f2)) / 2, 1062), t2, font=f2, fill=CREAM_DIM)
    chrome(img, 8, True); sticker(img, True, 150)
    return img


def main():
    out = Path(sys.argv[1])
    slides = [
        s_cover(),
        s_hour(2, 0, "5:30", "AM", 0.9, "THE ALARM WINS.",
               "Coffee in one hand, keys in the other. Out the door before the sun."),
        s_hour(3, 1, "12:30", "PM", 0.6, "LUNCH ON THE GO.",
               "In the truck, at the counter, standing up. Ten minutes, if you're lucky."),
        s_hour(4, 2, "2:00", "PM", 0.3, "THE POST-LUNCH SLUMP.",
               "Eyes heavy. Half the day still ahead of you."),
        s_hour(5, 3, "3:00", "PM", 0.2, "CUP NUMBER TWO.",
               "Most people say it doesn't fix the slump. And it's still with you at bedtime."),
        s_hour(6, 4, "6:30", "PM", 0.05, "HOME. EMPTY TANK.",
               "The people waiting for you get whatever is left of you."),
        s_turn(),
        s_cta(),
    ]
    for i, s in enumerate(slides, 1):
        s.convert("RGB").save(out / f"carousel_{i}.jpg", quality=92)
    print(f"saved {len(slides)} slides to {out}")


if __name__ == "__main__":
    main()
