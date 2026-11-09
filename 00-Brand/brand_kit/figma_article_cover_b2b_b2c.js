// ============================================================
// THE POWER COFFEE — LinkedIn article cover
// "B2B and B2C are not the same game"
// Figma Scripter — paste into: Plugins → Scripter → Run
//
// Output: one 1200 × 644 frame (LinkedIn's article cover ratio), matching
// the layout language of figma_article_cover_certification.js (espresso bg,
// gold edge rule, Anton-style headline, cream plate on the right) — but the
// plate holds a split panel instead of a seal: a small connected "committee"
// of nodes for B2B vs a single dot mid-motion for B2C, visualizing the
// article's central image (a committee decides vs. one thumb decides).
//
// Reference render (Pillow/SVG, verified via Chrome before porting here):
// scratchpad/cover/b2b_b2c_cover.py → b2b_b2c_cover.svg
// ============================================================

// ── BRAND TOKENS ─────────────────────────────────────────────
const C = {
  BG:    { r: 23 / 255,  g: 20 / 255,  b: 18 / 255  }, // #171412 Deep Espresso
  CREAM: { r: 247 / 255, g: 240 / 255, b: 224 / 255 }, // #F7F0E0 Warm Cream
  GOLD:  { r: 217 / 255, g: 166 / 255, b: 51 / 255  }, // #D9A633 Golden Energy
  MUTED: { r: 0.55,      g: 0.52,      b: 0.47      },
};

const W = 1200, H = 644;
const PAD = 70;

// numeric-safe middle dot — matches the SVG source's &#183; fix (a raw "·"
// glyph is fine here since Scripter strings are real JS strings, not bytes
// going through an HTTP/charset boundary, but keeping the same visible
// character as the verified render avoids re-checking it twice).
const DOT = "·";
const OVERLINE = `THE POWER COFFEE  ${DOT}  FOUNDER NOTES`;
const HEADLINE = [
  ["B2B AND B2C", C.CREAM],
  ["ARE NOT",     C.GOLD],
  ["THE SAME GAME", C.CREAM],
];
const SUBLINE  = "Years selling to businesses taught me the wrong instincts for selling to people.";
const FOOTLINE = `FOUNDER STORY  ${DOT}  WHAT TRANSFERS AND WHAT BREAKS`;

// ── HELPERS ───────────────────────────────────────────────────
const solid = (c) => [{ type: "SOLID", color: c }];

async function fonts() {
  await figma.loadFontAsync({ family: "Anton", style: "Regular" });
  for (const s of ["Bold", "Regular"]) {
    await figma.loadFontAsync({ family: "Inter", style: s });
  }
}

function text(parent, chars, o) {
  const t = figma.createText();
  t.fontName = o.font;
  parent.appendChild(t);            // parent BEFORE positioning
  t.characters = chars;
  t.fontSize = o.size;
  t.fills = solid(o.fill);
  if (o.lineHeight) t.lineHeight = { unit: "PIXELS", value: o.lineHeight };
  if (o.tracking)   t.letterSpacing = { unit: "PERCENT", value: o.tracking };
  if (o.align) t.textAlignHorizontal = o.align;
  t.textAutoResize = "WIDTH_AND_HEIGHT";
  if (o.name) t.name = o.name;
  return t;
}

function line(parent, x1, y1, x2, y2, color, weight, opacity) {
  const l = figma.createLine();
  parent.appendChild(l);
  l.x = x1; l.y = y1;
  l.resize(Math.hypot(x2 - x1, y2 - y1), 0);
  l.rotation = -Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;
  l.strokes = solid(color);
  l.strokeWeight = weight;
  if (opacity !== undefined) l.opacity = opacity;
  return l;
}

// ── BUILD ─────────────────────────────────────────────────────
await fonts();

// place clear of anything already on the page
let ox = 0;
for (const n of figma.currentPage.children) ox = Math.max(ox, n.x + n.width);
ox += 200;

const f = figma.createFrame();
f.name = "LinkedIn cover — B2B vs B2C article (1200×644)";
figma.currentPage.appendChild(f);
f.resize(W, H);
f.x = ox;
f.y = 0;
f.fills = solid(C.BG);
f.clipsContent = true;

// hairline gold rule down the left edge — matches the certification cover
const rule = figma.createRectangle();
f.appendChild(rule);
rule.resize(6, H);
rule.x = 0; rule.y = 0;
rule.fills = solid(C.GOLD);
rule.name = "edge rule";

// ── split panel, right side, on a cream plate ──────────────────
const PANEL = 372;
const PLATE_PAD = 18;
const plateW = PANEL + PLATE_PAD * 2;
const plateH = PANEL + PLATE_PAD * 2;
const plateX = W - 80 - plateW;
const plateY = Math.round((H - plateH) / 2);

const plate = figma.createRectangle();
f.appendChild(plate);
plate.resize(plateW, plateH);
plate.x = plateX; plate.y = plateY;
plate.fills = solid(C.CREAM);
plate.cornerRadius = 18;
plate.name = "split panel plate";

const px = plateX + PLATE_PAD;
const py = plateY + PLATE_PAD;
const half = PANEL / 2;

// divider between the two halves — a thin filled rectangle rather than a
// rotated Line node (no rotation-direction ambiguity). dashPattern only
// applies to strokes, not fills, so this renders as a solid hairline —
// a fine substitute for the dashed rule in the SVG reference.
const divider = figma.createRectangle();
f.appendChild(divider);
divider.resize(1.5, PANEL - 32);
divider.x = px + half - 0.75; divider.y = py + 16;
divider.fills = solid(C.BG);
divider.opacity = 0.35;
divider.name = "panel divider";

