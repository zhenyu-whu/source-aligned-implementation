# openspec-propose artifact 运行约束

当执行或触发 `openspec-propose` 技能创建 OpenSpec change 时，必须遵守以下约束。

本文档约束 `openspec-propose` 的 artifact 生成语言、审查门禁，以及当当前 schema 包含 `source-truth` artifact 时的首个 `source-truth` 运行编排。artifact 内容规则、原始文档范围、字段格式和完整性标准仍以当前 schema 的 instructions 与 template 为准；本文档不得替代、扩写或放松 schema 指令。

## Artifact 中文约束

1. 创建或修改 OpenSpec artifacts 时，必须面向中文 reviewer；适用范围包括 `openspec/changes/**`、`openspec/specs/**` 以及由 schema template 生成的 artifact 内容。
2. 固定模板结构可以保持英文或原文，不需要也不应该强行翻译。这包括 artifact instruction / template 要求的固定标题、表头、字段名、trace block 字段名、规范关键字、ID、路径、代码/API/DB/package 标识、命令、文件名、模块名、函数名、类型名、枚举值，以及需要精确引用的源文档原文术语。
3. 上一条只豁免“固定字段或标识本身”，不豁免 agent 填写的解释性内容。凡是 agent 自己写入的句子、短语说明、表格单元格说明、trace block 字段值、proof、preserve、risk、verification、acceptance、design rationale、task description、Requirement 正文、Scenario 的 WHEN/THEN 条件与结果正文，都必须使用简体中文。
4. 技术英文术语可以作为标识或名词短语保留，但承载语义的句子必须中文化。换言之，允许写 `fixture loader`、`MUTATION_REGISTRY`、`npm run check` 这类标识；不允许写 `Runtime checks prove selected scenes load full envelopes` 这类英文解释句。应改为“运行时检查证明选中的 scenes 能加载完整 envelope”。
5. 表格判定规则：表头可以按 template 保持英文；表格中由 agent 填写的每个说明类单元格都按正文处理，必须中文。只有单元格内容完全由 ID、路径、代码标识、任务编号、capability 名称或源文档精确术语组成时，才可以保持英文或原文。
6. tasks artifact 的特殊判定：`Source Truth:`、`Spec:`、`Design:`、`Source:`、`Preserve:`、`Proof:` 这些 trace 字段名可以保持英文；字段值必须中文，除非字段值只是 ID、路径、代码标识、命令或精确 requirement/scenario 名称。checkbox 后的任务标题属于 task description，必须中文。
7. specs artifact 的特殊判定：OpenSpec 固定关键词和 heading 可保持 template 要求的形式；Requirement 正文、Scenario 的 WHEN/THEN 条件与结果说明必须中文。Requirement / Scenario 名称若由 agent 新拟定，优先中文；只有需要精确引用已有英文规范名或源文档原文术语时才保留英文。
8. proposal / design artifact 的特殊判定：固定章节标题可保持 template 形式；Why、What、Impact、Design decisions、Risks、Open Questions、Alignment Gate 等章节下的解释性正文必须中文。
9. 语言自查最低标准：把反引号中的代码/路径/命令/ID 暂时忽略后，每个由 agent 填写的自然语言句子仍应主要是简体中文；若剩余内容是一句英文或英文主导的说明，即判定为不合格。
10. 每生成或修订一个 artifact 后，主 agent 必须在继续下一个 artifact 前审查语言；若发现英文解释性正文，必须先修正当前 artifact，再继续后续 OpenSpec 流程。OpenSpec 结构校验、ST 覆盖校验或 schema validate 通过，不等同于语言门禁通过。
11. 若 artifact instruction 或 template 要求保留英文结构标题，不得为满足中文约束改写这些固定标题；正文用中文填充即可。

## Propose 执行入口

1. 严格执行 `openspec-propose` 技能原有的 change 创建、`openspec status --change "<name>" --json`、artifact 依赖顺序读取、以及 `openspec instructions <artifact-id> --change "<name>" --json`。
2. 对每个可写 artifact，主 agent 必须取得 schema 名称、instruction、template、outputPath、dependencies，并读取已完成 dependency artifact。读取 dependency 不等同于全文展开；当 dependency 是 `source-truth.md` 时，应按 Source Truth ID、`Source Pointers` 与 `Read Notes` 定点消费。
3. `context` 与 `rules` 是主 agent 必须遵守的约束，不得复制进 artifact 正文。
4. Artifact 生成顺序仍以 schema dependency graph 和 `applyRequires` 为准；本文档只增加语言和 source-truth 运行门禁，不改变 schema 定义的 artifact 内容职责。

