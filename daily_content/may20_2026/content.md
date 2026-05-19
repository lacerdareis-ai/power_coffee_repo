# Power Coffee — Content for May 20, 2026
**Pillar:** P3 — Founder Proof | **Day:** Wednesday | **Image set:** E2

---
## APPROVAL
- [x] APPROVED

> Auto-approved. To reject: change [x] to [ ] before 4am.

---

---

## INSTAGRAM
### Reel Script

**HOOK (0–3s):**
"I can't buy back a wasted morning."

**BODY (3–38s):**
Ironman prep means two hours before the day starts. Then the workday. Then Gabriel and Helena need a dad who's present — not running on cortisol fumes.

The window between your last interval and your first meeting is where most mornings fall apart. I built Power Coffee because mine kept falling apart.

Clean caffeine, matcha for a six-hour arc, taurine to support the full morning — not just the first forty minutes.

Still drinking it. Still the same formula.

**CTA (38–45s):**
"Link in bio. You'll know by day three."

**On-screen text:** "I can't buy back a wasted morning." → "5am training. 9am workday. 7am family." → "The gap between them is where the day is won or lost." → "I built something for that gap." → "Still the same formula. Link in bio."

---

## X.COM
### Post
I train at 5am, run a company by 9, and have two kids awake by 7. If my morning formula doesn't cover all three, something breaks. That's why I built Power Coffee.

### Thread
Post 1: The hardest part of Ironman training isn't the miles. It's the 90 minutes after the session when you have to switch from athlete to founder. That transition was costing me every morning — until I fixed the formula.

Post 2: Here's the physiology: a hard training session temporarily suppresses cortical function. You're asking your CNS to focus while it's still recovering. Standard caffeine spikes fast and drops. What bridges the gap is matcha — EGCG and L-theanine that extend the energy arc to 4–6 hours — paired with taurine to support neuromuscular recovery and output at the same time.

Post 3: Research on taurine and post-exercise recovery shows it may reduce oxidative stress markers and support mitochondrial function after hard efforts. Pairing it with caffeine and matcha doesn't just give you energy — it gives you functional energy. The kind that holds when your CNS is still rebuilding from a hard interval session.

Post 4: I built five versions of this formula before I found one that handled both sides of my morning. Francy still calls it my science project. But 5am training, 9am calls, present parenting by 7 — I needed something that could carry all of it. That formula is Power Coffee.

Post 5: If your mornings are doing two or three jobs at once, Power Coffee was built for exactly that. One scoop. 11 ingredients. The whole arc. thepowercoffee.com

---

## LINKEDIN
### Post

I used to treat my morning as two separate things.

The training block. Then the workday.

And somewhere between those two, I was supposed to be present for Gabriel and Helena before school.

It didn't work. The training half and the work half were competing for the same resource — my capacity — and the transitions between them were costing me more than the hours themselves.

What I figured out, after two years of iteration, is that the bridge between those demands matters more than any individual part of the routine.

Your energy isn't just a fuel tank. It's a transition system. If it doesn't carry you cleanly from one context to the next, you'll spend the first hour of every new thing just trying to catch up.

Power Coffee started as the formula I built so my training mornings didn't wreck my work mornings. One scoop into whatever I was already drinking. Matcha for a sustained arc. Taurine to support the recovery-to-output handoff. Clean caffeine without borrowing from the afternoon.

I still drink it every morning. It's the only part of my day I haven't second-guessed.

What's the ritual that holds your transitions together?

Leo, Founder — The Power Coffee

---

## TELEGRAM
### Message

If you train in the morning and then have to work a full day, you know what I mean when I say the gap between the two is where everything holds or falls apart. Ironman prep means two hours before anyone's awake — and that's fine, until 9am hits and I need to be sharp. Power Coffee is what I built for that gap. One scoop. Still drinking it every morning. thepowercoffee.com

---

## EMAIL
### Subject Line
The 90 minutes that built this brand

### Preview Text
5am training. 9am calls. 7am kids. One formula for all of it.

### Body

Hey,

Here's the honest version of why I started Power Coffee.

