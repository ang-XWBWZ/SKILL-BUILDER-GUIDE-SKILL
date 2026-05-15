# v3.1 三层激活架构迭代方案

> 基于两个参考实现（Karpathy Skills / Matt Pocock Skills）的融合分析，解决 Skill Builder 激活率问题。
> 日期：2026-05-15

---

## 一、问题诊断

Skill Builder v3.0 管线严谨但激活率低。四个根因：

| # | 问题 | 根因 |
|---|------|------|
| 1 | 用户不知道何时调哪个技能，调了也不对 | **召唤门槛高** — trigger 列表在 openai.yaml 里，但 description 太抽象，Agent 难以精确匹配 |
| 2 | 五阶段管线全跑一遍才能产出，用户等不住 | **冷启动成本高** — 无快速路径，小需求也得走完整 ANALYZE→CONFIRM |
| 3 | 各技能孤立触发，产出碎片化，用户看不到持续价值 | **技能无协作** — 无链式 handoff，技能间不互相推荐 |
| 4 | 生成的技能用通用术语说话，不融入项目语境 | **无环境感知** — 缺领域词汇表，产出像模板不像项目专属 |

两个参考实现的解法：

| 问题 | Karpathy 解了? | Pocock 解了? |
|------|:---:|:---:|
| 召唤门槛 | — | ✅ "Use when..." 句式 |
| 冷启动 | — | — |
| 技能协作 | — | ✅ Skill Chain + Handoff |
| 环境感知 | ✅ 行为准则 always-on | ✅ CONTEXT.md 词汇表 |

---

## 二、融合方案：三层激活架构

```
┌──────────────────────────────────────────────────────┐
│  L0: 环境层 (always-on, 零召唤, 激活率 100%)          │
│  CLAUDE.md 行为宪法 + 领域词汇表                       │
├──────────────────────────────────────────────────────┤
│  L1: 协作层 (链式触发, 一次入口, 激活率 ≥60%)          │
│  Skill Chain + Handoff 段 + setup 初始化技能           │
├──────────────────────────────────────────────────────┤
│  L2: 专业层 (按需召唤, 渐进加载, 激活率 ≥30%)          │
│  五阶段管线 + 模板 + 验证 + 快速路径                    │
└──────────────────────────────────────────────────────┘
```

### L0 从 Karpathy 借什么

Karpathy 核心洞察：**最好的技能是不需要召唤的技能**。4 条行为原则写在 CLAUDE.md 里，每次会话自动加载。

1. **行为宪法具体化** — 当前 CLAUDE.md Section B 是占位符（"propose→review, discover→report..."），需要落地为可判别准则
2. **Karpathy 的 4 条原则纳入** — Think Before Coding / Simplicity First / Surgical Changes / Goal-Driven Execution — 这些是 LLM 通用缺陷矫正，所有项目都需要

### L0 从 Pocock 借什么

1. **CONTEXT.md 领域词汇表** — 让技能用项目自己的语言说话，避免通用废话
2. **ADR 集成** — 架构决策记录与技能联动，避免重复建议已否决的方案

### L1 从 Pocock 借什么

1. **Skill Chain 定义** — 技能完成后自动推荐下一个，一次入口链式激活
2. **Handoff 段** — 每个技能 SKILL.md 末尾的 `## Handoff` 段，声明完成后的推荐
3. **setup 初始化技能** — 首次使用时扫描项目、交互式配置，降低冷启动门槛
4. **"Use when..." 触发句式** — 替代当前 openai.yaml 里的抽象 trigger 列表

### L2 保留 Skill Builder 原有 + 增加快速路径

1. **快速路径 (PICK→FILL→DONE)** — 与完整管线并行，3 步 ≤5 分钟出结果
2. **完整管线保留** — 新项目/复杂项目仍然走 ANALYZE→CONFIRM

---

## 三、变更清单

### 3.1 文件变更总览

