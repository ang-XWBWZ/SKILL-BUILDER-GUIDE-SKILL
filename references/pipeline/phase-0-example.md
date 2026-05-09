# End-to-End Example: Creating Skills for a NestJS Backend

> This is a concrete walkthrough showing what each phase produces. Use it as a granularity benchmark when creating skills for any project.

## Project Profile

- **Type**: NestJS REST API backend
- **Tech stack**: TypeScript, NestJS, Prisma ORM, PostgreSQL, Redis
- **Structure**: Layered (controller → service → repository)
- **Team**: 3 developers
- **Profile**: Medium → 3 skills: dev + code-map + change-model

---

## Phase 1 Output: Skill Plan

```
Conclusion: 3 skills for this NestJS project: nestjs-dev (L1/atomic),
nestjs-code-map (L0/atomic), nestjs-change-model (L1/functional).

Basis:
- Medium project (3 devs, ~50 API routes, 4 modules) → 3 skills per matrix
- TypeScript/NestJS/Prisma stack has clear layered conventions → dev skill needed
- Multiple modules (users, orders, payments, notifications) → code-map needed
- Team does structured releases → change-model needed
- No multi-service architecture → delegation/call-chain not needed
- Existing scripts are documented in package.json → scripts not needed

Uncertainty: None
```

---

## Phase 2 Output: Scan Code Samples (per layer)

```
=== Controller Layer ===
Files: 12 (users.controller.ts, orders.controller.ts, ...)
Pattern: @Controller('path') + @Get/@Post/@Patch/@Delete
Validation: class-validator decorators (@IsString, @IsNumber)
Auth guard: @UseGuards(JwtAuthGuard) on most routes
Response: Return service result directly (no unified wrapper)

=== Service Layer ===
Files: 8 (users.service.ts, orders.service.ts, ...)
Pattern: @Injectable() class → constructor injects PrismaService + other services
Transaction: this.prisma.$transaction([...])
Error handling: throw new HttpException(msg, code)

=== Data Layer ===
Files: 1 (schema.prisma) + generated client
ORM: Prisma Client (generated from schema.prisma)
Query pattern: this.prisma.user.findMany({ where, include, skip, take })
Pagination: skip + take (cursor-based in list endpoints)

=== Config ===
Env: .env + config module
Package manager: npm (package-lock.json exists)
Test: Jest (jest.config.js)
```

---

## Phase 3 Output: Generated Files

### nestjs-dev/SKILL.md (excerpt — shows correct granularity)

```markdown
---
name: nestjs-dev
description: >-
  NestJS project development standards. Triggered when asking about
  tech stack, code conventions, API patterns, Prisma queries, or
  module structure.
model_tier: L1
skill_tier: atomic
version: 1.0.0
status: active
---

# NestJS Development Standards

## Trigger Conditions
- Asking about NestJS patterns, decorators, guards, pipes
- "How to create a new module / controller / service"
- "What ORM / database setup"
- "Prisma query conventions"
- "How to handle errors / validation"

## Related Skills
- [Code Map](../nestjs-code-map/SKILL.md) — file locations [L0]
- [Change Model](../nestjs-change-model/SKILL.md) — change reports

---

## 1. Tech Stack

| Category | Technology | Version |
|----------|-----------|---------|
| Runtime | Node.js | 20.11.0 |
| Language | TypeScript | 5.3.3 |
| Framework | NestJS | 10.3.0 |
| ORM | Prisma | 5.9.0 |
| Database | PostgreSQL | 16 |
| Cache | Redis (ioredis) | 5.3.0 |
| Validation | class-validator | 0.14.0 |
| Auth | @nestjs/jwt + @nestjs/passport | 10.0.0 |

## 2. Module Structure

```
src/
├── common/           # Shared guards, pipes, filters, decorators
├── config/           # Configuration module
├── prisma/           # PrismaService (global)
├── users/            # User module
│   ├── users.controller.ts
│   ├── users.service.ts
│   └── dto/
└── orders/           # Order module (same pattern)
```

## 3. Controller Conventions
...
```

