# Power Coffee — Content for October 29, 2026
**Pillar:** P5 — SOCIAL PROOF | **Day:** Thursday | **Image set:** D1 or D3

---
## APPROVAL
- [ ] APPROVED

---

---

## INSTAGRAM
### Story Copy
**HEADLINE:**
REAL PEOPLE. REAL RESULTS.

**Subtext:** Someone just told us this changed their entire afternoon.

**Sticker:** Poll — "Do you crash after noon?" / YES, ALWAYS vs. NOT ANYMORE

---

### Caption
Someone reached out last week.

She said she stopped reaching for a third cup by noon.

Said the afternoon just held.

That is the whole point.

Every scoop is designed to help you keep the energy you started with — not chase it for the rest of the day.

If you have felt that shift, we want to hear it.

Drop your experience below or send it to us directly.

https://thepowercoffee.com/pages/betterday

---

### Hashtags
#cleanenergy #functionalcoffee #nooncrash #morningroutine #powercoffee #thefirstwin #biohacking #energyboost #focusfuel #sustainableenergy #nocrash #coffeeroutine

---

## X.COM
### Post
You said the 2pm wall just stopped showing up. That is the whole brief. Sharing it because more people need to hear it is possible.

---

### Thread
Post 1: The 2pm wall is not a personal failure. Three people messaged us this week saying the same thing — and then telling us it went away.

Post 2: One of them had been running on three cups of coffee and a handful of vitamins every day. Still losing the afternoon by 1:30.

Post 3: The issue is not the amount of caffeine. It is what happens after the caffeine spikes and clears. Without the right support, your brain has no bridge to stable energy on the other side.

Post 4: That bridge is what Power Coffee is built around. Taurine to help sustain the curve. Ginkgo to keep blood moving to where focus happens. Thermogenic spices to keep the engine warm. No spike. No cliff.

Post 5: If your afternoon is still falling apart, start here: https://thepowercoffee.com/pages/betterday

---

## LINKEDIN
### Post
Someone sent me a message last Tuesday.

She said she had not felt the 2pm drag in three weeks.

I read it twice.

Not because it was the biggest review we have ever gotten. Because it was specific. She did not say "I have more energy." She said the afternoon just held together in a way it had not before.

That specificity is the signal I have been chasing since we started this.

I built Power Coffee because I was losing my own afternoons. Work was fine in the morning. By early afternoon, something had shifted. Not dramatic. Just slower. Less decisive. The kind of tired that does not respond to another cup.

We formulated around that exact problem.

When a stranger describes the solution back to you without knowing the brief — that is the confirmation that means the most.

It is not the sale. It is the recognition.

Has a customer ever described your product back to you in a way that stopped you cold?

---

## TELEGRAM
### Message
Got a message this week from someone who said the 2pm crash just stopped happening for her.

Three weeks in. She did not change anything else in her routine.

That is why we built this thing. Sharing it here because if you are still on the fence, that is probably the most honest thing I can say right now.

https://thepowercoffee.com/pages/betterday

---

## REELS — Founder Vlog Script
**Series:** Building Power Coffee — Ep. 13
**Beat:** Social proof as business signal — when a real review tells you the formula is working
**Title formula:** When a stranger describes your product better than you do | Afternoon energy week
**Duration:** 30-45s · **Setting:** Leo at his desk, morning, the Power Coffee pouch visible but off to the side, slightly out of focus — casual, not staged

**HOOK (0-3s, text on screen + spoken):**
"She described our product back to me without knowing the brief."

**BODY (speak exactly this):**
"I got a message Tuesday. She said she had not felt the 2pm drag in three weeks. Three weeks. I had to read it twice — not because it was some huge number or a big account. Because she was specific. She did not say 'more energy.' She said the afternoon held together in a way it had not before. That is the exact sentence I had in my head when we were formulating this. Word for word. When a stranger finds the same words you wrote in a product brief eighteen months ago — that tells you something is working. Not the marketing. The actual product. That is the only metric I trust right now."

**CTA (last 5s):**
"If you are building something, follow the build. Drop a question below — I read all of them."

**B-ROLL:** Leo reading phone at desk with a quiet expression, close-up of hands wrapping around a mug with the pouch visible behind, Leo looking out a window briefly before turning back to camera

**CAPTION:**
When a stranger finds the same words you wrote in a product brief — that is the confirmation that matters most.

