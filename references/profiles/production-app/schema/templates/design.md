<!--
Language policy: 保留本模板中的 OpenSpec 结构、字段名、规范关键字、ID、路径、代码/API/DB/package 标识和常用技术术语；解释性正文、需求描述、设计说明、任务说明、风险、验收与验证说明使用简体中文。
-->

## Context

<!-- 用简体中文说明背景、current production state、source docs、constraints、dependencies 与 existing implementation context。 -->

## Goals / Non-Goals

**Goals:**
<!-- 用简体中文说明此 design 为 production system 达成什么。 -->

**Non-Goals:**
<!-- 用简体中文说明此 design 明确排除什么。 -->

## Production Source Map

<!-- 用简体中文将此 change 映射到 Source Truth IDs 与 exact original sources：PRD sections、architecture sections、prototype pages/objects/system docs、API/data/security/ops/deployment references 与 verification rows。 -->

## Decisions

<!-- 用简体中文记录 source-backed technical/product decisions；存在真实选择时说明 rationale 与 alternatives。 -->

## Architecture / Module Boundary Design

<!-- 用简体中文说明 app/package ownership、runtime/process boundaries、dependency direction、configuration ownership 与 forbidden cross-layer shortcuts。 -->

## Domain / Data / Migration Design

<!-- 用简体中文说明 domain commands/use-cases、policies/rules、data model、migrations、transaction boundaries、idempotency、locks、persistence，以及 relevant 时的 backfill/compatibility。 -->

## API / Auth / Security Design

<!-- 用简体中文说明 routes/handlers、DTO validation、session/user mapping、authorization、entitlement checks、privacy boundaries、sensitive data handling、asset access 与 audit behavior。 -->

## Async / Realtime / AI / Worker Design

<!-- 用简体中文说明 queues、job payloads、worker handlers、provider adapters、sandbox/fixture replay、SSE/outbox events、reconciler/maintenance loops、retries、failure recovery 与 lock release。 -->

## Frontend / UX / Prototype Fidelity Design

<!-- 用简体中文说明 page regions、route flow、client state、user interactions、object/component behavior、visual fidelity、responsive behavior、loading/empty/failure/disabled states，以及哪些 prototype UX 被有意保留。 -->

## Observability / Ops / Deployment Design

<!-- 用简体中文说明 structured logs、trace keys、audit records、metrics/alerts、environment variables、local/staging/production differences、deployment/migration ordering、operational runbooks 与 maintenance tasks。 -->

## Verification Design

<!-- 用简体中文描述 source-equivalent checks：domain unit tests、db integration tests、API/contract tests、worker/reconciler tests、SSE/outbox tests、auth/security/privacy negative tests、provider sandbox tests、frontend E2E/visual/responsive checks、deployment/config checks，以及 relevant 时的 staging smoke。 -->

## Rollout / Compatibility

<!-- 用简体中文描述 expand/deploy/switch/contract ordering、backward compatibility、migration/backfill、queue/job compatibility、feature flags/config 与 rollback constraints。不适用时才写“无”。 -->

## Production Alignment Gate

- Source Truth IDs implemented / preserved / deferred: <!-- ST-001 implemented, ST-002 preserved, ST-003 deferred, ...；逐个枚举 exact IDs，不使用 ST-001-ST-010 这类 ranges -->
- Canonical product and technical keys used: <!-- routes、commands、DTOs、tables、events、jobs、assets、entitlement names、env names、state keys；说明文字用简体中文 -->
- Source trace complete: <!-- yes/no 加缺失项；说明文字用简体中文 -->
- No unplanned route/page/object/service/API/table/job/event/provider/environment introduced: <!-- yes/no；说明文字用简体中文 -->
- Interactions trace to source-backed flows/contracts: <!-- yes/no 或 not applicable；说明文字用简体中文 -->
- Data writes, migrations, locks, idempotency, and transactions stay inside source-defined ownership boundaries: <!-- yes/no 或 not applicable；说明文字用简体中文 -->
- Auth, authorization, privacy, asset access, and audit rules trace to source-backed references: <!-- yes/no 或 not applicable；说明文字用简体中文 -->
- Async jobs, SSE/outbox, provider calls, sandbox behavior, and reconciler behavior trace to source-backed references: <!-- yes/no 或 not applicable；说明文字用简体中文 -->
- Assets/components/prototype UX/responsive obligations captured: <!-- yes/no 或 not applicable；说明文字用简体中文 -->
- Observability/ops/deployment obligations captured: <!-- yes/no 或 not applicable；说明文字用简体中文 -->
- Later-change boundaries preserved: <!-- yes/no；说明文字用简体中文 -->

## Risks / Trade-offs

<!-- 用简体中文说明 known risks 与 mitigations。 -->

## Open Questions

<!-- 用简体中文说明 outstanding questions。没有剩余问题时才写“无”。 -->
