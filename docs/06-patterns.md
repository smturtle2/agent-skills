# 06 · Patterns

Structural patterns that solve recurring authoring problems. Each is small enough to
apply directly; sources in [07-references.md](07-references.md).

## Progressive disclosure patterns

Three arrangements for growing content
([best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)):

**High-level guide with references.** Quick start inline; everything else behind
pointers with read conditions:

```markdown
## Advanced features
- Form filling: see [FORMS.md](FORMS.md)
- API reference: see [REFERENCE.md](REFERENCE.md)
```

**Domain organization.** One reference file per mutually-exclusive context; the agent
reads only the relevant one (sales query loads `reference/sales.md`, finance stays
unread):

```markdown
- Revenue/billing: [reference/finance.md](reference/finance.md)
- Pipeline: [reference/sales.md](reference/sales.md)
```

**Conditional workflow.** Decision point at the top, branches below or in linked files:

```markdown
1. Creating new content? → "Creation workflow"
2. Editing existing content? → "Editing workflow" (tracked changes: REDLINING.md)
```

All three keep the SKILL.md body a table of contents that costs nothing until opened.

## Workflow + checklist pattern

For multi-step procedures, give the agent a checklist it copies and checks off as it
progresses — visible progress prevents skipped steps, and the transcript becomes
reviewable step-by-step. Attach each step to its contract clause.

## Feedback-loop pattern

Run validator → fix → re-run until pass. The validator can be a script (`validate.py`)
or a reference document compared against by reading. This single pattern measurably
improves output quality on format-critical tasks; state explicitly when to loop and what
counts as passing.

## Plan-validate-execute pattern

For batch or destructive operations: create an intermediate plan file (`changes.json`),
validate it with a script **before** executing, then execute against the validated plan.
Errors surface while still reversible; verbose validation messages ("field
`signature_date` not found; available: …") make failures self-correcting.

## Description optimization (discovery)

The description is the trigger surface. Requirements from both major schools:

- Third person; states **what it does + when to use it**
  ([Anthropic](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)).
  Anthropic additionally recommends slightly "pushy" wording listing explicit triggers,
  since models under-trigger skills.
- Trigger-focused alternative ([superpowers](https://github.com/obra/superpowers)):
  open with "Use when…", list concrete symptoms and situations, technology-agnostic where
  possible.
- Include search keywords agents would grep for: error messages, symptom words, tool
  names, synonyms.

This repo's convention: `description: <What it does>. Use when <triggers>, <symptoms>,
<contexts>.` — both requirements in one sentence shape.

## Naming

Gerund form preferred (`extracting-pdfs`), noun phrases acceptable (`pdf-extract`);
consistent within the collection. Name by what the skill does or its core insight
(`condition-based-waiting` over `async-test-helpers`). Vague names (`helper`, `utils`,
`tools`) fail discovery and review alike.

## Token efficiency targets

| Content | Target |
|---------|--------|
| Frequently-loaded skill | ≤ 200 words |
| Standard skill body | ≤ 500 lines / ~5k tokens |
| Reference file | ≤ 100 lines before adding a TOC |

Techniques: cross-reference instead of repeating; one excellent example instead of many;
inline code only when short, otherwise link to `scripts/`.

## Script bundling signal

Read eval transcripts: if multiple runs independently write similar helper logic, bundle
it once into `scripts/` and reference the command. State whether each script is meant to
be **executed** ("run `analyze_form.py` to extract fields") or **read as reference**
("see `analyze_form.py` for the algorithm") — execution is the default since only output
enters context.

## Anti-patterns

Each anti-pattern pairs with its fix:

| Anti-pattern | Fix |
|--------------|-----|
| Windows-style paths | Forward slashes everywhere |
| Offering 3+ equivalent options mid-task | One default plus a named escape hatch for the exceptional case |
| Time-sensitive statements in body text | "Current method" section + collapsed legacy notes with deprecation dates |
| Deeply nested references (A→B→C) | All links one level deep from SKILL.md |
| Inconsistent terminology across sections | One term per concept, chosen once |
| Explanations of things the model already knows | Delete; assume a capable reader |
