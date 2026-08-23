---
name: <skill-name>
description: <What this skill does. Use when <trigger conditions>, <symptoms>, or <contexts that should activate it>.>
---

# <Skill Name>

<One paragraph: the core principle of this skill. What outcome it produces and the single
idea that makes it work. Assume the reader agent is capable; state only what it cannot
infer.>

<!-- Delete these HTML comments as you fill in each section. -->

## Contract

Define the interface first. Every instruction below must be derivable from this section.

### Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `<input-name>` | `<type>` | yes/no | <Shape, constraints, and what counts as valid.> |

### Outputs

<Exact shape of the result: file paths created, format, sections, length bounds.>
<"Produce a report" is not a spec; "produce `report.md` with sections X/Y/Z, each ≤ N words" is.>

### Invariants

<Properties that hold for every output regardless of input. One line each, phrased as the
property itself: "Every claim cites a span from the input.">

### Failure branches

<For each condition that blocks the happy path, name the branch and its behavior:
missing input → <action>; ambiguous request → <one clarifying question>; partial data →
<what to emit>. An explicit defer path replaces guessing.>

## Procedure

<Steps derived from the contract above. Match freedom to fragility:
- Fragile sequence → one exact command per step.
- Stable goal, variable path → describe the goal and let the agent choose the route.
State which mode each step uses.>

## Examples

**Input:** <realistic, concrete>

**Output:**

```
<complete expected output>
```

<!-- One excellent example beats several mediocre ones. -->

## References

<!-- Optional. Link additional files one level deep, telling the agent when to read each:
- [forms.md](forms.md) — read when filling form fields.
Keep this section empty if everything fits above. -->
