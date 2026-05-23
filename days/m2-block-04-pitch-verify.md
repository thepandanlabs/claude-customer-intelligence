# Module 2, Block 4 — Verify

**Time:** 01:15 – 01:30
**Goal:** Every attendee has run the verification checklist on their pitch output and identified at least one thing the tool got wrong or left unaddressed. The habit of checking the output before sending it is the lasting takeaway from this block.

<!-- participant-start -->
## Block 4 — What to do

Read the proposal output your tool just produced. Check it against the RFP. This is your job — not Claude's.

1. Open the proposal file that `account pitch` generated (in `proposals/`)
2. Open the RFP (`rfp/sample-rfp-globex.txt`) side by side
3. Go through every RFP requirement:
   - Did the proposal address it?
   - If it matched a capability: is that capability real — does the file exist in `capabilities/`?
   - If it made an evidence claim: is the evidence actually in the capability file?
   - Did it invent anything you don't have?
4. Run `/verify` to cross-check your manual read:
   ```bash
   > /verify
   ```
5. Compare what you found manually to what `/verify` caught. Did `/verify` miss anything?
6. Fix what needs fixing — either update a capability file, update a CLAUDE.md rule, or note a `[CAPABILITY-GAP]` that needs a real answer before this proposal goes out
<!-- participant-end -->

## Block shape

| Time | Activity |
|---|---|
| 01:15 – 01:20 | **Verify framing.** What you're checking for and why. The three failure modes. |
| 01:20 – 01:28 | **Attendees verify their own proposals.** Manual check, then `/verify`. |
| 01:28 – 01:30 | **Surface findings.** Two or three people share what they found. |

---

## Verify framing (01:15 – 01:20)

This is Claim 3. Say it plainly:

> *"The tool can be wrong. Not randomly — it has rules. But wrong in specific ways that the rules don't catch. Your job right now is to find those ways."*

Three things to look for. Put them on screen:

**1. Did it address all RFP requirements?**

Count the sections. The sample RFP has five requirements. The proposal should have five sections — either a matched capability or a `[CAPABILITY-GAP]` flag. A missing section means a requirement was not addressed. That is a harder error than a gap flag. A gap flag you can fix before submission. A missing section you might not notice until the client points it out.

**2. Did it match RFP requirements to capabilities that actually exist?**

Open `capabilities/` and look at what's there. Now look at the proposal. Every capability claim should trace to a file in that folder. If the proposal says "our certified regulatory compliance track record" and the only regulatory capability file is `regulatory-compliance-advisory.yaml` — does that file support the specific claim made? Or did the tool generalise beyond the evidence?

**3. Did it invent anything?**

This is harder to spot. It looks like confident, well-written prose. Look for:
- Specific numbers not in the evidence field ("we have delivered 20+ migrations")
- Timeline claims not in the capability file ("our typical assessment phase is 60 days")
- Reference claims not backed by evidence entries ("as trusted by [company name]")

> *"If you find something invented: that is not a reason to distrust the tool. That is the tool telling you your CLAUDE.md rule is missing a case. Write the rule. The next proposal won't do it."*

---

## Attendees verify their proposals (01:20 – 01:28)

Work individually. Two phases:

**Phase 1: Manual check (01:20 – 01:25)**

Open the proposal and the RFP side by side. Go through each requirement. Take notes:
- Addressed correctly
- Addressed but evidence is thin
- `[CAPABILITY-GAP]` — correct flag
- Missing — no section at all
- Invented — a claim not supported by the capability file

Most attendees will find at least one issue. Common ones on the sample RFP:

- The three-reference requirement: the tool matched the cloud migration capability but cited two evidence entries against a requirement of three. Correct to flag `[INSUFFICIENT-EVIDENCE]` — but only if the rule was written in Block 2. Without the rule: the tool may have written a confident paragraph with two examples and no flag.
- The on-site lead requirement: no capability file covers this. If the tool produced a `[CAPABILITY-GAP]` flag: correct. If it drafted a paragraph anyway: a rule is missing.
- The 90-day delivery window: the tool may have matched the cloud migration capability (which mentions "90-day hypercare") and claimed a 90-day delivery window — but "hypercare" (post-migration support) is not the same as the assessment phase the RFP requires. This is a capability-to-requirement mismatch. The rule to write:

```
- Do not conflate delivery phases. "90-day hypercare" (post-migration support)
  is not the same as "90-day delivery window" (time to complete migration).
  Match the phase the RFP specifies — not the number.
```

**Phase 2: Run `/verify` (01:25 – 01:28)**

```bash
> /verify
```

The verify command runs the checklist: requirement coverage, capability file existence, evidence presence. It reports what it found.

Compare the `/verify` output to the manual check:
- What did `/verify` catch that the manual check caught?
- What did the manual check catch that `/verify` missed?
- What did `/verify` flag that the manual check would have missed?

The most important outcome: `/verify` is also not infallible. It runs the rules in CLAUDE.md. If the rule was not written, the check does not happen. The manual read is not optional — it's the backup to the automated check.

---

## Surface findings (01:28 – 01:30)

Stop the room. Ask two or three people:

> *"What did you find? One sentence."*

- "The tool drafted a timeline section that wasn't in the capability file. I'm adding a rule."
- "It missed one RFP requirement entirely — the on-site lead. No section, no flag. I need to trace why."
- "It flagged three gaps correctly. I know which two we can actually fill — I need to add capability files for them."

Then say:

> *"Every finding here is a CLAUDE.md rule waiting to be written. The verify step is not where you fix the prose. It's where you find the gap in the spec — so the next proposal is better before it starts."*

---

## If someone's proposal looks perfect

Healthy skepticism:

> *"Read the evidence claims one more time. Pick one number or one specific claim. Can you trace it to the exact line in the capability file? If yes — great. If not — where did it come from?"*

This usually surfaces something. If it genuinely looks clean, ask:

> *"What would happen if you ran this on an RFP for something you definitely can't do? Does it flag gaps, or does it write prose for a capability you don't have?"*

---

## What happens with the gaps

Gaps found in verify have three destinations:

1. **A new CLAUDE.md rule** — if the tool produced wrong output due to a missing rule. Write it now.
2. **A new or updated capability file** — if the gap is a real capability you have but haven't documented. Add it and re-run the pitch.
3. **A real capability gap** — if you genuinely don't have this capability and shouldn't claim it. Leave the `[CAPABILITY-GAP]` flag. That is the correct output. The human's job is to decide whether to pursue the bid, find a partner, or decline.

> *"A proposal with [CAPABILITY-GAP] flags is more honest than a proposal without them. The flags show you checked. That is a feature, not a failure."*

[← Back to home](../index.html)
