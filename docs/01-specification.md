# 01 · Specification

The mechanical definition of a valid Agent Skill. Source:
[agentskills.io/specification](https://agentskills.io/specification) (open standard,
originated by Anthropic December 2025).

## Anatomy

A skill is a directory whose name matches the frontmatter `name` field:

```
skill-name/
├── SKILL.md          # Required: YAML frontmatter + markdown instructions
├── scripts/          # Optional: executable code agents run without loading into context
├── references/       # Optional: documentation loaded on demand
├── assets/           # Optional: templates, images, data files
├── evals/            # Recommended in this repo: evals.json + results
└── ...               # Any additional files
```

## Frontmatter fields

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | yes | 1–64 chars; lowercase letters, digits, hyphens; starts and ends with a letter or digit; matches parent directory name |
| `description` | yes | 1–1024 chars; states what the skill does **and** when to use it; third person |
| `license` | no | License name or reference to bundled license file |
| `compatibility` | no | ≤ 500 chars; environment requirements; include only when they exist |
| `metadata` | no | String-to-string map (e.g. `author`, `version`) |
| `allowed-tools` | no | Space-separated pre-approved tools (experimental; support varies) |

Minimal valid example:

```markdown
---
name: pdf-extract
description: Extract text and tables from PDF files, fill forms, merge documents. Use when handling PDFs or when the user mentions PDFs, forms, or document extraction.
---
```

## Body recommendations

- Keep `SKILL.md` under 500 lines / ~5000 tokens. Move detail into `references/*.md`.
- Link reference files one level deep from `SKILL.md`; nested chains cause partial reads.
- Add a table of contents at the top of any reference file longer than 100 lines.
- Name files descriptively (`form_validation_rules.md`, not `doc2.md`) — agents navigate
  by filename.
- Use forward slashes in all paths.

## Progressive disclosure

Agents load skills in three stages; cost accrues only as depth increases.

| Level | Loaded | Token cost | Content |
|-------|--------|-----------|---------|
| 1 Metadata | Always at startup | ~100 per skill | `name` + `description` |
| 2 Instructions | On activation | < 5k recommended | Full `SKILL.md` body |
| 3 Resources | On demand | Zero until read/run | `references/`, `scripts/`, `assets/` |

Scripts execute through bash with only their output entering context — deterministic
operations belong there rather than in prose.

## Validation

```bash
skills-ref validate ./skills/<skill-name>
```

Checks frontmatter validity and naming conventions. Reference implementation:
[skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref).
