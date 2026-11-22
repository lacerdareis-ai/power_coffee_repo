# Power Coffee — Content for November 18, 2026
**Pillar:** P3 — FOUNDER PROOF | **Day:** Wednesday | **Image set:** C4 or E3

---
## APPROVAL
- [x] APPROVED

---

---

## INSTAGRAM
### Story Copy
STILL CRASHING AT 2PM?
Same slump, different day — here's what's actually changing for me.
Sticker: Poll — "Third cup today?" Yes / Not again

### Caption
2pm hits. The laptop's open, the to-do list isn't moving, and the third cup is sitting there not doing its job.

I used to live that exact loop. Same crash, same second-guessing my own coffee.

What changed wasn't willpower. It was what I put in the cup before 6am even started — one scoop, same cup I already drink. That's it.

Still showing up at 4:50am most days. Not because I'm special. Because the morning is the one part of the day I can control.

How's your afternoon looking today? Tell me your 2pm.

FDA disclaimer: These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.

### Hashtags
#functionalcoffee #cleanenergy #afternoonslump #morningroutine #biohacking #powercoffee #thefirstwin #focusfuel #nocrash #coffeeroutine

---

## X.COM
### Post
Third coffee of the day and you're still fading by 2pm. I lived that exact loop for years. What fixed it wasn't more coffee — it was fixing the first cup. Same mug I already drink.

### Thread
Post 1: You're on your third coffee and still crashing by 2pm. I know that exact feeling — I lived it every afternoon before I built anything.
Post 2: The instinct is to add a cup. Problem is the second or third one rarely holds — some days it costs you sleep too.
Post 3: What actually changed things for me was the first cup, not the third. One scoop in my regular morning coffee, same ritual, different outcome by early afternoon.
Post 4: I still get up at 4:50am most days. Not for the content. Because the one part of my day I can fully control is the morning — and that's where I fixed this first.
Post 5: If your afternoon keeps falling apart, start with the morning cup, not another one. https://thepowercoffee.com/pages/betterday

---

## LINKEDIN
### Post
I almost didn't make the 4:50am alarm this week.

Three nights of bad sleep, a supplier call that ran long, and a part of me said sleep in, you earned it.

I got up anyway. Not because I had some iron rule about it. Because I've learned that the first decision of my day sets the tone for every decision after it.

Building Power Coffee has taught me that discipline isn't about intensity. It's about consistency on the days you don't feel like it.

Same thing I hear from customers about their afternoons — the fix usually isn't trying harder at 2pm. It's what you set up at 6am.

What's the one habit you keep even on the days you don't want to?

---

## WHATSAPP
### Message
Hey — quick one. What time does your energy actually drop today? For me it used to be 2pm, every single day, no matter how much coffee I drank. Curious what your slump looks like. Reply and tell me, I read every one.

---

## HIGGSFIELD (Story Image)
### Model
FLUX.2 Pro (image)

### Aspect Ratio
9:16 (Stories)

### Prompt
A man in his mid-30s walking through a dim garage at dawn, early blue light mixing with a warm kitchen glow through an open doorway behind him, holding a single travel mug in one hand, dressed in running gear, purposeful stride, not looking at camera, road bike leaning against the wall, black and gold color tones, cinematic shallow depth of field, high contrast, negative space in the upper third of the frame, no text, no logos, photographic realism

---

## REELS — Founder Vlog Script
**Series:** Building Power Coffee — Ep. 20
**Beat:** The 2pm crash, mirrored through a founder's own loop
**Title formula:** Why I stopped trying to fix the afternoon | 4:50am most days
**Duration:** 30-45s · **Setting:** Kitchen counter at dawn, natural window light

**HOOK (0-3s, text on screen + spoken):**
"I used to hit a wall every single day at 2pm."

**BODY (speak exactly this):**
"Same time, every day. Third coffee on the desk, still foggy, still behind. I spent a long time thinking the answer was trying harder in the afternoon. It wasn't. The one thing I could actually control was the morning — so that's where I started. Same cup I already drink, one scoop added before anything else happens. I'm still up most days around 4:50am. Not because I love mornings. Because it's the one part of the day nobody else touches yet."

**CTA (last 5s):**
"What's your 2pm look like? Comment below."

**B-ROLL:** hand spooning scoop into mug on kitchen counter, Leo walking out the door with travel mug in dawn light, quick shot of a clock or phone showing 2:00pm

**CAPTION:** Same crash, same desk, every day at 2pm — until I stopped fighting the afternoon and fixed the morning instead. Still up most days before 5am. Tell me your 2pm.
#buildingpowercoffee #founderjourney #morningroutine #cleanenergy #nocrash
Ep. 20 — Building Power Coffee

**ON-SCREEN TEXT:** 0:00 "2pm. Every day." / 0:15 "The fix wasn't more coffee" / 0:30 "4:50am. Most days."

---

## SCIENCE NOTE — Founder Interview Prep (not for publishing)
**Ingredient / mechanism:** Taurine as an osmolyte and cytoprotective modulator
Taurine is a sulfonic beta-amino acid present at high concentration (2.1g per serving here) in excitable tissues — skeletal muscle, heart, retina, and CNS. It functions primarily as an organic osmolyte, regulating cell volume under osmotic stress, and as a modulator of intracellular calcium handling in cardiac and skeletal muscle, which is part of why it's studied in exercise contexts. Separately, taurine has documented antioxidant-adjacent cytoprotective roles — it conjugates with hypochlorous acid to form a less reactive compound, reducing oxidative damage without acting as a classical free-radical scavenger itself. Unlike caffeine, it does not act on adenosine receptors; its relevance to energy/focus claims is indirect, via cellular resilience rather than CNS stimulation. Dosing in sports nutrition literature commonly ranges 1-3g acutely.
**Reference:** Ripps H, Shen W. "Review: Taurine: A "very essential" amino acid." Mol Vis. 2012;18:2673-2686. PMID: 23170060
**Interview angle:** Taurine isn't a stimulant — it may support cellular resilience and fluid balance during physical exertion, which is why it's paired with caffeine rather than relied on alone for energy.

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
const SLIDES = [{ id: 1, slideType: "hook", overline: "STILL CRASHING AT 2PM?", headline: "SAME SLUMP\nDIFFERENT DAY\nHERE'S WHAT\nCHANGED", subtext: "What changed wasn't willpower. It was what went in the cup before 6am even started  -  one scoop, same cup I already drink.", accent: "BROWN", bg: "BLACK", textColor: "CREAM" }
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
{"story": {"prompt": "A man in his mid-30s walking through a dim garage at dawn, early blue light mixing with a warm kitchen glow through an open doorway behind him, holding a single travel mug in one hand, dressed in running gear, purposeful stride, not looking at camera, road bike leaning against the wall, black and gold color tones, cinematic shallow depth of field, high contrast, negative space in the upper third of the frame, no text, no logos, photographic realism\n\n---", "text_overlay": "I used to hit a wall every single day at 2pm."}, "carousel": [{"prompt": "A man in his mid-30s walking through a dim garage at dawn, early blue light mixing with a warm kitchen glow through an open doorway behind him, holding a single travel mug in one hand, dressed in running gear, purposeful stride, not looking at camera, road bike leaning against the wall, black and gold color tones, cinematic shallow depth of field, high contrast, negative space in the upper third of the frame, no text, no logos, photographic realism\n\n---", "text_overlay": "I used to hit a wall every single day at 2pm."}]}
```
