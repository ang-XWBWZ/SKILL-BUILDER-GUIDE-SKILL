---
name: example-workflow
description: Feature delivery workflow example. Use when creating a project skill for implementing a bounded feature through evidence gathering, design, change, verification, and handoff.
---

# Feature Delivery Example

## Scope

Use this pattern for a normal product change with a clear acceptance outcome. Do not use it for a data migration, emergency release, or security incident; those need dedicated procedures.

## Required inputs

- Requested behavior, acceptance criteria, and affected user or system boundary.
- Relevant source paths, tests, and project commands.

## Procedure

1. Restate the requested behavior and identify explicit non-goals.
2. Trace the affected code, contract, and persistence boundary before editing.
3. Choose the smallest implementation that preserves existing behavior outside the request.
4. Add or update tests that demonstrate the accepted behavior and critical negative case.
5. Summarize files changed, evidence run, and remaining uncertainty.

## Constraints

- Do not broaden a feature into unrelated cleanup without approval.
- Treat compatibility changes as an API-contract or migration concern.
- Do not report a test as passed without the command and result.

## Deliverable

- An implementation, focused tests, and a concise evidence-backed change summary.

## Verification

- [ ] Acceptance criteria map to a test, executable check, or reviewed behavior.
- [ ] Existing behavior outside the request is preserved or explicitly approved to change.
- [ ] Relevant build and test commands pass.

## Handoff

| Condition | Next canonical skill |
|---|---|
| Public request or response shape changes | `project-api-contract` |
| Persistent data shape changes | `project-data-migration` |