| # | 文件 | 变更类型 | 层 | 依赖 |
|---|------|---------|----|------|
| C1 | `SKILL.md` | 修改 | L0+L1+L2 | — |
| C2 | `agents/openai.yaml` | 修改 | L1 | C1 |
| C3 | `CLAUDE.md` | 修改 | L0 | C1 |
| C4 | `templates/skill-template.md` | 修改 | L1 | C1 |
| C5 | `templates/openai-template.yaml` | 修改 | L1 | C2 |
| C6 | 新增 `references/skill-chain.md` | 新增 | L1 | C1 |
| C7 | 新增 `references/context-vocabulary.md` | 新增 | L0 | C1 |
| C8 | 6 个 template SKILL.md | 修改 | L1 | C4+C6 |
| C9 | `references/claude-md-spec.md` | 修改 | L0 | C3+C7 |
| C10 | `references/pipeline/phase-3-generate.md` | 修改 | L2 | C1 |
| C11 | `scripts/validate-skills.py` | 修改 | L2 | C1 |

---

### C1: SKILL.md — 核心方法论变更

**变更 1: §1.3 Skill Type Catalog — 增加 Handoff 列**

每个技能类型表格增加一列 `Handoff`，声明完成后推荐哪些技能：

```markdown
| Skill Type | Execution | Composition | Required Sections | Handoff | Template |
|---------|:--:|:--:|------|---------|------|
| Standards (dev) | L1 | atomic | Tech stack, layered arch, code standards | → code-map (new files ≥3) | `templates/example-dev/` |
| Code Map (code-map) | L0 | atomic | Dir structure, quick lookup, routes | → dev (non-standard structure) | `templates/example-code-map/` |
| Workflow (workflow) | L1 | functional | Phase→input→steps→output, checklists | → change-model (changes ≥2 modules) | `templates/example-workflow/` |
| Change Model (change-model) | L1 | functional | WHY/WHAT/HOW/VALIDATION, call-chain check | → call-chain (changes ≥3 layers) | `references/change-model.md` |
| Call-Chain (call-chain) | L1 | functional | Tracing method, type checking, final-call checklist | → change-model (new change) | `templates/example-call-chain/` |
| Scripts (scripts) | L0 | atomic | Script inventory, execution flow, error handling | — | — |
| Delegation (delegation) | L1 | planning | Decomposition criteria, model routing | → any (as needed) | `references/delegation.md` |
```

**变更 2: §1.4 后新增 §1.5 Skill Chains**

```markdown
### 1.5 Skill Chains

技能不应孤立触发。完成一个技能后，根据产出特征推荐下一个。

| 入口技能 | 完成后推荐 | 触发条件 |
|---------|-----------|---------|
| dev | code-map | 新建文件 ≥3 |
| code-map | dev | 发现非标准目录结构 |
| workflow | change-model | 变更涉及 ≥2 模块 |
| change-model | call-chain | 变更跨 ≥3 层级 (API→Service→Data→DB) |
| call-chain | change-model | 发现新的变更需求 |
| diagnose | change-model | bug 修复已确认，需归档 |
| triage | grill-with-docs | 需求描述模糊，需澄清 |

**实现**: 每个生成的 SKILL.md 末尾包含 `## Handoff` 段 (见 C4)。
```

**变更 3: §2.1 Pipeline Overview — 增加快速路径**

在现有管线表格后新增：

```markdown
### Quick Path (3 步, ≤5 min)

适用场景：已有项目补充技能、小项目快速配置、用户不想走完整管线。

| Step | Executor | Input | Output |
|------|:------:|------|------|
| PICK | Sonnet (L1) | 项目概述 | 从预设组合选择技能套餐 |
| FILL | Haiku (L0) | 套餐 + 关键配置文件 | 提取 tech stack / dir structure / entry points |
| DONE | Sonnet (L1) | FILL 结果 | 用模板填充生成，跳过 VALIDATE 直接交付 |

**预设套餐** (复用 §1.4 表格):
- S: standards + workflow
- M: + code-map
- L: + change-model
- XL: + call-chain + delegation

**Gate**: DONE 后提示用户 "补跑 VALIDATE 以验证准确性？"

**完整路径 vs 快速路径选择**:

