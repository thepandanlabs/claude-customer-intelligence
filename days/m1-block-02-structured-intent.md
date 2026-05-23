# Module 1 · Block 2 — Structured Intent

**Time:** 00:20 – 00:40
**Goal:** Everyone has read the PRD, and everyone has written at least one extraction rule in the CLAUDE.md. Not read it — written it. The shift from reader to author is the central beat of this block.

<!-- participant-start -->
## Block 2 — What to do

Open the seed repo. Your job is to write at least one extraction rule before this block ends.

1. `cd account-seed-repo` (or wherever you cloned it)
2. Open `PRD.md` — read the *In scope*, *Out of scope*, and *Stub* sections
3. Open `CLAUDE.md` — read the one example rule already there
4. Pick one of these — which matters most for your accounts?
   - A commitment your team made that often goes untracked?
   - A competitor that comes up in client calls?
   - A risk signal you wish you caught earlier?
5. Write your rule in `CLAUDE.md` in plain English — no code required
6. Enable Plan Mode: press **Shift + Tab twice** in Claude Code
7. Run `/prime` and wait for Claude to read back what it understood
<!-- participant-end -->

## What happens in this block

1. **00:20 – 00:28 — Walk the PRD aloud.** Section by section. Pause at each stub.
2. **00:28 – 00:37 — Live rule-writing exercise.** Read a sample interaction excerpt. Ask the room what rule is missing. They dictate it. You type it. Two or three rules total.
3. **00:37 – 00:39 — Tour the slash commands.** Four commands, one sentence each.
4. **00:39 – 00:40 — Q&A.** Three questions maximum. Park the rest.

---

## The PRD in 60 seconds (00:20 – 00:28)

Open `PRD.md` in the seed repo. Read it aloud — it is short by design.

The PRD says: a CLI called `account` that takes a folder of emails, call notes, and meeting transcripts, calls Claude to extract structured data from them, appends everything to a SQLite database (a lightweight file-based database — no server required), skips files already processed, generates client briefs on demand, and lets you query open commitments across all accounts.

Six commands: `add`, `brief`, `query`, `list`, `export`, `pitch` (Module 2). Out of scope: login systems, CRM sync (Track A), email drafting (Track B), Slack integration (Track C), pitch generation (Module 2 / Stub D).

### The stub sections

The PRD ships with five clearly marked gaps. Point them out:

> *"See these stub sections? v0.1 doesn't do these things yet. In Block 3, you'll pick one, write the spec for it, and build it. Each one is 30–40 minutes of work. You're not starting from scratch — you're extending a tool that already runs."*

The five stubs:

- **Stub A — Commitment extraction.** v0.1 only logs interactions. It does not extract structured commitments — who promised what by when. That's the most valuable thing missing.
- **Stub B — Sentiment per interaction.** No signal yet on whether a client conversation was positive, neutral, or negative. The brief can't flag declining sentiment trends.
- **Stub C — Competitive signal detection.** No tagging of competitor mentions. A client who names a rival three times in two months is a risk signal the brief currently misses.
- **Stub D — `account pitch` generation.** The pitch command is scaffolded but not implemented. Module 2 covers this in full.
- **Stub E — Capability library management.** The `capabilities/` folder exists but the tool doesn't yet read from it when generating briefs or pitches.

### Acceptance criteria

Six lines. All checkable without code knowledge:

- `account add acme-software inbox/acme-software/` on 8 files produces records in the ledger.
- Re-running it adds zero new records and reports 8 files skipped.
- `account brief acme-software` returns a structured markdown brief with last contact, open commitments, and key risks.
- `account query --open` returns all open commitments across all accounts.
- `account list` shows all accounts in the ledger.
- The chosen stub: its gap is closed and visible in the brief for the relevant account.

---

## Live rule-writing exercise (00:28 – 00:37)

This is the block's central moment. Do not skip it or convert it into a readthrough.

**What the seed CLAUDE.md ships with:** the Stack, Layout, and Conventions sections are filled in. The Extraction rules section has one pre-written example rule — showing the format — and blank space below it.

**The exercise:**

Open `CLAUDE.md` in the editor (or project it on screen). Read the example rule aloud:

