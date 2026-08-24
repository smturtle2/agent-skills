# 03 · Contract-first design

A skill is an interface before it is a procedure. This document defines the contract
sections every skill in this repo carries, and the rules that keep them honest.

## The failure mode this prevents

When behavior lives only in prose, one artifact plays three roles at once:
specification, implementation, and implicit test suite. Symptoms once a prompt outgrows
its original author ([spec-first analysis](https://tianpan.co/blog/2026-04-23-spec-first-agents-contract-before-prompt)):

- Edits become rewrites — no artifact exists to diff against.
- "Is this a bug or intended?" has no answer, because intent lived in prose.
- Each incident appends a rule; rules accumulate, conflict, and calcify until any change
  outweighs its benefit.

Writing the contract first splits these roles. The contract names what holds; procedure
text implements it; evals verify it. An instruction edit becomes a claim that the
contract still holds, reviewable as a diff.

## The contract's five components

Stated in a `## Contract` section before any procedure text:

1. **Inputs** — shape, type, required-or-not, and validity bounds of everything the skill
   receives. Include edge cases ("file may be empty"; "paths may contain spaces").
2. **Outputs** — exact result shape: files created, format, sections, length bounds.
   "Produce a report" is not a spec; "produce `report.md` with sections X/Y/Z, each
   ≤ N words" is ([guidance](https://agentscamp.com/guides/prompting/designing-system-prompts)).
3. **Invariants** — properties true of every output regardless of input, phrased as the
   property itself ("Every claim cites a span from the input").
4. **Failure branches** — named behavior for each condition that blocks the happy path:
   missing input → action; ambiguity → one clarifying question; partial data → what to
   emit. Every route needs an explicit defer path; without one the model fills the gap,
   which is where confident hallucination comes from.
5. **Escalation / stop conditions** — the specific observable conditions under which the
   skill hands off or terminates. "Stop when the test suite passes," with concrete
   triggers, replaces vague ones like "user frustration."

In most contracts in this collection, component 5 lives inside `### Failure branches`:
each blocked route already carries its named stop action ("stop before drafting", "ask
one question"), so a separate escalation section appears only when the transfer logic
outgrows a single line.

## Rules that keep contracts honest

### State each rule once

Duplicate rules drift apart independently. One authoritative location per requirement;
elsewhere, refer to the concept by name
([production-prompt guidance](https://contextosai.com/blog/production-prompt-engineering-evaluated-contract)).

### Replace adjectives with thresholds

"Concise", "robust", "high confidence", "recent" constrain nothing measurable. Write the
bound instead: "≤ 200 words", "sources updated within 90 days", "confidence ≥ 0.8 maps to
publish". The rewrite also exposes hidden decisions — "don't guess" forces you to choose
the fallback label you never chose.

### Parameterize every value

A literal in instructions or scripts is either (a) an input to the skill or (b) a constant
with a one-line justification beside its definition:

```python
# Three retries: most intermittent failures resolve by the second retry;
# a third covers tail cases without meaningfully extending wall time.
MAX_RETRIES = 3
```

Unjustified constants ("voodoo constants") transfer zero information to the next editor
and cannot be tuned safely ([Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)).

### Match freedom to fragility

Not every step deserves a script. Calibrate specificity per step
([degrees-of-freedom model](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)):

| Situation | Freedom level | Form |
|-----------|--------------|------|
| Many valid routes, context decides | High | Goal + heuristics |
| Preferred pattern exists | Medium | Template / pseudocode with parameters |
| Fragile sequence, consistency critical | Low | Exact commands |

Hardcoding appears when low-freedom form is applied to high-freedom steps: brittle
step-by-step scripts for tasks the model already knows how to do. Reserve exact commands
for steps where deviation causes damage, and say why that step is locked down.

## Mapping to SKILL.md

```
---
frontmatter            → discovery contract (what + when)
## Contract            → the five components above
## Procedure           → derived from the contract, freedom-calibrated
## Examples            → one complete realistic input/output pair
## References          → optional, one level deep
```

Every line of procedure text should be derivable from the contract section. During
review, ask of each line: which contract clause does this implement? A line with no
clause behind it is either missing from the contract or padding in the procedure.
