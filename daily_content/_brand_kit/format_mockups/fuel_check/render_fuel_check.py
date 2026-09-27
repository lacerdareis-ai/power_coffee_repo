#!/usr/bin/env python3
"""
Fuel Check — slides 2-6. Same system as slide 1 (v2): navy/cream halftone-
duotone photo treatment, no black anywhere, measured (not guessed) text
stacking and mascot sizing. Per Leo (2026-09-27): 2 of these 5 slides carry
no image (3 = the data table, 6 = the CTA close) — solid navy/cream instead.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
MARGIN = 108
BORDER_INSET = 44

NAVY        = (17, 58, 110)
NAVY_DEEP   = (10, 34, 66)
BORDER_BLUE = (66, 158, 235)
CREAM       = (238, 230, 202)
CREAM_DIM   = (196, 188, 158)
GOLD        = (212, 163, 58)

FONTS  = "/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/fonts"
POSES  = "/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/mascot_poses"
IMGS   = "/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/images"
OUT    = "/private/tmp/claude-501/-Users-lacerdareis-Documents-Claude-ClaudeAI/f98d6e2e-f544-4fa9-bed1-641be79c6a41/scratchpad/fuel_check"

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
    return total

def cover_fit(im, w, h):
    src_r = im.width / im.height
    dst_r = w / h
    if src_r > dst_r:
        new_h, new_w = h, int(h * src_r)
    else:
        new_w, new_h = w, int(w / src_r)
    im = im.resize((new_w, new_h), Image.LANCZOS)
    x0, y0 = (new_w - w) // 2, (new_h - h) // 2
    return im.crop((x0, y0, x0 + w, y0 + h))

def halftone_duotone(im, cell=5, dark=NAVY, light=CREAM):
    gray = im.convert("L")
    def lut(lo, hi):
        return [int(lo + (hi - lo) * (i / 255)) for i in range(256)]
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
    return Image.composite(navy_layer, duotone, dots.point(lambda v: int(v * 0.55)))

def measure_stack(lines):
    y = 0
    for text, font, gap in lines:
        bbox = font.getbbox(text)
        y += (bbox[3] - bbox[1]) + gap
    return y

def draw_stack(d, x, y0, lines):
    y = y0
    for text, font, fill, gap in lines:
        d.text((x, y), text, font=font, fill=fill)
        bbox = font.getbbox(text)
        y += (bbox[3] - bbox[1]) + gap
    return y

def place_mascot(img, pose_file, top_clear_y, bottom_limit_y, max_w=480):
    """Size a mascot to whatever vertical room is actually left, anchored
    bottom-right, with a soft cream glow — same measured approach as slide 1
    so this can't repeat the block/mascot collision bug found there."""
    mascot_full = Image.open(f"{POSES}/{pose_file}").convert("RGBA")
    mascot_src = mascot_full.crop(mascot_full.getbbox())
    aspect = mascot_src.height / mascot_src.width
    available_h = bottom_limit_y - top_clear_y
    m_w = min(max_w, int(available_h / aspect))
    m_h = int(m_w * aspect)
    mascot = mascot_src.resize((m_w, m_h), Image.LANCZOS)
    m_x = W - BORDER_INSET - 40 - m_w
    m_y = bottom_limit_y - m_h

    glow_pad = 34
    glow_alpha = mascot.split()[3].filter(ImageFilter.GaussianBlur(glow_pad / 2))
    glow_alpha = glow_alpha.point(lambda v: min(255, int(v * 1.6)))
    glow_full_alpha = Image.new("L", (W, H), 0)
    glow_full_alpha.paste(glow_alpha, (m_x, m_y))
    cream_fill = Image.new("RGBA", (W, H), CREAM + (255,))
    glow_layer = Image.composite(cream_fill, Image.new("RGBA", (W, H), (0, 0, 0, 0)), glow_full_alpha)
    img.paste(glow_layer, (0, 0), glow_layer)
    img.paste(mascot, (m_x, m_y), mascot)
    return m_x, m_y, m_w, m_h

def base_canvas(kind, photo_file, solid_color):
    img = Image.new("RGB", (W, H), NAVY)
    if kind == "photo":
        photo = Image.open(f"{IMGS}/{photo_file}").convert("RGB")
        photo = cover_fit(photo, W, H)
        bg = halftone_duotone(photo, cell=5)
        img.paste(bg, (0, 0))
    else:
        d0 = ImageDraw.Draw(img)
        d0.rectangle([0, 0, W, H], fill=solid_color)
    return img