### nestjs-code-map/SKILL.md (excerpt — shows L0 brevity)

```markdown
---
name: nestjs-code-map
description: >-
  NestJS project file location map. Triggered when asking where to
  find or modify code. L0 — delegate to Haiku.
model_tier: L0
skill_tier: atomic
version: 1.0.0
status: active
---

# NestJS Code Map

## Quick Lookup

| Need | Look Here |
|------|----------|
| Add API endpoint | `src/{module}/{module}.controller.ts` |
| Change business logic | `src/{module}/{module}.service.ts` |
| Change database schema | `prisma/schema.prisma` |
| Add validation | `src/{module}/dto/*.dto.ts` |
| Add auth guard | `src/common/guards/` |

## Module Index

| Module | Path | Routes |
|--------|------|--------|
| Users | `src/users/` | /api/users, /api/users/:id |
| Orders | `src/orders/` | /api/orders, /api/orders/:id |
...
```

### openai.yaml for nestjs-dev

```yaml
interface:
  display_name: "L1-atomic — nestjs-dev"
  short_description: "L1-atomic — NestJS dev standards. Tech stack, module patterns, Prisma conventions, validation rules."
  default_prompt: "Use nestjs-dev to query NestJS project conventions and coding standards."
policy:
  allow_implicit_invocation: false
triggers:
  - NestJS 模式
  - 模块结构
  - Prisma 查询
  - DTO 校验
  - controller 写法
  - service 写法
  - 依赖注入
  - guard pipe
  - 异常处理
```

---

## Phase 4 Output: Validation Report

```
=== 技能验证报告 ===
[OK] nestjs-dev
[OK] nestjs-code-map
[OK] nestjs-change-model
扫描技能数: 3
错误数: 0
警告数: 0
[OK] 全部通过！
```

---

## Phase 5 Output: Confirmation

```
【Generated Skills】
nestjs-dev (L1/atomic): NestJS development standards
  - SKILL.md: .claude/skills/nestjs-dev/SKILL.md (~3400 tokens)
  - openai.yaml: .claude/skills/nestjs-dev/agents/openai.yaml (9 triggers)
  - Validation: V1 ✅ V2 ✅

nestjs-code-map (L0/atomic): File location map
  - SKILL.md: .claude/skills/nestjs-code-map/SKILL.md (~600 tokens)
  - openai.yaml: .claude/skills/nestjs-code-map/agents/openai.yaml (7 triggers)
  - Validation: V1 ✅ V2 ✅

nestjs-change-model (L1/functional): Change reports
  - SKILL.md: .claude/skills/nestjs-change-model/SKILL.md (~2800 tokens)
  - openai.yaml: .claude/skills/nestjs-change-model/agents/openai.yaml (11 triggers)
  - Validation: V1 ✅ V2 ✅

【Confirmation Items】
- Version numbers from package.json scan: NestJS 10.3.0, Prisma 5.9.0, etc.
- Trigger words extracted from project: NestJS 模式, Prisma 查询, DTO 校验, ...
- Cross-references: all 3 skills reference each other with relative paths
- User document integration: no user docs provided, all content from code scan

Confirm? (approved / revise({feedback}) / reject)
```

---

## Key Takeaways (for AI following this pipeline)

1. **dev skill** is the longest (~3000-4000 tokens) — it captures conventions the AI needs to follow
2. **code-map skill** is the shortest (~500-800 tokens) — pure lookup table, zero reasoning
3. **change-model skill** is medium (~2000-3000 tokens) — the four-layer template is most of it
4. **Every generated skill** has concrete code snippets from the actual project scan (sanitized)
5. **Trigger words** match the project's primary language and actual terminology
6. **No placeholders** remain in any generated file — all `{placeholder}` replaced with scan results
