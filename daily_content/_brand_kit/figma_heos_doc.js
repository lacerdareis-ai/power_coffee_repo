// ============================================================
// HE-OS — High Energy Operational System
// Figma Scripter document generator
// Plugins > Scripter > Run
//
// Generates 10 slides (1440 × 900) — one per section:
//   01 · Cover
//   02 · Architecture (3-layer diagram)
//   03 · Content Flow
//   04 · Cron Schedule (daily timeline)
//   05 · Platforms
//   06 · Skills
//   07 · Credentials Map
//   08 · Alerting Rules
//   09 · Known Limits
//   10 · Cloud Routines
// ============================================================

const W = 1440;
const H = 900;
const GAP = 60;

// ── COLORS ───────────────────────────────────────────────────
const C = {
  bg:       { r: 0.09, g: 0.08, b: 0.07 },   // #171412 Deep Espresso
  bg2:      { r: 0.18, g: 0.16, b: 0.14 },   // #2E2824 Dark Charcoal
  bg3:      { r: 0.13, g: 0.12, b: 0.10 },   // card surface
  gold:     { r: 0.85, g: 0.65, b: 0.20 },   // #D9A633 Golden Energy
  cream:    { r: 0.97, g: 0.94, b: 0.88 },   // #F7F0E0 Warm Cream
  muted:    { r: 0.55, g: 0.50, b: 0.44 },   // muted text
  brown_l:  { r: 0.75, g: 0.48, b: 0.28 },   // Brown Light
  brown:    { r: 0.48, g: 0.24, b: 0.12 },   // Brown Mid
  matcha:   { r: 0.22, g: 0.45, b: 0.30 },   // #38724D
  red:      { r: 0.70, g: 0.22, b: 0.22 },   // error / disabled
  green:    { r: 0.22, g: 0.55, b: 0.30 },   // ok / enabled
  white:    { r: 1.00, g: 1.00, b: 1.00 },
};

// ── FONTS ────────────────────────────────────────────────────
const F = {
  hero:    { family: "Georgia", style: "Bold Italic" },   // big headlines
  h:       { family: "Georgia", style: "Bold" },          // section headlines
  body:    { family: "Georgia", style: "Regular" },       // body copy
  italic:  { family: "Georgia", style: "Italic" },        // taglines, quotes
  label:   { family: "Arial",   style: "Bold" },          // ALL CAPS labels
  small:   { family: "Arial",   style: "Regular" },       // small captions
  mono:    { family: "Courier New", style: "Bold" },      // code / paths
};

// ── HELPERS ──────────────────────────────────────────────────
let slideX = 0;

function newSlide(name) {
  var f = figma.createFrame();
  f.name = name;
  f.resize(W, H);
  f.x = slideX; f.y = 0;
  f.fills = [{ type: "SOLID", color: C.bg }];
  f.clipsContent = true;
  figma.currentPage.appendChild(f);
  slideX += W + GAP;
  return f;
}

function r(p, x, y, w, h, col, op) {
  var el = figma.createRectangle();
  el.x = x; el.y = y; el.resize(w, h);
  el.fills = [{ type: "SOLID", color: col, opacity: op !== undefined ? op : 1 }];
  p.appendChild(el);
  return el;
}

async function t(p, str, x, y, w, size, font, col, align, lineH) {
  await figma.loadFontAsync(font);
  var el = figma.createText();
  el.fontName = font;
  el.characters = str;
  el.fontSize = size;
  el.textAlignHorizontal = align || "LEFT";
  el.fills = [{ type: "SOLID", color: col }];
  el.lineHeight = { unit: "PERCENT", value: (lineH || 1.35) * 100 };
  el.x = x; el.y = y;
  el.resize(w, el.height);
  p.appendChild(el);
  return el;
}

function divLine(p, x, y, w, col, op) {
  r(p, x, y, w, 1, col || C.gold, op || 0.5);
}

function tag(p, label, x, y, bg, textCol) {
  r(p, x, y, label.length * 8 + 24, 28, bg || C.brown, 0.9);
  figma.loadFontAsync(F.label).then(function() {
    var el = figma.createText();
    el.fontName = F.label;
    el.characters = label;
    el.fontSize = 10;
    el.textAlignHorizontal = "CENTER";
    el.fills = [{ type: "SOLID", color: textCol || C.cream }];
    el.letterSpacing = { unit: "PERCENT", value: 15 };
    el.x = x; el.y = y + 8;
    el.resize(label.length * 8 + 24, 28);
    p.appendChild(el);
  });
}