I'm in Ironman prep. My days start before 5am — two hours of training before Gabriel and Helena are awake, before Francy's alarm goes off, before any of the day's demands are visible.

That part I love. It's mine.

The hard part is what comes after.

By 7, the kids are up. By 9, I'm in calls. By noon, I need to have done real, focused work — not just survived the morning on willpower and a second cup.

For a long time I was losing the transition. The training session would end and I'd come inside already anticipating the crash. Caffeine that peaked fast and dropped faster. No protein to hold blood sugar steady. No extended-release mechanism to carry me through.

The formula I built was designed to close that gap. Matcha for a four-to-six-hour energy arc. Taurine to support the recovery-to-output handoff. Clean caffeine that doesn't leave you borrowing from the afternoon.

One scoop. The same cup you're already drinking. The whole morning, covered.

If your schedule looks anything like mine — this was made for it.

[Try Power Coffee — thepowercoffee.com](https://www.thepowercoffee.com)

— Leo

---

## HIGGSFIELD (Video Reel)
### Model
cinematic_studio_3_0

### Aspect Ratio
9:16

### Resolution
1080p

### Duration
15

### Prompt
A man in his mid-30s wearing a lightweight cycling kit enters a clean, quiet kitchen from a side door as dawn light begins to fill the room. He sets a cycling helmet on the counter without looking at it — the movement is automatic, familiar. His expression is calm and purposeful, not exhausted. He reaches for a matte black canister on the counter and adds a measured scoop of dark powder into a ceramic mug already waiting beside it. Slow, steady push-in toward his face as he waits for the kettle. At 8 seconds, he wraps both hands around the mug and his posture shifts almost imperceptibly: shoulders settle back, jaw unclenches, gaze steadies toward the window. A soft, implied sound from the hallway — he glances toward it with a slight smile. Warm amber morning light, cream and espresso brown palette, slate blue traces of pre-dawn still visible. No text in frame. Cinematic grain, handheld-steady camera. Natural window light only — no studio fill. Photorealistic.

---

## FIGMA SCRIPTER
```javascript
// Power Coffee - POST - Figma Scripter
// Paste into: Plugins > Scripter > Run
// Reel format — generate video in Higgsfield (no Figma slides needed)

// BRAND COLORS - use quoted string keys in SLIDES data
const COLORS = {
  BLACK:   { r: 0.07, g: 0.06, b: 0.05 },
  BROWN:   { r: 0.48, g: 0.24, b: 0.12 },
  BROWN_L: { r: 0.75, g: 0.48, b: 0.28 },
  CREAM:   { r: 0.94, g: 0.91, b: 0.84 },
  WHITE:   { r: 1,    g: 1,    b: 1    },
  DARK_BG: { r: 0.10, g: 0.09, b: 0.08 },
};
function col(name) { return COLORS[name] || name; }

const W = 1080;
const H = 1920;
const GAP = 60;

// SLIDE DATA - accent/bg/textColor must be quoted strings: "BLACK", "BROWN", "BROWN_L", "CREAM", "WHITE"
const SLIDES = [  // Reel format — no Figma slides. Generate video in Higgsfield instead.
];

// ── HELPERS ──────────────────────────────────────────────────
function addRect(parent, x, y, w, h, color, opacity) {
  if (opacity === undefined) { opacity = 1; }
  var r = figma.createRectangle();
  r.x = x; r.y = y; r.resize(w, h);
  r.fills = [{ type: "SOLID", color: col(color), opacity: opacity }];
  parent.appendChild(r);
  return r;
}

async function addText(parent, txt, x, y, w, size, weight, color, align, lineH) {
  if (align === undefined) { align = "LEFT"; }
  if (lineH === undefined) { lineH = 1.05; }
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

async function buildSlide(data, offsetX) {
  var frame = figma.createFrame();
  frame.name = "Slide " + data.id + " - " + data.slideType;
  frame.resize(W, H);
  frame.x = offsetX; frame.y = 0;
  frame.fills = [{ type: "SOLID", color: col(data.bg) }];
  frame.clipsContent = true;

  for (var i = 0; i < 12; i++) {
    var line = figma.createLine();
    line.x = -100 + i * 110; line.y = 0;
    line.resize(H * 1.5, 0);
    line.rotation = -55;
    line.strokes = [{ type: "SOLID", color: col(data.accent), opacity: 0.04 }];
    line.strokeWeight = 40;
    frame.appendChild(line);
  }

  await addText(frame, "0" + data.id, 64, 60, 120, 13, "Bold", "WHITE");
  addRect(frame, 64, 85, 20, 2, data.accent);

  if (data.overline) {
    await addText(frame, data.overline, 64, 96, W - 128, 12, "Bold", "BROWN_L", "LEFT", 1.4);
  }

  if (data.pivotBar) { addRect(frame, 64, 148, 6, 260, data.accent); }

  var hX; if (data.pivotBar) { hX = 90; } else { hX = 64; }
  var hlColor; if (data.isCTA) { hlColor = "WHITE"; } else { hlColor = data.textColor; }
  await addText(frame, data.headline, hX, 148, W - hX - 40, 128, "Black Italic", hlColor, "LEFT", 0.92);

  var divY; if (data.isCTA) { divY = 740; } else { divY = 730; }
  addRect(frame, 64, divY, W - 128, 2, data.accent, 0.6);

  if (data.pills) {
    var pillX = 64;
    for (var j = 0; j < data.pills.length; j++) {
      var pill = data.pills[j];
      await figma.loadFontAsync({ family: "Inter", style: "Bold" });
      var pf = figma.createFrame();
      pf.resize(160, 36); pf.x = pillX; pf.y = divY + 20;
      pf.fills = [{ type: "SOLID", color: col("BROWN"), opacity: 0.25 }];
      pf.cornerRadius = 0;
      frame.appendChild(pf);
      var pt = figma.createText();
      pt.fontName = { family: "Inter", style: "Bold" };
      pt.characters = pill; pt.fontSize = 10;
      pt.textAlignHorizontal = "CENTER";
      pt.fills = [{ type: "SOLID", color: col("CREAM") }];
      pt.letterSpacing = { unit: "PERCENT", value: 20 };
      pt.resize(160, 36); pt.x = 0; pt.y = 12;
      pf.appendChild(pt);
      pillX += 172;
    }
  }

  if (data.subtext) {
    var subY; if (data.pills) { subY = divY + 70; } else { subY = divY + 24; }
    await addText(frame, data.subtext, 64, subY, W - 128, 22, "Regular", { r: 0.85, g: 0.80, b: 0.72 }, "LEFT", 1.6);
  }

  addRect(frame, 64, H - 96, W - 128, 1, "BROWN_L", 0.3);
  await addText(frame, "THE POWER COFFEE", 64, H - 78, 400, 11, "Bold", "BROWN_L", "LEFT", 1.4);
  await addText(frame, "CLEAN ENERGY. REAL FOCUS.", W - 380, H - 78, 316, 10, "Regular", { r: 0.6, g: 0.55, b: 0.48 }, "RIGHT", 1.4);

  if (data.isCTA) {
    addRect(frame, 0, H - 180, W, 180, "BROWN");
    await addText(frame, "POWER COFFEE", 64, H - 138, W - 128, 14, "Black", "WHITE", "LEFT", 1.2);
    await addText(frame, "thepowercoffee.com", 64, H - 110, W - 128, 13, "Regular", { r: 1, g: 0.95, b: 0.88 }, "LEFT", 1.4);
    await addText(frame, "@POWERCOFFEE.OFC", 64, H - 76, W - 128, 12, "Bold", "WHITE", "LEFT", 1.4);
  }

  figma.currentPage.appendChild(frame);
  return frame;
}

async function main() {
  var frames = [];
  for (var i = 0; i < SLIDES.length; i++) {
    var frame = await buildSlide(SLIDES[i], i * (W + GAP));
    frames.push(frame);
  }
  figma.viewport.scrollAndZoomIntoView(frames);
  figma.notify("Power Coffee - slides created!", { timeout: 4000 });
}

main();
```

> **Instructions:** Reel day — no Figma slides needed. Generate the video in Higgsfield using the prompt above. Save output as `instagram.mp4` in today's folder.
