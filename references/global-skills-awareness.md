# Runtime Capability Awareness

Project skills should supply project facts and repeatable local procedures. They should not recreate capabilities already available from the active runtime, such as document processing, browser control, or repository search.

Add this short note to an `AGENTS.md` routing section when it is useful:

```markdown
Project skills provide local rules and context. Before creating a new general-purpose skill,
check the active runtime for an existing capability and combine it with the relevant project skill.
```

Do not name a particular global directory, command, or product UI in the portable core. Those details belong to a runtime adapter.
