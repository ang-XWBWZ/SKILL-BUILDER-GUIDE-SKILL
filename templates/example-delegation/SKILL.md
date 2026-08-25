---
name: example-delegation
description: Evidence-work decomposition example. Use when creating a project skill that splits independent investigation, review, or verification tasks while preserving scope, provenance, and clear merge criteria.
---

# Evidence Work Decomposition Example

## Scope

Use this pattern to split work into independently verifiable evidence packets. Do not use it to impose a particular agent hierarchy, model tier, or tool syntax.

## Required inputs

- A bounded objective and the relevant repository or external scope.
- Known risks, dependencies, and the decision that will consume the results.

## Procedure

1. Divide work by independent evidence source, such as code structure, test behavior, API contract, or release configuration.
2. Give each packet a concrete question, allowed scope, expected artifacts, and exit condition.
3. Require every packet to separate conclusion, evidence, and uncertainty.
4. Merge only after checking contradictions and gaps against the original objective.

## Constraints

- Keep destructive, privileged, or external actions outside a discovery packet unless explicitly authorized.
- Do not pass an intended conclusion to an independent reviewer.
- Escalate when evidence conflicts or a decision requires owner authority.

## Deliverable

- A merged decision record with traceable evidence and a list of unresolved risks.

## Verification

- [ ] Packets have non-overlapping evidence goals.
- [ ] Every conclusion names supporting paths, commands, or artifacts.
- [ ] Merge notes resolve or retain every contradiction.

## Handoff

| Condition | Next canonical skill |
|---|---|
| A repeated evidence pattern emerges | `project-context` |
| A risky boundary needs a decision | `project-security-review` |
