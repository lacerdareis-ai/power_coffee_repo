# Customer Referral Program — Power Coffee

**Status:** Not yet live. Priority: High (closes the customer flywheel HE-OS doesn't yet have).
**Skill:** Use `/referrals` when designing campaign mechanics.

---

## The Problem This Solves

HE-OS generates content and drives traffic, but there is no loop that turns satisfied buyers into acquisition. Word-of-mouth is the highest-converting channel for a product like this (the second cup test, Day 3 proof) but there is no system to activate it.

---

## Program Design

### Mechanic: Give $5, Get $5

- **Referrer gets:** $5 store credit when their referred friend places a first order
- **Referee gets:** $5 off their first order (reduces trial barrier)
- **Minimum order to trigger:** $18.90 (one bag — no gaming with a $1 purchase)
- **Credit expiry:** 90 days (creates urgency without alienating customers)

**Why $5 and not a percentage:**
$5 is concrete. "Get $5" reads as a reward. "Get 28% off" reads as math. Concrete dollar amounts test better for referral programs under $50 AOV.

### Mechanic: The "Two Morning" Share

Instead of a generic referral link, frame it as a dare:
> "You have two mornings left in this bag. Give one away."

The referral is embedded in a physical sampling moment: split the last two servings with someone who's been complaining about crashing. That person experiences the product before they ever see a sales page.

---

## Touchpoints (where to activate)

| Touchpoint | Mechanic | Timing |
|---|---|---|
| Post-purchase Email 5 (Day 21) | "Someone you know is crashing at 2pm — give them $5, get $5" | Already added to Email-Sequences.md |
| Bag insert card | Printed QR code: "Share your first win" → referral landing page | Add when next batch of bags is printed |
| Package slip | "Know someone who needs this? Forward them this page." | Immediate |
| IG Story sticker | "Tag someone who needs this" prompt in weekly CTA Story | Add to make_cta_story.py |

---

## Implementation options (in order of ease)

**Option 1 — Manual (start here):** Leo handles referrals by email. "Reply with your friend's email — I'll send them $5 off and credit your account." Low tech, proves the mechanic works before building infrastructure.

**Option 2 — Shopify Referral App:** Apps like Referral Candy ($49/mo), Loyalty Lion, or Smile.io have native Shopify integrations. Set up in under 2 hours. Auto-generates referral links, tracks conversions, issues credits automatically.

**Option 3 — Custom page:** A `/refer` page on Shopify that captures the referrer's email and auto-generates a code. More control over the experience. Buildable in 1-2 hours with Shopify Liquid.

**Recommended:** Start with Option 1 for 30 days to validate demand, then move to Option 2 when referrals are coming in faster than Leo can handle manually.

---

## Ambassador tier (future)

Once referrals are generating consistently, create a named tier:

**The Morning Council** (internally called the #FirstWin ambassadors)
- Customers who have referred 3+ people
- Get a permanent 20% code they can share
- Access to new flavor early drops
- Name in the Telegram group pinned message
- No paid commission — it's identity, not income

This is the desire-brand community mechanic. People want to be the person who introduced their team to Power Coffee.

---

## Copy for referral emails (no-ai-slop)

**Email subject:** "Someone you know is crashing at 2pm"
**Body:** "Three weeks in. If Power Coffee is working for you, you probably know someone who would benefit. Forward this email to them. When they order, you both get $5 off your next bag. No codes. No apps. Just reply with their name and email address and I'll take care of it. Leo"

**IG Story prompt:** "Tag someone who needs their afternoon back."
