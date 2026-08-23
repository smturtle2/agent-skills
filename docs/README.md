# Authoring Methodology

How skills in this repository are designed, written, and verified. Compiled from the
Agent Skills specification, official vendor guidance, and leading skill projects as of
August 2026.

## Reading order

| # | Document | Question it answers |
|---|----------|---------------------|
| 01 | [Specification](01-specification.md) | What is a valid skill, mechanically? |
| 02 | [Harnesses](02-harnesses.md) | Where do agents look for skills, and how do I distribute them? |
| 03 | [Contract-first design](03-contract-first.md) | How do I structure a skill so its behavior is reviewable and testable? |
| 04 | [Positive instructions](04-positive-instructions.md) | Why phrase rules affirmatively, and when are exclusions acceptable? |
| 05 | [Testing](05-testing.md) | What is the smallest test suite that proves a skill works? |
| 06 | [Patterns](06-patterns.md) | Which structural patterns solve recurring authoring problems? |
| 07 | [References](07-references.md) | Where is the primary source for each claim? |

## The four commitments this collection enforces

1. **Contract first.** A skill states inputs, outputs, invariants, and failure branches
   before any procedure text. Procedure edits become diffs against that contract.
2. **Affirmative phrasing.** Each rule names the target behavior so it can be checked by
   reading one line. Exclusions exist only where they are small, closed sets paired with
   their positive alternative.
3. **Parameterized values.** Every literal in instructions or scripts is an input or a
   constant justified beside its definition.
4. **Minimal tests.** Three eval prompts demonstrating the gap over a no-skill baseline;
   pressure scenarios reserved for discipline-enforcing rules.

## One-paragraph summary of why

Skills are prompts that ship to other people's sessions. An unstructured prompt grows
into sediment — every incident adds a rule, rules conflict, and nobody can tell which
line encodes a requirement versus a hint. Writing the contract first, phrasing each rule
once and affirmatively, parameterizing values, and testing against a no-skill baseline
keeps every future edit cheap. Sources per claim: [07-references.md](07-references.md).
