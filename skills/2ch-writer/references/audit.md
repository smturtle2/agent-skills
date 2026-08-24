# Thread Audit Guide

Companion to the audit step in SKILL.md. The rules live in the contract; this file
teaches how to *find* violations from the reader's side, and names the repair for each —
plus a scan for the specific artifacts the language model's default register leaks into
board text. Read before auditing any draft.

## Contents

- [Board reward channels](#board-reward-channels)
- [Reader simulation](#reader-simulation)
- [Residue scan](#residue-scan)
- [Calibration: when to stay open](#calibration-when-to-stay-open)

## Board reward channels

A thread rewards the reader through overlapping channels; when a thread feels off and
you can't name why, diagnose by channel — which one broke?

- **Lived-in board authenticity.** The thread is a place with history: concrete detail,
  internal consistency, posters who know their world. Breaks when: fake-precise details
  (bland numbers, generic names), a setting with no texture, an OP who seems to know the
  whole plot before the room does.
- **Voice pleasure.** The *way* people talk is the reading pleasure in board fiction —
  a killer retort, a repeatable tick, a tic you'd copy in real life. Breaks when every
  post could be authored by one competent person; no post contains a line worth quoting.
- **Mind simulation.** Readers model each poster as a mind with stakes, blind spots, and
  a temper — "that's so him", or worry when a regular goes quiet. Breaks when posters
  exist to deliver lines and nobody has anything to lose.
- **Curiosity / prediction.** The reader wants the next post and holds a private theory,
  satisfied or upended. Breaks when information arrives pre-digested, when the thread
  explains what the reader was about to ask, when the strongest moment — the reader's
  own theory being wrong *and mattering* — never happens.
- **Flow / rhythm.** Reading stays easy; meat and texture alternate so the page breathes.
  Breaks when posts are all the same width in a row, when a stretch is all short one-
  liners (meat) or all exposition, or when a single post buries its point mid-wall.

Diagnosis is a ladder: name the weakest channel, fix that channel first. Do not balance
all five.

## Reader simulation

State the persona before reading — a local who clicked the thread because it involves
their area, versus a stranger who stumbled into it. Give the persona their knowledge
boundaries: what they know from living, what they'd miss.

Read from the top, once, as that person. Track the felt experience and anchor it to the
text (post number + short quote):

- where you leaned in, where you drifted;
- the questions you were holding, and the moments they changed (a thread's pivots);
- the moments the thread started performing for you — a tidy info-dump, an instant
  expert who settles everything and gets believed, a payoff that's clean and expected;
- the moment the room's deduction runs ahead of the evidence.

Stay a reader during the read. The report is the experience; the mechanism checks come
after, in the audit tests. A report that says "it was fine" has found nothing — push to
the specific post that flattened, and name the channel it broke.

## Residue scan

The language model's default register is the average of everything it read; producing it
costs less than overriding it, so it leaks into every poster at once. Each artifact below
is a *tell* — only a problem once it's not serving a voice. Name the tell, then
restructure toward its alternative. Antidote is calibration, not reversal: a tell that a
character would naturally produce is fine; the same tell across every post is the default
register showing through.

| Tell (closed set) | Looks like on a board | Restructure to |
|---|---|---|
| Parallel-construction runs | consecutive posts with mirrored clause structure — same measure, same closing rhythm | break the meter: a fragment, a false start, an interrupted line |
| Uniform post shapes | posts of similar width and cadence in a row | let one be a one-liner, one end mid-vowel, one be a clipboard paste |
| Connective glue | "그리고", "또한", "이후", "마침내" — relationships carried by words instead of sequence | cut the word; leave the sequence to carry the relationship |
| Essay metaphor in a casual post | a well-turned image that no one at a keyboard would produce at that hour | keep the image only if the poster owns one anyway — and make theirs specific and a little wrong |
| Clean verdict close | "결론적으로…", a single certain answer everyone nods at, a summary that tidies every thread | let the thread end ceded by committee, interrupted, or with the verdict still being fought over |
| Uniform fluency | every reply complete, evenly grammatical, doubts phrased politely | give someone half-sentences and a pet cause, someone a messy wall with the answer buried, someone too loud too early |
| Keyboard perfection | identical punctuation and spelling habits across all posters | render each poster's keyboard: some full-width, some lowercase, some always typoing the same word |

## Calibration: when to stay open

The writer's instinct is useful: clear things up. On a board, clarity costs the reader
the work they came for. Decide per beat:

- If the room has argued toward the truth and one more answer lands it → the poster who
  earned it delivers, and the thread gets its payoff *and* its pride.
- If the full truth would kill the suspense and the end isn't there yet → the
  explanation that comes will be wrong, half-wrong, or delayed. A thread's stale
  takeover theories are the payoff of a mid-story mystery.
- If nobody has earned the answer and the author just wants the reader to know → keep it
  open. A pinned open question is an engine; a delivered answer is a resolution you can
  only spend once.

Same asymmetry applies to beats: a situation that resolves inside the same beat leaves
nothing for the next one to build on, while one that turns against the room's favorite
theory asks the reader to re-model everything — which is where the reward lives.
