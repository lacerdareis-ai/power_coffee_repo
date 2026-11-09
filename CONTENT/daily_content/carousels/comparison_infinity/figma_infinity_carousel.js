// Power Coffee -- INFINITY COMPARISON CAROUSEL (5 slides) -- Figma Scripter
// 1080x1350 px | Instagram portrait carousel | seamless: ghost wordmark + shelf run across all slides
// Paste into Figma -> Plugins -> Scripter -> Run
// Frames are placed edge-to-edge (gap 0) so the infinity flow previews correctly.
// Export each frame at 1x as JPG -> slide_1.jpg ... slide_5.jpg
// AFTER RUNNING: drop the real product PNGs onto the white placeholder panels
// (FOCUS pouch, C4 tub, ONNIT box, mushroom coffee pouch, Power Coffee pack)
// and replace the QR placeholder with the real QR image (QR -> thepowercoffee.com).
// Fonts: Anton (headlines) + Inter (body) -- brand type system, Leo 2026-06-26.

var COLORS = {
  ESPRESSO: { r: 0.090, g: 0.078, b: 0.071 },
  GHOST:    { r: 0.141, g: 0.122, b: 0.106 },
  SHELF:    { r: 0.259, g: 0.224, b: 0.192 },
  CREAM:    { r: 0.969, g: 0.941, b: 0.878 },
  GOLD:     { r: 0.851, g: 0.651, b: 0.200 },
  WHITE:    { r: 1.000, g: 1.000, b: 1.000 } };

function col(c) {
  if (typeof c === "string") { return COLORS[c]; }
  return c; }

var W = 1080;
var H = 1350;
var SHELF_Y = 1005;
var GHOST_TEXT = "THE FIRST WIN OF YOUR DAY";
var GHOST_SIZE = 560;
var GHOST_Y = 330;
var GHOST_X = -1650; // tuned so the phrase spans all 5 frames

// slideType: "hook" | "competitors" | "hero" | "cta"
var SLIDES = [{ id: 1, slideType: "hook",
    line1: "EVERY MORNING FIX",
    line2: "HAS A CATCH",
    sub: "We compared what they cost - and what they skip.",
    shelfNote: "price per serving included"
}, { id: 2, slideType: "competitors",
    items: [{ name: "BRAIN SUPPLEMENTS", catch1: "Mental clarity only.", catch2: "Zero physical energy.", price: "$1.50 / serving", ph: "FOCUS POUCH PNG"
    }, { name: "PRE-WORKOUTS", catch1: "Physical power. Jitters.", catch2: "No mental clarity.", price: "$2.00 / serving", ph: "C4 TUB PNG" }]
}, { id: 3, slideType: "competitors",
    items: [{ name: "NOOTROPICS", catch1: "Premium cognition.", catch2: "No energy support.", price: "$2.50 / serving", ph: "ONNIT BOX PNG"
    }, { name: "MUSHROOM COFFEE", catch1: "Calm and cozy.", catch2: "Barely a boost.", price: "$0.50 / serving", ph: "MUSHROOM POUCH PNG" }]
}, { id: 4, slideType: "hero",
    line1: "SMOOTH ENERGY",
    line2: "NO CRASH",
    sub: "Energy + focus + performance. All three. One cup.",
    price: "$1.26 / serving",
    ph: "POWER COFFEE PACK PNG"
}, { id: 5, slideType: "cta",
    line1: "ONE SCOOP.",
    line2: "YOUR SAME CUP.",
    site: "thepowercoffee.com",
    tagline: "The first win of your day" }];

// -- helpers ------------------------------------------------------------------

function addRect(parent, x, y, w, h, color, opacity, radius) {
  if (opacity === undefined) { opacity = 1; }
  if (radius === undefined) { radius = 0; }
  var r = figma.createRectangle();
  r.x = x;
  r.y = y;
  r.resize(w, h);
  r.cornerRadius = radius;
  r.fills = [{ type: "SOLID", color: col(color), opacity: opacity }];
  parent.appendChild(r);
  return r; }

async function addText(parent, txt, x, y, w, family, style, size, color, align, opacity) {
  if (align === undefined) { align = "CENTER"; }
  if (opacity === undefined) { opacity = 1; }
  await figma.loadFontAsync({ family: family, style: style });
  var t = figma.createText();
  t.fontName = { family: family, style: style };
  t.characters = txt;
  t.fontSize = size;
  t.textAlignHorizontal = align;
  t.fills = [{ type: "SOLID", color: col(color), opacity: opacity }];
  t.x = x;
  t.y = y;
  t.resize(w, t.height);
  parent.appendChild(t);
  return t; }

async function anton(parent, txt, cx, y, size, color) {
  var t = await addText(parent, txt, cx - W / 2, y, W, "Anton", "Regular", size, color, "CENTER");
  return t; }

async function inter(parent, txt, cx, y, size, style, color) {
  var t = await addText(parent, txt, cx - W / 2, y, W, "Inter", style, size, color, "CENTER");
  return t; }

