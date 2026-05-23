# Module 1 · Block 1 — Setup & The Thesis

**Time:** 00:00 – 00:20
**Goal:** Every laptop verified working. Every attendee understands why a chat tab and a purpose-built tool are structurally different — not in intelligence, but in what they remember.

<!-- participant-start -->
## Block 1 — What to do

Settle in and watch. This block belongs to the facilitator. No code yet.

1. Run `account --help` in your terminal when the facilitator asks.
2. Watch the Claude.ai demo first. Pay attention to what it cannot do.
3. Watch the `account` tool demo second. Notice what changed.
4. When the facilitator asks *"What's missing?"* — answer out loud.
<!-- participant-end -->

## The shape

| Time | Activity |
|---|---|
| 00:00 – 00:10 | Soft start. Tool check. Late arrivals settle. |
| 00:10 – 00:18 | The opening reframe. The three claims. The killer demo. |
| 00:18 – 00:20 | Q&A — two questions maximum. Park the rest. |

---

## Tool check — first 10 minutes

While people are arriving and getting settled, ask everyone to open a terminal and run:

```bash
claude --version     # should print a version number
claude doctor        # should show green checkmarks
python --version     # should be 3.11 or higher
```

Then confirm the seed repo is in place and the `account` tool is available:

```bash
cd account-seed-repo
account --help
```

Expected output: a short list of commands — `add`, `brief`, `query`, `list`, `export`, `pitch`.

If someone's setup is broken: pair them with a working neighbour immediately. Don't spend group time on one person's install — fix it at the next break.

---

## Opening reframe (say this at 00:10, before the claims)

Many people in the room heard "How to Code with AI" and assumed this meant writing Python or JavaScript. Correct that now — not apologetically, but as a reveal:

> *"Quick reframe before we start — what 'coding with AI' actually means for people in this room.*
>
> *Traditional coding: a developer types instructions that a computer executes.*
>
> *Coding with AI: you write a spec precise enough that an AI can execute it without guessing. The AI writes the instructions. You make the decisions that matter — what to build, what to extract, what counts as correct.*
>
> *That's the skill. And it turns out account managers and sales leaders are often better at it than developers, because you already know the domain. You know what a commitment sounds like in a client call. A developer would have to ask you. Today you're going to write the rules. Claude Code will write every line of Python. By the end, you'll have a working tool — and you'll understand exactly which part of that process you owned."*

---

## The three claims

State each one clearly. Don't rush past them — they are the thesis of the module.

**Claim 1: A chat tab has no memory of your client history. This tool does — and it accumulates across every interaction you add.**

> *"You've pasted a client email into Claude or ChatGPT and asked it to summarise. You got something useful. Then you closed the tab. Next week, you opened a new session and it knew nothing — not the previous call, not the commitment the client made, not the open item from three months ago.*
>
> *The tool you're building today persists. Every email, call note, or meeting transcript you process adds to a ledger. Every open commitment is queryable — across accounts, across dates, across whoever made the promise. A chat tab is a notepad with no pages. This is a ledger."*

**Claim 2: The spec is the product. The extraction rules you write in CLAUDE.md determine what gets captured. You write them; Claude executes them.**

> *"In about 20 minutes we're going to write extraction rules in plain English — things like 'flag any sentence where the client mentions a competitor' or 'extract every commitment the account team made, with a deadline.' Claude will read those rules and build the tool to match them.*
>
> *You know which signals matter in your client conversations. A developer building this from scratch would need you to explain each one. You don't have to — you already know. That knowledge goes directly into the spec."*

**Claim 3: Verification makes it real. "It looked right" is not a guarantee. You hand-label one account's interactions and check whether the tool caught everything.**

> *"At some point today you'll run the tool on real-shaped data, then compare the output to what you know was there. That check — known input, known right answer, pass or fail — is an eval. It's the same thing software teams use to confirm tools work. The only difference is you don't need to write code to run one. You just need to know what the right answer is."*

---

## The killer demo (do this live, on the main screen — 00:12 to 00:18)

### Part 1 — What a chat tab cannot do

Open a fresh Claude.ai session. No files attached. Type, verbatim:

```
Brief me on the Acme Software account. What are the open commitments?
```

Claude will respond with something polished and useless: a generic template, or a helpful explanation that it has no access to your account data.

Ask the room:

> *"What's missing?"*

Wait. Don't fill the silence. Someone will say: *"It doesn't know anything about Acme."* Or: *"There's no history."* That sentence — whatever version surfaces — is the thesis.

Say:

> *"Exactly. The chat tab starts blank every single time. It has no memory of that client conversation last week, no record of the commitment you made in March, no way to show you what's still open across four accounts at once. We're about to change all three of those things."*

Close the Claude.ai tab.

### Part 2 — What the tool does

Switch to the terminal. The seed repo has 4 pre-populated accounts already sitting in `inbox/`.

Run, live:

```bash
account add acme-software inbox/acme-software/
```

You'll see it process 8 files. Takes a few seconds.

```bash
account brief acme-software
```

Structured brief appears in about 3 seconds:

```
## Acme Software — Account Brief

**Last contact:** 2026-05-18 (call — integration timeline review)
**Relationship owner:** Sarah Okafor

### Open commitments
- [ ] Send revised SLA terms by 2026-05-30 (us — Sarah)
- [ ] Confirm staging environment access (them — Acme IT)
- [ ] Provide reference customer list by 2026-06-07 (us — Ahmed)

### Key risks
- Integration timeline slipping: client flagged concern in 3 of 8 interactions
- No exec sponsor confirmed on their side
- Competitor mention: Salesforce named twice in last 30 days

### Last 3 interactions
- 2026-05-18: Call — integration timeline, SLA discussion
- 2026-05-04: Email — reference request, follow-up outstanding
- 2026-04-21: Meeting notes — scoping session, 3 open items logged
```

Now run three more:

```bash
account add globex-consulting inbox/globex-consulting/
account add initech-retail inbox/initech-retail/
account add umbrella-corp inbox/umbrella-corp/
```

Each one is fast — same speed as the first, because the ledger accumulates.

```bash
account query --open
```

All open commitments, across all four accounts, in one view.

Ask the room:

> *"How long did that take? The brief you just saw on Acme — how long would it normally take you to pull together from emails, call notes, and CRM entries?"*

Let them answer. Then:

> *"That brief ran in 3 seconds because the ledger accumulated everything. That's the structural advantage — not that Claude is clever, but that the tool remembered and you didn't have to re-paste everything."*

---

## What the room should leave Block 1 knowing

- Coding with AI means writing a spec, not typing syntax. Claude writes the code. You write the rules that determine whether the code is right.
- A chat session forgets. A tool accumulates. These are structural differences, not quality differences.
- The CLAUDE.md and PRD are the decisions that matter. Claude writes everything else.
- Verification is not a developer concept — it's "did the tool catch what was actually there?"

---

[← Back to home](../index.html)
