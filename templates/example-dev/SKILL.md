---
name: example-dev
description: Project convention reference example. Use when creating a skill that captures verified technology choices, code patterns, local constraints, and implementation checks for a specific repository.
---

# Project Conventions Example

## Scope

Use this pattern to build a concise project-conventions skill from real source evidence. Do not use it as a substitute for an API contract, migration plan, or release runbook.

## Required inputs

- Active dependency manifests and build configuration.
- Representative files from each meaningful code area.
- Existing contributor guidance and non-negotiable project rules.

## Procedure

1. Record the actual language, framework, package manager, and verification commands.
2. Compare several representative implementations before naming a convention.
3. Separate an established pattern from a legacy exception and state the exception’s scope.
4. Write only conventions that change a contributor’s implementation decision.

## Constraints

- Do not invent a layered architecture when the repository uses another structure.
- Preserve owner-provided conventions when they conflict with an inferred pattern.
- Link detailed examples from a `references/` file instead of copying long snippets.

## Deliverable

- A project-specific conventions skill with a technology table, key patterns, exceptions, and verified commands.

## Verification

- [ ] Each version comes from an active manifest or lockfile.
- [ ] Each named pattern has at least two source examples or an owner-provided rule.
- [ ] Every command is executable in the current repository.

## Handoff

| Condition | Next canonical skill |
|---|---|
| Contributors repeatedly need file locations | `project-code-map` |
| A change crosses a public boundary | `project-api-contract` |
