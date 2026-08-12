# Traceable Delivery and Iteration Management

Use this guide when a project needs a repeatable way to record a bounded delivery from scope through verification and closure. It complements canonical project skills: skills define durable project rules, while a delivery record preserves the evidence for one instance of work.

Do not use a formal record for a simple answer, a read-only lookup, or a low-risk reversible edit unless the project owner requires one. A delivery record is not authorization for deployment, deletion, external communication, or any other privileged action.

## Keep source history, delivery dates, and knowledge distinct

Git or another version-control system is the source of truth for exact code and configuration changes. A delivery record records the work’s dates, scope, decisions, acceptance evidence, and closure; it links to commits, reviews, or diffs rather than copying source changes. A separate knowledge area stores reusable conclusions only when the project selected it during consultation.

| Need | Record |
|---|---|
| Inspect an exact line-level or file-level change | Version-control commit, review, or diff |
| Know when a delivery began, what happened, and why it closed or stopped | Delivery record |
| Reuse a stable conclusion in future work | Knowledge note |

The delivery record’s creation date and dated implementation or verification entries are the lifecycle history. Do not use commit timestamps as a substitute for the project’s delivery chronology.

## Select the record size

| Work shape | Record |
|---|---|
| Question, investigation, or one-off lookup with no deliverable | State the result and evidence in the normal response. |
| Low-risk, bounded, reversible change | Use the compact completion report. |
| Feature, defect fix, cross-module change, configuration or dependency change, or work with explicit acceptance evidence | Use a full delivery record. |
| Persistent data, authority, security, external contract, or hard-to-reverse change | Use a full delivery record plus the applicable specialized skill and recovery planning. |

The project owner may require a full record at any lower risk level. Choose the record before implementation when possible; if the work expands, upgrade the compact report to a full record and explain why.

One full record represents one independently assessable delivery. Split records only when their objectives, acceptance evidence, ownership or timing, and recovery paths are genuinely independent; otherwise preserve one evidence chain across the affected boundaries.

## Lifecycle and gates

Normal lifecycle:

Draft → Scope confirmed → Work items confirmed → Plan confirmed → In progress → Verifying → Closed

Exceptional states: Blocked, Failed pending action, and Cancelled.

- Do not enter implementation while the objective, boundaries, or acceptance conditions are materially unclear. A low-impact assumption may proceed only when it is recorded.
- Do not mark a work item complete until its agreed behavior and acceptance evidence are known.
- Do not mark verification passed when it failed, was skipped, or was not run.
- Do not close a record while a blocking issue is unresolved.
- Record the reason for cancellation or failure and the required next action.
- Close only after evidence, plan-versus-actual differences, and remaining work or risk have a recorded conclusion.

## Full delivery record

A full record must make the following traceable:

1. Context, objective, in-scope and out-of-scope work, assumptions, dependencies, and risks.
2. Observable acceptance conditions and open questions with their resolution or effect.
3. Identified work items mapped to acceptance conditions.
4. Executable steps with prerequisites, expected outputs, evidence, stop conditions, and state.
5. Actual implementation, affected boundaries, artifacts, and timestamps when they matter.
6. Verification commands, paths, samples, observed results, and follow-up action for every failed, skipped, or inapplicable check.
7. Plan-versus-actual differences, open items, risks, and recovery or rollback limitations.
8. Final delivery, status, closure basis, and links to relevant source or validation artifacts.

Use the [delivery-record template](../templates/iteration-record-template.md) as a portable starting point. Let each project decide its record location, identifier, retention period, ownership fields, and approval policy; record those project facts in its canonical skills or AGENTS.md rather than in this guide.

If the project also uses a knowledge area, record whether this delivery is stored there or in a separate delivery-record area. Keep delivery records and reusable knowledge notes distinct even when both are under one documentation root. Follow [knowledge management guidance](knowledge-management.md).

## Compact completion report

For work that does not justify a full record, completion reporting still needs evidence:

~~~text
Result:       observable outcome
Changes:      files, configuration, or decision; write “none” for analysis-only work
Acceptance:   each applicable acceptance condition and result
Verification: commands, paths, or reviewed evidence actually used
Open items:   uncertainty, risk, follow-up, or “none”
Status:       completed / blocked / failed pending action / cancelled
~~~

Never replace evidence with an unsupported statement such as “implemented”, “tested”, or “complete”.

## Keep records distinct

Use a [change model](change-model.md) to preserve causal design reasoning for a risky or cross-boundary change. Use a delivery record to show lifecycle state and completion evidence for a bounded unit of work. Link the two records when both are useful; do not duplicate long design analysis or test logs between them.

At closure, review whether the delivery yielded a durable reusable conclusion only when the project enabled knowledge capture. Put an eligible conclusion in the selected knowledge area with links to its sources; otherwise record “not captured” and why. Do not turn every delivery record into a knowledge note.

## Safety and maintenance

- Redact credentials, secrets, personal data, private endpoints, and license material.
- Link to source files and stored artifacts instead of copying large or sensitive output.
- Retain only the record detail required by the project policy.
- Update or retire the project iteration-management skill when its workflow, approval gates, or evidence sources change.
