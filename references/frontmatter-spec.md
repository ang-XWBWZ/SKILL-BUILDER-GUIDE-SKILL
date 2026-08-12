# Portable SKILL.md Frontmatter

Use the smallest frontmatter contract that travels across agent runtimes:

```yaml
---
name: project-capability
description: Explain what the skill does and the requests or conditions that should use it.
---
```

## Required fields

| Field | Rule |
|---|---|
| `name` | Lowercase letters, digits, and hyphens; keep it short and align it with the skill directory name. |
| `description` | States the outcome and concrete trigger contexts. Prefer 30–150 words. |

## Portable syntax subset

Keep metadata simple enough to read and adapt across runtimes:

- Use unindented, top-level `key: value` entries only; blank lines and comments are allowed.
- Use exactly one `name` and one `description`; avoid duplicate keys.
- Write `name` as a single-line scalar.
- Write `description` as a single-line scalar or an indented folded/literal block (`>-`, `>`, `|-`, or `|`). Every non-empty block line must be indented.
- Quote a scalar only with a matching opening and closing quote. Collections such as `[a, b]` and `{key: value}` are not portable frontmatter.

For example:

```yaml
---
name: project-capability
description: >-
  Explain what the skill does and the requests or conditions that should use it.
---
```

Do not use an unindented block description:

```yaml
description: >-
this line is not indented
```

## Keep out of the portable core

Do not add model tiers, vendor names, tool allowlists, automatic-discovery flags, version fields, ownership fields, or arbitrary lifecycle metadata to portable frontmatter. Those fields either bind a skill to one runtime or become stale when no tool consumes them.

If a runtime requires metadata, put it in `.agents/adapters/{runtime}/` and document how it maps back to the portable `SKILL.md`.

## Description pattern

```yaml
description: >-
  Acme API contract workflow. Use when adding, changing, reviewing, or
  documenting a public endpoint, request schema, response schema, or
  compatibility rule in this repository.
```

Avoid vague descriptions such as `Development helper` or `Useful for coding`; they do not define a reliable boundary.
