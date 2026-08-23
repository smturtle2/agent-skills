# 04 · Positive instructions

Why this repository phrases rules as targets rather than exclusions, when an exclusion
earns its place, and how hardcoding sneaks back in.

## Why prohibitions underperform

Three mechanisms, none of which require the model to be contrary
([full analysis](https://multigrid.ai/learn/negative-prompting)):

1. **A prohibition names an unbounded set.** "Be concise" excludes one region of output
   space and specifies nothing about where to land; a compliant continuation is any of
   infinitely many. "Answer in at most two sentences" names one target the model can move
   toward.
2. **The forbidden token enters context.** A model conditions on tokens; "never mention
   the competitor's name" raises the salience of that name.
3. **Prohibitions must hold at every generation step**, while a positive format rule is
   satisfied once by the finished text.

The decisive practical difference: **positive constraints with literals are checkable** —
a length test, a first-character test, a membership test can fail a run in CI. A
prohibition can only be audited by a human reading output.

## Rewrite table

| Prohibition | Affirmative replacement |
|-------------|------------------------|
| Don't be verbose | Answer in ≤ 3 sentences; stop after the recommendation |
| Don't make things up | Every claim quotes a span from `<source>`; with no supporting span, reply exactly `NOT_FOUND` |
| Don't add commentary after the JSON | Output exactly one JSON object; final character is `}` |
| Don't guess the customer's intent | Choose one of `refund`/`technical`/`billing`; use `other` when tied |
| Don't use jargon | Write for a reader with no industry background; define terms on first use |

Notice what the rewrites expose: several prohibitions were hiding two decisions ("don't
guess" required choosing a fallback label nobody had chosen). Rewriting them is a design
exercise, which is exactly their value
([source](https://multigrid.ai/learn/negative-prompting)).

## When an exclusion earns its place

Prohibitions remain useful in three cases:

1. **The excluded set is small and nameable** — and therefore testable: "use the words
   X, Y, Z" has a closed complement.
2. **It is a safety boundary paired with enforcement** — its value lies in being
   defensible, with the real gate living outside the prompt (a validator, policy engine,
   or approval step). Prose alone is always talkable-past.
3. **It sits beside its positive alternative**, ten tokens from where the constraint
   applies: "if the price is absent from the catalog, emit `price: null`" belongs inside
   the field description, in a general rules list two thousand tokens earlier it competes
   for attention with everything else.

Each surviving exclusion names its landing place. An exclusion with an alternative is a
branch; one without leaves the allowed path undefined
([guidance](https://dust.tt/blog/how-to-write-ai-agent-instructions)).

## Explain why instead of escalating force

Anthropic's authoring guidance flags ALL-CAPS `ALWAYS`/`NEVER` chains as a yellow flag:
today's models respond better to reasoning than to imperative escalation. State the rule,
then state why it exists — the why generalizes to cases the rule's letter misses, and
survives paraphrase better than the letter does
([best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices),
[skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)).

One caveat from the discipline-enforcing school ([obra/superpowers](https://github.com/obra/superpowers)):
when baseline testing shows an agent rationalizing past a rule under pressure, the fix is
an explicit counter for each observed rationalization — targeted, evidence-driven
exclusions, added only where tests showed failure. That is case 3 above applied
empirically: exclusions earned by observation, each paired with its positive branch.

## Where hardcoding returns

Two forms to watch for during review:

- **Voodoo constants** in scripts — values without justification transfer nothing to the
  next editor. See [03-contract-first.md § Parameterize every value](03-contract-first.md).
- **Overfit examples** — rules grown from one incident generalize poorly across the many
  prompts a skill will serve. When feedback demands a fiddly change, prefer reframing or
  a different pattern over adding another narrow clause
  ([skill-creator improvement guidance](https://github.com/anthropics/skills/tree/main/skills/skill-creator)).
