// ============================================================
// THE POWER COFFEE — Father's Day Stories
// Figma Scripter · Plugins > Scripter > Run
//
// Creates 2 story frames (1080 × 1920 px — 9:16):
//   Story 1 · "Elected" — bold award-announcement statement
//   Story 2 · "The Gift" — warm, emotional, dad-forward
//
// After running:
//   Export each frame as PNG → save as story.jpg / story2.jpg
//   Drop into: Sales_motor/daily_content/jun2026_content/jun21_2026/
// ============================================================

// ── BRAND TOKENS ─────────────────────────────────────────────

const BLACK    = { r: 0.07, g: 0.06, b: 0.05 };   // Deep Espresso
const CHARCOAL = { r: 0.18, g: 0.16, b: 0.14 };   // Dark Charcoal
const GOLD     = { r: 0.85, g: 0.65, b: 0.20 };   // Golden Energy
const CREAM    = { r: 0.97, g: 0.94, b: 0.88 };   // Warm Cream
const BROWN    = { r: 0.48, g: 0.24, b: 0.12 };   // Brown Mid
const BROWN_L  = { r: 0.75, g: 0.48, b: 0.28 };   // Brown Light
const MID_GRAY = { r: 0.55, g: 0.50, b: 0.44 };

const W = 1080;
const H = 1920;
const GAP = 80;

// ── HELPERS ───────────────────────────────────────────────────

function rect(parent, x, y, w, h, fill, opacity, radius) {
  var r = figma.createRectangle();
  r.x = x; r.y = y; r.resize(w, h);
  r.fills = [{ type: "SOLID", color: fill, opacity: opacity !== undefined ? opacity : 1 }];
  if (radius) r.cornerRadius = radius;
  parent.appendChild(r);
  return r;
}

function ellipse(parent, x, y, w, h, fill, opacity) {
  var e = figma.createEllipse();
  e.x = x; e.y = y; e.resize(w, h);
  e.fills = [{ type: "SOLID", color: fill, opacity: opacity !== undefined ? opacity : 1 }];
  parent.appendChild(e);
  return e;
}

async function txt(parent, str, x, y, w, size, style, color, align, lineH) {
  var fn = (style === "Bold Italic" || style === "Italic")
    ? { family: "Georgia", style: style }
    : style === "Regular"
    ? { family: "Georgia", style: "Regular" }
    : { family: "Arial", style: style };
  await figma.loadFontAsync(fn);
  var t = figma.createText();
  t.fontName = fn;
  t.characters = str;
  t.fontSize = size;
  t.textAlignHorizontal = align || "CENTER";
  t.fills = [{ type: "SOLID", color: color }];
  t.lineHeight = { unit: "PERCENT", value: (lineH || 1.0) * 100 };
  t.x = x; t.y = y;
  t.resize(w, t.height);
  parent.appendChild(t);
  return t;
}

async function label(parent, str, x, y, w, size, weight, color, align, spacing) {
  var fn = { family: "Arial", style: weight || "Bold" };
  await figma.loadFontAsync(fn);
  var t = figma.createText();
  t.fontName = fn;
  t.characters = str;
  t.fontSize = size;
  t.textAlignHorizontal = align || "CENTER";
  t.fills = [{ type: "SOLID", color: color }];
  if (spacing) t.letterSpacing = { unit: "PERCENT", value: spacing };
  t.x = x; t.y = y;
  t.resize(w, t.height);
  parent.appendChild(t);
  return t;
}

function storyFrame(name, offsetX) {
  var f = figma.createFrame();
  f.name = name;
  f.resize(W, H);
  f.x = offsetX; f.y = 0;
  f.fills = [{ type: "SOLID", color: BLACK }];
  f.clipsContent = true;
  figma.currentPage.appendChild(f);
  return f;
}

// Diagonal texture lines (brand signature)
function diagonalLines(parent, count, opacity) {
  for (var i = 0; i < count; i++) {
    var l = figma.createLine();
    l.x = -60 + i * 160; l.y = 0;
    l.resize(H * 1.3, 0);
    l.rotation = -55;
    l.strokes = [{ type: "SOLID", color: GOLD, opacity: opacity || 0.04 }];
    l.strokeWeight = 40;
    parent.appendChild(l);
  }
}

// Gold horizontal rule
function rule(parent, x, y, w, opacity) {
  rect(parent, x, y, w, 2, GOLD, opacity || 0.8);
}

// ── STORY 1 — "ELECTED" ───────────────────────────────────────
// Bold award-announcement. Black bg. Gold accent ring.
// Top: badge. Center: headline. Bottom: brand + CTA.

