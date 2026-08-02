---
name: example-release-runbook
description: Release runbook example. Use when creating a project skill for preparing, approving, deploying, observing, communicating, and rolling back a production release or operational change.
---

# Release Runbook Example

## Scope

Use this pattern for a production deployment, configuration change, or operational rollout. Do not use it to replace normal feature implementation or change approval policies.

## Required inputs

- Release contents, approval requirements, environment differences, and owner contacts.
- Deployment commands, health signals, rollback method, and communication channel.

## Procedure

1. Freeze the exact artifact, configuration, and change list to be released.
2. Verify preflight checks, approvals, migration prerequisites, and rollback readiness.
3. Deploy using the documented sequence and record timestamps and outcomes.
4. Observe health, error rates, critical user paths, and business signals for the defined window.
5. Decide to continue, pause, or roll back using pre-agreed thresholds.

## Constraints

- Do not improvise production commands or approval bypasses.
- Do not call a release healthy without the defined observation evidence.
- Keep credentials and private operational endpoints out of the runbook.

## Deliverable

- A completed release record with artifact identity, checks, observation results, and rollback status.

## Verification

- [ ] Artifact and configuration are traceable to reviewed sources.
- [ ] Preflight, deployment, and observation checks have recorded evidence.
- [ ] Rollback decision criteria were available before deployment.

## Handoff

| Condition | Next canonical skill |
|---|---|
| A release incident occurs | `project-bug-investigation` |
| A contract or migration requires follow-up | `project-api-contract` |
