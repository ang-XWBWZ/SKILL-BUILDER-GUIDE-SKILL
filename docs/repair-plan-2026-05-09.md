# v3.0 完整性修复方案

> 基于 tengxunCVM 真实项目生成测试 + 两次独立 worktree 评估 + 用户 7 项诊断。
> 日期：2026-05-09

---

## 一、问题诊断

tengxunCVM 生成测试暴露了 7 个问题，收敛为 3 个根因：

| # | 问题 | 根因 |
|---|------|------|
| 1 | Haiku L0 分级策略被严重忽略 — Agent 不实际委托 | A |
| 2 | 变更报告在修改完成后不产出 — 用户变更没有归档 | A |
| 3 | 不主动识别可复用流程制作脚本 — 重复劳动不消除 | A |
| 4 | Plan Tree 与管线/分治/委托分裂为四个独立概念 — 没有统一模型 | C |
| 5 | 指南专属化生成时丢失方法论内容 — 渐进式加载、已有规范被忽略 | B |
| 6 | 深度复核能力未集成 — 用户不能选择"审查已生成的技能" | C |
| 7 | 渐进式加载未在生成技能中体现 — functional 层技能缺少 references/ | B |

**根因定义**：

| 根因 | 含义 |
|------|------|
| **A — 声明没有执行机制** | 方法论写了"应该做"，但管线没有在 Gate 处强制检查"做了没有" |
| **B — GENERATE 缺少完整性清单** | 6→8 条硬规则只覆盖格式和规范，不覆盖方法论自身概念的传递验证 |
| **C — 概念分散没有统一模型** | 五阶段管线、H-ADMC、Plan Tree、委托模式、渐进式加载是同一件事的不同视角，但被写成独立章节 |

---

## 二、统一模型：执行树

### 2.1 概念

当前项目有 5 个独立概念：

| 概念 | 当前章节 | 实际含义 |
|------|------|------|
| 五阶段管线 | SKILL.md §2 | 做什么，按什么顺序 |
| H-ADMC | references/delegation.md §III | 什么时候拆解任务 |
| Plan Tree | docs/design/plan-tree.md (v0.1) | 拆解后长什么样 |
| 委托模式 | references/delegation.md §V | 拆解后的节点怎么分配执行者 |
| 渐进式加载 | SKILL.md 开头声明 | 任务执行时加载什么文件 |

**它们是同一件事**：一个任务 → 判断是否拆解（H-ADMC）→ 拆成树（Plan Tree）→ 每个节点分配执行者（委托模式）→ 每层只加载需要的文件（渐进式加载）→ 按阶段执行（五阶段管线）。

统一后的概念——**执行树**：

```
执行树 = {
  管线：定义了树的生命周期（ANALYZE 建树 → SCAN 填充 → GENERATE 产出 → VALIDATE 验证 → CONFIRM 关闭）
  拆解：定义了树的展开规则（6 条 H-ADMC 标准 → AND/OR/LEAF 节点）
  委托：定义了节点的执行分配（L0→Haiku, L1→Sonnet, L2→Sonnet/Opus, L3→Opus）
  加载：定义了节点的上下文范围（L1 元数据 → L2 核心 body → L3 深度引用 → L4 脚本）
}
```

### 2.2 在 SKILL.md 中的体现

当前 §2（执行管线）保持为操作入口。在其中明确：**管线的每一步都是在操作这棵执行树**。

`references/delegation.md` 和 `docs/design/plan-tree.md` 的内容合并为 `references/execution-tree.md`——统一的深度参考。删除分散的独立概念文档。

### 2.3 改动清单

