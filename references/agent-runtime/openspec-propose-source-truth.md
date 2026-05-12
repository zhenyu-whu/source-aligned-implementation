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

## 主 Agent 审查门禁

1. 主 agent 必须审查 `source-truth.md` 是否遵守当前 schema 的 `source-truth` instruction 与 template，而不是依据本文档重新定义 source extraction 规则。
2. 主 agent 至少确认文件写入了 instruction 指定的 `outputPath`、结构符合 template、`Source Truth Alignment Gate` 存在且无未处理 blocker。
3. 若审查发现 `source-truth.md` 未满足 schema instruction、template 或本运行约束，主 agent 必须暂停后续 artifact 生成，并要求原 subagent 修正或报告 blocker。
4. 只有 `source-truth.md` 通过审查后，主 agent 才能继续执行 `openspec-propose` 的 proposal、specs、design、tasks 流程。
