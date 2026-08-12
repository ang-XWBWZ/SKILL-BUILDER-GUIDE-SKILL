# Low-Threshold Process Optimization Suggestions

Use this guide to make a small, evidence-backed process improvement suggestion without turning every delivery into an optimization project.

## Delivery order

Keep the following order. A later item must not delay an earlier one:

| Order | Work | Completion rule |
|---|---|---|
| 1 | Direct single request | Meet its acceptance condition or state the blocker. |
| 2 | Landing implementation | Make and verify the requested project change when a change is in scope. |
| 3 | Required documentation | Update the affected project documentation, or explicitly record why none is needed. |
| 4 | Process optimization suggestion | Offer an optional post-delivery note only when the suggestion threshold is met. |

## Thresholds

| Level | Threshold | Allowed outcome |
|---|---|---|
| No trigger | Orders 1–3 are incomplete, or no verified friction signal exists. | Do not add an optimization note. |
| Suggestion threshold | Orders 1–3 are complete and `verified friction signals >= 1` in the current delivery. | Provide at most one concise, optional recommendation. |
| Authorized-change threshold | A suggestion exists and the user or project owner explicitly authorizes the change. | Plan or implement the process, documentation, or automation change within that authorization. |

The suggestion threshold is intentionally low: one signal is enough to surface an idea. It is not enough to change a project process, create a tracking item, add a skill, or start a follow-up task without direction.

## Valid suggestion signals

Count a signal only when it is observed and can be named with evidence from the current delivery:

- A manual step, repository search, or clarification had to be repeated.
- A missing, stale, or ambiguous instruction caused rework or delayed verification.
- A handoff or validation step had to be rediscovered from source files.
- A documentation gap was corrected while completing the direct request.

Do not count a hypothetical best practice, a vague feeling that the process could be better, or an unverified report.

## Recommendation format

Keep the post-delivery note bounded:

```text
Process optimization suggestion (optional)
Signal:   {one observed friction event}
Evidence: {path, command, or action from this delivery}
Proposal: {smallest project-owned improvement}
Benefit:  {time, clarity, safety, or verification improvement}
Status:   Suggestion only; no process change made
```

Make no more than one suggestion per delivery. Omit the note when it would only restate a broad engineering preference.

## Boundaries

- Do not reopen an accepted direct request merely to optimize the process around it.
- Do not make a recommendation that requires authority outside the project without naming that dependency.
- Do not claim a projected saving, risk reduction, or automation result without evidence.
- Prefer a documentation correction, checklist, or small deterministic helper over a new skill when that is sufficient.
