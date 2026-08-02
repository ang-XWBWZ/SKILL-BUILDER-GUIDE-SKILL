# AGENTS.md Specification

Use `AGENTS.md` as the short, portable entry point for agents working in a project. It should answer: what is this project, which constraints matter now, how to verify work, and which project skill owns a recurring task.

## Required shape

Keep the file small enough to read before ordinary work. Use only facts that have been checked in the repository or supplied by the project owner.

```markdown
# {project name}

{one-sentence purpose and primary technology}

## Non-negotiable rules
- {project-specific safety or compatibility rule}

## Commands
| Intent | Command | Evidence |
|---|---|---|
| Test | `{verified command}` | {expected result} |

## Skill routing
| Request | Canonical skill |
|---|---|
| {recurring task} | `.agents/skills/{project}-{capability}/SKILL.md` |
```

## Include

- A precise project identity and scope.
- Hard constraints that would be dangerous or expensive to rediscover.
- Copy-paste executable commands with an expected outcome.
- A compact map to skills that actually exist under `.agents/skills/`.
- A short note about an active uncertainty when it materially changes safe behavior.

## Exclude

- Vendor-specific invocation syntax or model names.
- Full skill procedures, long technology inventories, release history, or generated change logs.
- Claims that a runtime automatically discovers the file unless an adapter proves it.
- Generic advice that applies to every software project.

## Routing rules

Prefer the narrowest applicable project skill. If no skill matches, work from repository evidence and decide afterward whether the task is recurring enough to justify a new skill. Keep the routing table one-to-one with real directories; remove a row when the corresponding skill is retired.

## Validation

- Verify every command in the current repository.
- Check every routed relative path exists.
- Keep `AGENTS.md` independent from optional adapters.
- Update it whenever a hard rule, command, or skill boundary changes.
