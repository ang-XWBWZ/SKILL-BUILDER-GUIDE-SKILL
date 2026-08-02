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
| `name` | Lowercase letters, digits, and hyphens; 1–64 characters; matches the skill directory name. |
| `description` | States the outcome and concrete trigger contexts. Prefer 30–150 words. |

## Portable syntax subset

The bundled validator intentionally accepts only a small YAML subset, so malformed metadata is not silently treated as valid:

- Use unindented, top-level `key: value` entries only; blank lines and comments are allowed.
- Use exactly one `name` and one `description`; duplicate keys are errors.
- Write `name` as a single-line scalar.
- Write `description` as a single-line scalar or an indented folded/literal block (`>-`, `>`, `|-`, or `|`). Every non-empty block line must be indented.
- Quote a scalar only with a matching opening and closing quote. Collections such as `[a, b]` and `{key: value}` are not portable frontmatter.

For example, this is valid:

```yaml
---
name: project-capability
description: >-
  Explain what the skill does and the requests or conditions that should use it.
---
```

This is invalid because the description line is not indented:

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
