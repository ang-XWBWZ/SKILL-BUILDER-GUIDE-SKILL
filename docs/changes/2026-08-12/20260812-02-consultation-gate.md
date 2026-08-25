# Consultation Gate for Skill Construction

## WHY

- Problem: a broad or repeated skill-builder activation could move directly from repository inspection to generation, even when the user’s current operation, desired depth, or preservation intent was unknown.
- Desired outcome: every initial or repeat activation establishes the current operation before a scan, generation, copy, or overwrite begins.
- Constraints: keep portable frontmatter limited to name and description; do not persist runtime-specific conversation state as canonical project knowledge; do not ask redundant questions when the user already supplied the material facts.

## WHAT

| Concern | Change | Risk control |
|---|---|---|
| Initial activation | Add a concise current-operation consultation gate | Ask before generation when intent is broad or ambiguous |
| Repeat activation | Treat existing assets as a re-entry context | Preserve by default; require an exact scope for replacement |
| Build depth | Define baseline, focused, and comprehensive maturity choices | Do not default to a broad library |
| Evidence review | Add a manual consultation review | Do not equate document shape with user-intent confirmation |

## HOW

- Add a portable consultation protocol with opening question, targeted follow-up, re-entry behavior, intent summary, and activation gate.
- Make consultation step 0 of the core builder workflow and connect it to skill selection, phase-0 analysis, evidence review, architecture review, and onboarding.
- Keep confirmed durable project facts in canonical project files only when relevant; keep active consultation state in the current conversation or a project-owned record.

## EVIDENCE

- Review the consultation gate against the active conversation and target-project sources.
- Check local Markdown links after documentation updates.
- Remaining limitation: a document check cannot observe a conversation, so an agent must report the consultation gate as manual evidence.
