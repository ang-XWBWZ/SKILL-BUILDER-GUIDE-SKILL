# Skill Builder — 跨 Agent 的项目专属 Skill 指南

这个仓库帮助团队把“项目事实、重复流程和风险边界”沉淀为可复用的项目级 skill，而不是绑定某个 Agent 或模型。

核心约定是：`AGENTS.md` 作为项目入口，`.agents/skills/` 作为唯一的可移植 skill 源。任何平台原生目录、UI 元数据或调用语法都只能作为显式适配层存在。

## 目标结构

```text
your-project/
├── AGENTS.md                    # 项目入口：约束、命令、skill 路由
└── .agents/
    ├── skills/                  # 跨 Agent 的 canonical skills
    │   └── project-capability/
    │       ├── SKILL.md
    │       ├── references/
    │       ├── scripts/
    │       └── assets/
    └── adapters/                # 可选：某个运行时的安装/元数据
```

`AGENTS.md` 采用跨平台常用的大写命名；它对应于需求中所说的 `agents.md`，可避免在大小写敏感文件系统上的歧义。

本仓库本身是一个可分发的构建器包，因此不把同一份核心内容再复制一份到根目录 `.agents/`；目标项目应从 [项目脚手架](templates/project-scaffold/) 获得该目录。根目录的 `agents/openai.yaml` 仅是当前宿主界面的可选展示元数据，不参与生成项目的规范或目录约定。

## 架构原则

| 层 | 放什么 | 不放什么 |
|---|---|---|
| `AGENTS.md` | 高优先级约束、可执行命令、skill 路由 | 完整操作流程、重复的领域知识 |
| `.agents/skills/` | 项目事实、可复用步骤、验收条件 | 平台绑定的模型名和命令语法 |
| `references/` | 按需加载的长文档、模式、示例 | 与主 skill 重复的内容 |
| `adapters/` | 特定运行时的安装或元数据 | 唯一业务规则来源 |

## 交付与流程优化顺序

流程优化建议永远排在直接单次需求、落地实现和必要文档之后。只要当前交付中出现 1 条可验证的摩擦信号，就可以提出 1 条可选建议；但没有用户或项目负责人明确授权时，不得借此修改流程、创建任务或新增 skill。详见[流程优化建议阈值](references/process-optimization.md)。

## 快速开始

前置条件：Python 3.10 或更高版本。若系统将该解释器命名为 `python3`，请将下列命令中的 `python` 替换为 `python3`。

1. 复制 [项目脚手架](templates/project-scaffold/) 到目标项目。
2. 根据 [决策指南](references/decision-guide.md) 选择最少的一组 skill。
3. 扫描真实项目文件，填入命令、路径、约束和验证方式。
4. 用 [通用 skill 骨架](templates/skill-template.md) 创建 `.agents/skills/{project}-{capability}/SKILL.md`。
5. 运行校验：

```bash
python scripts/validate-skills.py .agents/skills --project-root .
python scripts/check-skill-health.py .agents/skills
```

模板库可用以下命令检查（模板保留占位符是正常的）：

```bash
python scripts/validate-skills.py templates --allow-placeholders
```

## 内容导航

- [核心工作流](SKILL.md)
- [AGENTS.md 规范](references/agents-md-spec.md)
- [平台适配契约](references/adapter-contract.md)
- [流程优化建议阈值](references/process-optimization.md)
- [领域专用指南](references/scenarios/)
- [通用样例库](templates/README.md)
- [5 分钟上手](docs/quick-start.md)

## 验证范围

校验器验证目录结构、frontmatter、命名、相对链接和未替换占位符。它不会替代对真实项目路径、版本、接口或命令的人工/工具核验；这些事实必须来自目标项目本身。

## License

MIT
