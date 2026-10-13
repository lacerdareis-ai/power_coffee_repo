# Power Coffee — Content for October 14, 2026
**Pillar:** P3 — FOUNDER PROOF | **Day:** Wednesday | **Image set:** C4 or E3

---
## APPROVAL
- [x] APPROVED

---

---

## INSTAGRAM
### Story Copy
STILL CRASHING AT 2PM?

I used to think it was me. It wasn't.

Sticker: Poll — "Does your afternoon still fall apart?" Yes, every day / No, I fixed it

---

## X.COM
### Post
Two years ago I was on my third coffee by 10am and still foggy by 2pm. I thought that was just adulthood. It wasn't. It was a formula problem, not a discipline problem.

### Thread
Post 1: Two years ago I was on my third coffee by 10am and still crashing by 2pm. I thought that was just what being busy felt like.
Post 2: Turns out the crash wasn't about effort or willpower. It was about what was missing from my cup, not what I was lacking as a person.
Post 3: I spent two years testing formulas before I had one that got me through a full day without the 2pm wall. That part took longer than I expected.
Post 4: That testing became Power Coffee. One scoop into the coffee I already drink, same ritual, no second routine to learn.
Post 5: If 2pm still owns your day, try a week of it. https://thepowercoffee.com/pages/betterday

---

## LINKEDIN
### Post
You are not the same decision-maker at 10am and 4pm.

Same person, same calendar, genuinely different capacity — and most of us let whatever's open on the calendar decide which version handles the hard call, instead of deciding on purpose.

I scheduled the hardest conversation of a week for 4:47pm once, by accident. I've since started treating "who's actually available right now" as a real question, not just "what's open."

---

## TELEGRAM
### Message
Quick one today. Two years ago I was running on three coffees a day and still hitting a wall by 2pm — and I genuinely thought that was just how it had to be. It wasn't. Took two years of testing to find out what was actually missing. If your afternoons still disappear on you, that's worth fixing before anything else.

---

## HIGGSFIELD (Story Image)
### Model
FLUX.2 Pro (image)

### Aspect Ratio
9:16 (Stories)

### Prompt
A man in his mid-30s walking through a dim garage at dawn past a road bike, wearing cycling kit, holding a single travel mug in one hand, dawn light streaming through the open garage door behind him creating a strong silhouette and lens flare. Purposeful stride, face turned slightly away from camera, not posed. Deep shadows in foreground, warm golden light in background creating high contrast. Black, gold, and navy color tones. Shallow depth of field, cinematic documentary photography style, grain texture. Negative space in the upper third of the frame for text overlay. No text, no logos, no signage in image. --ar 9:16

---

## REELS — Founder Vlog Script
**Series:** Building Power Coffee — Ep. 15
**Beat:** The two-year formula testing grind, told through this week's Ironman training load
**Title formula:** Why the formula took two years | 5am training block this week
**Duration:** 35s · **Setting:** Garage at dawn, Leo in cycling kit, bike behind him, travel mug in hand

**HOOK (0-3s, text on screen + spoken):**
"Two years. Five versions. One formula I'd actually trust."

**BODY (speak exactly this):**
"This week I logged my longest training block yet for the Ironman, and it reminded me why I built this in the first place. I didn't start with a business plan. I started with my own 2pm crash, three coffees deep and still foggy. It took two years and five full versions before I had something I'd put my name on. I still mix it the same way, every morning, before I touch a bike or a laptop. Not because I run the company. Because it works."

**CTA (last 5s):**
"Follow along — I'm documenting the whole build. What should I cover next week?"

**B-ROLL:** Leo walking past the bike in the garage, close-up of hands mixing one scoop into a travel mug, Leo clipping into the bike and riding off down the driveway at dawn

**CAPTION:** Two years, five formula versions, one crash I was done living with. Documenting the real build, not the highlight reel. Ep. 15 — Building Power Coffee
#buildinginpublic #founderstory #cleanenergy #morningroutine #powercoffee

**ON-SCREEN TEXT:** 0-3s: "2 years. 5 versions." / 15s: "Still mixed the same way every morning" / 30s: "Follow the build"

---

## SCIENCE NOTE — Founder Interview Prep (not for publishing)
**Ingredient / mechanism:** Taurine as an osmolyte and cytoprotective modulator
Taurine is one of the most abundant free amino acids in excitable tissue — skeletal muscle, heart, and brain — where it functions primarily as an organic osmolyte, regulating cell volume and intracellular calcium handling under metabolic stress. In the central nervous system, taurine modulates GABA-A and glycine receptor activity at low-affinity sites, which is distinct from acting as a classic inhibitory neurotransmitter itself; this has been proposed as a mechanism for its reported calming, non-sedating effect alongside stimulant caffeine. In mitochondria, taurine conjugates with tRNA to support efficient oxidative phosphorylation, and deficiency has been linked in animal models to impaired mitochondrial protein synthesis and increased oxidative stress. At 2.1g per serving, Power Coffee's dose sits within the range studied in sports-performance and cardiovascular literature, though effects vary by individual and taurine status.
**Reference:** Ripps H, Shen W. "Review: Taurine: A "very essential" amino acid." Mol Vis. 2012;18:2673-2686. PMID: 23170060
**Interview angle:** Taurine may help support a steadier, less jittery stimulant response when paired with caffeine — it doesn't cure fatigue or guarantee performance, but it's one of the more mechanistically studied aminos in the stack.

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
const SLIDES = [{ id: 1, slideType: "hook", overline: "THE 2PM CRASH", headline: "STILL CRASHING\nAT 2PM?", subtext: "I used to think it was me. It wasn't.", accent: "BROWN", bg: "BLACK", textColor: "CREAM" }
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
{"story": {"prompt": "A man in his mid-30s walking through a dim garage at dawn past a road bike, wearing cycling kit, holding a single travel mug in one hand, dawn light streaming through the open garage door behind him creating a strong silhouette and lens flare. Purposeful stride, face turned slightly away from camera, not posed. Deep shadows in foreground, warm golden light in background creating high contrast. Black, gold, and navy color tones. Shallow depth of field, cinematic documentary photography style, grain texture. Negative space in the upper third of the frame for text overlay. No text, no logos, no signage in image. --ar 9:16\n\n---", "text_overlay": "Two years. Five versions. One formula I'd actually trust."}, "carousel": [{"prompt": "A man in his mid-30s walking through a dim garage at dawn past a road bike, wearing cycling kit, holding a single travel mug in one hand, dawn light streaming through the open garage door behind him creating a strong silhouette and lens flare. Purposeful stride, face turned slightly away from camera, not posed. Deep shadows in foreground, warm golden light in background creating high contrast. Black, gold, and navy color tones. Shallow depth of field, cinematic documentary photography style, grain texture. Negative space in the upper third of the frame for text overlay. No text, no logos, no signage in image. --ar 9:16\n\n---", "text_overlay": "Two years. Five versions. One formula I'd actually trust."}]}
```
