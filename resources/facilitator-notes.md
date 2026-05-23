# Facilitator Notes — Module 1

Practical guidance for running the Customer Intelligence & Pitch Suite workshop. Read this the evening before, not the morning of.

---

## Before the room opens

**The day before:**

- [ ] Clone the seed repo and run it yourself. Run `account add` on all four accounts. Check that `account brief acme-software` returns sensible output. If anything is broken, you have time to fix it.
- [ ] Hand-label the Acme Software account. Read the 8 files in `inbox/acme-software/` and write down the correct commitments, risks, and competitor mentions. This is your Block 4 answer sheet. Don't skip this — without it, Block 4 has no ground truth.
- [ ] Print the answer sheet or set it up on a second screen. You'll display it during Block 4.
- [ ] Prepare the bad-prompt demo. Open Claude.ai in an incognito window with no files attached. Know exactly what you're going to type.

**The morning of:**

- [ ] Arrive 30 minutes early. Set up the main display. Confirm you can project your terminal.
- [ ] Put the repo on a shared drive link or USB if any attendees need it at the last minute.
- [ ] Write on the whiteboard, visible from the back of the room: the three claims. These anchor every block.
- [ ] Test the projector with the terminal font at full size. Small terminals lose the back row.

**Room setup:**

- Tables facing the main screen, not theatre-style rows. People need to use laptops.
- Power strips on every table. Laptop work with no power is a distraction after 45 minutes.
- A clear aisle between tables so you can circulate during Block 3 without asking people to move.
- Water on tables. This is a 2-hour session with a lot of reading and writing.

---

## Attendee types and how to handle them

In a room of non-technical managers and sales professionals, you'll usually encounter five types. Recognising them early lets you adapt without losing the room.

**The Skeptic**

*Signs:* Arms crossed, one-word answers to your questions, occasionally audible sighs. Often a senior person who was told to attend and doesn't see the point.

*What they're actually thinking:* "I've seen AI demos before. It looked impressive and then nothing changed."

*What to do:* Don't try to convince them in the first 20 minutes. Let the killer demo do the work. When the brief appears in 3 seconds with the Acme commitments, ask them directly: "How long would that normally take you?" Don't argue — ask. The number they give you is the argument. In Block 3, pair them with a specific stub that matches their actual job. They often become the most rigorous verifiers in Block 4.

*What not to do:* Don't call them out in front of the room. Don't oversell. Don't say "imagine if this scaled to your whole team" in the first 10 minutes — that triggers the "demo" alarm.

**The Eager Beaver**

*Signs:* Already has 5 questions before Block 1 is done. Opens their laptop immediately. Asks whether they can connect it to Slack right now.

*What they're actually thinking:* "This is exactly what I've been waiting for. Can we skip ahead?"

*What to do:* Give them a job. Point them at Stub A and tell them to start writing the PRD section while you're doing the Block 2 exercise with the rest of the room. In Block 3, they're fine on their own — check in once.

*What not to do:* Don't let them run ahead in Block 1. The killer demo only works if everyone watches it together. Don't let them answer the facilitator's questions for the room — the "What's missing?" moment needs to come from someone who doesn't already know.

**The Silent One**

*Signs:* Polite, attentive, takes notes, but says nothing in group exercises. Not unengaged — just processing.

*What they're actually thinking:* Often "I'm not sure my question is smart enough to ask aloud."

*What to do:* In the rule-writing exercise (Block 2), go to them directly: "What's one thing from your accounts that you track manually right now that feels like it should be automatic?" They usually have a very specific answer that makes a good rule.

*What not to do:* Don't cold-call them for the "What's missing?" question in Block 1 — that's a high-stakes moment and they'll feel put on the spot. Engage them individually during Block 3 when the room is working on laptops.

**The "Can I Do This in Excel?" Person**

*Signs:* First question is "couldn't I do this in a spreadsheet?" or "we already have a CRM for this."

*What they're actually thinking:* "Why do I need to build a tool when we have tools?"

*What to do:* Acknowledge it. *"A spreadsheet is great for structured data you enter manually. The problem is the input — a call note is not structured. You'd have to read 8 files and fill 24 rows by hand. The tool reads the files and fills the rows automatically. You're not replacing the spreadsheet — you're removing the manual extraction step."* Then run `account query --open` live. The cross-account view is the answer — CRMs don't generate briefs from unstructured notes.

**The Worried About Data Person**

*Signs:* Asks early about where the data goes, who can see it, whether the client emails are safe.

*What they're actually thinking:* "I cannot put confidential client information into an AI system."

*What to do:* This is a legitimate concern, not a red flag. Address it directly: *"The tool runs entirely on your own laptop. Nothing goes to a server. The only external call is to the Claude API — the same API that powers Claude.ai, with the same Anthropic data policies. For this workshop, we're using fictional accounts, so nothing you process today is real client data."* For their real use: point them to Anthropic's enterprise API data policies. If their company has specific restrictions, they should check with their security team before running real client data through any AI API.

---

## Pacing tips per block

**Block 1 (00:00–00:20)**

The bad-prompt demo is the most important 4 minutes in the module. Don't rush it. Let the silence after "What's missing?" breathe — 5 seconds of silence feels long but it works. If no one answers in 8 seconds, ask the question more specifically: *"If I open this tab again tomorrow, what does it know about Acme?"*

