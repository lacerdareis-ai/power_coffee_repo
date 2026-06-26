// ============================================================
// THE POWER COFFEE — T-Shirt Designs
// Figma Scripter · Plugins > Scripter > Run
//
// Creates 5 black t-shirt design layouts (1200 × 1200 canvas):
//   01 · The Faith Drop    — mascot top, text stack below
//   02 · The Hustle Stack  — "WORK HARD" dominant, mascot accent
//   03 · The Arc           — mascot center, text above + below
//   04 · The Minimal       — text-forward, mascot small icon
//   05 · The Power Drop    — full chest, overlaid gold text
//
// MASCOT PLACEHOLDER:
//   Each design has a gold-bordered rectangle labeled
//   "PLACE mascot_logo.png" — replace with the actual image
//   from: Sales_motor/daily_content/_brand_kit/cutouts/mascot_logo.png
// ============================================================

// ── BRAND TOKENS ─────────────────────────────────────────────

const BLACK    = { r: 0.07, g: 0.06, b: 0.05 };   // Deep Espresso
const CHARCOAL = { r: 0.18, g: 0.16, b: 0.14 };   // Dark Charcoal
const GOLD     = { r: 0.85, g: 0.65, b: 0.20 };   // Golden Energy
const CREAM    = { r: 0.97, g: 0.94, b: 0.88 };   // Warm Cream
const WHITE    = { r: 1.00, g: 1.00, b: 1.00 };
const MID_GRAY = { r: 0.55, g: 0.50, b: 0.44 };

const CANVAS_W = 1200;
const CANVAS_H = 1200;
const GAP      = 120;

let cursorX = 80;
let cursorY = 80;

// ── HELPERS ───────────────────────────────────────────────────

function rect(parent, x, y, w, h, fill, opacity, radius) {
  var r = figma.createRectangle();
  r.x = x; r.y = y;
  r.resize(w, h);
  r.fills = [{ type: "SOLID", color: fill, opacity: opacity !== undefined ? opacity : 1 }];
  if (radius) r.cornerRadius = radius;
  parent.appendChild(r);
  return r;
}

function ellipse(parent, x, y, w, h, fill, opacity) {
  var e = figma.createEllipse();
  e.x = x; e.y = y;
  e.resize(w, h);
  e.fills = [{ type: "SOLID", color: fill, opacity: opacity !== undefined ? opacity : 1 }];
  parent.appendChild(e);
  return e;
}

async function txt(parent, str, x, y, w, size, style, color, align, lineH) {
  var fn = style === "Italic" || style === "Bold Italic"
    ? { family: "Georgia", style: style }
    : style === "Bold" || style === "Regular"
    ? { family: "Georgia", style: style }
    : { family: "Arial", style: style };
  await figma.loadFontAsync(fn);
  var t = figma.createText();
  t.fontName   = fn;
  t.characters = str;
  t.fontSize   = size;
  t.textAlignHorizontal = align || "CENTER";
  t.fills      = [{ type: "SOLID", color: color }];
  t.lineHeight = { unit: "PERCENT", value: (lineH || 1.1) * 100 };
  t.x = x; t.y = y;
  t.resize(w, t.height);
  parent.appendChild(t);
  return t;
}

async function label(parent, str, x, y, w, size, style, color, align) {
  var fn = { family: "Arial", style: style || "Bold" };
  await figma.loadFontAsync(fn);
  var t = figma.createText();
  t.fontName   = fn;
  t.characters = str;
  t.fontSize   = size;
  t.textAlignHorizontal = align || "CENTER";
  t.fills      = [{ type: "SOLID", color: color }];
  t.x = x; t.y = y;
  t.resize(w, t.height);
  parent.appendChild(t);
  return t;
}

