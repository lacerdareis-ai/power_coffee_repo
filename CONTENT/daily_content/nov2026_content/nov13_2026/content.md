# Power Coffee — Content for November 13, 2026
**Pillar:** P6 — DIRECT CTA | **Day:** Friday | **Image set:** A1 or A2

---
## APPROVAL
- [ ] APPROVED

---

---

## INSTAGRAM
### Carousel Copy

**Slide 1:**
STILL ADDING A SECOND CUP AT 3PM?

**Slide 2:**
You already had coffee this morning. By mid-afternoon, after lunch, it's gone — and the second cup doesn't always fix it. Sometimes it just costs you sleep tonight.

**Slide 3:**
The move isn't more coffee. It's a better first one.

**Slide 4:**
One scoop in the coffee you already drink, in the morning. Designed to help you carry steady energy and focus through the afternoon slump, without stacking another cup.

**Slide 5:**
This weekend only: use MORNING15 for 15 percent off, one-time purchases, one use per customer.

**Slide 6:**
Keep your morning coffee. Skip the 3pm one. Shop at thepowercoffee.com/pages/betterday — link @powercoffee.ofc

### Caption
Three coffees in and still losing the afternoon.

That's not a willpower problem. It's a one-cup problem.

Power Coffee goes into the coffee you're already drinking in the morning — designed to help you hold steady energy and real focus through the post-lunch slump, so you're not reaching for a second or third cup later.

This weekend: MORNING15 gets you 15 percent off, one-time purchases, one use per customer.

Keep your morning coffee. Skip the 3pm one.

Shop at thepowercoffee.com/pages/betterday.

Not intended to diagnose, treat, cure, or prevent any disease.

### Hashtags
#afternoonslump #coffeecrash #functionalcoffee #morningroutine #cleanenergy #biohacking #powercoffee #thefirstwin #worklife #focusmode

---

## X.COM
### Post
Still adding a 3pm coffee to fix the 2pm crash? Try fixing the morning one instead. MORNING15 for 15% off this weekend. thepowercoffee.com/pages/betterday

### Thread
Post 1: You don't have an afternoon problem. You have a morning problem that shows up at 2pm.
Post 2: The second cup feels like the fix. Often it just trades today's crash for tonight's sleep.
Post 3: The better move: one scoop in the coffee you already drink in the morning, designed to help carry steady energy into the afternoon.
Post 4: That's what Power Coffee is built to do. Keep your ritual. Skip the stacking.
Post 5: This weekend only: MORNING15 for 15% off, one-time purchases. thepowercoffee.com/pages/betterday

---

## LINKEDIN
### Post
Good news if you missed a day of something you're trying to build: it barely matters.

In Phillippa Lally's habit study at UCL, a new habit took 66 days on average to become automatic, and one missed day hardly changed the result.

What breaks a rhythm isn't the missed day. It's the week you quietly let slide.

So miss a day if you have to. Just don't miss the second one.

---

## WHATSAPP
### Message
Hey, quick one before the weekend. If you're the "third coffee by 3pm and still dragging" type, this is for you. We've got MORNING15 live for 15 percent off through the weekend, one-time purchases. thepowercoffee.com/pages/betterday. Keep your morning coffee, skip the extra cup.

---

## HIGGSFIELD (Carousel Cover)
### Model
FLUX.2 Pro (image)

### Aspect Ratio
1:1 (feed carousel)

### Prompt
A man in his late 30s standing at a kitchen counter in early morning light, mid-motion spooning powder from a white stand-up pouch with a navy-blue side panel into a single ceramic mug. He is dressed for the day, slightly rushed but focused, phone and keys on the counter nearby. Warm golden-hour light through a window, soft shadows, shallow depth of field. Muted cream and espresso-brown tones with subtle gold accent light. Only one mug in frame, product pouch visible but not centered. Negative space in the upper third of the frame. No text, no logos rendered. Documentary lifestyle photography style, candid, unposed.

---

## REELS — Founder Vlog Script
**Series:** Building Power Coffee — Ep. 19
**Beat:** The weekend offer and why I keep saying "skip the second cup," not "buy more"
**Title formula:** Why I built an offer around less coffee, not more | Saturday long run before sunrise
**Duration:** 30-45s · **Setting:** Kitchen counter, early morning, natural window light, Leo in running gear

**HOOK (0-3s, text on screen + spoken):**
"I built a coffee brand telling people to drink less coffee."

**BODY (speak exactly this):**
"Every offer we run, people expect me to say buy more. I don't. This weekend's code, MORNING15, it's for your one morning cup, not a third one at 3pm. That's been the whole bet since day one — fix the first cup, skip the stacking. I ran six miles this morning before this call, one scoop in my coffee before I left the house, nothing after lunch. That's the test I keep running on myself, every single day."

**CTA (last 5s):**
"MORNING15 this weekend only, link at thepowercoffee.com/pages/betterday."

**B-ROLL:** Leo spooning powder into one mug at counter, running shoes by the door, early morning street shot mid-run
**CAPTION:** One offer, one rule: fix the morning cup, skip the extra one. MORNING15 live this weekend only. Ep. 19 — Building Power Coffee
**ON-SCREEN TEXT:** "0:01 — 'Drink less coffee?'" / "0:15 — MORNING15, this weekend" / "0:35 — Link at thepowercoffee.com/pages/betterday"

