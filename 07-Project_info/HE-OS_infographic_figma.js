// HE-OS body-analogy infographic (single frame, 1080x1350).
// Paste into Figma > Plugins > Scripter > Run. Then export the frame as PNG.
// ES5, ASCII only, uses Inter (ships with Figma by default).

var W = 1080;
var H = 1350;

var DARK   = { r: 0.09, g: 0.08, b: 0.07 };
var CARD   = { r: 0.13, g: 0.115, b: 0.10 };
var CREAM  = { r: 0.95, g: 0.92, b: 0.85 };
var GOLD   = { r: 0.86, g: 0.66, b: 0.24 };
var GRAY   = { r: 0.66, g: 0.62, b: 0.56 };
var BROWNL = { r: 0.75, g: 0.48, b: 0.28 };

function part(n, name, eq, a, b) { return { n: n, part: name, eq: eq, a: a, b: b }; }

var PARTS = [
  part("01", "THE BRAIN", "= core intelligence", "Writes the content for six channels", "Picks the angle, adapts per platform"),
  part("02", "THE MEMORY", "= brain + its books", "Brand voice and every rule, stored", "Never forgets a single correction"),
  part("03", "THE HANDS", "= brain + hands", "Makes the media, publishes everywhere", "Ships. It does not just think"),
  part("04", "THE NERVOUS SYSTEM", "= connects everything", "Wires the store and every platform", "Runs on schedule, catches up on wake"),
  part("05", "THE EYES", "= sees what works", "Reads its own results every week", "Plans on evidence, not opinion"),
  part("06", "THE IMMUNE SYSTEM", "= quality gate", "Scores every post from 0 to 100", "Blocks off-brand before it ships")
];

function addRect(parent, x, y, w, h, c, radius) {
  var rect = figma.createRectangle();
  rect.x = x; rect.y = y; rect.resize(w, h);
  rect.fills = [{ type: "SOLID", color: c }];
  if (radius) { rect.cornerRadius = radius; }
  parent.appendChild(rect);
  return rect;
}

function txt(parent, s, x, y, w, size, style, c, align, spacing) {
  var t = figma.createText();
  t.fontName = { family: "Inter", style: style };
  t.characters = s;
  t.fontSize = size;
  t.fills = [{ type: "SOLID", color: c }];
  if (align) { t.textAlignHorizontal = align; }
  if (spacing) { t.letterSpacing = { unit: "PERCENT", value: spacing }; }
  t.x = x; t.y = y;
  t.resize(w, t.height);
  parent.appendChild(t);
  return t;
}

function build() {
  var frame = figma.createFrame();
  frame.name = "HE-OS Infographic";
  frame.resize(W, H);
  frame.fills = [{ type: "SOLID", color: DARK }];
  frame.clipsContent = true;

  txt(frame, "HE-OS", 64, 66, W - 128, 96, "Black", CREAM, "LEFT", -2);
  addRect(frame, 66, 176, 120, 8, GOLD, 4);
  txt(frame, "The marketing system I built instead of an agency", 64, 200, W - 128, 30, "Medium", GRAY, "LEFT");
  txt(frame, "One founder. One body. Every channel, every day.", 64, 240, W - 128, 26, "Regular", BROWNL, "LEFT");

  var top = 308;
  var rowH = 144;
  var gap = 12;
  for (var i = 0; i < PARTS.length; i++) {
    var y = top + i * (rowH + gap);
    var p = PARTS[i];
    addRect(frame, 48, y, W - 96, rowH, CARD, 18);
    addRect(frame, 72, y + 28, 88, 88, DARK, 14);
    txt(frame, p.n, 72, y + 48, 88, 40, "Black", GOLD, "CENTER");
    txt(frame, p.part, 192, y + 24, W - 192 - 72, 34, "Bold", CREAM, "LEFT");
    txt(frame, p.eq, 192, y + 64, W - 192 - 72, 26, "Semi Bold", GOLD, "LEFT");
    txt(frame, "- " + p.a, 192, y + 96, W - 192 - 72, 22, "Regular", GRAY, "LEFT");
    txt(frame, "- " + p.b, 192, y + 122, W - 192 - 72, 22, "Regular", GRAY, "LEFT");
  }

  var fy = top + PARTS.length * (rowH + gap) + 6;
  addRect(frame, 48, fy, W - 96, 2, BROWNL, 0);
  txt(frame, "THE POWER COFFEE", 64, fy + 16, 520, 22, "Bold", BROWNL, "LEFT", 8);
  txt(frame, "A body beats a retainer.", W - 476, fy + 12, 412, 28, "Bold", CREAM, "RIGHT");

  figma.currentPage.appendChild(frame);
  figma.viewport.scrollAndZoomIntoView([frame]);
}

function main() {
  return figma.loadFontAsync({ family: "Inter", style: "Regular" }).then(function () {
    return figma.loadFontAsync({ family: "Inter", style: "Medium" });
  }).then(function () {
    return figma.loadFontAsync({ family: "Inter", style: "Semi Bold" });
  }).then(function () {
    return figma.loadFontAsync({ family: "Inter", style: "Bold" });
  }).then(function () {
    return figma.loadFontAsync({ family: "Inter", style: "Black" });
  }).then(function () {
    build();
    figma.notify("HE-OS infographic created");
  });
}

main();