| 条件 | 路径 |
|------|------|
| 新项目 / 首次生成 ≥4 技能 | 完整管线 |
| 已有项目补充 1-2 技能 | 快速路径 |
| 用户明确说"快速"/"简单" | 快速路径 |
| 用户明确说"完整"/"严格" | 完整管线 |
| 不确定 | 默认快速路径，完成后提示可补完整管线 |
```

**变更 4: §2.4 GENERATE — 增加 Handoff 段生成规则**

在 10 条硬规则后追加第 11 条：

```markdown
11. **Handoff 段**: 每个生成的 SKILL.md 末尾必须包含 `## Handoff` 段，声明完成后推荐哪些技能及触发条件。推荐来源：§1.5 Skill Chains 表格，根据技能类型选取对应行。
```

同步更新 §2.4.1 Completeness Checklist，追加：

```markdown
- [ ] **Handoff 段**: 每个生成的 SKILL.md 包含 `## Handoff` 段，且推荐技能与 §1.5 一致
```

---

### C2: agents/openai.yaml — 触发词优化

**变更**: 在每个 trigger 后补 "Use when..." 上下文，提升 Agent 匹配精度。

当前格式（抽象）：
```yaml
triggers:
  - create skill
  - skill system
  - skill template
```

改为（Pocock 模式，description 内含触发语义）：

```yaml
interface:
  display_name: "L1 — Skill Builder"
  short_description: "L1 — AI Agent Skills creation methodology and pipeline. Use when creating project-specific skills, generating SKILL.md files, setting up skill systems, understanding model tier delegation, or validating skill accuracy."
  default_prompt: "Use skill-builder to create or validate project-specific AI Agent skills"
policy:
  allow_implicit_invocation: false
triggers:
  - create skill
  - skill system
  - skill template
  - skill creation
  - generate project skill
  - model tier
  - L0 delegation
  - skill validation
  - frontmatter spec
  - openai.yaml
  - Plan Tree
  - task decomposition
  - skill builder
  - validate skill
  - skill directory
  - quick skill
  - setup skills
```

关键变更：
1. `short_description` 加 "Use when..." 句式（Pocock 模式）
2. 新增 `quick skill` / `setup skills` 两个触发词（对应快速路径和 setup 技能）

---

### C3: CLAUDE.md — 行为宪法落地

当前 Section B 是占位符。需改为具体可判别的行为准则。

**变更**: 重写 CLAUDE.md 的行为准则部分，融合 Karpathy 4 原则：

```markdown
## Behavioral Constitution

These rules apply to every session, every skill, every change. No exceptions for "trivial" tasks.

1. **Think Before Coding** — State assumptions explicitly. If uncertain, ask. If multiple interpretations exist, present them. If something is unclear, stop and name what's confusing.
2. **Simplicity First** — Minimum code that solves the problem. No speculative features, no abstractions for single-use code, no error handling for impossible scenarios.
3. **Surgical Changes** — Touch only what you must. Match existing style. Remove only orphans your changes created. Every changed line traces to the user's request.
4. **Goal-Driven Execution** — Transform tasks into verifiable goals. "Fix the bug" → "Write a test that reproduces it, then make it pass." For multi-step tasks, state plan with verify checkpoints.
5. **L0 Delegation** — File ops, lookups, script exec → Haiku. Main model executing L0 = 5-15x token waste.
6. **Discover → Report** — Found something unexpected? Report it. Don't silently skip or work around.
7. **Change → Test** — Changed code? Verify it. No naked modifications.
8. **Complete → Archive** — Work done? Offer a change report. Don't leave dangling context.
```

注意：规则 1-4 来自 Karpathy（LLM 通用缺陷矫正），5-8 来自 Skill Builder 自身（项目特定行为）。

---

### C4: templates/skill-template.md — 增加 Handoff 段

在模板末尾（`## Reference` 或最后一节之后）新增：

```markdown
## Handoff

After completing this skill, recommend the next skill based on output characteristics:

| Condition | Recommend |
|-----------|-----------|
| {condition_1} | `{project}-{skill_name}` |
| {condition_2} | `{project}-{skill_name}` |
```

生成时由 GENERATE 阶段根据 §1.5 Skill Chains 表格填充具体条件。

---

### C5: templates/openai-template.yaml — 触发描述模板

在模板的 `interface.short_description` 中加入 "Use when..." 模板句式：

```yaml
interface:
  display_name: "{model_tier} — {skill_name}"
  short_description: "{model_tier} — {one-line description}. Use when {specific trigger scenarios}."
  default_prompt: "Use {skill-name} to {primary action}"
```

这是 Pocock 的核心触发优化：description 是 Agent 决定加载哪个技能的唯一信息源，必须包含足够的具体触发上下文。

---

### C6: 新增 references/skill-chain.md

Skill Chain 的完整方法论参考（L3 渐进加载）。

