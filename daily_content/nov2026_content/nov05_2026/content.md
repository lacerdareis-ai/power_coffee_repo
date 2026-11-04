# Power Coffee — Content for November 05, 2026
**Pillar:** P5 — SOCIAL PROOF | **Day:** Thursday | **Image set:** D1 or D3

---
## APPROVAL
- [ ] APPROVED

---

---

## INSTAGRAM
### Story Copy
STILL CRASHING AT 2PM?

You're not the only one. Tap below and tell us when your afternoon falls apart.

Sticker: Poll — "Do you crash by 2pm? YES / NO"

### Caption
Renata told us she didn't feel the usual mid-morning crash after her run.

Welma said the aroma pulled her in, but it was the focus through the day that kept her coming back.

We don't write these. People send them to us.

If your afternoon has a breaking point, tell us when it hits. We read every reply.

Individual experiences. Results vary.

www.thepowercoffee.com

### Hashtags
#cleanenergy #morningroutine #realtalk #nocrash #focusfuel #powercoffee #thefirstwin #energywithoutthejitters #afternoonslump #biohacking

---

## X.COM
### Post
"I didn't feel the usual crash of energy mid-morning." That's Renata, after her morning run. Not a script. A real reply. When does your afternoon usually break? https://thepowercoffee.com/pages/betterday

### Thread
Post 1: We asked people what actually changes when the 2pm crash doesn't happen. The answers surprised us.
Post 2: Renata runs in the morning. She told us the usual mid-run, mid-morning fade just didn't show up.
Post 3: Welma said the first thing she noticed was the aroma. The second thing was that her focus held steady for hours after.
Post 4: We didn't write any of this. These are unedited replies from real mornings.
Post 5: If your afternoon has a breaking point, we want to hear it. https://thepowercoffee.com/pages/betterday

---

## LINKEDIN
Last week someone replied to one of our posts with a single line: "I didn't feel the usual crash of energy mid-morning."

That's it. No pitch. No ask. Just a person telling us something changed in her day.

We get a handful of these a week now. Not thousands. A handful. But they're real, and we read every one out loud in our Teams channel before we do anything else that day.

Early on, I thought growth meant volume. More posts, more ads, more reach.

What actually moved me was one woman telling me her run felt different.

I'm learning that the smallest, most specific piece of feedback is worth more than any metric on a dashboard.

What's the smallest piece of feedback that's ever changed how you think about your work?

---

## TELEGRAM
Quick one for you today. A customer named Renata told us she didn't feel her usual mid-morning crash after a run — first time that's happened in a while for her. Small thing, but it made our day. What time does your afternoon usually start to slip? Tell us, we're genuinely curious.

---

## HIGGSFIELD (Story Image)
### Model
FLUX.2 Pro (image)

### Aspect Ratio
9:16 (Stories)

### Prompt
A woman in her late 30s mid-stride on a quiet morning run, captured from a low angle against a rising sun, strong motion blur in the background trees, her expression calm and focused, breath visible in cool morning air, warm gold rim light catching her shoulder and jaw, muted cream and espresso color grade, shallow depth of field, authentic documentary photography feel, negative space in the upper third of the frame for text overlay, no text in image, high contrast, vertical composition. --ar 9:16

---

## REELS — Founder Vlog Script
**Series:** Building Power Coffee — Ep. 18
**Beat:** Social proof / reading real customer replies on camera
**Title formula:** Reading our first unscripted customer replies | the week I stopped chasing metrics
**Duration:** 35s · **Setting:** Leo at his kitchen counter, morning light, phone in hand, laptop closed beside him

**HOOK (0-3s, text on screen + spoken):**
"A customer said something last week that stopped me."

**BODY (speak exactly this):**
"I used to check our analytics dashboard first thing every morning. Last week I stopped. A woman named Renata replied to one of our posts and said she didn't feel her usual crash after a morning run. That's it. No ask, nothing fancy. I read it out loud to my brother Lucas before I even opened my laptop. We didn't write it, we didn't ask for it, she just told us. That one line meant more to me than any reach number this month. This cup on my counter right now is the same one she's talking about."

**CTA (last 5s):**
"Tell me in the comments — when does your afternoon usually break?"

**B-ROLL:** Leo reading phone at counter, hand scooping into mug (single mug, incidental), Leo walking out the door with travel mug
**CAPTION:** A customer reply stopped me mid-scroll last week. Not a metric. A sentence. Ep. 18 — Building Power Coffee
#buildingpowercoffee #founderjourney #realtalk #cleanenergy #morningroutine

**ON-SCREEN TEXT:**
0-3s: "A customer said something that stopped me"
15s: "We didn't ask for it. She just told us."
30s: "When does your afternoon break?"

---

## SCIENCE NOTE — Founder Interview Prep (not for publishing)
**Ingredient / mechanism:** Taurine as an osmolyte and cytoprotective modulator
Taurine is a beta-amino sulfonic acid present at roughly 2.1g per serving in Power Coffee's formula. Unlike classical neurotransmitters, taurine doesn't act primarily through a dedicated high-affinity receptor; its functional role is largely as an organic osmolyte, regulating cell volume and intracellular ion balance, particularly in skeletal muscle, cardiac tissue, and the central nervous system. It also acts as a cytoprotective agent by stabilizing mitochondrial membrane potential and buffering calcium overload during metabolic stress, which is part of why it shows up so heavily in exercise physiology research — tissues under exertion see less oxidative and osmotic strain when taurine availability is adequate. In the context of a caffeinated beverage, taurine's relevance is less about acute stimulation and more about supporting cellular resilience during the sustained physical or cognitive demand that follows caffeine intake. It also has modest interaction with GABA-A receptors at higher concentrations, contributing to a calming counterbalance rather than added stimulation.
**Reference:** Schaffer SW, Jong CJ, Ito T, Azuma J. "Role of taurine in the pathologies of the metabolic syndrome." Diabetol Metab Syndr. 2014. PMID: 25530822
**Interview angle:** Taurine doesn't stimulate — it supports the cells doing the work while you're stimulated. That distinction matters more than people think.

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
const SLIDES = [{ id: 1, slideType: "hook", overline: "STILL CRASHING?", headline: "STILL CRASHING\nAT 2PM?", subtext: "Tell us when your afternoon falls apart. We read every reply.", accent: "BROWN", bg: "BLACK", textColor: "CREAM" }
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
{"story": {"prompt": "A woman in her late 30s mid-stride on a quiet morning run, captured from a low angle against a rising sun, strong motion blur in the background trees, her expression calm and focused, breath visible in cool morning air, warm gold rim light catching her shoulder and jaw, muted cream and espresso color grade, shallow depth of field, authentic documentary photography feel, negative space in the upper third of the frame for text overlay, no text in image, high contrast, vertical composition. --ar 9:16\n\n---", "text_overlay": "A customer said something last week that stopped me."}, "carousel": [{"prompt": "A woman in her late 30s mid-stride on a quiet morning run, captured from a low angle against a rising sun, strong motion blur in the background trees, her expression calm and focused, breath visible in cool morning air, warm gold rim light catching her shoulder and jaw, muted cream and espresso color grade, shallow depth of field, authentic documentary photography feel, negative space in the upper third of the frame for text overlay, no text in image, high contrast, vertical composition. --ar 9:16\n\n---", "text_overlay": "A customer said something last week that stopped me."}]}
```