async function card(p, x, y, w, h, title, titleCol) {
  r(p, x, y, w, h, C.bg3);
  r(p, x, y, 3, h, C.gold);
  if (title) await t(p, title, x + 20, y + 18, w - 40, 12, F.label, titleCol || C.muted, "LEFT");
  return { x: x, y: y, w: w, h: h };
}

// diagonal texture lines (subtle)
function texture(p) {
  for (var i = 0; i < 16; i++) {
    var line = figma.createLine();
    line.x = -200 + i * 120; line.y = 0;
    line.resize(H * 1.8, 0);
    line.rotation = -35;
    line.strokes = [{ type: "SOLID", color: C.gold, opacity: 0.025 }];
    line.strokeWeight = 60;
    p.appendChild(line);
  }
}

function slideHeader(p, num, title, sub) {
  r(p, 0, 0, 6, H, C.gold);
  return Promise.all([
    t(p, num, 48, 40, 80, 11, F.label, C.muted),
    t(p, title, 48, 60, W - 120, 42, F.hero, C.cream, "LEFT", 1.0),
    sub ? t(p, sub, 48, 114, W - 120, 14, F.small, C.muted) : Promise.resolve(),
  ]);
}

// ── SLIDE 01 · COVER ─────────────────────────────────────────
async function slide01() {
  var p = newSlide("01 · Cover");
  texture(p);
  r(p, 0, H - 8, W, 8, C.gold);

  await t(p, "HE-OS", 80, 140, 900, 160, F.hero, C.cream, "LEFT", 0.88);
  await t(p, "High Energy Operational System", 84, 320, 900, 28, F.h, C.gold, "LEFT");
  divLine(p, 84, 368, 600, C.gold, 0.6);
  await t(p, "Autonomous Sales & Content Engine  ·  Claude Stack  ·  v2.1 (Jun 2026)", 84, 382, 900, 16, F.small, C.muted);
  await t(p, "The Power Coffee", 84, 430, 400, 14, F.italic, C.brown_l);

  // right column — layer badges
  var badges = [
    ["INTELLIGENCE LAYER", "/brain · /pulse · /lens · /studio · /ads"],
    ["KNOWLEDGE BASE", "Obsidian vault · git-tracked · brain/references"],
    ["AUTOMATION ENGINE", "13 cron jobs · publisher.py · he_common.py"],
  ];
  for (var i = 0; i < badges.length; i++) {
    var bx = W - 520; var by = 200 + i * 140;
    r(p, bx, by, 420, 110, C.bg2);
    r(p, bx, by, 3, 110, C.gold);
    await t(p, badges[i][0], bx + 20, by + 18, 380, 11, F.label, C.gold);
    await t(p, badges[i][1], bx + 20, by + 44, 380, 14, F.body, C.cream, "LEFT", 1.5);
  }

  await t(p, "THE POWER COFFEE  ·  thepowercoffee.com  ·  @powercoffee.ofc", 84, H - 52, 800, 11, F.label, C.muted);
}

// ── SLIDE 02 · ARCHITECTURE ──────────────────────────────────
async function slide02() {
  var p = newSlide("02 · Architecture");
  texture(p);
  await slideHeader(p, "02", "Architecture", "Three layers — Intelligence · Knowledge · Automation");

  var layers = [
    {
      title: "INTELLIGENCE LAYER",
      sub: "~/.claude/plugins/.../skills/",
      col: C.gold,
      items: [
        ["/brain",  "Content strategy, ideas, calendar, hooks, captions"],
        ["/pulse",  "Buyer intel: Amazon/web reviews → pain language"],
        ["/lens",   "Results analyzer: engagement → Winning-Patterns.md"],
        ["/studio", "Visual generator (Higgsfield AI)"],
        ["/ads",    "Meta Ads: campaigns, audiences, creatives, insights"],
      ]
    },
    {
      title: "KNOWLEDGE BASE",
      sub: "Sales_motor/ · Obsidian vault · git-tracked",
      col: C.matcha,
      items: [
        ["brain/references/", "brand.md · content-system.md · market.md"],
        ["daily_content/",    "{mon}{yyyy}_content/{day}/content.md"],
        ["04-Analytics/",     "Winning-Patterns.md · instagram-analytics-*.csv"],
        ["publish_confirm.md","post-publish receipt per day"],
        ["media files",       "carousel_N.jpg · story.jpg · instagram.mp4"],
      ]
    },
    {
      title: "AUTOMATION ENGINE",
      sub: "power_coffee_bot/sales_motor/ · 13 cron jobs",
      col: C.brown_l,
      items: [
        ["generate_content.py", "Claude API → content.md → git push"],
        ["publisher.py",        "X / IG / LinkedIn / TG / WA / Shopify / Email"],
        ["check_approval.py",   "reads [x] APPROVED before publishing"],
        ["m365_mailer.py",      "Resend API → M365 Graph → SMTP fallback"],
        ["_alert.sh",           "failure alerts → ALERT_CHAT_ID only"],
      ]
    },
  ];

  for (var i = 0; i < layers.length; i++) {
    var lx = 80 + i * 440; var ly = 160; var lw = 420; var lh = 680;
    r(p, lx, ly, lw, lh, C.bg2);
    r(p, lx, ly, lw, 4, layers[i].col);
    await t(p, layers[i].title, lx + 20, ly + 22, lw - 40, 11, F.label, layers[i].col);
    await t(p, layers[i].sub, lx + 20, ly + 42, lw - 40, 12, F.small, C.muted);
    divLine(p, lx + 20, ly + 68, lw - 40, layers[i].col, 0.3);

    for (var j = 0; j < layers[i].items.length; j++) {
      var iy = ly + 90 + j * 108;
      r(p, lx + 20, iy, lw - 40, 92, C.bg3);
      r(p, lx + 20, iy, 3, 92, layers[i].col, 0.7);
      await t(p, layers[i].items[j][0], lx + 36, iy + 12, lw - 76, 13, F.mono, layers[i].col, "LEFT");
      await t(p, layers[i].items[j][1], lx + 36, iy + 36, lw - 76, 12, F.body, C.cream, "LEFT", 1.5);
    }
  }
}

