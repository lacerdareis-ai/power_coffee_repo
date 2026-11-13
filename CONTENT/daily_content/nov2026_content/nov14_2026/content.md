# Power Coffee — Content for November 14, 2026
**Pillar:** P4 — RITUAL CONTENT | **Day:** Saturday | **Image set:** A4

---
## APPROVAL
- [ ] APPROVED

---

---

## INSTAGRAM
### Caption
Saturday morning. No alarm, no rush, just the slow kind of ritual that actually sticks. One scoop in the cup, a quiet kitchen, the day not asking anything of you yet.

This is the version of the routine that holds up Monday through Friday too — not because it's complicated, but because it isn't. One cup. One scoop. Done before the day gets loud.

The afternoon slump usually starts with how the morning went. Start it steady, keep more of the day.

Not intended to diagnose, treat, cure, or prevent any disease.

### Hashtags
#morningroutine #cleanenergy #functionalcoffee #thefirstwin #slowmornings #biohacking #capecod #powercoffee #nocrash #realmornings

---

## X.COM
### Post
Saturday mornings are the test. No deadline forcing the routine — and the scoop still goes in the cup first. That's how you know a ritual actually stuck. https://thepowercoffee.com/pages/betterday

### Thread
Post 1: Weekday routines are easy to fake. Saturday mornings tell the truth.
Post 2: If the ritual only survives when a calendar makes you do it, it's not a ritual. It's a chore with good PR.
Post 3: Mine's one scoop, one cup, before the house wakes up. Takes less time than deciding what to wear.
Post 4: That's the whole design behind Power Coffee — it has to fit into a real morning, not a curated one.
Post 5: If your weekday energy depends on your weekend discipline, start there. https://thepowercoffee.com/pages/betterday

---

## LINKEDIN
### Post
This week I found out our daily content had stopped two days earlier. An account that one of our tools runs on ran out of credit, and the morning job quietly failed. Nobody complained, because nobody notices something that isn't there.

When your energy runs out, you feel it.
When your cadence stops, nothing tells you.

