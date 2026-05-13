<!--
Language policy: 保留本模板中的 OpenSpec 结构、字段名、规范关键字、ID、路径、代码/API/DB/package 标识和常用技术术语；解释性正文、需求描述、设计说明、任务说明、风险、验收与验证说明使用简体中文。
-->

## Source Manifest

<!--
提取 Source Truth items 前，先为此 change 分类 source documents。
使用 exact paths。Required documents 必须读取。Conditionally relevant documents 在被 required docs 引用并影响当前 change 的 routes、scenes、fixtures、mutations、assets、object states、verification checks 或 later-change boundaries 时必须读取。
-->

| Classification | Source Document | Reason / Change Link |
| --- | --- | --- |
| required | <!-- exact path --> | <!-- change row / capability / route / scene / fixture / mutation / asset / verification link；说明文字用简体中文 --> |
| conditionally relevant and read | <!-- exact path --> | <!-- 用简体中文说明此 document 为什么影响当前 change --> |
| reference-only | <!-- exact path --> | <!-- 例如 existing capability names only；不得缩小 source truth --> |
| intentionally not read | <!-- exact path --> | <!-- 用简体中文说明具体 no-overlap reason；convenience 或 file size 不是有效理由 --> |

## Source Documents Read

<!-- 用简体中文列出为此 change 读取过的每个 original PRD、architecture、prototype、design、interaction、API、data、system 与 verification document。包含 exact paths 与 relevant headings/sections。 -->

## Source Coverage Ledger

<!--
每个已读取的 source document 维护一行。每个 document 必须贡献 Source Truth、deferred/non-goal Source Truth、unresolved conflict，或 explicit no-current-change-impact note。
-->

| Source Document | Sections / Anchors Read | Extraction Buckets | Coverage Outcome |
| --- | --- | --- | --- |
| <!-- exact path --> | <!-- headings / rows / scene IDs / fixture keys / mutation names / asset IDs / object states --> | <!-- runtime / scene-loader; scene fixtures; shared slices; mock mutations; object-state fixtures; visual assets; mark / selection / token payloads; export preview / record; state vocabulary / forbidden drift; component / responsive constraints; verification obligations; later-change / non-goal boundaries; change-specific bucket --> | <!-- ST-001, ST-002 / deferred ST-... / unresolved conflict ST-... / no-current-change-impact: reason；说明文字用简体中文 --> |

## Extraction Buckets

<!--
使用 buckets，避免在合并 Source Truth items 前丢失 source detail。
Buckets 不能替代 Source Truth items；buckets 中每个 implementation-relevant obligation 都必须在下方表示。
需要时添加 change-specific buckets。
-->

### Runtime / Scene-Loader

<!-- 用简体中文记录 route、scene config、fixture loading、shell/page/object consumption chain 与 runtime boundary obligations。 -->

### Scene Fixtures

<!-- 用简体中文记录 Scene IDs、fixture keys、required slice presence、representative state combinations 与 fixture acceptance obligations。 -->

### Shared Slices

<!-- 用简体中文记录 data slice ownership、required fields、deterministic values 与 state/data boundaries。 -->

### Mock Mutations

<!-- 用简体中文记录 mutation names、affected slices、allowed writes、forbidden side effects、success/failure/running semantics。 -->

### Object-State Fixtures

<!-- 用简体中文记录 hosted inside scenes 的 object state variants、open/close context、local object fields 与 non-scene boundaries。 -->

### Visual Assets

<!-- 用简体中文记录 canvas、thumbnails、placeholders、empty states、export previews、dimensions、visual semantics 与 no-real-asset boundaries。 -->

### Mark / Selection / Token Payloads

<!-- 用简体中文记录 mark targets、selection geometry、token candidates、custom labels、stale/read-only behavior 与 payload immutability。 -->

### Export Preview / Record

<!-- 用简体中文记录 export preview asset、mock records、current-version-only export 与 no real file generation。 -->

