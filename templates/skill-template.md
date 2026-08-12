# Portable SKILL.md Template

Replace every `{placeholder}` with verified project information before placing the file in `.agents/skills/{project}-{capability}/SKILL.md`.

```markdown
---
name: {project}-{capability}
description: >-
  {Project} {capability} workflow. Use when {specific requests, conditions,
  or project vocabulary that should trigger this skill}.
---

# {Project} {Capability}

## Scope

Use this skill to {bounded outcome}. Do not use it to {nearby non-goal}; use
`{other-skill}` when that condition applies.

## Required inputs

- {ticket, files, user decision, or evidence required before acting}

## Procedure

1. {verified first step}
2. {decision point and evidence to collect}
3. {change or analysis step}
4. {verification step}

## Constraints

- {compatibility, security, or ownership constraint}

## Deliverable

- {files, report, decision, or implementation result}

## Verification

- [ ] {observable check}
- [ ] {command, test, or review evidence}

## Completion report

- Result: {observable outcome}
- Changes: {files, configuration, or decision; write “none” for analysis-only work}
- Acceptance and verification: {actual evidence and result}
- Open items: {uncertainty, risk, follow-up, or “none”}
- Status: completed / blocked / failed pending action / cancelled

Use a project delivery record when the work has multiple steps, explicit closure requirements, or material recovery risk.

## Handoff

| Condition | Next canonical skill |
|---|---|
| {measurable condition} | `{project}-{other-capability}` |
```

Keep runtime metadata and installation notes out of this file; put them in `.agents/adapters/`.
