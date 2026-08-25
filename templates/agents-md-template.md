# AGENTS.md Template

Copy this file to the project root as `AGENTS.md`, then replace every placeholder with verified project facts.

```markdown
# {Project name}

{One sentence describing the project and its primary responsibility.}

## Project map

| Concern | Verified location or fact |
|---|---|
| Main source or entry point | `{verified path}` |
| Tests or checks | `{verified path}` |
| Configuration, generated output, or external contract | `{verified path}` |

## Non-negotiable rules

- {compatibility, safety, or ownership constraint}
- {project convention that must not be inferred}

## Commands

| Intent | Command | Expected evidence |
|---|---|---|
| Build | `{verified command}` | {expected artifact or exit status} |
| Test | `{verified command}` | {expected report or exit status} |

## Knowledge and delivery records

- Knowledge area: {verified location and access/update rule, or “not configured”}
- Delivery records: {verified location and date/archive policy, or “not configured”}
- Knowledge capture: {trigger and note location, or “not enabled”}

## Skill routing

| Request | Canonical skill |
|---|---|
| {recurring task} | `.agents/skills/{project}-{capability}/SKILL.md` |
```

Do not copy entire skill procedures into this file.

When AGENTS.md already exists, assess and augment or merge it by explicit user choice; do not overwrite it by default.