### State Vocabulary / Forbidden Drift

<!-- 用简体中文记录 canonical keys、stage/overlay whitelist、no new routes/scenes/states/assets/mutations/services 与 semantic separation。 -->

### Component / Responsive Constraints

<!-- 用简体中文记录 token、component specimen、density、responsive、object degradation 与 visual fidelity obligations。 -->

### Verification Obligations

<!-- 用简体中文记录与此 change 相关的 smoke、screenshot、object、key-flow 与 source-equivalent verification obligations。 -->

### Later-Change / Non-Goal Boundaries

<!-- 用简体中文记录 downstream artifacts 必须保留的 source-backed deferrals 与 explicit non-goals。 -->

## Source Truth Items

<!--
使用 stable IDs。提取与所选 prototype/UI change 相关的每个 source-backed item。
不要用本节决定 implementation shortcuts。先捕获 source truth。
只为 implementation-relevant obligations 创建 Source Truth items：需要实现的 behavior、需要保留的 behavior、需要执行的 verification、需要执行的 boundaries，或需要解决的 conflicts。
不要为 workflow metadata、artifact readiness、dependency status、absence of blockers、“no questions” 或 “can proceed”等流程事实创建 Source Truth items；这些内容放入 Conflicts / Ambiguities 或 Alignment Gate。
-->

### ST-001 <!-- short source-backed obligation name -->

- Source: <!-- exact file path plus heading / stable anchor / row / scene / route / object / API / asset / fixture / interaction name -->
- Extract: <!-- 使用简体中文复制或紧密改写 source truth，并保留所有 implementation-relevant details -->
- Relevance: <!-- 用简体中文说明为什么它属于当前 change -->
- Implementation Implication: <!-- 用简体中文说明 proposal/spec/design/tasks/apply 必须保留什么 -->
- Boundary: <!-- current-change scope / preserve-existing / later-change / non-goal / unresolved conflict；必要说明用简体中文 -->

## Deferred / Non-Goal Source Truth

<!-- 用简体中文按 Source Truth ID 列出 source-backed later-change 与 non-goal items。不要发明没有 original sources 支持的 deferrals。 -->

## Conflicts / Ambiguities

<!-- 用简体中文记录 conflicts、ambiguous ownership 或 source gaps。没有剩余问题时才写“无”。 -->

## Source Truth Alignment Gate

- Source documents read: <!-- exact paths；说明文字用简体中文 -->
- Source documents intentionally not read: <!-- exact paths and reasons，或“无”；说明文字用简体中文 -->
- Required manifest coverage: <!-- 用简体中文确认每个 required document 都被 Source Truth / deferred Source Truth / unresolved conflict / no-current-change-impact note 覆盖 -->
- Conditional manifest coverage: <!-- 用简体中文确认每个 conditionally relevant document 已读取并覆盖，或列出 blockers -->
- Extraction bucket coverage: <!-- 列出每个 applicable bucket 及覆盖它的 Source Truth IDs 或 deferred/non-goal IDs；说明文字用简体中文 -->
- Named identifier coverage: <!-- relevant 时枚举 covered scenes / routes / object states / fixture keys / slices / mutations / asset IDs / component specimens / viewports / verification checks；说明文字用简体中文 -->
- Current-change Source Truth IDs: <!-- ST-001, ST-002, ... -->
- Preserve-existing Source Truth IDs: <!-- ST-... or "无" -->
- Deferred / non-goal Source Truth IDs: <!-- ST-... or "无" -->
- Unresolved conflicts: <!-- ST-... or "无" -->
- Completeness confirmation: <!-- 用简体中文确认没有 intentionally omitted 的 relevant source-backed obligation，或列出 blockers -->

<!-- Source Truth ID lists 必须逐个枚举 exact IDs；不要使用 ST-001-ST-010 这类 ranges。 -->