// Draws a placeholder box for the mascot_logo image
async function mascotPlaceholder(parent, x, y, w, h) {
  var box = figma.createRectangle();
  box.x = x; box.y = y;
  box.resize(w, h);
  box.fills = [{ type: "SOLID", color: CHARCOAL, opacity: 0.6 }];
  box.strokes = [{ type: "SOLID", color: GOLD }];
  box.strokeWeight = 2;
  box.dashPattern = [12, 8];
  parent.appendChild(box);

  // diagonal cross lines
  var l1 = figma.createLine();
  l1.x = x; l1.y = y;
  l1.resize(Math.sqrt(w * w + h * h), 0);
  l1.rotation = -Math.atan2(h, w) * 180 / Math.PI;
  l1.strokes = [{ type: "SOLID", color: GOLD, opacity: 0.15 }];
  l1.strokeWeight = 1;
  parent.appendChild(l1);

  await label(parent, "PLACE mascot_logo.png", x, y + h / 2 - 12, w, 11, "Bold", GOLD, "CENTER");
  await label(parent, "cutouts/mascot_logo.png", x, y + h / 2 + 4, w, 10, "Regular", MID_GRAY, "CENTER");
  return box;
}

function designFrame(name) {
  var f = figma.createFrame();
  f.name    = name;
  f.resize(CANVAS_W, CANVAS_H);
  f.x       = cursorX;
  f.y       = cursorY;
  f.fills   = [{ type: "SOLID", color: BLACK }];
  f.clipsContent = true;
  figma.currentPage.appendChild(f);
  return f;
}

function nextFrame() {
  cursorX += CANVAS_W + GAP;
}

// ── DESIGN 01 — "THE FAITH DROP" ──────────────────────────────
// Mascot large top half · text centered below · gold underline accent

async function buildDesign01() {
  var f = designFrame("01 · The Faith Drop");

  // background subtle texture lines
  for (var i = 0; i < 8; i++) {
    var l = figma.createLine();
    l.x = -40; l.y = 80 + i * 140;
    l.resize(CANVAS_W + 80, 0);
    l.strokes = [{ type: "SOLID", color: GOLD, opacity: 0.03 }];
    l.strokeWeight = 40;
    f.appendChild(l);
  }

  // mascot placeholder — upper center
  await mascotPlaceholder(f, 300, 80, 600, 520);

  // gold thin rule
  rect(f, 200, 630, 800, 2, GOLD, 0.7);

  // main headline
  await txt(f, "WORK HARD", 60, 660, CANVAS_W - 120, 110, "Bold Italic", CREAM, "CENTER", 0.9);
  await txt(f, "TRUST GOD", 60, 770, CANVAS_W - 120, 110, "Bold Italic", GOLD, "CENTER", 0.9);

  // tagline
  await label(f, "— THE POWER COFFEE —", 60, 906, CANVAS_W - 120, 13, "Bold", MID_GRAY, "CENTER");

  // bottom accent bar
  rect(f, 0, CANVAS_H - 6, CANVAS_W, 6, GOLD);

  // design label (top left)
  await label(f, "01 · THE FAITH DROP", 40, 40, 400, 11, "Bold", MID_GRAY, "LEFT");

  nextFrame();
  return f;
}

// ── DESIGN 02 — "THE HUSTLE STACK" ────────────────────────────
// Large "WORK HARD" dominant top · mascot as mid accent · "TRUST GOD" bold bottom

async function buildDesign02() {
  var f = designFrame("02 · The Hustle Stack");

  // full bleed dark gradient feel
  rect(f, 0, 0, CANVAS_W, CANVAS_H / 2, CHARCOAL, 0.3);

  // large primary text — top dominant
  await txt(f, "WORK", 40, 80, CANVAS_W - 80, 200, "Bold Italic", CREAM, "CENTER", 0.85);
  await txt(f, "HARD", 40, 270, CANVAS_W - 80, 200, "Bold Italic", GOLD, "CENTER", 0.85);

  // mascot placeholder — center band
  await mascotPlaceholder(f, 400, 480, 400, 240);

  // gold rules framing the mascot
  rect(f, 60, 480, CANVAS_W - 120, 2, GOLD, 0.5);
  rect(f, 60, 720, CANVAS_W - 120, 2, GOLD, 0.5);

  // bottom text
  await txt(f, "TRUST GOD", 40, 750, CANVAS_W - 80, 140, "Bold Italic", CREAM, "CENTER", 0.85);

  // footer micro label
  await label(f, "THEPOWERCOFFEE.COM", 60, CANVAS_H - 52, CANVAS_W - 120, 11, "Bold", MID_GRAY, "CENTER");
  rect(f, 0, CANVAS_H - 6, CANVAS_W, 6, GOLD);

  await label(f, "02 · THE HUSTLE STACK", 40, 40, 400, 11, "Bold", MID_GRAY, "LEFT");

  nextFrame();
  return f;
}