---

## SCIENCE NOTE — Founder Interview Prep (not for publishing)
**Ingredient / mechanism:** Taurine as an osmolyte and cytoprotective modulator

Taurine is one of the most abundant free amino acids in excitable tissue — skeletal muscle, heart, and brain — where it functions primarily as an organic osmolyte, helping cells regulate volume and ionic balance under metabolic stress. Beyond osmoregulation, taurine stabilizes mitochondrial membrane potential and modulates calcium handling in cardiac and skeletal muscle, which is part of why it's studied in exercise physiology for recovery and oxidative stress markers. It also interacts with GABA-A and glycine receptors at a low-affinity level, contributing a mild inhibitory tone in the CNS without acting as a classical sedative. At 2.1g per serving, Power Coffee's dose sits within the range used in several human exercise-performance trials. This isn't a stimulant pathway — it runs parallel to caffeine's adenosine antagonism, which is part of the rationale for pairing the two.

**Reference:** Schaffer & Kim, "Effects and Mechanisms of Taurine as a Therapeutic Agent," Biomolecules & Therapeutics, 2018, PMID 29370967

**Interview angle:** Taurine may support cellular resilience under physical stress — it's not a stimulant, and individual results vary; not intended to diagnose, treat, cure, or prevent any disease.

---

## FIGMA SCRIPTER
```javascript
// Power Coffee - CAROUSEL - Figma Scripter
// Paste into: Plugins > Scripter > Run
// Creates N slides (1080x1080 px each) as a row of frames

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
const SLIDES = [{ id: 1, slideType: "hook", overline: "THE 3PM QUESTION", headline: "STILL ADDING\nA SECOND CUP\nAT 3PM?", subtext: "There's a better fix than another coffee.", accent: "BROWN", bg: "BLACK", textColor: "CREAM" }, { id: 2, slideType: "teach", overline: "WHAT'S HAPPENING", headline: "THE MORNING\nCOFFEE WEARS\nOFF", subtext: "By mid-afternoon, after lunch, it's gone  -  and the second cup doesn't always fix it. Sometimes it just costs you sleep tonight.", accent: "BROWN_L", bg: "BLACK", textColor: "CREAM" }, { id: 3, slideType: "teach", overline: "THE REAL FIX", headline: "NOT MORE\nCOFFEE. A\nBETTER FIRST\nONE.", subtext: "The move isn't stacking cups. It's starting stronger.", accent: "BROWN_L", bg: "BLACK", textColor: "CREAM" }, { id: 4, slideType: "teach", overline: "HOW IT WORKS", headline: "ONE SCOOP.\nONE MORNING\nCOFFEE.", subtext: "Designed to help you carry steady energy and focus through the afternoon slump, without stacking another cup.", pills: ["ONE SCOOP", "MORNING ONLY", "STEADY FOCUS"], accent: "BROWN_L", bg: "BLACK", textColor: "CREAM" }, { id: 5, slideType: "teach", overline: "THIS WEEKEND ONLY", headline: "15% OFF\nYOUR FIRST\nORDER", subtext: "Use MORNING15 for 15 percent off, one-time purchases, one use per customer.", accent: "BROWN_L", bg: "BLACK", textColor: "CREAM" }, { id: 6, slideType: "cta", isCTA: true, overline: "KEEP THE MORNING, SKIP THE 3PM", headline: "KEEP YOUR\nMORNING COFFEE.\nSKIP THE\n3PM ONE.", subtext: "Shop at thepowercoffee.com/pages/betterday  -  link @powercoffee.ofc", accent: "CREAM", bg: "BROWN", textColor: "WHITE" }
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

> **Instructions:** Paste into Figma → Plugins → Scripter → Run. Export each frame at 1x as PNG → save as `carousel_1.jpg, carousel_2.jpg...` in today's folder.

```media-spec
{"story": {"prompt": "A man in his late 30s standing at a kitchen counter in early morning light, mid-motion spooning powder from a white stand-up pouch with a navy-blue side panel into a single ceramic mug. He is dressed for the day, slightly rushed but focused, phone and keys on the counter nearby. Warm golden-hour light through a window, soft shadows, shallow depth of field. Muted cream and espresso-brown tones with subtle gold accent light. Only one mug in frame, product pouch visible but not centered. Negative space in the upper third of the frame. No text, no logos rendered. Documentary lifestyle photography style, candid, unposed.\n\n---", "text_overlay": "STILL ADDING A SECOND CUP AT 3PM?"}, "carousel": [{"prompt": "A man in his late 30s standing at a kitchen counter in early morning light, mid-motion spooning powder from a white stand-up pouch with a navy-blue side panel into a single ceramic mug. He is dressed for the day, slightly rushed but focused, phone and keys on the counter nearby. Warm golden-hour light through a window, soft shadows, shallow depth of field. Muted cream and espresso-brown tones with subtle gold accent light. Only one mug in frame, product pouch visible but not centered. Negative space in the upper third of the frame. No text, no logos rendered. Documentary lifestyle photography style, candid, unposed.\n\n---", "text_overlay": "STILL ADDING A SECOND CUP AT 3PM?"}]}
```
