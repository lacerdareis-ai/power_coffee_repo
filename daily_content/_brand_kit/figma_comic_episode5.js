// ============================================================
// THE POWER COFFEE — "Eisner Stories" Ep. 5 · "The Parent"
// Figma Scripter — paste into: Plugins → Scripter → Run
//
// Builds the 4 carousel slides at 1080 × 1350, with the exact chrome
// make_comic_episode.compose_slides() produces: black header bar with the
// episode tag, gold slide counter, cream caption box with a 3px black rule,
// and the black footer bar in gold.
//
// WHAT THIS DOES NOT DO: generate the noir panel art. Figma cannot draw that.
// Each slide gets a full-bleed rectangle named "panel_art" — select it and set
// an image fill (or paste the panel over it) once the art exists. Everything
// else is finished and positioned correctly.
//
// The panel prompt for each slide is placed on the canvas beneath its frame so
// it can be copied straight into an image generator.
//
// EXPORT: select the four frames → Export → 1x JPG → name them
// carousel_1..carousel_4.jpg → drop into the day folder. publisher.py picks up
// carousel_N.* automatically as an Instagram carousel.
// ============================================================

// ── TOKENS ────────────────────────────────────────────────────
// Sampled from make_comic_episode.py, NOT the general brand palette — the comic
// uses a deeper gold (#BF922A) than the brand's #D9A633.
const C = {
  BLACK: { r: 10 / 255, g: 10 / 255, b: 10 / 255 },   // #0A0A0A
  CREAM: { r: 247 / 255, g: 240 / 255, b: 224 / 255 }, // #F7F0E0
  GOLD:  { r: 191 / 255, g: 146 / 255, b: 42 / 255 },  // #BF922A
  PLACEHOLDER: { r: 0.14, g: 0.13, b: 0.12 },
};

const W = 1080, H = 1350;
const GAP = 120;
const EP = 5;
const TITLE = "The Parent";

const HEADER_H = 58;
const COUNTER_W = 70;
const FOOTER_H = 70;
const CAP_X = 40, CAP_Y = 90, CAP_PAD = 18, CAP_LINE = 38, CAP_SIZE = 30;
const CAP_MAX_TEXT_W = W - 140 - CAP_PAD * 2; // PIL wraps at W-140 incl. padding

const PANELS = [
  {
    caption: "THE THIRD TIME UP SINCE MIDNIGHT.",
    prompt:
      "A woman in her early 30s, hair disheveled, robe over pajamas, paces a dark nursery at 3am, " +
      "rocking a crying baby against her shoulder, eyes half-closed with exhaustion, moonlight through a window.",
  },
  {
    caption: "THE BABY WAS ASLEEP. SHE WASN'T.",
    prompt:
      "Dawn light through a kitchen window, the same woman - disheveled hair, robe over pajamas - slumped at " +
      "the kitchen table, staring blankly at a full pot of coffee she has no energy left to pour, baby monitor " +
      "on the table beside her.",
  },
  {
    caption: "THEN SOMETHING SHOWED UP LOUDER THAN THE EXHAUSTION.",
    prompt:
      "MASCOT bursts through the kitchen door in a blaze of light, dish towels and apron strings flying. " +
      "The same woman - robe over pajamas - looks up startled from the kitchen table. Comic book energy lines " +
      "radiating from the doorway.",
  },
  {
    caption: "THE FIRST WIN OF THE DAY. EVERY DAY.",
    prompt:
      "The same woman - hair now pulled back, robe traded for a jacket - walks out the front door into morning " +
      "sunlight, coffee cup in one hand, diaper bag on her shoulder, standing a little taller.",
  },
];

// ── HELPERS ───────────────────────────────────────────────────
const solid = (c) => [{ type: "SOLID", color: c }];

async function fonts() {
  // NOTE: Figma's Inter style is "Semi Bold" with a space — "SemiBold" throws.
  for (const s of ["Bold", "Semi Bold", "Regular"]) {
    await figma.loadFontAsync({ family: "Inter", style: s });
  }
}

function rect(parent, x, y, w, h, fill, name) {
  const r = figma.createRectangle();
  parent.appendChild(r);              // parent BEFORE positioning
  r.resize(w, h);
  r.x = x; r.y = y;
  r.fills = solid(fill);
  if (name) r.name = name;
  return r;
}

function text(parent, chars, opts) {
  const t = figma.createText();
  t.fontName = { family: "Inter", style: opts.weight || "Bold" };
  parent.appendChild(t);
  t.characters = chars;
  t.fontSize = opts.size;
  t.fills = solid(opts.fill);
  t.lineHeight = opts.lineHeight
    ? { unit: "PIXELS", value: opts.lineHeight }
    : { unit: "AUTO" };
  if (opts.letterSpacing) {
    t.letterSpacing = { unit: "PERCENT", value: opts.letterSpacing };
  }
  t.textAutoResize = "WIDTH_AND_HEIGHT";
  if (opts.maxWidth && t.width > opts.maxWidth) {
    t.textAutoResize = "HEIGHT";
    t.resize(opts.maxWidth, t.height);   // wrap like PIL's _wrap()
  }
  if (opts.align) t.textAlignHorizontal = opts.align;
  return t;
}