// ── DESIGN 03 — "THE ARC" ─────────────────────────────────────
// Overline text arc · mascot center · underline text arc · badge feel

async function buildDesign03() {
  var f = designFrame("03 · The Arc");

  // outer ring / badge circle
  ellipse(f, 100, 100, CANVAS_W - 200, CANVAS_H - 200, CHARCOAL, 0.25);
  // inner ring
  var ring = figma.createEllipse();
  ring.x = 120; ring.y = 120;
  ring.resize(CANVAS_W - 240, CANVAS_H - 240);
  ring.fills = [{ type: "SOLID", color: BLACK, opacity: 0 }];
  ring.strokes = [{ type: "SOLID", color: GOLD, opacity: 0.5 }];
  ring.strokeWeight = 2;
  ring.dashPattern = [16, 10];
  f.appendChild(ring);

  // arc-simulated text — "WORK HARD" top banner (straight, positioned to suggest arc)
  await label(f, "· · · W O R K  H A R D · · ·", 60, 220, CANVAS_W - 120, 22, "Bold", CREAM, "CENTER");
  rect(f, 200, 260, CANVAS_W - 400, 1, GOLD, 0.6);

  // mascot placeholder — center
  await mascotPlaceholder(f, 300, 290, 600, 440);

  // arc-simulated text — "TRUST GOD" bottom banner
  rect(f, 200, 740, CANVAS_W - 400, 1, GOLD, 0.6);
  await label(f, "· · · T R U S T  G O D · · ·", 60, 760, CANVAS_W - 120, 22, "Bold", GOLD, "CENTER");

  // cross accent marks at top/bottom of circle
  rect(f, CANVAS_W / 2 - 1, 100, 2, 30, GOLD, 0.6);
  rect(f, CANVAS_W / 2 - 1, CANVAS_H - 130, 2, 30, GOLD, 0.6);
  rect(f, 100, CANVAS_H / 2 - 1, 30, 2, GOLD, 0.6);
  rect(f, CANVAS_W - 130, CANVAS_H / 2 - 1, 30, 2, GOLD, 0.6);

  // brand footer
  await label(f, "THE POWER COFFEE", 60, CANVAS_H - 80, CANVAS_W - 120, 13, "Bold", MID_GRAY, "CENTER");
  await label(f, "CLEAN ENERGY. REAL FOCUS.", 60, CANVAS_H - 60, CANVAS_W - 120, 10, "Regular", MID_GRAY, "CENTER");

  await label(f, "03 · THE ARC", 40, 40, 400, 11, "Bold", MID_GRAY, "LEFT");

  nextFrame();
  return f;
}

// ── DESIGN 04 — "THE MINIMAL" ─────────────────────────────────
// Typography-forward · huge text · mascot as small bottom-right icon

async function buildDesign04() {
  var f = designFrame("04 · The Minimal");

  // vertical gold accent bar — left edge
  rect(f, 60, 120, 5, CANVAS_H - 240, GOLD, 0.8);

  // overline tag
  await label(f, "THE POWER COFFEE PRESENTS", 90, 130, CANVAS_W - 160, 11, "Bold", MID_GRAY, "LEFT");
  rect(f, 90, 156, 300, 1, GOLD, 0.4);

  // massive "WORK HARD"
  await txt(f, "WORK\nHARD", 80, 180, CANVAS_W - 100, 320, "Bold Italic", CREAM, "LEFT", 0.82);

  // divider
  rect(f, 80, 600, CANVAS_W - 140, 2, GOLD);

  // "TRUST GOD" — secondary but large
  await txt(f, "TRUST GOD", 80, 628, CANVAS_W - 100, 160, "Bold Italic", GOLD, "LEFT", 0.82);

  // mascot placeholder — small, bottom right corner
  await mascotPlaceholder(f, CANVAS_W - 260, 820, 200, 200);

  // bottom micro text
  await label(f, "THEPOWERCOFFEE.COM  ·  @POWERCOFFEE.OFC", 80, CANVAS_H - 56, 600, 11, "Bold", MID_GRAY, "LEFT");

  await label(f, "04 · THE MINIMAL", 40, 40, 400, 11, "Bold", MID_GRAY, "LEFT");

  nextFrame();
  return f;
}

