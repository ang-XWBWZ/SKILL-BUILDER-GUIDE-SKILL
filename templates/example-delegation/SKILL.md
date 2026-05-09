---
name: example-delegation
description: >-
  Delegation rules skill template. Used to guide creation of project-specific
  delegation rules. Defines which tasks must be delegated to Haiku,
  delegation format, and sub-agent output standards.
model_tier: L1
skill_tier: atomic
version: 1.2.0
status: active
---

# Delegation Rules Skill Template

> **Position**: Atomic tier / L1 execution tier — a **reference template** for other projects to create project-level delegation rules. Composed by [skill-builder-guide](../../SKILL.md) (meta).
>
> **Full implementation**: See [delegation](../../references/execution-tree.md) (planning tier) for this project's actual delegation skill.

## Trigger Conditions

- Creating delegation rules skill / Defining L0 task delegation rules
- Asking "should this task be delegated"
- Need delegation rules template reference

## Related Skills

- [Delegation](../../references/execution-tree.md) — actual planning-tier delegation skill used by this project
- [Dev Standards](../example-dev/SKILL.md) — L0 info lookup scenarios
- [Code Map](../example-code-map/SKILL.md) — L0 file location scenarios [L0]

---

## 1. Mandatory Delegation Principle

**Main model must not execute L0 tasks.** All L0 tasks must be delegated via `Agent(model: "haiku")`.

## 2. L0 Task Catalog

| Category | Example Tasks | Target Skill |
|------|---------|---------|
| File lookup | Find file location, directory structure | code-map |
| Info lookup | Check version number, API routes | dev |
| Command execution | Deploy, package, service start/stop | scripts |
| Static tracing | Draw dataflow diagram, verify API list | code-map / dev |
| Mechanical edit | Rename variable, update version number | (direct) |

## 3. Standard Delegation Format

```
Agent(
  description: "3-5 word task description",
  model: "haiku",
  prompt: """
    【Task】What specifically to do
    【Files】List of paths to read
    【Output】Conclusion/Basis/Uncertainty format
  """
)
```

## 4. Sub-Agent Output Format

```
Conclusion:   One sentence answering the assigned goal
Basis:        Specific evidence, observations, reasoning path
Uncertainty:  Risks, missing information, failure modes (write "None" if none)
```

Main model does only three things after receiving: extract conclusions → identify conflicts → decide.

## 5. Upgrade / Fallback Strategy

| Trigger | Threshold | Action |
|---------|------|------|
| User repeatedly unsatisfied | Same task ≥2 correction rounds failed | Package context, submit to top-tier model |
| Work rework | Same code repeatedly modified, problem not converging | Stop modifying, re-analyze root cause |

**Upgrade info package**: Original requirements + attempted solutions and failure reasons + current blockers + excluded assumptions.

## 6. Model Tier

**L1 — Sonnet / atomic tier**: Rule interpretation and orchestration, requires reasoning. This skill is a template reference. See [delegation](../../references/execution-tree.md) for actual execution.
