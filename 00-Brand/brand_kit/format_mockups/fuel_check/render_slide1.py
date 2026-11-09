#!/usr/bin/env python3
"""
Fuel Check — Slide 1 mockup (new save-worthy reference-carousel format).
Vintage Athletic navy/cream system, faceless mascot, Anton + Inter.
Canvas: 1080x1350 (4:5 feed/carousel), ~10% safe margin per platform-specs.md.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
MARGIN = 108  # ~10% safe zone, per social-media-design/references/platform-specs.md

# Vintage Athletic palette (reused from the navy/cream Story system for series
# consistency across formats — same fixed anchor logic as the mascot poses).
BG          = (24, 24, 24)
NAVY        = (11, 60, 125)
BORDER_BLUE = (13, 140, 233)
CREAM       = (228, 218, 185)
CREAM_DIM   = (170, 163, 140)
GOLD        = (191, 146, 42)

FONTS = "/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/fonts"
MASCOT = "/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/mascot_poses/pose_pointing.png"

def anton(size):
    return ImageFont.truetype(f"{FONTS}/Anton-Regular.ttf", size)

def inter(size, weight="Regular"):
    f = ImageFont.truetype(f"{FONTS}/Inter-Variable.ttf", size)
    try: f.set_variation_by_name(weight)
    except Exception: pass
    return f

def tracked_text(d, xy, text, font, fill, tracking=0, anchor_right=False):
    """Draw text with letter-spacing. If anchor_right, xy is the right edge."""
    widths = [d.textlength(ch, font=font) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x, y = xy
    if anchor_right:
        x = x - total
    for ch, w in zip(text, widths):
        d.text((x, y), ch, font=font, fill=fill)
        x += w + tracking

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ── decorative card border (fixed layout anchor for the series) ────────────
border_inset = 44
d.rectangle(
    [border_inset, border_inset, W - border_inset, H - border_inset],
    outline=BORDER_BLUE, width=4,
)

# ── eyebrow row: series badge (left) + slide counter (right) ───────────────
eyebrow_y = 96
ef = inter(30, "Bold")
tracked_text(d, (MARGIN, eyebrow_y), "FUEL CHECK", ef, GOLD, tracking=4)
cf = inter(30, "SemiBold")
tracked_text(d, (W - MARGIN, eyebrow_y), "01 / 06", cf, CREAM_DIM, tracking=2, anchor_right=True)

rule_y = eyebrow_y + 54
d.line([(MARGIN, rule_y), (W - MARGIN, rule_y)], fill=BORDER_BLUE, width=2)

# ── headline: the vetted brand.md hook (line 154), not a bare superiority stat ──
# Stack lines using each font's *measured* bbox rather than guessed pixel
# offsets — Anton's real glyph height doesn't match its point size, and a
# guessed gap is exactly what caused the headline/save-cue collision here.
hf = anton(96)
h2 = anton(64)
head_x = MARGIN
cursor_y = rule_y + 90

def draw_line(y, text, font, fill, gap_after):
    d.text((head_x, y), text, font=font, fill=fill)
    bbox = font.getbbox(text)
    line_h = bbox[3] - bbox[1]
    return y + line_h + gap_after

cursor_y = draw_line(cursor_y, "TAURINE IS IN", hf, CREAM, 18)
cursor_y = draw_line(cursor_y, "RED BULL.", hf, CREAM, 34)
cursor_y = draw_line(cursor_y, "BUT NOT WHY", h2, BORDER_BLUE, 12)
cursor_y = draw_line(cursor_y, "YOU THINK.", h2, BORDER_BLUE, 56)

# ── save cue, directly under the headline — direct answer to the account's
# near-zero-saves gap (see swipe_file/README.md). Placed here, not at the
# bottom, so it never has to compete for space with the mascot below.
save_y = cursor_y
bf = inter(30, "Bold")
d.ellipse([MARGIN, save_y - 6, MARGIN + 42, save_y + 36], outline=CREAM, width=3)
d.polygon(
    [(MARGIN + 15, save_y + 3), (MARGIN + 27, save_y + 3),
     (MARGIN + 27, save_y + 24), (MARGIN + 21, save_y + 18), (MARGIN + 15, save_y + 24)],
    fill=CREAM,
)
save_text = "SAVE THIS — PART 1 OF 6"
d.text((MARGIN + 58, save_y), save_text, font=bf, fill=CREAM)

# ── mascot, bottom-right — cropped to its real content bbox so sizing/placement
# is exact instead of guessed against the source file's transparent padding ──
mascot_full = Image.open(MASCOT).convert("RGBA")
mascot = mascot_full.crop(mascot_full.getbbox())
m_w = 520
scale = m_w / mascot.width
mascot = mascot.resize((m_w, int(mascot.height * scale)), Image.LANCZOS)
m_x = W - border_inset - 40 - mascot.width
m_y = H - border_inset - 46 - mascot.height
img.paste(mascot, (m_x, m_y), mascot)

# ── handle, bottom center ───────────────────────────────────────────────────
hf2 = inter(28, "SemiBold")
handle = "@POWERCOFFEE.OFC"
hw = d.textlength(handle, font=hf2)
d.text(((W - hw) / 2, H - border_inset - 46), handle, font=hf2, fill=CREAM_DIM)

img.save("/private/tmp/claude-501/-Users-lacerdareis-Documents-Claude-ClaudeAI/f98d6e2e-f544-4fa9-bed1-641be79c6a41/scratchpad/fuel_check/slide1.jpg", quality=95)
print("saved")
