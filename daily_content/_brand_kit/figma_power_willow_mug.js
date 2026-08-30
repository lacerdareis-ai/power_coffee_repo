// ============================================================
// THE POWER COFFEE — "Power Willow" mug
// Figma Scripter — paste into: Plugins → Scripter → Run
//
// A Blue-Willow / chinoiserie china pattern reinterpreted with the brand's own
// iconography, in the pouch's navy on white:
//   · willow tree      → coffee branch with weeping fronds
//   · the two doves    → two lightning bolts
//   · figures on the   → two walking mug mascots
//     bridge
//   · pagoda finial    → a lightning bolt
//   · border cartouche → alternating bolts and diamonds
//
// Everything is LINE ART (strokes), like real willow china — solid fills read as
// blobs at this scale. Geometry was designed and visually verified as SVG first;
// the path strings below are that same source.
//
// Output: one 1200 × 1400 frame, all layers named and grouped.
// Export the frame at 2x PNG, or copy the "pattern" group alone as print art.
// ============================================================

// ── TOKENS ────────────────────────────────────────────────────
const NAVY  = { r: 0x1F/255, g: 0x2E/255, b: 0x5A/255 };  // #1F2E5A, the pouch navy
const WHITE = { r: 1, g: 1, b: 1 };
const BG    = { r: 0xE9/255, g: 0xE5/255, b: 0xDE/255 };
const RIM   = { r: 0xC9/255, g: 0xCF/255, b: 0xDD/255 };
const INNER = { r: 0xF3/255, g: 0xF1/255, b: 0xEC/255 };

const W = 1200, H = 1400;
const BODY_X = 340, BODY_Y = 330, BODY_W = 560, BODY_H = 790;
const CX = BODY_X + BODY_W / 2;          // 620
const RIM_RY = 44;
const PX0 = BODY_X + 26, PX1 = BODY_X + BODY_W - 26;   // 366 .. 874
const BAND_TOP = 400, BAND_H = 78;

// motif paths, origin at 0,0
const BOLT    = "M 13 0 L 0 24 L 9 24 L 5 44 L 22 17 L 12 17 Z";
const DIAMOND = "M 10 0 L 20 12 L 10 24 L 0 12 Z";
const LEAF    = "M 0 0 Q 15 -12 30 0 Q 15 12 0 0 Z";
const FROND   = "M 0 0 q -7 22 3 38";

const solid = (c) => [{ type: "SOLID", color: c }];
const roof  = (hw, rise) => `M ${-hw} 8 Q 0 ${-rise} ${hw} 8`;

let frame;

// ── HELPERS ───────────────────────────────────────────────────
// NOTE ON vectorPaths: Figma interprets the path data in the node's own
// coordinate space. These paths carry absolute canvas coordinates, so each
// vector is left at x/y = 0 inside the frame and lands where the data says.
// If a shape ever appears offset, that is this behaviour — fix the data, not
// the node position.
function vpath(d, opt = {}) {
  const v = figma.createVector();
  frame.appendChild(v);
  v.vectorPaths = [{ windingRule: "NONZERO", data: d }];
  v.fills   = opt.fill ? solid(opt.fill) : [];
  v.strokes = opt.stroke ? solid(opt.stroke) : [];
  if (opt.weight) v.strokeWeight = opt.weight;
  v.strokeCap  = opt.cap || "ROUND";
  v.strokeJoin = "ROUND";
  if (opt.name) v.name = opt.name;
  return v;
}

// a motif placed by translation (+ optional rotation / uniform scale)
function motif(d, x, y, opt = {}) {
  const v = figma.createVector();
  frame.appendChild(v);
  v.vectorPaths = [{ windingRule: "NONZERO", data: d }];
  v.fills   = opt.fill ? solid(opt.fill) : [];
  v.strokes = opt.stroke ? solid(opt.stroke) : [];
  if (opt.weight) v.strokeWeight = opt.weight;
  v.strokeCap = "ROUND";
  if (opt.scale && opt.scale !== 1) v.rescale(opt.scale);
  v.x = x; v.y = y;
  if (opt.rot) v.rotation = opt.rot;        // degrees, counter-clockwise
  if (opt.name) v.name = opt.name;
  return v;
}

function line(x1, y1, x2, y2, weight, name) {
  return vpath(`M ${x1} ${y1} L ${x2} ${y2}`, { stroke: NAVY, weight, name });
}

