# Figma Scripter — Brand Kit

**Type:** Figma Scripter (Plugins > Scripter > Run)
**Output:** 8 brand reference sections on a single page
**Last updated:** 2026-06-05
**Source file:** `daily_content/_brand_kit/figma_brand_kit.js`
**Fonts:** Georgia (headlines/body) + Arial (labels/pills/footer) — both native to Figma

## What it generates

| Section | Content |
|---|---|
| 00 · Cover | Brand name, tagline, handles |
| 01 · Color System | 8 swatches with hex, RGB, usage |
| 02 · Typography | Full type scale — Georgia + Arial specimens |
| 03 · Carousel Template | 5 slide types at 50% (Hook/Teach/Proof/Result/CTA) |
| 04 · Story Template | 9:16 at 35% with annotated zones |
| 05 · Components | Pills, dividers, pivot bar, footer bar |
| 06 · Ingredient Hooks | All 7 ingredients with doses and content hooks |
| 07 · Voice & Tone | ✅/❌ rules + LENS performance data |

## Font system

| Use | Font | Weight |
|-----|------|--------|
| Headlines (carousel/story) | Georgia | Bold Italic |
| Sub-headlines / CTA | Georgia | Bold |
| Body copy | Georgia | Regular |
| Quotes / tagline | Georgia | Italic |
| Labels / Overlines | Arial | Bold |
| Footer brand name | Arial | Bold |
| Footer tagline | Arial | Regular |
| Ingredient pills | Arial | Bold (+20% letter-spacing) |

## How to use

1. Open Figma → create or open any file
2. **Plugins → Scripter → Run Script**
3. Paste the full script below
4. Hit **Run**

## Script

