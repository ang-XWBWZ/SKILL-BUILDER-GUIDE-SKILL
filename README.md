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

## 先咨询，再构建

每次初始或再次激发构建器，都先确认用户此刻要做什么：初始化、评估、修复、扩展、迁移、校验还是仅制定计划。用户未明确时，必须先提问；再次激发时默认保留已有 skill，不因重复触发直接生成或覆盖。还要确认既有 `AGENTS.md` 的处理方式、是否有可用知识库、交付记录与知识提炼是否进入该库，以及没有知识库时的文档存放位置。详见[咨询协议](references/consultation-protocol.md)。

## 交付与流程优化顺序

流程优化建议永远排在直接单次需求、落地实现和必要文档之后。只要当前交付中出现 1 条可验证的摩擦信号，就可以提出 1 条可选建议；但没有用户或项目负责人明确授权时，不得借此修改流程、创建任务或新增 skill。详见[流程优化建议阈值](references/process-optimization.md)。

## 可追溯交付

当项目反复需要对功能、缺陷修复、跨模块变更或高风险操作保留从范围到结案的证据时，可创建迭代管理 skill。版本控制保存精确代码和配置差异；迭代记录保存日期、工作项、验收、验证与结案，并链接对应 revision 或 diff；可复用知识则独立存入已确认的知识区。项目自行定义记录目录、编号、审批、留存和负责人字段。详见[可追溯交付指南](references/iteration-management.md)、[知识管理指南](references/knowledge-management.md)和[通用交付记录模板](templates/iteration-record-template.md)。

## 快速开始

前置条件：Python 3.10 或更高版本。若系统将该解释器命名为 `python3`，请将下列命令中的 `python` 替换为 `python3`。

1. 通过[咨询协议](references/consultation-protocol.md)确认当前操作、目标范围和完善程度。
2. 复制 [项目脚手架](templates/project-scaffold/) 到目标项目。
3. 根据 [决策指南](references/decision-guide.md) 选择最少的一组 skill。
4. 扫描真实项目文件，填入命令、路径、约束和验证方式。
5. 用 [通用 skill 骨架](templates/skill-template.md) 创建 `.agents/skills/{project}-{capability}/SKILL.md`。
6. 基于真实项目证据审查：

```bash
python scripts/check-markdown-links.py .
```

链接检查只发现本地 Markdown 链接问题；它不证明 skill 会被正确激发、理解用户意图或完成工作。结合目标项目的路径、命令、接口与实际输出审查每一条关键指令；详见[证据审查指南](references/evidence-review.md)。

## 内容导航

- [核心工作流](SKILL.md)
- [咨询协议](references/consultation-protocol.md)
- [证据审查指南](references/evidence-review.md)
- [知识管理指南](references/knowledge-management.md)
- [AGENTS.md 规范](references/agents-md-spec.md)
- [平台适配契约](references/adapter-contract.md)
- [可追溯交付指南](references/iteration-management.md)
- [流程优化建议阈值](references/process-optimization.md)
- [领域专用指南](references/scenarios/)
- [通用样例库](templates/README.md)
- [5 分钟上手](docs/quick-start.md)

## 审查边界

不以固定目录、章节或脚本通过作为 skill 质量的判据。应以当前用户目标、真实项目路径、版本、接口、命令和实际交付证据审查技能；未能确认的内容必须保留为不确定性。

## License

MIT