function ellipse(cx, cy, rx, ry, opt = {}) {
  const e = figma.createEllipse();
  frame.appendChild(e);
  e.resize(rx * 2, ry * 2);
  e.x = cx - rx; e.y = cy - ry;
  e.fills   = opt.fill ? solid(opt.fill) : [];
  e.strokes = opt.stroke ? solid(opt.stroke) : [];
  if (opt.weight) e.strokeWeight = opt.weight;
  if (opt.name) e.name = opt.name;
  return e;
}

function rect(x, y, w, h, r, opt = {}) {
  const n = figma.createRectangle();
  frame.appendChild(n);
  n.resize(w, h);
  n.x = x; n.y = y;
  n.cornerRadius = r;
  n.fills   = opt.fill ? solid(opt.fill) : [];
  n.strokes = opt.stroke ? solid(opt.stroke) : [];
  if (opt.weight) n.strokeWeight = opt.weight;
  if (opt.name) n.name = opt.name;
  return n;
}

// ── BUILD ─────────────────────────────────────────────────────
await figma.loadFontAsync({ family: "Inter", style: "Bold" });

let ox = 0;
for (const n of figma.currentPage.children) ox = Math.max(ox, n.x + n.width);
ox += 200;

frame = figma.createFrame();
frame.name = "Power Willow mug";
figma.currentPage.appendChild(frame);
frame.resize(W, H);
frame.x = ox; frame.y = 0;
frame.fills = solid(BG);
frame.clipsContent = true;

// handle — drawn first so the body overlaps it
ellipse(BODY_X + 8, 700, 104, 136, { stroke: WHITE, weight: 46, name: "handle" });
ellipse(BODY_X + 8, 700, 127, 159, { stroke: RIM, weight: 2, name: "handle outer" });
ellipse(BODY_X + 8, 700, 81, 113,  { stroke: RIM, weight: 2, name: "handle inner" });

// body + rim
rect(BODY_X, BODY_Y, BODY_W, BODY_H, 30, { fill: WHITE, stroke: RIM, weight: 2, name: "body" });
ellipse(CX, BODY_Y, BODY_W / 2, RIM_RY, { fill: WHITE, stroke: RIM, weight: 2, name: "rim" });
ellipse(CX, BODY_Y + 6, BODY_W / 2 - 26, RIM_RY - 12, { fill: INNER, stroke: RIM, weight: 1.5, name: "rim inner" });

// ── top border band ──────────────────────────────────────────
[[BAND_TOP, 4], [BAND_TOP + 8, 2], [BAND_TOP + BAND_H - 8, 2], [BAND_TOP + BAND_H, 4]]
  .forEach(([y, w]) => line(PX0, y, PX1, y, w, "band rule"));

let bx = PX0 + 18, i = 0;
const bandCy = BAND_TOP + BAND_H / 2;
while (bx < PX1 - 26) {
  if (i % 2 === 0) {
    motif(BOLT, bx - 11, bandCy - 22, { fill: NAVY, name: "band bolt" });
  } else {
    motif(DIAMOND, bx - 10, bandCy - 12, { stroke: NAVY, weight: 3, name: "band diamond" });
    ellipse(bx, bandCy, 3, 3, { fill: NAVY, name: "band dot" });
  }
  bx += 66; i++;
}

// ── pagoda ───────────────────────────────────────────────────
[[122, 566, 34], [98, 630, 30], [74, 690, 26]].forEach(([hw, y, rise]) => {
  vpath(`M ${CX - hw} ${y + 8} Q ${CX} ${y - rise} ${CX + hw} ${y + 8}`,
        { stroke: NAVY, weight: 4, name: "roof" });
  vpath(`M ${CX - (hw - 12)} ${y + 19} Q ${CX} ${y + 11 - (rise - 8)} ${CX + (hw - 12)} ${y + 19}`,
        { stroke: NAVY, weight: 2.5, name: "roof inner" });
});
[[580, 626], [644, 686]].forEach(([y0, y1]) => {
  [-34, 34].forEach((dx) => line(CX + dx, y0, CX + dx, y1, 4, "storey post"));
});

rect(CX - 52, 706, 104, 86, 4, { stroke: NAVY, weight: 4, name: "pavilion" });
line(CX - 18, 706, CX - 18, 792, 4, "pavilion post");
line(CX + 18, 706, CX + 18, 792, 4, "pavilion post");
vpath(`M ${CX - 10} 792 q 10 -30 20 0`, { stroke: NAVY, weight: 3, name: "doorway" });
line(CX - 72, 796, CX + 72, 796, 4, "platform");
motif(BOLT, CX - 11, 508, { fill: NAVY, name: "finial bolt" });

// ── coffee branches (the willow) ─────────────────────────────
vpath(`M ${PX0 + 4} 690 C ${PX0 + 70} 600 ${PX0 + 150} 566 ${CX - 140} 560`,
      { stroke: NAVY, weight: 5, name: "branch left" });
