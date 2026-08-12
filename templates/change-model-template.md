# Change Record Template

Use this template for a change whose reasoning, risk, or rollback plan should remain discoverable. Replace every `{placeholder}` before publishing.

```markdown
# {change title}

## WHY

- Problem: {observed need}
- Desired outcome: {verifiable behavior}
- Constraints and non-goals: {compatibility, scope, ownership}

## WHAT

| Concern | Impact | Evidence |
|---|---|---|
| Callers/consumers | {impact} | {source or contract} |
| Data/state | {impact} | {schema or migration} |
| Risk | R0/R1/R2/R3 | {mitigation} |

## HOW

| Change | Location/boundary | Reason |
|---|---|---|
| {implementation step} | `{verified path}` | {reason} |

Rollback or recovery: {real recovery path, or explicit limitation}

## VALIDATION

| Check | Command/evidence | Result |
|---|---|---|
| {check} | `{verified command}` | {result} |

Remaining uncertainty: {none or concrete gap}

## CLOSURE

- Actual delivered result: {observable outcome}
- Exact source change: {version-control revision, review, or diff}
- Delivery record: {project record location, or “not used”}
- Knowledge note: {separate knowledge location, or “not captured”}
- Open work, risk, or recovery limitation: {none or concrete gap}
- Status: completed / blocked / failed pending action / cancelled
```

Use risk labels to describe impact, never to select a model or runtime.
