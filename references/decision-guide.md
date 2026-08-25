# Decision Guide — Select the First Skills

Create skills for recurring project work with stable inputs, a bounded outcome, and evidence that can be refreshed. Do not create a broad “do everything” skill.

## Confirm the current operation

Before selecting skills, use [the consultation protocol](consultation-protocol.md) to determine whether the user wants to initialize, assess, repair, extend, migrate, review, or only plan. A repeated builder trigger does not by itself authorize generation or replacement.

## Then ask four selection questions

| Question | What it reveals |
|---|---|
| Which work repeatedly makes contributors search the same files or conventions? | Candidate project-context or code-map skill |
| Which change classes have a repeated sequence and acceptance criteria? | Candidate workflow skill |
| Which boundary can cause compatibility, data, security, or release risk? | Candidate specialized skill |
| Which facts change often enough to require a refresh source? | Reference layout and maintenance plan |

## Start small

| Signal | First skill to create |
|---|---|
| New or unfamiliar repository | `project-context` or `code-map` |
| Repeated feature delivery with reviews/tests | `feature-delivery` |
| Versioned or externally consumed API | `api-contract` |
| Persistent data changes | `data-migration` |
| Production release steps or rollback | `release-runbook` |
| Sensitive boundaries, secrets, or permissions | `security-review` |
| Repeated incident diagnosis | `bug-investigation` |
| Consequential deliveries need a repeatable scope-to-closure evidence trail | `iteration-management` |
| Verified conclusions repeatedly need reuse outside their original delivery | `knowledge-capture` |

Add one skill at a time. A skill earns its place when it saves a real rediscovery cost, reduces a known risk, or supplies a check that otherwise gets missed.

An iteration-management skill owns the lifecycle record for a bounded delivery; it does not replace the specialized skill that owns API, data, release, or security decisions. Add it when the project repeatedly needs comparable completion evidence, explicit closure gates, or a reliable history of plan-versus-actual differences.

A knowledge-capture skill owns the extraction of reusable conclusions into the selected knowledge area; it does not replace version-control history or delivery records. Add it only when a knowledge destination and ongoing update responsibility exist.

## Low-threshold suggestions are not new skills

After a direct request, implementation, and required documentation are complete, one verified friction signal is enough to offer one optional process improvement suggestion. It is not enough to create a new skill or change a process. Use the [process-optimization guide](process-optimization.md) for the suggestion threshold and the explicit-approval threshold for change.

## Boundaries before content

For each candidate selected after consultation, write this mini-contract before authoring it:

```text
Trigger:      {specific request or condition}
Inputs:       {project facts, files, ticket, or evidence required}
Output:       {decision, files, report, or verified result}
Verification: {observable check}
Non-goals:    {nearby work owned by another skill}
```

If Trigger and Non-goals cannot be distinguished, merge or defer the candidate instead of creating two overlapping skills.

## Review cadence

Refresh a skill after a structural refactor, toolchain change, new external contract, or repeated correction. Remove a skill when the underlying workflow no longer exists.