## Source-truth 执行入口

本节只在当前 schema 包含 `source-truth` artifact，且 `source-truth` 是当前可写 artifact 时适用。

本节只约束第一个 `source-truth` artifact 的运行编排。source extraction 的内容规则、原始文档范围、字段格式和完整性标准以当前 schema 的 `source-truth` instructions 与 template 为准；本节不得替代、扩写或放松 schema 指令。

1. 严格先执行 `openspec-propose` 技能原有的 change 创建、`openspec status --change "<name>" --json`、artifact 依赖顺序读取、以及 `openspec instructions source-truth --change "<name>" --json`。
2. 主 agent 必须确认 `source-truth` 是当前可写 artifact，并取得 schema 名称、instruction、template、outputPath、dependencies。
3. `source-truth` 是独立 source extraction 阶段，不是 proposal、spec、design 或 tasks 的压缩草稿。
4. 在 `source-truth.md` 由 subagent 完成并通过主 agent 接口门禁前，不得进入 proposal、specs、design 或 tasks。

## 强制 Subagent 分派

1. 主 agent 必须为第一个可写 `source-truth` artifact 直接创建一个独立 subagent，由该 subagent 生成或修订 `source-truth.md`。不得把 subagent 分派降级为主 agent 直接编写。
2. 本文档的 source-truth 分节构成 `openspec-propose` source-truth 阶段的项目级显式分派指令。用户要求使用 `openspec-propose` 创建 OpenSpec change，且 `source-truth` 是当前可写 artifact 时，即视为用户已明确授权主 agent 为该 artifact 创建 subagent。
3. 主 agent 不得在该流程中再次要求用户确认或授权 subagent 分派；也不得以“需要用户明确授权 subagent”为由暂停在 `source-truth` 阶段。
4. 若运行环境没有可用 subagent 能力，或平台 / 更高优先级规则硬性禁止创建 subagent，主 agent 必须暂停 `openspec-propose` 后续 artifact 生成并报告 blocker；不得静默改为主 agent 自行生成 `source-truth.md`。
5. 该 subagent 只负责完成 `source-truth.md`。不得同时起草、修改或预填 proposal、specs、design、tasks。
6. 启动 subagent 时使用显式任务包；默认不要 fork 完整对话历史，除非该 artifact 依赖尚未写入文件的关键对话决策。
7. 任务包必须包含 change 意图、schema 名称、当前可写 artifact、完整 `source-truth` instruction/template/outputPath/dependencies、已知 source 文档路径、本文档的 Artifact 中文约束，以及交付物/最终回复要求。必须要求每个 Source Truth item 写出可供后续 artifacts 精准回读原文的 `Source Pointers` 与 `Read Notes`，不得添加 `Downstream Consumers` 字段。
8. 任务包必须明确要求 subagent 执行 schema 中的 zero-omission extraction protocol：先完成 `Source Manifest`、`Source Coverage Ledger` 和 `Section / Anchor Obligation Inventory`，再合并 `Extraction Buckets` 与最终 `Source Truth Items`。不得从宽泛阅读摘要直接起草最终 ST items。
9. 任务包必须要求 subagent 对每个 required / conditionally relevant source 采用 source-native structure 与 high-risk scan 双重方式建立候选 anchor：包括 headings、tables、rows、routes、commands、APIs、DTOs、entities/tables、jobs/events、assets/fixtures、verification rows、deployment/ops anchors，以及 `必须`、`不得`、`MUST`、`MUST NOT`、non-goal、later、auth、privacy、security、migration、transaction、idempotency、failure、retry、recovery、responsive、environment、observability 等高风险信号。
10. 任务包必须要求 `Section / Anchor Obligation Inventory` 的每一行闭环到 exact ST IDs、preserve-existing IDs、deferred/non-goal IDs、unresolved-conflict IDs，或具体 `no-current-change-impact` reason；任何未闭环 anchor 都是 blocker。
11. 任务包必须要求 subagent 在最终回复中只返回简短闭环报告：读取的 required / conditionally relevant docs 数量、inventory rows 数量、current / preserve / deferred / conflict ST 数量、是否存在 unclosed inventory rows 或 blocker。不得把大段 source docs 或完整 source-truth 正文带回主线程。
12. 必须明确告知 subagent：source 文档缺失、source 冲突、change 边界不清、用户请求与 source 不一致、schema instruction 无法满足、inventory 无法闭环、或 artifact 中文约束无法满足时，必须记录 blocker，不得静默选择较弱解释。