// ── SLIDE 03 · CONTENT FLOW ──────────────────────────────────
async function slide03() {
  var p = newSlide("03 · Content Flow");
  texture(p);
  await slideHeader(p, "03", "Content Flow", "From idea to published post to smarter brain");

  // main flow — top row
  var steps = [
    { label: "/brain",          sub: "generates ideas",     x: 60  },
    { label: "generate_content", sub: "5am · Claude API",   x: 280 },
    { label: "content.md",      sub: "saved + git pushed",  x: 500 },
    { label: "Leo reviews",     sub: "Obsidian · approval", x: 720 },
    { label: "publisher.py",    sub: "4am cron",            x: 940 },
  ];

  for (var i = 0; i < steps.length; i++) {
    var s = steps[i];
    r(p, s.x, 180, 180, 88, C.bg2);
    r(p, s.x, 180, 180, 3, C.gold);
    await t(p, s.label, s.x + 12, 195, 156, 13, F.mono, C.gold);
    await t(p, s.sub, s.x + 12, 220, 156, 12, F.small, C.muted);
    if (i < steps.length - 1) {
      await t(p, "→", s.x + 190, 213, 40, 18, F.h, C.gold);
    }
  }

  // platforms fan out
  var platforms = ["X.com", "Instagram", "LinkedIn", "Telegram", "WhatsApp", "Shopify", "Email (Mon)"];
  var fanX = 60;
  var fanY = 400;
  r(p, 940, 268, 2, 100, C.gold, 0.4);  // down arrow from publisher
  await t(p, "↓", 952, 340, 40, 22, F.h, C.gold);
  await t(p, "PUBLISHES TO", 60, 370, 500, 11, F.label, C.muted);

  for (var j = 0; j < platforms.length; j++) {
    r(p, fanX + j * 190, fanY, 170, 56, C.bg2);
    r(p, fanX + j * 190, fanY, 170, 3, C.brown_l);
    await t(p, platforms[j], fanX + j * 190 + 12, fanY + 18, 146, 13, F.label, C.cream);
  }

  // feedback loop
  r(p, 60, 540, 2, 200, C.matcha, 0.5);
  await t(p, "↓", 68, 570, 40, 18, F.h, C.matcha);
  await t(p, "FEEDBACK LOOP", 60, 550, 300, 11, F.label, C.muted);

  var loopSteps = [
    ["fetch_analytics.py", "6am · pulls IG + Shopify data"],
    ["/lens (Sat)",         "engagement data → Winning-Patterns.md"],
    ["/brain update",      "brain references get smarter"],
  ];
  for (var k = 0; k < loopSteps.length; k++) {
    r(p, 100, 580 + k * 100, 340, 74, C.bg2);
    r(p, 100, 580 + k * 100, 3, 74, C.matcha, 0.8);
    await t(p, loopSteps[k][0], 120, 596 + k * 100, 300, 13, F.mono, C.matcha);
    await t(p, loopSteps[k][1], 120, 620 + k * 100, 300, 12, F.small, C.muted);
    if (k < loopSteps.length - 1) await t(p, "↓", 270, 658 + k * 100, 40, 14, F.h, C.matcha);
  }

  // right: key rule callout
  r(p, W - 440, 520, 380, 300, C.bg2);
  r(p, W - 440, 520, 380, 4, C.gold);
  await t(p, "CONTENT NEVER SKIPS THE CHECK", W - 420, 542, 340, 11, F.label, C.gold);
  await t(p, "check_approval.py reads the [x] APPROVED checkbox in content.md before publisher.py fires. If not checked by 4am — nothing posts that day.", W - 420, 568, 340, 14, F.body, C.cream, "LEFT", 1.6);
  divLine(p, W - 420, 650, 340, C.gold, 0.3);
  await t(p, "ALERT ROUTING", W - 420, 668, 340, 11, F.label, C.gold);
  await t(p, "All failures → ALERT_CHAT_ID (Leo DM)\nNever → TELEGRAM_CHAT_ID (group)", W - 420, 692, 340, 13, F.body, C.cream, "LEFT", 1.6);
}

