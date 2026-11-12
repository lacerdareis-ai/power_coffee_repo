# Power Coffee — Content for November 12, 2026
**Pillar:** P5 — SOCIAL PROOF | **Day:** Thursday | **Image set:** D1 or D3

---
## APPROVAL
- [x] APPROVED

---

---

## INSTAGRAM
### Story Copy
[9:16 Story frame. "STILL CRASHING AT 2PM?" Subtext: Real mornings, real routines, one scoop at a time. Sticker: Poll — "Does your afternoon slump hit before or after lunch?"]

### Caption
Real mornings. Real people. Real afternoons that don't fall apart.

This week we got a few photos from people stirring one scoop into their regular coffee before the day gets loud. No stock photos. No actors. Just the routine, working.

Renata told us she went for her morning run, and skipped the usual mid-morning crash that used to follow. Individual experiences. Results vary.

Send us a photo of your morning cup. We might feature you next.

www.thepowercoffee.com

### Hashtags
#functionalcoffee #cleanenergy #morningroutine #realpeople #afternoonslump #biohacking #powercoffee #thefirstwin #nocrash #communityovereverything

---

## X.COM
### Post
Renata told us she skipped her usual mid-morning crash after her morning run. One scoop in her regular coffee, nothing else changed. Individual experiences, results vary. Send us your morning cup. www.thepowercoffee.com

### Thread
Post 1: We don't pay for reviews. We just ask people to send us a photo of their morning cup. Here's why that matters more than any ad we could run.

Post 2: Renata runs in the morning. She added one scoop to her regular coffee before heading out. Said the usual mid-morning crash just didn't show up that day.

Post 3: Rita's been doing it daily for weeks now. Says it's just part of her routine at this point, more energy, better disposition. Individual experiences, results vary.

Post 4: This is the whole thesis of Power Coffee. Not a new coffee. Not a replacement ritual. One scoop into the coffee you already make.

Post 5: If you've got a morning cup story, send it. We feature real ones. www.thepowercoffee.com

---

## LINKEDIN
### Post
"I'll do it when I feel inspired" loses to "I'll do it Tuesday at 7am."

The psychologist Robert Boice studied academics who struggled to write. The ones on a fixed schedule wrote several times more, and had more new ideas, than the ones who waited for inspiration.

Teresa Amabile found the same thing from the other side: after reading about 12,000 work diaries, the biggest boost to people's day was making small progress on work that mattered.

Progress makes the motivation. Not the other way around.

---

## WHATSAPP
### Message
Hey, quick one. We've been collecting real photos of people's morning cups this week, Renata's post-run coffee, Rita's daily routine. If you've got a morning ritual with your scoop in it, send us a pic. We love featuring real mornings over anything staged. www.thepowercoffee.com

---

## HIGGSFIELD (Story Image)
### Model
FLUX.2 Pro (image)

### Aspect Ratio
9:16 (Stories)

### Prompt
A candid overhead shot of a kitchen table at early morning, a smartphone lying face-up showing a blurred-out photo being texted, next to a single mug catching warm window light, a folded napkin and a set of keys nearby suggesting someone about to leave for the day. Warm cream and espresso-brown tones with a subtle gold highlight from the sunrise. Shallow depth of field, slightly grainy candid phone-photo aesthetic, not studio-polished. Negative space in the lower third for text overlay. No text in image, no readable content on the phone screen. --ar 9:16

---

## REELS — Founder Vlog Script
**Series:** Building Power Coffee — Ep. 19
**Beat:** Social proof week — real customer photos coming in unprompted
**Title formula:** Why I stopped chasing influencers | What Renata's photo taught me about trust
**Duration:** 35s · **Setting:** Leo in his kitchen, morning light, phone in hand showing a text thread (screen not legible to camera)

**HOOK (0-3s, text on screen + spoken):**
"Renata sent me this and I almost didn't believe it."

