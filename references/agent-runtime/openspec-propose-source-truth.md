# openspec-propose source-truth 运行约束

当用户要求使用 `openspec-propose` 创建 OpenSpec change，且当前 schema 包含 `source-truth` artifact 时，必须遵守以下约束。

本文档只约束第一个 `source-truth` artifact 的运行编排。source extraction 的内容规则、原始文档范围、字段格式和完整性标准以当前 schema 的 `source-truth` instructions 与 template 为准；本文档不得替代、扩写或放松 schema 指令。

## 执行入口

1. 严格先执行 `openspec-propose` 技能原有的 change 创建、`openspec status --change "<name>" --json`、artifact 依赖顺序读取、以及 `openspec instructions source-truth --change "<name>" --json`。
2. 主 agent 必须确认 `source-truth` 是当前可写 artifact，并取得 schema 名称、instruction、template、outputPath、dependencies。
3. `source-truth` 是独立 source extraction 阶段，不是 proposal、spec、design 或 tasks 的压缩草稿。
4. 在 `source-truth.md` 由 subagent 完成并通过主 agent 审查前，不得进入 proposal、specs、design 或 tasks。

## 强制 Subagent 分派

1. 主 agent 必须为第一个可写 `source-truth` artifact 直接创建一个独立 subagent，由该 subagent 生成或修订 `source-truth.md`。不得把 subagent 分派降级为主 agent 直接编写。
2. 本运行文档构成 `openspec-propose` source-truth 阶段的项目级显式分派指令。用户要求使用 `openspec-propose` 创建 OpenSpec change，且 `source-truth` 是当前可写 artifact 时，即视为用户已明确授权主 agent 为该 artifact 创建 subagent。
3. 主 agent 不得在该流程中再次要求用户确认或授权 subagent 分派；也不得以“需要用户明确授权 subagent”为由暂停在 `source-truth` 阶段。
4. 若运行环境没有可用 subagent 能力，或平台 / 更高优先级规则硬性禁止创建 subagent，主 agent 必须暂停 `openspec-propose` 后续 artifact 生成并报告 blocker；不得静默改为主 agent 自行生成 `source-truth.md`。
5. 该 subagent 只负责完成 `source-truth.md`。不得同时起草、修改或预填 proposal、specs、design、tasks。
6. 启动 subagent 时使用显式任务包；默认不要 fork 完整对话历史，除非该 artifact 依赖尚未写入文件的关键对话决策。
7. 任务包必须包含 change 意图、schema 名称、当前可写 artifact、完整 `source-truth` instruction/template/outputPath/dependencies、已知 source 文档路径，以及交付物/最终回复要求。
8. 必须明确告知 subagent：source 文档缺失、source 冲突、change 边界不清、用户请求与 source 不一致、或 schema instruction 无法满足时，必须记录 blocker，不得静默选择较弱解释。

## 分阶段 Source Truth 任务包

为避免 subagent 在大范围 source reading 中长期停留在不可观察的阅读 / 规划阶段，主 agent 的任务包必须要求 subagent 增量写入同一个 `source-truth.md`。

1. subagent 不得等全部 source reading 完成后才首次写入 `source-truth.md`。
2. subagent 应按当前 schema template 的自然顺序构建产物：先写骨架和 `Source Manifest`，再随 source reading 进度更新 `Source Coverage Ledger` 与 `Extraction Buckets`，最后合并 `Source Truth Items`、deferred/non-goal、conflicts 和 alignment gate。
3. 阶段性内容可以是不完整草稿，但必须保持结构可审查，并清楚标明未完成部分、待覆盖 source 或 blocker。
4. 增量写入是 source-truth artifact 的自然构建流程，不要求额外创建独立 heartbeat 文件或复杂心跳协议。
5. 最终回复前，subagent 必须完成 schema instruction 要求的 source coverage 和 alignment gate；不得以阶段性草稿冒充完成品。

## 主 Agent 等待与关闭约束

主 agent 的默认行为是持续等待 subagent 完成 `source-truth.md`，不得因为耗时较长、`wait_agent` 超时、目标文件暂时不存在或阶段性内容不完整而打断、催促或关闭 subagent。只有出现明确不可继续信号时，主 agent 才可介入：

   - subagent 线程已明确 `shutdown`、`failed` 或工具返回不可恢复错误；
   - subagent 明确报告 blocker，且 blocker 阻止继续生成 artifact；
   - 用户明确要求暂停、停止、关闭或重新分派 subagent。

## 主 Agent 审查门禁

1. 主 agent 必须审查 `source-truth.md` 是否遵守当前 schema 的 `source-truth` instruction 与 template，而不是依据本文档重新定义 source extraction 规则。
2. 主 agent 至少确认文件写入了 instruction 指定的 `outputPath`、结构符合 template、`Source Manifest`、`Source Coverage Ledger`、`Extraction Buckets`、`Source Truth Alignment Gate` 存在且无未处理 blocker。
3. 主 agent 必须抽查 manifest-required 文档和 conditionally relevant 文档是否在 ledger 中有 coverage outcome，且每个 applicable bucket 在 alignment gate 中映射到 Source Truth ID、deferred/non-goal ID 或 unresolved conflict。
4. 主 agent 必须抽查当前 change 的命名标识覆盖，至少包括 source docs 中出现的 scene、route、object state、fixture key、slice、mutation、asset ID、component specimen、viewport、verification check、workflow、module、command、API、entity/table、job/event、environment 等相关标识。
5. 若审查发现 `source-truth.md` 未满足 schema instruction、template 或本运行约束，主 agent 必须暂停后续 artifact 生成，并要求原 subagent 修正或报告 blocker。
6. 只有 `source-truth.md` 通过审查后，主 agent 才能继续执行 `openspec-propose` 的 proposal、specs、design、tasks 流程。