function chevrons(frame) {
  var i;
  for (i = 0; i < 2; i++) {
    var v = figma.createVector();
    v.vectorPaths = [{ windingRule: "NONE", data: "M 0 0 L 16 20 L 0 40" }];
    v.strokes = [{ type: "SOLID", color: col("GOLD") }];
    v.strokeWeight = 6;
    v.fills = [];
    v.x = W - 70 + i * 26;
    v.y = 660;
    frame.appendChild(v); } }

function productPanel(frame, cx, panelW, panelH, label) {
  var x0 = cx - panelW / 2;
  var y0 = SHELF_Y - panelH;
  addRect(frame, x0, y0, panelW, panelH, "WHITE", 1, 28);
  return { x0: x0, y0: y0 }; }

async function placeholderLabel(frame, cx, y, label) {
  await inter(frame, "[ " + label + " ]", cx, y, 26, "SemiBold", { r: 0.55, g: 0.55, b: 0.55 }); }

// -- seamless background layers (same in every frame, offset by frame index) --

async function seamlessLayers(frame, idx) {
  var ghost = await addText(frame, GHOST_TEXT, GHOST_X - idx * W, GHOST_Y, 9000, "Anton", "Regular", GHOST_SIZE, "GHOST", "LEFT");
  addRect(frame, 0, SHELF_Y, W, 5, "SHELF"); }

// -- slide builders -----------------------------------------------------------

async function buildHook(frame, s) {
  var c = W / 2;
  await inter(frame, "THE POWER COFFEE", c, 120, 40, "Bold", "CREAM");
  await anton(frame, s.line1, c, 380, 108, "CREAM");
  await anton(frame, s.line2, c, 520, 108, "GOLD");
  await inter(frame, s.sub, c, 700, 40, "SemiBold", "CREAM");
  await inter(frame, s.shelfNote, c, SHELF_Y + 40, 38, "Regular", "GOLD");
  chevrons(frame); }

async function buildCompetitors(frame, s) {
  var centers = [300, 790];
  var i;
  for (i = 0; i < s.items.length; i++) {
    var it = s.items[i];
    var cx = centers[i];
    var p = productPanel(frame, cx, 380, 400, it.ph);
    await placeholderLabel(frame, cx, p.y0 + 180, it.ph);
    await anton(frame, it.name, cx, p.y0 - 150, 58, "CREAM");
    await inter(frame, it.catch1, cx, p.y0 - 84, 34, "SemiBold", "CREAM");
    await inter(frame, it.catch2, cx, p.y0 - 44, 34, "SemiBold", "CREAM");
    await inter(frame, it.price, cx, SHELF_Y + 40, 46, "Bold", "GOLD"); }
  chevrons(frame); }

async function buildHero(frame, s) {
  var c = W / 2;
  var p = productPanel(frame, c, 480, 560, s.ph);
  await placeholderLabel(frame, c, p.y0 + 260, s.ph);
  await anton(frame, s.line1, c, p.y0 - 262, 96, "CREAM");
  await anton(frame, s.line2, c, p.y0 - 148, 96, "GOLD");
  await inter(frame, s.sub, c, SHELF_Y + 36, 38, "SemiBold", "CREAM");
  await anton(frame, s.price, c, SHELF_Y + 100, 84, "GOLD");
  chevrons(frame); }

async function buildCTA(frame, s) {
  var c = W / 2;
  await anton(frame, s.line1, c, 300, 120, "CREAM");
  await anton(frame, s.line2, c, 448, 120, "GOLD");
  addRect(frame, c - 180, 640, 360, 360, "CREAM", 1, 28);
  addRect(frame, c - 150, 670, 300, 300, "WHITE", 1, 0);
  await placeholderLabel(frame, c, 800, "QR PNG -> thepowercoffee.com");
  await inter(frame, s.site, c, SHELF_Y + 40, 48, "Bold", "GOLD");
  await inter(frame, s.tagline, c, SHELF_Y + 120, 40, "SemiBold", "CREAM"); }

// -- main ---------------------------------------------------------------------

async function main() {
  var i;
  for (i = 0; i < SLIDES.length; i++) {
    var s = SLIDES[i];
    var frame = figma.createFrame();
    frame.name = "Carousel " + s.id + " of 5 - infinity comparison";
    frame.resize(W, H);
    frame.x = i * W;
    frame.y = 0;
    frame.clipsContent = true;
    frame.fills = [{ type: "SOLID", color: col("ESPRESSO") }];
    await seamlessLayers(frame, i);
    if (s.slideType === "hook") { await buildHook(frame, s); }
    if (s.slideType === "competitors") { await buildCompetitors(frame, s); }
    if (s.slideType === "hero") { await buildHero(frame, s); }
    if (s.slideType === "cta") { await buildCTA(frame, s); } }
  figma.viewport.scrollAndZoomIntoView(figma.currentPage.children);
  figma.notify("Infinity carousel built - 5 frames. Drop product PNGs + QR onto placeholders."); }

await main();
