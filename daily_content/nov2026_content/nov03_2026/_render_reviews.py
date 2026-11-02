#!/usr/bin/env python3
"""Nov 3 2026 social-proof carousel (Leo: old one 'seems weird'; it described a meetup that
never happened). Real homepage reviews only, navy/cream Register B, www + Amazon footer."""
from pathlib import Path
import textwrap
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).resolve().parent
KIT = Path("/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit")
W, H = 1080, 1350
NAVY_DEEP, NAVY, BLUE, CREAM, DIM, GOLD = (10, 34, 66), (17, 58, 110), (66, 158, 235), (238, 230, 202), (196, 188, 158), (212, 163, 58)
ANTON = str(KIT / "fonts/Anton-Regular.ttf"); INTER = str(KIT / "fonts/Inter-Variable.ttf")
N = 6


def inter(size, w="SemiBold"):
    f = ImageFont.truetype(INTER, size)
    try: f.set_variation_by_name(w)
    except Exception: pass
    return f


def base(i, last=False):
    c = Image.new("RGBA", (W, H), NAVY_DEEP + (255,))
    dots = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dd = ImageDraw.Draw(dots)
    for y in range(0, H, 10):
        for x in range(0, W, 10):
            dd.ellipse((x, y, x + 2, y + 2), fill=CREAM + (16,))
    c.alpha_composite(dots)
    g = Image.new("L", (W, H), 0); ImageDraw.Draw(g).ellipse((560, -260, 1300, 420), fill=70)
    c.alpha_composite(Image.merge("RGBA", (*Image.new("RGB", (W, H), GOLD).split(), g.filter(ImageFilter.GaussianBlur(120)))))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle((44, 44, W - 44, H - 44), radius=6, outline=CREAM + (90,), width=3)
    f = inter(26, "ExtraBold")
    d.text((96, 104), "REAL CUSTOMERS", font=f, fill=GOLD)
    d.line((96 - 0, 150, 96 + 44, 150), fill=GOLD, width=3)
    pill = f"{i}/{N}"; pw = d.textlength(pill, font=inter(24, "Bold")) + 32
    d.rounded_rectangle((W - 96 - pw, 96, W - 96, 136), radius=20, fill=GOLD)
    d.text((W - 96 - pw + 16, 102), pill, font=inter(24, "Bold"), fill=NAVY_DEEP)
    ff = inter(26, "Bold")
    if last:
        amz = Image.open(KIT / "logos/amazon_logo_cream.png").convert("RGBA"); amz = amz.resize((int(amz.width * 34 / amz.height), 34))
        t = "WWW.THEPOWERCOFFEE.COM  ·  ALSO ON"; tw = d.textlength(t, font=ff); x = (W - tw - 14 - amz.width) / 2
        d.text((x, H - 120), t, font=ff, fill=CREAM); c.alpha_composite(amz, (int(x + tw + 14), H - 116))
    else:
        t = "@POWERCOFFEE.OFC  ·  SWIPE →"; d.text(((W - d.textlength(t, font=ff)) / 2, H - 120), t, font=ff, fill=DIM)
    return c, d


def mascot(c, pose, h, xy):
    m = Image.open(KIT / f"mascot_poses/{pose}").convert("RGBA"); m = m.crop(m.getbbox())
    m = m.resize((int(m.width * h / m.height), h), Image.LANCZOS)
    a = m.getchannel("A"); pad = 60
    glow = Image.new("L", (m.width + 2 * pad, m.height + 2 * pad), 0); glow.paste(a, (pad, pad))
    glow = glow.filter(ImageFilter.GaussianBlur(28)).point(lambda v: int(v * 0.55))
    layer = Image.new("RGBA", glow.size, CREAM + (0,)); layer.putalpha(glow)
    x, y = xy; c.alpha_composite(layer, (x - pad, y - pad)); c.alpha_composite(m, (x, y))


def anton_lines(d, lines, y, size, colors, x=92):
    f = ImageFont.truetype(ANTON, size)
    for line, col in zip(lines, colors):
        d.text((x, y), line, font=f, fill=col); y += int(size * 0.98)
    return y


def quote_slide(i, quote, name):
    c, d = base(i)
    d.text((84, 170), "“", font=ImageFont.truetype(ANTON, 300), fill=GOLD)
    f = inter(62, "SemiBold"); y = 420
    for line in textwrap.wrap(quote, 26):
        d.text((96, y), line, font=f, fill=CREAM); y += 84
    y += 40
    d.text((96, y), name.upper(), font=ImageFont.truetype(ANTON, 64), fill=GOLD)
    d.text((96, y + 84), "Customer review", font=inter(32, "Medium"), fill=DIM)
    d.text((96, H - 176), "Individual experiences. Results may vary.", font=inter(24, "Regular"), fill=DIM)
    return c


slides = []
c, d = base(1)
y = anton_lines(d, ["REAL CUSTOMERS.", "REAL MORNINGS."], 300, 128, [CREAM, BLUE])
fs = inter(42, "Medium")
for k, line in enumerate(["What people told us after making", "it part of their morning."]):
    d.text((96, y + 50 + k * 58), line, font=fs, fill=DIM)
mascot(c, "pose_pointing_cutout.png", 470, (610, 760)); slides.append(c)
slides.append(quote_slide(2, "I drank it before going for a run in the morning… I didn't feel the usual crash of energy mid-morning.", "Renata Silvano"))
slides.append(quote_slide(3, "I've been drinking it every morning and feeling great… It's already part of my daily routine.", "Rita Batista"))
slides.append(quote_slide(4, "The natural herbal aroma captivated me right away, and the taste… I'm speechless!", "Welma Santos"))
c, d = base(5)
y = anton_lines(d, ["ONE SCOOP.", "THE COFFEE YOU", "ALREADY DRINK."], 300, 140, [CREAM, BLUE, BLUE])
d.rounded_rectangle((92, y + 70, W - 92, y + 190), radius=60, fill=GOLD)
t = "FREE SHIPPING ON YOUR FIRST ORDER · FIRST10"; f = inter(34, "ExtraBold")
d.text(((W - d.textlength(t, font=f)) / 2, y + 108), t, font=f, fill=NAVY_DEEP)
slides.append(c)
c, d = base(6, last=True)
anton_lines(d, ["YOUR TURN.", "FIRST WIN OF", "THE DAY."], 220, 140, [CREAM, BLUE, BLUE])
mascot(c, "pose_fistpump.png", 440, (330, 760)); slides.append(c)
for n, s in enumerate(slides, 1):
    s.convert("RGB").save(HERE / f"carousel_{n}.jpg", quality=92)
print("wrote", len(slides))
