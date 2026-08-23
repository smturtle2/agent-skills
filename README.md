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

## Install a skill

```bash
# Via the community CLI (73+ agents supported)
npx skills add smturtle2/agent-skills -s <skill-name>

# Via GitHub CLI
gh skill install smturtle2/agent-skills <skill-name>
```

Both tools discover skills under the standard `skills/<name>/SKILL.md` convention.
For local development, agents pick the folder up directly from `.claude/skills/`,
`.agents/skills/`, or `.opencode/skills/` — see `docs/02-harnesses.md` for the full path
matrix.

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
