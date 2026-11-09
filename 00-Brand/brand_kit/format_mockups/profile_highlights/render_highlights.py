#!/usr/bin/env python3
"""
Instagram Highlight covers — Vintage Athletic navy/cream system, applying
the structured-highlights pattern from the Everyday Dose reference (FAQ,
Quality, Recipes, Community, etc. as organized circular covers) to Power
Coffee's own established visual system and mascot pose library, instead of
copying Everyday Dose's black/purple look.
"""
import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-lacerdareis-Documents-Claude-ClaudeAI/f98d6e2e-f544-4fa9-bed1-641be79c6a41/scratchpad/fuel_check")
from render_fuel_check import W as _W, NAVY, NAVY_DEEP, BORDER_BLUE, CREAM, CREAM_DIM, GOLD, anton, inter
from PIL import Image, ImageDraw

POSES = "/Users/lacerdareis/Documents/Claude/ClaudeAI/The_Power_Coffee/Sales_motor/daily_content/_brand_kit/mascot_poses"
OUT = "/private/tmp/claude-501/-Users-lacerdareis-Documents-Claude-ClaudeAI/f98d6e2e-f544-4fa9-bed1-641be79c6a41/scratchpad/profile_redesign"

S = 1080  # IG highlight cover upload size — IG applies its own circular mask

def circle_mask(size):
    m = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(m)
    d.ellipse([0, 0, size - 1, size - 1], fill=255)
    return m

def make_cover(name, label, pose_file=None, icon_draw=None):
    img = Image.new("RGB", (S, S), NAVY_DEEP)
    d = ImageDraw.Draw(img)
    # subtle ring, matches the border-frame device used across the whole system
    d.ellipse([26, 26, S - 26, S - 26], outline=CREAM, width=10)
    d.ellipse([50, 50, S - 50, S - 50], outline=BORDER_BLUE, width=3)

    if pose_file:
        mascot = Image.open(f"{POSES}/{pose_file}").convert("RGBA")
        mascot = mascot.crop(mascot.getbbox())
        target_h = int(S * 0.62)
        scale = target_h / mascot.height
        mascot = mascot.resize((int(mascot.width * scale), target_h), Image.LANCZOS)
        mx = (S - mascot.width) // 2
        my = int(S * 0.14)
        img.paste(mascot, (mx, my), mascot)
    elif icon_draw:
        icon_draw(d)

    # export square (IG masks it); also save a circular preview for review
    img.save(f"{OUT}/highlight_{name}_square.jpg", quality=95)
    circ = Image.new("RGB", (S, S), (30, 30, 30))
    circ.paste(img, (0, 0), circle_mask(S))
    circ.save(f"{OUT}/highlight_{name}_preview.png")
    print(f"highlight_{name} saved")


def founder_icon(d):
    # A hand-drawn mug icon here was a real bug (disconnected shapes) and
    # fiddly to get right in the first place — a clean Anton monogram is
    # simpler, reliable, and deliberately NOT the mascot, since this
    # highlight is about Leo the person, not the product character.
    f = anton(360)
    text = "L."
    bbox = d.textbbox((0, 0), text, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text((S / 2 - tw / 2 - bbox[0], S / 2 - th / 2 - bbox[1]), text, font=f, fill=CREAM)


if __name__ == "__main__":
    make_cover("faq", "FAQ", pose_file="pose_skeptical.png")
    make_cover("formula", "FORMULA", pose_file="pose_pointing_cutout.png")
    make_cover("fuelcheck", "FUEL CHECK", pose_file="pose_armscrossed_cutout.png")
    make_cover("events", "EVENTS", pose_file="pose_shouting.png")
    make_cover("shop", "SHOP", pose_file="pose_fistpump.png")
    make_cover("founder", "FOUNDER", icon_draw=founder_icon)

    # ── contact sheet for quick review ──
    cols, rows = 6, 1
    sheet = Image.new("RGB", (S * cols, S * rows + 140), (40, 40, 40))
    names = [("faq", "FAQ"), ("formula", "FORMULA"), ("fuelcheck", "FUEL CHECK"),
             ("events", "EVENTS"), ("shop", "SHOP"), ("founder", "FOUNDER")]
    label_f = inter(46, "Bold")
    for i, (name, label) in enumerate(names):
        thumb = Image.open(f"{OUT}/highlight_{name}_preview.png").resize((S, S))
        sheet.paste(thumb, (i * S, 0))
        dd = ImageDraw.Draw(sheet)
        lw = dd.textlength(label, font=label_f)
        dd.text((i * S + S / 2 - lw / 2, S + 30), label, font=label_f, fill=CREAM)
    sheet.save(f"{OUT}/contact_sheet.jpg", quality=92)
    print("contact sheet saved")
