---
name: sample-context
description: Sample project context skill. Use when navigating this project, locating its core files, or checking the verified commands and constraints recorded for the repository.
---

# Sample Context

## Scope

Use this sample to orient work in a new project. Replace it with real project facts before relying on it for implementation decisions.

## Required inputs

- Current repository tree, active manifests, and contributor documentation.

## Procedure

1. Confirm the project root and active build configuration.
2. Locate source, tests, configuration, and generated outputs.
3. Record only verified paths and commands.

## Constraints

- Do not treat this sample as a source of project-specific truth.

## Deliverable

- A refreshed project-context skill based on current repository evidence.

## Verification

- [ ] Every recorded path exists.
- [ ] Every command is verified before publishing.

## Handoff

| Condition | Next canonical skill |
|---|---|
| A recurring feature workflow is discovered | `project-feature-delivery` |
