# Power Coffee — Content for November 19, 2026
**Pillar:** P5 — SOCIAL PROOF | **Day:** Thursday | **Image set:** D1 or D3

---
## APPROVAL
- [ ] APPROVED

---

---

## INSTAGRAM
### Story Copy
STILL LOSING THE AFTERNOON?

Real people, real mornings. Swipe up and see who showed up Saturday.

Sticker: Poll — "Which cup are you today?" Options: "Steady" / "Crashing by 2"

### Caption
Saturday's Power Morning turned into exactly what we hoped for: real faces, real cups, real conversation.

No script. Just people stopping by, saying hi, and starting their day a little steadier.

This is why we do it in person, not just online.

Thank you to everyone who came out. Come say hi next time.

www.thepowercoffee.com

### Hashtags
#powercoffee #thefirstwin #capecod #morningroutine #cleanenergy #community #functionalcoffee #realpeople

---

## X.COM
### Post
Saturday's Power Morning: real cups, real people, zero scripts. This is the part of building a brand you can't fake. Come say hi next time. www.thepowercoffee.com

### Thread
Post 1: We didn't plan a "content moment" Saturday. We just showed up at the cafe with scoops and said hi to people.
Post 2: Some had never heard of us. Some came back for round two. A few told us about their own 2pm crash before we said a word.
Post 3: That's the part that gets me. People volunteering their own afternoon story, unprompted, just from one conversation.
Post 4: That's the whole bet behind Power Coffee: meet people where their day actually breaks down, not where a feed algorithm says it should.
Post 5: Next Power Morning is coming. Want in? www.thepowercoffee.com

---

## LINKEDIN
### Post
Saturday morning, a folding table, and a bag of scoops.

That was the whole setup for our latest Power Morning.

No ad spend. No influencer. Just people walking up, grabbing their regular coffee order, and letting us stir a scoop in.

A few told us about their own afternoon crash before we even explained what we do. That's the moment that stays with me, people recognizing themselves before the pitch.

Building a brand this way is slower. It is also the only way I know to actually earn trust instead of renting attention.

Anyone else building something the slow, in-person way right now? What's working for you?

---

## WHATSAPP
### Message
Saturday's Power Morning was a good one. Real people, real cups, a few honest conversations about the afternoon crash before we even said a word. If you were there, thank you. If you weren't, the next one is coming soon and we'd love to see you. www.thepowercoffee.com

---

## HIGGSFIELD (Story Image)
### Model
FLUX.2 Pro (image)

### Aspect Ratio
9:16 (Stories)

### Prompt
Candid vertical photo at a small neighborhood cafe on a crisp fall morning, Cape Cod light. A man behind a simple folding table handing a small paper cup to a woman mid-laugh, genuine unposed moment, other people blurred in the background holding their own coffee cups. Warm golden-hour light mixing with the cafe's interior glow. Muted cream, espresso brown, and gold color grading. Shallow depth of field, slightly grainy real-photo texture, not overly polished. Negative space kept quiet in the top 14% and bottom 25% of the frame for UI and text overlay. No text in image. Vertical 9:16 composition.

visual_style: UGC-phone

---

## REELS — Founder Vlog Script
**Series:** Building Power Coffee — Ep. 20
**Beat:** Saturday Power Morning recap, moving from "event" to "ritual"
**Title formula:** What I learned from a folding table | Saturday mornings are non-negotiable now
**Duration:** 35s · **Setting:** Leo walking into frame outside the partner cafe, Monday morning light, casual

**HOOK (0-3s, text on screen + spoken):**
"Saturday, a folding table, and twenty-something cups of coffee."

**BODY (speak exactly this):**
"That's the whole setup for our Power Morning this weekend. No ad budget behind it, just us showing up at the cafe and stirring a scoop into people's regular order. What got me was how many people told me about their own 2pm crash before I even explained what we do. Nobody taught me that this is how trust actually gets built, one cup, one conversation at a time. I used to think growth meant bigger posts. Now I think it means smaller rooms."

**CTA (last 5s):**
"Next Power Morning is coming. Follow along and I'll post the date."

**B-ROLL:** wide shot of the cafe exterior in morning light, hands stirring a scoop into a cup, Leo greeting someone and shaking hands
**CAPTION:** Twenty-something cups, one folding table, zero scripts. This is what building Power Coffee actually looks like some weekends. Ep. 20 — Building Power Coffee
#powercoffee #buildinginpublic #capecod #foundervoice #thefirstwin
**ON-SCREEN TEXT:** 0s "A folding table." / 15s "They told me about their crash first." / 30s "Smaller rooms > bigger posts."

---

## SCIENCE NOTE — Founder Interview Prep (not for publishing)
**Ingredient / mechanism:** Taurine as an osmolyte and cytoprotective modulator
Taurine is one of the most abundant free amino acids in excitable tissue, including skeletal muscle and the central nervous system, where it functions primarily as an organic osmolyte, helping cells regulate volume and resist osmotic stress during exertion. It also acts as a membrane stabilizer, modulating calcium flux in cardiac and skeletal muscle cells, which has been linked to improved contractile function and reduced oxidative stress during exercise. In the CNS, taurine interacts weakly with GABA-A and glycine receptors, producing a mild inhibitory tone that may blunt overexcitation without sedation, distinct from caffeine's stimulant action. At the 2.1g dose in Power Coffee, this sits within ranges studied in sports nutrition literature, though most trials use isolated taurine rather than a caffeine-taurine combination, so stacked effects remain an open question.
**Reference:** da Silva et al., "Taurine supplementation decreases oxidative stress and modulates intracellular calcium cycling," Amino Acids, 2016 [VERIFY CITATION]
**Interview angle:** Taurine may support cellular resilience during exertion and takes the edge off overstimulation, it does not stimulate on its own, that job belongs to caffeine.

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
const SLIDES = [{ id: 1, slideType: "hook", overline: "STILL LOSING THE AFTERNOON", headline: "REAL PEOPLE\nREAL MORNINGS\nREAL CUPS", subtext: "Swipe up and see who showed up Saturday.", accent: "BROWN", bg: "BLACK", textColor: "CREAM" }
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
{"story": {"prompt": "Candid vertical photo at a small neighborhood cafe on a crisp fall morning, Cape Cod light. A man behind a simple folding table handing a small paper cup to a woman mid-laugh, genuine unposed moment, other people blurred in the background holding their own coffee cups. Warm golden-hour light mixing with the cafe's interior glow. Muted cream, espresso brown, and gold color grading. Shallow depth of field, slightly grainy real-photo texture, not overly polished. Negative space kept quiet in the top 14% and bottom 25% of the frame for UI and text overlay. No text in image. Vertical 9:16 composition.\n\nvisual_style: UGC-phone\n\n---", "text_overlay": "Saturday, a folding table, and twenty-something cups of coffee."}, "carousel": [{"prompt": "Candid vertical photo at a small neighborhood cafe on a crisp fall morning, Cape Cod light. A man behind a simple folding table handing a small paper cup to a woman mid-laugh, genuine unposed moment, other people blurred in the background holding their own coffee cups. Warm golden-hour light mixing with the cafe's interior glow. Muted cream, espresso brown, and gold color grading. Shallow depth of field, slightly grainy real-photo texture, not overly polished. Negative space kept quiet in the top 14% and bottom 25% of the frame for UI and text overlay. No text in image. Vertical 9:16 composition.\n\nvisual_style: UGC-phone\n\n---", "text_overlay": "Saturday, a folding table, and twenty-something cups of coffee."}]}
```