// ── BUILD ─────────────────────────────────────────────────────
await fonts();

// place the set clear of existing canvas content
let originX = 0;
for (const n of figma.currentPage.children) {
  originX = Math.max(originX, n.x + n.width);
}
originX += 200;

const frames = [];

for (let i = 0; i < PANELS.length; i++) {
  const p = PANELS[i];
  const n = i + 1;

  const f = figma.createFrame();
  f.name = `carousel_${n}`;
  figma.currentPage.appendChild(f);
  f.resize(W, H);
  f.x = originX + i * (W + GAP);
  f.y = 0;
  f.fills = solid(C.BLACK);
  f.clipsContent = true;

  // 1. full-bleed art plate — replace this fill with the generated panel
  const art = rect(f, 0, 0, W, H, C.PLACEHOLDER, "panel_art  ← set image fill here");
  const hint = text(f, `PANEL ${n}\nset image fill on "panel_art"`, {
    size: 34, fill: C.GOLD, weight: "Semi Bold", align: "CENTER", lineHeight: 46,
  });
  hint.name = "placeholder hint (delete once art is in)";
  hint.textAutoResize = "HEIGHT";
  hint.resize(W - 200, hint.height);
  hint.x = 100;
  hint.y = Math.round(H / 2 - hint.height / 2);
  hint.opacity = 0.5;

  // 2. header bar + episode tag
  rect(f, 0, 0, W, HEADER_H, C.BLACK, "header bar");
  const tag = text(f, `EISNER STORIES  ·  EP. ${EP}`, {
    size: 24, fill: C.CREAM, weight: "Bold", align: "CENTER",
  });
  tag.name = "episode tag";
  tag.textAutoResize = "HEIGHT";
  tag.resize(W, tag.height);
  tag.x = 0;
  tag.y = 16;

  // 3. gold slide counter, top-right
  rect(f, W - COUNTER_W, 0, COUNTER_W, HEADER_H, C.GOLD, "counter plate");
  const cnt = text(f, `${n}/4`, {
    size: 22, fill: C.BLACK, weight: "Bold", align: "CENTER",
  });
  cnt.name = "counter";
  cnt.textAutoResize = "HEIGHT";
  cnt.resize(COUNTER_W, cnt.height);
  cnt.x = W - COUNTER_W;
  cnt.y = 16;

  // 4. caption box — cream plate with a 3px black rule, hugging the text
  const cap = text(f, p.caption, {
    size: CAP_SIZE, fill: C.BLACK, weight: "Bold",
    lineHeight: CAP_LINE, maxWidth: CAP_MAX_TEXT_W,
  });
  cap.name = "caption";
  const boxW = Math.ceil(cap.width) + CAP_PAD * 2;
  const boxH = Math.ceil(cap.height) + CAP_PAD * 2;
  const box = rect(f, CAP_X, CAP_Y, boxW, boxH, C.CREAM, "caption box");
  box.strokes = solid(C.BLACK);
  box.strokeWeight = 3;
  box.strokeAlign = "INSIDE";
  // text must sit above the plate
  f.appendChild(cap);
  cap.x = CAP_X + CAP_PAD;
  cap.y = CAP_Y + CAP_PAD;

  // 5. footer bar
  rect(f, 0, H - FOOTER_H, W, FOOTER_H, C.BLACK, "footer bar");
  const footChars = n < 4
    ? "@POWERCOFFEE.OFC  ·  SWIPE  →"
    : "@POWERCOFFEE.OFC  ·  THEPOWERCOFFEE.COM  ·  NEW EPISODE EVERY WEEK";
  const foot = text(f, footChars, {
    size: 22, fill: C.GOLD, weight: "Semi Bold", align: "CENTER",
  });
  foot.name = "footer";
  foot.textAutoResize = "HEIGHT";
  foot.resize(W, foot.height);
  foot.x = 0;
  foot.y = H - FOOTER_H + 22;

  // 6. the generation prompt, on canvas under the frame (not part of the export)
  const note = figma.createText();
  note.fontName = { family: "Inter", style: "Regular" };
  figma.currentPage.appendChild(note);
  note.characters = `PANEL ${n} PROMPT\n\n${p.prompt}`;
  note.fontSize = 20;
  note.lineHeight = { unit: "PIXELS", value: 28 };
  note.fills = solid({ r: 0.45, g: 0.45, b: 0.45 });
  note.textAutoResize = "HEIGHT";
  note.resize(W, note.height);
  note.x = f.x;
  note.y = H + 60;
  note.name = `panel_${n} prompt`;

  frames.push(f);
}

// tidy: select the four frames and zoom to them
figma.currentPage.selection = frames;
figma.viewport.scrollAndZoomIntoView(frames);

console.log(
  `Built Ep. ${EP} "${TITLE}" — ${frames.length} slides at ${W}×${H}.\n` +
  `Next: set an image fill on each "panel_art" rect, delete the placeholder hint,\n` +
  `then export the frames 1x JPG as carousel_1..4.jpg into the day folder.`
);
