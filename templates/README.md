# Templates

Copy these to your project's `.claude/skills/` and customize.

> Each template is a mini-skill (SKILL.md + agents/openai.yaml + references/). Replace `{placeholder}` content with project-specific details.

---

## Template Inventory

| Template | Execution | Composition | Purpose |
|------|:------:|:------:|------|
| [example-dev](example-dev/) | L1 | atomic | Tech stack, code standards, layered architecture |
| [example-code-map](example-code-map/) | **L0** | atomic | File location, directory structure [Haiku] |
| [example-delegation](example-delegation/) | L1 | atomic | Delegation rules, dispatch format, output standards |
| [example-workflow](example-workflow/) | L1 | functional | Development workflow, phase-step checklists |
| [example-call-chain](example-call-chain/) | L1 | functional | Call-chain tracing, data flow, type matching |

## Skeleton Templates

| File | Purpose |
|------|------|
| `skill-template.md` | SKILL.md skeleton with frontmatter |
| `openai-template.yaml` | openai.yaml trigger config skeleton |
| `change-model-template.md` | Change report template (WHY/WHAT/HOW/VALIDATION) |

## How to Use

```bash
# Copy a template to your project
cp -r templates/example-dev/ myproject/.claude/skills/myproject-dev/

# Customize: replace {project}, {skill-type}, triggers, tech stack details
# Validate: python scripts/validate-skills.py .claude/skills/myproject-dev/
```
