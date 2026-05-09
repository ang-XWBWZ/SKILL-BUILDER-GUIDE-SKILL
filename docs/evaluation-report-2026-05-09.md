# SKILL-BUILDER-GUIDE v3.0 评估报告

> 基于真实项目 `tengxunCVM` 的全流程生成测试 + 两次独立 worktree 评估。
> 日期：2026-05-09

---

## 一、测试过程

在 `D:\demo\tengxunCVM`（Spring Boot 2.7 + Vue 3.4 + SM2/SM4 国密加密链，全栈生产项目）上，严格按 SKILL.md §2 五阶段管线执行：

| 阶段 | 执行情况 | 输出 |
|------|:--:|------|
| ANALYZE | 分析项目类型/技术栈/模块结构 → 匹配 §1.4 选择矩阵 | 4 技能计划（dev + code-map + workflow + change-model） |
| SCAN | 深度扫描 6 层 50+ 文件，记录具体方法签名/版本号/类名 | 每层代码样本 |
| GENERATE | 按 8 条硬规则生成，加载对应 L3 reference | 4 个 SKILL.md + 4 个 openai.yaml |
| VALIDATE | validate-skills.py 通过 | 4/4 V1+V2 通过 |
| CONFIRM | 用户审查 | 发现 3 个方法论缺口，已修复进 GENERATE 规则 |

## 二、产出质量

### 2.1 独立评估结果（worktree 隔离，零上下文）

| 维度 | 评级 | 关键发现 |
|------|:--:|------|
| 实用价值 | **强** | 版本号 100% 准确（与 pom.xml/package.json 逐项核对），加密链文档项目独有且不可替代 |
| 过度设计 | **低** | SM2/SM4/SM3 加密链 + 14 依赖注入 + 双云 API 的复杂度值得 4 个技能 |
| 逻辑冲突 | **可接受** | 1 个问题：生成的 `docs/changes/` 路径不存在，忽略了已有 `openclaw-change-log/` |
| 开发指导性 | **强** | 可逐步骤完成"新增 API 端点"，覆盖 8 个具体步骤含精确文件路径和方法签名 |
| 工程稳定性 | **可接受** | 代码地图随文件增删需更新，其余技能稳定 |

### 2.2 意外发现：生成的技能比项目自身 README 更准确

| 错误 | 项目 README | 生成技能（扫描源码后） |
|------|------|------|
| API 方法 | GET | POST（`CvmApiController.java` 证实） |
| SDK 版本 | 3.1.1290 | 3.1.1443（`pom.xml` 证实） |
| 文件存在性 | `CvmInstanceCheckService.java` | 此文件不存在（代码地图正确排除） |

**结论**：Phase 2 深度代码扫描是质量驱动因素。生成的技能不是模板空壳——它们比人工维护的文档更准确。

### 2.3 模型分级落地情况

| 技能 | model_tier | L0 委托 | 状态 |
|------|:--:|------|:--:|
| code-map | **L0** | body 标注"must delegate to Haiku" | ✅ |
| dev | L1 | body 标注文件查找委托 code-map (L0) | ✅ |
| workflow | L1 | body 标注文件查找委托 code-map (L0) | ✅ |
| change-model | L1 | 关联技能表标注 code-map [L0] | ✅ |

### 2.4 渐进式加载落地情况

| 层 | 状态 | 问题 |
|------|:--:|------|
| L1 (openai.yaml) | ✅ 全部 4 个技能有 triggers 5-15 个 | — |
| L2 (SKILL.md) | ✅ body ≤5000t，包含可操作内容 | — |
| L3 (references/) | ❌ 全部缺失 | functional 层技能应有但未创建 |
| L4 (scripts/) | N/A | 该项目无可执行脚本 |

## 三、方法论缺口（已修复）

在生成过程中发现并修复了 3 个缺口：

| # | 缺口 | 修复 | 提交 |
|---|------|------|------|
| 1 | GENERATE 规则未要求创建 references/ | 新增规则 7：functional 技能必须创建 references/ | `9fdeefd` |
| 2 | GENERATE 规则未要求加载 L3 reference | 新增规则 8：生成 X 类型技能前先加载对应 L3 reference | `9fdeefd` |
| 3 | 风险等级 L0-L3 与执行层级命名冲突 | R0-R3 辨析说明，同步更新 phase-3-generate.md | `9fdeefd` |

