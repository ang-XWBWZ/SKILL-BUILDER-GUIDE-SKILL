---
name: example-iteration-management
description: Traceable delivery management example. Use when creating a project skill for planning, recording, verifying, and closing a bounded feature, defect fix, cross-boundary change, or other delivery that needs durable evidence and explicit status.
---

# Traceable Delivery Management Example

## Scope

Use this pattern when a project repeatedly needs evidence from scope through closure for consequential deliveries. Do not use it for a simple question, read-only lookup, or low-risk reversible edit unless the project requires a record.

## Required inputs

- Requested outcome, boundaries, acceptance conditions, and applicable owner decisions.
- Project-defined location, naming, retention, and approval rules for delivery records.
- Knowledge-base location and disposition rules when the project wants reusable knowledge capture.
- Affected source, configuration, contract, data, and verification evidence.

## Procedure

1. Select no record, a compact completion report, or a full delivery record based on risk, reversibility, and the project policy.
2. Confirm the objective, boundaries, acceptance conditions, assumptions, dependencies, and open questions before implementation.
3. Map work items to acceptance conditions and plan executable steps with evidence and stop conditions.
4. Record dates, actual work, version-control references, and verification results as they occur; treat failed, skipped, and inapplicable checks differently.
5. Compare actual work with the plan, record open work, risk, recovery, and any knowledge-capture disposition, then close only when the project closure gate is met.

## Constraints

- A delivery record is evidence, not authorization for privileged or irreversible actions.
- Treat version control as the exact source of code change; link revisions or diffs instead of copying them into the record.
- Do not mark a result passed, complete, or closed without the observed evidence.
- Keep secrets, unnecessary personal data, and large sensitive output out of records.

## Deliverable

- A compact completion report or full delivery record with traceable dates, scope, version-control evidence, verification, open work, knowledge disposition, and final status.

## Verification

- [ ] Every work item maps to an acceptance condition or has an explicit disposition.
- [ ] Every applicable check records its actual result and evidence.
- [ ] Version-control and knowledge-capture dispositions are explicit.
- [ ] Closure includes plan-versus-actual differences, remaining risk, and recovery or its limitation.

## Handoff

| Condition | Next canonical skill |
|---|---|
| A public interface changes | project-api-contract |
| Persistent state changes | project-data-migration |
| A production rollout needs observation | project-release-runbook |