```markdown
---
name: skill-chain
description: Skill Chain methodology — defining handoff relationships between skills for chain activation.
model_tier: L3
skill_tier: meta
version: 1.0.0
status: active
---

# Skill Chain Methodology

## Core Principle

技能不应孤立触发。一个技能完成后的产出，是下一个技能的天然入口。链式激活 > 独立召唤。

## Handoff Definition

每个 SKILL.md 末尾的 `## Handoff` 段定义：

```markdown
## Handoff

After completing this skill, recommend the next skill based on output characteristics:

| Condition | Recommend |
|-----------|-----------|
| {measurable condition} | `{skill-name}` |
```

### Handoff 规则

1. **条件必须可判别** — 不能写"如果需要"，要写"新建文件 ≥3"
2. **推荐必须具体** — 写 `{project}-code-map`，不写"code-map 类技能"
3. **最多 3 条推荐** — 超过 3 条说明技能职责不清，应拆分
4. **避免循环** — A→B→A 允许（不同场景返回），A→B→C→A 禁止
5. **推荐时说明原因** — "因为本次变更涉及 3 个模块，建议运行 change-model 归档变更"

## Chain Patterns

### Pattern A: Sequential (顺序链)

```
dev → code-map → workflow → change-model → call-chain
```

适用：新项目首次配置，按依赖顺序逐一生成。

### Pattern B: Hub-and-Spoke (枢纽链)

```
         ┌→ code-map
dev ─────┤
         └→ workflow → change-model
```

适用：dev 是枢纽，根据产出特征选择分支。

### Pattern C: Feedback Loop (反馈链)

```
change-model → call-chain → (发现新问题) → change-model
```

适用：验证阶段发现新问题，回到分析阶段。

## Interaction with Pipeline

- **完整管线**: Skill Chain 在 GENERATE 阶段自动写入 Handoff 段
- **快速路径**: PICK 阶段选择的套餐已隐含链式关系，FILL 时补入
- **VALIDATE**: V2 检查 Handoff 推荐的技能是否存在

## Metrics

| 指标 | 目标 | 衡量方式 |
|------|------|---------|
| 链式激活率 | ≥60% | 技能 A 完成后，推荐的技能 B 被执行的比例 |
| 孤立激活率 | ≤30% | 技能被直接调用但未触发链的比例 |
| 链式完成率 | ≥80% | 链式激活后，后续技能成功完成的比例 |
```

---

### C7: 新增 references/context-vocabulary.md

领域词汇表方法论（Pocock 的 CONTEXT.md 模式）。

```markdown
---
name: context-vocabulary
description: Domain vocabulary methodology — building and maintaining project-specific term glossaries for skill output quality.
model_tier: L3
skill_tier: meta
version: 1.0.0
status: active
---

# Domain Vocabulary Methodology

## Core Principle

技能用项目自己的语言说话，不用通用术语。生成的代码、文档、报告中的术语必须与项目现有术语一致。

这是 Pocock 的 CONTEXT.md 模式，核心价值：
1. **减少 Agent 冗余** — 用 1 个精确词替代 20 字解释
2. **命名一致** — 变量、函数、文件名用统一术语
3. **代码可导航** — Agent 用项目术语搜索代码更准确
4. **Token 节省** — 精确术语比模糊描述消耗更少 token

## Vocabulary Table Format

```markdown
| Term | Meaning | Avoid |
|------|---------|-------|
| {canonical} | {precise definition} | {ambiguous synonyms to avoid} |
```

### Rules

1. **Term 列**: 项目中实际使用的词，不是通用词。如用 "Order" 不用 "request"
2. **Meaning 列**: 一句话定义，不含实现细节
3. **Avoid 列**: 列出容易混淆的近义词，防止 Agent 使用项目外的替代词

## Placement Options

| 位置 | 适用场景 | 加载方式 |
|------|---------|---------|
| CLAUDE.md Section M5 | 术语 ≤15 个 | always-on |
| `CONTEXT.md` (项目根) | 术语 15-50 个 | Agent 按需读取 |
| `CONTEXT-MAP.md` (项目根) | 多模块/多上下文 | Agent 按模块读取 |

## Integration with Skill Builder Pipeline

