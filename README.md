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
| [`2ch-writer`](#2ch-writer) | Turning any material into anonymous-board thread stories | Standalone light-theme HTML thread page | [Prompt](#2ch-writer) |
| [`reading-writer`](#reading-writer) | Converting any material into TTS-ready listening scripts | Plain-text narration script (`.txt`) | [Prompt](#reading-writer) |

## Quick Install

Any Agent-Skills-compatible harness (Claude Code, OpenAI Codex, OpenCode, Gemini CLI,
Cursor) accepts this prompt:

```text
Install skills/<skill-name> from https://github.com/smturtle2/agent-skills into your skills directory.
```

<!--
Catalog entry shape for every future skill. Adding a skill means doing all three in the
same change: append its row here, append its catalog section below, and include its own
install prompt in that section.

Skills table row:

| [`<skill-name>`](#<skill-name>) | <best for> | <output> | [Prompt](#<skill-name>) |

Catalog section:

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

### `2ch-writer`

Turns any source material into an anonymous text-board thread story in any genre;
occult-or-horror threads are led by 「悪魔情報」.

| Field | Details |
| --- | --- |
| Folder | `skills/2ch-writer` |
| Use when | material, links, or news should become thread-format fiction, or a fake-documentary board story is requested |
| Produces | standalone light-theme HTML thread page |

Install:

```text
Install skills/2ch-writer from https://github.com/smturtle2/agent-skills into your skills directory.
```

### `reading-writer`

Converts any material — documents, articles, transcripts, web pages — into
TTS-friendly plain text with spoken-form normalization and uniform pauses.

| Field | Details |
| --- | --- |
| Folder | `skills/reading-writer` |
| Use when | content is being prepared for listening or a text-to-speech engine |
| Produces | plain-text narration script (`.txt`) |

Install:

```text
Install skills/reading-writer from https://github.com/smturtle2/agent-skills into your skills directory.
```


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
