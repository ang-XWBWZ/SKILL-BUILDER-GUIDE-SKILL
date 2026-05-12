# Skill Validation Protocol

> *人谁无过，过而能改，善莫大焉。* ——《左传·宣公二年》
> 信不过自己写的东西，才是写出好东西的开始。

## Three-Layer Model

| Layer | Checks | Tool |
|------|--------|------|
| V1 Format | frontmatter complete, triggers ≥5, YAML valid, no forbidden fields (author/signature/contact) | `validate-skills.py` |
| V2 Structure | dual-axis consistency, skill references exist, cross-references use relative paths | `validate-skills.py` |

> V3 Semantic validation (file paths ≥95%, method names ≥90%, versions 100%) is planned but not yet implemented. See project roadmap.

## Acceptance Criteria (Hard)

| Declaration | Verification | Pass Rate |
|------------|-------------|:---:|
| File paths | Glob/Read to confirm existence | ≥95% |
| Method names | Grep source to confirm | ≥90% |
| Version numbers | Read dependency config | 100% |
| API routes | Read route config | ≥90% |

Below standard = must not publish.

## When to Validate

| Timing | Scope |
|------|---------|
| At creation | All declarations (V1+V2) |
| After refactor | Affected skills (V1+V2) |
| Quarterly | All skills (V1+V2) |
| After V3 implemented | Add semantic checks (file paths, method names, versions) |
