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
