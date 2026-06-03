# Power Coffee — Content for June 03, 2026
**Pillar:** P3 — FOUNDER PROOF | **Day:** Wednesday | **Image set:** C4 or E3

---
## APPROVAL
- [x] APPROVED

> Auto-approved. To reject: change [x] to [ ] before 4am.

---

## INSTAGRAM
### Story Copy
**HEADLINE:** I DRINK MY OWN PRODUCT DAILY

Subtext: 550+ days in. Here's what changed.

**Sticker:** Poll — "Would you try it?" → YES, ALREADY ON IT / NOT YET

---

### Caption
550 days of drinking the same formula I built.

Not because I have to.
Because it works.

Every morning. One scoop. Before the day hits.

The energy is real. The focus holds.
No crash by noon. No second or third cup.

That's the proof I care about most —
my own body, my own results, every single day.

Link in bio if you want to try what I can't stop drinking.

---

### Hashtags
#thepowercoffee #founderstory #functionalcoffee #cleanenergy #morningritual #biohacking #nocrash #powercoffee #disciplineispower #morningroutine #performancefuel #thefirstwin

---

## X.COM
### Post
I've been drinking my own formula every single day for 550 days. Not as a test. Because I haven't found anything better.

---

### Thread
Post 1: I've been drinking my own formula every single day for 550 days. Not as a test. Because I haven't found anything better.

Post 2: I built Power Coffee because I was tired of the options. Pre-workouts that made me anxious. Energy drinks that crashed me by noon. Coffee that just wasn't enough for the kind of days I was trying to have.

Post 3: So I spent months researching. Fed ingredient studies into AI. Tested 5 versions on myself and real people. Dialed in 11 ingredients — taurine, matcha, pea protein, ginkgo — around a clean caffeine base. ~175mg. No sugar. No junk.

Post 4: Day 550 feels the same as day 1. Except now I know it wasn't luck. The formula works because the ingredients are doing real things — not just masking fatigue with a spike.

Post 5: If you've ever built something you actually use every day, you know that's the only proof that matters. Try it yourself: [link]

---

## LINKEDIN
### Post
550 days ago I started drinking a formula I built from scratch.

I didn't know if it would work long-term. I just knew the alternatives weren't good enough.

Most energy products solve one problem and create two more. Spike and crash. Focus and anxiety. Convenience and garbage ingredients.

I wanted something that fit the way I actually live — early mornings, long work blocks, four training sessions a week, a family to show up for.

So I built it. Tested it. Refined it. And kept drinking it.

550 days later, I haven't switched. I haven't needed to.

There's a version of founder-market fit that goes beyond demographics and addressable markets. It's when you are the problem you're solving.

I'm still the customer I built this for. That hasn't changed.

What's the thing you've built that you'd use even if you didn't own it?

---

## TELEGRAM
### Message
Quick one for you — I've been drinking the same formula I built for 550 straight days now. Not because I have to. Because it genuinely works better than anything else I've tried.

If you've been on the fence, that's the most honest pitch I've got. A founder who still can't put it down after a year and a half.

Grab it here: [link]

---

## SHOPIFY BLOG
### Title
Why I Still Drink My Own Coffee Formula 550 Days After Building It

### Body

## The Founder Who Couldn't Find a Better Option

Most founders build products for a market.

I built Power Coffee because I was the market — and nothing out there was doing the job.

I needed clean energy that lasted through long work blocks, early training sessions, and evenings when my family needed me present. What I kept finding were products that either spiked and crashed, wired me with anxiety, or required a 12-step supplement stack just to get through a Tuesday.

## What 550 Days of Daily Use Actually Proves

I've been drinking the same formula every single morning for over 550 days. That's not a marketing number. It's a personal one.

The question I kept asking myself during development was simple: would I drink this even if I didn't own the brand? The answer had to be yes before I'd put it in front of anyone else.

## What's Inside the Formula — And Why It Holds Up

Power Coffee combines ~175mg of clean caffeine with matcha for sustained release, taurine as a neuromodulator, pea protein to stabilize blood sugar, and ginkgo biloba for cerebral blood flow support.

Together, they address the core failure of regular coffee: the spike without the structure.

## The Real Test

The real test of any energy product isn't how you feel at 8am. It's how you feel at 2pm. For 550 days, the answer has been: still sharp, still steady, no crash.

That's why I keep drinking it. And why I think you will too.

**Try The Power Coffee →** [product link]

---

### Image Prompt
A man in his mid-30s standing in a dim garage doorway at dawn, wearing cycling kit, holding a travel mug with both hands, road bike visible behind him leaning against the wall. Warm golden light spilling through the open door onto a concrete floor. A matte black bag of coffee product sits on a wooden shelf just inside the frame. The man is looking forward with quiet focus, not at the camera. Cinematic depth of field, warm espresso and gold tones, no text in frame. 4:5 portrait orientation. Shot on 35mm, natural light.

---

## HIGGSFIELD (Story Image)
### Model
FLUX.2 Pro (image)

### Aspect Ratio
9:16 (Stories)

### Prompt
A man in his late 30s walking through an open garage door at pre-dawn, wearing cycling kit, holding a matte black travel mug in one hand, road bike silhouetted in the background. Warm amber light pours through the garage opening onto a dark concrete floor, creating a strong high-contrast rim light around the figure. The scene feels purposeful and cinematic — like the first frame of a documentary. Matte black bag of coffee product barely visible on a shelf inside. Deep shadows in the upper frame, warm gold light in the lower half. No text, no logos visible in frame. Ultra-realistic, film grain texture, 9:16 vertical portrait, Kodak cinematic tone.

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
const SLIDES = [{
  id: 1,
  slideType: "hook",
  overline: "550+ DAYS IN",
  headline: "I DRINK MY\nOWN PRODUCT\nDAILY",
  subtext: "Here's what changed.",
  accent: "BROWN",
  bg: "BLACK",
  textColor: "CREAM",
  poll: {
    question: "Would you try it?",
    optionA: "YES, ALREADY ON IT",
    optionB: "NOT YET"
  }
}
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

> **Instructions:** Paste into Figma → Plugins → Scripter → Run. Export each frame at 1x as PNG → save as `story.jpg` in today's folder.
