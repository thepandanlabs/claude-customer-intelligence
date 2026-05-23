# Module 1 · Block 4 — Verify

**Time:** 01:25 – 01:40
**Goal:** Every attendee answers three verification questions about their enhanced tool, using the hand-labelled Acme Software account as the reference. The discipline of "right, not just plausible" becomes concrete — without requiring any code knowledge.

<!-- participant-start -->
## Block 4 — What to do

Three verification questions. Answer each one with evidence from the tool output.

1. Run `account brief acme-software` — look at the output in detail
2. Compare your output to the facilitator's hand-labelled answer sheet (shown on screen)
3. Answer these three questions:
   - **Did it catch everything?** Count open commitments in the label vs. your brief
   - **Did it invent anything?** Any item in your brief that doesn't come from a real interaction file?
   - **Is it consistent?** Run `account add acme-software inbox/acme-software/` again — confirm zero new rows
4. If time allows: run `account export` and open `dashboard.html`
<!-- participant-end -->

## Why this block exists

A tool that "looks right" is not a tool. It's a demo.

The difference: a tool that *is* right has been checked against a known-correct answer. You know what should come out. You ran it. You compared. It either matched or it didn't.

That check is called an eval — short for evaluation. It's the same discipline a software team uses with automated tests, just without the code ceremony. Three parts: a prepared input, a correct answer you labelled by hand, and a pass/fail comparison. For an account intelligence tool in a business context, any account manager can run one. The only requirement is the willingness to write down what the right answer is *before* you run the tool.

---

## What the facilitator prepared before the session

Before the room arrived, the facilitator read all 8 interaction files in `inbox/acme-software/` and hand-labelled the correct commitments, risks, and competitor mentions. The label is printed on paper or shown on screen.

### Hand-labelled answer: Acme Software

**Open commitments (account team → client):**

| # | Content | Owner | Deadline | Source file |
|---|---|---|---|---|
| 1 | Send revised SLA terms after legal review | Ahmed | TBD | 2026-04-21-scoping-notes.txt |
| 2 | Provide reference customer list (similar verticals) | Sarah | TBD | 2026-04-21-scoping-notes.txt |
| 3 | Share integration architecture diagram | Sarah | 2026-05-30 | 2026-05-18-call-notes.txt |

**Key risks:**

| # | Risk | Evidence |
|---|---|---|
| 1 | Integration timeline concern | Flagged in 3 of 8 interactions |
| 2 | No confirmed exec sponsor on client side | Mentioned in 2026-05-18 call notes |

**Competitor mentions:**

| # | Competitor | Mentioned in | Count |
|---|---|---|---|
| 1 | Salesforce | 2026-05-04-email.txt, 2026-05-18-call-notes.txt | 2 |

This is the ground truth. Three commitments, two risks, one competitor. Hand-labelled by the facilitator from reading the source files.

---

## The three verification questions

Ask every attendee to run:

```bash
account brief acme-software
```

Then answer three questions:

**Question 1 — Did it catch everything? (Recall)**

> *"Does your brief show all three commitments from the label? If any are missing, the tool has a recall problem — it didn't surface something that was actually there. That's a spec problem: the CLAUDE.md extraction rule needs to be clearer about what counts as a commitment."*

Count them explicitly. Don't skim. A missing commitment from the brief means someone in your team doesn't know they have an open obligation.

**Question 2 — Did it invent anything that wasn't there? (Precision)**

> *"Does your brief contain anything that doesn't come from the real interaction files? An extra commitment that wasn't made, a competitor that wasn't mentioned? If so, the tool created false data. That's worse than missing something — you now have a record in your ledger that isn't real."*

Check each commitment in the brief against the source files. If something can't be traced to a real file, it's a hallucination. Find the rule in CLAUDE.md that let it through and tighten it.

**Question 3 — Is the output the same if you run it twice? (Determinism)**

```bash
account add acme-software inbox/acme-software/
```

Run it again. The answer should be: `0 new records. 8 files skipped (already processed).`

> *"Same input, same result, every time. That's what makes this a tool and not a demo. Six months from now, when a client says 'you promised us a reference list in April,' you can point to the ledger and confirm — or dispute. That reliability comes from this check."*

---

## What a good result looks like

If an attendee's tool returns all three commitments, no extras, and deduplicates correctly — they're done. That's the bar.

**If it's missing one:** look at the CLAUDE.md extraction rule. Is the rule clear enough that Claude would recognise the missed item in the raw text? Probably not — tighten the language. A good test: read the rule aloud to a colleague and ask if they'd identify the same thing in the transcript.

**If it invented one:** look at the source files. Is there anything in the raw text that could be misread as a commitment? Update the rule to add a counter-example — something like: *"Do not extract client-side commitments as account team commitments. The account team is us, not the client."*

**If the second run adds records:** the deduplication logic is broken or the stub was implemented without it. Ask Claude to fix idempotency and re-run `/verify`.

---

## The three verification questions, written on the board

Write these up at the front before Block 4 starts:

> **1. Did it catch everything?** — Recall
> **2. Did it invent anything?** — Precision
> **3. Does it produce the same result twice?** — Determinism

These three questions are the complete verification framework for any LLM-powered extraction tool. No code. No test runner. Just: do you know what the right answer is, and did you get it?

The hard part is not the comparison — it's writing down the right answer before you run the tool. The tool will always produce *something*. The question is whether *something* is *correct*.

---

## What to say from the front of the room

> *"Every team that ships AI-powered tools has a version of this process. The gap between a working demo and a trustworthy tool is not the model — it's whether anyone wrote down what 'right' looks like before running it. You just did. That discipline — known input, known answer, pass/fail — is the whole thing."*

---

## Outputs from this block

- Every attendee has compared tool output to a pre-labelled ground truth for a real-shaped account.
- Every attendee can name the difference between a recall failure (missed commitment) and a precision failure (invented commitment).
- Every attendee has confirmed that re-running `account add` on the same folder adds zero new records.
- The three verification questions are named and understood.

---

[← Back to home](../index.html)
