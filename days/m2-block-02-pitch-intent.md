# Module 2, Block 2 — Pitch Intent

**Time:** 00:10 – 00:30
**Goal:** Everyone has read the pitch PRD stubs, understands what the capability library is and why it matters, and has written at least one pitch rule in the CLAUDE.md. Not read it — written it. That shift from reader to author is the central beat of this block.

<!-- participant-start -->
## Block 2 — What to do

Read the spec, write a rule. That's the whole block.

1. Open `PRD.md` — read Stub D (pitch command) and Stub E (capability library)
2. Open `capabilities/` — look at the structure of one `.yaml` file
3. Open `CLAUDE.md` — read the one pitch rule at the top of the "Pitch rules" section
4. Think of one pitch rule that matters for *your* proposals:
   - What should the tool never claim you can do?
   - How should it handle a requirement where your match is partial — not a perfect fit but not impossible?
   - What tone or language constraints belong in proposals from your company?
5. Write your rule in plain English in the pitch rules section of `CLAUDE.md` — no code required
6. Activate Plan Mode: press **Shift + Tab twice** in Claude Code
7. Run `/prime` and wait for Claude to confirm it understood the updated spec
<!-- participant-end -->

## What happens in this block

1. **00:10 – 00:18 — Walk the PRD stubs aloud.** Stub D, Stub E. Pause at the capability library concept.
2. **00:18 – 00:27 — Live rule-writing exercise.** Read an RFP excerpt aloud. Ask the room what rule is missing. They dictate it. You type it into `CLAUDE.md`. Five minutes. Two or three rules.
3. **00:27 – 00:29 — Tour the slash commands.** Four commands, one sentence each.
4. **00:29 – 00:30 — Q&A.** Three questions. Park the rest to Block 6.

---

## Walk the PRD stubs (00:10 – 00:18)

Open `PRD.md`. Read Stub D and Stub E aloud — they are short by design.

**Stub D — The pitch command.** `account pitch --rfp <file>` takes an RFP document and produces a draft proposal. It reads two sources: the account brief (from `account brief <name>`) and the capability library (from `capabilities/`). It maps RFP requirements to matching capabilities. It drafts a section for each requirement. Where no capability matches: it flags `[CAPABILITY-GAP]` instead of inventing.

**Stub E — Capability library.** The `capabilities/` folder is a set of plain-text YAML files (a simple structured format — key: value, readable by both humans and the tool). Each file describes one thing your company can do: a service, a product, a delivery track record, a certifications. The `account capability add` command adds entries. `account capability list` shows what's there.

Show one seed entry on screen. Read it aloud:

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

> *"This is the library. The tool does not invent capabilities beyond what is in here. If an RFP asks for something you don't have a capability file for, the proposal says [CAPABILITY-GAP] — not a confident paragraph about something you've never done.*
>
> *That flag is the most important feature in this tool. It protects you from a proposal that promises something your delivery team will have to explain away six months later."*

### The capability library concept

Say this once, slowly:

> *"A new proposal starts with: what do we do well? Most teams answer that question from scratch every time — digging through old decks, asking a colleague what we called that thing we did for Aramco. The library is the answer written down, once, in the format the tool can read. Every new pitch draws from it. You don't start from scratch. You accumulate."*

This is Claim 1:

> *A proposal that starts from scratch every time is a proposal that forgets what worked before. The capability library accumulates your best pitch language.*

---

## Live rule-writing exercise (00:18 – 00:27)

This is the block's central moment. Do not skip it or convert it to a readthrough.

**What the seed CLAUDE.md ships with:** the Stack, Layout, Conventions, and Extraction rules sections filled in. The Pitch rules section has one pre-written example rule — showing the format — and a blank space below it.

**The exercise:**

Open `CLAUDE.md`. Read the pre-written rule aloud:

> *"Only match RFP requirements to capabilities that exist in the capabilities/ folder. Never invent a capability. If no match: flag [CAPABILITY-GAP]."*

Then read this excerpt from `sample-rfp-globex.txt`:

> *"The successful vendor will demonstrate prior experience delivering regulatory-compliant cloud migration at enterprise scale, with a minimum of three verifiable government or financial-sector references."*

Ask the room:

> *"What rule is missing? The tool has a cloud migration capability — but what about the three-reference requirement?"*

Wait. Someone will say: *"It should check whether we actually have three references in the evidence field before it commits to that claim."*

Type the rule into `CLAUDE.md`, in the room, as they dictate. Roughly:

```
- When an RFP requires a minimum number of references or case studies:
  count the evidence entries in the matched capability file.
  If the count is below the requirement: flag [INSUFFICIENT-EVIDENCE <N> required, <M> available].
  Do not present partial evidence as full evidence.
```

Then read this excerpt:

> *"We lost a bid last year because the proposal promised a delivery timeline we couldn't actually hit. The RFP asked for 90-day delivery. We matched it to our migration capability and said yes. It took 180 days."*

Ask:

> *"What rule prevents that?"*

They'll get it: the tool should not match timeline requirements to capabilities unless the capability file explicitly states a delivery window.

```
- Timeline claims must be supported by an explicit delivery_window field
  in the capability file. If the field is missing: flag [TIMELINE-UNVERIFIED].
  Do not infer a timeline from the description text.
```

Stop after two or three rules. Block 3 is where they build more.

**What just happened:** they have written business rules that directly govern what a language model is allowed to claim about their company. No code. The insight to land:

> *"The CLAUDE.md pitch rules are the guardrails on your proposal. If the tool ever produces something you wouldn't sign, the fix is a new rule — not a rewrite of the output. You own the spec. Claude builds to it."*

### If the room is slow to respond

Don't fill the silence with your own answer. Ask more specifically:

> *"The RFP asks for three government references. We have two. Should the proposal say 'we have extensive government experience' — or something else?"*

Someone will say: *"It should say we have two, or flag it."* That's enough. Type it.

### What not to do

- Don't read a pre-filled CLAUDE.md as a document to study. The insight only lands when they write the rule.
- Don't try to fill all the stub space. Leave room — that's for Block 3.
- Don't let anyone say "make the AI more accurate." Ask: *"What rule, specifically, would produce accurate output here?"*

---

## The four slash commands (00:27 – 00:29)

Same commands as Module 1, same format:

| Command | What it does |
|---|---|
| `/prime` | Reads `PRD.md` and `CLAUDE.md`, confirms what it understood. If the readback misses a pitch rule you wrote, the rule is not clear enough — fix the file. |
| `/plan` | Produces a written, numbered plan. Does not write code. Waits for your approval. |
| `/implement` | Executes the approved plan, step by step. |
| `/verify` | Runs the proposal verification checklist: did it cover all RFP sections? Did it reference only real capabilities? |

One thing to say about `/verify`:

> *"Verify is not spell-check. It's checking whether the proposal made claims the capability library doesn't support. That check is what makes this tool worth using."*

---

## Common questions in this block

- **"Can I add my own capabilities before we start?"** Yes. Run `account capability add` or drop a `.yaml` file directly into `capabilities/`. But write it clearly — the tool reads exactly what you write.
- **"What if our capabilities are confidential — we don't want them in a file?"** The `capabilities/` folder lives on your machine, not in the cloud. It's as private as a spreadsheet on your laptop.
- **"What if the RFP is a PDF?"** The tool handles `.pdf` and `.txt`. Scanned images will not work — the text must be machine-readable. If in doubt, paste the text into a `.txt` file.

[← Back to home](../index.html)
