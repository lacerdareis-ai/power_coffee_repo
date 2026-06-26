// HIGH ENERGY OS — Welcome Dashboard
// Figma Scripter · Plugins > Scripter > Run
// File: Power Coffee — Father's Day Stories (jUxqC3CPqDmot8v4LwAHFZ)
//   OR paste into any new Figma file
// Output: 1440 × 900 desktop dashboard frame
// Fonts required: Lora (Bold Italic, Bold, Regular) + Inter (Bold, Regular)

const BG     = { r: 0.07, g: 0.06, b: 0.05 };
const PANEL  = { r: 0.12, g: 0.10, b: 0.09 };
const CARD   = { r: 0.16, g: 0.14, b: 0.12 };
const GOLD   = { r: 0.85, g: 0.65, b: 0.20 };
const CREAM  = { r: 0.97, g: 0.94, b: 0.88 };
const BROWN  = { r: 0.48, g: 0.24, b: 0.12 };
const BROWN_L= { r: 0.75, g: 0.48, b: 0.28 };
const DIM    = { r: 0.40, g: 0.36, b: 0.30 };
const GREEN  = { r: 0.20, g: 0.72, b: 0.40 };
const W = 1440; const H = 900;

async function loadFonts() {
  const fonts = [
    { family:"Lora", style:"Bold Italic" },
    { family:"Lora", style:"Bold" },
    { family:"Lora", style:"Regular" },
    { family:"Inter", style:"Bold" },
    { family:"Inter", style:"Regular" },
  ];
  for (const f of fonts) {
    try { await figma.loadFontAsync(f); } catch(e) {}
  }
}

function R(parent, x, y, w, h, fill, opacity, radius) {
  const r = figma.createRectangle();
  r.x = x; r.y = y; r.resize(w, h);
  r.fills = [{ type:"SOLID", color:fill, opacity:opacity??1 }];
  if (radius) r.cornerRadius = radius;
  parent.appendChild(r); return r;
}
function E(parent, x, y, w, h, fill, opacity) {
  const e = figma.createEllipse();
  e.x = x; e.y = y; e.resize(w, h);
  e.fills = [{ type:"SOLID", color:fill, opacity:opacity??1 }];
  parent.appendChild(e); return e;
}
async function T(parent, str, x, y, w, size, family, style, color, align, lh, ls) {
  const fn = { family, style };
  try { await figma.loadFontAsync(fn); } catch(e) {
    fn.family = "Inter"; fn.style = style.includes("Bold") ? "Bold" : "Regular";
    await figma.loadFontAsync(fn).catch(()=>{ fn.style="Regular"; });
  }
  const t = figma.createText();
  t.fontName = fn; t.characters = str; t.fontSize = size;
  t.textAlignHorizontal = align||"LEFT";
  t.fills = [{ type:"SOLID", color }];
  if (lh) t.lineHeight = { unit:"PERCENT", value: lh*100 };
  if (ls) t.letterSpacing = { unit:"PERCENT", value: ls };
  t.x = x; t.y = y; t.resize(w, t.height);
  parent.appendChild(t); return t;
}

await loadFonts();
figma.currentPage.name = "HE-OS — Welcome Dashboard";

const root = figma.createFrame();
root.name = "HIGH ENERGY OS — Welcome";
root.resize(W, H); root.x = 0; root.y = 0;
root.fills = [{ type:"SOLID", color:BG }];
root.clipsContent = true;
figma.currentPage.appendChild(root);

// Background glow + diagonal texture
E(root, W/2 - 400, H/2 - 400, 800, 800, GOLD, 0.04);
E(root, W/2 - 220, H/2 - 220, 440, 440, GOLD, 0.05);
for (let i = 0; i < 14; i++) {
  const l = figma.createLine();
  l.x = -100 + i * 130; l.y = 0;
  l.resize(H * 1.6, 0); l.rotation = -55;
  l.strokes = [{ type:"SOLID", color:GOLD, opacity:0.025 }];
  l.strokeWeight = 40; root.appendChild(l);
}

// ── TOP BAR ──────────────────────────────────────────────────
const topBar = figma.createFrame();
topBar.name = "Top Bar"; topBar.resize(W, 56);
topBar.x = 0; topBar.y = 0;
topBar.fills = [{ type:"SOLID", color:PANEL }];
root.appendChild(topBar);
R(topBar, 0, 55, W, 1, GOLD, 0.4);
E(topBar, 20, 18, 20, 20, GOLD);
E(topBar, 26, 24, 8, 8, BG);
await T(topBar, "HIGH ENERGY OS", 52, 17, 280, 15, "Inter", "Bold", GOLD, "LEFT", 1.0, 14);
await T(topBar, "v 1.0", 240, 20, 60, 10, "Inter", "Regular", DIM, "LEFT");
await T(topBar, "●  SYSTEM ONLINE", W - 340, 20, 200, 11, "Inter", "Bold", GREEN, "LEFT");
await T(topBar, "JUN 15, 2026  ·  4:45 AM", W - 230, 20, 210, 11, "Inter", "Regular", DIM, "LEFT");

