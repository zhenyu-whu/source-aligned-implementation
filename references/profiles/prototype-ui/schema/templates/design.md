## Context

<!-- 说明背景、current prototype state、source docs、constraints 与 dependencies。 -->

## Goals / Non-Goals

**Goals:**
<!-- 说明此 design 为 prototype 达成什么。 -->

**Non-Goals:**
<!-- 说明此 design 明确排除什么。 -->

## Prototype Source Map

<!-- 将此 change 映射到 Source Truth IDs 与 exact original sources：plan row、PRD/architecture/prototype docs、handoff、page/object specs、system readiness docs、API/data contracts 与 verification matrix rows。 -->

## Decisions

<!-- 记录 source-backed technical/design decisions；存在真实选择时说明 rationale 与 alternatives。 -->

## Runtime / Data Flow Design

<!-- 说明此 change 的 route -> scene config -> fixture -> shell -> page body -> object state，以及 applicable 时的 equivalent frontend/backend/data flow。覆盖每个 current-change Source Truth item。 -->

## Fixture / Mutation / Asset Design

<!-- 说明 deterministic fixture slices、local state、mock mutations、stable assets 与 forbidden real services。 -->

## Page / Object / Responsive Design

<!-- 说明 page regions、object open/close 与 recovery behavior、component specimens、viewport behavior 与 object degradation。 -->

## Verification Design

<!-- 描述此 change 需要的 source-equivalent checks：user-equivalent interactions、API/contract tests、mutation/persistence assertions、failure/edge paths、rendered layout checks、scene smoke、key flow、object、asset 与 responsive checks。 -->

## Prototype Alignment Gate

- Source Truth IDs implemented / preserved / deferred: <!-- ST-001 implemented, ST-002 preserved, ST-003 deferred, ...；逐个枚举 exact IDs，不使用 ST-001-ST-010 这类 ranges -->
- Canonical keys used: <!-- state keys、stage keys、overlay keys、scene IDs、object keys；说明文字 -->
- Source trace complete: <!-- yes/no 加缺失项；说明文字 -->
- No new scene/page/object/lifecycle/overlay introduced: <!-- yes/no；说明文字 -->
- Interactions trace to source-backed interaction map or equivalent source document: <!-- yes/no 或 not applicable；说明文字 -->
- Fixture writes stay inside allowed slices/local state: <!-- yes/no 或 not applicable；说明文字 -->
- Assets/components trace to readiness docs: <!-- yes/no 或 not applicable；说明文字 -->
- Responsive obligations captured: <!-- yes/no 或 not applicable；说明文字 -->
- Later-change boundaries preserved: <!-- yes/no；说明文字 -->

## Risks / Trade-offs

<!-- 说明 known risks 与 mitigations。 -->

## Open Questions

<!-- 说明 outstanding questions。没有剩余问题时才写“无”。 -->
