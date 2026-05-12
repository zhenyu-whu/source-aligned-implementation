# openspec-apply-change 运行约束

当用户要求使用 `openspec-apply-change` 技能实施某个 OpenSpec change 时，必须遵守以下约束。

## 执行入口

1. 严格先执行 `openspec-apply-change` 技能原有的选择 change、读取 `openspec status --change "<name>" --json`、读取 `openspec instructions apply --change "<name>" --json`，并从 apply instructions 中获取 `contextFiles` 路径、进度、任务列表和动态指令。
2. 主 agent 只需要读取任务 artifact 以解析未完成任务章节、`Requirement Coverage`、以及每个任务的 `Source Truth` / `Spec` / `Design` / `Source` / `Preserve` / `Proof` trace 字段；不要在主 agent 中再次展开读取 source-truth、proposal、specs、design 或原始 source docs 等上下文文件内容，除非后续协调冲突、coverage gate 失败或审查结果时确有必要进行定点核对。
3. 完成任务 artifact 解析并展示当前进度后，即可分派 worker subagent。不得在完成 change 选择、status / instructions 读取、任务 artifact 解析和进度展示前启动实现或分派 subagent。
4. 本运行文档对技能中“读取 context files”的执行方式作项目级特化：主 agent 传递 `contextFiles` 路径清单，由各 worker subagent 在自己的任务范围内读取并遵守所需上下文。

## Coverage Gates

1. **Gate 1 / Apply 前任务覆盖检查**：在分派 worker 之前，主 agent 必须检查任务 artifact 是否包含 `Requirement Coverage`，以及所有未完成 checkbox 任务是否带有 `Source Truth`、`Spec`、`Design`、`Source`、`Preserve`、`Proof` trace 字段。若缺少这些结构，或明显存在 Source Truth item / scenario / design obligation 没有 implementation task、verification task 或 proof 的 coverage 表行，必须暂停实现并要求先更新 tasks artifact。若 artifact 仍包含未完成的 `Prototype Source Lock` 或等价的 source-reading / reconciliation-only checkbox 章节，视为过期任务结构：暂停实现，先更新 tasks artifact，把仍有代码或验证价值的内容迁移到具体实现或验证章节。
2. **Gate 2 / Worker 勾选前 proof 检查**：worker 在实现某个任务前，必须读取该任务 trace 字段指向的 source-truth、specs、design 和原始 source docs 相关片段；勾选前必须执行或说明 `Proof` 中列出的完成证据，并在最终回复中按任务列出 proof 结果。若任务摘要弱于 source-truth 或原始 source docs，worker 必须停止并报告 artifact mismatch，不得按较弱任务实现或勾选。
3. **Gate 3 / 完成后 coverage audit**：所有 worker 返回后，主 agent 必须统一核对 `Requirement Coverage` 三张表的每一行是否有已勾选任务、实现证据、验证证据，并能回链到 Source Truth IDs 和原始 source docs。若发现文本存在但结构、数量、区域、交互、data/API contract、失败/边界或 responsive 约束未被证明，不得视为 ready for archive。
4. Coverage gate 是实现质量闸门，不替代 OpenSpec artifacts。若 gate 暴露 task 与 specs/design/source docs 不一致，应更新对应 artifact，而不是用代码绕过。

## 任务章节拆分

1. 在进入实现阶段前，必须定位任务 artifact，并解析其中所有未完成任务所属的一级章节。
2. “一级章节”指任务文件中承载任务分组的最高层级 Markdown 章节；如果文件只有一个 `#` 标题，则以其下的 `##` 章节作为一级章节。
3. 只为包含未完成任务的一级章节创建开发任务。
4. `Requirement Coverage` 章节不属于开发任务章节；它只作为分派、勾选和最终审核的 coverage 索引使用。
5. `Prototype Source Lock` 是废弃章节，不再作为开发任务章节。新的 tasks artifact 不应生成该章；若历史 artifact 中存在已完成的该章，只能作为背景记录忽略，不得为它单独创建 worker。

## Subagent 分派

