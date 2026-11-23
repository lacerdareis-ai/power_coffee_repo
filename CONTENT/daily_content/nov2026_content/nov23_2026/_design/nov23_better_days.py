#!/usr/bin/env python3
"""
nov23_better_days.py: Nov 23, 2026 carousel + Story + LinkedIn image ("You don't need more hours.").

Brand-purpose post: The Power Coffee exists to help people have better days, with more focus and energy.
Problem-led (a day slipping away, told by the clock), then the purpose, then the answer. No ingredient or
feature talk. Copy matches the day's content.md word for word.

Usage: python3 nov23_better_days.py <day_folder>
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).parent))
import nov20_one_scoop as k  # noqa: E402  (shared fonts, colors, pack, icons, chrome)

W, H, M = k.W, k.H, k.M
ESP, CREAM, GOLD, INK, GRAY, DIM = k.ESPRESSO, k.CREAM, k.GOLD, k.INK, k.GRAY, k.CREAM_DIM
k.TOTAL = 7


def eyebrow(d, y, text, color):
    d.rectangle([M, y + 14, M + 46, y + 20], fill=color)
    d.text((M + 62, y), text, font=k.inter(30, "Bold"), fill=color)


def headline(d, y, text, size, fill, mw=W - 2 * M, lh=1.04):
    f = k.anton(size)
    for ln in k.wrap(d, text, f, mw):
        d.text((M, y), ln, font=f, fill=fill)
        y += int(size * lh)
    return y


def body(d, y, text, fill, size=42, mw=W - 2 * M):
    f = k.inter(size, "Medium")
    return k.text_block(d, M, y, k.wrap(d, text, f, mw), f, fill, int(size * 1.42))


def day_bar(d, y, frac, dark, label):
    """A day from 6am to 10pm with a marker at the current time: the energy left in the tank."""
    x0, x1 = M, W - M
    track = (70, 62, 56) if dark else (222, 212, 192)
    d.rounded_rectangle([x0, y, x1, y + 14], radius=7, fill=track)
    xm = x0 + int((x1 - x0) * frac)
    d.rounded_rectangle([x0, y, xm, y + 14], radius=7, fill=GOLD)
    d.ellipse([xm - 20, y - 13, xm + 20, y + 27], fill=GOLD, outline=ESP if not dark else CREAM, width=5)
    f = k.inter(24, "SemiBold")
    c = DIM if dark else GRAY
    d.text((x0, y + 34), "6 AM", font=f, fill=c)
    d.text((x1 - d.textlength("10 PM", font=f), y + 34), "10 PM", font=f, fill=c)
    lw = d.textlength(label, font=f)
    lx = min(max(xm - lw / 2, x0 + 90), x1 - 90 - lw)
    d.text((lx, y - 52), label, font=k.inter(24, "Bold"), fill=GOLD)


def clock_slide(n, time, frac, bar_label, head, text, dark):
    img = k.base(dark)
    d = ImageDraw.Draw(img)
    fg = CREAM if dark else INK
    eyebrow(d, 190, "THE PROBLEM", GOLD if dark else k.GOLD_DEEP)
    d.text((M - 6, 240), time, font=k.anton(260), fill=GOLD if dark else INK)
    day_bar(d, 660, frac, dark, bar_label)
    y = headline(d, 780, head, 112, fg, mw=720)
    body(d, y + 40, text, DIM if dark else GRAY, size=44)
    k.chrome(img, n, dark)
    return img


def s1():
    img = k.base(True)
    d = ImageDraw.Draw(img)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([520, -200, 1300, 580], fill=GOLD + (70,))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(120)))
    eyebrow(d, 210, "WHY THE POWER COFFEE EXISTS", GOLD)
    y = headline(d, 300, "YOU DON'T NEED MORE HOURS.", 150, CREAM)
    y = headline(d, y + 10, "YOU NEED BETTER ONES.", 150, GOLD)
    f = k.inter(34, "SemiBold")
    d.text((M, H - 190), "Swipe  →", font=f, fill=DIM)
    k.chrome(img, 1, True)
    k.sticker(img, True)
    return img


def s5():
    img = Image.new("RGBA", (W, H), GOLD + (255,))
    d = ImageDraw.Draw(img)
    eyebrow(d, 170, "WHY WE EXIST", ESP)
    y = headline(d, 250, "THAT'S THE DAY WE BUILT THIS FOR.", 120, ESP)
    y = body(d, y + 40, "The Power Coffee has one purpose: to help people have better days, with more focus "
                        "and more energy for the work, the people and the faith that matter to them.", ESP, size=50)
    m = Image.open(k.BK / "high_energy_guy.png").convert("RGBA").resize((400, 400), Image.LANCZOS)
    img.alpha_composite(m.rotate(-8, expand=True, resample=Image.BICUBIC), (W - 500, H - 540))
    k.chrome(img, 5, False)
    return img


def s6():
    img = k.base(False)
    d = ImageDraw.Draw(img)
    eyebrow(d, 170, "OUR ANSWER", k.GOLD_DEEP)
    y = headline(d, 250, "NOT A NEW ROUTINE. A BETTER ONE.", 118, INK, mw=W - 2 * M)
    body(d, y + 36, "One scoop in the coffee you already drink. Designed to support focus and steady energy "
                    "into the afternoon, without stacking another cup.", GRAY, size=42, mw=560)
    p = k.pack(330, angle=-5)
    k.shadow(p, img, (W - M - 330, H - 560), alpha=80)
    img.alpha_composite(p, (W - M - 330, H - 560))
    k.chrome(img, 6, False)
    return img


def s7():
    img = k.base(True)
    d = ImageDraw.Draw(img)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([240, 520, 840, 1120], fill=GOLD + (80,))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(110)))
    y = headline(d, 150, "MORE FOCUS.", 120, CREAM)
    y = headline(d, y, "MORE ENERGY.", 120, CREAM)
    headline(d, y, "BETTER DAYS.", 120, GOLD)
    mascot = Image.open(k.BK / "high_energy_guy_whitecolor.png").convert("RGBA").resize((400, 400), Image.LANCZOS)
    p = k.pack(280, angle=-6)
    k.shadow(p, img, (630, 600))
    img.alpha_composite(p, (630, 600))
    img.alpha_composite(mascot.rotate(8, expand=True, resample=Image.BICUBIC), (120, 620))
    bx0, by0, bx1, by1 = M, 1080, W - M, 1200
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=60, fill=GOLD)
    url = "thepowercoffee.com/pages/betterday"
    fu = k.inter(38, "Bold")
    d.text(((W - d.textlength(url, font=fu)) / 2, by0 + 37), url, font=fu, fill=ESP)
    k.chrome(img, 7, True)
    return img


def story():
    SW, SH = 1080, 1920
    img = Image.new("RGBA", (SW, SH), ESP + (255,))
    d = ImageDraw.Draw(img)
    glow = Image.new("RGBA", (SW, SH), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([300, 1000, 1000, 1700], fill=GOLD + (80,))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(130)))
    eyebrow(d, 300, "WHY THE POWER COFFEE EXISTS", GOLD)
    y = headline(d, 390, "YOU DON'T NEED MORE HOURS.", 150, CREAM)
    y = headline(d, y + 10, "YOU NEED BETTER ONES.", 150, GOLD)
    body(d, y + 40, "More focus and energy for the work, the people and the faith that matter.", DIM, size=44)
    m = Image.open(k.BK / "high_energy_guy_whitecolor.png").convert("RGBA").resize((420, 420), Image.LANCZOS)
    img.alpha_composite(m.rotate(8, expand=True, resample=Image.BICUBIC), ((SW - 440) // 2, 1150))
    bx0, by0, bx1, by1 = M, 1640, SW - M, 1760
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=60, fill=GOLD)
    url = "thepowercoffee.com/pages/betterday"
    fu = k.inter(38, "Bold")
    d.text(((SW - d.textlength(url, font=fu)) / 2, by0 + 37), url, font=fu, fill=ESP)
    d.text((M, 160), "@POWERCOFFEE.OFC", font=k.inter(28, "SemiBold"), fill=DIM)
    return img


def main():
    out = Path(sys.argv[1])
    slides = [
        s1(),
        clock_slide(2, "9:00", 0.19, "FULL TANK", "THE DAY STARTS STRONG.",
                    "Coffee in hand, a plan for the week, real intentions. Monday feels winnable.", False),
        clock_slide(3, "2:15", 0.52, "AFTER LUNCH", "THEN THE FOG ROLLS IN.",
                    "You reread the same email three times. The plan you made at 9 quietly falls apart.", True),
        clock_slide(4, "6:30", 0.78, "RUNNING ON EMPTY", "AND HOME GETS WHAT'S LEFT.",
                    "You walk in the door with nothing left for the people you were working for in the first place.",
                    False),
        s5(), s6(), s7(),
    ]
    for i, s in enumerate(slides, 1):
        s.convert("RGB").save(out / f"carousel_{i}.jpg", quality=92)
        print("saved", out / f"carousel_{i}.jpg")
    story().convert("RGB").save(out / "story.jpg", quality=92)
    li = s1().convert("RGB")
    li.save(out / "linkedin.jpg", quality=92)
    print("saved story.jpg, linkedin.jpg")


if __name__ == "__main__":
    main()
