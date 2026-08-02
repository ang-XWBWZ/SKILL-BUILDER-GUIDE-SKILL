# AGENTS.md Template

Copy this file to the project root as `AGENTS.md`, then replace every placeholder with verified project facts.

```markdown
# {Project name}

{One sentence describing the project and its primary responsibility.}

## Non-negotiable rules

- {compatibility, safety, or ownership constraint}
- {project convention that must not be inferred}

## Commands

| Intent | Command | Expected evidence |
|---|---|---|
| Build | `{verified command}` | {expected artifact or exit status} |
| Test | `{verified command}` | {expected report or exit status} |

## Skill routing

| Request | Canonical skill |
|---|---|
| {recurring task} | `.agents/skills/{project}-{capability}/SKILL.md` |
```

Do not copy entire skill procedures into this file.