// ── SLIDE 04 · CRON SCHEDULE ─────────────────────────────────
async function slide04() {
  var p = newSlide("04 · Cron Schedule");
  texture(p);
  await slideHeader(p, "04", "Cron Schedule", "13 local jobs · Mac wakes 3:50am daily via pmset");

  var jobs = [
    { time: "03:50", label: "WAKE",             desc: "pmset wakes Mac",                      col: C.muted,   days: "every day" },
    { time: "04:00", label: "PUBLISH",           desc: "run_publish.sh → all platforms",       col: C.gold,    days: "every day" },
    { time: "04:00", label: "LENS",              desc: "run_lens.sh → brain refs update",      col: C.matcha,  days: "Saturday" },
    { time: "05:00", label: "GENERATE",          desc: "run_generate.sh → tomorrow's content", col: C.gold,    days: "every day" },
    { time: "06:00", label: "ANALYTICS",         desc: "run_analytics.sh → IG + Shopify CSVs", col: C.brown_l, days: "every day" },
    { time: "07:00", label: "MORNING BRIEF",     desc: "run_morning_brief.sh → Leo DM",        col: C.brown_l, days: "every day" },
    { time: "08:00", label: "REPORT",            desc: "run_report.sh → Telegram Leo DM",      col: C.brown_l, days: "every day" },
    { time: "08:00", label: "OBSIDIAN",          desc: "run_obsidian_brief.sh → open note",    col: C.muted,   days: "every day" },
    { time: "09:00", label: "REVIEWS",           desc: "run_review_scanner.sh → Leo DM",       col: C.matcha,  days: "every 2d" },
    { time: "09:00", label: "WA BROADCAST",      desc: "run_weekly_broadcast.sh",              col: C.matcha,  days: "Monday" },
    { time: "09:15", label: "WA DIGEST",         desc: "run_biweekly_digest.sh",               col: C.matcha,  days: "Mon biweekly" },
    { time: "10:00", label: "COMPETITORS",       desc: "run_competitor_monitor.sh → Leo DM",   col: C.brown_l, days: "every day" },
    { time: "10:00", label: "CAMPAIGN",          desc: "run_campaign.sh → Resend batch",       col: C.gold,    days: "every day" },
    { time: "*/5m",  label: "STATUS",            desc: "run_status.sh → dashboard JSON",       col: C.muted,   days: "every 5min" },
  ];

  for (var i = 0; i < jobs.length; i++) {
    var col1 = i < 7 ? 80  : 760;
    var row  = i < 7 ? i   : i - 7;
    var jy   = 170 + row * 92;
    var jw   = 640;

    r(p, col1, jy, jw, 74, C.bg2);
    r(p, col1, jy, 3, 74, jobs[i].col);

    await t(p, jobs[i].time,  col1 + 16, jy + 12, 80,  13, F.mono,  C.gold);
    await t(p, jobs[i].label, col1 + 110, jy + 12, 200, 12, F.label, jobs[i].col);
    await t(p, jobs[i].days,  col1 + 460, jy + 12, 160, 11, F.small, C.muted, "RIGHT");
    await t(p, jobs[i].desc,  col1 + 110, jy + 38, 500, 13, F.small, C.muted);
  }
}