1. 对每个包含未完成任务的一级章节，必须分别创建一个 `worker` subagent 进行开发。
2. 每个 subagent 只负责自己章节内的任务。
3. 启动 subagent 时默认不要 fork 完整对话历史；应使用显式任务包传递必要上下文，例如 `fork_context: false`。只有当该章节必须依赖当前对话中尚未写入文件的决策或用户补充说明时，才允许 fork，并必须在分派说明中写明原因。
4. 启动 subagent 时必须明确传入：
   - change 名称。
   - schema 名称。
   - `contextFiles` 路径清单，并要求 worker 自行读取与本章节任务相关的 source-truth、proposal、specs、design、tasks 和源文档内容。
   - 对应一级章节的完整任务内容，包括每个任务的 `Source Truth`、`Spec`、`Design`、`Source`、`Preserve`、`Proof` trace 字段。
   - 与本章节任务 ID 相关的 `Requirement Coverage` 行。
   - 预期交付物。
   - 允许修改的代码范围或模块边界。
   - 任务状态更新要求：worker 完成并验证自己章节内任务后，必须自行把对应任务文件 checkbox 从 `- [ ]` 更新为 `- [x]`；未完成、未验证、缺少 trace 字段、`Proof` 未执行或存在 blocker 的任务不得勾选。
   - 最终回复要求：列出完成并已勾选的任务、每个任务覆盖的 `Requirement Coverage` 行、每个任务的 proof 结果、未勾选任务及原因、修改的文件、执行的验证命令、未验证项、潜在冲突或 blocker。
5. 必须明确告知 subagent：它负责读取并遵守完成本章节所需的 OpenSpec context 和被引用 source docs；实现前必须先读取任务 trace 字段指向的 source-truth、specs、design 和原始 source docs 相关片段；若发现 context 冲突、任务边界不清、trace 缺失、proof 不可执行、任务摘要弱于 source-truth / 原始 source docs，或需要跨章节决策，必须停止猜测并在最终回复中标明 blocker。
6. 必须明确告知 subagent：它不是唯一的开发者，不得回滚或覆盖其他 agent / 用户的改动，遇到重叠文件或冲突风险必须适配现有改动并在最终回复中说明。

## 主 Agent 职责

1. 主 agent 主要负责 orchestration：选择 change、读取 status / instructions、解析任务 artifact、按一级章节分派 worker、协调文件 ownership、等待全部 worker 结果、统一审查改动、运行或汇总验证和最终汇报。
2. 主 agent 在 subagent 开发期间负责协调和非重叠工作，不得直接替代某个已分派章节完成实现，除非该 subagent 返回明确 blocker 且用户同意主 agent 接手。
3. 主 agent 应避免为了“预热上下文”而批量读取 proposal、specs、design、`docs/prototype/` 或其他 source docs；需要核对时只做与冲突协调、结果审查或任务勾选直接相关的定点读取。
4. 如果多个一级章节必然修改同一文件或模块，主 agent 必须先声明冲突风险，并通过更细的文件 ownership、串行等待或明确集成步骤降低冲突；不得让多个 subagent 无约束地改同一片代码。
5. 主 agent 不应在每个 subagent 刚完成时立刻做完整审查；应先收集所有已分派 subagent 的最终回复和改动结果，再进行一次统一集成审核。只有出现明确 blocker、文件冲突需要立刻协调、或某个 worker 的结果会阻塞其他 worker 继续时，才做提前定点审查。
6. 统一集成审核至少确认：
   - 相关代码改动符合对应章节任务、任务 trace 字段、Source Truth IDs、原始 source docs 和 OpenSpec context。
   - `Requirement Coverage` 三张表的每一行都有已勾选任务、实现证据、验证证据，并能回链到 Source Truth IDs。
   - 未引入明显跨章节冲突。
   - subagent 报告的测试、验证或未验证项清晰可信。
   - 所有可完成任务都有对应实现证据和 proof 证据；无法完成的任务有明确 blocker 和后续选项。

## 任务状态更新

1. 任务勾选由负责对应一级章节的 worker subagent 执行；worker 完成并验证自己章节内任务后，应立即把对应任务文件 checkbox 从 `- [ ]` 更新为 `- [x]`。
2. worker 只能勾选自己章节内已经完成且满足 `Proof`、linked spec scenario、linked design obligation 和 `Preserve` 约束的任务；未完成、未验证、trace 缺失、上下文不足、设计不清或存在 blocker 的任务必须保持未勾选，并在最终回复中说明原因。
3. 主 agent 不负责常规任务勾选；主 agent 在统一集成审核中只核对 worker 已勾选任务是否有实现证据、proof 证据、coverage 行覆盖、是否存在跨章节冲突、是否需要纠偏。
4. 若统一审核发现 worker 误勾选、任务实现不完整、proof 不足、coverage 行未覆盖或验证不足，主 agent 必须在最终汇报中指出并提出处理方式；必要时可定点修正 checkbox 状态，但不得把常规勾选流程重新收回主 agent。

## 最终汇报

最终汇报必须按一级章节列出：

- 已完成的章节和任务。
- 每个 subagent 的关键改动范围。
- `Requirement Coverage` 审核结果，尤其是未覆盖或 proof 不足的 scenario / design obligation。
- 已执行的验证命令及结果。
- 未完成、被阻塞或需要用户决策的事项。
