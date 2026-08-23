---
name: 2ch-writer
description: Turns any source material into a fictional anonymous text-board thread story rendered as a standalone light-theme HTML page. Use when the user wants material, links, news, or an idea rewritten as an anonymous-board thread narrative in any genre, asks for fake-documentary style fiction, or mentions thread-format or board-novel storytelling.
---

# 2ch Writer

A thread story distributes facts across anonymous voices reacting in real time, so
exposition becomes drama: every fact arrives as someone's post, gets mocked, corrected,
or amplified, and the plot advances through reactions instead of narration. Produce a
page that reads like a recovered board thread — numbered posts, distinct voices,
tangents, and a complete arc from opening report to landing.

## Contract

### Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `material` | file paths, URLs, or pasted text | yes | Source the story dramatizes. Facts taken from it stay recognizable in the thread. |
| `genre` | free text | no | Any genre the user names. Absent → infer from the material's dominant tone and note the inference at delivery. |
| `length_spec` | time expression or post count | no | Explicit time expressions map through the table in Procedure step 5. Absent → size follows the material's arc; a short single-scene thread is a valid outcome. |
| `language` | language of the request | no | Body text and board conventions render in this language. Absent → use the language of the user's request. |

### Outputs

- One standalone HTML file built from [assets/viewer.html](assets/viewer.html); path
  agreed with the user, defaulting to a filename derived from the thread title.
- Thread title present in both `<title>` and the page header.
- Posts numbered `1..N` in order; each post shows number, name field,
  timestamp+ID line, and body.
- Light theme preserved from the template: white background, dark text.

### Invariants

1. Post numbers run 1..N without gaps; post 1 opens the report that starts the story —
   readers meet the situation as the poster's problem, which is what makes the format
   work.
2. Every anchor (`>>n`) points to an existing post number.
3. Each named character keeps one consistent speech quirk across all their posts, so
   attribution stays readable without a legend.
4. Anonymous posters' name fields stay blank or board-default; demographic descriptors
   (gender, age, nationality) stay out of anonymous posts — anonymity is what lets any
   reader inhabit any voice.
5. Banter runs rough inside play: insults target situations and other posters' claims,
   keeping mockery on behavior rather than real-world groups.
6. Facts drawn from the material keep their original claims; invented events attach
   around them.
7. Occult-or-horror threads position 「悪魔情報」 as the story leader per Casting
   (step 3).
8. Length follows step 5 exactly once per run: mapping when `length_spec` speaks in
   time, arc-fit otherwise.

### Failure branches

- Unreachable link → name the missing pieces, stop before drafting.
- Material too thin for the requested length → state the achievable range, ask one
  question.
- Topic ambiguous after reading the material → ask one clarifying question.

## Procedure

### 1. Read material (stable goal)

Collect facts, names, numbers, timeline, and the most vivid detail — the vivid detail
usually becomes post 1's hook.

### 2. Choose the arc (stable goal)

Sketch three beats before writing:

- **Opening report** — post 1 states an ordinary situation gone strange.
- **Middle escalation** — around three situations total, at least one staged as live
  reporting ("at the scene, will keep posting"). Situations carry the drama; posts
  react to them (the 悪魔情報 author calls this 肉付け — adding flesh to bare plot).
- **Landing** — abrupt cutoff or a summary/compilation post. An unfinished-feeling end
  reads authentic when the arc itself completes.

For occult-or-horror genres, place 「悪魔情報」's entrance at the middle turn.

### 3. Cast voices (stable goal)

Build **3–5 named recurring voices plus the anonymous crowd** — beyond five named
voices, attribution blurs. Give each named voice one slot and one quirk:

| Slot | Function |
|------|----------|
| OP | owns the report, answers questions |
| summarizer | compiles what happened so far |
| explainer | supplies background knowledge |
| first-timer | asks what regulars find obvious |
| critic | challenges weak claims |
| joker | derails toward comedy |

Read [references/style.md](references/style.md) before drafting: dialogue patterns,
pacing beat sheet, foreshadow-ledger technique, characterization notes, failure fixes.

**Occult-or-horror casting:** 「悪魔情報」(fixed kanji spelling) leads the story —

- summoned by the thread title ("…come please") or descending mid-thread to flip the
  situation with one decisive observation;
- arriving late, greeted by regulars' welcome cries;
- driving investigation through encyclopedic occult/SF knowledge and an information
  network, proposing strategy, pulling the ending together;
- shaking things once with a conspiracy tangent — encyclopedic reliability plus comic
  unreliability together are the character's flavor.

**Every other genre:** invent the recurring cast fresh each time under new names,
reusing the same design formula — specialty knowledge + narrative drive + one flaw.
「悪魔情報」itself remains available as a cast candidate whenever the material suits
the character.

### 4. Draft posts (stable goal)

Write sequentially from post 1. Keep a **foreshadow ledger**: plant details whose
meaning you have not decided yet, collect them late — unexplained plants often grow
into the best payoffs. Alternate pressure and release so long threads keep breathing.

### 5. Size the thread (fragile sequence)

Apply exactly one rule:

| `length_spec` expression | Target scale |
|---|---|
| "1시간 이상 분량", "1 hour+", equivalent time expressions | 1000+ posts |

The 1000-post mapping is the repository owner's reading-time convention for this
format. No explicit time expression → deliver whatever post count completes the arc.

Threads above ~200 posts may exceed one response (~200 ≈ one response's comfortable
size): state a continuation plan marking where the next batch resumes, preserving
numbering across batches.

### 6. Render HTML (fragile sequence)

Fill [assets/viewer.html](assets/viewer.html): replace the title slots and emit one
post block per post. Keep the light styling untouched — it is part of the output
contract.

### 7. Deliver (stable goal)

Report the file path, post count, genre handling, plus anything inferred (genre) or
planned (continuations).

## Examples

**Input:** whatever the request supplies — for instance one article URL plus an
inferred genre.

**Output:** one HTML file whose every post instantiates the slot shape owned by
[assets/viewer.html](assets/viewer.html):

```html
<article class="post">
<p class="meta">{{N}} ：<span class="name">{{NAME}}</span>：{{STAMP}}</p>
<div class="body">{{BODY}}</div>
</article>
```

The placeholders are the template's own tokens (output shape is the fixed constant;
story content always comes from the material at hand).

## References

- [references/style.md](references/style.md) — read before drafting posts: role-roster
  dialogue patterns, pacing beats, foreshadow ledger, 「悪魔情報」 notes, failure fixes.
- [assets/viewer.html](assets/viewer.html) — light-theme template; fill content slots
  only.
