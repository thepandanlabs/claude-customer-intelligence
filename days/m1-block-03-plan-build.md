# Module 1 · Block 3 — Plan & Build

**Time:** 00:40 – 01:25
**Goal:** Every attendee has run `account add` and `account brief`, identified a gap in the output, picked a stub, edited the spec, and built the enhancement. The tool on their laptop is now better than the one that shipped.

<!-- participant-start -->
## Block 3 — What to do

45 minutes. Work on your own laptop. The facilitator circulates.

**Phase 1 (00:40–00:55) — Run v0.1 and observe**

1. Run `account add acme-software inbox/acme-software/` — ingests 8 interaction files
2. Run `account brief acme-software` — look at what's in the brief
3. Run the remaining three accounts:
   ```bash
   account add globex-consulting inbox/globex-consulting/
   account add initech-retail inbox/initech-retail/
   account add umbrella-corp inbox/umbrella-corp/
   ```
4. Run `account query --open` — look at open commitments across all accounts
5. Note what's missing: are commitments extracted? Competitor mentions? Sentiment?

**Phase 2 (00:55–01:00) — Pick a stub**

1. Open `PRD.md` and read the stub sections
2. Pick the stub that matches the gap that bothered you most in Phase 1
3. Stub A (commitment extraction) is the recommended starting point — it closes the biggest gap

**Phase 3 (01:00–01:25) — Plan, implement, verify**

1. Edit your chosen stub section in `PRD.md` — fill in the requirements in your own words
2. Update `CLAUDE.md` with any extraction rules the stub needs
3. Enable Plan Mode (Shift + Tab twice), run `/prime`, then run `/plan`
4. Read the plan — push back on anything wrong, then approve it
5. Exit Plan Mode, run `/implement` — Claude builds the enhancement
6. Run `account brief acme-software` again — compare to Phase 1
<!-- participant-end -->

## Block shape

This is the longest block — 45 minutes. Most of it is individual laptop work. The facilitator circulates, troubleshoots quietly, and resists the urge to narrate.

| Time | Activity |
|---|---|
| 00:40 – 00:48 | Facilitator demos Plan Mode live. Approve a plan together as a room. |
| 00:48 – 00:55 | Run v0.1. Every attendee runs `account add` on all four accounts. Observe the output. Find the gaps. |
| 00:55 – 01:00 | Pick a stub. Each attendee chooses one enhancement from the PRD stub list. |
| 01:00 – 01:20 | Edit spec → plan → implement. |
| 01:20 – 01:25 | Pause. Surface results. Before vs. after on one account. |

---

## The Plan Mode demo (00:40 – 00:48)

Read this aloud as you do it. Project the screen.

> *"Open the repo. Run `claude`. Press Shift+Tab once — the footer says `accept edits on`. Press Shift+Tab again — it says `plan mode on`.*
>
> *In Plan Mode, Claude physically cannot write files, run commands, or change anything. It can only read, search, and ask questions. This is enforced at the tool level — it's not a polite suggestion.*
>
> *I'm running `/prime` first. It reads `PRD.md` and `CLAUDE.md` and tells me what it understood. If anything in the readback is wrong, I edit the files — not the prompt. Claude is reading exactly what I wrote.*
>
> *Now I'm running `/plan`. A numbered list of steps comes back. I'm reading it line by line. If I see something I didn't intend — a step I don't want, a database change I wasn't expecting — I push back now. Not after the code is written.*
>
> *I approve the plan. Claude exits Plan Mode and executes the steps in order. I watch the diffs — the green lines are code being added, the red lines are code being removed. The discipline is: read the diffs."*

---

## Phase 1 — Run v0.1, find the gaps (00:48 – 00:55)

Every attendee runs:

```bash
account add acme-software inbox/acme-software/
account brief acme-software
```

What v0.1 produces on Acme Software:

- Logs all 8 interactions correctly.
- Last contact and interaction history: present.
- Open commitments section: **empty** — v0.1 doesn't extract them, it only logs interactions.
- Competitor mentions: **missing** — Salesforce appears twice in the raw files but the brief doesn't surface it.
- Sentiment trend: **missing** — no signal on whether the relationship is improving or declining.

Then run the other three accounts and check `account query --open`:

```bash
account add globex-consulting inbox/globex-consulting/
account add initech-retail inbox/initech-retail/
account add umbrella-corp inbox/umbrella-corp/
account query --open
```

Open commitments list: **empty across all accounts** — because Stub A (commitment extraction) is not yet built.

**Facilitator: do not explain the gaps. Ask.**

> *"Look at the open commitments section of the Acme brief. What's there?"*

Wait. Someone will notice it's empty despite the call notes clearly containing promises. That moment of discovery — not instruction — is what makes the gap stick.

Now run:

```bash
account add acme-software inbox/acme-software/
```

Second run: `0 new records. 8 files skipped (already processed).`

**This is the idempotency moment. Pause for it.**

