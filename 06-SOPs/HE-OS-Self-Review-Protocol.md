# HE-OS Self-Review Protocol

> The watchdog that watches the watchdog. LENS reviews **content**; self-review reviews the **engine**.
> Added 2026-06-24 after a manual audit found `generate_content.py` had been crash-looping for days with no job noticing (which is why content went manual).

---

## Schedule

| When | Job | Wrapper | Engine |
|---|---|---|---|
| **Sunday 16:00** (weekly) | HE-OS Self-Review | `run_self_review.sh` | `self_review.py` |

Runs before Monday's Analyze + Plan block so its findings feed the week. Log: `/tmp/power_coffee_self_review.log`. Report lands in `04-Analytics/self-review/`.

---

## Autonomy

**FULL** (set by Leo, 2026-06-24) — no human approval gate.

The one safety rail (agreed, not an approval gate): **the routine never keeps a change that breaks the build.**
- Every `*.py` edit is `py_compile`-checked; if it fails, the edit is **auto-reverted**.
- Code heals keep a timestamped on-disk backup (`<file>.selfreview-bak-YYYYMMDD-HHMMSS`) — the bot dir is not git-tracked, so this is how a code heal is reversible.
- Vault changes are **git-committed** (commit only, never pushed), reversible via `git revert` / `git reset`.
- Publishing / credential / money changes are reported, never auto-applied.

---

## What it does each week

1. **HEALTH** — scans `/tmp/power_coffee_*.log`: error counts + how long since each job last ran.
2. **FRESHNESS** — flags `brain/references/*.md` untouched for > 21 days.
3. **CLOCKS** — days until the IG/Meta token expires; flags it if records disagree (HE-OS.md says Jul 19, memory says Jul 11).
4. **HYGIENE** — vault git dirty? stray duplicate `HE-OS/` folder present?
5. **HEAL** — `py_compile`s the core scripts; for any that fail, asks Claude for the smallest unique fix, applies it, recompiles, and **keeps it only if it now compiles** (else reverts).
6. **ANALYZE** — Claude writes a ranked review: health colour, what's broken, improvements tagged `[AUTO]` vs `[LEO]`, one thing to watch.
7. **APPLY** — commits the vault, appends `Open-Items-Log.md`, writes the dated report, sends a Telegram summary to Leo's **personal DM** (never the group).

`CORE_SCRIPTS` (heal targets): generate_content, generate_media, qa_critic, qa_callback_poller, publisher, run_lens, he_common, self_review.

---

## Outputs (in this vault)

- `04-Analytics/self-review/self-review-YYYY-MM-DD.md` — full weekly report + raw JSON snapshot
- `04-Analytics/self-review/Open-Items-Log.md` — running list of flags and what got auto-healed

---

## How to run manually

```bash
/Users/lacerdareis/power_coffee_bot/sales_motor/run_self_review.sh
# or just the engine:
cd /Users/lacerdareis/power_coffee_bot/sales_motor && python3 self_review.py
```

## Tuning

- `FRESH_DAYS` (default 21) — staleness threshold for brain refs.
- `TOKEN_EXPIRY_RECORDS` — update both dates when the token is refreshed.
- To narrow what auto-heal may touch, edit `CORE_SCRIPTS`.