So every rhythm needs two things: a floor (the minimum you do no matter what) and a tripwire (how you know, the same day, that it didn't happen).

I had the floor. I'm building the tripwire now.

---

## WHATSAPP
### Message
Happy Saturday. No alarm today, but the scoop still went in first thing, before coffee even finished brewing. Some habits you keep because they work, not because you have to. What does your slow morning look like today?

---

## HIGGSFIELD (Image)
### Model
FLUX.2 Pro (image)

### Aspect Ratio
1:1 (feed post)

### Prompt
A relaxed Saturday morning kitchen scene, soft warm natural light pouring through a window, a man in his late 30s in a simple t-shirt standing at a counter mid-pour, spooning powder from a white stand-up pouch with a navy-blue left side panel into a single ceramic mug, unhurried posture, slight morning stubble, a newspaper or book nearby, muted cream and espresso-brown tones with soft gold accents, shallow depth of field, lived-in kitchen details, candid unposed moment, negative space in the upper third of the frame for text overlay, no text rendered in image, photographic realism, warm golden-hour style lighting.

---

## REELS — Founder Vlog Script
**Series:** Building Power Coffee — Ep. 19
**Beat:** Saturday ritual check — does the routine hold without pressure forcing it
**Title formula:** The habit that doesn't need a deadline | Saturday morning routine
**Duration:** 30-45s · **Setting:** Leo's home kitchen, handheld, natural morning light

**HOOK (0-3s, text on screen + spoken):**
"No alarm today. I still did it first thing."

**BODY (speak exactly this):**
"It's Saturday. Nothing's making me do this. No meeting, no 5am swim session, nothing on the calendar. And I still scooped this into my cup before I did anything else. That's the test I actually trust — not what you do when the week is pushing you, what you do when it isn't. Same thing happened when we were building the formula. The batches that worked weren't the ones we rushed under deadline pressure. They were the ones we kept testing on the days nobody was watching."

**CTA (last 5s):**
"What's the one habit you keep even with nothing forcing you? Comment below."

**B-ROLL:** scoop going into mug on quiet counter, hand stirring, Leo looking out kitchen window with mug in hand
**CAPTION:** The habit test isn't Monday. It's Saturday, when nothing's forcing you. Still one scoop, same cup, same ten quiet minutes.
#morningritual #founderstory #buildinginpublic #capecod #powercoffee
Ep. 19 — Building Power Coffee

**ON-SCREEN TEXT:**
0:00 "No alarm today."
0:08 "Still the first thing I did."
0:25 "That's the real test."

---

## SCIENCE NOTE — Founder Interview Prep (not for publishing)
**Ingredient / mechanism:** Taurine as an osmolyte and cytoprotective modulator
Taurine is a sulfonic beta-amino acid present in high concentration in excitable tissues like skeletal muscle, the heart, and the central nervous system. It functions primarily as an organic osmolyte, helping cells regulate volume and ionic balance under metabolic or osmotic stress. Beyond osmoregulation, taurine modulates calcium flux across cell membranes in cardiac and skeletal muscle, which has been linked to its role supporting exercise performance and delaying fatigue onset in some studies. It also acts as a mild agonist at GABA-A and glycine receptors in the CNS, contributing to its described "calming without sedating" profile — distinct from classical stimulants. In mitochondria, taurine conjugates with tRNA to support proper mitochondrial protein synthesis, and deficiency has been associated with impaired mitochondrial function and oxidative stress accumulation. At the 2.1g dose per serving in Power Coffee, taurine sits within ranges studied for exercise and cognitive performance contexts, well below reported safety thresholds.
**Reference:** Schaffer & Kim, "Effects and Mechanisms of Taurine as a Therapeutic Agent," Biomolecules & Therapeutics, 2018, PMID 29631391
**Interview angle:** Taurine may support cellular resilience and calm focus through osmotic and receptor-level mechanisms — not a stimulant, a modulator, and results vary by individual.

---

## FIGMA SCRIPTER
```javascript
// Power Coffee - POST - Figma Scripter
// Paste into: Plugins > Scripter > Run
// Creates 1 frame (1080x1080 px)

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
const H = 1080;
const GAP = 60;

// SLIDE DATA - accent/bg/textColor must be quoted strings: "BLACK", "BROWN", "BROWN_L", "CREAM", "WHITE"
const SLIDES = [{ id: 1, slideType: "hook", overline: "SATURDAY MORNING RITUAL", headline: "One Scoop.\nQuiet Kitchen.\nSteady Day Ahead.", subtext: "The routine that holds up Monday through Friday too  -  not because it's complicated, but because it isn't.", accent: "BROWN", bg: "BLACK", textColor: "CREAM" }
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

> **Instructions:** Paste into Figma → Plugins → Scripter → Run. Export each frame at 1x as PNG → save as `instagram.jpg` in today's folder.

```media-spec
{"story": {"prompt": "A relaxed Saturday morning kitchen scene, soft warm natural light pouring through a window, a man in his late 30s in a simple t-shirt standing at a counter mid-pour, spooning powder from a white stand-up pouch with a navy-blue left side panel into a single ceramic mug, unhurried posture, slight morning stubble, a newspaper or book nearby, muted cream and espresso-brown tones with soft gold accents, shallow depth of field, lived-in kitchen details, candid unposed moment, negative space in the upper third of the frame for text overlay, no text rendered in image, photographic realism, warm golden-hour style lighting.\n\n---", "text_overlay": "No alarm today. I still did it first thing."}, "carousel": [{"prompt": "A relaxed Saturday morning kitchen scene, soft warm natural light pouring through a window, a man in his late 30s in a simple t-shirt standing at a counter mid-pour, spooning powder from a white stand-up pouch with a navy-blue left side panel into a single ceramic mug, unhurried posture, slight morning stubble, a newspaper or book nearby, muted cream and espresso-brown tones with soft gold accents, shallow depth of field, lived-in kitchen details, candid unposed moment, negative space in the upper third of the frame for text overlay, no text rendered in image, photographic realism, warm golden-hour style lighting.\n\n---", "text_overlay": "No alarm today. I still did it first thing."}]}
```
