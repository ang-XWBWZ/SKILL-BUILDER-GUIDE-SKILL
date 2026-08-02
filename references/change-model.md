# Change Model — WHY / WHAT / HOW / VALIDATION

Use a change model for work that benefits from a durable causal record: a cross-module feature, a risky bug fix, an interface change, a migration, or a release-sensitive implementation.

## Four-layer record

| Layer | Record |
|---|---|
| WHY | User or system need, desired outcome, constraints, and non-goals |
| WHAT | Affected callers, data, contracts, risk, and compatibility impact |
| HOW | Chosen design, files or boundaries, sequencing, and rollback/recovery |
| VALIDATION | Checks run, observed evidence, release conditions, and remaining risk |

## Risk is independent of agent capability

Use project-defined risk labels. A portable default is:

| Level | Meaning |
|---|---|
| R0 | Internal behavior with no supported external or persistent effect |
| R1 | Internal interface or operational behavior with bounded consumers |
| R2 | Supported external contract or integration behavior changes |
| R3 | Persistent data, authority, security, or hard-to-reverse state changes |

Escalate authorization, verification, and rollback planning with risk. Do not treat these labels as model or runtime tiers.

## Change record outline

```markdown
# {change title}

## WHY
- Problem:
- Desired outcome:
- Constraints and non-goals:

## WHAT
- Affected callers and consumers:
- Contract/data impact:
- Risk and mitigation:

## HOW
- Design and file/boundary map:
- Rollback or recovery:

## VALIDATION
- Commands/checks and results:
- Release/monitoring condition:
- Remaining uncertainty:
```

Use [the change-model template](../templates/change-model-template.md) when a full report is warranted. Do not make reports mandatory for small, low-risk edits.
