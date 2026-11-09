// ============================================================
// THE POWER COFFEE — LinkedIn article cover
// "I paid a stranger to fact-check my own product"
// Figma Scripter — paste into: Plugins → Scripter → Run
//
// Output: one 1200 × 644 frame (LinkedIn's article cover ratio).
// Export at 2x PNG for a crisp cover on retina.
//
// THE SEAL: pulled live from the repo CDN via figma.createImageAsync, so the
// real registered trademark is used rather than a redrawn approximation. If the
// fetch is blocked, the script falls back to a labelled cream plate — drag
// 07-Project_info/certifications/Illuminate_Labs_Certified_Seal.svg onto it
// (that file is vector, so it scales cleanly).
//
// Article: Sales_motor/articles/Illuminate-Labs-Certification-LinkedIn-Article.md
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

// SHA-pinned so the asset can never change under the design.
const SEAL_URL =
  "https://cdn.jsdelivr.net/gh/lacerdareis-ai/power_coffee_repo@0924894715dc585b9f8182655cc23afac4ea9189/daily_content/_brand_kit/illuminate_labs_certified_seal.png";

const OVERLINE = "THE POWER COFFEE  ·  FOUNDER NOTES";
const HEADLINE = [
  ["I PAID A STRANGER", C.CREAM],
  ["TO FACT-CHECK",     C.GOLD ],
  ["MY OWN PRODUCT",    C.CREAM],
];
const SUBLINE  = "It found three things I'd been getting wrong.";
const FOOTLINE = "ILLUMINATE LABS CERTIFIED  ·  THIRD-PARTY, MEDICALLY REVIEWED";

// ── HELPERS ───────────────────────────────────────────────────
const solid = (c) => [{ type: "SOLID", color: c }];

async function fonts() {
  await figma.loadFontAsync({ family: "Anton", style: "Regular" });
  // Figma's Inter style is "Semi Bold" WITH a space — "SemiBold" throws.
  for (const s of ["Bold", "Regular", "Semi Bold"]) {
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
  t.textAutoResize = "WIDTH_AND_HEIGHT";
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
f.name = "LinkedIn cover — certification article (1200×644)";
figma.currentPage.appendChild(f);
f.resize(W, H);
f.x = ox;
f.y = 0;
f.fills = solid(C.BG);
f.clipsContent = true;

// hairline gold rule down the left edge — quiet brand marker
const rule = figma.createRectangle();
f.appendChild(rule);
rule.resize(6, H);
rule.x = 0; rule.y = 0;
rule.fills = solid(C.GOLD);
rule.name = "edge rule";

// ── seal block, right side, on a cream plate ─────────────────
// Cream plate is required, not decorative: the seal's "il" mark and ILLUMINATE
// LABS wordmark are black and vanish on the espresso background.
const SEAL_H = 372;
const SEAL_W = Math.round(SEAL_H * (1000 / 1500)); // asset is 1000×1500
const PLATE_PAD = 18;
const plateW = SEAL_W + PLATE_PAD * 2;
const plateH = SEAL_H + PLATE_PAD * 2;
const plateX = W - 80 - plateW;
const plateY = Math.round((H - plateH) / 2);

const plate = figma.createRectangle();
f.appendChild(plate);
plate.resize(plateW, plateH);
plate.x = plateX; plate.y = plateY;
plate.fills = solid(C.CREAM);
plate.cornerRadius = 18;
plate.name = "seal plate";

const seal = figma.createRectangle();
f.appendChild(seal);
seal.resize(SEAL_W, SEAL_H);
seal.x = plateX + PLATE_PAD;
seal.y = plateY + PLATE_PAD;
seal.name = "illuminate labs seal";

let sealLoaded = false;
try {
  const image = await figma.createImageAsync(SEAL_URL);
  seal.fills = [{ type: "IMAGE", imageHash: image.hash, scaleMode: "FIT" }];
  sealLoaded = true;
} catch (e) {
  // Network blocked — leave a labelled target to drop the SVG onto.
  seal.fills = solid({ r: 0.86, g: 0.84, b: 0.80 });
  const hint = text(f, "drop\nIlluminate_Labs_Certified_Seal.svg\nhere", {
    font: { family: "Inter", style: "Bold" }, size: 15,
    fill: { r: 0.35, g: 0.33, b: 0.30 }, lineHeight: 22,
    name: "seal placeholder hint",
  });
  hint.textAlignHorizontal = "CENTER";
  hint.textAutoResize = "HEIGHT";
  hint.resize(SEAL_W - 20, hint.height);
  hint.x = seal.x + 10;
  hint.y = seal.y + Math.round(SEAL_H / 2 - hint.height / 2);
}

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
  font: { family: "Inter", style: "Semi Bold" }, size: 13,
  fill: C.CREAM, tracking: 10, name: "footline",
});
foot.x = PAD;
foot.y = H - 74;

figma.currentPage.selection = [f];
figma.viewport.scrollAndZoomIntoView([f]);

console.log(
  `Cover built: ${W}×${H}.  Seal ${sealLoaded ? "loaded from CDN ✓" : "NOT loaded — drop the SVG on the plate"}.\n` +
  `Export the frame at 2x PNG and use it as the LinkedIn article cover.`
);
