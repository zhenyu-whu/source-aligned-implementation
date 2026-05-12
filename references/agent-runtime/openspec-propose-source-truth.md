# openspec-propose source-truth 运行约束

当用户要求使用 `openspec-propose` 创建 OpenSpec change，且当前 schema 包含 `source-truth` artifact 时，必须遵守以下约束。

## 执行入口

1. 严格先执行 `openspec-propose` 技能原有的 change 创建、`openspec status --change "<name>" --json`、artifact 依赖顺序读取、以及 `openspec instructions source-truth --change "<name>" --json`。
2. `source-truth` 是独立 source extraction 阶段，不是 proposal、spec、design 或 tasks 的压缩草稿。
3. 主 agent 必须从 `source-truth` instructions 中获取 schema 名称、instruction、template、outputPath、dependencies，并确认该 artifact 是当前可写 artifact。
4. 在进入 proposal/specs/design/tasks 前，必须完成并审查 `source-truth.md`。

## 原始文档范围

1. `docs/` 目录下的原始文档是 source-truth 的权威来源。必须读取 change plan、用户请求和 schema 指令指向的 `docs/` 文档。
2. 对 prototype schema，至少应覆盖相关的 `docs/prototype/handoff/`、`docs/prototype/pages/`、`docs/prototype/objects/`、`docs/prototype/system/`、flow contracts、fixture、interaction、asset 和 verification 文档。
3. `openspec/specs/` 只能用于识别既有 capability 名称和已接受行为；不得用它替代 `docs/` 原始文档，也不得用它缩小 `docs/` 中描述的 source-backed obligation。
4. 当前代码、已有实现、历史 proposal/design/tasks、运行时现状和测试结果不能作为 source truth 的替代来源；它们只能用于发现冲突或辅助定位。

## Subagent 建议

1. 当当前环境和用户授权允许使用 subagent 时，主 agent 应优先为 `source-truth` 创建一个独立 subagent。
2. 该 subagent 只负责读取相关 `docs/` 原始文档并生成或修订 `source-truth.md`，不得同时起草 proposal/specs/design/tasks。
3. 启动 subagent 时默认不要 fork 完整对话历史；应使用显式任务包传递必要上下文。
4. 启动 subagent 时必须明确传入：
   - change 名称。
   - schema 名称。
   - `source-truth` instructions、template 和 outputPath。
   - 用户请求中描述的 change 意图。
   - 必读 `docs/` 原始文档路径清单；若路径清单不完整，要求 subagent 从 change plan 和 schema 指令补齐相关 `docs/` 文档。
   - 明确禁止用 `openspec/specs/`、历史 artifacts、代码实现或运行结果替代 `docs/` source truth。
   - 交付物要求：写入 `source-truth.md`，列出 Source Truth IDs、读取过的 source docs、未读文档及原因、deferred/non-goal IDs、冲突和完整性确认。
5. 必须明确告知 subagent：如果发现 source docs 冲突、change 边界不清、所需 `docs/` 文档缺失、或用户请求与 source docs 不一致，必须记录 blocker，不得静默选择较弱解释。

## 主 Agent 审查门禁

1. 主 agent 必须审查 `source-truth.md` 是否只把实现相关义务列为 Source Truth item，未把 workflow metadata、artifact readiness、无 blocker、可继续等流程事实当作 current-change scope。
2. 每个 current-change Source Truth item 必须包含 `Source`、`Extract`、`Relevance`、`Implementation Implication`、`Boundary`，且 `Source` 必须指向具体 `docs/` 路径和稳定锚点。
3. Source Truth ID 列表必须逐个枚举，不能使用 `ST-001-ST-010`、`ST-001..ST-010`、`ST-001 through ST-010` 等范围写法。
4. 若 `source-truth.md` 未读取必要 `docs/` 原始文档、用既有 specs/实现替代原始文档、遗漏明显 source-backed obligation、或存在未记录冲突，主 agent 必须暂停后续 artifact 生成并要求先修正 source-truth。
