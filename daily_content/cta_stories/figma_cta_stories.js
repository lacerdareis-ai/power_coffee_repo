// Power Coffee — CTA STORIES (10 slides) — Figma Scripter
// 1080×1920 px | Instagram Story format | CTA → thepowercoffee.com
// Paste into Figma → Plugins → Scripter → Run
// Export each frame at 1x as JPG → story1.jpg … story10.jpg

const COLORS = {
  BLACK:   { r: 0.07, g: 0.06, b: 0.05 },
  BROWN:   { r: 0.48, g: 0.24, b: 0.12 },
  BROWN_L: { r: 0.75, g: 0.48, b: 0.28 },
  CREAM:   { r: 0.94, g: 0.91, b: 0.84 },
  WHITE:   { r: 1,    g: 1,    b: 1    },
};
function col(c) { return (typeof c === "string") ? COLORS[c] : c; }

const W = 1080, H = 1920, GAP = 60, TOTAL = 10;
const SITE   = "thepowercoffee.com";
const HANDLE = "@powercoffee.ofc";

// ── SLIDE DATA ────────────────────────────────────────────────────────────────
// Funnel arc: Problem (1-3) → Solution (4-6) → Comparison + proof (7-8) → Simple (9) → CTA (10)

const SLIDES = [
  {
    id: 1,
    overline: "THE ENERGY QUESTION",
    headline: "STILL\nCRASHING\nBY 10AM?",
    subtext: "It's not you. It's your formula.",
    accent: "BROWN",
    bg: "BLACK",
  },
  {
    id: 2,
    overline: "WHY IT HAPPENS",
    headline: "REGULAR\nCOFFEE\nPEAKS IN\n45 MINUTES.",
    subtext: "Then cortisol drops. Blood sugar crashes. Focus fades. That's not a willpower problem — it's a formula problem.",
    accent: "BROWN_L",
    bg: "BLACK",
  },
  {
    id: 3,
    overline: "THE REAL COST",
    headline: "THE 10AM\nFOG IS\nNOT NORMAL.",
    subtext: "You're not tired. You're running on the wrong fuel. Every single morning.",
    accent: "BROWN",
    bg: "BLACK",
  },
  {
    id: 4,
    overline: "THE UPGRADE",
    headline: "SAME\nRITUAL.\nBETTER\nFORMULA.",
    subtext: "One scoop into whatever you're already drinking. No new habit. Just better ingredients.",
    accent: "BROWN_L",
    bg: "BLACK",
  },
  {
    id: 5,
    overline: "WHAT'S INSIDE",
    headline: "11\nINGREDIENTS.\nZERO\nFILLERS.",
    subtext: "175mg caffeine · Matcha · Taurine · 5g Pea Protein · Cinnamon · Ginger · Ginkgo",
    pills: ["NO CRASH", "CLEAN LABEL", "SUGAR-FREE"],
    accent: "BROWN",
    bg: "BLACK",
  },
  {
    id: 6,
    overline: "THE MATH",
    headline: "$1.19\nA MORNING.\nFOCUS\nTHROUGH NOON.",
    subtext: "Fifteen mornings for $17.90. Less than three lattes. More than your entire stack.",
    accent: "BROWN_L",
    bg: "BLACK",
  },
  {
    id: 7,
    overline: "THE COMPARISON",
    headline: "$6 LATTE:\n45 MINUTES.\n\n$1.19 SCOOP:\n5 HOURS.",
    subtext: "Same ritual. Different outcome. The math isn't complicated.",
    accent: "BROWN",
    bg: "BLACK",
  },
  {
    id: 8,
    overline: "HOW IT FEELS",
    headline: "DAY 3: NO\nSECOND CUP.\nDAY 5: NO\n2PM SLUMP.",
    subtext: "A clean arc from first scoop through your last meeting. That's what the upgrade actually feels like.",
    accent: "BROWN_L",
    bg: "BLACK",
  },
  {
    id: 9,
    overline: "HOW SIMPLE",
    headline: "SCOOP.\nSTIR.\nDONE.\nWIN.",
    subtext: "One step between you and your best morning. No blender. No new routine. Just upgraded coffee.",
    accent: "BROWN",
    bg: "BLACK",
  },
  {
    id: 10,
    overline: "YOUR FIRST WIN STARTS HERE",
    headline: "TRY IT\nTODAY.",
    subtext: "15 mornings. $17.90. One scoop into what you're already drinking. See what changes.",
    isCTA: true,
    accent: "CREAM",
    bg: "BROWN",
  },
];

// ── HELPERS ───────────────────────────────────────────────────────────────────

function addRect(parent, x, y, w, h, color, opacity) {
  if (opacity === undefined) { opacity = 1; }
  var r = figma.createRectangle();
  r.x = x; r.y = y; r.resize(w, h);
  r.fills = [{ type: "SOLID", color: col(color), opacity: opacity }];
  parent.appendChild(r);
  return r;
}

async function addText(parent, txt, x, y, w, size, weight, color, align, lineH) {
  if (!align) { align = "LEFT"; }
  if (!lineH) { lineH = 1.05; }
  await figma.loadFontAsync({ family: "Inter", style: weight });
  var t = figma.createText();
  t.fontName = { family: "Inter", style: weight };
  t.characters = txt;
  t.fontSize = size;
  t.textAlignHorizontal = align;
  t.fills = [{ type: "SOLID", color: col(color) }];
  t.lineHeight = { unit: "PERCENT", value: lineH * 100 };
  t.x = x; t.y = y;
  t.resize(w, t.height);
  parent.appendChild(t);
  return t;
}

// ── BUILD STORY FRAME ─────────────────────────────────────────────────────────

