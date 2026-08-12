---
name: example-call-chain
description: Integration tracing example. Use when creating a project skill that traces a request, event, job, or data flow across components and verifies boundaries, transformations, and final side effects.
---

# Integration Trace Example

## Scope

Use this pattern to establish an evidence-backed path from trigger to side effect. Do not use it to prescribe a project architecture that source evidence does not support.

## Required inputs

- A concrete request, event, job, or user action.
- Source declarations at each boundary and the relevant tests or telemetry.

## Procedure

1. Identify the trigger and its validated input shape.
2. Follow each transformation, service call, queue publish, persistence write, or external request.
3. Record assumptions, type or schema transitions, error handling, and idempotency points.
4. Verify the final side effect and the observable result returned to the caller.

## Constraints

- Distinguish proven links from inferred links.
- Include asynchronous consumers and retries where they affect correctness.
- Do not expose secrets or production identifiers in the trace.

## Deliverable

- A compact flow diagram or table with evidence paths, boundary checks, and unresolved gaps.

## Verification

- [ ] Each hop has a source path, trace, or documented interface as evidence.
- [ ] Input and output contracts are compared at every meaningful boundary.
- [ ] Failure and retry behavior is covered where applicable.

## Handoff

| Condition | Next canonical skill |
|---|---|
| A public contract changes | `project-api-contract` |
| A risky production side effect is introduced | `project-security-review` |
