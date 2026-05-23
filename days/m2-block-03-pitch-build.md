# Module 2, Block 3 — Plan + Build

**Time:** 00:30 – 01:15
**Goal:** Every attendee has a working `account pitch` command and a populated capability library. The tool on their laptop generates a section-by-section proposal draft from an RFP. 45 minutes.

<!-- participant-start -->
## Block 3 — What to do

45 minutes. Work on your own laptop. The facilitator circulates.

**Phase 1 (00:30 – 00:45) — Run the brief and read the RFP**

1. Run `account brief acme` (or your account name from Module 1)
2. Open `rfp/sample-rfp-globex.txt` — read the requirements section
3. Run `account capability list` — see what's already in your library
4. Note what's missing: capabilities that would cover this RFP but don't exist yet

**Phase 2 (00:45 – 00:50) — Seed your capability library**

1. Open `capabilities/` — read one existing `.yaml` file for format reference
2. Add at least one capability that your real work would include:
   ```bash
   account capability add
   ```
   Or drop a `.yaml` file directly into `capabilities/` and run `account capability list` to confirm it appears

**Phase 3 (00:50 – 01:10) — Plan, build, and run the pitch**

1. Fill in your chosen stub section in `PRD.md` (Stub D or Stub E — whichever you haven't done)
2. Update `CLAUDE.md` with any pitch rules the stub needs
3. Enable Plan Mode (Shift + Tab twice), then run `/plan` — read and approve
4. Exit Plan Mode, then run `/implement` — Claude builds the command
5. Run the pitch:
   ```bash
   account pitch acme --rfp rfp/sample-rfp-globex.txt
   ```

**Phase 4 (01:10 – 01:15) — Read the output**

Read the first two sections of the draft. Ask yourself:
- Did it reference the client's actual situation (from the brief)?
- Did it match a real capability — or flag where it couldn't?
- Did it invent anything?
<!-- participant-end -->

## Block shape

| Time | Activity |
|---|---|
| 00:30 – 00:38 | **Facilitator demos Plan Mode live.** Brief → capability list → plan approval. |
| 00:38 – 00:45 | **Run the brief, read the RFP.** Every attendee. Find the gaps in the capability library. |
| 00:45 – 00:50 | **Seed the capability library.** Add at least one capability. |
| 00:50 – 01:10 | **Edit spec → plan → implement.** Fill in the PRD stub. Update CLAUDE.md. Run `/plan` → `/implement`. |
| 01:10 – 01:15 | **Pause.** Read the pitch output. Before/after comparison. |

---

## The Plan Mode demo (00:30 – 00:38)

Project the screen. Read this aloud as you do it.

> *"Open the repo. Run `claude`. Press Shift+Tab once — the footer says `accept edits on`. Press Shift+Tab again — it says `plan mode on`.*
>
> *In Plan Mode, Claude cannot edit files, run commands, or modify anything. It reads. It asks questions. That's it. This is enforced at the tool level — not a polite suggestion.*
>
> *I'm running `/prime` first. It reads `PRD.md` and `CLAUDE.md` and tells me what it understood. I'm listening to the readback of the pitch rules. If anything is missing or wrong, I fix the file — not the prompt.*
>
> *Now I'm running `/plan`. The plan comes back as a numbered list. I'm reading every step. I want to know: does step 3 match what I intended? If not, I say so now — not after the code is written.*
>
> *I approve the plan. Claude exits Plan Mode and executes. Watch the diffs — those are the code changes. Read them."*

Before running `/plan`, show the brief and the RFP side by side:

```bash
account brief acme
```

> *"This is what the tool knows about Acme. Watch whether the proposal references any of this — the Q3 procurement deadline, the procurement contact name, the commitment we made in March. If it does, the brief is working. If it doesn't, check whether the brief is being passed to the pitch command."*

---

## Phase 1 — Brief and RFP (00:38 – 00:45)

Every attendee runs:

```bash
account brief acme
account capability list
```

What to observe:
- The brief shows: last contact date, open commitments, key contacts, risks
- The capability list shows: what the tool currently knows your company can do

Then open `rfp/sample-rfp-globex.txt`. Read the requirements section. Five requirements in the seed RFP:

1. Cloud infrastructure migration — enterprise scale
2. Regulatory compliance: SAMA/NCA frameworks (if applicable)
3. Minimum 3 verifiable references in financial or government sector
4. 90-day delivery window for initial assessment phase
5. Dedicated on-site technical lead for first 60 days

**Facilitator: do not explain what matches. Ask.**

> *"Look at your capability list. Which of these five requirements do you have a clear match for? Which are gaps?"*

Wait. Let the room find it. The seed library ships with two capabilities: managed cloud migration and regulatory compliance. References, delivery window, and on-site lead are gaps. The `[CAPABILITY-GAP]` flags will appear in the pitch output — but only if they built the rule in Block 2.

This is the moment Claim 2 lands:

> *The brief seeds the pitch. Account history isn't decoration — it's how you write a proposal that references the client's actual situation.*

Run the brief again and point to the Q3 procurement deadline line:

> *"That line came from a meeting note six weeks ago. If the pitch tool reads this brief and writes a proposal that says 'we understand your Q3 deadline is critical' — that's not the tool being clever. That's the tool reading what you captured. The capture is the discipline."*

---

## Phase 2 — Seed the capability library (00:45 – 00:50)

Open `capabilities/sample-cloud-migration.yaml`. Read it aloud:

```yaml
id: managed-cloud-migration
name: Managed Cloud Migration
description: End-to-end migration from on-premise infrastructure to cloud.
  Includes assessment, architecture design, cutover, and 90-day hypercare.
evidence:
  - "Delivered Aramco Digital: 14 systems migrated, zero downtime cutover, Q2 2025"
  - "SAMA cloud readiness programme: 6 regulatory workloads migrated with full compliance sign-off"
keywords: [cloud, migration, infrastructure, hypercare, on-premise]
```

> *"Every field matters. The evidence field is where the tool finds proof to cite. If the evidence is vague — 'we have done cloud work' — the proposal will be vague. Specific evidence produces specific proposals."*

Each attendee adds at least one capability. Either:

```bash
account capability add
```

(interactive prompt — walks through each field)

Or create a `.yaml` file manually in `capabilities/` following the same structure, then:

```bash
account capability list
```

Confirm the new entry appears.

**If someone doesn't know what to add:** use one of the sample capabilities from the seed. The goal is to understand the format — they can refine the content later.

---

## Phase 3 — Edit spec → plan → implement (00:50 – 01:10)

### What attendees do

**Step 1: Fill in the PRD stub.**

Open `PRD.md`. Find Stub D or Stub E (whichever is still empty). The stub has a comment block:

```
<!-- STUB D — Pitch command
Currently: `account pitch --rfp <file>` is not implemented.

Add to this PRD section:
- The command reads: (1) the account brief for the named account,
  (2) all files in capabilities/, (3) the RFP file.
- It produces a section-by-section proposal draft in markdown.
- For each RFP requirement: find the best-matching capability file
  (by keyword overlap and description relevance).
- If a clear match exists: draft a proposal section citing the capability
  and evidence. Use the account brief to personalise where possible.
- If no match: output [CAPABILITY-GAP: <requirement summary>].
- Output: saved to proposals/<account>-<date>.md

Test: run account pitch acme --rfp rfp/sample-rfp-globex.txt
      The output should address all 5 requirements.
      Requirements 3, 4, 5 should produce [CAPABILITY-GAP] flags.
-->
```

The attendee reads the comment, then writes the actual PRD section below it. One paragraph in their own words. Plain English — no code.

**Step 2: Update the CLAUDE.md pitch rule.**

The stub comment tells them which rule to add. For Stub D:

```
- For each RFP requirement: search capabilities/ by keyword match first,
  then description relevance. Use the best match only.
  Do not combine multiple capability files to cover a single requirement
  unless the RFP explicitly allows a consortium or sub-contractor approach.
```

**Step 3: Run `/prime` → `/plan` → `/implement`.**

```bash
> /prime
```

Claude reads the updated PRD and CLAUDE.md. Confirms the change. If the readback misses the pitch command: the stub section is not clear enough — fix the writing.

```bash
> /plan
```

Plan comes back. Read it. Typical plan for Stub D is 4–6 steps: a new `pitch` subcommand, a brief-reader function, a capability-matcher function, a proposal-formatter, and a file writer. If any step looks wrong, push back before approving.

```bash
> /implement
```

Claude executes. The whole change should be 60–120 lines — a new command, a simple matcher, a formatter. Watch the diffs.

**Step 4: Run the pitch.**

```bash
account pitch acme --rfp rfp/sample-rfp-globex.txt
```

Expected output: a markdown file in `proposals/`. It should contain:
- A personalised opening that references the Acme brief
- A section for each RFP requirement
- Two capability-matched sections (cloud migration, regulatory compliance)
- Three `[CAPABILITY-GAP]` flags (references, delivery window, on-site lead)

---

## Phase 4 — Pause and read the output (01:10 – 01:15)

Stop the room. Ask two or three people to read one section of their draft aloud:

- "Mine referenced the Q3 deadline from the brief. It said 'as discussed in your March procurement meeting' — that came from the interaction notes."
- "I got a [CAPABILITY-GAP] for the three-reference requirement. We only have two evidence entries. It didn't make something up — it flagged it."
- "One section matched cloud migration correctly. The evidence it cited matched our actual case study."

The room hears what the tool produced. The question to put to the room:

> *"Would you send this draft? Or does something need to change first?"*

Don't answer. Let them assess. That question is what Block 4 is about.

---

## When someone is stuck

1. **"Did you fill in the PRD stub AND update the CLAUDE.md?"** Missing one is the most common error. The PRD says *what* to build; the CLAUDE.md says *how* it should behave.
2. **"Run `/prime` and read the readback."** If Claude didn't understand the pitch command spec, the plan will be wrong. Fix the file, not the prompt.
3. **"What does `account pitch acme --rfp rfp/sample-rfp-globex.txt` output?"** Get real output or a real error before guessing.
4. **"Does your capability list show any entries?"** If `account capability list` is empty, the matcher has nothing to match against. Add at least one capability first.
5. **"Let's `/rewind` and re-plan."** `/rewind` undoes Claude's last set of changes. Don't hesitate — 80 lines written in three minutes can be rewritten in three minutes.

[← Back to home](../index.html)
