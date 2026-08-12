# Delivery Record Template

Use this portable template for a distinct delivery that needs traceable scope, implementation, verification, and closure. Copy it to the location defined by the target project, then replace every placeholder with verified project facts. Do not create fictional implementation, test, or closure evidence.

For a low-risk bounded change, use only the compact completion report at the end. Project-specific naming, storage location, approvals, retention, and responsible roles belong in the target project, not in this template.

## Full record

~~~markdown
# {delivery title}

## Record

- Identifier: {project-defined identifier}
- Record date: {project-defined delivery date or archive date}
- Status: Draft / Scope confirmed / Work items confirmed / Plan confirmed / In progress / Verifying / Closed / Blocked / Failed pending action / Cancelled
- Started:
- Closed:
- Owner:
- Request source:
- Affected areas:
- Related branch, version, issue, or change record:
- Delivery-record location:
- Knowledge disposition: separate delivery area / knowledge-base record / not requested

## 1. Scope and acceptance

### Context and objective

- Context: {observed problem or requested outcome}
- Objective: {observable result}

### Boundaries

- In scope:
- Out of scope:
- Constraints and assumptions:
- Dependencies and risks:

### Acceptance conditions

- [ ] {observable acceptance condition}

### Open questions

| ID | Question | Impact | Resolution or owner | State |
|---|---|---|---|---|
| Q-01 |  |  |  | Open |

## 2. Work items

| ID | Behavior or outcome | Affected boundary | Acceptance condition | State |
|---|---|---|---|---|
| W-01 |  |  |  | Planned |

## 3. Plan

| Step | Prerequisite | Action | Expected output | Evidence and stop condition | State |
|---|---|---|---|---|---|
| 1 | Scope and work items confirmed | Identify affected files, interfaces, configuration, and data paths | Impact list | Paths and boundaries verified | Planned |
| 2 |  |  |  |  | Planned |
| 3 | Changes complete | Run applicable verification | Results with evidence | Failure, skip, or evidence gap blocks closure | Planned |
| 4 | Verification results available | Review and close this record | Closure material | Record completeness and sensitive-data check | Planned |

## 4. Dated implementation log

| Time | Related step or work item | Changed boundary or artifact | Actual work | Evidence and result | State |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 5. Version-control evidence

Git or the project’s version-control system is the source of truth for exact code and configuration changes. Link to the relevant revision, review, or diff; do not copy the source diff into this record.

| Revision, review, or diff | Exact-change source | Affected boundary | Relationship to this delivery |
|---|---|---|---|
|  |  |  |  |

## 6. Verification

| Check | Command, path, sample, or review evidence | Result | Evidence or error summary | Follow-up |
|---|---|---|---|---|
| Build or static check |  | Passed / Failed / Not run / Not applicable |  |  |
| Tests or focused verification |  | Passed / Failed / Not run / Not applicable |  |  |
| Runtime, integration, or contract check |  | Passed / Failed / Not run / Not applicable |  |  |
| Configuration or environment check |  | Passed / Failed / Not run / Not applicable |  |  |
| Record review |  | Passed / Failed |  |  |

## 7. Plan versus actual

- Planned:
- Actual:
- Difference and reason:
- Effect on scope, risk, or acceptance:

## 8. Open work, risk, and recovery

### Open work

| ID | Item | Impact | Next action | Owner or due condition | State |
|---|---|---|---|---|---|
| O-01 | None /  |  |  |  |  |

### Risk and recovery

- Remaining risk:
- Rollback, recovery, or explicit limitation:

## 9. Closure

### Closure checklist

- [ ] Objective, boundaries, and acceptance conditions are confirmed.
- [ ] Every confirmed work item is complete or has a recorded deferral, cancellation, or failure outcome.
- [ ] Completed steps have actual outputs and evidence.
- [ ] Applicable verification has recorded passed, failed, not-run, or not-applicable results.
- [ ] The record date, dated implementation entries, and applicable version-control references are present.
- [ ] Plan-versus-actual differences are explained.
- [ ] Open work, risk, and recovery are recorded.
- [ ] Knowledge capture has an explicit disposition; any reusable note is stored separately from this delivery record.
- [ ] The record contains no secrets, unnecessary personal data, or sensitive copied output.

### Actual delivery

- Delivered result:
- Changed artifacts or decisions:
- Version-control evidence:
- Key verification evidence:
- Knowledge note or no-capture disposition:

### Final conclusion

- Final status: Closed / Blocked / Failed pending action / Cancelled
- Closure basis:
- Closing authority:
- Closure time:

## Related material

- Source or configuration paths:
- Version-control revisions, reviews, or diffs:
- Validation logs or artifacts:
- Related documentation:
- Knowledge notes:
~~~

## Compact completion report

~~~text
Result:       {observable outcome}
Changes:      {files, configuration, or decision; “none” for analysis-only work}
Acceptance:   {each applicable acceptance condition and result}
Verification: {commands, paths, or reviewed evidence actually used}
Open items:   {uncertainty, risk, follow-up, or “none”}
Status:       completed / blocked / failed pending action / cancelled
~~~
