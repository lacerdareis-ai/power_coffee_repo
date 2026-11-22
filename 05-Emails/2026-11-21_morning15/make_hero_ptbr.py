"""Hero for the MORNING15 email (1200x1400, shown at 600 wide). Navy/cream, no black."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
BK = Path.home() / "Documents/Claude/The_Power_Coffee/Sales_motor/00-Brand/brand_kit"
NAVY_DEEP, NAVY, CREAM, CREAM_DIM, GOLD = (10, 34, 66), (17, 58, 110), (238, 230, 202), (196, 188, 158), (212, 163, 58)
W, H = 1200, 1400
def anton(s): return ImageFont.truetype(str(BK / "fonts/Anton-Regular.ttf"), s)
def inter(s, w="Regular"):
    f = ImageFont.truetype(str(BK / "fonts/Inter-Variable.ttf"), s)
    try: f.set_variation_by_name(w)
    except Exception: pass
    return f
img = Image.new("RGBA", (W, H), NAVY_DEEP + (255,))
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(glow).ellipse([200, 620, 1000, 1420], fill=NAVY + (255,))
img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(140)))
d = ImageDraw.Draw(img)
def ctext(y, t, f, fill):
    d.text(((W - d.textlength(t, font=f)) / 2, y), t, font=f, fill=fill)
d.rectangle([570, 80, 630, 86], fill=GOLD)
ctext(118, "A PRIMEIRA VITÓRIA DO SEU DIA.", inter(34, "Bold"), GOLD)
ctext(190, "15% OFF", anton(250), CREAM)
ctext(500, "na sua primeira compra com o código MORNING15", inter(40, "SemiBold"), CREAM_DIM)
p = Image.open(BK / "cutouts/frente.png").convert("RGBA")
p = p.crop(p.split()[3].point(lambda v: 255 if v > 200 else 0).getbbox())
p = p.resize((560, int(p.height * 560 / p.width)), Image.LANCZOS)
sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sh).ellipse([360, 1250, 840, 1320], fill=(0, 0, 0, 120))
img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(24)))
px, py = (W - p.width) // 2, 600
img.alpha_composite(p, (px, py))
# step chips
f = inter(30, "Bold")
chips = ["0 G DE AÇÚCAR", "11 INGREDIENTES", "FEITO NOS EUA"]
ws = [d.textlength(c, font=f) + 60 for c in chips]
x = (W - (sum(ws) + 24 * (len(ws) - 1))) / 2; y = 1300
for c, w in zip(chips, ws):
    d.rounded_rectangle([x, y, x + w, y + 64], radius=32, fill=CREAM)
    d.text((x + 30, y + 14), c, font=f, fill=NAVY_DEEP)
    x += w + 24
img.convert("RGB").save(Path(__file__).with_name("email_hero_offer.jpg"), quality=90)
