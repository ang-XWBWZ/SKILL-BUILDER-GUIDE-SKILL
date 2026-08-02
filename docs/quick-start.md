# 5 分钟建立跨 Agent 项目 Skill

目标不是一次性堆满 skill，而是先把最容易重复、最需要项目事实支撑的工作固化下来。

## 1. 建立入口与目录

在目标项目创建：

```text
AGENTS.md
.agents/skills/
.agents/adapters/
```

从 [项目脚手架](../templates/project-scaffold/) 开始。`AGENTS.md` 放高优先级约束、真实命令和 skill 路由；详细流程放在 `.agents/skills/`。

## 2. 选择一个真实场景

优先选择下列之一，而不是创建包罗万象的“开发 skill”：

- 新成员总在问目录、入口和常用命令：创建 `project-context`。
- 每次功能开发都漏掉测试或兼容性检查：创建 `feature-delivery`。
- API、数据迁移、发布或权限边界经常出错：选择对应的专用 skill。

用 [决策指南](../references/decision-guide.md) 写清楚触发条件、输入、输出、验收和非目标。

## 3. 从证据填写 skill

以 [通用骨架](../templates/skill-template.md) 新建：

```text
.agents/skills/acme-feature-delivery/SKILL.md
```

所有路径、版本、命令、约束都必须来自项目文件或已确认的团队规则。将长表格和领域细节移到同级 `references/`，不要塞进 `AGENTS.md`。

## 4. 校验并交付

```bash
python scripts/validate-skills.py .agents/skills --project-root .
python scripts/check-skill-health.py .agents/skills
```

再逐项确认构建/测试命令、链接、源代码路径和接口契约。只有在某一运行时的安装方式已经验证后，才在 `.agents/adapters/` 添加该运行时的适配说明。

## 示例路线

| 需要 | 从这里开始 |
|---|---|
| 项目导航 | [example-code-map](../templates/example-code-map/SKILL.md) |
| 功能交付 | [example-workflow](../templates/example-workflow/SKILL.md) |
| Bug 定位 | [example-bug-investigation](../templates/example-bug-investigation/SKILL.md) |
| API 变更 | [example-api-contract](../templates/example-api-contract/SKILL.md) |
| 数据变更 | [example-data-migration](../templates/example-data-migration/SKILL.md) |
| 发布与回滚 | [example-release-runbook](../templates/example-release-runbook/SKILL.md) |
