# Power Coffee — Content for November 04, 2026
**Pillar:** P3 — FOUNDER PROOF | **Day:** Wednesday | **Image set:** C4 or E3

---
## APPROVAL
- [x] APPROVED

---

---

## INSTAGRAM
### Story Copy
STILL CRASHING AT 2PM?
Leo's been exactly there — same desk, same wall.
Sticker: Poll — "Does your afternoon crash too? YES / EVERY DAY"

### Caption
Six months ago I was the guy hitting the wall at 2pm, reaching for a third coffee that did nothing but make my hands shake.

I didn't build Power Coffee because I love ingredients. I built it because I was tired of losing my afternoons.

If that's you right now, you're not undisciplined. You're missing something your coffee isn't giving you.

Try it for a week. Then tell me if your 2pm changed.

https://thepowercoffee.com/pages/betterday

### Hashtags
#2pmcrash #founderstory #cleanenergy #morningroutine #nocrash #realtalk #thefirstwin #highperformance #workfromhome #focusmode

---

## X.COM
### Post
Six months ago I was the guy reaching for a third coffee at 2pm that did nothing but make my hands shake. Built Power Coffee because I was tired of losing my afternoons. If that's you, you're not undisciplined. Something's missing from your cup.

### Thread
Post 1: Six months ago I was face-down at my desk at 2pm every single day. Three coffees in. Still gone. I thought something was wrong with me.
Post 2: Turns out nothing was wrong with me. My coffee was giving me a fast spike and an even faster drop. That's not a focus problem. That's a formula problem.
Post 3: I spent two years testing what actually holds energy steady through an afternoon instead of torching it in 45 minutes.
Post 4: That's how Power Coffee started. One scoop added to the coffee you already drink. Built for the exact wall I used to hit.
Post 5: If 2pm has been winning for too long, try it for a week. https://thepowercoffee.com/pages/betterday

---

## LINKEDIN
### Post
"Nothing's there yet" and "something's there and someone already said yes" are two completely different states.

Our content pipeline treated them identically for months — regenerate either way — until it quietly erased a day of approved work that happened to look, to the script, exactly like an empty one.

---

## TELEGRAM
### Message
Quick one from Leo — six months before this company existed, I was the guy hitting a wall at 2pm every single day, three coffees in, nothing working. That's actually why Power Coffee exists. If your afternoon has been losing to you lately, reply and tell me what time it happens. I read every one.

---

## HIGGSFIELD (Story Image)
### Model
FLUX.2 Pro (image)

### Aspect Ratio
9:16 (Stories)

### Prompt
A man in his mid-30s standing alone in a dim home office at dusk, hands pressed flat on a cluttered desk, head slightly bowed in exhaustion, warm desk lamp casting a small pool of gold light against deep shadow, window behind him showing a fading orange sky, high contrast between the warm lamp glow and the cool blue shadow, cinematic documentary photography, shallow depth of field, grainy film texture, moody and real, no text in frame, negative space in upper third for overlay, 9:16 vertical composition.

---

## REELS — Founder Vlog Script
**Series:** Building Power Coffee — Ep. 18
**Beat:** Founder origin thread — the real 2pm wall that started the company
**Title formula:** Why I almost shelved the whole idea | the 2pm wall that built it
**Duration:** 35s · **Setting:** Home office, late afternoon light, Leo seated at desk, laptop closed

**HOOK (0-3s, text on screen + spoken):**
"I almost didn't start this company."

**BODY (speak exactly this):**
"Before Power Coffee existed, I had a bad habit. Three coffees, every day, and by 2pm I was done. Head on the desk. I thought it was a discipline problem, so I pushed harder. It wasn't discipline. It was the coffee — fast up, faster down. That's the actual reason I started testing formulas, kitchen table, two years, more failed batches than I'll admit. This cup right here is version whatever-number-we're-on-now. Still not done improving it."

**CTA (last 5s):**
"Comment your 2pm time. I read all of them."

**B-ROLL:** Leo closing a laptop at a cluttered desk, late-afternoon window light fading to dusk, hand stirring one scoop into a mug on the counter
**CAPTION:** The real reason Power Coffee exists — my own 2pm wall, six months before launch. Still fixing it one batch at a time. Ep. 18 — Building Power Coffee #founderstory #buildinginpublic #2pmcrash #cleanenergy #powercoffee
**ON-SCREEN TEXT:** 0s "I almost didn't start this company" / 15s "Three coffees. Still done by 2pm." / 30s "Comment your 2pm time"

---

## SCIENCE NOTE — Founder Interview Prep (not for publishing)
**Ingredient / mechanism:** Taurine as an osmolyte and cytoprotective modulator
Taurine is one of the most abundant free amino acids in excitable tissue, including skeletal muscle and the central nervous system, yet it isn't a classical neurotransmitter. Its primary mechanistic roles are as an osmolyte, regulating cell volume and ionic balance under metabolic stress, and as a modulator of mitochondrial protein synthesis via taurine-modified mitochondrial tRNAs, which supports efficient oxidative phosphorylation. It also interacts with GABA-A and glycine receptors at inhibitory synapses, contributing to a calming, non-sedating effect distinct from caffeine's stimulatory action. In the context of a caffeinated beverage, taurine's role is best understood as a cellular stability and stress-buffering co-factor rather than an energy source itself — it doesn't spike arousal, it supports the cellular environment that sustained arousal depends on. At 2.1g per serving, Power Coffee's dose sits within ranges studied in exercise and cognitive performance literature.
**Reference:** Schaffer & Kim, "Taurine and Cell Survival," J Biomed Sci, 2018 [VERIFY CITATION]
**Interview angle:** Taurine may support the body's ability to buffer physical and metabolic stress during sustained mental effort — it's a stability layer, not a stimulant, and individual responses vary.

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
const SLIDES = [{ id: 1, slideType: "hook", overline: "STILL CRASHING AT 2PM?", headline: "SAME DESK.\nSAME WALL.\nSAME 2PM.", subtext: "Leo's been exactly there. Does your afternoon crash too?", accent: "BROWN", bg: "BLACK", textColor: "CREAM" }
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
{"story": {"prompt": "A man in his mid-30s standing alone in a dim home office at dusk, hands pressed flat on a cluttered desk, head slightly bowed in exhaustion, warm desk lamp casting a small pool of gold light against deep shadow, window behind him showing a fading orange sky, high contrast between the warm lamp glow and the cool blue shadow, cinematic documentary photography, shallow depth of field, grainy film texture, moody and real, no text in frame, negative space in upper third for overlay, 9:16 vertical composition.\n\n---", "text_overlay": "I almost didn't start this company."}, "carousel": [{"prompt": "A man in his mid-30s standing alone in a dim home office at dusk, hands pressed flat on a cluttered desk, head slightly bowed in exhaustion, warm desk lamp casting a small pool of gold light against deep shadow, window behind him showing a fading orange sky, high contrast between the warm lamp glow and the cool blue shadow, cinematic documentary photography, shallow depth of field, grainy film texture, moody and real, no text in frame, negative space in upper third for overlay, 9:16 vertical composition.\n\n---", "text_overlay": "I almost didn't start this company."}]}
```
