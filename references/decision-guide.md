# Decision Guide — Select the First Skills

Create skills for recurring project work with stable inputs, a bounded outcome, and evidence that can be refreshed. Do not create a broad “do everything” skill.

## Ask four questions

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

Add one skill at a time. A skill earns its place when it saves a real rediscovery cost, reduces a known risk, or supplies a check that otherwise gets missed.

## Boundaries before content

For each candidate, write this mini-contract before authoring it:

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
