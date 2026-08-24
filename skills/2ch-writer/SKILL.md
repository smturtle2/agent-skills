---
name: 2ch-writer
description: Turns any material — links, news, articles, texts, ideas — into a complete anonymous text-board thread story with researched detail, distinct voices, and no filler, rendered as a standalone light-theme HTML page; also converts any thread in its post shape into a TTS listening script (role-labeled 2ch convention) when listening delivery is requested. Use when the user wants material or an idea rewritten as board-thread fiction, a fake-documentary thread narrative, or 2ch-style スレッド storytelling — including when they only say "스레드로 만들어줘", "thread story", "as if the board found out", or describe a situation they imagine a board would chew on.
---

# 2ch Writer

A board thread's power is that a statement gets torn apart, built on, and derailed by
anonymous people in real time — exposition becomes confrontation. What makes a thread
worth reading is what makes any board worth reading: precise detail, distinguishable
voices, and the collision between how obsessively a community knows its thing and how
absurd the situation is. What kills one is filler — posts that exist only because the
thread came to need them. This skill delivers the first kind and refuses the second.

## Contract

### Inputs

The run is one or both of two modes, picked by what is supplied: `material` starts the
writing run; `thread_input` starts the conversion run; when the request asks for a
listening script ("읽게", "tts", "audiobook"), the writing run also converts the thread
it just wrote. Neither input → failure branches.

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `material` | file paths, URLs, or pasted text | yes | What the story dramatizes. Its facts stay recognizable in the thread. |
| `genre` | free text | no | Any named genre. Absent → inferred from the material's tone, and the inference is stated at delivery. |
| `length_hint` | time- or scale-like expression | no | What the user expects the reading to *feel* like. It is a signal about breadth of drama — how many distinct situations the thread can carry — not a target count. Absent → the arc's own needs set the size; a short thread that completes its arc is a valid output. |
| `voice_samples` | pasted text, or links | no | The user's own writing, a writer they like, or a community's posts. When present, extract spoken habits from them first — rhythm, vocabulary, tics, register — and build the thread's voices from those habits instead of inventing. |
| `language` | language of the request | no | Body text and board conventions render in this language. Absent → the request's language. Proper nouns and researched names keep the spelling their source uses. |
| `thread_input` | path or URL of an existing thread HTML | no | Source for the conversion run. May be a thread written by this skill or any external thread whose posts expose number, name field, ID, and body. |

### Outputs

**Writing run (each thread):**

- One standalone HTML file built from [assets/viewer.html](assets/viewer.html): the
  template's slots are filled, nothing else in the file changes. Path agreed with the
  user; absent agreement, a filename derived from the thread title.
- Thread title present in both `<title>` and the page header.
- Posts numbered `1..N` in order; each shows number, name field, timestamp+ID line, and
  body.
- Light theme preserved: white background, dark text.

**Conversion run (each script):**

- One plain-text `.txt` file; path agreed with the user or derived from the thread
  title, same convention as the HTML file.
- The thread title as a heading line, then the posts in order as role segments — each
  segment opens with its label once and continues without repetition (see invariant 13).
- Every sentence-final mark followed by exactly two newlines — the spacing constant: two
  newlines is the shared pause token a TTS engine reads as a break.
- No raw post IDs, stamps, post numbers, anchor text, markup, or invented strings
  anywhere in the script.

### Invariants

1. **The arc completes.** Post 1 states an ordinary situation gone strange — readers meet
   the story as a stranger's problem. The middle escalates; the landing is an abrupt
   cutoff when the arc is done, or a summary/compilation post. This is the entry
   condition: the format's drama lives in the room's reactions, not in narration about
   the events.
2. **The thread reads straight through.** Everything a reader needs appears in order or is
   asked for in the post that needs it. References back to earlier content name the
   *content* ("the one who went back inside", "아까 그 인형 찍은 사람"), not a position.
   `>>n` anchors may appear as board idiom, but a reader who ignores them loses nothing —
   where a post depends on being understood, the words carry it.