async function buildStory1(offsetX) {
  var f = storyFrame("Story 1 — Elected · Father's Day", offsetX);

  // Background texture
  diagonalLines(f, 9, 0.035);

  // Outer glow ring (subtle)
  ellipse(f, W / 2 - 520, H / 2 - 520, 1040, 1040, GOLD, 0.04);
  ellipse(f, W / 2 - 380, H / 2 - 380, 760, 760, GOLD, 0.04);

  // ── TOP BADGE AREA ──────────────────────────────────────────

  // Badge circle
  var badgeY = 220;
  var badgeR = 160;
  ellipse(f, W / 2 - badgeR, badgeY - badgeR, badgeR * 2, badgeR * 2, CHARCOAL, 0.7);
  // Badge ring
  var ring = figma.createEllipse();
  ring.x = W / 2 - badgeR; ring.y = badgeY - badgeR;
  ring.resize(badgeR * 2, badgeR * 2);
  ring.fills = [{ type: "SOLID", color: BLACK, opacity: 0 }];
  ring.strokes = [{ type: "SOLID", color: GOLD, opacity: 0.9 }];
  ring.strokeWeight = 3;
  f.appendChild(ring);

  // Badge icon — coffee cup silhouette (simplified with rects)
  rect(f, W / 2 - 36, badgeY - 44, 72, 52, GOLD, 0.9, 4);       // cup body
  rect(f, W / 2 - 36, badgeY - 52, 72, 10, BROWN_L, 0.7, 2);    // liquid top
  rect(f, W / 2 + 36, badgeY - 32, 18, 28, GOLD, 0, 0);
  var handle = figma.createRectangle();                            // handle (right side arc sim)
  handle.x = W / 2 + 36; handle.y = badgeY - 32;
  handle.resize(18, 28);
  handle.fills = [{ type: "SOLID", color: BLACK, opacity: 0 }];
  handle.strokes = [{ type: "SOLID", color: GOLD, opacity: 0.9 }];
  handle.strokeWeight = 5;
  handle.cornerRadius = 10;
  f.appendChild(handle);
  rect(f, W / 2 - 44, badgeY + 12, 88, 8, GOLD, 0.5, 2);        // saucer
  // Steam lines
  for (var s = 0; s < 3; s++) {
    rect(f, W / 2 - 20 + s * 20, badgeY - 72 - s * 6, 4, 20, GOLD, 0.4, 2);
  }

  await label(f, "THE POWER COFFEE", W / 2 - 200, badgeY + 30, 400, 10, "Bold", GOLD, "CENTER", 20);

  // ── GOLD DIVIDER ────────────────────────────────────────────
  rule(f, 120, 450, W - 240, 0.5);

  // ── OVERLINE TAG ────────────────────────────────────────────
  await label(f, "THIS FATHER'S DAY", 60, 476, W - 120, 13, "Bold", GOLD, "CENTER", 15);

  // ── MAIN HEADLINE ───────────────────────────────────────────
  await txt(f, "WE WERE", 60, 540, W - 120, 148, "Bold Italic", CREAM, "CENTER", 0.85);
  await txt(f, "ELECTED", 60, 670, W - 120, 200, "Bold Italic", GOLD, "CENTER", 0.82);

  // ── SUBLINE ─────────────────────────────────────────────────
  rect(f, 180, 896, W - 360, 2, GOLD, 0.4);
  await label(f, "BEST FATHER'S DAY GIFT", 60, 918, W - 120, 14, "Bold", CREAM, "CENTER", 12);
  rect(f, 180, 948, W - 360, 2, GOLD, 0.4);

  // ── BODY COPY ───────────────────────────────────────────────
  await txt(f, "For the dad who wakes up before\nthe house does. For the one who\nshows up — every morning.", 80, 994, W - 160, 36, "Italic", { r: 0.80, g: 0.75, b: 0.68 }, "CENTER", 1.55);

  // ── PRICE ANCHOR ────────────────────────────────────────────
  rect(f, 120, 1180, W - 240, 2, GOLD, 0.25);
  await label(f, "$1.19 A MORNING  ·  7 INGREDIENTS  ·  NO CRASH", 60, 1200, W - 120, 11, "Bold", MID_GRAY, "CENTER", 8);
  rect(f, 120, 1228, W - 240, 2, GOLD, 0.25);

  // ── MASCOT PLACEHOLDER ──────────────────────────────────────
  // (replace with mascot_logo.png after export)
  var mascotBox = figma.createRectangle();
  mascotBox.x = W / 2 - 140; mascotBox.y = 1280;
  mascotBox.resize(280, 280);
  mascotBox.fills = [{ type: "SOLID", color: CHARCOAL, opacity: 0.4 }];
  mascotBox.strokes = [{ type: "SOLID", color: GOLD, opacity: 0.4 }];
  mascotBox.strokeWeight = 1;
  mascotBox.dashPattern = [10, 6];
  f.appendChild(mascotBox);
  await label(f, "mascot_logo.png", W / 2 - 140, 1405, 280, 10, "Bold", MID_GRAY, "CENTER");

  // ── BOTTOM CTA BAR ──────────────────────────────────────────
  rect(f, 0, H - 200, W, 200, BROWN, 0.85);
  rect(f, 0, H - 200, W, 2, GOLD, 0.7);
  await label(f, "GIFT THE UPGRADE", 60, H - 160, W - 120, 22, "Bold", CREAM, "CENTER", 10);
  await label(f, "thepowercoffee.com", 60, H - 120, W - 120, 16, "Regular", GOLD, "CENTER");
  await label(f, "LINK IN BIO  ↑", 60, H - 80, W - 120, 13, "Bold", CREAM, "CENTER", 8);

  return f;
}

