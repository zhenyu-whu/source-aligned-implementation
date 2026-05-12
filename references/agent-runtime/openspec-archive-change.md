# openspec-archive-change runtime instructions

## 默认行为

- 当用户明确要求使用 `openspec-archive-change` 技能或归档已完成 change，且未指定 change 名称时，先运行 `openspec list --json`。如果活跃 change 只有一个，则默认选择该 change 继续归档流程，不再额外要求用户确认选择；如果存在多个活跃 change、无活跃 change，或上下文与列表结果冲突，必须停下向用户确认。
- 归档前仍需读取 `openspec status --change "<name>" --json`、检查 `tasks.md` 完成度，并评估 `openspec/changes/<name>/specs/` 下的 delta specs 是否需要同步。检查结果中的非阻断性警告应在最终汇总中说明，但默认不要求二次确认。
- 如果 delta specs 存在且同步评估显示主 specs 需要新增或修改，默认执行“同步并归档”：优先使用 `openspec archive "<name>" -y` 完成 spec 更新与归档；如果 CLI 不可用或自动同步失败，再按 `openspec-sync-specs` 技能手动同步后归档。
- 只有遇到冲突或高风险状态时才向用户确认，包括但不限于：多个候选 change、归档目标目录已存在、delta spec 与主 spec 无法明确合并、存在未完成任务或未完成 artifact 且其状态看起来会影响交付完整性、命令失败、校验失败，或归档会覆盖/删除非目标文件。
- 归档完成后必须运行 `openspec validate --specs --strict --json`，并汇总 change 名称、schema、归档路径、spec 同步结果、任务完成情况、遗留警告和校验结果。
