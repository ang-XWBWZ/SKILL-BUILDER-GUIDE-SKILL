---
name: example-data-migration
description: Data migration example. Use when creating a project skill for changing persistent schema, stored data, backfills, imports, retention, or state transitions with safety checks and rollback planning.
---

# Data Migration Example

## Scope

Use this pattern for any change that can alter persistent data or long-lived state. Do not use it for a read-only query change with no data transformation.

## Required inputs

- Current schema or data contract, target state, volume, ownership, and retention constraints.
- Migration tooling, backup/restore capabilities, and deployment window requirements.

## Procedure

1. Define source state, target state, invariants, and a measurable success condition.
2. Classify compatibility for old and new application versions during rollout.
3. Design an idempotent migration or explicitly document why it cannot be idempotent.
4. Rehearse on representative non-production data and measure duration and failure handling.
5. Execute with checkpoints, validate invariants, and retain evidence for rollback or repair.

## Constraints

- Do not run destructive or irreversible actions without explicit authority and a verified backup plan.
- Never assume a migration can be rolled back; state the actual recovery path.
- Keep production data out of documentation and examples.

## Deliverable

- A migration plan, implementation, rehearsal evidence, validation query or check, and recovery plan.

## Verification

- [ ] Source and target invariants are explicit.
- [ ] Rollout compatibility is checked for all active application versions.
- [ ] Rehearsal and post-run validation evidence are recorded.

## Handoff

| Condition | Next canonical skill |
|---|---|
| Migration is released to production | `project-release-runbook` |
| Migration exposes access-control risk | `project-security-review` |