// ── SLIDE 05 · PLATFORMS ─────────────────────────────────────
async function slide05() {
  var p = newSlide("05 · Platforms");
  texture(p);
  await slideHeader(p, "05", "Platforms", "7 channels · all dispatched by publisher.py");

  var platforms = [
    { name: "Instagram",   handle: "@powercoffee.ofc", what: "Story · Carousel · Reel",          how: "Manual media drop → auto-post", freq: "daily",   col: C.gold   },
    { name: "X",           handle: "@boosteddays",     what: "1 standalone post/day",            how: "auto · publisher.py",           freq: "daily",   col: C.cream  },
    { name: "LinkedIn",    handle: "Leo Lacerda",      what: "Founder narrative post",           how: "auto · publisher.py",           freq: "daily",   col: C.brown_l},
    { name: "Telegram",    handle: "Better Days group",what: "Community message",                how: "auto · publisher.py",           freq: "daily",   col: C.matcha },
    { name: "WhatsApp",    handle: "broadcast list",   what: "Monday motivation + biweekly",     how: "auto · he_common.py",           freq: "Mon+",    col: C.matcha },
    { name: "Shopify Blog",handle: "thepowercoffee.com","what":"SEO article (300w HTML)",        how: "auto · Tue + Thu only",         freq: "2×/week", col: C.brown_l},
    { name: "Email",       handle: "Resend API",       what: "Newsletter + campaign (8,096)",    how: "auto · Resend · Mon + daily batch","freq":"Mon+", col: C.gold   },
  ];

  var CW = 380; var CH = 220;
  var cols = [80, 480, 880, 1280, 80, 480, 880];
  var rows = [160,160,160,160,410,410,410];

  for (var i = 0; i < platforms.length; i++) {
    var pl = platforms[i];
    var px = cols[i]; var py = rows[i];
    r(p, px, py, CW, CH, C.bg2);
    r(p, px, py, CW, 4, pl.col);
    await t(p, pl.name,   px + 20, py + 22, CW - 40, 20, F.h,     pl.col);
    await t(p, pl.handle, px + 20, py + 50, CW - 40, 13, F.mono,  C.muted);
    divLine(p, px + 20, py + 78, CW - 40, pl.col, 0.3);
    await t(p, pl.what, px + 20, py + 96,  CW - 40, 13, F.body,  C.cream, "LEFT", 1.5);
    await t(p, pl.how,  px + 20, py + 140, CW - 40, 12, F.small, C.muted, "LEFT", 1.5);
    await t(p, pl.freq, px + CW - 80, py + 190, 60, 11, F.label, pl.col, "RIGHT");
  }
}

// ── SLIDE 06 · SKILLS ────────────────────────────────────────
async function slide06() {
  var p = newSlide("06 · Skills");
  texture(p);
  await slideHeader(p, "06", "Skills", "5 Claude Code skills — invoke from any session");

  var skills = [
    {
      cmd: "/brain",  name: "BRAIN",  col: C.gold,
      role: "Content engine",
      desc: "Generates ideas, captions, hooks, and full content calendar. Reads brand.md + content-system.md + market.md. The primary creative driver.",
      trigger: "ideas, content, hook, reel idea, what to post, weekly content",
    },
    {
      cmd: "/pulse",  name: "PULSE",  col: C.matcha,
      role: "Buyer intelligence",
      desc: "Mines Amazon + web reviews for real buyer language. Surfaces pain points, loyalty triggers, objections. Writes to Buyer-Intelligence.md.",
      trigger: "reviews, who is buying, voice of customer, amazon, buyer feedback",
    },
    {
      cmd: "/lens",   name: "LENS",   col: C.brown_l,
      role: "Results loop",
      desc: "Reads published content + engagement data. Extracts what's working. Updates Winning-Patterns.md and brain references. Run every Friday.",
      trigger: "analyze results, what's working, engagement, update patterns, LENS",
    },
    {
      cmd: "/studio", name: "STUDIO", col: C.cream,
      role: "Visual generator",
      desc: "Generates images and videos via Higgsfield AI. Handles carousels, reels, stories, and CTA story images for every content piece.",
      trigger: "generate image, generate video, studio, higgsfield, make the carousel",
    },
    {
      cmd: "/ads",    name: "ADS",    col: C.gold,
      role: "Meta Ads manager",
      desc: "Campaign overview, launch from content.md, optimize budgets, manage audiences (email list + retargeting + LAL), upload creatives, insights → Telegram DM.",
      trigger: "ads, meta ads, campaign, ad performance, boost, audience, retargeting",
    },
  ];

  var SW = 240; var SH = 600;
  for (var i = 0; i < skills.length; i++) {
    var sk = skills[i];
    var sx = 60 + i * (SW + 28);
    r(p, sx, 160, SW, SH, C.bg2);
    r(p, sx, 160, SW, 5, sk.col);
    await t(p, sk.cmd,  sx + 20, 182, SW - 40, 22, F.mono,   sk.col);
    await t(p, sk.name, sx + 20, 214, SW - 40, 32, F.h,      sk.col, "LEFT", 1.0);
    await t(p, sk.role, sx + 20, 256, SW - 40, 13, F.label,  C.muted);
    divLine(p, sx + 20, 284, SW - 40, sk.col, 0.3);
    await t(p, sk.desc, sx + 20, 300, SW - 40, 13, F.body,   C.cream, "LEFT", 1.65);
    divLine(p, sx + 20, 520, SW - 40, sk.col, 0.2);
    await t(p, "TRIGGERS", sx + 20, 536, SW - 40, 10, F.label, C.muted);
    await t(p, sk.trigger, sx + 20, 554, SW - 40, 11, F.small, C.muted, "LEFT", 1.6);
  }
}