// ── LEFT half: B2B — a small committee of connected nodes ───────
const cx1 = px + half / 2;
const cy1 = py + PANEL / 2 - 18;
const nodePts = [
  [cx1, cy1 - 70],
  [cx1 - 62, cy1 + 10],
  [cx1, cy1 + 60],
  [cx1 + 62, cy1 + 10],
];
for (const [nx, ny] of nodePts) {
  line(f, cx1, cy1, nx, ny, C.BG, 2.5, 0.55);
}
const hub = figma.createEllipse();
f.appendChild(hub);
hub.resize(24, 24);
hub.x = cx1 - 12; hub.y = cy1 - 12;
hub.fills = solid(C.BG);
hub.name = "b2b hub node";
for (const [nx, ny] of nodePts) {
  const dot = figma.createEllipse();
  f.appendChild(dot);
  dot.resize(18, 18);
  dot.x = nx - 9; dot.y = ny - 9;
  dot.fills = [];
  dot.strokes = solid(C.BG);
  dot.strokeWeight = 2.5;
  dot.name = "b2b stakeholder node";
}

const b2bLabel = text(f, "B2B", {
  font: { family: "Inter", style: "Bold" }, size: 16,
  fill: C.BG, tracking: 30, align: "CENTER", name: "b2b label",
});
b2bLabel.resize(160, b2bLabel.height);
b2bLabel.x = cx1 - 80; b2bLabel.y = py + PANEL - 60;

const b2bCaption = text(f, "A COMMITTEE DECIDES", {
  font: { family: "Inter", style: "Regular" }, size: 10.5,
  fill: C.BG, tracking: 8, align: "CENTER", name: "b2b caption",
});
b2bCaption.opacity = 0.55;
b2bCaption.resize(200, b2bCaption.height);
b2bCaption.x = cx1 - 100; b2bCaption.y = py + PANEL - 36;

// ── RIGHT half: B2C — one person, one fast decision ──────────────
const cx2 = px + half + half / 2;
const cy2 = py + PANEL / 2 - 18;

const b2cDot = figma.createEllipse();
f.appendChild(b2cDot);
b2cDot.resize(30, 30);
b2cDot.x = cx2 - 15; b2cDot.y = cy2 - 15;
b2cDot.fills = solid(C.GOLD);
b2cDot.name = "b2c decision dot";

// motion arc suggesting a fast scroll/swipe arriving at the single dot
const arc = figma.createVector();
f.appendChild(arc);
arc.name = "b2c motion arc";
arc.vectorPaths = [{
  windingRule: "NONE",
  data: `M ${cx2 - 70} ${cy2 - 34} Q ${cx2 - 20} ${cy2 - 46} ${cx2 + 2} ${cy2 - 14}`,
}];
arc.strokes = solid(C.GOLD);
arc.strokeWeight = 2.5;
arc.strokeCap = "ROUND";
arc.opacity = 0.55;

const b2cLabel = text(f, "B2C", {
  font: { family: "Inter", style: "Bold" }, size: 16,
  fill: C.BG, tracking: 30, align: "CENTER", name: "b2c label",
});
b2cLabel.resize(160, b2cLabel.height);
b2cLabel.x = cx2 - 80; b2cLabel.y = py + PANEL - 60;

const b2cCaption = text(f, "ONE THUMB DECIDES", {
  font: { family: "Inter", style: "Regular" }, size: 10.5,
  fill: C.BG, tracking: 8, align: "CENTER", name: "b2c caption",
});
b2cCaption.opacity = 0.55;
b2cCaption.resize(200, b2cCaption.height);
b2cCaption.x = cx2 - 100; b2cCaption.y = py + PANEL - 36;

// ── text column, left ────────────────────────────────────────
const colW = plateX - PAD - 46;

const over = text(f, OVERLINE, {
  font: { family: "Inter", style: "Bold" }, size: 15,
  fill: C.GOLD, tracking: 14, name: "overline",
});
over.x = PAD; over.y = 96;

let y = 156;
const LINE = 82;
HEADLINE.forEach(([chars, fill], i) => {
  const t = text(f, chars, {
    font: { family: "Anton", style: "Regular" }, size: 74,
    fill, lineHeight: LINE, name: `headline ${i + 1}`,
  });
  if (t.width > colW) {                    // shrink rather than wrap
    t.fontSize = Math.floor(74 * (colW / t.width));
  }
  t.x = PAD;
  t.y = y;
  y += LINE;
});

const sub = text(f, SUBLINE, {
  font: { family: "Inter", style: "Regular" }, size: 25,
  fill: C.MUTED, lineHeight: 34, name: "subline",
});
sub.textAutoResize = "HEIGHT";
sub.resize(colW, sub.height);
sub.x = PAD;
sub.y = y + 26;

const foot = text(f, FOOTLINE, {
  font: { family: "Inter", style: "Bold" }, size: 13,
  fill: C.CREAM, tracking: 10, name: "footline",
});
foot.x = PAD;
foot.y = H - 74;

figma.currentPage.selection = [f];
figma.viewport.scrollAndZoomIntoView([f]);

console.log(
  `B2B vs B2C cover built: ${W}×${H}.\n` +
  `Export the frame at 2x PNG and use it as the LinkedIn article cover.`
);