3. **Every post earns its place.** Each post adds at least one of: new information about
   the world, a character beat, tension, comedy, or a reply collision. A post whose whole
   function is observing the thread's own state — counting progress, noting how far the
   thread has come, cheering on volume, empty agreement — does not earn its place; that
   same beat-space carries a remark about the world instead (mock the event, not the
   thread's size). Single-line reactions ("ㅁㅊ", "wat", "lol") are texture and belong in
   a thread's rhythm; they stop being texture the moment they replace content.
4. **Voices are distinguishable people, not labels.** Any two posts by different posters,
   swapped, must read wrong. Anonymous posters carry no demographic description —
   anonymity is what lets any reader inhabit any voice.
5. **Truth discipline.** Material facts keep their own claims. Real-world specifics —
   names, numbers, terminology, precedent — are the researched or established ones.
   Invented specifics attach to the world as rumor or local knowledge ("~라는 소문인데"),
   never as the material's own fact.
6. **Mockery lands on claims and situations.** Board cruelty attacks arguments and
   behavior inside the frame, not groups of real people.
7. **Horror or occult threads are led by 「悪魔情報」**, a late-arriving regular who enters
   after the room has piled up, knows encyclopedic detail across occult and SF, drives
   the investigation, and carries a standing flaw: a taste for conspiracy tangents that
   scatter the thread at mid-investigation. The handle is a proper noun from the story
   tradition it comes from; the thread's script is the thread's own business. Other
   genres invent their leaders fresh per story (see the leader formula in the style
   guide).
8. **Length is the arc's outcome, not a target.** The hint adjusts how much drama there
   is; the post count is what the drama needs. At delivery, the achieved scale and the
   reasoning behind it are reported.
9. **The room's knowledge moves at the room's pace.** Understanding arrives only through
   what the posters actually figure out — no narrator, no answers handed down before the
   evidence is in. Open questions stay open when they carry the thread; when a beat wants
   an explanation, it is delivered by a poster who just earned it, or it is wrong, or it
   does not come. Readers invest in what they reconstructed themselves — this is the
   format's fuel and its hardest failure mode, because the writer's own instinct is to
   clear things up.
10. **Voices differ in fluency, not only in subject.** Some posters write carefully,
     some are sparse, evasive, gappy, or simply wrong in a way that belongs to that
     poster. A thread where every reply is complete, even, and politely argued has one
     voice wearing names.

11. **The script sounds the way the thread reads.** Outside the closed conversion set in
    [references/tts.md](references/tts.md) — numbers, dates, and times to spoken forms;
    emoticons and letter-repetition to sound equivalents; markup unwrapped; stamps, post
    numbers, and anchors dropped or spoken per the table — the wording of every post
    survives verbatim. The conversion never paraphrases a voice.

12. **Voices are source roles, never random strings.** A post carries the voice of its
    name field when it has one. The opening post's ID belongs to the thread's own voice —
    **글쓴이**, the board's standard term for it. Every other post without a name is the
    anonymous voice, **익명** — many anonymous hands, one voice, because without names
    they are indistinguishable; their IDs are never read. No label is invented where the
    source supplies none.

13. **Labels sit at role changes and are spoken once.** Each segment opens with its
    label on the same line as the first unit it labels — `글쓴이: `, `익명: `, or the
    source's own name — and carries no punctuation of its own; the pause after it comes
    from the content's sentence-final mark. Within a segment, labels never repeat.

### Failure branches

- Material unreachable → name the missing pieces, stop before drafting.
- Material too thin for what the user wants → state the honestly achievable breadth and
  ask one question (once).
- No information-gathering tools at session time → build the texture from established
  knowledge and flag at delivery which specifics come from memory rather than current
  sources.
- Genre not inferable *and* the choice changes the whole shape → ask one clarifying
  question; otherwise infer and state the inference at delivery.
- Neither `material` nor `thread_input` supplied → name the missing input, stop.
- Thread posts missing any of number, name field, ID, or body → name the missing part,
  stop before converting (the source's shape decides who speaks; nothing is inferred
  that the source itself does not carry).

## Procedure

Freedom markers: creative steps are stated as goals with heuristics and done-conditions;
only the render step is an exact sequence, because the HTML shape is the output contract
and any deviation breaks it.

### 1. Read for grain (stable goal)

Pull three things and keep them as the skeleton: the material's facts; the one detail
vivid or strange enough to grab someone immediately — usually post 1's hook; and the
point a person who lives in this field would argue against on sight. That reaction is
the thread's first spark.

### 2. Ground the world (stable goal)

Before inventing, collect what a regular in this world carries by default: the terms,
tools, numbers, precedents, customs a practitioner recognizes on sight. Use the session's
information tools when they exist; use established knowledge otherwise — and remember the
flag for delivery. This is where the thread earns its texture: generic detail reads like
fabric; specific detail reads like a place the writer lives. Research findings later
enter the thread as things *people in this world already say*.

### 3. Design the people (stable goal)

Give each recurring poster a **stake** in the matter and one **speech habit** — register,
topic vocabulary, rhythm, or a tick. The stake decides what they know and why they post;
the habit decides how they're recognized. Named voices number whatever the drama
requires — some threads run on the OP plus the crowd — and the board-function roster in
the style guide is a diagnostic for hearing blur, not a headcount to fill.

### 4. Write sequentially (stable goal)

Write in order from post 1, one situation at a time: a situation rises, hits its turn,
releases, then the next begins. Threads succeed the way beats succeed, not the way quotas
fill. When a story must span several responses, stop at the end of a beat, state a
continuation plan, and keep numbering continuous if the work continues — each batch
opens its own complete beat so the whole is a series of full rises, never a stretched
middle.

### 5. Reader audit (stable goal — feedback loop)

Audit in two passes: a felt read that decides what to fix, then the mechanism checks.

**First pass — the felt read.** Declare a reader persona (a local who followed the
thread because it touches their area, or a stranger who found it by accident — see the
reader-simulation method in [references/audit.md](references/audit.md)), then read the
draft from the top once as that person. Record the felt experience against the board
reward channels in [references/audit.md](references/audit.md): where you leaned in,
where you drifted, what questions you held, and where they changed — each anchored to
the post that produced it. Name the single weakest channel before fixing anything; the
diagnosis decides the fix, not the firehose.

**Then the mechanism checks:**
- **Every post earns its place.** One that doesn't → replace it; most often it reports
  on the thread instead of the world.
- **Callbacks carry their meaning.** If following a post requires looking up a number,
  reword it to name the content.
- **Swap test.** Two posters' lines swapped read wrong? If not, sharpen stake or habit.
- **Fluency range.** Sparse, evasive, gappy, or wrong-voiced posts exist among the
  careful ones — a roster of articulate, complete replies is one voice.
- **Ledger sweep.** Every planted detail pays off or gets wound into world texture.
- **Truth test.** Material facts unchanged; invented specifics still framed as rumor.
- **Residue scan.** Run the closed-set tell list in [references/audit.md](references/audit.md)
  against the draft; any match gets restructured toward its alternative.

Fix what the felt read identified, then read the draft once more from the top: the fix
should be visible in the reader's next pass, not just checked off.

### 6. Render (fragile sequence)

This is the locked step because the HTML shape is the output contract: fill
[assets/viewer.html](assets/viewer.html) — title in both slots; one post block per post,
numbered from 1, anonymous name fields left empty; body text with HTML special
characters escaped. Leave the styling untouched.

### 7. Convert to a TTS script (fragile sequence)

Runs when conversion is requested — on `thread_input` or, when the request asked for a
script alongside writing, on the thread finished in steps 1–6.

1. **Verify structure.** Each post exposes number, name field (possibly empty), ID in
   its stamp, and body; otherwise follow the failure branch.
2. **Segment by role.** In post order: the opening post's ID key gets 글쓴이; named posts
   get their name; the rest get 익명. Consecutive posts of the same role merge into one
   segment; every role change opens a new one.
3. **Emit labels.** Each segment begins with its label (`글쓴이: `, `익명: `, or the
   source's name) on the head line, once — never repeated inside the segment.
4. **Apply spoken forms.** Walk the segment content through the closed set in
   [references/tts.md](references/tts.md): numbers, dates, times → spoken forms;
   emoticons and letter-repetition → sound equivalents; markup unwrapped; stamps, post
   numbers, and `>>n` anchors dropped or spoken per the table. Everything else verbatim.
5. **Space it.** After each sentence-final mark write exactly two newlines; head the
   file with the thread title as a heading line.
6. **Deliver.** Write the `.txt`; report the path, segment count, the role assignment
   (글쓴이's ID key, named voices), and every conversion or drop the closed set applied.

### 8. Deliver (stable goal)

Report the file path, post count, genre handling (named or inferred), which specifics
came from research vs. established knowledge, the achieved scale relative to the
length hint, and any continuation plan.

## Examples

**Input:** an article link about a hyperscale farm that hums over a valley — no genre,
no length hint.

**Output shape** (the template's tokens — the fixed constant; story content always comes
from the material at hand):

```html
<article class="post">
<p class="meta">{{N}} ：<span class="name">{{NAME}}</span>：{{STAMP}}</p>
<div class="body">{{BODY}}</div>
</article>
```

The contract runs through the writing itself: post 1 is a resident's complaint, an
agnostic naming a real piece of hardware is an explainer who has a stake, the joke lands
on the company's spokesperson rather than on the residents, callbacks run by content
("the one under the pylons"), and the thread ends when its arc closes.

**TTS script shape** (the spacing constant; content always comes from the thread):

```text
<thread title>


글쓴이: 
<post 1 wording, untouched>


익명: 
<posts 2–4 merged; each sentence-final mark closes its line with two newlines>

```

## References

- [references/style.md](references/style.md) — craft guide: read before drafting —
  voice mechanics, comedy, research-into-posts, callback language, beat rhythm,
  foreshadow ledger, 「悪魔情報」 and the leader formula, failure fixes.
- [references/audit.md](references/audit.md) — audit guide: read before step 5 — board
  reward channels, reader-simulation method, residue scan, and when-to-leave-open
  calibration.
- [references/tts.md](references/tts.md) — conversion table: read before step 7 — the
  closed set of spoken forms and drop rules, each with its reason.
- [assets/viewer.html](assets/viewer.html) — light-theme template; fill slots only.