The killer demo (running `account add` and `account brief`) should be smooth and fast. Practice it twice the day before so the commands flow without hesitation.

If you're running behind by 00:15: cut the third claim (verification) short and say *"We'll come back to why verification matters — you're about to experience it."* Block 4 will make the claim without you stating it.

**Block 2 (00:20–00:40)**

The rule-writing exercise is not optional. If you're behind, cut the PRD walkthrough short — not the rule-writing. A 5-minute exercise where attendees author a rule produces more learning than a 10-minute PRD walkthrough. The insight that they are writing the spec that governs AI behaviour is the central beat of the workshop.

If the room writes a rule that's technically wrong (e.g., a rule that would match too broadly), write it anyway and note it: *"Let's run this and see what it catches. If it's too broad, we'll tighten it in Block 4."* Don't correct people mid-exercise — let the tool correct them.

**Block 3 (00:40–01:25)**

The first 8 minutes (Plan Mode demo) need to be projected clearly. Font size 18 minimum. Narrate every keypress — many people in the room have never seen a terminal before.

During the 25-minute working period (01:00–01:25), circulate constantly. Don't stand at the front. The people who need help won't raise their hands — they'll quietly stare at a stuck terminal.

Common thing to find: someone who edited the PRD but forgot to update the CLAUDE.md. Check both files whenever someone says "it's not working." The other common issue: someone who ran `/implement` without reading the plan. They're often stuck because Claude built something they didn't want. The fix is `/rewind` and a more careful read of the next plan.

If a third of the room finishes early: ask them to try a second stub. Don't let idle time accumulate — it breaks momentum for the room.

**Block 4 (01:25–01:40)**

Display the hand-labelled Acme answer sheet before you ask anyone to run `account brief`. The comparison only works if the answer is visible first.

Walk the three verification questions slowly. Many attendees have never heard the words "recall" and "precision" in a technical context — explain each one with the plain-English version: *"Did it miss anything? Did it make something up?"*

The determinism check (running `account add` a second time and seeing zero new rows) always gets a reaction. Pause for it. That moment — "it didn't add duplicates" — is when the structural advantage of a tool over a chat tab becomes tangible.

**Block 5 (01:40–01:50)**

Don't try to explain all four tracks in detail. Read the table aloud, ask people to pick by what they'd actually use, and get them reading a track page. The plan is the deliverable — not the implementation.

If the room is tired or behind schedule: make it simple. *"Pick Module 2 or Track B. Both are an evening of work. Read the starting prompt and paste it in."*

**Block 6 (01:50–02:00)**

Go around the room for one-line takeaways before the three-files wrap — not after. Ending on attendee voices is better than ending on yours. The send-off line ("You came in with a chat tab...") lands best when the room has already heard 8 people articulate what they built.

Don't run over. Respect the 2-hour commitment. If you hit 02:00 mid-sentence, stop. People who want to keep going will ask.

---

## What to do when things go wrong

**The demo fails (account add throws an error)**

Don't panic. Say: *"The demo broke — which is actually useful. This is exactly what happens when you're building real tools. Let me show you how to diagnose this."*

Open the error message. Read it aloud. Then fix it live — or if it's a setup issue, switch to a pre-recorded screen capture of the working demo. Have one ready.

**Half the room's laptops aren't set up**

Shift to pairs immediately. One working laptop per pair is enough for Blocks 2, 3, and 4. The person without a working laptop should be the one writing the spec — driving the PRD and CLAUDE.md while their partner runs the commands.

Fix the broken setups at the break using the setup guide. Don't try to do it from the front of the room.

**The room finishes Block 3 early**

Good problem. Use the extra time for Block 4 — more time on verification is always worthwhile. Or open the Q&A you parked from Block 1.

**The room is behind by Block 3**

Cut the Phase 4 surface-and-share (01:20–01:25) short. Go straight to Block 4 at 01:20. Block 4 can compress to 10 minutes (skip the extended discussion, just run the three questions). Block 5 can be 5 minutes — just pick a track.

Don't skip Block 6. The wrap is 10 minutes and it lands the workshop.

**Someone builds something that clearly doesn't work**

Don't fix it for them. Ask: *"Run `/prime` and read back exactly what Claude said it understood."* Then: *"Does that match what you intended?"* If not: *"Fix the sentence in CLAUDE.md that caused the misunderstanding. Then run `/prime` again."*

The loop — write, run, compare, fix — is the discipline. Let them experience it, even if the fix takes 3 more minutes than just editing the file yourself.

**A senior attendee pushes back on the whole premise**

*"We have Salesforce for this."* or *"This is a toy. Our accounts are more complex."*

Agree with the premise, then reframe: *"Salesforce is great at tracking what you enter. The gap is the 40% of account intelligence that lives in emails and call notes you never had time to enter. This tool reads those files. It's not replacing your CRM — it's feeding it."*

If they're still resistant after the killer demo: let it go. One unconvinced person in a room of 15 is not the session's job to solve. The sessions after this one are.

---

## The single most important thing to get right

The rule-writing exercise in Block 2. If attendees leave the session having only watched the facilitator type rules, the workshop produced a demo. If they leave having written at least one rule themselves — in their own words, for their own domain — they understand what they built and why. That's the difference between inspiration and capability.

Everything else can run imperfectly. The rule-writing exercise cannot.

---

[← Back to home](../index.html)
