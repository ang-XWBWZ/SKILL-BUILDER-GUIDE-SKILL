---
name: example-api-contract
description: API contract example. Use when creating a project skill for adding, changing, reviewing, documenting, or validating a public request, response, event, schema, version, or compatibility commitment.
---

# API Contract Example

## Scope

Use this pattern for interfaces consumed outside the immediate implementation boundary. Do not use it for internal refactors that do not alter a supported contract.

## Required inputs

- Current contract source, consumers, versioning policy, and change request.
- Compatibility expectations, error semantics, examples, and validation tooling.

## Procedure

1. Locate the authoritative contract and identify known consumers.
2. Describe the proposed change as additions, removals, semantic changes, and compatibility impact.
3. Choose an evolution path: compatible extension, explicit version, deprecation window, or approved breaking change.
4. Update implementation, documentation, examples, and contract tests together.
5. Communicate consumer actions and a rollback or containment strategy.

## Constraints

- Never infer public compatibility from implementation convenience.
- Preserve response/error semantics unless the change explicitly approves a break.
- Keep secrets, internal hostnames, and production tokens out of examples.

## Deliverable

- An updated contract, compatibility assessment, consumer impact list, and verification evidence.

## Verification

- [ ] Request, response, errors, and defaults are documented and tested.
- [ ] Consumer impact is classified as compatible, coordinated, or breaking.
- [ ] Contract links and examples match the implementation.

## Handoff

| Condition | Next canonical skill |
|---|---|
| Data shape requires persistent conversion | `project-data-migration` |
| A release needs observation and rollback | `project-release-runbook` |
