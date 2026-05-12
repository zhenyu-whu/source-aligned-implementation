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
2. 本运行文档构成 `openspec-propose` source-truth 阶段的显式分派指令；只要用户已要求使用 `openspec-propose` 创建 OpenSpec change，且 `source-truth` 是当前可写 artifact，主 agent 不得再要求用户额外确认或授权 subagent 分派。
3. 若运行环境没有可用 subagent 能力，或更高优先级规则明确禁止创建 subagent，主 agent 必须暂停 `openspec-propose` 后续 artifact 生成并报告 blocker；不得静默改为主 agent 自行生成 `source-truth.md`。
4. 该 subagent 只负责完成 `source-truth.md`。不得同时起草、修改或预填 proposal、specs、design、tasks。
5. 启动 subagent 时使用显式任务包；默认不要 fork 完整对话历史，除非该 artifact 依赖尚未写入文件的关键对话决策。
6. 任务包必须包含 change 意图、schema 名称、当前可写 artifact、完整 `source-truth` instruction/template/outputPath/dependencies、已知 source 文档路径，以及交付物/最终回复要求。
7. 必须明确告知 subagent：source 文档缺失、source 冲突、change 边界不清、用户请求与 source 不一致、或 schema instruction 无法满足时，必须记录 blocker，不得静默选择较弱解释。

## 分阶段 Source Truth 任务包

为避免 subagent 在大范围 source reading 中长期停留在不可观察的阅读 / 规划阶段，主 agent 的任务包必须要求 subagent 按以下顺序写入同一个 `source-truth.md`。这些步骤不放松 schema 的完整性要求，只把完整阅读与无损抽取拆成可审查的中间结构。

1. **Source Manifest**
   - 先根据 change 意图、change plan、control sheet、handoff、schema instruction 与用户指定文档列出 source manifest。
   - manifest 至少区分 `required`、`conditionally relevant and read`、`reference-only`、`intentionally not read`。
   - change plan 或 handoff 明确点名的 readiness、system、source、PRD、architecture、data/API、security/ops、verification 文档默认属于 `required`，不得因为文档多而跳过。
   - 被 required 文档直接引用且影响当前 change 的 page/object/PRD/architecture/API/data/system/security/ops/verification 文档属于 `conditionally relevant and read`，必须读取后再关闭 source-truth。

2. **Source Coverage Ledger**
   - 每读完一个文档，立刻在 `source-truth.md` 的 ledger 中记录 exact path、sections/headings/anchors read、extraction buckets、coverage outcome。
   - coverage outcome 必须指向 Source Truth ID、deferred/non-goal Source Truth ID、unresolved conflict，或写明具体 `no-current-change-impact` reason。
   - 不允许把“尚未判断”“可能无关”“文件太大”作为最终 coverage outcome。

3. **Extraction Buckets**
   - subagent 必须先按 schema template 的 buckets 归集 obligations，再合并 Source Truth items。
   - bucket 名称以当前 schema template 为准；若 template 未列明某个 source-backed obligation 的 bucket，必须新增 change-specific bucket，不得丢弃。
   - 常见 prototype buckets 包括 runtime / scene-loader、scene fixtures、shared slices、mock mutations、object-state fixtures、visual assets、mark / selection / token payloads、export preview / record、state vocabulary / forbidden drift、component / responsive constraints、verification obligations、later-change / non-goal boundaries。
   - 常见 production buckets 包括 product / workflow scope、architecture / module boundaries、domain / data / migrations、API / auth / security、async / realtime / AI / worker、storage / assets、frontend / UX / prototype fidelity、observability / ops / deployment、verification obligations、later-change / non-goal boundaries。

4. **Source Truth Consolidation**
   - bucket 内容完成后，再合并成稳定 `ST-001` 等 Source Truth items。
   - Source Truth item 可以合并多个相邻 source obligations，但不得删掉实现相关细节、命名标识、边界、失败/禁用/恢复规则或验收义务。
   - 每个 item 仍必须包含 `Source`、`Extract`、`Relevance`、`Implementation Implication`、`Boundary`。

5. **Alignment Gate**
   - 最终 gate 必须核对 manifest-required 文档、conditional 文档、bucket、named identifiers 与 Source Truth IDs 的覆盖。
   - 如果任一 required / conditional source 尚未读取或无法覆盖，subagent 必须记录 unresolved conflict / blocker，而不是生成“无冲突”结论。

任务包应明确：subagent 可以分批写入 `source-truth.md`，但最终回复前必须完成 manifest 中所有 required 与 conditionally relevant 文档的读取和 gate 覆盖；不得以阶段性草稿冒充完成品。

## 主 Agent 审查门禁

1. 主 agent 必须审查 `source-truth.md` 是否遵守当前 schema 的 `source-truth` instruction 与 template，而不是依据本文档重新定义 source extraction 规则。
2. 主 agent 至少确认文件写入了 instruction 指定的 `outputPath`、结构符合 template、`Source Manifest`、`Source Coverage Ledger`、`Extraction Buckets`、`Source Truth Alignment Gate` 存在且无未处理 blocker。
3. 主 agent 必须抽查 manifest-required 文档和 conditionally relevant 文档是否在 ledger 中有 coverage outcome，且每个 applicable bucket 在 alignment gate 中映射到 Source Truth ID、deferred/non-goal ID 或 unresolved conflict。
4. 主 agent 必须抽查当前 change 的命名标识覆盖，至少包括 source docs 中出现的 scene、route、object state、fixture key、slice、mutation、asset ID、component specimen、viewport、verification check、workflow、module、command、API、entity/table、job/event、environment 等相关标识。
5. 若审查发现 `source-truth.md` 未满足 schema instruction、template 或本运行约束，主 agent 必须暂停后续 artifact 生成，并要求原 subagent 修正或报告 blocker。
6. 只有 `source-truth.md` 通过审查后，主 agent 才能继续执行 `openspec-propose` 的 proposal、specs、design、tasks 流程。
