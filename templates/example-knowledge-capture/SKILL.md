---
name: example-knowledge-capture
description: Project knowledge capture example. Use when creating a project skill that distills verified, reusable conclusions from completed work into a separately managed knowledge area without confusing version-control history, delivery records, or sensitive raw evidence.
---

# Project Knowledge Capture Example

## Scope

Use this pattern when a project repeatedly needs to preserve durable knowledge from implementation, investigation, or operations. Do not use it as a daily log, a source-diff mirror, or a place to store secrets or unreviewed conclusions.

## Required inputs

- Confirmed knowledge destination, access rules, organization, and retention policy.
- Verified source paths, owner decisions, delivery records, or validation artifacts.
- A concrete reason the conclusion will be useful beyond the current delivery.

## Procedure

1. Confirm that the project selected a knowledge area and that this conclusion is reusable rather than task-local.
2. Separate the exact code change in version control from the delivery timeline and the reusable conclusion.
3. Record the concise conclusion, applicability, source links, action implication, exceptions, and refresh trigger.
4. Link affected AGENTS.md or project skills to the narrow note when it changes future work.
5. Record no-capture when the delivery yields no stable knowledge despite a requested review.

## Constraints

- Keep delivery evidence and knowledge notes separate even when they share a documentation root.
- Do not elevate an inference to a fact without verified evidence or an owner decision.
- Do not copy credentials, personal data, private endpoints, or large source output.

## Deliverable

- A verified knowledge note in the selected knowledge area, or a recorded no-capture disposition.

## Verification

- [ ] The note has an authoritative source and an explicit applicability boundary.
- [ ] The note links to source, delivery, or version-control evidence instead of duplicating it.
- [ ] A refresh trigger and any uncertainty are recorded.

## Handoff

| Condition | Next canonical skill |
|---|---|
| The note reveals a recurring project workflow | project-context |
| The note identifies an unsafe boundary | project-security-review |