| 文件 | 操作 | 内容 |
|------|------|------|
| `SKILL.md` §2 | 修改 | 开篇增加执行树概念声明，每个 Phase 的 Gate 增加检查项 |
| `SKILL.md` §2.4 | 修改 | GENERATE 硬规则增加到 9 条，增加完整性检查清单 |
| `SKILL.md` §2 | 新增 | §2.8 深度复核（可选第 6 阶段） |
| `references/execution-tree.md` | **新建** | 合并 delegation.md 的拆解/委托内容 + plan-tree.md 的树结构内容 |
| `references/delegation.md` | 删除 | 内容已合并到 execution-tree.md |
| `docs/design/plan-tree.md` | 删除 | 内容已合并到 execution-tree.md |
| `references/change-model.md` | 修改 | 增加"变更报告触发时机"说明（隐式触发 + 显式触发） |
| `SKILL.md` §1.3 | 修改 | 技能类型目录增加 change-model 的隐式触发说明 |
| `scripts/validate-skills.py` | 修改 | 增加 `--semantic` 模式（V3） |
| `scripts/check-skill-health.py` | 修改 | 增加 token 预算硬阻止 |

---

## 三、根因 A 修复：声明 → 执行机制

### 3.1 每个 Phase 增加 Gate 检查项

当前 Gate 只有"用户确认"一个条件。修复后每个 Phase 增加检查项：

| Phase | 当前 Gate | 新增 Gate 检查项 |
|------|------|------|
| ANALYZE | 用户确认技能计划 | 无（本阶段不涉及委托） |
| SCAN | 所有层扫描完毕 | ☐ SCAN 子任务已派 Haiku 执行？☐ 已有项目规范/文档已检测？☐ 可复用脚本/流程已识别？ |
| GENERATE | 8 条硬规则通过 | ☐ 完整性检查清单全部 ✅？☐ functional 层技能已创建 references/？☐ 变更报告模板已包含？（如是 change-model 类型） |
| VALIDATE | V1+V2 通过 | ☐ V3 语义验证通过（如可用）？☐ 交叉引用无断链？ |
| CONFIRM | 用户批准 | ☐ 本次修改的变更报告已产出？☐ 如有可复用流程，已归档为脚本/模板？ |

### 3.2 变更报告隐式触发

在 `SKILL.md` 和 `references/change-model.md` 中增加：

> 当 Agent 完成对项目的任何修改（代码变更、技能生成、配置更新），在 CONFIRM 阶段自动询问用户是否生成变更报告。不等待用户主动说"生成变更报告"。

在 `references/change-model.md` 开头增加触发条件：

```markdown
> **Load when**: (explicit) generating change reports, archiving change records
> **Also load when**: (implicit) Agent has completed a modification to the project
> and is entering the CONFIRM phase of any pipeline execution.
```

### 3.3 工具复用识别

在 `SKILL.md` §2.3（SCAN）增加扫描维度：

| 扫描维度 | 记录内容 | 用途 |
|------|------|------|
| 可复用流程 | 项目中重复执行的操作序列（部署、构建、数据迁移、测试套件运行） | 生成 scripts/ 或 workflow 技能的自动化步骤 |
| 已有脚本 | 项目中已存在的 bash/python 脚本 | 注册到 code-map，评估是否可泛化为模板 |

---

## 四、根因 B 修复：GENERATE 完整性清单

### 4.1 第 9 条硬规则

```markdown
9. Completeness checklist: before delivering generated skills, verify:
   ☐ Progressive loading: functional-tier skills have references/ if body >3000t
   ☐ Model delegation: L0 skills marked "must delegate to Haiku", L1 skills note L0 delegation points
   ☐ Naming disambiguation: risk levels use R0-R3 (not L0-L3), execution tiers use L0-L3
   ☐ Existing conventions: project's existing docs/changelogs/workflows are either incorporated or explicitly replaced
   ☐ Cross-references: all relative paths resolve to existing files
   ☐ Trigger words: 5-15, project-specific (no generic terms like "develop" or "modify")
   ☐ No placeholders: every {placeholder} replaced with actual content from scan
   ☐ Token budget: each SKILL.md ≤5000t (enforced by check-skill-health.py)
```

### 4.2 同步更新 phase-3-generate.md