// ── LEFT SIDEBAR ─────────────────────────────────────────────
const sb = figma.createFrame();
sb.name = "Sidebar"; sb.resize(200, H - 56);
sb.x = 0; sb.y = 56;
sb.fills = [{ type:"SOLID", color:PANEL }];
root.appendChild(sb);
R(sb, 199, 0, 1, H-56, GOLD, 0.3);
await T(sb, "MODULES", 24, 32, 152, 9, "Inter", "Bold", DIM, "LEFT", 1.0, 18);
R(sb, 24, 50, 152, 1, GOLD, 0.2);
const nav = ["BRAIN","LENS","PULSE","STUDIO","ADS"];
const navSub = ["Content Engine","Results Analysis","Audience Intel","Visual Generator","Meta Campaigns"];
for (let i = 0; i < nav.length; i++) {
  const ny = 68 + i * 72;
  R(sb, 16, ny, 168, 56, CARD, 1, 4);
  await T(sb, nav[i], 36, ny + 11, 140, 13, "Inter", "Bold", CREAM, "LEFT");
  await T(sb, navSub[i], 36, ny + 31, 140, 9, "Inter", "Regular", DIM, "LEFT");
}
R(sb, 16, H-56-82, 168, 1, GOLD, 0.2);
await T(sb, "LEO LACERDA", 24, H-56-68, 152, 10, "Inter", "Bold", GOLD, "LEFT", 1.0, 10);
await T(sb, "Founder · The Power Coffee", 24, H-56-50, 152, 9, "Inter", "Regular", DIM, "LEFT");

// ── COFFEE MUG HERO ──────────────────────────────────────────
const MX = 200; const MY = 56;
const mugCX = MX + 240; const mugCY = MY + 80;
const cupW = 240; const cupH = 220;

await T(root, "GOOD MORNING, LEO", MX + 40, MY + 24, 400, 10, "Inter", "Bold", DIM, "LEFT", 1.0, 16);
R(root, MX + 40, MY + 42, 360, 1, GOLD, 0.2);

E(root, mugCX - 60, mugCY + 140, 360, 280, GOLD, 0.05);
E(root, mugCX - 20, mugCY + 318, 280, 28, BROWN, 0.35);
R(root, mugCX - 16, mugCY + 318, 272, 14, BROWN_L, 0.5, 7);

const cup = figma.createRectangle();
cup.x = mugCX; cup.y = mugCY + 100; cup.resize(cupW, cupH);
cup.fills = [{ type:"SOLID", color:BROWN }];
cup.topLeftRadius = 6; cup.topRightRadius = 6;
cup.bottomLeftRadius = 20; cup.bottomRightRadius = 20;
root.appendChild(cup);

R(root, mugCX - 10, mugCY + 92, cupW + 20, 22, BROWN_L, 0.85, 5);
E(root, mugCX + 10, mugCY + 108, cupW - 20, 24, { r:0.88, g:0.70, b:0.45 }, 0.9);
R(root, mugCX + 10, mugCY + 126, cupW - 20, cupH - 36, { r:0.28, g:0.13, b:0.06 }, 0.45, 6);

// Steam
for (let s = 0; s < 3; s++) {
  const sx = mugCX + 60 + s * 60;
  for (let seg = 0; seg < 4; seg++) {
    R(root, sx + (seg%2===0 ? -3:3), mugCY + 54 - seg*22, 4, 16, CREAM, 0.12 - seg*0.025, 3);
  }
}

await T(root, "THE POWER\nCOFFEE", mugCX + 24, mugCY + 176, cupW - 48, 17, "Lora", "Bold Italic", { r:0.90, g:0.75, b:0.50 }, "CENTER", 1.25);
await T(root, "⚡", mugCX + 106, mugCY + 238, 30, 18, "Inter", "Regular", GOLD, "CENTER");

const handle = figma.createEllipse();
handle.x = mugCX + cupW - 6; handle.y = mugCY + 130;
handle.resize(66, 100);
handle.fills = [{ type:"SOLID", color:BG, opacity:0 }];
handle.strokes = [{ type:"SOLID", color:BROWN_L }];
handle.strokeWeight = 16;
root.appendChild(handle);
R(root, mugCX + cupW - 8, mugCY + 126, 22, 108, BROWN);

await T(root, "POWER COFFEE", mugCX + 10, mugCY + 348, cupW - 20, 9, "Inter", "Bold", GOLD, "CENTER", 1.0, 14);
await T(root, "CLEAN ENERGY · REAL FOCUS", mugCX + 10, mugCY + 364, cupW - 20, 8, "Inter", "Regular", DIM, "CENTER", 1.0, 6);