## 分阶段 Source Truth 任务包

为避免 subagent 在大范围 source reading 中长期停留在不可观察的阅读 / 规划阶段，主 agent 的任务包必须要求 subagent 增量写入同一个 `source-truth.md`。

1. subagent 不得等全部 source reading 完成后才首次写入 `source-truth.md`。
2. subagent 应按当前 schema template 的自然顺序构建产物：先写骨架和 `Source Manifest`，再随 source reading 进度更新 `Source Coverage Ledger` 与 `Section / Anchor Obligation Inventory`，随后整理 `Extraction Buckets`，最后合并带有 `Source Pointers` / `Read Notes` 的 `Source Truth Items`、deferred/non-goal、conflicts 和 alignment gate。
3. 阶段性内容可以是不完整草稿，但必须保持结构可审查，并清楚标明未完成部分、待覆盖 source 或 blocker。
4. 增量写入是 source-truth artifact 的自然构建流程，不要求额外创建独立 heartbeat 文件或复杂心跳协议。
5. 最终回复前，subagent 必须完成 schema instruction 要求的 source coverage、alignment gate 和 Artifact 中文约束；不得以阶段性草稿冒充完成品。

## 主 Agent 等待与关闭约束

主 agent 的默认行为是持续等待 subagent 完成 `source-truth.md`，不得因为耗时较长、`wait_agent` 超时、目标文件暂时不存在或阶段性内容不完整而打断、催促或关闭 subagent。只有出现明确不可继续信号时，主 agent 才可介入：

   - subagent 线程已明确 `shutdown`、`failed` 或工具返回不可恢复错误；
   - subagent 明确报告 blocker，且 blocker 阻止继续生成 artifact；
   - 用户明确要求暂停、停止、关闭或重新分派 subagent。

## 主 Agent 接口门禁

1. 主 agent 对 `source-truth.md` 只做接口门禁，不做内容复审；不得为了审核 `source-truth.md` 而重新读取大量原始 source docs、全文展开 source docs，或全文复核每个 ST item 的 source extraction 正确性。
2. 主 agent 至少确认文件写入了 instruction 指定的 `outputPath`、结构符合 template、`Source Manifest`、`Source Coverage Ledger`、`Section / Anchor Obligation Inventory`、`Extraction Buckets`、`Source Truth Items`、`Source Truth Alignment Gate` 存在且无未处理 blocker。
3. 主 agent 必须用结构化检查、`rg`、脚本或小窗口抽查确认每个 Source Truth item 具备 `Source`、`Source Pointers`、`Read Notes`、`Extract`、`Relevance`、`Implementation Implication` 与 `Boundary` 字段；不得添加 `Downstream Consumers` 字段。
4. 主 agent 必须检查 manifest-required 文档和 conditionally relevant 文档在 ledger 中有 coverage outcome，`Section / Anchor Obligation Inventory` 在 alignment gate 中声明每一行均已闭环，且每个 applicable bucket 在 alignment gate 中映射到 Source Truth ID、deferred/non-goal ID 或 unresolved conflict。该检查应基于 ledger/inventory/gate 结构，不要求主 agent 重新打开原始 source docs。
5. 主 agent 必须检查当前 change 的命名标识覆盖由 alignment gate 枚举或记录 blocker，至少包括 relevant 的 scene、route、object state、fixture key、slice、mutation、asset ID、component specimen、viewport、verification check、workflow、module、command、API、entity/table、job/event、environment 等标识。该检查只确认接口可消费，不替代 subagent 的 source extraction 责任。
6. 主 agent 必须审查 `source-truth.md` 是否满足 Artifact 中文约束；优先使用定点扫描或脚本结果。若发现英文解释性正文，必须先修正或要求原 subagent 修正，不得进入后续 artifact。
7. 若接口门禁发现 `source-truth.md` 缺少 required structure、inventory 未闭环、ST item 缺少 Source Pointers / Read Notes、存在未处理 blocker、ST ID 使用 range、或语言门禁失败，主 agent 必须暂停后续 artifact 生成，并要求原 subagent 修正或报告 blocker。
8. 只有 `source-truth.md` 通过接口门禁后，主 agent 才能继续执行 `openspec-propose` 的 proposal、specs、design、tasks 流程。
