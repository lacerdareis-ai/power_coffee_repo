// ============================================================
// THE POWER COFFEE — Welcome Screen · Figma Scripter
// Paste into: Plugins → Scripter → Run
// Creates 2 frames side by side: "GOOD MORNING" + "HELLO THERE"
// Export at 1x as PNG → use as title card / video intro screen
// Format: 1080 × 1920 (9:16 vertical — Reels, TikTok, Stories)
// ============================================================

// ── BRAND TOKENS ─────────────────────────────────────────────
const C = {
  BG:      { r: 0.090, g: 0.078, b: 0.071 }, // #171412 Deep Espresso
  GOLD:    { r: 0.851, g: 0.651, b: 0.200 }, // #D9A633 Golden Energy
  CREAM:   { r: 0.969, g: 0.941, b: 0.878 }, // #F7F0E0 Warm Cream
  BROWN:   { r: 0.180, g: 0.157, b: 0.141 }, // #2E2824 Dark Charcoal
  BROWN_L: { r: 0.294, g: 0.141, b: 0.071 }, // #4B2412 mid brown
  BLACK:   { r: 0,     g: 0,     b: 0     },
};

const W = 1080;
const H = 1920;
const GAP = 80;

// ── FONT LOADER ───────────────────────────────────────────────
async function fonts() {
  for (const s of ["Bold Italic","Bold","Regular","Italic"]) {
    await figma.loadFontAsync({ family: "Georgia", style: s });
  }
  await figma.loadFontAsync({ family: "Arial", style: "Bold" });
  await figma.loadFontAsync({ family: "Arial", style: "Regular" });
}

// ── HELPERS ───────────────────────────────────────────────────
function rect(parent, x, y, w, h, color, opacity) {
  const r = figma.createRectangle();
  r.x = x; r.y = y; r.resize(w, h);
  r.fills = [{ type: "SOLID", color, opacity: opacity ?? 1 }];
  parent.appendChild(r);
  return r;
}

function line(parent, x1, y1, x2, y2, color, weight, opacity) {
  const dx = x2 - x1, dy = y2 - y1;
  const len = Math.sqrt(dx*dx + dy*dy);
  const l = figma.createLine();
  l.x = x1; l.y = y1;
  l.resize(len, 0);
  l.rotation = -Math.atan2(dy, dx) * 180 / Math.PI;
  l.strokes = [{ type: "SOLID", color, opacity: opacity ?? 1 }];
  l.strokeWeight = weight ?? 1;
  parent.appendChild(l);
  return l;
}

async function text(parent, str, x, y, w, size, family, style, color, align, lineH) {
  const t = figma.createText();
  t.fontName = { family, style };
  t.characters = str;
  t.fontSize = size;
  t.fills = [{ type: "SOLID", color }];
  t.textAlignHorizontal = align ?? "LEFT";
  if (lineH) t.lineHeight = { unit: "PERCENT", value: lineH * 100 };
  t.resize(w, t.height);
  t.x = x; t.y = y;
  parent.appendChild(t);
  return t;
}

async function img(parent, url, x, y, w, h) {
  try {
    const hash = await figma.createImageAsync(url);
    const n = figma.createRectangle();
    n.x = x; n.y = y; n.resize(w, h);
    n.fills = [{ type: "IMAGE", imageHash: hash.hash, scaleMode: "FIT" }];
    parent.appendChild(n);
    return n;
  } catch (e) {
    console.log("Image load failed:", e);
    return null;
  }
}

// ── DIAGONAL TEXTURE ──────────────────────────────────────────
function drawTexture(frame, accentColor, opacity) {
  for (let i = 0; i < 18; i++) {
    line(frame, -200 + i * 130, 0, -200 + i * 130 + H * 0.65, H,
         accentColor, 60, opacity ?? 0.03);
  }
}

// ── GOLD ACCENT LINES ─────────────────────────────────────────
function goldAccents(frame) {
  rect(frame, 0, 0, W, 6, C.GOLD);          // top bar
  rect(frame, 0, H - 6, W, 6, C.GOLD);      // bottom bar
  rect(frame, 64, H / 2 - 260, 4, 520, C.GOLD); // left vertical accent
}

