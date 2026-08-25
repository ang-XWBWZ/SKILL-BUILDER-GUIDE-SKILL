---
name: example-code-map
description: Repository orientation example. Use when creating a project skill that helps an agent locate entry points, modules, generated artifacts, configuration, and verified development commands.
---

# Repository Orientation Example

## Scope

Use this pattern to make unfamiliar repositories navigable. Do not describe implementation conventions in depth; point to the project-conventions skill for that information.

## Required inputs

- Root directory tree, manifests, and contributor documentation.
- Entry points, test locations, configuration roots, and generated-code boundaries.

## Procedure

1. Map the top-level directories that matter to ordinary changes.
2. Identify the entry point for each runnable component or service.
3. List exact locations for tests, configuration, schemas, and generated output.
4. Add a task-to-location table using only paths that exist.

## Constraints

- Keep the map shallow and task-oriented.
- Mark generated directories as read-only unless project rules permit direct edits.
- Remove stale paths during every structural refactor.

## Deliverable

- A concise directory map and a quick lookup table for common change targets.

## Verification

- [ ] Every listed path exists.
- [ ] Every command was checked against the active build configuration.
- [ ] Generated and source-owned paths are clearly distinguished.

## Handoff

| Condition | Next canonical skill |
|---|---|
| The task changes behavior across modules | `project-feature-delivery` |
| The task exposes an external interface | `project-api-contract` |
