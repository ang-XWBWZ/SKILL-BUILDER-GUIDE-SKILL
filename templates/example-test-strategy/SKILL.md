---
name: example-test-strategy
description: Test strategy example. Use when creating a project skill that chooses proportional automated and manual verification for a change, identifies risk-based cases, and records evidence without mandating one test framework.
---

# Test Strategy Example

## Scope

Use this pattern to select tests based on behavioral risk and project evidence. Do not use it to force a generic coverage target or replace an existing test policy.

## Required inputs

- Change summary, affected boundaries, existing tests, and test commands.
- Known failure modes, compatibility expectations, and environment limits.

## Procedure

1. Enumerate changed behaviors and affected callers or state transitions.
2. Select a smallest useful set of unit, integration, contract, end-to-end, and manual checks.
3. Include a normal case, an important edge case, and a negative or failure path where risk warrants it.
4. Run targeted checks first, then broader checks proportional to the blast radius.
5. Record commands, environments, exclusions, and observed results.

## Constraints

- Reuse project test conventions before adding new tooling.
- Do not claim coverage for an unrun or unavailable environment.
- Treat security, migration, and release checks as separate specialized concerns.

## Deliverable

- A risk-based test matrix and evidence record for the change.

## Verification

- [ ] Every changed behavior has an appropriate check or justified exception.
- [ ] Existing failures are distinguished from failures introduced by the change.
- [ ] Commands and results are reproducible by another contributor.

## Handoff

| Condition | Next canonical skill |
|---|---|
| API behavior is externally consumed | `project-api-contract` |
| Release confidence depends on production observation | `project-release-runbook` |