// ── SLIDE 07 · CREDENTIALS MAP ───────────────────────────────
async function slide07() {
  var p = newSlide("07 · Credentials (.env)");
  texture(p);
  await slideHeader(p, "07", "Credentials (.env)", "power_coffee_bot/sales_motor/.env · never commit this file");

  var groups = [
    {
      title: "META (Instagram + WhatsApp)",
      col: C.gold,
      keys: [
        ["INSTAGRAM_ACCESS_TOKEN",       "Meta Graph API · expires ~Jul 19 ⚠️"],
        ["INSTAGRAM_BUSINESS_ACCOUNT_ID","IG publishing"],
        ["INSTAGRAM_APP_SECRET",         "appsecret_proof"],
        ["WHATSAPP_ACCESS_TOKEN",        "WhatsApp Business API"],
        ["WHATSAPP_PHONE_NUMBER_ID",     "WA Business number"],
        ["WHATSAPP_APP_SECRET",          "WA appsecret_proof"],
      ]
    },
    {
      title: "LINKEDIN + SHOPIFY",
      col: C.brown_l,
      keys: [
        ["LINKEDIN_ACCESS_TOKEN",  "LinkedIn UGC API"],
        ["LINKEDIN_PERSON_URN",    "LinkedIn identity"],
        ["SHOPIFY_ACCESS_TOKEN",   "Shopify Admin API"],
        ["SHOPIFY_STORE_URL",      "1uu3i0-jg.myshopify.com"],
        ["SHOPIFY_BLOG_ID",        "91683717305"],
      ]
    },
    {
      title: "EMAIL (Resend + M365)",
      col: C.matcha,
      keys: [
        ["RESEND_API_KEY",   "Resend.com · primary mailer"],
        ["EMAIL_FROM",       "info@thepowercoffee.com"],
        ["M365_MAILBOX",     "leo@thepowercoffee.com"],
        ["M365_TENANT_ID",   "Azure app (optional fallback)"],
        ["M365_CLIENT_ID",   "Azure app client ID"],
        ["M365_CLIENT_SECRET","Azure app secret"],
      ]
    },
    {
      title: "TELEGRAM + GITHUB + PATHS",
      col: C.cream,
      keys: [
        ["TELEGRAM_BOT_TOKEN",  "@Powercoffeebot"],
        ["TELEGRAM_CHAT_ID",    "Publishing supergroup · Better Days"],
        ["ALERT_CHAT_ID",       "478617395 · Leo DM only · NEVER the group"],
        ["ANTHROPIC_API_KEY",   "Claude API · generate_content + he_common"],
        ["GITHUB_REPO",         "lacerdareis-ai/power_coffee_repo"],
        ["SALES_MOTOR_PATH",    "Absolute path to Sales_motor/"],
      ]
    },
  ];

  for (var i = 0; i < groups.length; i++) {
    var gx = 60 + (i % 2) * 690;
    var gy = 160 + Math.floor(i / 2) * 340;
    var gw = 650; var gh = 310;
    r(p, gx, gy, gw, gh, C.bg2);
    r(p, gx, gy, gw, 4, groups[i].col);
    await t(p, groups[i].title, gx + 20, gy + 18, gw - 40, 11, F.label, groups[i].col);

    for (var j = 0; j < groups[i].keys.length; j++) {
      var ky = gy + 48 + j * 40;
      r(p, gx + 20, ky, gw - 40, 32, C.bg3);
      await t(p, groups[i].keys[j][0], gx + 32, ky + 8, 280, 11, F.mono,  C.gold);
      await t(p, groups[i].keys[j][1], gx + 340, ky + 9, 290, 11, F.small, C.muted);
    }
  }
}

