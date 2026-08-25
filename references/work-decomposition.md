# Work Decomposition for Skill Authoring

Split investigation when it produces independent evidence, not merely because multiple agents or tools are available.

## Create independent evidence packets

Use one packet per concern:

| Concern | Inputs | Output |
|---|---|---|
| Repository orientation | tree, manifests, root docs | project map and verified commands |
| Convention extraction | representative source files | patterns and exceptions |
| Boundary analysis | APIs, schemas, integrations | risks and affected consumers |
| Workflow discovery | CI, scripts, runbooks | repeatable phases and checks |

Each packet must distinguish facts, inferences, and unknowns. Merge only after checking for contradictions.

## Match work to capability

Describe the capability required by the work rather than a particular model:

- **Inspection**: enumerate files, read configuration, collect source evidence.
- **Synthesis**: compare evidence, infer a pattern, choose a skill boundary.
- **Change**: edit files within an approved scope.
- **Verification**: run tests, validate links, inspect diffs.
- **Coordination**: ask the owner for missing authority or an irreversible decision.

Escalate when evidence conflicts, risk rises, or a task requires authority that has not been granted. Do not invent a mandatory delegation policy around a particular model or provider.

## Output format

Use this compact result format when a scan is performed separately:

```text
Conclusion: {direct answer}
Evidence:   {paths, commands, or observed patterns}
Uncertainty:{missing data, ambiguity, or "none"}
```
