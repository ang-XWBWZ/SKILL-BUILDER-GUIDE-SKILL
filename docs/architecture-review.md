# Architecture Review — Portable Project Skills

## Findings

The previous guide mixed three different concerns in the same files:

1. Portable project knowledge and procedures.
2. Runtime-specific discovery, model, and metadata assumptions.
3. Long examples, plans, and validation rules that duplicated one another.

That structure made a generated skill less portable, made the guide difficult to validate, and left too little room for distinct project scenarios.

## Adopted decisions

| Decision | Reason |
|---|---|
| Use `AGENTS.md` plus `.agents/skills/` as the canonical project contract | Keep source material portable and easy to locate |
| Keep runtime adaptation under `.agents/adapters/` | Prevent one runtime from defining project truth |
| Restrict portable frontmatter to `name` and `description` | Avoid stale, unconsumed, vendor-bound metadata |
| Describe task capability and risk rather than model tiers | Make instructions valid across runtimes |
| Keep detailed material in direct `references/` links | Preserve progressive disclosure without duplication |
| Validate a single skill, a library, and an optional project layout | Make the documented commands match actual behavior |
| Expand focused examples and scenario guides | Cover recurring work without a generic catch-all skill |

## Non-negotiable boundaries

- `AGENTS.md` routes; it does not duplicate skill procedures.
- `.agents/skills/` is canonical; adapters may translate but not silently change rules.
- A specialized skill must have a distinct trigger, output, verification method, and non-goal.
- Every claimed project fact must be traceable to a repository source or owner-provided rule.

## Review questions for future changes

1. Does the change add project value that cannot live in a general runtime capability?
2. Does it preserve one canonical source instead of creating a parallel copy?
3. Can the validator or a repository check prove its important claims?
4. Is the new template genuinely distinct from an existing example?
5. Does the change keep portable content free of runtime-specific assumptions?
