# agent-skills

A personal repository of [Agent Skills](https://agentskills.io) — reusable instruction
packages (`SKILL.md` folders) that coding agents discover and load on demand.

Skills follow the open Agent Skills specification (originated by Anthropic, Dec 2025;
adopted by Claude Code, OpenAI Codex, Gemini CLI, Cursor, OpenCode, Amp, and others).
This repository also documents the authoring methodology used here: **contract-centric,
affirmatively phrased, parameterized skills with minimal tests**.

## Structure

```
agent-skills/
├── AGENTS.md        # Contract for agents working in this repo
├── docs/            # Authoring methodology (start at docs/README.md)
├── skills/          # Skill bodies: skills/<name>/SKILL.md (+ scripts/, references/, assets/)
└── template/        # Copy this scaffold when creating a new skill
```

## Skills

| Skill | Best for | Output | Install |
|-------|----------|--------|---------|

_No skills yet. The first skill added populates this table and appends its catalog entry
below._

## Quick Install

Any Agent-Skills-compatible harness (Claude Code, OpenAI Codex, OpenCode, Gemini CLI,
Cursor) accepts this prompt:

```text
Install skills/<skill-name> from https://github.com/smturtle2/agent-skills into your skills directory.
```

CLI alternative: `npx skills add smturtle2/agent-skills -s <skill-name>` or
`gh skill install smturtle2/agent-skills <skill-name>` — path matrix in
`docs/02-harnesses.md`.

<!--
Catalog template. When adding a skill, append a section here following this shape and add
its row to the Skills table above:

### `<skill-name>`

<one-line description>

| Field | Details |
| --- | --- |
| Folder | `skills/<skill-name>` |
| Use when | <trigger conditions> |
| Produces | <outputs> |

Install:

```text
<the Quick Install prompt above, with <skill-name> replaced>
```

-->




## Create a skill

1. Read `docs/README.md` (reading order: 01 → 07).
2. `cp -r template skills/<skill-name>` and fill in the contract sections.
3. Validate: `skills-ref validate skills/<skill-name>`.
4. Run the eval prompts from `evals/evals.json` against a fresh agent session; confirm the
   gap the skill closes actually closes.

## Authoring philosophy

Every skill here states a **contract** (inputs, outputs, invariants, failure branches)
before any procedure; phrases rules **affirmatively** so each one is checkable; treats
every literal as either an **input or a justified constant**; and carries just enough
**tests** to demonstrate its value over a no-skill baseline. The reasoning lives in
`docs/03-contract-first.md` and `docs/04-positive-instructions.md`.

## License

See [LICENSE](LICENSE).