### ANALYZE Phase
- 扫描项目 README / CONTRIBUTING / docs/ / 代码注释中的关键术语
- 提取项目特有的领域概念
- 产出: 术语候选列表

### SCAN Phase
- 验证术语候选在代码中的使用情况
- 识别术语不一致（同一概念多种叫法）
- 产出: Vocabulary Table 初稿

### GENERATE Phase
- 将 Vocabulary Table 写入 CLAUDE.md M5 或 CONTEXT.md
- 所有生成的 SKILL.md 使用 Vocabulary Table 中的术语
- Handoff 段中的条件描述使用项目术语

### VALIDATE Phase
- V3 semantic: 检查生成文件中的术语是否与 Vocabulary Table 一致
- 术语不一致 → FAIL

## Vocabulary Maintenance

- **新增术语**: 发现新概念时立即添加，不批量
- **冲突处理**: 用户使用的术语 > 代码中的术语 > 通用术语
- **删除术语**: 项目不再使用的概念标记 deprecated，不立即删除
- **ADR 联动**: 重大术语变更应记录 ADR
```

---

### C8: 6 个 template SKILL.md — 增加 Handoff 段

每个模板的 SKILL.md 末尾追加 `## Handoff` 段，内容根据 §1.5 Skill Chains：

| 模板 | Handoff 内容 |
|------|-------------|
| example-dev | new files ≥3 → `{project}-code-map`; non-standard structure found → `{project}-workflow` |
| example-code-map | → `{project}-dev` (conventions lookup) |
| example-workflow | changes ≥2 modules → `{project}-change-model` |
| example-call-chain | new change found → `{project}-change-model` |
| example-delegation | → any skill as needed |
| change-model-template | changes ≥3 layers → `{project}-call-chain` |

---

### C9: references/claude-md-spec.md — 行为宪法 + 词汇表

**变更 1**: Section B (Behavioral Constitution) 的定义改为 C3 中的 8 条具体准则。

**变更 2**: Module M5 (Domain Glossary) 的生成规则改为引用 `references/context-vocabulary.md` 方法论，数据源从 SCAN 提取。

**变更 3**: 新增模块 M5.1 触发条件调整：

当前: `≥5 project-specific terms trigger`
改为: `所有项目都生成 M5，术语 0-5 个时标记 "基础词汇，需补充"；≥5 个时标记 "核心词汇"`

理由：词汇表对所有项目都有价值，不应设置高门槛。Karpathy 证明 even 4 条规则都有用。

---

### C10: references/pipeline/phase-3-generate.md — 快速路径 + Handoff

**变更 1**: 新增 Quick Path 的 GENERATE 规则：

```markdown
### Quick Path GENERATE

1. 根据用户选择的套餐 (S/M/L/XL) 选取对应模板
2. FILL 阶段提取的数据填入模板占位符
3. 不做深度逐层扫描，只填充关键数据点:
   - tech stack: 从 package.json / pom.xml / go.mod / requirements.txt
   - dir structure: 顶层 3 级目录
   - entry points: main 文件 / 路由文件
4. Handoff 段根据套餐自动填充 (见 references/skill-chain.md)
5. 交付时提示: "已跳过 VALIDATE，建议补跑 `python scripts/validate-skills.py .claude/skills/{name} --semantic`"
```

**变更 2**: 完整管线的 GENERATE 阶段追加 Handoff 段生成指令。

---

### C11: scripts/validate-skills.py — Handoff 验证

**变更**: V2 验证增加 Handoff 段检查：

```python
# 在 validate_skill() 中追加:

# 4. 检查 Handoff 段 (V2+)
skill_md_path = os.path.join(skill_dir, "SKILL.md")
if os.path.exists(skill_md_path):
    with open(skill_md_path, "r", encoding="utf-8") as f:
        content = f.read()
    body = content.split("---", 2)[2] if content.startswith("---") else content

    if "## Handoff" not in body:
        warnings.append("SKILL.md: 缺少 ## Handoff 段 — 建议添加以支持链式激活")
    else:
        # 检查 Handoff 中引用的技能是否存在
        handoff_section = body.split("## Handoff")[1].split("##")[0]
        referenced_skills = re.findall(r'`(\w+-\w+)`', handoff_section)
        for ref in referenced_skills:
            # 在同目录的兄弟技能中查找
            parent_dir = os.path.dirname(skill_dir)
            ref_path = os.path.join(parent_dir, ref)
            if not os.path.exists(ref_path):
                warnings.append(f"Handoff: 引用的技能 `{ref}` 在同目录下不存在")
```

