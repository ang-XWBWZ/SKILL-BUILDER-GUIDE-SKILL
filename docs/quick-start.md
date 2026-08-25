# 5 分钟建立跨 Agent 项目 Skill

目标不是一次性堆满 skill，而是先把最容易重复、最需要项目事实支撑的工作固化下来。

## 0. 确认本次要做什么

初始或再次激发构建器时，先只读确认是否已有 `AGENTS.md`、`.agents/skills/` 或其他项目约定，然后确认当前操作：初始化、评估、修复、扩展、迁移、审查或仅制定计划。

如果用户没有明确本次目标，先问“这次想对项目的 skill 系统做什么？”；再按需要确认目标范围、期望完善程度和会影响范围、权限、兼容性或验收的约束。询问是否已有可用知识库、交付记录是否进入该库、是否提炼可复用知识；没有知识库时，由用户决定创建项目文档区还是使用专门的文档位置。已有 `AGENTS.md` 必须先评估，再由用户选择保留、增补、合并、迁移或替换。重复激发默认保留已有资产，不直接重建或覆盖。详见[咨询协议](../references/consultation-protocol.md)。

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
- 多步骤或高风险交付需要范围、验证和结案证据：创建 `iteration-management`。

用 [决策指南](../references/decision-guide.md) 写清楚触发条件、输入、输出、验收和非目标。

## 3. 从证据填写 skill

以 [通用骨架](../templates/skill-template.md) 新建：

```text
.agents/skills/acme-feature-delivery/SKILL.md
```

所有路径、版本、命令、约束都必须来自项目文件或已确认的团队规则。将长表格和领域细节移到同级 `references/`，不要塞进 `AGENTS.md`。但 `AGENTS.md` 不能只是空入口：必须包含项目地图、硬约束、真实命令、已确认的知识/迭代记录位置和 skill 路由，足以让 agent 开始日常工作。

若项目需要可追溯交付，使用[通用交付记录模板](../templates/iteration-record-template.md)作为起点，并由项目自行规定保存位置、编号、审批与留存规则。低风险工作可使用简要完成汇报；多步骤、跨边界或恢复风险较高的工作使用完整记录。精确代码变更留在 Git 或其他版本控制的 revision/diff 中，迭代模板记录日期与交付生命周期；可复用结论再使用[知识笔记模板](../templates/knowledge-note-template.md)单独提炼到已确认的知识区。

## 4. 审查并交付

```bash
python scripts/check-markdown-links.py .
```

链接检查仅检查本地 Markdown 链接。再逐项审查构建/测试命令、链接、源代码路径和接口契约，并根据当前用户目标判断指令是否足以完成工作。完成交付时报告实际结果、实际改动或决策、验收与验证证据、未闭环事项及最终状态；不要以“已完成”代替证据。只有在某一运行时的安装方式已经验证后，才在 `.agents/adapters/` 添加该运行时的适配说明。参见[证据审查指南](../references/evidence-review.md)。

在直接需求、实现和必要文档都完成后，如果本次交付出现 1 条有证据的摩擦信号，可补充 1 条可选的流程优化建议；未经明确授权，不改变流程或创建后续任务。参见[流程优化建议阈值](../references/process-optimization.md)。

## 示例路线

| 需要 | 从这里开始 |
|---|---|
| 项目导航 | [example-code-map](../templates/example-code-map/SKILL.md) |
| 功能交付 | [example-workflow](../templates/example-workflow/SKILL.md) |
| Bug 定位 | [example-bug-investigation](../templates/example-bug-investigation/SKILL.md) |
| API 变更 | [example-api-contract](../templates/example-api-contract/SKILL.md) |
| 数据变更 | [example-data-migration](../templates/example-data-migration/SKILL.md) |
| 发布与回滚 | [example-release-runbook](../templates/example-release-runbook/SKILL.md) |
| 迭代记录与结案 | [example-iteration-management](../templates/example-iteration-management/SKILL.md) |
| 知识提炼 | [example-knowledge-capture](../templates/example-knowledge-capture/SKILL.md) |
