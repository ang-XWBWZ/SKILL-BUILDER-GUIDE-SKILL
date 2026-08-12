---
name: example-bug-investigation
description: Bug investigation workflow example. Use when creating a project skill for reproducing a defect, isolating its cause, implementing the smallest safe fix, and proving the regression is covered.
---

# Bug Investigation Example

## Scope

Use this pattern for a reported behavior that differs from the intended behavior. Do not use it for speculative cleanup or incident communication that requires a dedicated operations process.

## Required inputs

- Observed behavior, expected behavior, and a reproduction context.
- Relevant logs, tests, source paths, and environment constraints.

## Procedure

1. Create the smallest reliable reproduction or state why it cannot yet be reproduced.
2. Compare the observed path with the expected contract and identify the first divergence.
3. Inspect surrounding invariants before proposing a fix.
4. Implement the smallest correction and add a regression test or other durable proof.
5. Re-run the reproduction, targeted checks, and relevant broader validation.

## Constraints

- Do not label a root cause until evidence excludes plausible alternatives.
- Preserve diagnostic evidence before changing state when an incident is active.
- Keep unrelated refactors out of the fix unless explicitly approved.

## Deliverable

- A root-cause summary, focused fix, regression evidence, and known residual risk.

## Verification

- [ ] The original symptom is reproduced or the reproduction limitation is explicit.
- [ ] The new proof fails before and passes after the fix when practical.
- [ ] Relevant existing tests still pass.

## Handoff

| Condition | Next canonical skill |
|---|---|
| The defect changes a public interface | `project-api-contract` |
| The defect requires a production mitigation | `project-release-runbook` |
