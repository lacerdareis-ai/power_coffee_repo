#!/usr/bin/env python3
"""
Fuel Check — Slide 1, v2. Same hook/mascot as v1, but:
  - no black anywhere (standing rule, Leo 2026-09-27)
  - real photo background, treated as a navy/cream halftone duotone
    (the vintage-athletic screen-print technique — matches the mascot's own
    line work) instead of a flat color panel
Background source: img_28_power.png — the "person striding through city,
sustained energy" PERSONA shot. Chosen deliberately: no product pack in
frame, so it can't carry the fabricated-label defect found earlier today in
15 of the 24 pack photos (see swipe_file/README.md section 3).
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
MARGIN = 108

NAVY        = (17, 58, 110)
NAVY_DEEP   = (10, 34, 66)     # for the headline block — same family, just darker, not black
BORDER_BLUE = (66, 158, 235)
CREAM       = (238, 230, 202)
CREAM_DIM   = (196, 188, 158)
GOLD        = (212, 163, 58)

FONTS  = "/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/fonts"
MASCOT = "/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/mascot_poses/pose_pointing_cutout.png"
PHOTO  = "/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/images/img_28_power.png"

def anton(size):
    return ImageFont.truetype(f"{FONTS}/Anton-Regular.ttf", size)

def inter(size, weight="Regular"):
    f = ImageFont.truetype(f"{FONTS}/Inter-Variable.ttf", size)
    try: f.set_variation_by_name(weight)
    except Exception: pass
    return f

def tracked_text(d, xy, text, font, fill, tracking=0, anchor_right=False):
    widths = [d.textlength(ch, font=font) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x, y = xy
    if anchor_right:
        x = x - total
    for ch, w in zip(text, widths):
        d.text((x, y), ch, font=font, fill=fill)
        x += w + tracking

def cover_fit(im, w, h):
    """Crop+resize a photo to exactly fill (w,h), like CSS object-fit: cover."""
    src_r = im.width / im.height
    dst_r = w / h
    if src_r > dst_r:
        new_h = h
        new_w = int(h * src_r)
    else:
        new_w = w
        new_h = int(w / src_r)
    im = im.resize((new_w, new_h), Image.LANCZOS)
    x0 = (new_w - w) // 2
    y0 = (new_h - h) // 2
    return im.crop((x0, y0, x0 + w, y0 + h))

def halftone_duotone(im, cell=5, dark=NAVY, light=CREAM):
    """Continuous navy/cream duotone (keeps the photo recognizable) with a
    fine newspaper-pitch halftone dot layer for the screen-print texture —
    a coarse dot grid (tried first at cell=9) turned the subject into
    unrecognizable blobs, which defeats the point of using a real photo."""
    gray = im.convert("L")

    def lut(lo, hi):
        return [int(lo + (hi - lo) * (i / 255)) for i in range(256)]
    # dark photo pixels (i=0) -> dark(navy); light photo pixels (i=255) -> light(cream)
    r, g, b = [gray.point(lut(dark[i], light[i])) for i in range(3)]
    duotone = Image.merge("RGB", (r, g, b))

    small = gray.resize((max(1, W // cell), max(1, H // cell)), Image.BOX)
    dots = Image.new("L", (W, H), 0)
    dd = ImageDraw.Draw(dots)
    px = small.load()
    for gy in range(small.height):
        for gx in range(small.width):
            v = px[gx, gy] / 255.0
            rad = (1 - v) * (cell * 0.62)
            if rad < 0.5:
                continue
            cx, cy = gx * cell + cell / 2, gy * cell + cell / 2
            dd.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], fill=255)
    navy_layer = Image.new("RGB", (W, H), dark)
    out = Image.composite(navy_layer, duotone, dots.point(lambda v: int(v * 0.55)))
    return out

img = Image.new("RGB", (W, H), NAVY)

# ── background: real photo, halftone-duotone treated ───────────────────────
photo = Image.open(PHOTO).convert("RGB")
photo = cover_fit(photo, W, H)
bg = halftone_duotone(photo, cell=9)
img.paste(bg, (0, 0))

d = ImageDraw.Draw(img)

# ── decorative card border (fixed layout anchor for the series) ────────────
border_inset = 44
d.rectangle([border_inset, border_inset, W - border_inset, H - border_inset], outline=CREAM, width=4)

# ── top scrim band so the eyebrow row stays legible over a busy sky/building
# area regardless of what the photo underneath happens to be ───────────────
top_band_h = 168
d.rectangle([border_inset + 4, border_inset + 4, W - border_inset - 4, top_band_h], fill=NAVY_DEEP)

eyebrow_y = 96
ef = inter(30, "Bold")
tracked_text(d, (MARGIN, eyebrow_y), "FUEL CHECK", ef, GOLD, tracking=4)
cf = inter(30, "SemiBold")
tracked_text(d, (W - MARGIN, eyebrow_y), "01 / 06", cf, CREAM_DIM, tracking=2, anchor_right=True)
d.line([(MARGIN, top_band_h - 18), (W - MARGIN, top_band_h - 18)], fill=BORDER_BLUE, width=2)

# ── headline block: opaque navy "jersey stripe" band, guarantees contrast
# over the photo no matter what's behind it — a real vintage-athletic device
# (the research: stripe/badge blocks behind type), not just a scrim hack ──
hf = anton(92)
h2 = anton(60)
block_x0, block_y0 = 0, 280
block_x1 = 848
head_x = MARGIN

def measure_stack(lines):
    y = 0
    for text, font, gap in lines:
        bbox = font.getbbox(text)
        y += (bbox[3] - bbox[1]) + gap
    return y

lines = [
    ("TAURINE IS IN", hf, 18),
    ("RED BULL.", hf, 34),
    ("BUT NOT WHY", h2, 12),
    ("YOU THINK.", h2, 30),
    ("SAVE THIS — PART 1 OF 6", inter(30, "Bold"), 0),
]
block_h = measure_stack(lines) + 88
d.rectangle([block_x0, block_y0, block_x1, block_y0 + block_h], fill=NAVY_DEEP)
d.rectangle([block_x0, block_y0, block_x1, block_y0 + block_h], outline=BORDER_BLUE, width=3)

cursor_y = block_y0 + 44
def draw_line(y, text, font, fill, gap_after):
    d.text((head_x, y), text, font=font, fill=fill)
    bbox = font.getbbox(text)
    return y + (bbox[3] - bbox[1]) + gap_after

cursor_y = draw_line(cursor_y, "TAURINE IS IN", hf, CREAM, 18)
cursor_y = draw_line(cursor_y, "RED BULL.", hf, CREAM, 34)
cursor_y = draw_line(cursor_y, "BUT NOT WHY", h2, BORDER_BLUE, 12)
cursor_y = draw_line(cursor_y, "YOU THINK.", h2, BORDER_BLUE, 30)

save_y = cursor_y
bf = inter(30, "Bold")
d.ellipse([MARGIN, save_y - 6, MARGIN + 42, save_y + 36], outline=CREAM, width=3)
d.polygon(
    [(MARGIN + 15, save_y + 3), (MARGIN + 27, save_y + 3),
     (MARGIN + 27, save_y + 24), (MARGIN + 21, save_y + 18), (MARGIN + 15, save_y + 24)],
    fill=CREAM,
)
d.text((MARGIN + 58, save_y), "SAVE THIS — PART 1 OF 6", font=bf, fill=CREAM)

# ── mascot, bottom-right — sized to the space actually left over below the
# headline block (measured, not guessed) so it can't collide with it, with a
# soft blurred cream glow hugging its own silhouette for contrast against the
# photo instead of a fixed-geometry badge disc that has to be hand-fitted ──
mascot_full = Image.open(MASCOT).convert("RGBA")
mascot_src = mascot_full.crop(mascot_full.getbbox())
aspect = mascot_src.height / mascot_src.width

bottom_band_h = 110
available_bottom = H - border_inset - bottom_band_h - 24
available_top = block_y0 + block_h + 24
available_h = available_bottom - available_top
m_w = min(480, int(available_h / aspect))
m_h = int(m_w * aspect)
mascot = mascot_src.resize((m_w, m_h), Image.LANCZOS)
m_x = W - border_inset - 40 - m_w
m_y = available_bottom - m_h
print(f"available_top={available_top} available_bottom={available_bottom} "
      f"m_w={m_w} m_h={m_h} mascot_top={m_y}")

glow_pad = 34
glow_alpha = mascot.split()[3].filter(ImageFilter.GaussianBlur(glow_pad / 2))
glow_alpha = glow_alpha.point(lambda v: min(255, int(v * 1.6)))
glow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow_full_alpha = Image.new("L", (W, H), 0)
glow_full_alpha.paste(glow_alpha, (m_x, m_y))
cream_fill = Image.new("RGBA", (W, H), CREAM + (255,))
glow_layer = Image.composite(cream_fill, glow_layer, glow_full_alpha)
img.paste(glow_layer, (0, 0), glow_layer)

img.paste(mascot, (m_x, m_y), mascot)

# ── bottom scrim + handle ───────────────────────────────────────────────────
bottom_band_h = 110
d.rectangle([border_inset + 4, H - border_inset - bottom_band_h, W - border_inset - 4, H - border_inset - 4], fill=NAVY_DEEP)
hf2 = inter(28, "SemiBold")
handle = "@POWERCOFFEE.OFC"
hw = d.textlength(handle, font=hf2)
d.text(((W - hw) / 2, H - border_inset - 46), handle, font=hf2, fill=CREAM_DIM)

out_path = "/private/tmp/claude-501/-Users-lacerdareis-Documents-Claude-ClaudeAI/f98d6e2e-f544-4fa9-bed1-641be79c6a41/scratchpad/fuel_check/slide1_v2.jpg"
img.save(out_path, quality=95)
print("saved", out_path)