> *"Extract every commitment made by the account team — things the seller promised the client, with a deadline. If no deadline is stated, write TBD. Never omit the commitment because the deadline is missing."*

Then read this excerpt from `inbox/acme-software/2026-04-21-scoping-notes.txt` aloud:

> *"Sarah said she'd get them a reference customer list — a few names in similar verticals. No firm date, but client wants it before the next call. Ahmed mentioned we'd revisit the SLA terms once legal finishes their review."*

Ask the room:

> *"What should the tool do with that? What's there that we'd lose if we just filed the email?"*

Wait. Don't fill the silence. Someone will say: *"Two promises — the reference list and the SLA terms."* Or: *"Sarah's commitment has no date."*

Type the rule they surface into `CLAUDE.md`, in the room, as they dictate it. Roughly:

```
- Extract commitments made by our team to the client. An account team commitment
  is any sentence where someone on our side promises an action, delivery, or follow-up.
  Fields: what was promised, who made the promise, deadline (YYYY-MM-DD or TBD).
  If the speaker is unclear, use [UNCLEAR-OWNER].
```

Then read this excerpt from `inbox/acme-software/2026-05-04-email.txt` aloud:

> *"Just circling back on the Salesforce comparison they raised on the last call. They mentioned Salesforce twice and Dynamics once. Worth flagging."*

Ask:

> *"What rule catches that?"*

They'll get it: competitor detection. Type what they give you:

```
- Flag any interaction where a named competitor is mentioned. Competitor mentions
  are any named alternative software or vendor the client brings up. Record the
  competitor name and the date of the interaction. Do not invent competitors —
  only log names the client explicitly stated.
```

Stop after two or three rules. Don't try to write all five — Block 3 is for that.

**What just happened:** attendees have written business rules that directly govern AI behaviour. No code. The insight to land:

> *"The CLAUDE.md is yours to own. If the tool gets something wrong, the fix belongs here — not in the prompt, not in the code. You wrote the spec. Claude builds to it. If it misses a competitor mention, the rule needs to be clearer — that's a writing problem, not a technology problem."*

### If the room is slow to respond

Don't fill the silence with your own answer. Ask a more specific question:

> *"Sarah committed to something and there's no date. What should the tool do with that — skip it, or record it with a flag?"*

Someone will say: *"Record it — TBD is better than missing."* That's the rule. Type it.

### What not to do

- Don't read a pre-filled CLAUDE.md aloud as if it were a policy document. The insight only lands when they write the rule.
- Don't write all five rules. Leave the room wanting to write more — they will in Block 3.
- Don't let someone say "use NLP" or "parse it with regex." Redirect: *"Write it as you'd explain it to a new analyst on their first week. What should they look for?"*

---

## The four slash commands (00:37 – 00:39)

Slash commands are reusable prompts stored in `.claude/commands/` as plain text files. Type one in a Claude Code session and it runs immediately. Four ship with the seed repo:

| Command | What it does |
|---|---|
| `/prime` | Reads `PRD.md` and `CLAUDE.md` and reads back what it understood. If the readback misses something you wrote, the writing is not clear enough — fix the file, not the prompt. |
| `/plan` | Produces a written, numbered plan. Does not write code. Stops and waits for your approval. |
| `/implement` | Executes the approved plan, step by step. |
| `/verify` | Runs the verification checklist against the hand-labelled answer for `acme-software` and reports any gaps. |

One thing to say about `/prime`:

> *"If Claude's readback misses a rule you wrote, that rule is not clear enough yet. Claude is reading exactly what you wrote — it's a mirror. If the reflection is wrong, fix the writing."*

---

## Common questions in this block

- **"Can I change the PRD before we build?"** Yes — the PRD is yours. Write the change down first, then build. Don't prompt first and write the spec afterwards. The spec drives the tool, not the other way around.
- **"Who writes the CLAUDE.md for my real accounts?"** You do — or your team does together. Start with this skeleton. After a week of real use, cut anything that turned out to be obvious. Add anything the tool kept getting wrong. Keep it under 100 lines — a clear memo, not a policy manual.
- **"What if a rule I write produces wrong output?"** Run it on a sample interaction and check. If the output is wrong, fix the rule. That loop — write rule, run tool, compare output — is the entire discipline.

---

[← Back to home](../index.html)
