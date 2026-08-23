# 02 · Harnesses

Where agents discover skills, and how skills from this repository reach them. State of
the ecosystem as of August 2026.

## Discovery paths by harness

| Harness | Project scope | User scope | Notes |
|---------|--------------|------------|-------|
| OpenAI Codex CLI | `.agents/skills/` (walked CWD → repo root) | `~/.agents/skills/`, `~/.codex/skills/` | Symlinked folders followed |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | Also loads plugin-bundled skills |
| OpenCode | `.opencode/skills/`, `.claude/skills/`, `.agents/skills/` | matching `~/.config/opencode/skills/`, `~/.claude/skills/`, `~/.agents/skills/` | Walks up to git worktree root |
| Gemini CLI | `.agents/skills/` | `~/.gemini/skills/` | |
| Amp (Sourcegraph) | `.agents/skills/` | `~/.config/agents/skills/` | |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` | |
| GitHub Copilot CLI | `.github/skills/` | `~/.copilot/skills/` | Shares user path with VS Code |

Sources: [Codex skills](https://developers.openai.com/codex/skills),
[Claude Code](https://code.claude.com/docs/en/skills),
[OpenCode](https://opencode.ai/docs/skills/),
[Gemini CLI](https://geminicli.com/docs/cli/skills/),
[vercel-labs agent table](https://github.com/vercel-labs/skills).

## Convergence

Project-scope discovery has converged on **`.agents/skills/<name>/SKILL.md`** — Codex,
Gemini CLI, and Amp read it natively, and OpenCode reads it as a fallback. Authoring a
repository against this convention plus the standard layout makes it loadable everywhere;
tool-specific directories remain useful only as symlinks when a harness lacks the shared
path.

## Distribution CLIs

Two CLIs dominate distribution. Both discover skills under `skills/<name>/SKILL.md`
inside a repository (category subfolders up to two levels deep also resolve), which is
why this repository keeps that exact layout.

| Tool | Install | Scope control |
|------|---------|---------------|
| [`npx skills`](https://github.com/vercel-labs/skills) (skills.sh) | `npx skills add owner/repo -s <name> [-g] [-a <agent>]` | Per-agent targets; symlinks or copies |
| [`gh skill install`](https://cli.github.com/manual/gh_skill_install) | `gh skill install owner/repo <name> [--scope project\|user]` | Copies files; pins via `--pin` tag/SHA |

For local development against any of these harnesses, point your agent at this checkout
directly: the repo root already matches the discovery conventions above.

## Practical defaults used in this repository

- Skills live at `skills/<name>/SKILL.md` → both CLIs install from this URL unmodified.
- Each skill's frontmatter carries no harness-specific fields; portability comes from
  sticking to the [specification](01-specification.md).
- Harness quirks (e.g. Gemini CLI's TOML command format) affect slash commands, not
  skills; skills use one standard format across all harnesses listed.