// ── SLIDE 08 · ALERTING RULES ────────────────────────────────
async function slide08() {
  var p = newSlide("08 · Alerting Rules");
  texture(p);
  await slideHeader(p, "08", "Alerting Rules", "Where failures go — and where they never go");

  // BIG rule cards
  r(p, 80, 180, 580, 260, C.bg2);
  r(p, 80, 180, 580, 5, C.green);
  await t(p, "✅  ALWAYS", 110, 204, 520, 14, F.label, C.green);
  await t(p, "All failure alerts\n→ ALERT_CHAT_ID\n(Leo's personal DM)", 110, 232, 520, 36, F.hero, C.cream, "LEFT", 1.1);
  await t(p, "chat_id = 478617395", 110, 390, 520, 14, F.mono, C.muted);

  r(p, 700, 180, 580, 260, C.bg2);
  r(p, 700, 180, 580, 5, C.red);
  await t(p, "❌  NEVER", 730, 204, 520, 14, F.label, C.red);
  await t(p, "Alerts or reports\n→ TELEGRAM_CHAT_ID\n(publishing group)", 730, 232, 520, 36, F.hero, C.cream, "LEFT", 1.1);
  await t(p, "That channel is for published content only", 730, 390, 520, 14, F.small, C.muted);

  // Scripts that enforce this
  await t(p, "HOW IT'S ENFORCED", 80, 480, 600, 11, F.label, C.muted);

  var scripts = [
    { name: "_alert.sh",          rule: "Shared shell helper · sourced by every run_*.sh · sends ONLY to ALERT_CHAT_ID",    col: C.gold   },
    { name: "he_common.send_telegram()", rule: "Default target changed to ALERT_CHAT_ID — only publisher.py passes TELEGRAM_CHAT_ID explicitly", col: C.brown_l },
    { name: "report_sender.py",   rule: "Sends daily Telegram report to ALERT_CHAT_ID · no email dependency",               col: C.matcha },
    { name: "competitor_monitor / review_scanner / morning_brief", rule: "All hard-coded to ALERT_CHAT_ID — removed the 'if test else group' toggle", col: C.cream  },
  ];

  for (var i = 0; i < scripts.length; i++) {
    r(p, 80, 510 + i * 88, W - 160, 72, C.bg2);
    r(p, 80, 510 + i * 88, 3, 72, scripts[i].col);
    await t(p, scripts[i].name, 100, 522 + i * 88, 580, 13, F.mono,  scripts[i].col);
    await t(p, scripts[i].rule, 100, 546 + i * 88, W - 200, 13, F.small, C.muted);
  }
}

// ── SLIDE 09 · KNOWN LIMITS ──────────────────────────────────
async function slide09() {
  var p = newSlide("09 · Known Limits");
  texture(p);
  await slideHeader(p, "09", "Known Limits & Open Items", "Manual steps and pending fixes as of Jun 2026");

  var items = [
    {
      item:   "Instagram media",
      status: "MANUAL",
      scol:   C.gold,
      action: "Name files story.jpg / carousel_1.jpg etc. and git commit before 4am. Publisher auto-detects correct names — 'stories.jpg' is silently skipped.",
    },
    {
      item:   "Meta Ads MCP",
      status: "PENDING",
      scol:   C.brown_l,
      action: "/ads skill is fully built and wired to act_614811411349257 (personal, active). Meta rolling out MCP access gradually — check back in days/weeks.",
    },
    {
      item:   "Blessed Brands ad account",
      status: "DISABLED",
      scol:   C.red,
      action: "Flagged for unusual activity. Appeal at business.facebook.com/accountquality. Once restored, update /ads skill account ID.",
    },
    {
      item:   "Resend domain DNS",
      status: "PENDING",
      scol:   C.brown_l,
      action: "Add SPF / DKIM / DMARC records for thepowercoffee.com in GoDaddy DNS. Until verified, emails may land in spam. Resend dashboard → Domains.",
    },
    {
      item:   "Meta token expiry",
      status: "⚠️ JUL 19",
      scol:   C.gold,
      action: "Cloud routine fires Jul 5 → email reminder to refresh. Exchange current token via Graph API and update INSTAGRAM_ACCESS_TOKEN + WHATSAPP_ACCESS_TOKEN in .env.",
    },
    {
      item:   "Email campaign",
      status: "ACTIVE",
      scol:   C.green,
      action: "7,436 of 8,096 remaining. Sends 100/day (Resend free tier). Upgrade to $20/mo plan for 270/day. Campaign auto-resumes at 10am cron; never re-sends to already-sent addresses.",
    },
    {
      item:   "pmset wake guard",
      status: "ACTIVE",
      scol:   C.green,
      action: "sudo pmset repeat wake MTWRFSU 03:50:00 — confirmed set. Mac wakes at 3:50am daily before 4am publish cron. Verify: pmset -g | grep repeat",
    },
  ];

  for (var i = 0; i < items.length; i++) {
    var col1 = i < 4 ? 80 : 80 + (i - 4) * 440 + (i >= 4 && i < 7 ? (i === 4 ? 0 : 0) : 0);
    var leftItems  = items.slice(0, 4);
    var rightItems = items.slice(4);
    var isLeft = i < 4;
    var idx  = isLeft ? i : i - 4;
    var ix   = isLeft ? 80 : 80 + idx * 450;
    var iy   = isLeft ? 165 + i * 168 : 165 + idx * 240;
    var iw   = isLeft ? 640 : 420;
    var ih   = isLeft ? 148 : 210;

    r(p, ix, iy, iw, ih, C.bg2);
    r(p, ix, iy, 3, ih, items[i].scol);

    await t(p, items[i].item,   ix + 20, iy + 16, iw - 120, 14, F.h,     C.cream);
    r(p, ix + iw - 130, iy + 14, 110, 26, items[i].scol, 0.2);
    await t(p, items[i].status, ix + iw - 130, iy + 18, 110, 11, F.label, items[i].scol, "CENTER");
    await t(p, items[i].action, ix + 20, iy + 46, iw - 40, 12, F.small, C.muted, "LEFT", 1.65);
  }
}