## 四、方法论缺口（待修复）

| # | 缺口 | 严重程度 | 建议 |
|---|------|:--:|------|
| 1 | **V3 语义验证未实现** | 高 | validate-skills.py 增加 `--semantic` 模式，检查文件路径存在性/方法名准确性/版本号一致性 |
| 2 | **SCAN 不检测已有规范/文档** | 高 | Phase 2 增加"已有文档扫描"维度：现有 README、CHANGELOG、CONTRIBUTING 等应被检测并纳入生成决策 |
| 3 | **技能已存在时无冲突处理** | 中 | 管线增加"技能冲突"分支：覆盖/合并/跳过，用户确认 |
| 4 | **Token 预算无工具强制** | 中 | check-skill-health.py 已做估算但 validate-skills.py 不阻止超限文件 |
| 5 | **Plan Tree v0.1 仍未集成** | 低 | 当前在 `docs/design/` 中标注为设计文档，短期内不需操作 |

## 五、结构评估（两次独立 worktree 评估）

### 5.1 第一次评估（结构完整性）

通过：渐进式加载、自举规则、方法论完整性。发现 6 个交叉引用/路径问题 → 已修复（`c872ca0`）。

### 5.2 第二次评估（实用性）

发现理论过度问题 → 已修复（`40c344c`）：
- Plan Tree 404 行理论从 references/ 移至 docs/design/
- "45% Rule" 从 delegation.md 删除
- 自举规则从 SKILL.md 移至 CLAUDE.md
- 风险等级 R0-R3 与执行层级 L0-L3 辨析

### 5.3 第三次评估（章节逻辑）

12 个平级章节重新组织为 4 大章 → 已修复（`4f33a9d`）：
1. 核心概念（双轴 + 模型路由 + 技能类型 + 选择矩阵）
2. 执行管线（五阶段 + L3 路由表）
3. 部署（目录结构 + CLAUDE.md 集成 + 冲突解决）
4. 参考（模板索引 + 导入步骤 + 规范）

## 六、当前项目状态

```
SKILL-BUILDER-GUIDE/              ← 部署到 .claude/skills/skill-builder/
├── SKILL.md                      ← L2: 4 大章，8 条 GENERATE 硬规则
├── agents/openai.yaml            ← L1: 15 触发词
├── CLAUDE.md                     ← 维护者路由 + 自举规则
├── README.md                     ← 人类索引
│
├── references/                   ← L3: 按需加载
│   ├── delegation.md             ← H-ADMC + 3 模式 + C/B/U 格式 + 升级策略
│   ├── change-model.md           ← 4 层架构 + 8 项调用链检查 + 归档（R0-R3）
│   ├── frontmatter-spec.md       ← 必填/禁止/删除字段
│   ├── validation-protocol.md    ← V1/V2/V3 标准 + 接受率
│   └── pipeline/                 ← Phase 0/2/3 模板和示例
│
├── templates/                    ← 5 个 example-* 模板 + 3 个骨架
├── scripts/                      ← validate + health-check + package
├── docs/
│   ├── design/plan-tree.md       ← Plan Tree v0.1 设计文档
│   └── evaluation-report-2026-05-09.md  ← 本报告
└── workflows/                    ← CI
```

## 七、下一步推进建议

### P0（阻塞生成质量）
1. **V3 语义验证**：validate-skills.py 增加 `--semantic` 模式
2. **SCAN 已有文档检测**：Phase 2 增加维度，避免生成与现有规范冲突的技能

### P1（提升生成完整性）
3. **技能冲突处理**：管线增加"技能已存在"分支
4. **Token 预算强制**：validate-skills.py 硬阻止 >5000t

### P2（方法论完善）
5. **Plan Tree 集成或降级**：要么实现到 delegation pipeline，要么从 references 完全移除
6. **第二次真实项目测试**：用修复后的方法论重新生成 tengxunCVM 技能，对比改进效果
