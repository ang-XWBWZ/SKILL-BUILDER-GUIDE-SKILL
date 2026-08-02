---
name: example-feedback-capture
description: Feedback improvement example. Use when creating a project skill that turns recurring user, reviewer, or operator feedback into scoped evidence, prioritized improvements, and verified follow-up without retaining unnecessary personal data.
---

# Feedback Improvement Example

## Scope

Use this pattern for recurring product or workflow feedback that can improve project behavior. Do not use it as an unbounded conversation log or a place to store sensitive user content.

## Required inputs

- Feedback source, date range, and consent or retention requirements.
- The affected workflow, component, or documented expectation.

## Procedure

1. Normalize feedback into an observed problem, impact, and supporting evidence.
2. Group duplicates without preserving unnecessary personally identifying detail.
3. Identify the smallest project-owned change or documentation correction that could address the recurring issue.
4. Define a measurable follow-up signal and review the result after the change.

## Constraints

- Follow project privacy and retention rules.
- Do not treat praise or frustration as an instruction without a concrete project implication.
- Delete or redact raw feedback when the agreed retention period ends.

## Deliverable

- A prioritized improvement record with evidence, owner decision, and success signal.

## Verification

- [ ] The record contains no unnecessary personal or secret data.
- [ ] The proposed change is tied to a repeated or material observation.
- [ ] A follow-up measure or review date exists.

## Handoff

| Condition | Next canonical skill |
|---|---|
| Feedback exposes a reproducible defect | `project-bug-investigation` |
| Feedback exposes an unsafe boundary | `project-security-review` |