vpath(`M ${PX1 - 4} 676 C ${PX1 - 70} 590 ${PX1 - 150} 558 ${CX + 140} 552`,
      { stroke: NAVY, weight: 5, name: "branch right" });

// weeping fronds
[[432, 626], [478, 600], [526, 582], [574, 568]].forEach(([fx, fy]) => {
  motif(FROND, fx, fy, { stroke: NAVY, weight: 3, name: "frond" });
  motif(LEAF, fx - 8, fy + 38, { stroke: NAVY, weight: 4, scale: 0.5, rot: -70, name: "frond leaf" });
});
[[PX1 - 66, 612], [PX1 - 112, 588], [PX1 - 160, 570]].forEach(([fx, fy]) => {
  motif(FROND, fx, fy, { stroke: NAVY, weight: 3, name: "frond" });
  motif(LEAF, fx + 2, fy + 38, { stroke: NAVY, weight: 4, scale: 0.5, rot: 70, name: "frond leaf" });
});
[[470, 590, -22], [548, 566, -8], [PX1 - 104, 578, 22]].forEach(([lx, ly, rot]) => {
  motif(LEAF, lx, ly, { stroke: NAVY, weight: 3, rot, name: "leaf" });
});

// ── two "birds" → bolts ──────────────────────────────────────
motif(BOLT, CX - 186, 520, { fill: NAVY, rot: 22, scale: 0.86, name: "bolt bird" });
motif(BOLT, CX + 168, 506, { fill: NAVY, rot: -20, scale: 0.68, name: "bolt bird" });

// ── bridge + two walking mugs ────────────────────────────────
const BY = 892;
vpath(`M ${CX - 172} ${BY} Q ${CX} ${BY - 58} ${CX + 172} ${BY}`, { stroke: NAVY, weight: 4, name: "bridge" });
vpath(`M ${CX - 172} ${BY + 16} Q ${CX} ${BY - 42} ${CX + 172} ${BY + 16}`, { stroke: NAVY, weight: 3, name: "bridge rail" });
[[-150, 6], [-96, -14], [96, -14], [150, 6]].forEach(([t, dy]) =>
  line(CX + t, BY + dy - 26, CX + t, BY + dy + 18, 3, "bridge post"));

[[CX - 58, BY - 74], [CX + 26, BY - 78]].forEach(([mx, my]) => {
  rect(mx, my, 30, 34, 5, { stroke: NAVY, weight: 4, name: "mascot body" });
  vpath(`M ${mx + 30} ${my + 9} q 14 8 0 16`, { stroke: NAVY, weight: 4, name: "mascot handle" });
  line(mx + 8, my + 34, mx + 4, my + 48, 4, "mascot leg");
  line(mx + 22, my + 34, mx + 26, my + 48, 4, "mascot leg");
  motif(BOLT, mx + 7, my - 22, { fill: NAVY, scale: 0.44, name: "mascot bolt" });
});

// ── water ────────────────────────────────────────────────────
[946, 966].forEach((yy, k) =>
  vpath(`M ${PX0 + 30 + k * 22} ${yy} q 30 -10 60 0 t 60 0 t 60 0 t 60 0 t 60 0`,
        { stroke: NAVY, weight: 3, name: "water" }));

// ── foreground fence ─────────────────────────────────────────
const FY = 1004;
line(PX0 + 10, FY, PX1 - 10, FY, 4, "fence rail");
line(PX0 + 10, FY + 18, PX1 - 10, FY + 18, 4, "fence rail");
for (let fx = PX0 + 24; fx < PX1 - 16; fx += 36) line(fx, FY - 13, fx, FY + 31, 4, "fence post");

// ── bottom rule + wordmark ───────────────────────────────────
line(PX0, 1062, PX1, 1062, 4, "base rule");
const t = figma.createText();
frame.appendChild(t);
t.fontName = { family: "Inter", style: "Bold" };
t.characters = "THE POWER COFFEE";
t.fontSize = 24;
t.letterSpacing = { unit: "PERCENT", value: 28 };
t.fills = solid(NAVY);
t.textAlignHorizontal = "CENTER";
t.textAutoResize = "HEIGHT";
t.resize(PX1 - PX0, t.height);
t.x = PX0; t.y = 1080;
t.name = "wordmark";

figma.currentPage.selection = [frame];
figma.viewport.scrollAndZoomIntoView([frame]);

console.log(
  `Power Willow mug built — ${W}×${H}, ${frame.children.length} layers.\n` +
  `Export the frame at 2x PNG, or lift the pattern alone for print/packaging art.`
);
