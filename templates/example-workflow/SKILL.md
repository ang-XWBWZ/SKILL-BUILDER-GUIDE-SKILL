---
name: example-workflow
description: >-
  Development workflow skill template. Guides creation of project-specific
  workflow skills. Triggered when asking about development steps, phase
  order, or checklists for common tasks.
model_tier: L1
skill_tier: functional
version: 1.0.0
status: active
---

# Development Workflow Skill Template

> **Positioning**: Functional tier skill — provides **step-by-step workflow guides** for common development tasks. Orchestrated by [delegation](../../references/execution-tree.md) (planning) and [skill-builder-guide](../../SKILL.md) (meta).

## Trigger Conditions

- Asking about development steps, phase order, workflow
- "How do I add a new feature / fix a bug / deploy"
- Need a checklist for a specific task type
- Creating project-specific workflow skills

## Related Skills

- [Dev Standards](../example-dev/SKILL.md) — tech stack reference for each step
- [Code Map](../example-code-map/SKILL.md) — file locations to modify [L0]
- [Change Model](../../references/change-model.md) — change reports for completed work

---

## 1. Workflow Template

Each workflow follows: **Phase → Input → Steps → Output → Checklist → Rollback**

```markdown
## {Workflow Name}

**Trigger**: {when to use this workflow}
**Duration**: {typical time}

### Input
- {required information / files / branch / ticket}

### Steps

| # | Step | Action | Verification |
|:-:|------|--------|-------------|
| 1 | {phase} | {what to do} | {how to verify done} |
| 2 | {phase} | {what to do} | {how to verify done} |

### Output
- {deliverables: PR / deploy / test report}

### Checklist
- [ ] {check item 1}
- [ ] {check item 2}

### Rollback
- {how to undo if this goes wrong}
```

## 2. Common Workflow Types

### Feature Development

```
Branch from main → Implement → Self-review → Create PR → Code review → Merge → Deploy
```

### Bug Fix

```
Reproduce → Locate root cause → Fix → Add regression test → Create PR → Deploy
```

### Hotfix

```
Branch from release → Fix → Emergency review → Deploy → Backport to main
```

## 3. Customization

When generating a project-specific workflow skill, extract workflow information from CI configs, contribution docs, package scripts, and team conventions. Map each step to real project files and commands.

Detailed extraction guide: [references/customization-guide.md](references/customization-guide.md).

## 4. Model Tier

**L1 — Sonnet / functional tier**: Requires understanding project workflow conventions and structuring them into actionable step-by-step guides. File lookups delegated to L0 — Haiku.