**BODY (speak exactly this):**
"Last week a customer texted me a photo of her coffee before her morning run. No ask, no discount code, she just said the usual crash after didn't happen that day. I've spent four months trying to land influencer deals. This did more. We're not a brand with a big budget for ambassadors yet. We're a brand where the first fifty fans actually talk to us. That's the whole strategy right now. Individual results vary, but this is why I still answer every DM myself, even at five in the morning before my run."

**CTA (last 5s):**
"Send me your morning cup. I read every one."

**B-ROLL:** Leo holding phone with blurred text thread visible, Leo pouring one scoop into his own mug mid-conversation, Leo lacing up running shoes by the front door

**CAPTION:** Real people send real photos. That's the whole strategy right now. Send us yours, we read every one.
#buildinginpublic #realcustomers #powercoffee #founderlife #morningritual
Ep. 19 — Building Power Coffee

**ON-SCREEN TEXT:**
0:00 "She sent this unprompted"
0:12 "No ad. No code. Just a text."
0:28 "Send me yours."

---

## SCIENCE NOTE — Founder Interview Prep (not for publishing)
**Ingredient / mechanism:** Taurine as a cellular osmolyte and cytoprotective modulator
Taurine is one of the most abundant free amino acids in excitable tissue (brain, heart, skeletal muscle), but it is not metabolized for energy and does not act as a classical neurotransmitter. Its primary mechanistic role is as an organic osmolyte: it helps regulate cell volume and ionic balance under metabolic stress, which is relevant during sustained physical or cognitive exertion when cells face osmotic and oxidative load. Taurine also modulates intracellular calcium handling in cardiac and skeletal muscle, supporting contractile function, and has demonstrated antioxidant-adjacent effects by stabilizing mitochondrial membranes and reducing reactive oxygen species accumulation during exertion. At 2.1g per serving, Power Coffee's dose sits within ranges studied for exercise performance and recovery support, though taurine's reported "calming" reputation is more accurately described as a stabilizing effect on cell excitability rather than sedation.
**Reference:** Schaffer SW, Jong CJ, Ito T, Azuma J. "Role of taurine in the pathologies of the metabolic syndrome." European Journal of Pharmacology, 2014. PMID: 24631240
**Interview angle:** Taurine may help support cellular resilience and muscle function during exertion — it's a stabilizer, not a stimulant, and individual response varies.

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
const SLIDES = [{ id: 1, slideType: "hook", overline: "REAL MORNINGS, REAL PEOPLE", headline: "STILL CRASHING\nAT 2PM?", subtext: "Real mornings, real routines, one scoop at a time.", accent: "BROWN", bg: "BLACK", textColor: "CREAM" }
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
{"story": {"prompt": "A candid overhead shot of a kitchen table at early morning, a smartphone lying face-up showing a blurred-out photo being texted, next to a single mug catching warm window light, a folded napkin and a set of keys nearby suggesting someone about to leave for the day. Warm cream and espresso-brown tones with a subtle gold highlight from the sunrise. Shallow depth of field, slightly grainy candid phone-photo aesthetic, not studio-polished. Negative space in the lower third for text overlay. No text in image, no readable content on the phone screen. --ar 9:16\n\n---", "text_overlay": "Renata sent me this and I almost didn't believe it."}, "carousel": [{"prompt": "A candid overhead shot of a kitchen table at early morning, a smartphone lying face-up showing a blurred-out photo being texted, next to a single mug catching warm window light, a folded napkin and a set of keys nearby suggesting someone about to leave for the day. Warm cream and espresso-brown tones with a subtle gold highlight from the sunrise. Shallow depth of field, slightly grainy candid phone-photo aesthetic, not studio-polished. Negative space in the lower third for text overlay. No text in image, no readable content on the phone screen. --ar 9:16\n\n---", "text_overlay": "Renata sent me this and I almost didn't believe it."}]}
```
