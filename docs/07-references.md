# 07 · References

Primary sources behind every claim in this collection. Surveyed August 2026.

Link verification (2026-08-24): all links below were fetched and live except the Dust
post, whose content renders client-side and returns empty to a fetch — treat its claims
as unverified until read in a browser.

## Specification and standards

- [Agent Skills specification](https://agentskills.io/specification) — canonical format:
  frontmatter fields, directory conventions, progressive disclosure, validation.
- [agentskills/agentskills](https://github.com/agentskills/agentskills) — spec repo;
  [`skills-ref`](https://github.com/agentskills/agentskills/tree/main/skills-ref)
  validation library.
- [Anthropic engineering: Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) —
  design rationale for the format.

## Official authoring guidance

- [Skill authoring best practices (Anthropic)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) —
  conciseness, degrees of freedom, progressive disclosure patterns, workflows, eval-first
  development, anti-patterns, checklists.
- [Agent Skills overview (Anthropic)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) —
  runtime architecture, loading levels.
- [Codex skills (OpenAI)](https://developers.openai.com/codex/skills) — discovery
  scopes, plugin packaging.
- [OpenCode skills](https://opencode.ai/docs/skills/) — multi-path discovery incl.
  `.claude/` and `.agents/` fallbacks.
- [Gemini CLI skills](https://geminicli.com/docs/cli/skills/) ·
  [Cursor skills](https://cursor.com/docs/skills) ·
  [Copilot CLI skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills).

## Methodology projects

- [anthropics/skills](https://github.com/anthropics/skills) — official skills +
  [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator):
  draft → test → human review → improve loop; description trigger optimization; "explain
  why over ALL-CAPS" guidance; script-bundling signal.
- [obra/superpowers](https://github.com/obra/superpowers) — TDD-for-skills methodology:
  [`writing-skills/SKILL.md`](https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md)
  (RED-GREEN-REFACTOR for documentation),
  [`testing-skills-with-subagents.md`](https://github.com/obra/superpowers/blob/main/skills/writing-skills/testing-skills-with-subagents.md)
  (pressure scenarios, rationalization tables).
- [vercel-labs/skills](https://github.com/vercel-labs/skills) — `npx skills` CLI;
  supported-agent path table; discovery-depth rules.

## Ecosystem indexes

- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) —
  curated collection, official team skills.
- [awesomeskills.dev](https://www.awesomeskills.dev/en) — cross-platform skill index.
- [skills.sh](https://skills.sh) — install badges and registry for `npx skills`.

## Instruction-design research

- [Negative Instructions: Why "Don't" Often Backfires (Multigrid, 2026-08)](https://multigrid.ai/learn/negative-prompting) —
  mechanisms behind prohibition failure; rewrite table; when exclusions survive.
- [Spec-First Agents: Why the Contract Has to Land Before the Prompt (2026-04)](https://tianpan.co/blog/2026-04-23-spec-first-agents-contract-before-prompt) —
  contract components; prompt-as-three-artifacts failure mode.
- [Production Prompt Engineering in 2026 (ContextOS, 2026-08)](https://contextosai.com/blog/production-prompt-engineering-evaluated-contract) —
  enforceable-layer placement; rule-stated-once; threshold substitution; defer paths.
- [Designing System Prompts (AgentsCamp, 2026-06)](https://agentscamp.com/guides/prompting/designing-system-prompts) —
  durable/per-request split; explicit outs; termination conditions.
- [How to Write AI Agent Instructions That Actually Work (Dust, 2026-04)](https://dust.tt/blog/how-to-write-ai-agent-instructions) —
  affirmative phrasing; three-tier boundaries; anti-pattern list.
- [Contract First (Agents First, 2026-04)](https://agentsfirst.dev/principles/contract-first/) —
  AGENTS.md as load-bearing contract; common-mistakes sections; versioning discipline.
