# MORNING15 Saturday email (draft for Sat Nov 21, 2026)

status:: draft, needs Leo's OK, not scheduled
files:: `05-Emails/2026-11-21_morning15/` (email_override.json, the 3 images, email_preview.html, and the "MORNING15 email — preview.html" that opens anywhere)
related:: [[2026-11-18 — Kit Café do Trabalhador (Power Coffee + The Bread)]] | [[Brand Memory — 6 Principles]]

- **Subject:** One scoop. That's the whole change.
- **Preview text:** 15% off your first order with MORNING15.
- **Design:** the offer_email.py template, in navy and cream with no black.
  - Hero: "15% OFF" with the pack and two step chips, "01 Brew your coffee" and "02 Add one scoop".
  - Then the headline "Keep your coffee. Add one scoop.", the code block, a coral "Get 15% off" button, the hands-and-mug photo, and the math card.
  - Footer: www.thepowercoffee.com plus the Amazon logo, the FDA disclaimer, and an unsubscribe link.
- **Facts used** (from config.json): 11 ingredients, 0g sugar, Made in USA, $18.90 for a 15-serving pack. The first pack is $16.07 with the code, about $1.07 a cup before shipping and tax.
- **Code terms** (from offers.py): 15% off, first order only, one use per customer, one-time purchases, no end date. The email doesn't say "this weekend only".
- **Button link:** https://www.thepowercoffee.com/discount/MORNING15 (no /pages/ link).

## To send it
1. Check that MORNING15 shows Active in Shopify admin → Discounts. This hasn't been verified from this Mac.
2. Copy `email_override.json` and its 3 jpgs into `CONTENT/daily_content/nov2026_content/nov21_2026/`.
3. Make sure the Saturday publish run includes `email`. The last few Saturdays skipped it ("not in --platform list").

## Update 2026-11-20: order buttons
- Added an "Order yours" row above the footer with two buttons:
  - "Order on our website" (cream) → https://www.thepowercoffee.com/discount/MORNING15
  - "Order on Amazon" (gold) → https://www.amazon.com/dp/B0DYK75WP7, the ASIN used in the CTA Stories
- Note under the buttons: "Code MORNING15 works on www.thepowercoffee.com only."
- `offer_email.py` has new optional fields: `order_buttons`, `order_title`, `order_note`. Emails without them render exactly as before.

## Update 2026-11-20: Brazilian Portuguese version (now the main draft)
- **Subject:** A primeira vitória do seu dia.
- **Preview text:** 15% de desconto na sua primeira compra com o código MORNING15.
- **Headline:** "Sua rotina. Sua primeira vitória."
- **Buttons:** "Comprar no site" and "Comprar na Amazon", with the note "O código MORNING15 vale só em www.thepowercoffee.com."
- **PT brand rule:** the email never says the scoop is mixed into coffee. It leads with the brand and the routine ("o Power Coffee entra nesse ritual com uma dose").
  - The hero's step chips became fact chips: 0 g de açúcar · 11 ingredientes · Feito nos EUA.
- **Prices:** US$ 18,90 → US$ 16,07 for the first pack, about US$ 1,07 per dose.
- **Disclaimer:** the PT translation runs first, then the English FDA text, which always stays.
- **Files:** the English version is kept as `email_override.en.json` and `email_hero_offer.en.jpg`. The PT hero comes from `make_hero_ptbr.py`.
- **Template:** `offer_email.py` got an optional `labels` field (code, math, order title, footer, unsubscribe, disclaimer_extra). Defaults are English, so older emails don't change.
- **Open question:** who receives it? The whole newsletter list, or only Portuguese speakers?

