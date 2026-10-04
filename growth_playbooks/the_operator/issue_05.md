---
**The Operator** · Issue 5 · Operator week
**Platform:** LinkedIn Newsletter (Leo's personal profile)
**Series:** the_operator | **week_type:** operator
---

# Our own automation erased a day of approved content overnight. We only found out because we went looking.

Nothing crashed. Nothing errored. The job did exactly what it was built to do.

We run a script that writes tomorrow's content automatically, unattended, at 5am — that's the whole point of it, one less thing to do by hand every morning. One morning, a routine check turned up a day that had already been approved — real images already staged, a real person having already signed off on the words next to them — now carrying a completely different, generic caption that had nothing to do with those images. The script hadn't failed. It had just done its one job, "generate fresh content for tomorrow," without knowing tomorrow already had an answer.

Here's the part that actually scared me, once I understood it: the script is version-controlled, but only the auto-generated version had ever been committed. The real one — the one a person had actually reviewed — existed in exactly one place: a conversation from earlier that hadn't been saved anywhere else. One commit in the history, not two. If that conversation hadn't still been sitting there, there was no path back. Approved work had quietly become unrecoverable, and nobody had decided that on purpose.

That's the actual failure, and it's not really a code bug. It's a confusion between two states that look identical to a script but mean completely different things to a person: *nothing is here yet* and *something is here, and someone already said yes to it*. Our pipeline had been treating both states the same way for months — generate either way — because nothing had ever forced the difference to matter. Until it did.

The fix wasn't making the generator smarter about merging or regenerating correctly. It was making it humbler: before doing any real work, check whether the target day already shows a signed-off approval or already has real files sitting in it. If either is true, stop, and print exactly why it stopped. A deliberate override exists for the rare case where regenerating really is the intent — but that has to be asked for, not assumed.

The broader lesson isn't really about this one script. Any system that writes into a space a person also works in needs a default, and the safe default is *defer to whatever's already there*, not *assume I'm the only one touching this*. That default doesn't show up for free. Somebody has to decide it's the rule and build it in on purpose — usually only after the first time it wasn't there and something real almost got lost because of it.

We got lucky. The conversation that saved us happened to still exist. That's not a system. That's luck wearing a system's clothes, which is exactly why the actual guard exists now.

---

### Expansion seeds
- Approved work that only lives in a conversation, never in version control, isn't actually safe — this incident is what that gap looks like when it bites.
- "Nothing's here yet" and "something's here and someone said yes" are two different states most automation never learns to tell apart.
- A guard that skips and explains itself beats a guard that tries to be clever about merging — when it trips, you want to know immediately, not debug a merge.
- Any system writing into shared space on a timer needs to default to deferring to a prior human decision — and that default has to be built in on purpose, it's never free.

— Leo, building Power Coffee one real decision at a time.