// ── SLIDE 10 · CLOUD ROUTINES ────────────────────────────────
async function slide10() {
  var p = newSlide("10 · Cloud Routines");
  texture(p);
  await slideHeader(p, "10", "Cloud Routines", "claude.ai/code/routines · manage at that URL (can't delete via API)");

  var routines = [
    {
      id:      "trig_01DdxXe72sFrukFrB22DEfR7",
      name:    "powercoffee-daily-motor",
      status:  "DISABLED",
      scol:    C.red,
      cron:    "0 0 * * * (00:00 UTC daily)",
      env:     "the_power_coffee environment",
      why:     "Old flat-path content generator. Set git user as 'Power Coffee Motor / agent@powercoffee.motor'. Wrote to daily_content/<day>/ (wrong path). Replaced by local 5am generate_content.py cron which uses correct nested path + auto-pushes.",
    },
    {
      id:      "trig_012iU4uVwxt2R7XUrADVGyv5",
      name:    "sales-motor-generate",
      status:  "DISABLED",
      scol:    C.red,
      cron:    "3 3 * * * (03:03 UTC daily)",
      env:     "Millers_bid environment (wrong env!)",
      why:     "Old junk-path generator. Used 'Claude' git identity. Wrote to Sales_motor/<day>/ (doubly-nested junk path). Was the source of the 'Claude' committer divergence. Replaced by local cron.",
    },
    {
      id:      "trig_01Czr5HJxdzL9PxftSemb1EL",
      name:    "Meta token refresh reminder",
      status:  "ENABLED",
      scol:    C.green,
      cron:    "run_once_at: 2026-07-05T13:00:00Z",
      env:     "the_power_coffee environment",
      why:     "One-time reminder email on Jul 5. Sends to lacerdareis@gmail.com via Gmail MCP. Instructs Leo to refresh INSTAGRAM_ACCESS_TOKEN + WHATSAPP_ACCESS_TOKEN before Jul 19 expiry.",
    },
  ];

  for (var i = 0; i < routines.length; i++) {
    var rt = routines[i];
    var ry = 165 + i * 218;
    r(p, 80, ry, W - 160, 196, C.bg2);
    r(p, 80, ry, W - 160, 4, rt.scol);

    r(p, W - 260, ry + 20, 120, 30, rt.scol, 0.2);
    await t(p, rt.status, W - 260, ry + 24, 120, 12, F.label, rt.scol, "CENTER");

    await t(p, rt.name, 100, ry + 18, 700, 18, F.h,    C.cream);
    await t(p, rt.id,   100, ry + 46, 700, 11, F.mono,  C.muted);
    await t(p, rt.cron, 100, ry + 66, 500, 12, F.small, rt.scol);
    await t(p, rt.env,  620, ry + 66, 400, 12, F.small, C.muted);
    divLine(p, 100, ry + 92, W - 260, rt.scol, 0.2);
    await t(p, rt.why,  100, ry + 106, W - 220, 13, F.small, C.muted, "LEFT", 1.65);
  }

  // bottom footnote
  divLine(p, 80, H - 50, W - 160, C.gold, 0.3);
  await t(p, "Last updated: Jun 4, 2026  ·  ADS skill added · Resend email · report→Telegram DM · nested content paths · external cloud writers disabled · pmset 3:50am wake · Shopify token refreshed", 80, H - 38, W - 160, 11, F.small, C.muted);
}

// ── MAIN ─────────────────────────────────────────────────────
async function main() {
  figma.currentPage.name = "HE-OS · The Power Coffee";

  await slide01();
  await slide02();
  await slide03();
  await slide04();
  await slide05();
  await slide06();
  await slide07();
  await slide08();
  await slide09();
  await slide10();

  figma.viewport.scrollAndZoomIntoView(figma.currentPage.children);
  figma.notify("✅ HE-OS document created — 10 slides", { timeout: 5000 });
}

main();
