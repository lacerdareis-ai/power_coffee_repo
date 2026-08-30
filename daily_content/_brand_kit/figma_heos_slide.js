// ============================================================
// THE POWER COFFEE — Pitch deck slide: "HE-OS"
// Matches Deck-Power-Coffee slide 10 ("Business Model & Go-to-Market") style:
// white bg, black Anton two-line headline, gray subtitle, three left-aligned
// bulleted subsections with bold caps mini-headers.
// Figma Scripter — paste into: Plugins → Scripter → Run
//
// Output: one 1920 × 1080 frame (matches the deck's slide canvas size).
// Reference render (Pillow, for visual verification before porting here):
// scratchpad/deck/heos_slide.py → heos_slide.png
// ============================================================

// ── BRAND TOKENS ─────────────────────────────────────────────
const C = {
  BLACK: { r: 17 / 255,  g: 17 / 255,  b: 17 / 255  }, // #111111
  GRAY:  { r: 90 / 255,  g: 90 / 255,  b: 90 / 255  }, // #5A5A5A
  WHITE: { r: 1, g: 1, b: 1 },
};

const W = 1920, H = 1080;
const MARGIN = 130;

const TITLE_LINES = ["HE-OS: THE CONTENT ENGINE", "NOBODY ELSE IS RUNNING"];
const SUBTITLE = "AI-run operations — from brand strategy to six channels, unattended, every day.";

const SECTIONS = [
  {
    head: "THE PIPELINE",
    bullets: [
      "Brain (strategy) → Claude drafts 6 platforms + video/image prompts",
      "QA Critic auto-scores every post — blocks banned claims, wrong URLs, off-brand jargon",
      "Approved content publishes unattended at 4am, 12pm, and Saturdays",
    ],
  },
  {
    head: "WHAT SHIPS DAILY",
    bullets: [
      "Instagram (reel / carousel / story, rotates by weekday), X, LinkedIn, Telegram",
      "Shopify Blog (Tue/Thu) and Email newsletter (Sat) — generated only on the days they publish",
    ],
  },
  {
    head: "WHY IT'S A MOAT",
    bullets: [
      "Replaces a ~$10K/mo agency retainer with one founder and Claude",
      "Same-day content velocity a funded competitor can't match without headcount",
    ],
  },
];

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
  parent.appendChild(t);            // parent BEFORE positioning (Scripter quirk)
  t.characters = chars;
  t.fontSize = o.size;
  t.fills = solid(o.fill);
  if (o.lineHeight) t.lineHeight = { unit: "PIXELS", value: o.lineHeight };
  if (o.letterSpacing) t.letterSpacing = { unit: "PIXELS", value: o.letterSpacing };
  t.x = o.x; t.y = o.y;
  if (o.width) {
    t.textAutoResize = "HEIGHT";
    t.resize(o.width, t.height);
  } else {
    t.textAutoResize = "WIDTH_AND_HEIGHT";
  }
  if (o.name) t.name = o.name;
  return t;
}

// ── BUILD ─────────────────────────────────────────────────────
await fonts();

// place clear of anything already on the page
let ox = 0;
for (const n of figma.currentPage.children) ox = Math.max(ox, n.x + n.width);
ox += 200;

const f = figma.createFrame();
f.name = "HE-OS — pitch deck slide (1920×1080)";
figma.currentPage.appendChild(f);
f.resize(W, H);
f.x = ox;
f.y = 0;
f.fills = solid(C.WHITE);
f.clipsContent = true;

// ── title (two-line Anton headline) ────────────────────────────
const TITLE_LINE_H = 70;
TITLE_LINES.forEach((line, i) => {
  const t = text(f, line, {
    font: { family: "Anton", style: "Regular" }, size: 64,
    fill: C.BLACK, lineHeight: TITLE_LINE_H, name: `title line ${i + 1}`,
  });
  t.x = MARGIN;
  t.y = 108 + i * TITLE_LINE_H;
});

// ── SUBTITLE ────────────────────────────────────────────────────
const sub = text(f, SUBTITLE, {
  font: { family: "Inter", style: "Regular" }, size: 24,
  fill: C.GRAY, width: W - MARGIN * 2, name: "subtitle",
});
sub.x = MARGIN;
sub.y = 108 + TITLE_LINES.length * TITLE_LINE_H + 22;