## Update 2026-11-20: Leo's own copy (PT)
- **Headline:** "Chega de terminar o dia cansado!"
- **Body:** Leo's text as he wrote it, with one change: the accent on "Só". "Primeira vez? 15%…" stays at the end.
- **Flag:** "Só adicionar um scoop do seu café preferido" goes against the PT brand rule (never say the scoop goes into the coffee). Left as is because it's Leo's text. Leo to confirm, and to decide whether he meant "no seu café".
- **2026-11-20, Leo:** replaced "São 11 ingredientes, com 0 g de açúcar." with "**CENTENAS DE PESSOAS JÁ TESTARAM E CONFIRMAM OS RESULTADOS**".
  - The source is the brand's existing "300 people tested, 70% reported more energy and focus" (Amazon listing, a June 23 reel). It is not in the certified facts (config.json / the Illuminate Labs certification).
  - Per `dtc-cpg-sales/references/compliance.md`, a survey claim should say what people *reported* and keep the survey data on file. "Confirmam os resultados" is broader than that.
  - The hero image still shows "0 g de açúcar · 11 ingredientes · Feito nos EUA", so those facts stay in the email.
- **2026-11-20, Leo:** keep "CONFIRMAM OS RESULTADOS" as written; he chose this over the softer survey wording.

## Scheduled 2026-11-20 (Leo: whole newsletter list)
- status:: **scheduled**, sends Sat Nov 21 at 4:00am ET (the `com.powercoffee.publish` job, `--platform=…,email`) to the whole Resend newsletter segment.
- **Installed in `nov2026_content/nov21_2026/`:** `email_override.json` plus the 3 images. A `## EMAIL` block was added to content.md so the run doesn't skip email for "no copy"; that block is not what gets sent.
- **Pushed:** commit 5559d95. All 3 images load from jsDelivr (HTTP 200).
- **Kept as Leo wrote it:** "Só adicionar um scoop do seu café preferido!" (he didn't ask for a change).
- **To cancel before 4am:** delete or move `email_override.json` and the `## EMAIL` block from the Nov 21 folder.
- **Not verified:**
  - that MORNING15 is active in Shopify (if not, the button and code won't work)
  - that the Mac is awake at 4am
  - the actual send result (check `nov21_2026/publish_status.json` → email)

## Shopify check 2026-11-20 (Shopify admin, read only)
- MORNING15 is **Active**, since Oct 27 with no end date.
- **Settings:** 15% off the whole order, one-time purchases only, one use per customer, no minimum, stacks with shipping discounts, online store. Used 0 times so far.
- ⚠️ **Eligibility is "Todos os clientes" (all customers), not first-time buyers.**
  - The first-order segment described in offers.py isn't attached, so returning customers can also use it once.
  - The email says "Só na primeira compra", so Shopify is looser than the email. Customers won't be refused, but it isn't limited to new buyers.
  - Not changed; that's Leo's decision.
- The API token in .env has expired (the offers.py `plan` check was rejected), so this was checked in Shopify admin in Chrome.

## Send attempts 2026-11-21: not sent
- **4:00am scheduled run:** failed. Resend returned 403 "You have reached your contacts quota. Please upgrade your plan to send more emails."
- **11:53am:** Leo said he had added Resend credits, so the email step was re-run on its own (`publisher.py --platform=email`). It failed with the same 403, and **no broadcast was created**.
- **Why:** Resend limits broadcasts by how many contacts the account holds, not by credits. The newsletter segment has **~8,487 contacts**. The contact sync skipped all 8,487 as already present and created none, so the plan's contact limit has to cover that many.
- **Fix:** in Resend → Settings → Billing, choose the *Marketing* plan tier that covers ≥ 8,500 contacts. Sending credits for transactional email don't raise this limit. Then re-run the same command; it can't send twice, because the broadcast ID is stored in `newsletter_send_progress.json`.
- **Also seen:** the Shopify subscriber fetch returned 401 (expired Shopify token, same as before), so Shopify opt-ins weren't added this run. This doesn't block sending.
- **12:25pm:** Leo said the plan was upgraded. Re-ran the send and got the same 403 contacts-quota error, so **still not sent**.
  - The Resend account holds **8,524 contacts in total** across 3 segments: "Power Coffee Newsletter", an Oct 8 test segment and "General". That's slightly more than the 8,487 in the newsletter list.
  - Next: confirm Billing shows the **Marketing** plan (not only Transactional) at a tier ≥ 8,524 contacts, then re-run. No duplicate is possible.
- **Rescheduled (Leo, 2026-11-21):** a one-time local scheduled task, `morning15-email-sunday-send`, runs **Sun Nov 22 at 8:00am ET**.
  - It runs `publisher.py --platform=email --date=2026-11-21`, after a dry run first. `--date` keeps the Saturday-only gate passing.
  - It saves to Auto mode and runs only if the Claude app is open and the Mac is awake.
  - It stops if the contacts-quota 403 comes back, and logs the result here and in HE-OS Control.
- **2026-11-22 08:00 — Sunday send result: FAILED.** Dry run OK, real send hit Resend 403 "You have reached your contacts quota" again. No broadcast ID, not retried. Leo needs to upgrade the Resend Marketing plan (≥ 8,524 contacts) before re-running.

## Send result: NOT SENT
- **Sat Nov 22, 8:00am:** failed. Resend returned 403 "You have reached your contacts quota. Please upgrade your plan to send more emails."
- **Thu Nov 26:** retried once at Leo's request ("send today email again / try again"), with the eyebrow changed from "Sábado de manhã" to "Bom dia" for a weekday send. The same 403 came back, so nothing went out.
- **Cause:** the newsletter list has 8,490 addresses (email_list.txt plus Shopify subscribers), which is more than the Resend plan's contact limit allows. Resend blocks every broadcast until the plan is upgraded or the contacts are cut below the limit.
- **Options:**
  - upgrade the Resend plan, which only Leo can do
  - trim the Resend audience to fit the limit
  - send from Shopify Email instead

## Shopify change 2026-11-26 (Leo approved: "Yes, restrict it")
- MORNING15 eligibility changed from "Todos os clientes" to the built-in segment **"Customers who haven't purchased"**. Saved and checked on the discount page; everything else is unchanged (15%, one use per customer, one-time purchases, no end date, still Active).
- **Not verified:** a test checkout as a brand-new customer. Segment discounts only apply once Shopify recognizes the buyer at checkout (from their email or login).
- **2026-11-26, 3rd attempt:** same 403, nothing sent.
- **Root cause:** found on the Resend billing page (viewed, nothing changed). The account has two separate plans:
  - **Transactional Pro:** 50,000 emails a month, $20/mo. This is the "50,000 emails" Leo sees, and it does NOT cover Broadcasts.
  - **Marketing:** free tier, **1,000 contacts**. Broadcasts (the newsletter) count against this.
  - The account holds 8,524 contacts. To send, the Marketing plan must go up to a tier with at least about 10,000 contacts, under Resend → Settings → Billing → View plans → Marketing.

## ✅ SENT 2026-11-26 (~3pm ET) through Resend Transactional (Leo's choice)
- **Why Transactional:** Broadcasts need the Marketing plan (free tier, 1,000 contacts). Leo chose to send through the Transactional Pro plan (50k emails a month) instead.
- **Script:** `~/power_coffee_bot/sales_motor/send_transactional_blast.py` (batches of 100, resumable). Progress is in `data/blast_morning15_pt_2026-11-26.json`.
- **Recipients:** 8,487, from email_list.txt minus unsubscribe_list.txt and Resend-unsubscribed contacts. All 85 batches were accepted, with 0 failures.
- **Version:** the PT-BR copy with the eyebrow "Bom dia" (it said "Sábado de manhã" before).
- **Replies and unsubscribes** go to **leo@thepowercoffee.com**. A test to info@ bounced, so info@ seems to have no mailbox.
  - The unsubscribe link and header are a mailto ("Unsubscribe - Power Coffee").
  - **Add each requester to `unsubscribe_list.txt` by hand**; Resend won't handle these automatically.
- **Delivery sample** (first 500 checked): 288 delivered, 112 still sending, 91 suppressed (Resend blocks addresses that bounced or complained before), 9 bounced.
