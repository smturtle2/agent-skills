# AGENTS.md

This file is the contract for agents working inside this repository. It is itself an
example of the style this repo enforces — see `docs/03-contract-first.md` and
`docs/04-positive-instructions.md` for the reasoning behind each rule.

## Repository layout

- New skills live at `skills/<skill-name>/SKILL.md`. The directory name matches the
  frontmatter `name` field exactly.
- The authoring scaffold lives at `template/SKILL.md`; copy it into `skills/<name>/` when
  creating a skill.
- Methodology documentation lives under `docs/`, numbered by reading order.

## Skill requirements

Every skill in this repository satisfies all of the following:

- Valid frontmatter per the Agent Skills specification: `name` (lowercase letters,
  digits, hyphens; 1–64 chars) and `description` (≤ 1024 chars, states what the skill does
  and when to use it).
- A `## Contract` section stating inputs, outputs, invariants, and failure branches
  before any procedure text.
- Affirmative phrasing throughout; each prohibition (if any) names a small, closed set of
  exclusions and sits next to its positive alternative.
- Parameterized values: every literal in instructions or scripts is either an input to the
  skill or a constant justified in one line beside its definition.
- An `evals/evals.json` with 3+ prompts and expected behaviors, sized to demonstrate the
  gap this skill closes relative to a no-skill run.
- A README entry, updated in the same commit as the skill itself: one row in the
  `## Skills` table and one catalog section carrying its install prompt. The repository
  URL is defined only in the README Quick Install section; every other surface derives
  its prompt from there, and Codex's `$skill-installer` variant lives in that section
  alone.

## Writing rules

- State each rule once, at the location where it applies.
- Replace qualitative adjectives ("concise", "robust") with measurable thresholds.
- Explain why a rule exists instead of escalating imperative force (ALL-CAPS, MUST chains).
- Keep `SKILL.md` bodies under 500 lines; move detail into `references/*.md` linked one
  level deep from `SKILL.md`.

## Verification

Before committing a new or modified skill:

```bash
skills-ref validate skills/<name>
```

Run the eval prompts against a fresh agent session with the skill loaded and confirm the
expected behaviors hold. Record results in `evals/results-<date>.md` beside `evals.json`.

## Commits

One skill (or one doc change) per commit. Commit message: `<area>: <change>`, e.g.
`skills/pdf-extract: add form-filling branch`.