> *"You could run this a hundred times. The ledger stays correct — no duplicates, no double-counting. A chat tab cannot do this. Every session starts blank. This tool remembers, and it accumulates cleanly."*

---

## Phase 2 — Pick a stub (00:55 – 01:00)

Read the stubs aloud from the PRD. Ask each attendee which gap bothered them most in Phase 1. That's usually the right stub.

Default recommendation: **Stub A (commitment extraction)** — it closes the most visible gap and the before/after is immediately obvious in `account query --open`.

| Stub | Who should pick it |
|---|---|
| A — Commitment extraction | Anyone who tracks what their team promised clients |
| B — Sentiment per interaction | Anyone managing at-risk accounts or wanting early warning signals |
| C — Competitive signal detection | Anyone in competitive deals or wanting to track competitor mentions |
| D — `account pitch` (preview) | Anyone curious about Module 2 — note: this is a preview only, full build is Module 2 |
| E — Capability library | Anyone who wants briefs to reference company capabilities automatically |

If someone wants two stubs: pick one for today. The second one is an evening of work at home.

---

## Phase 3 — Edit spec → plan → implement (01:00 – 01:20)

### What attendees do

**Step 1: Edit the PRD stub.**

Open `PRD.md`. Find the stub section for their chosen stub. Each stub has a comment block describing what's missing and what to add. For Stub A:

```
<!-- STUB A — Commitment extraction
Currently: account add logs each interaction (date, file, summary) but extracts
no structured commitments. The brief's "Open commitments" section is always empty.

Add the following to this PRD section:
- Define "commitment" as a record type: something the account team promised
  the client, with a named owner and a deadline.
- Fields: content (what was promised), owner (who made the promise),
  deadline (YYYY-MM-DD or TBD), status (open/closed).
- If the owner is named in the interaction, use that name.
  If only a role is named ("our legal team"), use that + [UNCLEAR-OWNER].
- If no deadline is stated, store TBD — never omit the record.

Test: run account add on inbox/acme-software/ and then account query --open.
      Confirm Sarah's reference list commitment and Ahmed's SLA commitment appear.
-->
```

The attendee reads this, then writes the actual PRD requirement below the comment block. One clear paragraph in their own words.

**Step 2: Update the CLAUDE.md extraction rule.**

The stub comment points to which rule to add. For Stub A:

```
- Extract commitments made by the account team to the client. A commitment is
  a sentence where someone on our side promises a deliverable, action, or follow-up.
  Fields: content, owner (name as spoken or role + [UNCLEAR-OWNER]), deadline
  (YYYY-MM-DD or TBD if not stated). Never omit a commitment because no deadline exists.
```

**Step 3: Run `/prime` → `/plan` → approve → `/implement`.**

```bash
> /prime
```

Claude reads the updated PRD and CLAUDE.md and reads back what it understood. If the readback misses something, the writing is not clear — fix the file, not the prompt.

```bash
> /plan
```

Plan comes back. Read it. If any step does something the attendee didn't intend, push back now. Common things to watch for: a plan that modifies the database schema in a way that would break existing records, or a plan that skips updating the brief output.

```bash
> /implement
```

Claude executes. Watch the diffs. The full change for Stub A is typically 30–60 lines — an updated extraction prompt, a new database table for commitments, and an updated brief template.

**Step 4: Run on the test account.**

```bash
account add acme-software inbox/acme-software/
account brief acme-software
account query --open
```

Before (v0.1): Open commitments: *(none)*.
After (Stub A): Open commitments: Sarah's reference list (TBD), Ahmed's SLA review (TBD), plus any others the tool correctly extracted from the 8 files.

That before/after comparison is the proof the stub worked.

---

## Phase 4 — Pause and surface (01:20 – 01:25)

Stop the room. Ask two or three people to read out loud what they built:

- *"I added commitment extraction. Acme now shows 4 open items across 8 interactions."*
- *"I added competitive signal detection. The Acme brief now flags Salesforce mentioned twice."*
- *"I added sentiment tracking. The brief now shows a declining trend over the last 3 calls."*

The room hears different stubs producing different results on the same accounts. This is the point: the spec change drove the behaviour change. Claude wrote the code; they wrote the rules.

---

## When someone is stuck

1. **"Did you edit both the PRD and the CLAUDE.md?"** Missing one of the two is the most common error. The PRD says *what* to extract; the CLAUDE.md says *how to recognise it* in plain language.
2. **"Run `/prime` and read the readback carefully."** If Claude misunderstood the spec, the readback will show it. Fix the file, not the prompt.
3. **"What does `account brief acme-software` actually output?"** Get real output before guessing what went wrong.
4. **"Let's `/rewind` and re-plan."** `/rewind` undoes Claude's last set of changes — restores files to where they were before `/implement`. Don't be sentimental about 40 lines Claude wrote two minutes ago.

---

[← Back to home](../index.html)
