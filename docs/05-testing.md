# 05 · Testing

The smallest test effort that demonstrates a skill's value. Two schools converge on the
same shape: measure the gap first, write the minimum that closes it, verify with fresh
sessions.

## Eval-first development

Anthropic's recommended order — evals before documentation
([best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)):

1. **Identify the gap.** Run representative tasks without a skill; record specific
   failures or missing context.
2. **Write three eval prompts** targeting those gaps, each with expected behaviors:

```json
{
  "skill_name": "pdf-extract",
  "evals": [
    {
      "id": 1,
      "prompt": "<realistic user task>",
      "expectations": [
        "Uses an appropriate PDF library or CLI",
        "Covers every page of the document",
        "Saves output to <path> in <format>"
      ]
    }
  ]
}
```

The key names follow the official skill-creator schema (`skill_name` + `evals[]`
with `expectations`).

3. **Establish the no-skill baseline** for those same prompts.
4. **Write minimal instructions** sufficient to pass — content addressing observed gaps
   only.
5. **Iterate**: rerun evals, compare against baseline, refine.

This repo stores evals at `skills/<name>/evals/evals.json` and results at
`evals/results-<date>.md` (see [AGENTS.md](../AGENTS.md)). Expected behaviors are phrased
as checkable statements — each maps to an assertion a reviewer can mark pass/fail from
the transcript alone.

## The TDD-for-skills cycle (for discipline-enforcing rules)

[obra/superpowers](https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md)
applies RED-GREEN-REFACTOR to documentation:

| TDD concept | Skill equivalent |
|-------------|-----------------|
| Failing test first | Run pressure scenarios **without** the skill; record failures verbatim |
| Minimal implementation | Write guidance addressing exactly the observed rationalizations |
| Regression | New rationalization appears → add its explicit counter → re-verify |

Use this when the skill enforces discipline (rules agents will be tempted to skip). For
technique and reference skills, lighter verification suffices — see sizing below.

### Pressure scenario anatomy (final gate only)

Full subagent runs are expensive per iteration; they are the last check, after wording is
settled ([method](https://github.com/obra/superpowers/blob/main/skills/writing-skills/testing-skills-with-subagents.md)):

- Combine 3+ pressures: time, sunk cost, authority, exhaustion, social appearance.
- Force concrete choices ("what do you do?" over "what should you do?"), real paths,
  explicit options, and an exit that requires choosing.
- Record rationalizations word-for-word; each becomes either a contract clause or a
  paired exclusion under the [positive-instructions rules](04-positive-instructions.md).

### Micro-tests before full runs

Verify wording cheaply before committing to scenario suites: one fresh-context call
(raw API or single-shot subagent) where the system prompt contains the realistic skill
context and the user message applies temptation pressure. Iterate on wording here;
reserve full scenarios for the final gate.

## Trigger evaluation

The `description` field decides activation, so it earns its own eval set
([skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)):

- 8–10 **should-trigger** queries: varied phrasings, casual/formal mix, including cases
  where the user never names the domain explicitly. Queries must be substantive enough
  that consulting the skill would help — trivial one-step requests may legitimately skip
  any skill.
- 8–10 **should-not-trigger near-misses**: shared keywords, adjacent domains, ambiguous
  phrasings. Obviously irrelevant negatives test nothing.

## Keeping tests minimal

Signals that test effort is correctly sized:

- Every eval names a gap observed in the baseline; an eval passing both with and without
  the skill measures nothing and gets deleted.
- Scripts bundled in `scripts/` earn inclusion by repetition: if multiple eval runs
  independently produce the same helper logic, bundle it once — then the script itself is
  the deterministic part of the test surface.
- Programmatic assertions (file exists, format parses, length within bounds) run as
  scripts rather than eyeballing; judgment calls stay qualitative and human-reviewed.

## Iteration loop summary

Draft skill → run evals with-skill and without-skill in parallel → compare → revise
against the contract (not by appending clauses) → repeat until the delta is stable and
the feedback is empty.

**Improving an existing skill:** the baseline is the previous version — snapshot it into
the eval workspace before editing, then run the same eval prompts against both versions
in parallel (see skill-creator's improve mode). The delta between versions, not the
pass-count of the new one, decides what changed.
