---
name: example-security-review
description: Security boundary review example. Use when creating a project skill for evaluating changes that affect authentication, authorization, secrets, data exposure, external inputs, privileged actions, or security-sensitive dependencies.
---

# Security Boundary Review Example

## Scope

Use this pattern before changing a security-sensitive boundary. Do not use it as a claim that a general code review provides a complete security audit.

## Required inputs

- Proposed change, asset or data classification, trust boundaries, and threat assumptions.
- Existing policy, tests, logging, dependency, and incident-response evidence.

## Procedure

1. Identify assets, actors, entry points, and trust boundaries touched by the change.
2. Compare authentication, authorization, validation, logging, and secret handling with project policy.
3. Consider misuse cases such as privilege escalation, data disclosure, replay, injection, and unsafe defaults.
4. Define mitigations, test cases, monitoring signals, and any owner approval needed.
5. Re-check the implementation and configuration after mitigation.

## Constraints

- Do not expose secret material in reports, tests, or logs.
- Escalate unapproved privileged actions and policy conflicts to the responsible owner.
- Treat third-party dependency changes as part of the boundary when they handle sensitive data or authority.

## Deliverable

- A threat-aware review record, mitigation plan, verification evidence, and residual-risk statement.

## Verification

- [ ] Every touched trust boundary has an explicit access-control and input-validation check.
- [ ] Secret, logging, and error-handling behavior is reviewed for disclosure risk.
- [ ] Residual risk and required owner decisions are explicit.

## Handoff

| Condition | Next canonical skill |
|---|---|
| Change reaches production | `project-release-runbook` |
| Finding reveals a defect | `project-bug-investigation` |