def eyebrow_row(d, counter):
    d.rectangle([BORDER_INSET + 4, BORDER_INSET + 4, W - BORDER_INSET - 4, 168], fill=NAVY_DEEP)
    ef = inter(30, "Bold")
    tracked_text(d, (MARGIN, 96), "FUEL CHECK", ef, GOLD, tracking=4)
    cf = inter(30, "SemiBold")
    tracked_text(d, (W - MARGIN, 96), counter, cf, CREAM_DIM, tracking=2, anchor_right=True)
    d.line([(MARGIN, 150), (W - MARGIN, 150)], fill=BORDER_BLUE, width=2)

def bottom_handle(d, deep_band=True):
    band_h = 110
    if deep_band:
        d.rectangle([BORDER_INSET + 4, H - BORDER_INSET - band_h, W - BORDER_INSET - 4, H - BORDER_INSET - 4], fill=NAVY_DEEP)
    hf2 = inter(28, "SemiBold")
    handle = "@POWERCOFFEE.OFC"
    w = ImageDraw.Draw(Image.new("RGB", (1, 1))).textlength(handle, font=hf2)
    color = CREAM_DIM
    d.text(((W - w) / 2, H - BORDER_INSET - 46), handle, font=hf2, fill=color)
    return band_h


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 2 — "THE SCIENCE" (photo bg: img_16, calm hands-on-mug morning ritual)
# ══════════════════════════════════════════════════════════════════════════
def slide2():
    img = base_canvas("photo", "img_16_power.png", None)
    d = ImageDraw.Draw(img)
    d.rectangle([BORDER_INSET, BORDER_INSET, W - BORDER_INSET, H - BORDER_INSET], outline=CREAM, width=4)
    eyebrow_row(d, "02 / 06")

    hf, h2 = anton(92), anton(60)
    lines = [
        ("IT'S NOT THERE", hf, CREAM, 18),
        ("TO HYPE YOU UP.", hf, CREAM, 34),
        ("IT KEEPS YOU", h2, BORDER_BLUE, 12),
        ("SMOOTH INSTEAD.", h2, BORDER_BLUE, 30),
        ("SOURCE: MOLECULAR VISION, 2012", inter(26, "SemiBold"), CREAM_DIM, 0),
    ]
    block_x0, block_y0, block_x1 = 0, 280, 848
    block_h = measure_stack([(t, f, g) for t, f, _, g in lines]) + 88
    d.rectangle([block_x0, block_y0, block_x1, block_y0 + block_h], fill=NAVY_DEEP)
    d.rectangle([block_x0, block_y0, block_x1, block_y0 + block_h], outline=BORDER_BLUE, width=3)
    draw_stack(d, MARGIN, block_y0 + 44, lines)

    bottom_handle(d)
    img.save(f"{OUT}/slide2.jpg", quality=95)
    print("slide2 saved, block_bottom=", block_y0 + block_h)


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 3 — "THE NUMBERS" (NO IMAGE — solid cream data table)
# ══════════════════════════════════════════════════════════════════════════
def slide3():
    img = base_canvas("solid", None, CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([BORDER_INSET, BORDER_INSET, W - BORDER_INSET, H - BORDER_INSET], outline=NAVY, width=4)

    # eyebrow on cream: same layout, colors flipped for contrast
    d.rectangle([BORDER_INSET + 4, BORDER_INSET + 4, W - BORDER_INSET - 4, 168], fill=CREAM)
    ef = inter(30, "Bold")
    tracked_text(d, (MARGIN, 96), "FUEL CHECK", ef, GOLD, tracking=4)
    cf = inter(30, "SemiBold")
    tracked_text(d, (W - MARGIN, 96), "03 / 06", cf, NAVY, tracking=2, anchor_right=True)
    d.line([(MARGIN, 150), (W - MARGIN, 150)], fill=NAVY, width=2)

    label_f = inter(26, "Bold")
    d.text((MARGIN, 200), "PER SERVING", font=label_f, fill=NAVY)
    title_f = anton(76)
    d.text((MARGIN, 234), "THE NUMBERS.", font=title_f, fill=NAVY_DEEP)

    # ── table ────────────────────────────────────────────────────────────
    table_x0, table_x1 = MARGIN, W - MARGIN
    table_y0 = 420
    col0_w = 230
    col_w = (table_x1 - table_x0 - col0_w) / 3
    cols = ["POWER\nCOFFEE", "RED BULL", "BLACK\nCOFFEE"]
    rows = [
        ("CAFFEINE", ["175mg", "80mg", "~95mg"]),
        # 2.1g is the Illuminate Labs certified figure (07-Project_info/
        # certifications/README_Illuminate_Labs_Certification.md) — brand.md's
        # ingredient table says "2,000mg (2g)" but that doc predates the cert
        # and is explicitly flagged there as the imprecise, commonly-repeated
        # figure. 2.1g is ground truth.
        ("TAURINE", ["2,100mg", "1,000mg", "0mg"]),
        ("SUGAR", ["0g", "27g", "0g"]),
    ]
    row_h = 150
    header_h = 90

    # highlight the "us" column
    hi_x0 = table_x0 + col0_w
    d.rectangle([hi_x0, table_y0, hi_x0 + col_w, table_y0 + header_h + row_h * len(rows)], fill=(224, 214, 180))

    col_hdr_f = inter(24, "Bold")
    for i, name in enumerate(cols):
        cx = table_x0 + col0_w + col_w * i + col_w / 2
        for j, ln in enumerate(name.split("\n")):
            w = d.textlength(ln, font=col_hdr_f)
            fill = NAVY_DEEP if i == 0 else NAVY
            d.text((cx - w / 2, table_y0 + 14 + j * 28), ln, font=col_hdr_f, fill=fill)
    d.line([(table_x0, table_y0 + header_h), (table_x1, table_y0 + header_h)], fill=NAVY, width=2)

    row_label_f = inter(28, "Bold")
    val_f = inter(38, "Bold")
    y = table_y0 + header_h
    for label, vals in rows:
        d.text((table_x0, y + row_h / 2 - 16), label, font=row_label_f, fill=NAVY)
        for i, v in enumerate(vals):
            cx = table_x0 + col0_w + col_w * i + col_w / 2
            w = d.textlength(v, font=val_f)
            fill = NAVY_DEEP if i == 0 else NAVY
            d.text((cx - w / 2, y + row_h / 2 - 20), v, font=val_f, fill=fill)
        y += row_h
        d.line([(table_x0, y), (table_x1, y)], fill=(200, 190, 160), width=2)

    table_bottom = y

    # save cue — the actual save-worthy moment of the whole series
    save_y = table_bottom + 46
    bf = inter(28, "Bold")
    d.ellipse([MARGIN, save_y - 4, MARGIN + 38, save_y + 32], outline=NAVY, width=3)
    d.polygon(
        [(MARGIN + 13, save_y + 2), (MARGIN + 25, save_y + 2),
         (MARGIN + 25, save_y + 21), (MARGIN + 19, save_y + 16), (MARGIN + 13, save_y + 21)],
        fill=NAVY,
    )
    d.text((MARGIN + 52, save_y), "SAVE THIS — YOUR FUEL CHEAT SHEET", font=bf, fill=NAVY_DEEP)

    hf2 = inter(28, "SemiBold")
    handle = "@POWERCOFFEE.OFC"
    w = d.textlength(handle, font=hf2)
    d.text(((W - w) / 2, H - BORDER_INSET - 46), handle, font=hf2, fill=NAVY)

    img.save(f"{OUT}/slide3.jpg", quality=95)
    print("slide3 saved, table_bottom=", table_bottom, "save_y=", save_y)


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 4 — "SUSTAINED ENERGY" (photo bg: img_14, gym bag at dawn)
# ══════════════════════════════════════════════════════════════════════════
def slide4():
    img = base_canvas("photo", "img_14_power.png", None)
    d = ImageDraw.Draw(img)
    d.rectangle([BORDER_INSET, BORDER_INSET, W - BORDER_INSET, H - BORDER_INSET], outline=CREAM, width=4)
    eyebrow_row(d, "04 / 06")

    hf, h2 = anton(92), anton(60)
    lines = [
        ("NO SPIKE.", hf, CREAM, 18),
        ("NO CRASH.", hf, CREAM, 34),
        ("JUST 4-6 HOURS OF", h2, BORDER_BLUE, 12),
        ("CLEAN FOCUS.", h2, BORDER_BLUE, 30),
    ]
    block_x0, block_y0, block_x1 = 0, 280, 848
    block_h = measure_stack([(t, f, g) for t, f, _, g in lines]) + 88
    d.rectangle([block_x0, block_y0, block_x1, block_y0 + block_h], fill=NAVY_DEEP)
    d.rectangle([block_x0, block_y0, block_x1, block_y0 + block_h], outline=BORDER_BLUE, width=3)
    draw_stack(d, MARGIN, block_y0 + 44, lines)

    bottom_handle(d)
    img.save(f"{OUT}/slide4.jpg", quality=95)
    print("slide4 saved, block_bottom=", block_y0 + block_h)


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 5 — "THE PAYOFF" (photo bg: img_13, woman in deep focus, energized)
# ══════════════════════════════════════════════════════════════════════════
def slide5():
    img = base_canvas("photo", "img_13_power.png", None)
    d = ImageDraw.Draw(img)
    d.rectangle([BORDER_INSET, BORDER_INSET, W - BORDER_INSET, H - BORDER_INSET], outline=CREAM, width=4)
    eyebrow_row(d, "05 / 06")

    hf, h2 = anton(92), anton(60)
    lines = [
        ("STILL SHARP", hf, CREAM, 18),
        ("AT 2PM.", hf, CREAM, 34),
        ("THAT'S THE FIRST", h2, BORDER_BLUE, 12),
        ("WIN, TWICE.", h2, BORDER_BLUE, 30),
    ]
    block_x0, block_y0, block_x1 = 0, 280, 848
    block_h = measure_stack([(t, f, g) for t, f, _, g in lines]) + 88
    d.rectangle([block_x0, block_y0, block_x1, block_y0 + block_h], fill=NAVY_DEEP)
    d.rectangle([block_x0, block_y0, block_x1, block_y0 + block_h], outline=BORDER_BLUE, width=3)
    draw_stack(d, MARGIN, block_y0 + 44, lines)

    band_h = bottom_handle(d)
    place_mascot(img, "pose_armscrossed_cutout.png", block_y0 + block_h + 24, H - BORDER_INSET - band_h - 24)
    img.save(f"{OUT}/slide5.jpg", quality=95)
    print("slide5 saved, block_bottom=", block_y0 + block_h)


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 6 — "CTA" (NO IMAGE — solid navy close)
# ══════════════════════════════════════════════════════════════════════════
def slide6():
    # No mascot on this slide (Leo, 2026-09-27: mascot only on slides 1 & 5) —
    # first pass left the bottom half of the card empty, which read as
    # unfinished rather than intentional. Rebuilt with a real CTA button and
    # the brand's own tagline as a closing signature line, so the space is
    # doing something instead of just being absent of a mascot.
    img = base_canvas("solid", None, NAVY_DEEP)
    d = ImageDraw.Draw(img)
    d.rectangle([BORDER_INSET, BORDER_INSET, W - BORDER_INSET, H - BORDER_INSET], outline=CREAM, width=4)
    eyebrow_row(d, "06 / 06")

    hf = anton(100)
    lines = [
        ("YOUR FIRST WIN", hf, CREAM, 22),
        ("STARTS HERE.", hf, CREAM, 56),
    ]
    cursor_y = draw_stack(d, MARGIN, 340, lines)

    # ── gold CTA button — a real filled button device, not just a text line ──
    btn_f = inter(32, "Bold")
    btn_text = "SHOP THEPOWERCOFFEE.COM  →"
    btn_pad_x, btn_pad_y = 40, 26
    btn_w = d.textlength(btn_text, font=btn_f) + btn_pad_x * 2
    btn_h = 32 + btn_pad_y * 2
    btn_y0 = cursor_y + 26
    d.rectangle([MARGIN, btn_y0, MARGIN + btn_w, btn_y0 + btn_h], fill=GOLD)
    d.text((MARGIN + btn_pad_x, btn_y0 + btn_pad_y), btn_text, font=btn_f, fill=NAVY_DEEP)

    save_y = btn_y0 + btn_h + 54
    bf = inter(28, "Bold")
    d.ellipse([MARGIN, save_y - 4, MARGIN + 38, save_y + 32], outline=CREAM, width=3)
    d.polygon(
        [(MARGIN + 13, save_y + 2), (MARGIN + 25, save_y + 2),
         (MARGIN + 25, save_y + 21), (MARGIN + 19, save_y + 16), (MARGIN + 13, save_y + 21)],
        fill=CREAM,
    )
    save_text = "SAVE THIS. SEND IT TO SOMEONE WHO NEEDS SMOOTH ENERGY."
    words = save_text.split()
    line1, line2 = "", ""
    for w in words:
        trial = (line1 + " " + w).strip()
        if d.textlength(trial, font=bf) <= (W - MARGIN - (MARGIN + 52)):
            line1 = trial
        else:
            line2 = (line2 + " " + w).strip()
    d.text((MARGIN + 52, save_y), line1, font=bf, fill=CREAM)
    save_bottom = save_y + 40
    if line2:
        d.text((MARGIN + 52, save_y + 40), line2, font=bf, fill=CREAM)
        save_bottom += 40

    # ── closing signature line — the brand's own tagline (brand.md), anchors
    # the lower half instead of leaving it bare ─────────────────────────────
    tag_y = H - BORDER_INSET - 220
    d.line([(MARGIN, tag_y), (W - MARGIN, tag_y)], fill=BORDER_BLUE, width=2)
    tag_f = anton(46)
    tag_text = "THE FIRST WIN OF YOUR DAY."
    tw = d.textlength(tag_text, font=tag_f)
    d.text(((W - tw) / 2, tag_y + 36), tag_text, font=tag_f, fill=CREAM_DIM)

    bottom_handle(d, deep_band=False)
    img.save(f"{OUT}/slide6.jpg", quality=95)
    print("slide6 saved, save_bottom=", save_bottom, "tag_y=", tag_y)


if __name__ == "__main__":
    slide2()
    slide3()
    slide4()
    slide5()
    slide6()