// ── HEADLINE ─────────────────────────────────────────────────
const hX = MX + 530; const hY = MY + 80;
await T(root, "YOUR MORNING\nCOMMAND\nCENTER.", hX, hY, 360, 38, "Lora", "Bold Italic", CREAM, "LEFT", 0.92);
R(root, hX, hY + 148, 280, 2, GOLD, 0.7);
await T(root, "Energy. Focus. Momentum.\n550 mornings. No days missed.", hX, hY + 162, 340, 14, "Lora", "Regular", { r:0.75, g:0.68, b:0.58 }, "LEFT", 1.5);

// ── METRIC CARDS ─────────────────────────────────────────────
const cardStartX = MX + 520; const cardStartY = MY + 280;
const cardW = 210; const cardH = 108; const gap = 16;
const cards = [
  { t:"MORNING STREAK", v:"550", u:"DAYS",      bar:1.0,  c:GOLD,  s:"No days missed" },
  { t:"ENERGY STATUS",  v:"OPTIMAL", u:"",       bar:0.88, c:GREEN, s:"Peak: 6–11am" },
  { t:"INGREDIENTS",    v:"7",   u:"ACTIVE",     bar:1.0,  c:GOLD,  s:"All compounds loaded" },
  { t:"CRASH RISK",     v:"0%",  u:"",           bar:0.0,  c:GREEN, s:"Taurine buffer on" },
  { t:"FOCUS LEVEL",    v:"HIGH", u:"",          bar:0.82, c:GOLD,  s:"L-theanine engaged" },
  { t:"NEXT DOSE",      v:"TOMORROW",u:"6:45 AM",bar:0,    c:DIM,   s:"Auto-scheduled" },
];
for (let ci = 0; ci < cards.length; ci++) {
  const cd = cards[ci];
  const col = ci % 2; const row = Math.floor(ci / 2);
  const cx = cardStartX + col * (cardW + gap);
  const cy = cardStartY + row * (cardH + gap);
  R(root, cx, cy, cardW, cardH, CARD, 1, 8);
  R(root, cx, cy, 4, cardH, cd.c, cd.c===DIM ? 0.3 : 0.85, 2);
  await T(root, cd.t, cx+16, cy+14, cardW-32, 8, "Inter", "Bold", DIM, "LEFT", 1.0, 14);
  const isLong = cd.v.length > 5;
  await T(root, cd.v, cx+16, cy+30, cardW-32, isLong ? 20 : 28, "Lora", "Bold Italic", cd.c===DIM ? DIM : CREAM, "LEFT");
  if (cd.u) await T(root, cd.u, cx+16, cy+64, cardW-32, 8, "Inter", "Bold", cd.c, "LEFT", 1.0, 10);
  if (cd.bar > 0) {
    R(root, cx+16, cy+80, cardW-32, 4, { r:0.20, g:0.17, b:0.14 }, 1, 2);
    R(root, cx+16, cy+80, Math.max(4,(cardW-32)*cd.bar), 4, cd.c, 0.85, 2);
  }
  await T(root, cd.s, cx+16, cy+92, cardW-32, 8, "Inter", "Regular", DIM, "LEFT");
}

// ── BOTTOM LOG ───────────────────────────────────────────────
const logY = H - 130;
R(root, MX + 40, logY, W - MX - 60, 1, GOLD, 0.2);
await T(root, "SYSTEM LOG", MX + 40, logY + 10, 160, 8, "Inter", "Bold", DIM, "LEFT", 1.0, 16);
const log = [
  "04:00  Pipeline fired — X, Telegram, WhatsApp, LinkedIn published                                      OK",
  "04:02  Instagram Reel scheduled — instagram.mp4 detected                                                OK",
  "04:05  CTA Story rotated — story.jpg active                                                             OK",
  "04:10  Brain references synced — content-system.md updated                                              OK",
];
for (let li = 0; li < log.length; li++) {
  await T(root, log[li], MX + 40, logY + 28 + li * 18, W - MX - 80, 9, "Inter", "Regular", DIM, "LEFT");
}

// ── STATUS BAR ───────────────────────────────────────────────
R(root, 0, H - 30, W, 30, PANEL);
R(root, 0, H - 30, W, 1, GOLD, 0.3);
await T(root, "●  ALL SYSTEMS NOMINAL", 24, H - 19, 240, 10, "Inter", "Bold", GREEN, "LEFT");
await T(root, "POWERED BY THE POWER COFFEE  ·  CLEAN ENERGY. REAL FOCUS.", W/2-240, H-19, 480, 10, "Inter", "Regular", DIM, "CENTER");
await T(root, "thepowercoffee.com", W - 196, H - 19, 180, 10, "Inter", "Regular", GOLD, "LEFT");

figma.viewport.scrollAndZoomIntoView([root]);
figma.notify("✅  HE-OS Welcome Dashboard ready!", { timeout: 4000 });
