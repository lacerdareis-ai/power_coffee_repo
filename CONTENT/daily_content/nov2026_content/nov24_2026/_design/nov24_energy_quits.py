#!/usr/bin/env python3
"""
nov24_energy_quits.py: Nov 24, 2026 carousel + Story ("Your energy quits before you do.").

Problem-first social proof (Leo's rules, CONTENT_RULES_ACTIVE.md): trigger on slide 1, the crash as the
problem, real customer words as proof, website + Amazon CTA. Same design system as nov23_better_days.py.

Usage: python3 nov24_energy_quits.py <day_folder>
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).parent))
import nov20_one_scoop as k  # noqa: E402
import nov23_better_days as b  # noqa: E402

W, H, M = k.W, k.H, k.M
ESP, CREAM, GOLD, INK, GRAY, DIM = k.ESPRESSO, k.CREAM, k.GOLD, k.INK, k.GRAY, k.CREAM_DIM
k.TOTAL = 7


def glow(img, box, a=75):
    g = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(g).ellipse(box, fill=GOLD + (a,))
    img.alpha_composite(g.filter(ImageFilter.GaussianBlur(120)))


def s1():
    img = k.base(True)
    d = ImageDraw.Draw(img)
    glow(img, [520, -200, 1300, 580])
    b.eyebrow(d, 210, "SOUND FAMILIAR?", GOLD)
    y = b.headline(d, 300, "YOUR ENERGY", 150, CREAM)
    y = b.headline(d, y, "QUITS BEFORE", 150, CREAM)
    y = b.headline(d, y, "YOU DO.", 150, GOLD)
    b.body(d, y + 40, "Four real people who were done with the crash.", DIM, size=44)
    d.text((M, H - 190), "Swipe  →", font=k.inter(34, "SemiBold"), fill=DIM)
    k.chrome(img, 1, True)
    k.sticker(img, True)
    return img


def s2():
    img = k.base(False)
    d = ImageDraw.Draw(img)
    b.eyebrow(d, 190, "THE PROBLEM", k.GOLD_DEEP)
    y = b.headline(d, 270, "IT'S NOT A WILLPOWER PROBLEM.", 128, INK, mw=860)
    b.body(d, y + 40, "You start the day strong. Then mid-morning, or right after lunch, the tank empties "
                      "and the plan falls apart. Another cup rarely fixes it.", GRAY, size=46)
    k.chrome(img, 2, False)
    return img


def quote(n, name, who, text, dark):
    img = k.base(dark)
    d = ImageDraw.Draw(img)
    fg = CREAM if dark else INK
    b.eyebrow(d, 190, "WHAT CHANGED FOR " + name.upper(), GOLD if dark else k.GOLD_DEEP)
    f = k.inter(76, "SemiBold")
    lines = k.wrap(d, text, f, W - 2 * M)
    y0 = max(500, int((H - (len(lines) * 104 + 170)) / 2) + 90)
    d.text((M - 10, y0 - 280), "“", font=k.anton(300), fill=GOLD)
    y = k.text_block(d, M, y0, lines, f, fg, 104)
    d.rectangle([M, y + 40, M + 60, y + 46], fill=GOLD)
    d.text((M, y + 70), name + (", " + who if who else ""), font=k.inter(42, "Bold"), fill=fg)
    d.text((M, H - 140), "Individual experience. Results vary.", font=k.inter(26, "Medium"),
           fill=DIM if dark else GRAY)
    k.chrome(img, n, dark)
    return img


def s7():
    img = k.base(True)
    d = ImageDraw.Draw(img)
    glow(img, [240, 480, 840, 1080], 80)
    y = b.headline(d, 150, "WIN BACK", 130, CREAM)
    y = b.headline(d, y, "YOUR AFTERNOON.", 130, GOLD)
    mascot = Image.open(k.BK / "high_energy_guy_whitecolor.png").convert("RGBA").resize((380, 380), Image.LANCZOS)
    p = k.pack(270, angle=-6)
    k.shadow(p, img, (640, 500))
    img.alpha_composite(p, (640, 500))
    img.alpha_composite(mascot.rotate(8, expand=True, resample=Image.BICUBIC), (130, 560))
    bx0, by0, bx1, by1 = M, 1040, W - M, 1160
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=60, fill=GOLD)
    url = "thepowercoffee.com/pages/betterday"
    fu = k.inter(38, "Bold")
    d.text(((W - d.textlength(url, font=fu)) / 2, by0 + 37), url, font=fu, fill=ESP)
    b.amazon_line(d, W, by1 + 26)
    k.chrome(img, 7, True)
    return img


def story():
    SW, SH = 1080, 1920
    img = Image.new("RGBA", (SW, SH), ESP + (255,))
    d = ImageDraw.Draw(img)
    glow(img, [300, 1000, 1000, 1700], 80)
    d.text((M, 160), "@POWERCOFFEE.OFC", font=k.inter(28, "SemiBold"), fill=DIM)
    b.eyebrow(d, 300, "SOUND FAMILIAR?", GOLD)
    y = b.headline(d, 390, "YOUR ENERGY", 150, CREAM)
    y = b.headline(d, y, "QUITS BEFORE", 150, CREAM)
    y = b.headline(d, y, "YOU DO.", 150, GOLD)
    b.body(d, y + 40, "“I didn't feel the usual crash of energy mid-morning.” Renata. "
                      "Individual experience, results vary.", DIM, size=44)
    m = Image.open(k.BK / "high_energy_guy_whitecolor.png").convert("RGBA").resize((400, 400), Image.LANCZOS)
    img.alpha_composite(m.rotate(8, expand=True, resample=Image.BICUBIC), ((SW - 420) // 2, 1150))
    bx0, by0, bx1, by1 = M, 1600, SW - M, 1720
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=60, fill=GOLD)
    url = "thepowercoffee.com/pages/betterday"
    fu = k.inter(38, "Bold")
    d.text(((SW - d.textlength(url, font=fu)) / 2, by0 + 37), url, font=fu, fill=ESP)
    b.amazon_line(d, SW, by1 + 30)
    return img


def main():
    out = Path(sys.argv[1])
    slides = [
        s1(), s2(),
        quote(3, "Renata", "before a morning run", "I didn't feel the usual crash of energy mid-morning.", True),
        quote(4, "Welma", "", "Each sip recharged my energy and boosted my focus.", False),
        quote(5, "Rita", "", "I've been drinking it every morning and feeling great, with more energy and "
                            "disposition.", True),
        quote(6, "Lucas", "Leo's brother", "Helped me keep focused throughout the day.", False),
        s7(),
    ]
    for i, s in enumerate(slides, 1):
        s.convert("RGB").save(out / f"carousel_{i}.jpg", quality=92)
    story().convert("RGB").save(out / "story.jpg", quality=92)
    s1().convert("RGB").save(out / "linkedin.jpg", quality=92)
    print("saved carousel_1-7, story.jpg, linkedin.jpg")


if __name__ == "__main__":
    main()
