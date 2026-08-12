# Skill Composition and Handoff

Compose skills around distinct project decisions, not around a fixed hierarchy of agent or model tiers.

## Use a handoff only when it is measurable

Add a `## Handoff` section when completion of one skill reliably creates a different kind of work. Good conditions include:

| Current result | Handoff condition | Next skill |
|---|---|---|
| Repository map | A change crosses a public boundary | API contract |
| Feature plan | Persistent data must change | Data migration |
| API review | Production rollout needs monitoring | Release runbook |
| Bug investigation | Reproduction shows an access-control concern | Security review |

Do not hand off merely because another skill exists. A terminal skill may omit the section.

## Keep ownership clear

- Give each skill a distinct trigger and non-goal.
- Link to canonical sibling skills under `.agents/skills/`.
- Do not duplicate detailed steps from a neighboring skill.
- Retire or merge skills when their triggers cannot be distinguished.

## Handoff format

```markdown
## Handoff

| Condition | Next canonical skill |
|---|---|
| Persistent schema or stored-state change is required | `project-data-migration` |
```

Verify that the named skill exists before publishing a generated project library.