async function buildStory(data, offsetX) {
  var frame = figma.createFrame();
  frame.name = "Story " + (data.id < 10 ? "0" + data.id : "" + data.id) + (data.isCTA ? " — CTA" : "");
  frame.resize(W, H);
  frame.x = offsetX; frame.y = 0;
  frame.clipsContent = true;
  frame.fills = [{ type: "SOLID", color: col(data.bg) }];

  // Diagonal texture lines (very faint)
  for (var i = 0; i < 10; i++) {
    var line = figma.createLine();
    line.x = -300 + i * 160; line.y = 0;
    line.resize(H * 1.3, 0);
    line.rotation = -70;
    line.strokes = [{ type: "SOLID", color: col(data.accent), opacity: 0.04 }];
    line.strokeWeight = 80;
    frame.appendChild(line);
  }

  // Large faint watermark number
  await figma.loadFontAsync({ family: "Inter", style: "Black" });
  var wm = figma.createText();
  wm.fontName = { family: "Inter", style: "Black" };
  wm.characters = (data.id < 10 ? "0" + data.id : "" + data.id);
  wm.fontSize = 700;
  wm.fills = [{ type: "SOLID", color: col(data.accent), opacity: 0.06 }];
  wm.x = 240; wm.y = 900;
  frame.appendChild(wm);

  // ── TOP BAR (0–120px) ──────────────────────────────────────────────────────
  var topColor = data.isCTA ? "BLACK" : "BROWN";
  addRect(frame, 0, 0, W, 120, topColor);
  await addText(frame, "POWER COFFEE", 80, 46, 500, 15, "Black", "WHITE", "LEFT", 1.2);
  var cnt = (data.id < 10 ? "0" + data.id : "" + data.id) + " / " + (TOTAL < 10 ? "0" + TOTAL : "" + TOTAL);
  await addText(frame, cnt, W - 200, 50, 120, 12, "Regular", { r: 0.80, g: 0.77, b: 0.70 }, "RIGHT", 1.2);

  // ── CONTENT AREA (starts at y=200) ────────────────────────────────────────
  var P = 80;
  var curY = 200;

  // Overline
  if (data.overline) {
    var olNode = await addText(frame, data.overline, P, curY, W - P * 2, 13, "Bold", data.accent, "LEFT", 1.4);
    curY += Math.ceil(olNode.height) + 16;
  }

  // Accent rule under overline
  addRect(frame, P, curY, 56, 4, data.accent);
  curY += 32;

  // Headline
  var hlColor = data.isCTA ? "WHITE" : "CREAM";
  var hlSize  = data.isCTA ? 160 : 128;
  var hlNode  = await addText(frame, data.headline, P, curY, W - P * 2, hlSize, "Black", hlColor, "LEFT", 0.88);
  curY += Math.ceil(hlNode.height) + 44;

  // Divider
  addRect(frame, P, curY, W - P * 2, 2, data.accent, 0.5);
  curY += 28;

  // Pills (optional)
  if (data.pills) {
    var pillX = P;
    for (var j = 0; j < data.pills.length; j++) {
      await figma.loadFontAsync({ family: "Inter", style: "Bold" });
      var pf = figma.createFrame();
      pf.resize(200, 40); pf.x = pillX; pf.y = curY;
      pf.fills = [{ type: "SOLID", color: col(data.accent), opacity: 0.18 }];
      pf.cornerRadius = 4;
      frame.appendChild(pf);
      var pt = figma.createText();
      pt.fontName = { family: "Inter", style: "Bold" };
      pt.characters = data.pills[j]; pt.fontSize = 11;
      pt.textAlignHorizontal = "CENTER";
      pt.fills = [{ type: "SOLID", color: col(data.accent) }];
      pt.letterSpacing = { unit: "PERCENT", value: 18 };
      pt.resize(200, 40); pt.x = 0; pt.y = 13;
      pf.appendChild(pt);
      pillX += 216;
    }
    curY += 60;
  }

  // Subtext
  if (data.subtext) {
    var subColor = data.isCTA ? { r: 0.94, g: 0.91, b: 0.84 } : { r: 0.80, g: 0.74, b: 0.64 };
    await addText(frame, data.subtext, P, curY, W - P * 2, 27, "Regular", subColor, "LEFT", 1.65);
  }

  // ── BOTTOM CTA BAR (last 220px) ───────────────────────────────────────────
  var ctaH = 220;
  var ctaY = H - ctaH;
  var ctaBarColor = data.isCTA ? "BLACK" : "BROWN";
  addRect(frame, 0, ctaY, W, ctaH, ctaBarColor);

  // "ORDER NOW" label top-right of bar
  await addText(frame, "ORDER NOW  →", W - 300, ctaY + 38, 220, 11, "Bold", { r: 0.94, g: 0.84, b: 0.60 }, "RIGHT", 1.2);

  // URL (larger on final CTA slide)
  var urlSize = data.isCTA ? 44 : 30;
  await addText(frame, SITE, P, ctaY + 36, W - P * 2, urlSize, "Bold", "CREAM", "LEFT", 1.2);

  // Handle
  await addText(frame, HANDLE, P, ctaY + 36 + urlSize + 16, W - P * 2, 18, "Regular", { r: 0.90, g: 0.78, b: 0.56 }, "LEFT", 1.3);

  figma.currentPage.appendChild(frame);
  return frame;
}

// ── MAIN ──────────────────────────────────────────────────────────────────────

async function main() {
  var frames = [];
  for (var i = 0; i < SLIDES.length; i++) {
    var frame = await buildStory(SLIDES[i], i * (W + GAP));
    frames.push(frame);
  }
  figma.viewport.scrollAndZoomIntoView(frames);
  figma.notify("Power Coffee — 10 CTA Stories ready!", { timeout: 4000 });
}

main();
