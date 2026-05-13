# Source-Aligned Implementation Skill

This Codex skill synchronizes source-aligned OpenSpec workflows into a target repository. It is intended for projects where implementation artifacts must stay aligned with original source documents such as PRDs, architecture notes, reviewed prototypes, API/data contracts, design references, and verification plans.

## What It Syncs

When a profile is selected, copy these bundled resources into the target repository:

- `openspec/schemas/<schema_name>/`: profile-owned OpenSpec schema and artifact templates.
- `openspec/agent-runtime/*.md`: runtime constraints for propose, apply, and archive workflows.
- `openspec/config.yaml`: active schema selection via top-level `schema: <schema_name>`.

The skill also includes an `AGENTS.md` runtime section under `references/agent-runtime/agents-md-source-aligned-section.md`. Add or update that section in the target repository instructions after syncing schema/runtime files.

## Profiles

Two profiles are bundled:

- `prototype-ui`: source-aligned prototype/UI implementation workflow. Use it when source docs define routes, scenes, surfaces, objects, state, fixtures/data, interactions, assets, responsive behavior, and verification.
- `production-app`: source-aligned production application workflow. Use it when source docs define product behavior, architecture/module boundaries, data/API contracts, security/privacy, async processing, observability, deployment, UX fidelity, and verification.

Each profile contains:

- `profile.yaml`: profile metadata and target schema name.
- `schema/`: OpenSpec schema and templates.

## Usage

Use the skill workflow in `SKILL.md`. In summary:

1. Select one bundled profile.
2. Read its `profile.yaml` to get `schema_name` and optional `schema_dir`.
3. Copy the profile schema directory to `openspec/schemas/<schema_name>/`.
4. Copy shared runtime markdown files to `openspec/agent-runtime/`.
5. Create or update `openspec/config.yaml` so `schema:` points to `<schema_name>`, preserving unrelated project config.
6. Add or update the source-aligned runtime section in `AGENTS.md`.

## Verification

After syncing a profile, verify:

- `openspec/config.yaml` selects the requested schema.
- `openspec/schemas/<schema_name>/schema.yaml` exists.
- `openspec/agent-runtime/openspec-propose-artifacts.md` exists.
- `openspec/agent-runtime/openspec-apply-change.md` exists.
- `openspec/agent-runtime/openspec-archive-change.md` exists.
- `AGENTS.md` includes the source-aligned runtime section.

## Development Notes

Keep profile changes semantically aligned. Shared behavior, such as language policy or design-depth guidance, should usually live in shared runtime constraints and apply to both `prototype-ui` and `production-app`, while profile-specific templates preserve their own vocabulary and scope.
