# Source-Aligned Implementation Skill

This Codex skill installs source-aligned OpenSpec workflows into a target repository. It is intended for projects where implementation artifacts must stay aligned with original source documents such as PRDs, architecture notes, reviewed prototypes, API/data contracts, design references, and verification plans.

## What It Installs

The setup script copies a selected profile into the target repository:

- `openspec/schemas/<schema_name>/`: profile-owned OpenSpec schema and artifact templates.
- `openspec/agent-runtime/*.md`: runtime constraints for propose, apply, and archive workflows.
- `openspec/config.yaml`: active schema selection plus profile-owned config defaults when provided.

The skill also includes an `AGENTS.md` runtime section under `references/agent-runtime/agents-md-source-aligned-section.md`. Add or update that section in the target repository instructions after running the setup script.

## Profiles

Two profiles are bundled:

- `prototype-ui`: source-aligned prototype/UI implementation workflow. Use it when source docs define routes, scenes, surfaces, objects, state, fixtures/data, interactions, assets, responsive behavior, and verification.
- `production-app`: source-aligned production application workflow. Use it when source docs define product behavior, architecture/module boundaries, data/API contracts, security/privacy, async processing, observability, deployment, UX fidelity, and verification.

Each profile contains:

- `profile.yaml`: profile metadata and target schema name.
- `schema/`: OpenSpec schema and templates.
- `config.yaml`: optional profile-owned OpenSpec config defaults such as artifact language policy.

## Usage

Run the installer from this skill directory:

```bash
scripts/setup_source_aligned.py --target /path/to/repo --profile prototype-ui
scripts/setup_source_aligned.py --target /path/to/repo --profile production-app
```

Use `--force` only after reviewing existing target files. It overwrites differing installed schema/runtime files and installs the profile config exactly.

## Config Sync Behavior

Without `--force`, `openspec/config.yaml` is merged conservatively:

- `schema:` is inserted or updated to the selected profile schema.
- If the profile has a literal `context: |` block, only the `Artifact language policy:` section is inserted or replaced.
- Existing project context outside that policy is preserved.
- Existing non-literal top-level `context:` formats are rejected instead of being rewritten implicitly.

When the target config does not exist, the profile config is copied as the initial file. With `--force`, the profile config fully replaces the target config.

## Verification

For installer changes:

```bash
python3 -m py_compile scripts/setup_source_aligned.py
```

For profile-install behavior, run the installer against a temporary repository and verify:

- `openspec/config.yaml` selects the requested schema.
- `openspec/schemas/<schema_name>/schema.yaml` exists.
- `openspec/agent-runtime/*.md` exists.
- Re-running or switching profiles does not duplicate the artifact language policy.

## Development Notes

Keep profile changes semantically aligned. Shared behavior, such as language policy or design-depth guidance, should usually be applied to both `prototype-ui` and `production-app`, but profile-specific templates should preserve their own vocabulary and scope.
