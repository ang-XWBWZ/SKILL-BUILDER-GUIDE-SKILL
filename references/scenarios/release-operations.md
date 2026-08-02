# Release and Operations Skills

Create an operations skill when a project has repeatable production actions whose safety depends on sequencing, observation, approval, or rollback.

## Good candidates

| Need | Skill focus |
|---|---|
| Routine deployment | Release runbook |
| Configuration rollout | Configuration change procedure |
| Incident mitigation | Incident triage or rollback procedure |
| Scheduled maintenance | Maintenance window checklist |

## Authoring notes

- Freeze artifact, configuration, and approval evidence before a release step.
- Define observable health and business signals, a review window, and thresholds for pause or rollback.
- Distinguish deployment success from service health.
- Store commands only after they are verified for the current environment; never record credentials.

## Done definition

The skill gives an operator enough context to prepare, act, observe, communicate, and recover without improvising privileged or irreversible actions.