// ── DESIGN 05 — "THE POWER DROP" ──────────────────────────────
// Full chest mascot bleeds · text overlaid with gold glow effect

async function buildDesign05() {
  var f = designFrame("05 · The Power Drop");

  // background glow — centered radial feel (layered ellipses)
  ellipse(f, CANVAS_W / 2 - 400, CANVAS_H / 2 - 400, 800, 800, { r: 0.85, g: 0.65, b: 0.20 }, 0.04);
  ellipse(f, CANVAS_W / 2 - 250, CANVAS_H / 2 - 250, 500, 500, { r: 0.85, g: 0.65, b: 0.20 }, 0.06);

  // mascot placeholder — large, full bleed center
  await mascotPlaceholder(f, 80, 60, CANVAS_W - 160, CANVAS_H - 120);

  // dark overlay band — top for text legibility
  rect(f, 0, 0, CANVAS_W, 260, BLACK, 0.75);

  // dark overlay band — bottom for text legibility
  rect(f, 0, CANVAS_H - 280, CANVAS_W, 280, BLACK, 0.80);

  // top text — "WORK HARD"
  await txt(f, "WORK HARD", 60, 60, CANVAS_W - 120, 170, "Bold Italic", CREAM, "CENTER", 0.88);

  // bottom text — "TRUST GOD"
  await txt(f, "TRUST GOD", 60, CANVAS_H - 230, CANVAS_W - 120, 150, "Bold Italic", GOLD, "CENTER", 0.88);

  // gold rules separating text from image
  rect(f, 80, 242, CANVAS_W - 160, 2, GOLD, 0.8);
  rect(f, 80, CANVAS_H - 252, CANVAS_W - 160, 2, GOLD, 0.8);

  // power dot accent
  ellipse(f, CANVAS_W / 2 - 5, 252 + 12, 10, 10, GOLD);
  ellipse(f, CANVAS_W / 2 - 5, CANVAS_H - 252 - 22, 10, 10, GOLD);

  await label(f, "05 · THE POWER DROP", 40, 40, 400, 11, "Bold", MID_GRAY, "LEFT");

  nextFrame();
  return f;
}

// ── DESIGN SHEET HEADER ────────────────────────────────────────

async function buildHeader() {
  var HW = 5 * CANVAS_W + 4 * GAP;
  var HH = 72;
  var header = figma.createFrame();
  header.name   = "T-Shirt Designs — Header";
  header.resize(HW, HH);
  header.x      = cursorX;
  header.y      = cursorY - HH - 40;
  header.fills  = [{ type: "SOLID", color: CHARCOAL }];
  figma.currentPage.appendChild(header);

  rect(header, 0, HH - 4, HW, 4, GOLD);
  await label(header, "THE POWER COFFEE — T-SHIRT DESIGNS  ·  \"WORK HARD, TRUST GOD\"  ·  5 Layout Variants  ·  1200 × 1200 px", 40, 22, HW - 80, 14, "Bold", CREAM, "LEFT");
  await label(header, "Replace all mascot placeholders with: Sales_motor/daily_content/_brand_kit/cutouts/mascot_logo.png", 40, 44, HW - 80, 11, "Regular", MID_GRAY, "LEFT");
}

// ── MAIN ──────────────────────────────────────────────────────

async function main() {
  figma.currentPage.name = "Power Coffee — T-Shirt Designs";

  await buildHeader();
  await buildDesign01();
  await buildDesign02();
  await buildDesign03();
  await buildDesign04();
  await buildDesign05();

  figma.viewport.scrollAndZoomIntoView(figma.currentPage.children);
  figma.notify("✅  5 T-Shirt designs created! Replace mascot placeholders with mascot_logo.png", { timeout: 6000 });
}

main();
