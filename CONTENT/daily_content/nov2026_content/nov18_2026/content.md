# Power Coffee — Content for November 18, 2026
**Pillar:** P3 — FOUNDER PROOF | **Day:** Wednesday | **Image set:** C4 or E3

---
## APPROVAL
- [ ] APPROVED

---

---

## INSTAGRAM
### Story Copy
STILL ON YOUR THIRD CUP?

Here's what 5am actually looks like at my house.

Sticker: Poll — "Coffee #1, #2, or #3 right now?" (Options: Just started / Already on #2 / Lost count)

### Caption
5:10am. Garage door open, bike waiting, legs still half asleep.

This is the part nobody posts. Not the finish line. The part where you have to show up before you feel like it.

Same thing I tell people about the afternoon. You don't need a third cup to push through. You need one thing that actually carries you.

Not intended to diagnose, treat, cure, or prevent any disease.

### Hashtags
#morningroutine #founderlife #disciplineoverfeelings #buildinginpublic #cleanenergy #morningritual #capecod #showup #ironmantraining #realtalk

---

## X.COM
### Post
5:10am, garage door open, half the neighborhood still asleep. Nobody tells you that showing up before you feel like it is the whole job. Same rule applies at 2pm. One scoop, not a third cup.

### Thread
Post 1: I used to think discipline was a mindset. Turns out it's just a garage door opening at the same time every day.
Post 2: Year two of building this company, I still don't "feel ready" most mornings. I get up anyway. That's the actual skill nobody sells you.
Post 3: Same thing happens to our customers at 2pm. They don't lack willpower. They lack a system that carries them through without a third cup.
Post 4: That's the whole bet behind Power Coffee: one scoop in your existing coffee, built to carry the afternoon instead of patching it.
Post 5: If your 2pm looks like my 5am feels, start here: https://thepowercoffee.com/pages/betterday

---

## LINKEDIN
### Post
5:10am. Garage door open. Bike in the driveway. I did not want to be there.

I've learned that most of what people call motivation is just a decision made the night before, repeated enough times that it stops feeling like a decision.

I see the same pattern in our customers. The 2pm crash isn't a willpower failure. It's a system failure — nothing in place to carry the afternoon, so they reach for a third cup and hope.

Building Power Coffee taught me the fix is never "try harder." It's "build the thing that shows up for you before you have to decide."

That's as true for a training plan as it is for a formula.

What's the one system you built that replaced willpower for you?

---

## WHATSAPP
### Message
Quick one from me this morning — garage door up at 5:10am, half asleep, bike waiting. Some days discipline just looks like showing up before you feel like it. Same logic applies to your afternoon: one scoop beats a third cup every time. Hope your Wednesday is a good one.

---

## HIGGSFIELD (Story Image)
### Model
FLUX.2 Pro (image)

### Aspect Ratio
9:16 (Stories)

### Prompt
Early dawn garage scene, cool blue-grey pre-sunrise light spilling through an open garage door onto a road bike leaning against the wall, a man's silhouette in cycling kit walking past mid-stride toward the light, motion blur on his back leg, warm interior lamp glow contrasting the cold morning outside, moody cinematic documentary photography, shallow depth of field, grainy film texture, high contrast between warm interior and cool exterior, vertical composition with open negative space in the upper third, no text, no logos

---

## REELS — Founder Vlog Script
**Series:** Building Power Coffee — Ep. 20
**Beat:** The 5am discipline thread meets a real supplier number this week
**Title formula:** Why I almost switched ginkgo suppliers over 3 cents | 5am training week
**Duration:** 35s · **Setting:** Garage, bike against the wall, Leo in cycling kit, phone propped on a shelf

**HOOK (0-3s, text on screen + spoken):**
"I almost switched suppliers over three cents a unit."

**BODY (speak exactly this):**
"This week our ginkgo supplier raised the price. Three cents a serving. Doesn't sound like much until you multiply it by every bag we ship. I spent two days getting quotes from two other suppliers, cheaper, but neither one had the same certificate of analysis we trust. I stayed. Paid the three cents. Some decisions aren't about the math, they're about what you're willing to protect. Same reason I'm out here at 5am before a ride I don't feel like doing. The easy version is never the one that holds up."

**CTA (last 5s):**
"Follow the build. What's a three-cent decision you've made that was actually about something bigger?"

**B-ROLL:** Leo wheeling bike out of garage, close on ginkgo supplier email/invoice on laptop screen (blurred numbers ok), hand scooping Power Coffee pouch into travel mug before the ride

**CAPTION:** Three cents a serving. That's what almost moved us to a cheaper supplier this week. Here's why we didn't. Ep. 20 — Building Power Coffee
#buildinginpublic #founderstory #supplychain #cleanenergy #capecod

**ON-SCREEN TEXT:** 0:02 "3 cents a serving" / 0:15 "Cheaper ≠ better CoA" / 0:30 "We stayed."

---

## SCIENCE NOTE — Founder Interview Prep (not for publishing)
**Ingredient / mechanism:** Ginkgo biloba extract — flavonoid glycosides and terpene lactones
**Interview angle context:** 207mg per 10g serving
Ginkgo biloba's standardized extracts are typically characterized by two active fractions: flavonoid glycosides (quercetin, kaempferol, isorhamnetin derivatives) and terpene lactones (ginkgolides A, B, C and bilobalide). The flavonoid glycosides act primarily as free-radical scavengers, reducing oxidative stress in vascular endothelial tissue. The terpene lactones, particularly the ginkgolides, are platelet-activating factor (PAF) antagonists, which is thought to contribute to improved microcirculatory blood flow. Bilobalide additionally appears to have a protective effect on mitochondrial function under metabolic stress. Clinically, standardized extracts (commonly EGb 761) dosed around 120-240mg/day have been studied for associations with cognitive performance and peripheral circulation in adults, though effect sizes in healthy (non-impaired) populations are modest and heterogeneous across trials.
**Reference:** Kennedy DO, Scholey AB, Wesnes KA. "Modulation of cognition and mood following administration of single doses of Ginkgo biloba, ginseng, and a ginkgo/ginseng combination to healthy young adults." Physiol Behav. 2002;75(5):739-751. PMID: 12099852
**Interview angle:** Ginkgo's role here is about supporting healthy circulation and reducing oxidative load, not a cognitive enhancer claim — results vary by individual and this isn't intended to diagnose, treat, cure, or prevent any disease.

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
const SLIDES = [{ id: 1, slideType: "hook", overline: "STILL ON YOUR THIRD CUP", headline: "5AM LOOKS\nLIKE THIS\nAT MY HOUSE", subtext: "Garage door open, bike waiting, legs still half asleep. You don't need a third cup. You need one thing that actually carries you.", accent: "BROWN", bg: "BLACK", textColor: "CREAM" }
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
{"story": {"prompt": "Early dawn garage scene, cool blue-grey pre-sunrise light spilling through an open garage door onto a road bike leaning against the wall, a man's silhouette in cycling kit walking past mid-stride toward the light, motion blur on his back leg, warm interior lamp glow contrasting the cold morning outside, moody cinematic documentary photography, shallow depth of field, grainy film texture, high contrast between warm interior and cool exterior, vertical composition with open negative space in the upper third, no text, no logos\n\n---", "text_overlay": "I almost switched suppliers over three cents a unit."}, "carousel": [{"prompt": "Early dawn garage scene, cool blue-grey pre-sunrise light spilling through an open garage door onto a road bike leaning against the wall, a man's silhouette in cycling kit walking past mid-stride toward the light, motion blur on his back leg, warm interior lamp glow contrasting the cold morning outside, moody cinematic documentary photography, shallow depth of field, grainy film texture, high contrast between warm interior and cool exterior, vertical composition with open negative space in the upper third, no text, no logos\n\n---", "text_overlay": "I almost switched suppliers over three cents a unit."}]}
```
