---
name: example-code-map
description: >-
  Code map skill template. Used to guide creation of project-specific
  code map skills. Triggered when asking about file locations, directory
  structure, component navigation, or route mapping.
  L0 — Must be executed by Haiku, pure file path lookup.
model_tier: L0
skill_tier: atomic
version: 1.2.0
status: active
---

> *不识庐山真面目，只缘身在此山中。* ——苏轼《题西林壁》
> 在一个陌生项目里迷路的时间，本可以用来做出好东西。

# Code Map Skill Template

> **Position**: Atomic tier / L0 execution tier — pure file path mapping, **no reasoning required, must be executed by Haiku**. Composed by [change-model](../../references/change-model.md) (functional), [delegation](../../references/execution-tree.md) (planning), [skill-builder-guide](../../SKILL.md) (meta).
>
> **Usage**: Scan the project directory, then fill in actual paths following this template structure.

## Trigger Conditions

- Creating a code map skill
- Asking about file locations, directory structure
- Asking "where to develop", "which file has the component"
- Asking about page routes, route mapping

## Related Skills

- [Dev Standards](../example-dev/SKILL.md) — tech stack info
- [Delegation](../example-delegation/SKILL.md) — model delegation rules

---

## 1. Project Structure (Template)

> AI scans the project and replaces `{placeholder}` with actual directory layout.

```
{project}/
├── {source_dir}/
│   ├── {entry_file}
│   ├── {config_dir}/
│   ├── {api_layer_dir}/
│   ├── {service_layer_dir}/
│   └── {data_layer_dir}/
├── {resource_dir}/
│   └── {config_file}
└── {frontend_dir}/          # if present
    └── {pages_dir}/
```

---

## 2. Quick Lookup (Template)

> AI fills in actual paths after scanning the project.

| Need | Lookup Method |
|------|----------|
| Modify API | `{api_layer_dir}/{module}*.{ext}` |
| Modify business logic | `{service_layer_dir}/{module}*.{ext}` |
| Modify data access | `{data_layer_dir}/{module}*.{ext}` |
| Modify config | `{config_dir}/{config_file}` |
| Modify frontend page | `{frontend_dir}/{pages_dir}/*.{ext}` |

---

## 3. Routes & Pages (Template)

| Path | File | Description |
|------|------|------|
| / | `{file_path}` | Homepage |
| /{path} | `{file_path}` | {description} |

---

## 4. Model Tier

**L0 — Haiku / atomic tier**: Pure file path lookup, zero reasoning required. Main model must not directly execute this skill — **must delegate to Haiku**.
