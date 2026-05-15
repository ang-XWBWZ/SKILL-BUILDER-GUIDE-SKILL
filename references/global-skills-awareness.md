---
name: global-skills-awareness
description: How to ensure generated project skills don't overshadow globally installed skills — a small awareness block for CLAUDE.md and SKILL.md templates.
model_tier: L3
skill_tier: meta
version: 1.0.0
status: active
---

# Global Skills Awareness

> *登高而招，臂非加长也，而见者远。* ——《荀子·劝学》
> Project skills keep you focused on the present. Global skills keep you from reinventing wheels.

## Problem

After initializing project-specific skills, agents tend to only look within the project's skills, ignoring globally installed ones (`~/.claude/skills/`). The result: the agent uses the project dev skill for everything — even when a better global diagnose skill already exists.

## Solution

Embed a ≤100-word content block in generated output to remind the agent that global skills exist.

### Position 1: End of CLAUDE.md §C Skill Routing

```markdown
### Global Skills

Project skills take priority, but don't forget globally installed skills (`~/.claude/skills/`).
Use `/skills` to list all available skills. Don't reimplement what a global skill already does.
```

### Position 2: SKILL.md template, `## Related Skills`

Append a one-line hint at the end of `## Related Skills`:

```markdown
- Global skills (`~/.claude/skills/`) may already have related functionality. Use `/skills` to check.
```

## Design Constraints

- ≤100 words — a signpost, not a tutorial
- No specific global skill names — each environment is different
- Insert into existing sections, not a new standalone section — reduce reading overhead
