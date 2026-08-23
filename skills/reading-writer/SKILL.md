---
name: reading-writer
description: Converts any material — documents, articles, book excerpts, transcripts, web pages, pasted text — into TTS-friendly plain text with spoken-form normalization, speaker labels exactly at speaker changes, and uniform pauses after sentence-final punctuation. Use when preparing content for listening, building narration scripts, or cleaning text before feeding a text-to-speech engine.
---

# Reading Writer

Written text leans on layout; speech leans on sequence and pause. Re-express every
content element in a form a voice engine renders naturally while wording and order
stay intact — the listener receives the same document, spoken well.

## Contract

### Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `material` | file paths, URLs, or pasted text | yes | Anything readable: articles, books, papers, reports, transcripts, chat or thread dumps, mixes of these. |
| `output_path` | file path | no | Absent → `<source-basename>-tts.txt` beside the primary source (deterministic naming replaces asking). |
| `restructuring` | free-text instruction | no | Present → activates the reorder/condense branch (Procedure step 5). Absent → original unit order and prose wording stand. |

### Outputs

One `.txt` narration script where:

- Every sentence-final punctuation mark (`.` `!` `?`, fullwidth `。！？`) is followed by
  exactly two newline characters — one uniform pause the engine renders consistently.
- Heading lines carry extra surrounding blank lines as transition pauses.
- Speaker labels appear only at speaker-change boundaries.

### Invariants

1. Source units appear in original order; each meaningful unit reaches the script
   through exactly one row of the element-handling table.
2. Prose wording survives verbatim; transformations route through the element table
   only.
3. Pause format holds uniformly across the whole file: two newlines after terminal
   punctuation, padded headings.
4. A speaker label marks exactly the points where the current unit's speaker differs
   from the previous unit's; consecutive same-speaker units share one label.

### Failure branches

- Link unreachable → name the missing pieces, stop before writing output.
- Abbreviation ambiguous in context → choose the expansion that fits and record the
  decision in the delivery message (notes stay out of the script — a voice would read
  them aloud).
- Mixed-language block → normalize each language with its native readings, flag it in
  the delivery message.

## Procedure

1. **Acquire** (fragile sequence): read files / fetch URLs; list anything unreachable.
2. **Extract units** (stable goal): walk the source top-to-bottom, tagging each unit's
   element type.
3. **Handle elements** (table-driven): apply exactly one row per unit.
4. **Voice pass** (conditional): multi-speaker content gets change-boundary labels;
   single-narrator text skips this step entirely.
5. **Restructure branch** (conditional): runs only when `restructuring` is present —
   reorder or condense per that instruction; otherwise source order stands.
6. **Pacing pass** (fragile sequence): enforce terminal-punctuation newlines
   everywhere; pad heading lines.
7. **Deliver** (stable goal): write the `.txt`, then summarize decisions in the
   delivery message — expansions chosen, elements summarized, counts of decorative
   elements dropped.

### Element-handling table

| Element | Handling |
|---------|----------|
| Prose paragraph | Verbatim wording; paragraphs longer than 4 sentences split at sentence boundaries (audiobook breathing convention). |
| Heading | One signpost line, blank-line padded. |
| Ordered list | Spoken enumeration in the requester's language ("첫째… 둘째…" / "First… Second…"), one item per line. |
| Unordered list | Flowing sentence with connectives; items over 15 words go one-per-line instead. |
| Table or chart | Takeaway plus up to two key figures in 1–2 sentences; sprawling data tables reduce to one pointer line naming the source section. |
| Image or figure | One descriptive line drawn from caption or alt text; purely decorative images produce nothing. |
| Footnote carrying argument or anecdote | Woven into the flow right after its anchor sentence. |
| Bare-citation footnote | Collapses into one closing pointer naming the source. |
| Link | Anchor text kept; the URL reduces to its domain in spoken form ("example dot com"). |
| Email address | Spoken form: "name at domain dot com". |
| Code block or command | Purpose in one plain sentence; commands get a "Command:" prefix with blank lines around them. |
| Quotation | Wrapped in the requester's-language quotation frame ("quote … end quote"). |
| Numbers, dates, times, currency, units | Spoken forms: ambiguous numerals written out; dates and times normalized ("four p.m.", "twenty twenty-five"). |
| Acronyms | Expanded at first occurrence; pronounceable ones (NASA) stay words. |
| Emoticons, emoji, letter-repetition ("sllooooow"), chat slang | Spoken equivalent, dropped when meaningless aloud. |
| Multi-speaker exchange | Speaker-change boundary starts a new paragraph labeled with that speaker's name once; consecutive same-speaker units merge under one label. |

The thresholds (4 sentences, 15 words) are audiobook readability conventions; adjust
them only when the requester overrides.

## Examples

**Input:** any unit sequence — heading, prose, list, link, exchange.

**Output spacing shape** (wording passes through the element table untouched; only the
layout changes):

```text
<heading line>


<prose sentence.>


First: <list item>.

Second: <list item>.

```

Every terminal mark carries exactly two newlines and headings sit inside blank-line
padding — the spacing is the skill's one fixed constant; wording stays the source's.

## References

Everything fits above; no external files needed.