在 `references/pipeline/phase-3-generate.md` 的质量自检清单中同步这 8 项。

---

## 五、根因 C 修复：统一模型

### 5.1 文件操作

| 操作 | 文件 |
|------|------|
| **新建** | `references/execution-tree.md` |
| **删除** | `references/delegation.md`（内容合并） |
| **删除** | `docs/design/plan-tree.md`（内容合并） |
| **修改** | `SKILL.md` §2 — 管线作为执行树的生命周期 |
| **修改** | `SKILL.md` §7（原 L3 路由表）— 更新引用路径 |

### 5.2 execution-tree.md 内容大纲

```
# 执行树 — 统一任务分解与执行模型

## 1. 概念
执行树 = 管线(生命周期) + 拆解(展开规则) + 委托(执行分配) + 加载(上下文范围)

## 2. 树的构建（ANALYZE → SCAN → GENERATE）
## 3. 树的展开（H-ADMC 6 条标准 → AND/OR/LEAF/CONDITION 节点）
## 4. 节点的执行分配（委托模式 A/B/C）
## 5. 节点的上下文加载（L1→L2→L3→L4 渐进式）
## 6. 树的验证（VALIDATE）与关闭（CONFIRM）
## 7. 子树局部重规划（失败恢复）
```

### 5.3 深度复核集成（可选第 6 阶段）

在 `SKILL.md` §2 管线末尾增加：

```markdown
### 2.8 Deep Review (Optional Phase 6)

After CONFIRM, the user may request a deep review of generated skills.
This spawns an independent agent in a clean context (worktree isolation)
that evaluates: practical value, over-design, logical conflicts, development
guidance, engineering stability. See docs/evaluation-report-*.md for rubric.

Trigger: user says "review the generated skills" or "evaluate the skill system".
```

---

## 六、文件改动汇总

| 文件 | 操作 | 涉及的根因 |
|------|------|:--:|
| `SKILL.md` §2 开篇 | 增加执行树概念声明 | C |
| `SKILL.md` §2.2-2.6 | 每个 Phase 增加 Gate 检查项 | A |
| `SKILL.md` §2.3 | SCAN 增加"可复用流程"和"已有规范"扫描维度 | A |
| `SKILL.md` §2.4 | GENERATE 硬规则 8→9 条，增加完整性清单 | B |
| `SKILL.md` §2.7 | L3 路由表更新引用（delegation.md → execution-tree.md） | C |
| `SKILL.md` §2.8 | 新增"深度复核"可选第 6 阶段 | C |
| `SKILL.md` §1.3 | 技能类型目录增加 change-model 隐式触发说明 | A |
| `references/execution-tree.md` | **新建**，合并 delegation + plan-tree | C |
| `references/delegation.md` | **删除**，内容合并 | C |
| `docs/design/plan-tree.md` | **删除**，内容合并 | C |
| `references/change-model.md` | 增加隐式触发条件 | A |
| `references/pipeline/phase-3-generate.md` | 质量自检清单同步 9 项完整性检查 | B |
| `scripts/validate-skills.py` | 增加 `--semantic` 模式 | B |
| `scripts/check-skill-health.py` | Token 预算超限从 warn 改为 fail | B |

---

## 七、执行后的验证标准

修复完成后，用 tengxunCVM 重新生成技能，验证：

| 检查项 | 标准 |
|------|------|
| 每个 functional 技能有 `references/` 目录 | 必须 |
| 生成的 change-model 中风险等级使用 R0-R3 | 必须 |
| L0 技能 body 标注"must delegate to Haiku" | 必须 |
| 生成过程中 Phase 2 检测到 `openclaw-change-log/` | 必须 |
| 生成后 CONFIRM 阶段提示"是否生成变更报告？" | 必须 |
| validate-skills.py `--semantic` 模式可用 | 必须 |
| execution-tree.md 替代 delegation.md 引用，SKILL.md 中无断链 | 必须 |
