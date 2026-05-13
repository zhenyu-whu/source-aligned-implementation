## Source Manifest

<!--
在提取 Source Truth items 前，对此 change 的 source documents 分类。
使用 exact paths。Required documents 必须读取；当 conditionally relevant documents 被 required docs 引用，且影响当前 change 的 workflows、routes、modules、commands、APIs、data entities、jobs/events、assets、security rules、environments、verification checks 或 later-change boundaries 时，也必须读取。
-->

| Classification | Source Document | Reason / Change Link |
| --- | --- | --- |
| required | <!-- exact path --> | <!-- change row / capability / workflow / route / module / API / entity / job / environment / verification link；说明文字 --> |
| conditionally relevant and read | <!-- exact path --> | <!-- 说明此 document 为什么影响当前 change --> |
| reference-only | <!-- exact path --> | <!-- 例如仅用于 existing capability names；不得缩小 source truth --> |
| intentionally not read | <!-- exact path --> | <!-- 说明具体 no-overlap reason；convenience 或 file size 不是有效理由 --> |

## Source Documents Read

<!-- 列出为此 change 读取过的每个 original PRD、architecture、prototype、design、interaction、API、data、security、ops、deployment 与 verification document。包含 exact paths 与 relevant headings/sections。 -->

## Source Coverage Ledger

<!--
每个已读 source document 保持一行。每个 document 必须贡献 Source Truth、deferred/non-goal Source Truth、unresolved conflict，或明确的 no-current-change-impact note。
-->

| Source Document | Sections / Anchors Read | Extraction Buckets | Coverage Outcome |
| --- | --- | --- | --- |
| <!-- exact path --> | <!-- headings / rows / workflow names / route names / command names / API names / entity names / job/event types / environment names / verification rows --> | <!-- product / workflow scope; architecture / module boundaries; domain / data / migrations; API / auth / security; async / realtime / AI / worker; storage / assets; frontend / UX / prototype fidelity; observability / ops / deployment; verification obligations; later-change / non-goal boundaries; change-specific bucket --> | <!-- ST-001, ST-002 / deferred ST-... / unresolved conflict ST-... / no-current-change-impact: reason；说明文字 --> |

## Extraction Buckets

<!--
使用 buckets 避免在合并 Source Truth items 前丢失 source detail。
Buckets 不能替代 Source Truth items；buckets 中每个 implementation-relevant obligation 都必须在下方表示。
如有需要，可添加 change-specific buckets。
-->

### Product / Workflow Scope

<!-- 记录 user goals、workflows、product surfaces、acceptance criteria 与 explicit product boundaries。 -->

### Architecture / Module Boundaries

<!-- 记录 package/app/module ownership、runtime boundaries、technology decisions、composition 与 forbidden architectural drift。 -->

### Domain / Data / Migrations

<!-- 记录 entities、tables、DTOs、migrations、transactions、locks、idempotency、persistence ownership 与 data invariants。 -->

### API / Auth / Security

<!-- 记录 API endpoints/contracts、commands、authorization、permissions、privacy/security rules、entitlement checks 与 audit requirements。 -->

### Async / Realtime / AI / Worker

<!-- 记录 jobs、queues、SSE/realtime events、outbox/reconciler behavior、AI provider boundaries、sandbox behavior、retries 与 recovery。 -->

### Storage / Assets

<!-- 记录 file/object storage、signing/access rules、generated assets、retained artifacts、export assets 与 cleanup boundaries。 -->

### Frontend / UX / Prototype Fidelity

<!-- 记录 routes、pages、component states、interactions、responsive behavior、accessibility 与 prototype fidelity obligations。 -->

### Observability / Ops / Deployment

<!-- 记录 logging、metrics、tracing、alerts、rollout、environment config、deployment、backfill、compatibility 与 operational readiness。 -->

### Verification Obligations

<!-- 记录 unit、contract、integration、E2E、smoke、migration、security、observability、deployment 与 source-equivalent verification obligations。 -->

### Later-Change / Non-Goal Boundaries

<!-- 记录 downstream artifacts 必须保留的 source-backed deferrals 与 explicit non-goals。 -->

## Source Truth Items

<!--
使用 stable IDs。提取与所选 production change 相关的每个 source-backed item。
不要在本节决定 implementation shortcuts；先捕获 source truth。
仅为 implementation-relevant obligations 创建 Source Truth items：需要实现的行为、需要保留的行为、需要执行的验证、需要执行的边界，或需要解决的 conflicts。
不要为 workflow metadata、artifact readiness、dependency status、absence of blockers、“no questions” 或 “can proceed”等流程事实创建 Source Truth items；这些内容放入 Conflicts / Ambiguities 或 Alignment Gate。
-->

### ST-001 <!-- 简短的 source-backed obligation name，可保留英文技术术语 -->

- Source: <!-- exact file path plus heading / stable anchor / row / route / object / API / command / table / event / job / asset / fixture / interaction / ops / deployment / verification name -->
- Extract: <!-- 复制或紧密改写 source truth，并保留所有 implementation-relevant details -->
- Relevance: <!-- 说明为什么它属于当前 change -->
- Implementation Implication: <!-- 说明 proposal/spec/design/tasks/apply 必须保留什么 -->
- Boundary: <!-- current-change scope / preserve-existing / later-change / non-goal / unresolved conflict；必要说明 -->

## Deferred / Non-Goal Source Truth

<!-- 按 Source Truth ID 列出 source-backed later-change 与 non-goal items。不要编造没有 original sources 支撑的 deferrals。 -->

## Conflicts / Ambiguities

<!-- 记录 conflicts、ambiguous ownership、missing production decisions 或 source gaps。没有剩余问题时才写“无”。 -->

## Source Truth Alignment Gate

- Source documents read: <!-- exact paths；说明文字 -->
- Source documents intentionally not read: <!-- exact paths and reasons，或“无” -->
- Required manifest coverage: <!-- 确认每个 required document 都被 Source Truth / deferred Source Truth / unresolved conflict / no-current-change-impact note 覆盖 -->
- Conditional manifest coverage: <!-- 确认每个 conditionally relevant document 已读取并覆盖，或列出 blockers -->
- Extraction bucket coverage: <!-- 列出每个 applicable bucket 及覆盖它的 Source Truth IDs 或 deferred/non-goal IDs；说明文字 -->
- Named identifier coverage: <!-- relevant 时枚举 covered workflows / routes / modules / commands / APIs / DTOs / entities / tables / migrations / job or event types / provider boundaries / asset or storage IDs / auth rules / entitlements / environments / verification checks -->
- Current-change Source Truth IDs: <!-- ST-001, ST-002, ... -->
- Preserve-existing Source Truth IDs: <!-- ST-... 或“无” -->
- Deferred / non-goal Source Truth IDs: <!-- ST-... 或“无” -->
- Unresolved conflicts: <!-- ST-... 或“无” -->
- Completeness confirmation: <!-- 确认没有 intentionally omitted 的 relevant source-backed obligation，或列出 blockers -->

<!-- Source Truth ID lists 必须枚举 exact IDs；不要使用 ST-001-ST-010 这类 ranges。 -->
