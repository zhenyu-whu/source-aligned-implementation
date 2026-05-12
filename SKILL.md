---
name: source-aligned-implementation
description: Set up source-aligned OpenSpec implementation workflows in a repository. Use when the user wants to initialize or switch an OpenSpec schema/profile so implementation tasks remain fully aligned to original PRD, architecture, prototype, API, data, design, and verification source documents; supports profile selection such as prototype-ui and installs matching schemas, agent-runtime constraints, config, and an AGENTS.md runtime section reference.
---

# Source-Aligned Implementation

Use this skill to configure a repository so OpenSpec artifacts and apply-time implementation enforce source-document alignment from original design docs through tasks and proof.

## Workflow

1. Inspect the target repository root. Default to the current working directory unless the user names another directory.
2. Inspect available profiles under `references/profiles/*/profile.yaml`.
3. Select a profile:
   - If the user specified one, use it.
   - If exactly one profile is available, use it.
   - If multiple profiles are available and the request does not identify one, ask the user to choose.
   - Do not invent a profile that is not bundled in this skill.
4. Run the setup script:

   ```bash
   <skill-root>/scripts/setup_source_aligned.py --target <repo-root> --profile <profile>
   ```

   `<skill-root>` is the actual directory containing this `SKILL.md`, whether the skill is installed in the repository or in a global Codex skills directory.

   Use `--force` only after reviewing existing differing schema or runtime files, because it overwrites them.

5. Update project instructions:
   - Read `<skill-root>/references/agent-runtime/agents-md-source-aligned-section.md`.
   - Add its runtime section to the target repository `AGENTS.md`, preserving existing project-specific instructions.
   - If an equivalent section already exists, update it instead of adding a duplicate.

6. Verify the result:
   - `openspec/config.yaml` has `schema: <schema_name>`.
   - `openspec/schemas/<schema_name>/` exists.
   - `openspec/agent-runtime/*.md` contains the installed runtime constraint files.
   - `AGENTS.md` includes the source-aligned runtime section from `references/agent-runtime/agents-md-source-aligned-section.md`.
   - If the repository has OpenSpec CLI available, run `openspec list --json` to inspect active changes, then run `openspec status --change "<name>" --json` for the relevant change when useful.

## Bundled Resources

- `references/profiles/prototype-ui/`: profile for reviewed prototype/UI implementation work. The bundled schema is the current project's source-aligned prototype schema.
- `references/agent-runtime/`: shared runtime constraints for OpenSpec propose/apply/archive workflows and the `AGENTS.md` runtime section reference.
- `scripts/setup_source_aligned.py`: deterministic installer for schemas, runtime files, and `openspec/config.yaml`.

## Profile Contract

Each profile directory must contain:

- `profile.yaml` with `profile`, `schema_name`, and `schema_dir`.
- The schema directory named by `schema_dir`, containing `schema.yaml` and any templates.

The setup script installs the schema to `openspec/schemas/<schema_name>/` and switches `openspec/config.yaml` to that schema.
