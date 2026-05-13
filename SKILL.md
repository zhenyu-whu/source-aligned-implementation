---
name: source-aligned-implementation
description: Set up source-aligned OpenSpec implementation workflows in a repository. Use when the user wants to initialize or switch an OpenSpec schema/profile so implementation tasks are guided by original PRD, architecture, prototype, API, data, design, and verification source documents; supports profile selection such as prototype-ui and production-app and syncs matching schemas, agent-runtime constraints, config, and an AGENTS.md runtime section reference.
---

# Source-Aligned Implementation

Use this skill to configure a repository so OpenSpec artifacts and apply-time implementation enforce source-document alignment from original source documents through tasks and proof.

## Workflow

1. Inspect the target repository root. Default to the current working directory unless the user names another directory.
2. Inspect available profiles under `references/profiles/*/profile.yaml`.
3. Select a profile:
   - If the user specified one, use it.
   - If exactly one profile is available, use it.
   - If multiple profiles are available and the request does not identify one, ask the user to choose.
   - Do not invent a profile that is not bundled in this skill.
4. Read the selected profile metadata:
   - `profile.yaml` provides `schema_name`.
   - `schema_dir` defaults to `schema` when omitted.

5. Sync bundled OpenSpec files into the target repository:
   - Copy `<skill-root>/references/profiles/<profile>/<schema_dir>/` to `<repo-root>/openspec/schemas/<schema_name>/`.
   - Copy `<skill-root>/references/agent-runtime/*.md` to `<repo-root>/openspec/agent-runtime/`.
   - Create or update `<repo-root>/openspec/config.yaml` so the top-level `schema:` value is `<schema_name>`.
   - Preserve unrelated project-specific config entries when updating an existing `openspec/config.yaml`.
   - If target schema or runtime files already exist and differ, inspect the differences and update them intentionally; do not invent merge behavior for schema or runtime files.

6. Update project instructions:
   - Read `<skill-root>/references/agent-runtime/agents-md-source-aligned-section.md`.
   - Add its runtime section to the target repository `AGENTS.md`, preserving existing project-specific instructions.
   - If an equivalent section already exists, update it instead of adding a duplicate.

7. Verify the result:
   - `openspec/config.yaml` has `schema: <schema_name>`.
   - `openspec/schemas/<schema_name>/` exists.
   - `openspec/agent-runtime/*.md` contains the installed runtime constraint files.
   - `AGENTS.md` includes the source-aligned runtime section from `references/agent-runtime/agents-md-source-aligned-section.md`.
   - If the repository has OpenSpec CLI available, run `openspec list --json` to inspect active changes, then run `openspec status --change "<name>" --json` for the relevant change when useful.

## Bundled Resources

- `references/profiles/prototype-ui/`: profile for reviewed prototype/UI implementation work. The bundled schema is a source-aligned prototype/UI schema.
- `references/profiles/production-app/`: profile for production application implementation work. The bundled schema is a source-aligned production schema.
- `references/agent-runtime/`: shared runtime constraints for OpenSpec propose/apply/archive workflows and the `AGENTS.md` runtime section reference.

## Profile Contract

Each profile directory must contain:

- `profile.yaml` with `profile`, `schema_name`, and optional `schema_dir` (defaults to `schema` when omitted).
- The schema directory named by `schema_dir`, containing `schema.yaml` and any templates.

The skill synchronizes the selected schema directory to `openspec/schemas/<schema_name>/`, switches `openspec/config.yaml` to that schema, synchronizes runtime constraints, and updates `AGENTS.md`.