// ── STORY 2 — "THE GIFT" ──────────────────────────────────────
// Warm, emotional. Two-tone split. Founder-voice copy. Feels human.

async function buildStory2(offsetX) {
  var f = storyFrame("Story 2 — The Gift · Father's Day", offsetX);

  // Bottom warm panel
  rect(f, 0, H * 0.52, W, H * 0.48, BROWN, 0.25);

  // Diagonal texture — lighter
  diagonalLines(f, 8, 0.03);

  // Top gold accent bar
  rect(f, 0, 0, W, 8, GOLD);

  // ── OVERLINE ────────────────────────────────────────────────
  await label(f, "· FATHER'S DAY 2026 ·", 60, 72, W - 120, 13, "Bold", GOLD, "CENTER", 16);
  rule(f, 200, 108, W - 400, 0.5);

  // ── HEADLINE ────────────────────────────────────────────────
  await txt(f, "THE GIFT\nTHAT SHOWS\nUP EVERY\nMORNING.", 60, 148, W - 120, 130, "Bold Italic", CREAM, "CENTER", 0.88);

  // ── DIVIDER ─────────────────────────────────────────────────
  rule(f, 120, 710, W - 240, 0.6);

  // ── BODY — Founder voice ─────────────────────────────────────
  await txt(f, "I built this because I was crashing\nat 2pm — right when my kids needed\nme to show up.", 80, 750, W - 160, 38, "Italic", { r: 0.85, g: 0.80, b: 0.72 }, "CENTER", 1.55);

  await txt(f, "Seven ingredients. One scoop.\nThe same formula I've used for\n550 mornings in a row.", 80, 912, W - 160, 38, "Italic", { r: 0.85, g: 0.80, b: 0.72 }, "CENTER", 1.55);

  // Signature
  rule(f, 300, 1078, W - 600, 0.35);
  await label(f, "Leo · Founder, The Power Coffee", 60, 1098, W - 120, 13, "Regular", MID_GRAY, "CENTER");
  rule(f, 300, 1124, W - 600, 0.35);

  // ── PRODUCT CALLOUT BOX ──────────────────────────────────────
  rect(f, 80, 1180, W - 160, 200, CHARCOAL, 0.6, 6);
  rect(f, 80, 1180, 6, 200, GOLD, 0.9);
  await label(f, "WHAT'S INSIDE", 120, 1206, W - 220, 10, "Bold", GOLD, "LEFT", 15);
  await txt(f, "Matcha · Taurine · Pea Protein\nGinkgo · Cinnamon · Ginger\n+ Clean Coffee Base", 120, 1238, W - 220, 30, "Regular", { r: 0.85, g: 0.80, b: 0.72 }, "LEFT", 1.6);
  await label(f, "No sugar · No crash · No jitters", 120, 1336, W - 220, 11, "Bold", CREAM, "LEFT", 5);

  // ── PRICE ────────────────────────────────────────────────────
  await label(f, "$1.19 A MORNING", 60, 1430, W - 120, 18, "Bold", GOLD, "CENTER", 10);
  await label(f, "VS. $5–6 AT THE COFFEE SHOP", 60, 1460, W - 120, 11, "Regular", MID_GRAY, "CENTER", 5);

  // ── MASCOT PLACEHOLDER ──────────────────────────────────────
  var mascotBox2 = figma.createRectangle();
  mascotBox2.x = W / 2 - 90; mascotBox2.y = 1510;
  mascotBox2.resize(180, 180);
  mascotBox2.fills = [{ type: "SOLID", color: CHARCOAL, opacity: 0.4 }];
  mascotBox2.strokes = [{ type: "SOLID", color: GOLD, opacity: 0.4 }];
  mascotBox2.strokeWeight = 1;
  mascotBox2.dashPattern = [8, 5];
  f.appendChild(mascotBox2);
  await label(f, "mascot_logo.png", W / 2 - 90, 1583, 180, 9, "Bold", MID_GRAY, "CENTER");

  // ── BOTTOM CTA ───────────────────────────────────────────────
  rect(f, 0, H - 180, W, 180, BLACK, 0.9);
  rect(f, 0, H - 180, W, 2, GOLD, 0.7);
  await label(f, "GIVE DAD THE UPGRADE", 60, H - 144, W - 120, 20, "Bold", CREAM, "CENTER", 8);
  await label(f, "thepowercoffee.com", 60, H - 104, W - 120, 16, "Regular", GOLD, "CENTER");
  await label(f, "LINK IN BIO  ↑", 60, H - 68, W - 120, 12, "Bold", { r: 0.55, g: 0.50, b: 0.44 }, "CENTER", 8);

  return f;
}

// ── MAIN ──────────────────────────────────────────────────────

async function main() {
  figma.currentPage.name = "Power Coffee — Father's Day Stories";

  var s1 = await buildStory1(0);
  var s2 = await buildStory2(W + GAP);

  figma.viewport.scrollAndZoomIntoView([s1, s2]);
  figma.notify("✅  Father's Day stories ready — export as PNG → save as story.jpg / story2.jpg", { timeout: 6000 });
}

main();
