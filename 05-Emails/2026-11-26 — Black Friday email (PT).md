# Black Friday email (PT-BR), BLACKFRIDAY20

status:: built, scheduled Thu Nov 26 at 7:00pm ET, **held until the code is confirmed**
files:: `CONTENT/email_campaigns/2026-11-26_blackfriday20/` (email_override.json, email_hero_bf.jpg, make_hero_bf.py, send_bf_email.py, "Black Friday email — preview.html")
related:: [[2026-11-21 — MORNING15 Saturday email]] | [[HE-OS Control]]

## Leo's choices (2026-11-22)
- Offer: **new code BLACKFRIDAY20, 20% off for everyone**, Nov 26–30.
- Send: **Thursday Nov 26 in the evening**, as early access.

## Email
- **Subject:** Black Friday começou: 20% off no Power Coffee
- **Preview:** Acesso antecipado: use o código BLACKFRIDAY20 até segunda, 30/11.
- **Headline:** "Sua manhã mais forte, 20% mais barata."
- **Body:** the workday/family angle, then "20% de desconto no site" starting tonight, the routine plus the ingredients (11 ingredientes, 0 g de açúcar, feito nos EUA), then "É a hora de fazer estoque", valid until Mon Nov 30.
- **Math:** US$ 18,90 → −20% → **US$ 15,12**, about US$ 1,01 per dose before shipping and tax.
- **Buttons:** "Quero 20% off" and "Comprar no site" → thepowercoffee.com/discount/BLACKFRIDAY20; "Comprar na Amazon" → B0DYK75WP7. Note: the code works on the website only.
- **Hero:** navy, "ACESSO ANTECIPADO · 26 A 30/11", BLACK FRIDAY in gold, 20% OFF, the pack, and fact chips. Same template, photo, footer and FDA disclaimer (PT + EN) as MORNING15.
- **Left out on purpose:** "Centenas de pessoas… confirmam os resultados" (not in the certified facts). Add it back if Leo wants it.

## Before Thursday 7pm, Leo has to
1. **Create BLACKFRIDAY20 in Shopify → Discounts.** Settings: 20% off the order, all customers, one-time purchases, one use per customer, Nov 26 7pm → Nov 30 11:59pm ET. The Shopify API token has expired, so this can't be done from here.
2. **Tell Claude it's live.** Then `"_code_confirmed": true` gets set in email_override.json. Until then, the scheduled send prints HELD and sends nothing.
3. **Fix the Resend Marketing plan** (≥ 8,524 contacts). Otherwise it fails with the same 403 as MORNING15.

## Scheduled
- One-time local task `black-friday-email-send` runs **Thu Nov 26 at 7:00pm ET**: a dry run, then the send. It can't send twice (sent.json).
- The app must be open and the Mac awake. The task runs in default permission mode, so it may pause for an approval unless Leo pre-approves it with "Run now" or sets the mode in the task page.
- Dry run on 2026-11-22: OK. Images load from jsDelivr; commit 71235eb, pushed.