```javascript
// ============================================================
// THE POWER COFFEE — Brand Kit
// Figma Scripter · Plugins > Scripter > Run
// Creates a full brand reference page:
//   01 · Color System
//   02 · Typography Scale
//   03 · Carousel Template (1080 × 1350)
//   04 · Story Template (1080 × 1920)
//   05 · Components (pills, dividers, footers, CTAs)
//   06 · Ingredient Hooks
//   07 · Voice & Tone Rules
// ============================================================

// ── TOKENS ───────────────────────────────────────────────────

const BRAND = {
  name:    "THE POWER COFFEE",
  tagline: '"The first win of your day."',
  website: "thepowercoffee.com",
  ig:      "@powercoffee.ofc",
  x:       "@boosteddays",
};

const COLORS = {
  "Deep Espresso":  { hex: "#171412", r: 0.09, g: 0.08, b: 0.07, role: "Primary BG · dark slides" },
  "Dark Charcoal":  { hex: "#2E2824", r: 0.18, g: 0.16, b: 0.14, role: "Secondary BG · layering" },
  "Golden Energy":  { hex: "#D9A633", r: 0.85, g: 0.65, b: 0.20, role: "Accent · CTA · highlights" },
  "Warm Cream":     { hex: "#F7F0E0", r: 0.97, g: 0.94, b: 0.88, role: "Text on dark · light BG" },
  "Matcha Green":   { hex: "#38724D", r: 0.22, g: 0.45, b: 0.30, role: "Ingredient accent · P2 days" },
  "Brown Mid":      { hex: "#7A3D1E", r: 0.48, g: 0.24, b: 0.12, role: "BROWN · slide BG variant" },
  "Brown Light":    { hex: "#C07A47", r: 0.75, g: 0.48, b: 0.28, role: "BROWN_L · overlines · labels" },
  "White":          { hex: "#FFFFFF", r: 1.00, g: 1.00, b: 1.00, role: "Headlines on CTA slides" },
};

// Font system: Headlines + body → Georgia | Labels, pills, footer, counter → Arial
// Matches make_carousel.py (Pillow) rendering exactly.
const TYPOGRAPHY = [
  { label: "Display / Hero",    size: 128, family: "Georgia", style: "Bold Italic", use: "Carousel headline (slide 1)" },
  { label: "Headline Large",    size:  80, family: "Georgia", style: "Bold Italic", use: "Carousel headlines (slides 2–5)" },
  { label: "Headline Mid",      size:  60, family: "Georgia", style: "Bold",        use: "Story / CTA headlines" },
  { label: "Subhead",           size:  28, family: "Georgia", style: "Bold",        use: "Slide subtext, pull quotes" },
  { label: "Body",              size:  22, family: "Georgia", style: "Regular",     use: "Carousel body copy" },
  { label: "Body Italic",       size:  22, family: "Georgia", style: "Italic",      use: "Tagline, quotes" },
  { label: "Label / Overline",  size:  12, family: "Arial",   style: "Bold",        use: "Overline tags (ALL CAPS)" },
  { label: "Caption / Footer",  size:  11, family: "Arial",   style: "Bold",        use: "Slide counter, footer brand" },
  { label: "Footer Sub",        size:  10, family: "Arial",   style: "Regular",     use: "Footer tagline, muted caption" },
  { label: "Pill",              size:  10, family: "Arial",   style: "Bold",        use: "Ingredient pills (letter-spaced +20%)" },
];

const INGREDIENTS = [
  { name: "Taurine",        dose: "2g",   hook: "Calms overstimulation. Neuromodulator, not stimulant." },
  { name: "Matcha",         dose: "—",    hook: "L-theanine gives a 4-6h arc vs 45-min caffeine spike." },
  { name: "Pea Protein",    dose: "5g",   hook: "Stabilises blood sugar → no energy crash at 10am." },
  { name: "Ginkgo Biloba",  dose: "—",    hook: "Survived a nuclear blast. Supports cerebral blood flow." },
  { name: "Cinnamon",       dose: "—",    hook: "Blood sugar stability changes focus quality, not just energy." },
  { name: "Ginger",         dose: "—",    hook: "Thermogenic metabolic support inside the blend." },
  { name: "Instant Coffee", dose: "~175mg", hook: "Base energy + ritual familiarity. Not the villain." },
];

const VOICE_RULES = [
  "✅  Direct, calm, confident — no hype, no fluff",
  "✅  Data hook → mechanism → payoff structure",
  "✅  Captions in flowing paragraphs, no bullets",
  "✅  FTC-safe: 'research suggests', 'associated with'",
  "❌  Never: hack / supplement / game-changer / quick fix",
  "❌  Never lead with the ingredient name (lead with the pain or mechanism)",
  "❌  Never: 'proven', 'clinically proven', 'guarantees'",
];

const LENS_RULES = [
  "Reels avg 199 reach vs Carousels avg 86 — 2.3× structural gap",
  "Reels avg 2.7 comments vs Carousels avg 0.1 — 27× difference",
  "Declarative hook vs question hook: 10.19% ER vs 1.30% ER (7.8× diff)",
  "Template confirmed: 'I [action]. And I'm not [hiding/apologising].'",
  "P3 days (Wed): always Reel, never Carousel",
];

// ── LAYOUT CONFIG ─────────────────────────────────────────────

const COL   = 1180;   // section column width
const PAD   = 80;     // section padding
const GAP_S = 32;     // gap between items in a section
const GAP_L = 100;    // gap between sections

let cursorX = PAD;
let cursorY = PAD;

// ── HELPERS ───────────────────────────────────────────────────

function rgb(c) { return { r: c.r, g: c.g, b: c.b }; }
const BLACK_COL = { r: 0.09, g: 0.08, b: 0.07 };
const CREAM_COL = { r: 0.97, g: 0.94, b: 0.88 };
const GOLD_COL  = { r: 0.85, g: 0.65, b: 0.20 };

// Font routing — matches make_carousel.py exactly:
//   Headlines / body / italic quotes → Georgia
//   Labels, overlines, pills, counter, footer → Arial
function _font(weight) {
  if (weight === "Bold Italic" || weight === "Black Italic") return { family: "Georgia", style: "Bold Italic" };
  if (weight === "Bold")     return { family: "Arial",   style: "Bold" };
  if (weight === "Italic")   return { family: "Georgia", style: "Italic" };
  if (weight === "Regular")  return { family: "Georgia", style: "Regular" };
  if (weight === "Black")    return { family: "Georgia", style: "Bold" };
  // fallback: Arial for anything else (e.g. "Regular Italic" on captions)
  return { family: "Arial", style: weight };
}

// Override: section labels and muted captions use Arial Regular
function _fontLabel(weight) {
  if (weight === "Bold")    return { family: "Arial", style: "Bold" };
  if (weight === "Regular") return { family: "Arial", style: "Regular" };
  return _font(weight);
}

function rect(parent, x, y, w, h, fill, opacity) {
  var r = figma.createRectangle();
  r.x = x; r.y = y; r.resize(w, h);
  r.fills = [{ type: "SOLID", color: fill, opacity: opacity !== undefined ? opacity : 1 }];
  parent.appendChild(r);
  return r;
}

// text() routes through _font() — Georgia for headlines/body, Arial for labels
async function text(parent, str, x, y, w, size, weight, fill, align, lineH) {
  var fn = _font(weight);
  await figma.loadFontAsync(fn);
  var t = figma.createText();
  t.fontName = fn;
  t.characters = str;
  t.fontSize = size;
  t.textAlignHorizontal = align || "LEFT";
  t.fills = [{ type: "SOLID", color: fill }];
  t.lineHeight = { unit: "PERCENT", value: (lineH || 1.3) * 100 };
  t.x = x; t.y = y;
  t.resize(w, t.height);
  parent.appendChild(t);
  return t;
}

// textLabel() always uses Arial (for section titles, annotations, small labels)
async function textLabel(parent, str, x, y, w, size, weight, fill, align, lineH) {
  var fn = _fontLabel(weight);
  await figma.loadFontAsync(fn);
  var t = figma.createText();
  t.fontName = fn;
  t.characters = str;
  t.fontSize = size;
  t.textAlignHorizontal = align || "LEFT";
  t.fills = [{ type: "SOLID", color: fill }];
  t.lineHeight = { unit: "PERCENT", value: (lineH || 1.3) * 100 };
  t.x = x; t.y = y;
  t.resize(w, t.height);
  parent.appendChild(t);
  return t;
}

function sectionFrame(label, w, h) {
  var f = figma.createFrame();
  f.name = label;
  f.resize(w, h);
  f.x = cursorX;
  f.y = cursorY;
  f.fills = [{ type: "SOLID", color: { r: 0.12, g: 0.10, b: 0.09 } }];
  f.clipsContent = false;
  figma.currentPage.appendChild(f);
  return f;
}

// ── 01 · COVER ────────────────────────────────────────────────

async function buildCover() {
  var H = 320;
  var f = sectionFrame("00 · Cover", COL, H);
  rect(f, 0, 0, COL, H, BLACK_COL);
  rect(f, 0, H - 6, COL, 6, GOLD_COL);
  await text(f, BRAND.name, PAD, 80, COL - PAD * 2, 52, "Bold Italic", CREAM_COL, "LEFT", 1.0);
  await text(f, BRAND.tagline, PAD, 148, COL - PAD * 2, 22, "Italic", GOLD_COL, "LEFT", 1.4);
  await textLabel(f, BRAND.website + "  ·  " + BRAND.ig + "  ·  " + BRAND.x, PAD, 210, COL - PAD * 2, 14, "Regular", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT", 1.4);
  await textLabel(f, "BRAND KIT · FIGMA REFERENCE  ·  Georgia (headlines/body)  +  Arial (labels/pills/footer)", PAD, 260, COL - PAD * 2, 11, "Bold", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT", 1.4);
  cursorY += H + GAP_L;
  return f;
}

// ── 02 · COLOR SYSTEM ─────────────────────────────────────────

async function buildColors() {
  var names  = Object.keys(COLORS);
  var SW     = 120;   // swatch size
  var ROWS   = Math.ceil(names.length / 4);
  var H      = 80 + ROWS * (SW + 80) + PAD;
  var f      = sectionFrame("01 · Color System", COL, H);
  rect(f, 0, 0, COL, H, BLACK_COL);
  rect(f, 0, 0, 4, H, GOLD_COL);
  await textLabel(f, "01  COLOR SYSTEM", PAD + 16, PAD, COL - PAD * 2, 11, "Bold", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");

  for (var i = 0; i < names.length; i++) {
    var col = COLORS[names[i]];
    var cx  = PAD + 16 + (i % 4) * (SW + 32);
    var cy  = PAD + 48 + Math.floor(i / 4) * (SW + 80);
    rect(f, cx, cy, SW, SW, rgb(col));
    await textLabel(f, names[i],   cx, cy + SW + 10, SW + 20, 13, "Bold",    CREAM_COL, "LEFT");
    await textLabel(f, col.hex,    cx, cy + SW + 28, SW + 20, 12, "Regular", GOLD_COL,  "LEFT");
    await textLabel(f, col.role,   cx, cy + SW + 46, SW + 60, 10, "Regular", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");
  }
  cursorY += H + GAP_L;
  return f;
}

// ── 03 · TYPOGRAPHY ───────────────────────────────────────────

async function buildTypography() {
  var H = 80 + TYPOGRAPHY.length * 72 + PAD;
  var f = sectionFrame("02 · Typography", COL, H);
  rect(f, 0, 0, COL, H, BLACK_COL);
  rect(f, 0, 0, 4, H, GOLD_COL);
  await textLabel(f, "02  TYPOGRAPHY  ·  Georgia (headlines / body)  +  Arial (labels / pills / footer)", PAD + 16, PAD, COL - PAD * 2, 11, "Bold", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");

  var dy = PAD + 48;
  for (var i = 0; i < TYPOGRAPHY.length; i++) {
    var t = TYPOGRAPHY[i];
    var renderSize = Math.min(t.size, 56);
    var fn = { family: t.family, style: t.style };
    await figma.loadFontAsync(fn);
    await textLabel(f, t.label, PAD + 16, dy, 260, 11, "Bold", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");
    // render "Aa" in the actual brand font
    var specimen = figma.createText();
    specimen.fontName = fn;
    specimen.characters = "Aa";
    specimen.fontSize = renderSize;
    specimen.textAlignHorizontal = "LEFT";
    specimen.fills = [{ type: "SOLID", color: CREAM_COL }];
    specimen.lineHeight = { unit: "PERCENT", value: 100 };
    specimen.x = 300; specimen.y = dy;
    specimen.resize(500, specimen.height);
    f.appendChild(specimen);
    await textLabel(f, t.size + "px · " + t.family + " " + t.style, 820, dy + 8, 320, 11, "Regular", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");
    await textLabel(f, t.use, 820, dy + 24, 320, 11, "Regular", GOLD_COL, "LEFT");
    dy += Math.max(renderSize + 18, 64);
  }
  cursorY += H + GAP_L;
  return f;
}

// ── 04 · CAROUSEL TEMPLATE (1080 × 1350) ─────────────────────

async function buildCarouselTemplate() {
  var CW = 1080; var CH = 1350;
  var SCALE = 0.5;
  var PW = CW * SCALE; var PH = CH * SCALE;

  var types  = ["HOOK", "TEACH", "PROOF", "RESULT", "CTA"];
  var bgs    = ["Black", "Charcoal", "Charcoal", "Black", "Brown Mid"];
  var TOTAL  = PAD * 2 + types.length * (PW + GAP_S) - GAP_S + 16;
  var H      = 80 + PH + 120 + PAD;

  var f = sectionFrame("03 · Carousel Template 1080×1350", Math.max(COL, TOTAL), H);
  rect(f, 0, 0, Math.max(COL, TOTAL), H, BLACK_COL);
  rect(f, 0, 0, 4, H, GOLD_COL);
  await textLabel(f, "03  CAROUSEL TEMPLATE  1080 × 1350 px (4:5)  —  shown at 50%", PAD + 16, PAD, 900, 11, "Bold", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");

  for (var i = 0; i < types.length; i++) {
    var ox = PAD + 16 + i * (PW + GAP_S);
    var oy = PAD + 48;
    var bgC = i === 4 ? { r: 0.48, g: 0.24, b: 0.12 } : i % 2 === 0 ? BLACK_COL : { r: 0.18, g: 0.16, b: 0.14 };
    rect(f, ox, oy, PW, PH, bgC);
    // accent lines (decorative)
    for (var li = 0; li < 5; li++) {
      var lr = figma.createLine();
      lr.x = ox - 20 + li * 120; lr.y = oy;
      lr.resize(PH * 1.2, 0);
      lr.rotation = -55;
      lr.strokes = [{ type: "SOLID", color: GOLD_COL, opacity: 0.04 }];
      lr.strokeWeight = 20;
      f.appendChild(lr);
    }
    // slide label
    await textLabel(f, types[i], ox, oy + PH + 12, PW, 13, "Bold", CREAM_COL, "LEFT");
    // slide number (Arial Bold — matches make_carousel.py counter font)
    await textLabel(f, "0" + (i + 1), ox + 24, oy + 20, 60, 10, "Bold", CREAM_COL, "LEFT");
    rect(f, ox + 24, oy + 34, 14, 1, GOLD_COL);
    // headline area
    await text(f, "HEADLINE
TEXT", ox + 24, oy + 44, PW - 48, 44, "Black Italic", CREAM_COL, "LEFT", 0.92);
    // divider
    rect(f, ox + 24, oy + PH * 0.54, PW - 48, 1, GOLD_COL, 0.6);
    // subtext area
    await text(f, "Body copy goes here.
2–3 sentences max.", ox + 24, oy + PH * 0.56, PW - 48, 11, "Regular", { r: 0.85, g: 0.80, b: 0.72 }, "LEFT", 1.6);
    // footer
    rect(f, ox + 24, oy + PH - 38, PW - 48, 1, { r: 0.75, g: 0.48, b: 0.28 }, 0.3);
    await textLabel(f, "THE POWER COFFEE", ox + 24, oy + PH - 26, 200, 7, "Bold", { r: 0.75, g: 0.48, b: 0.28 }, "LEFT");
    if (i === 4) {
      rect(f, ox, oy + PH - 72, PW, 72, { r: 0.48, g: 0.24, b: 0.12 });
      await textLabel(f, "thepowercoffee.com", ox + 24, oy + PH - 54, PW - 48, 10, "Regular", CREAM_COL, "LEFT");
      await textLabel(f, "@POWERCOFFEE.OFC", ox + 24, oy + PH - 36, PW - 48, 10, "Bold", CREAM_COL, "LEFT");
    }
  }
  cursorY += H + GAP_L;
  return f;
}

// ── 05 · STORY TEMPLATE (1080 × 1920) ────────────────────────

async function buildStoryTemplate() {
  var SW = 1080; var SH = 1920;
  var SCALE = 0.35;
  var PW = SW * SCALE; var PH = SH * SCALE;
  var H = 80 + PH + 120 + PAD;

  var f = sectionFrame("04 · Story Template 1080×1920", COL, H);
  rect(f, 0, 0, COL, H, BLACK_COL);
  rect(f, 0, 0, 4, H, GOLD_COL);
  await textLabel(f, "04  STORY TEMPLATE  1080 × 1920 px (9:16)  —  shown at 35%", PAD + 16, PAD, 900, 11, "Bold", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");

  var ox = PAD + 16;
  var oy = PAD + 48;
  rect(f, ox, oy, PW, PH, BLACK_COL);
  // diagonal lines
  for (var li = 0; li < 6; li++) {
    var lr = figma.createLine();
    lr.x = ox - 20 + li * 140; lr.y = oy;
    lr.resize(PH * 1.2, 0);
    lr.rotation = -55;
    lr.strokes = [{ type: "SOLID", color: GOLD_COL, opacity: 0.05 }];
    lr.strokeWeight = 25;
    f.appendChild(lr);
  }
  await text(f, "I DRINK MY
OWN PRODUCT
DAILY", ox + 24, oy + 60, PW - 48, 42, "Black Italic", CREAM_COL, "LEFT", 0.92);
  await text(f, "HERE'S WHAT CHANGED.", ox + 24, oy + 230, PW - 48, 14, "Bold", GOLD_COL, "LEFT");
  await text(f, "3–4 supporting lines.
The story. The result.
The proof.", ox + 24, oy + 260, PW - 48, 12, "Regular", { r: 0.85, g: 0.80, b: 0.72 }, "LEFT", 1.6);
  await text(f, "LINK IN BIO", ox + 24, oy + 350, PW - 48, 12, "Bold", GOLD_COL, "LEFT");

  // annotations
  await textLabel(f, "Safe zone
(avoid top/bottom 250px)", ox + PW + 20, oy, 200, 11, "Regular", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");
  await textLabel(f, "Headline block
(Black Italic, ~60px)", ox + PW + 20, oy + 60, 200, 11, "Regular", CREAM_COL, "LEFT");
  await textLabel(f, "Supporting copy
(Regular, 22px)", ox + PW + 20, oy + 260, 200, 11, "Regular", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");
  await textLabel(f, "CTA line (Bold, gold)", ox + PW + 20, oy + 350, 200, 11, "Regular", GOLD_COL, "LEFT");

  cursorY += H + GAP_L;
  return f;
}

// ── 06 · COMPONENTS ───────────────────────────────────────────

async function buildComponents() {
  var H = 400;
  var f = sectionFrame("05 · Components", COL, H);
  rect(f, 0, 0, COL, H, BLACK_COL);
  rect(f, 0, 0, 4, H, GOLD_COL);
  await textLabel(f, "05  COMPONENTS", PAD + 16, PAD, 400, 11, "Bold", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");

  // Ingredient pills
  await textLabel(f, "INGREDIENT PILLS", PAD + 16, PAD + 40, 400, 11, "Bold", CREAM_COL, "LEFT");
  var pillData = ["TAURINE 2g", "MATCHA", "PEA PROTEIN 5g", "GINKGO", "CINNAMON"];
  var px = PAD + 16;
  for (var i = 0; i < pillData.length; i++) {
    var pf = figma.createFrame();
    pf.resize(160, 36); pf.x = px; pf.y = PAD + 64;
    pf.fills = [{ type: "SOLID", color: { r: 0.48, g: 0.24, b: 0.12 }, opacity: 0.35 }];
    pf.cornerRadius = 0;
    f.appendChild(pf);
    await text(pf, pillData[i], 0, 10, 160, 10, "Bold", CREAM_COL, "CENTER");
    px += 172;
  }

  // Divider variants
  await textLabel(f, "DIVIDERS", PAD + 16, PAD + 120, 400, 11, "Bold", CREAM_COL, "LEFT");
  rect(f, PAD + 16, PAD + 144, 400, 2, GOLD_COL);
  await textLabel(f, "Gold full-width (opacity 1.0)", PAD + 430, PAD + 138, 400, 11, "Regular", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");
  rect(f, PAD + 16, PAD + 164, 400, 2, GOLD_COL, 0.6);
  await textLabel(f, "Gold full-width (opacity 0.6) — used between headline and body", PAD + 430, PAD + 158, 600, 11, "Regular", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");
  rect(f, PAD + 16, PAD + 184, 400, 1, { r: 0.75, g: 0.48, b: 0.28 }, 0.3);
  await textLabel(f, "Brown-light thin (opacity 0.3) — used as footer separator", PAD + 430, PAD + 178, 600, 11, "Regular", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");

  // Accent bar (pivot bar)
  await textLabel(f, "PIVOT BAR", PAD + 16, PAD + 210, 400, 11, "Bold", CREAM_COL, "LEFT");
  rect(f, PAD + 16, PAD + 234, 6, 80, GOLD_COL);
  await textLabel(f, "6px gold bar used left-of-headline
on teach / science slides", PAD + 40, PAD + 234, 400, 11, "Regular", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");

  // Footer bar
  await textLabel(f, "FOOTER BAR", PAD + 16, PAD + 330, 400, 11, "Bold", CREAM_COL, "LEFT");
  rect(f, PAD + 16, PAD + 354, COL - PAD * 2 - 16, 1, { r: 0.75, g: 0.48, b: 0.28 }, 0.3);
  await textLabel(f, "THE POWER COFFEE", PAD + 16, PAD + 358, 400, 11, "Bold", { r: 0.75, g: 0.48, b: 0.28 }, "LEFT");
  await textLabel(f, "CLEAN ENERGY. REAL FOCUS.", COL - PAD - 280, PAD + 358, 280, 10, "Regular", { r: 0.60, g: 0.55, b: 0.48 }, "RIGHT");

  cursorY += H + GAP_L;
  return f;
}

// ── 07 · INGREDIENT HOOKS ─────────────────────────────────────

async function buildIngredients() {
  var ROW_H = 64;
  var H = 80 + INGREDIENTS.length * ROW_H + PAD;
  var f = sectionFrame("06 · Ingredient Hooks", COL, H);
  rect(f, 0, 0, COL, H, BLACK_COL);
  rect(f, 0, 0, 4, H, GOLD_COL);
  await textLabel(f, "06  INGREDIENT HOOKS  —  never lead with the ingredient name; lead with the mechanism or pain", PAD + 16, PAD, COL, 11, "Bold", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");

  for (var i = 0; i < INGREDIENTS.length; i++) {
    var ing = INGREDIENTS[i];
    var iy  = PAD + 44 + i * ROW_H;
    rect(f, PAD + 16, iy, COL - PAD * 2 - 16, ROW_H - 8, { r: 0.18, g: 0.16, b: 0.14 });
    await textLabel(f, ing.name,  PAD + 28, iy + 10, 160, 13, "Bold",    CREAM_COL);
    await textLabel(f, ing.dose,  PAD + 196, iy + 12, 80,  11, "Regular", GOLD_COL);
    await text(f, ing.hook,  PAD + 280, iy + 10, COL - PAD * 2 - 280, 12, "Regular", { r: 0.85, g: 0.80, b: 0.72 }, "LEFT", 1.5);
  }
  cursorY += H + GAP_L;
  return f;
}

// ── 08 · VOICE & TONE + LENS DATA ────────────────────────────

async function buildVoice() {
  var H = 80 + (VOICE_RULES.length + LENS_RULES.length + 4) * 32 + PAD;
  var f = sectionFrame("07 · Voice · Tone · LENS Rules", COL, H);
  rect(f, 0, 0, COL, H, BLACK_COL);
  rect(f, 0, 0, 4, H, GOLD_COL);
  await textLabel(f, "07  VOICE & TONE", PAD + 16, PAD, 400, 11, "Bold", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");

  var dy = PAD + 44;
  for (var i = 0; i < VOICE_RULES.length; i++) {
    var clr = VOICE_RULES[i].startsWith("✅") ? { r: 0.22, g: 0.45, b: 0.30 } : { r: 0.70, g: 0.20, b: 0.20 };
    await text(f, VOICE_RULES[i], PAD + 16, dy, COL - PAD * 2, 13, "Regular", VOICE_RULES[i].startsWith("✅") ? CREAM_COL : { r: 0.90, g: 0.55, b: 0.55 });
    dy += 32;
  }

  dy += 24;
  await textLabel(f, "LENS DATA  —  what's working (updated weekly)", PAD + 16, dy, COL, 11, "Bold", { r: 0.55, g: 0.50, b: 0.44 }, "LEFT");
  dy += 28;
  for (var j = 0; j < LENS_RULES.length; j++) {
    await text(f, "→  " + LENS_RULES[j], PAD + 16, dy, COL - PAD * 2, 13, "Regular", GOLD_COL);
    dy += 32;
  }

  cursorY += H + GAP_L;
  return f;
}

// ── MAIN ──────────────────────────────────────────────────────

async function main() {
  figma.currentPage.name = "Power Coffee — Brand Kit";

  await buildCover();
  await buildColors();
  await buildTypography();
  await buildCarouselTemplate();
  await buildStoryTemplate();
  await buildComponents();
  await buildIngredients();
  await buildVoice();

  figma.viewport.scrollAndZoomIntoView(figma.currentPage.children);
  figma.notify("✅ Power Coffee Brand Kit created!", { timeout: 5000 });
}

main();
```
