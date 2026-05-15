---
name: example-call-chain
description: >-
  Call-chain tracing skill template. Guides creation of project-specific
  call-chain skills for tracing API data flow, verifying type matching,
  and checking endpoint correctness.
model_tier: L1
skill_tier: functional
version: 1.0.0
status: active
---

> *牵一发而动全身。* ——龚自珍《自春徂秋偶有所触》
> 改一行代码之前先知道谁在调用它。这不是顾虑，是常识。

# Call-Chain Tracing Skill Template

> **Positioning**: Functional tier skill — provides **structured call-chain tracing methodology** for verifying data flow correctness. Orchestrated by [delegation](../../references/execution-tree.md) (planning) and [skill-builder-guide](../../SKILL.md) (meta).

## Trigger Conditions

- Tracing API call chains, data flow, request lifecycle
- "How does data flow from X to Y"
- "What calls what in this endpoint"
- Verifying type matching across layers
- Creating project-specific call-chain skills

## Related Skills

- [Dev Standards](../example-dev/SKILL.md) — layer conventions and naming
- [Code Map](../example-code-map/SKILL.md) — file locations [L0]
- [Change Model](../../references/change-model.md) — call-chain check integration

---

## 1. Tracing Method

```
Step 1: Identify entry point
  ├─ API endpoint / event handler / scheduled task / message consumer
  └─ Record: input types, validation rules

Step 2: Trace through layers
  ├─ Entry layer → Business layer → Data layer → External calls
  └─ Record at each layer: method name, parameter types, return type

Step 3: Verify final call
  ├─ SQL query / external API call / message publish / cache write
  └─ Check: parameters correctly assembled, types match

Step 4: Error path check
  ├─ Exceptions caught at each layer?
  └─ Error response includes correct status code?
```

## 2. Call-Chain Template

```markdown
## {Endpoint Name} Call Chain

{Caller}
  │ {HTTP method} {path}
  ▼
{Controller}.{method}({param}: {type})
  │ → calls {Service}.{method}({param}: {type})
  ▼
{Service}.{method}({param}: {type})
  │ → business logic: {summary}
  │ → calls {Repository}.{method}({query})
  ▼
{Repository}.{method}({query})
  │ → {SQL / external API / message}
  ▼
{Database / External Service}
```

## 3. Type Matching Checklist

| # | Layer Transition | Check | Status |
|:-:|------|------|:--:|
| 1 | Request → Controller | Param types match DTO | ✅/❌ |
| 2 | Controller → Service | Service param = DTO or derived type | ✅/❌ |
| 3 | Service → Repository | Query params match Prisma/SQL types | ✅/❌ |
| 4 | Service → External | API contract types match | ✅/❌ |
| 5 | Service → Response | Return type matches API schema | ✅/❌ |

## 4. Customization

When generating a project-specific call-chain skill, map the project's actual layer names to the tracing template. Include project-specific external API call signatures, error handling patterns, and one worked example of a real endpoint's full chain.

Architecture-specific tracing patterns (CLI, event-driven, frontend, layered backend): [references/tracing-patterns.md](references/tracing-patterns.md).

## Handoff

After completing this skill, recommend the next skill based on output characteristics:

| Condition | Recommend |
|-----------|-----------|
| New change requirement found | `{project}-change-model` |

## 5. Model Tier

**L1 — Sonnet / functional tier**: Requires code-level tracing and type-compatibility reasoning. File lookups delegated to L0 — Haiku.
