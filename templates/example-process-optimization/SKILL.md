---
name: example-process-optimization
description: Process optimization suggestion example. Use after completing a direct request, its implementation, and required documentation when one verified friction signal warrants a low-cost optional improvement recommendation; do not use it to change project process without owner approval.
---

# Process Optimization Suggestion Example

## Scope

Use this pattern after a completed delivery reveals one concrete source of avoidable friction. Do not use it to interrupt current work, create a broad improvement program, or modify a project process without authorization.

## Required inputs

- Evidence that the direct request, requested change, and required documentation are complete or intentionally not applicable.
- One observed friction signal from the current delivery.

## Procedure

1. Confirm that the direct request, implementation, and documentation have been handled in that order.
2. Record one observed signal with its path, command, repeated action, or clarification.
3. Propose the smallest project-owned improvement that addresses that signal.
4. State the expected benefit and any owner decision needed.
5. Present no more than one optional recommendation; do not implement it unless authorized.

## Constraints

- One verified signal is enough to suggest; it is not enough to change a process.
- Do not infer a recurring problem from hypothetical or unverified friction.
- Do not create a new skill, task, ticket, or automation without direction.

## Deliverable

- A concise post-delivery suggestion containing signal, evidence, proposal, benefit, and a clear “suggestion only” status.

## Verification

- [ ] The original request, implementation, and documentation are complete before the suggestion appears.
- [ ] The signal comes from the current delivery and has concrete evidence.
- [ ] No process change is claimed or performed without explicit approval.

## Handoff

| Condition | Next canonical skill |
|---|---|
| Owner authorizes a documentation or workflow change | `project-feature-delivery` |