---

## 四、实现顺序

```
Phase 1: L0 环境层 (C3, C7, C9)  ← 不依赖其他变更，可独立交付
    │
    ├─ C3: CLAUDE.md 行为宪法落地
    ├─ C7: references/context-vocabulary.md 新增
    └─ C9: references/claude-md-spec.md 对齐

Phase 2: L1 协作层 (C6, C4, C5, C8, C2)  ← 依赖 Phase 1 的方法论定义
    │
    ├─ C6: references/skill-chain.md 新增
    ├─ C4: templates/skill-template.md 增加 Handoff
    ├─ C5: templates/openai-template.yaml 触发描述
    ├─ C8: 6 个 template SKILL.md 增加 Handoff
    └─ C2: agents/openai.yaml 触发词优化

Phase 3: L2 专业层 (C1, C10, C11)  ← 依赖 Phase 1+2 的概念和模板
    │
    ├─ C1: SKILL.md 核心方法论变更
    ├─ C10: references/pipeline/phase-3-generate.md 快速路径
    └─ C11: scripts/validate-skills.py Handoff 验证
```

**每个 Phase 完成后跑一次**:

```bash
python scripts/validate-skills.py . --semantic
python scripts/check-skill-health.py .
```

---

## 五、验收标准

### L0 验收

- [ ] CLAUDE.md 行为宪法包含 8 条可判别准则（4 条 Karpathy + 4 条项目特定）
- [ ] 生成的技能输出使用项目术语（与 Vocabulary Table 一致）
- [ ] M5 Domain Glossory 对所有项目默认生成，不设高门槛

### L1 验收

- [ ] 所有 6 个模板 SKILL.md 包含 `## Handoff` 段
- [ ] openai.yaml 的 short_description 包含 "Use when..." 句式
- [ ] references/skill-chain.md 定义了 3 种 Chain Pattern
- [ ] validate-skills.py 对缺失 Handoff 段发出警告

### L2 验收

- [ ] SKILL.md §1.5 Skill Chains 表格完整
- [ ] 快速路径 (PICK→FILL→DONE) 定义完整，与完整管线并列
- [ ] §2.4 硬规则追加第 11 条 (Handoff)
- [ ] §2.4.1 Completeness Checklist 追加 Handoff 检查项
- [ ] phase-3-generate.md 包含快速路径 GENERATE 规则

### 激活率目标

| 层 | 目标 | 衡量 |
|----|------|------|
| L0 环境层 | 100% always-on | CLAUDE.md 存在即激活 |
| L1 协作层 | ≥60% 链式激活 | Handoff 推荐被执行的比例 |
| L2 专业层 | ≥30% 完整管线 | 用户主动走完整 ANALYZE→CONFIRM |

---

## 六、风险与缓解

| 风险 | 缓解 |
|------|------|
| Handoff 段增加模板长度，可能突破 5000t 上限 | Handoff 段控制在 200t 以内；超限时拆入 references/ |
| 快速路径产出质量低，用户不信任 | DONE 后强制提示补跑 VALIDATE；首次使用默认完整路径 |
| 行为宪法 8 条太多，Agent 记不住 | 前 4 条 (Karpathy) 是自然语言行为，不需要精确记忆；后 4 条是流程强制，由 Gate 检查 |
| 词汇表维护成本高 | 初始从 SCAN 自动提取；后续增量更新，不批量重写 |
| Skill Chain 循环依赖 (A→B→A) | Handoff 段限制最多 3 条推荐；validate 检查循环 |

---

## 七、与 v3.0 修复方案的关系

v3.0 修复了 7 个问题（3 个根因）。本次迭代不冲突，且直接加强根因 A 的解法：

| v3.0 根因 | v3.0 解法 | v3.1 加强 |
|-----------|----------|----------|
| A — 声明没有执行机制 | Gate 检查 | 行为宪法具体化 (L0) + Handoff 链式激活 (L1) |
| B — GENERATE 缺完整性清单 | 10→12 条硬规则 | 继续追加至 11 条 (Handoff) |
| C — 概念分散无统一模型 | 统一执行树 | 三层激活架构是执行树的用户侧投影 |