Not the sale. The recognition.

Ep. 13 — Building Power Coffee

#buildingpowercoffee #founderstory #cleanenergy #functionalcoffee #powercoffee

**ON-SCREEN TEXT:**
0:00 — "she described it better than I could"
0:15 — "the afternoon just held together"
0:35 — "that's the only metric I trust"

---

## SCIENCE NOTE — Founder Interview Prep (not for publishing)
**Ingredient / mechanism:** Ginkgo Biloba Extract — flavonoid glycosides and microvascular regulation

Ginkgo biloba extract standardized to 24% flavonoid glycosides and 6% terpene lactones (ginkgolides A, B, C and bilobalide) exerts its primary cognitive effect through inhibition of platelet-activating factor (PAF) and modulation of nitric oxide signaling in cerebrovascular endothelium. The ginkgolides are competitive antagonists at the PAF receptor, reducing platelet aggregation and vasoconstriction in small cerebral vessels. Bilobalide has demonstrated neuroprotective properties via inhibition of GABA-A receptor chloride channels and mitochondrial protection against ischemic stress. The net effect on cerebral microcirculation is improved regional blood flow to prefrontal and hippocampal areas — the structures most associated with working memory and sustained attention. Power Coffee contains 207mg of ginkgo biloba extract per serving, consistent with the dose range studied in cognitive performance research.

**Reference:** Oken BS, Storzbach DM, Kaye JA. The efficacy of Ginkgo biloba on cognitive function in Alzheimer disease. Archives of Neurology, 1998; 55(11):1409-1415. [VERIFY CITATION for exact dose-response range in healthy adults]

**Interview angle:** Ginkgo in this formula is not about memory as a headline claim — it supports the microvascular conditions that allow the brain to stay supplied and responsive during cognitively demanding work, which is meaningfully different from a stimulant effect.

---

## FIGMA SCRIPTER
```javascript
// Power Coffee - POST - Figma Scripter
// Paste into: Plugins > Scripter > Run
// Creates 1 frame (1080x1920 px) — Story format

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
const SLIDES = [{ id: 1, slideType: "hook", bg: "BLACK", accent: "BROWN", textColor: "CREAM", overline: "REAL RESULTS", headline: "REAL PEOPLE.\nREAL RESULTS.", subtext: "Someone just told us this changed their entire afternoon.", poll: { question: "Do you crash after noon?", optionA: "YES, ALWAYS", optionB: "NOT ANYMORE" } }
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

// Font map — matches make_carousel.py (Pillow) rendering
// Headlines/body → Georgia | Labels/pills/footer → Arial
function _fontFor(weight) {
  if (weight === "Black Italic" || weight === "Bold Italic") { return { family: "Georgia", style: "Bold Italic" }; }
  if (weight === "Black" || weight === "Bold" && false)      { return { family: "Georgia", style: "Bold" }; }
  if (weight === "Italic" || weight === "Regular Italic")    { return { family: "Georgia", style: "Italic" }; }
  // Labels, overlines, pills, footer, counter use Arial
  if (weight === "Bold")    { return { family: "Arial", style: "Bold" }; }
  if (weight === "Regular") { return { family: "Georgia", style: "Regular" }; }
  return { family: "Arial", style: weight };
}

async function addText(parent, txt, x, y, w, size, weight, color, align, lineH) {
  if (align === undefined) { align = "LEFT"; }
  if (lineH === undefined) { lineH = 1.05; }
  var fn = _fontFor(weight);
  await figma.loadFontAsync(fn);
  var t = figma.createText();
  t.fontName = fn;
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
      await figma.loadFontAsync({ family: "Arial", style: "Bold" });
      var pf = figma.createFrame();
      pf.resize(160, 36); pf.x = pillX; pf.y = divY + 20;
      pf.fills = [{ type: "SOLID", color: col("BROWN"), opacity: 0.25 }];
      pf.cornerRadius = 0;
      frame.appendChild(pf);
      var pt = figma.createText();
      pt.fontName = { family: "Arial", style: "Bold" };
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

> **Instructions:** Paste into Figma → Plugins → Scripter → Run. Export each frame at 1x as PNG → save as `story.jpg` in today's folder.

```media-spec
{"story": {"prompt": "", "text_overlay": "She described our product back to me without knowing the brief."}, "carousel": [{"prompt": "", "text_overlay": "She described our product back to me without knowing the brief."}]}
```