// ── SECTIONS ────────────────────────────────────────────────────
let cursorY = sub.y + 90;
const HEAD_SIZE = 30, BODY_SIZE = 24, BODY_LINE_H = 34;
const BULLET_INDENT = 30;
const bodyMaxW = W - MARGIN * 2 - BULLET_INDENT;

for (const section of SECTIONS) {
  const head = text(f, section.head + ":", {
    font: { family: "Inter", style: "Bold" }, size: HEAD_SIZE,
    fill: C.BLACK, name: `section head — ${section.head}`,
  });
  head.x = MARGIN;
  head.y = cursorY;
  cursorY += 52;

  for (const bullet of section.bullets) {
    const b = text(f, bullet, {
      font: { family: "Inter", style: "Regular" }, size: BODY_SIZE,
      fill: C.BLACK, width: bodyMaxW, lineHeight: BODY_LINE_H, name: "bullet",
    });
    b.x = MARGIN + BULLET_INDENT;
    b.y = cursorY;

    const dot = figma.createEllipse();
    dot.resize(8, 8);
    dot.x = MARGIN + 4;
    dot.y = cursorY + 10;
    dot.fills = solid(C.BLACK);
    f.appendChild(dot);

    cursorY += b.height + 6;
  }
  cursorY += 34;
}

// ── PIPELINE ILLUSTRATION — horizontal flow diagram under the bullets ────
// Visualizes THE PIPELINE bullets above it: BRAIN -> CLAUDE -> QA CRITIC -> PUBLISH.
const STAGES = [
  { label: "BRAIN",     caption: "brand strategy" },
  { label: "CLAUDE",    caption: "drafts 6 platforms" },
  { label: "QA CRITIC", caption: "auto-scores + gates" },
  { label: "PUBLISH",   caption: "6 channels, unattended" },
];

const BOX_W = 330, BOX_H = 92, BOX_GAP = 88;
const totalW = STAGES.length * BOX_W + (STAGES.length - 1) * BOX_GAP;
const diagX0 = (W - totalW) / 2;
const diagTop = cursorY + 12;

const ARROW_SVG = '<svg width="14" height="14" viewBox="0 0 14 14">'
  + '<path d="M0 0 L14 7 L0 14 Z" fill="#111111"/></svg>';

STAGES.forEach((stage, i) => {
  const bx = diagX0 + i * (BOX_W + BOX_GAP);

  const box = figma.createRectangle();
  f.appendChild(box);
  box.resize(BOX_W, BOX_H);
  box.x = bx; box.y = diagTop;
  box.fills = [];
  box.strokes = solid(C.BLACK);
  box.strokeWeight = 2;
  box.cornerRadius = 10;
  box.name = `pipeline box — ${stage.label}`;

  const label = text(f, stage.label, {
    font: { family: "Inter", style: "Bold" }, size: 22,
    fill: C.BLACK, name: `pipeline label — ${stage.label}`,
  });
  label.textAlignHorizontal = "CENTER";
  label.x = bx + (BOX_W - label.width) / 2;
  label.y = diagTop + 22;

  const cap = text(f, stage.caption, {
    font: { family: "Inter", style: "Regular" }, size: 16,
    fill: C.GRAY, name: `pipeline caption — ${stage.label}`,
  });
  cap.textAlignHorizontal = "CENTER";
  cap.x = bx + (BOX_W - cap.width) / 2;
  cap.y = diagTop + BOX_H + 14;

  if (i < STAGES.length - 1) {
    const ax0 = bx + BOX_W + 14;
    const ax1 = ax0 + BOX_GAP - 28;
    const ay = diagTop + BOX_H / 2;

    const shaft = figma.createLine();
    f.appendChild(shaft);
    shaft.x = ax0; shaft.y = ay;
    shaft.resize(ax1 - ax0, 0);
    shaft.strokes = solid(C.BLACK);
    shaft.strokeWeight = 2;
    shaft.name = "pipeline arrow shaft";

    const arrow = figma.createNodeFromSvg(ARROW_SVG);
    f.appendChild(arrow);
    arrow.x = ax1; arrow.y = ay - 7;
    arrow.name = "pipeline arrow head";
  }
});

figma.currentPage.selection = [f];
figma.viewport.scrollAndZoomIntoView([f]);

console.log(`HE-OS slide built: ${W}×${H}. Export the frame at 1x PNG to drop into the deck.`);
