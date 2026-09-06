# Email Copywriting — What Actually Sells (added 2026-09-01)

Research-backed techniques for every Power Coffee email: the Saturday newsletter
(`publisher.py → send_weekly_newsletter`), the day-7 review request and day-14
reorder nudge (`post_purchase_review.py`, `post_purchase_reorder.py`), and any
one-off send (`send_email_now.py`). All of this sits ON TOP of the existing
Anti-AI-Slop rules and honesty guardrails in `content-system.md` — those still
govern. This file is technique, not a license to hype.

## 1. Pick the framework by list temperature

- **PAS (Problem → Agitate → Solve)** — default for our newsletter. The list
  already knows the brand; open on the problem the reader already has (the 2pm
  crash, the third coffee that isn't working), sit in it for one more line than
  feels comfortable, then position the scoop as relief. Keep it under ~300
  words — PAS is built for speed, not a full sales page.
- **BAB (Before → After → Bridge)** — best for founder-story or launch emails.
  Paint the before state concretely, the after state concretely, then the
  product is the bridge. Good fit for "Building Power Coffee" narrative beats
  ported into email form.
- **AIDA (Attention → Interest → Desire → Action)** — reserve for cold-list or
  longer sends (a full explainer email, a big campaign launch). Overkill for a
  warm weekly newsletter; use PAS instead for those.

## 2. Subject lines — what the data actually says

- **Length:** under 70 characters. Shorter (2-4 words) tests highest for raw
  open rate; 6-10 words tests highest for engaged opens. When in doubt, err
  short and specific over clever.
- **Personalization lifts opens ~26-31%** — even just a first name. We don't
  currently mail-merge first names into subject lines; worth adding if Resend
  volume/plan supports it.
- **Specificity beats cleverness.** "The real reason your afternoon coffee
  doesn't work" outperforms a pun. Name the mechanism or the moment, not a
  vague tease.
- **Real urgency lifts opens ~22%** — but this only applies when the urgency is
  true (an actual ship-by date, an actual limited restock). Never manufacture
  a countdown that isn't real — that's a guardrail violation, not just bad
  practice.

## 3. Structure — one idea, one CTA, one person

- Write to a single reader, not "our customers." Second person, direct.
- **One CTA per email.** A single, clear call to action can lift conversion
  dramatically versus a wall of links. Every Power Coffee email should have
  exactly one link doing the work (matches `_extract_cta`'s assumption of one
  terminal CTA — don't fight the template by burying multiple links mid-body).
- Preview text is real estate — use it to extend the subject line's hook, not
  restate it. It's the second thing a reader sees before opening.

## 4. Persuasion principles — mapped to what we're actually allowed to say

Cialdini's six levers, filtered through our honesty rule (real prices, real
scarcity, real numbers only — see `content-system.md` Persuasion Principles
section for the landing-page version of this same guardrail):

| Lever | Allowed version for us | Not allowed |
|---|---|---|
| Social proof | Real testimonial, real Amazon star rating, real verified-buyer count | Fabricated quotes or invented review counts |
| Scarcity | Real batch-size limits, real stock levels pulled from Shopify | "Only 3 left!" that isn't true |
| Reciprocity | Free recipe book, free content, genuinely useful ingredient education | A "free gift" with hidden strings |
| Authority | Illuminate Labs certification, MD review — framed as the receipt, never the headline | Overstating the certification as lab-testing the physical product (see the 2026-08-27 correction — this applies to email too) |
| Commitment/consistency | Referencing the reader's own stated goal ("you said mornings were the problem") | Fake foot-in-the-door sequences that manufacture false agreement |
| Liking | Founder-voice, first person, real stakes | Manufactured relatability |

## 5. Deliverability — this is a real 8,000+ list, protect it

- Avoid stacking spam-trigger phrases in subject lines: "act now," "limited
  time," "buy now," "guaranteed," "free" used more than once. One is fine in
  context; three in a subject line hurts inbox placement regardless of intent.
- Sounding human beats sounding like a sales blast — this is also just brand
  voice, so the incentive is aligned, not in tension.
- Keep the list clean (bounces/unsubscribes hurt sender reputation) —
  `fetch_gmail_contacts.py` / `email_list.txt` hygiene matters for
  deliverability, not just list size.

## 6. Applied example (used for the 2026-09-01 catch-up newsletter)

Subject: "The real reason your afternoon coffee doesn't work" — specific,
under 70 chars, names the mechanism.
Structure: PAS — problem (blame the caffeine) → agitate (explain why more
caffeine doesn't fix it) → solve (the actual formula, real doses, real
certification framing) → single CTA.
This is the reference pattern going forward — reuse this shape for the
weekly newsletter unless a launch/story angle calls for BAB instead.
