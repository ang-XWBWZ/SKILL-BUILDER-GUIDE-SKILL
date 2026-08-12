# AGENTS.md Specification

Use `AGENTS.md` as the short, portable entry point for agents working in a project. It should give an agent enough verified, high-frequency project context to begin ordinary work without rediscovering the project identity, key locations, constraints, commands, documentation destinations, and skill ownership.

## Required shape

Keep the file small enough to read before ordinary work. Use only facts that have been checked in the repository or supplied by the project owner.

```markdown
# {project name}

{one-sentence purpose and primary technology}

## Project map
| Concern | Verified location or fact |
|---|---|
| Main source or entry point | `{verified path}` |
| Tests or checks | `{verified path}` |
| Configuration or generated output | `{verified path}` |

## Non-negotiable rules
- {project-specific safety or compatibility rule}

## Commands
| Intent | Command | Evidence |
|---|---|---|
| Test | `{verified command}` | {expected result} |

## Knowledge and delivery records
- Knowledge area: {verified location, access rule, or “not configured”}
- Delivery records: {verified location and date/archive policy, or “not configured”}
- Knowledge capture: {when to add a reusable note, or “not enabled”}

## Skill routing
| Request | Canonical skill |
|---|---|
| {recurring task} | `.agents/skills/{project}-{capability}/SKILL.md` |
```

## Include

- A precise project identity and scope.
- A compact map of the source, tests, configuration, documentation, or other locations that ordinary work must find.
- Hard constraints that would be dangerous or expensive to rediscover.
- Copy-paste executable commands with an expected outcome.
- The confirmed knowledge-base and delivery-record locations, including an explicit “not configured” state when the project chose not to create them.
- A compact map to skills that actually exist under `.agents/skills/`.
- A short note about an active uncertainty when it materially changes safe behavior.

## Exclude

- Vendor-specific invocation syntax or model names.
- Full skill procedures, long technology inventories, release history, or generated change logs.
- Claims that a runtime automatically discovers the file unless an adapter proves it.
- Generic advice that applies to every software project.

## Existing entry points

Read an existing AGENTS.md before generating another one. Assess whether it is an adequate portable project contract, incomplete guidance, runtime-bound legacy material, or conflicting policy.

- Preserve an adequate file and make a minimal verified delta.
- Augment an incomplete file with missing project map, constraints, commands, knowledge/record locations, or routing facts.
- Merge only after reconciling duplicate or conflicting rules with the user or project owner.
- Move runtime-specific discovery, UI, or invocation details into an adapter only when migration is explicitly approved.
- Replace exact sections or the full file only with explicit scope, a preservation plan, and a check that incoming skill routes remain valid.

Do not create a second competing root instruction file.

## Routing rules

Prefer the narrowest applicable project skill. If no skill matches, work from repository evidence and decide afterward whether the task is recurring enough to justify a new skill. Keep the routing table one-to-one with real directories; remove a row when the corresponding skill is retired.

## Review

- Verify every command in the current repository.
- Confirm that the file gives a new agent enough project map, constraints, commands, documentation locations, and routes to begin ordinary work.
- Check every routed relative path exists.
- Keep `AGENTS.md` independent from optional adapters.
- Update it whenever a hard rule, command, or skill boundary changes.