// ── CORNER MARKS ──────────────────────────────────────────────
function cornerMarks(frame, color) {
  const s = 40, t = 4, pad = 48;
  // top-left
  rect(frame, pad, pad, s, t, color);
  rect(frame, pad, pad, t, s, color);
  // top-right
  rect(frame, W - pad - s, pad, s, t, color);
  rect(frame, W - pad - t, pad, t, s, color);
  // bottom-left
  rect(frame, pad, H - pad - t, s, t, color);
  rect(frame, pad, H - pad - s, t, s, color);
  // bottom-right
  rect(frame, W - pad - s, H - pad - t, s, t, color);
  rect(frame, W - pad - t, H - pad - s, t, s, color);
}

// ── FOOTER ────────────────────────────────────────────────────
async function footer(frame) {
  rect(frame, 0, H - 160, W, 160, C.BROWN, 0.9);
  rect(frame, 0, H - 162, W, 2, C.GOLD, 0.5);
  await text(frame, "THE POWER COFFEE", W / 2 - 300, H - 118, 600, 22,
             "Arial", "Bold", C.GOLD, "CENTER");
  await text(frame, "CLEAN ENERGY.  REAL FOCUS.", W / 2 - 280, H - 82, 560, 14,
             "Arial", "Regular", { r: 0.6, g: 0.55, b: 0.45 }, "CENTER");
}

// ── BUILD ONE SCREEN ──────────────────────────────────────────
async function buildScreen(greeting, sub, offsetX) {
  const frame = figma.createFrame();
  frame.name = `Welcome — ${greeting}`;
  frame.x = offsetX; frame.y = 0;
  frame.resize(W, H);
  frame.fills = [{ type: "SOLID", color: C.BG }];
  frame.clipsContent = true;

  // background texture
  drawTexture(frame, C.GOLD, 0.025);

  // subtle radial glow behind mascot (warm circle)
  const glow = figma.createEllipse();
  glow.x = W / 2 - 340; glow.y = H / 2 - 560;
  glow.resize(680, 680);
  glow.fills = [{ type: "SOLID", color: { r: 0.53, g: 0.25, b: 0.04 }, opacity: 0.18 }];
  frame.appendChild(glow);

  // gold accent lines + corner marks
  goldAccents(frame);
  cornerMarks(frame, { r: 0.85, g: 0.65, b: 0.20, opacity: 0.3 });

  // mascot — centered upper third
  const MASCOT_URL = "https://www.figma.com/api/mcp/asset/e247e676-68e2-4852-8229-eaebc37366db";
  await img(frame, MASCOT_URL, W / 2 - 260, 160, 520, 520);

  // thin gold divider
  rect(frame, 120, 740, W - 240, 2, C.GOLD, 0.5);

  // small overline
  await text(frame, "WELCOME  TO  YOUR  MORNING", 64, 770, W - 128, 12,
             "Arial", "Bold", C.GOLD, "CENTER", 1.6);

  // main greeting — big, italic, stacked
  const lines = greeting.split(" ");
  let ty = 820;
  for (const word of lines) {
    const t = figma.createText();
    t.fontName = { family: "Georgia", style: "Bold Italic" };
    t.characters = word;
    t.fontSize = word.length > 6 ? 148 : 168;
    t.fills = [{ type: "SOLID", color: C.CREAM }];
    t.textAlignHorizontal = "CENTER";
    t.lineHeight = { unit: "PERCENT", value: 88 };
    t.resize(W - 80, t.height);
    t.x = 40; t.y = ty;
    frame.appendChild(t);
    ty += t.height - 16;
  }

  // gold underline
  rect(frame, 120, ty + 24, W - 240, 3, C.GOLD);

  // sub-line
  await text(frame, sub, 64, ty + 50, W - 128, 28,
             "Georgia", "Italic", { r: 0.75, g: 0.65, b: 0.50 }, "CENTER", 1.5);

  // second accent — vertical right edge dot
  rect(frame, W - 68, H / 2 - 120, 4, 240, C.GOLD, 0.4);

  // footer
  await footer(frame);

  figma.currentPage.appendChild(frame);
  return frame;
}

// ── MAIN ─────────────────────────────────────────────────────
await fonts();

const screens = [
  { greeting: "GOOD\nMORNING", sub: "Let's win today.",       offset: 0 },
  { greeting: "HELLO\nTHERE",  sub: "Ready to fuel up?",      offset: W + GAP },
];

const frames = [];
for (const s of screens) {
  const f = await buildScreen(s.greeting, s.sub, s.offset);
  frames.push(f);
}

figma.viewport.scrollAndZoomIntoView(frames);
figma.notify("✅ Welcome screens created — export each at 1× PNG", { timeout: 5000 });
