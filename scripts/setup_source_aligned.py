#!/usr/bin/env python3
"""Install a source-aligned OpenSpec profile into a repository."""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def read_simple_yaml(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def list_profiles(root: Path) -> list[str]:
    profiles_dir = root / "references" / "profiles"
    if not profiles_dir.exists():
        return []
    return sorted(p.name for p in profiles_dir.iterdir() if (p / "profile.yaml").exists())


def dirs_equal(left: Path, right: Path) -> bool:
    cmp = filecmp.dircmp(left, right)
    if cmp.left_only or cmp.right_only or cmp.funny_files:
        return False
    for name in cmp.common_files:
        if not filecmp.cmp(left / name, right / name, shallow=False):
            return False
    return all(dirs_equal(left / name, right / name) for name in cmp.common_dirs)


def copy_dir(src: Path, dst: Path, force: bool) -> str:
    if dst.exists():
        if dirs_equal(src, dst):
            return f"unchanged {dst}"
        if not force:
            raise SystemExit(
                f"Refusing to overwrite existing different directory: {dst}\n"
                "Re-run with --force after reviewing the existing schema."
            )
        shutil.rmtree(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst)
    return f"installed {dst}"


def copy_runtime(src_dir: Path, dst_dir: Path, force: bool) -> list[str]:
    results: list[str] = []
    dst_dir.mkdir(parents=True, exist_ok=True)
    for src in sorted(src_dir.glob("*.md")):
        dst = dst_dir / src.name
        if dst.exists():
            if filecmp.cmp(src, dst, shallow=False):
                results.append(f"unchanged {dst}")
                continue
            if not force:
                raise SystemExit(
                    f"Refusing to overwrite existing different runtime file: {dst}\n"
                    "Re-run with --force after reviewing the existing runtime constraints."
                )
        shutil.copy2(src, dst)
        results.append(f"installed {dst}")
    return results


def extract_literal_block(text: str, key: str) -> list[str]:
    lines = text.splitlines()
    header = f"{key}: |"
    for index, line in enumerate(lines):
        if line.strip() != header:
            continue
        block: list[str] = []
        for block_line in lines[index + 1 :]:
            if block_line and not block_line.startswith(" "):
                break
            block.append(block_line)
        return block
    return []


def replace_schema_line(lines: list[str], schema_name: str) -> tuple[list[str], bool]:
    updated = list(lines)
    changed = False
    for index, line in enumerate(updated):
        if line.startswith("schema:"):
            next_line = f"schema: {schema_name}"
            if line != next_line:
                updated[index] = next_line
                changed = True
            return updated, changed
    return [f"schema: {schema_name}", *updated], True


def find_literal_block(lines: list[str], key: str) -> tuple[int, int] | None:
    header = f"{key}: |"
    for index, line in enumerate(lines):
        if line.strip() != header:
            continue
        end = index + 1
        while end < len(lines):
            if lines[end] and not lines[end].startswith(" "):
                break
            end += 1
        return index, end
    return None


def has_top_level_key(lines: list[str], key: str) -> bool:
    prefix = f"{key}:"
    return any(line.startswith(prefix) for line in lines)


def sync_context_policy(lines: list[str], template_context: list[str]) -> tuple[list[str], bool]:
    if not template_context:
        return lines, False

    updated = list(lines)
    block_range = find_literal_block(updated, "context")
    if block_range is None:
        if has_top_level_key(updated, "context"):
            raise ValueError("existing config uses a non-literal context format")
        schema_index = next((index for index, line in enumerate(updated) if line.startswith("schema:")), 0)
        insert_at = schema_index + 1
        insert_lines = ["", "context: |", *template_context]
        updated[insert_at:insert_at] = insert_lines
        return updated, True

    header_index, end_index = block_range
    block = updated[header_index + 1 : end_index]
    policy_index = next((index for index, line in enumerate(block) if line.strip() == "Artifact language policy:"), None)
    if policy_index is None:
        insert_lines = [*template_context]
        if block and block[0].strip():
            insert_lines.append("")
        updated[header_index + 1 : header_index + 1] = insert_lines
        return updated, True

    policy_end = policy_index + 1
    while policy_end < len(block):
        stripped = block[policy_end].strip()
        if not stripped or stripped.startswith("- "):
            policy_end += 1
            continue
        break

    if block[policy_index:policy_end] == template_context:
        return updated, False

    updated[header_index + 1 + policy_index : header_index + 1 + policy_end] = template_context
    return updated, True


def update_config(openspec_dir: Path, schema_name: str) -> str:
    config = openspec_dir / "config.yaml"
    if not config.exists():
        config.write_text(f"schema: {schema_name}\n", encoding="utf-8")
        return f"created {config}"

    lines = config.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.startswith("schema:"):
            if line.strip() == f"schema: {schema_name}":
                return f"unchanged {config}"
            lines[index] = f"schema: {schema_name}"
            config.write_text("\n".join(lines) + "\n", encoding="utf-8")
            return f"updated {config}"

    config.write_text(f"schema: {schema_name}\n" + "\n".join(lines) + "\n", encoding="utf-8")
    return f"updated {config}"


def sync_config(openspec_dir: Path, schema_name: str, template: Path | None, force: bool) -> str:
    if template is None or not template.exists():
        return update_config(openspec_dir, schema_name)

    config = openspec_dir / "config.yaml"
    template_text = template.read_text(encoding="utf-8")
    template_context = extract_literal_block(template_text, "context")

    if not config.exists():
        config.write_text(template_text.rstrip() + "\n", encoding="utf-8")
        return f"created {config}"

    if force:
        if config.read_text(encoding="utf-8") == template_text.rstrip() + "\n":
            return f"unchanged {config}"
        config.write_text(template_text.rstrip() + "\n", encoding="utf-8")
        return f"installed {config}"

    lines = config.read_text(encoding="utf-8").splitlines()
    lines, schema_changed = replace_schema_line(lines, schema_name)
    try:
        lines, context_changed = sync_context_policy(lines, template_context)
    except ValueError as exc:
        raise SystemExit(
            f"Refusing to merge profile config into existing different config: {config}\n"
            f"{exc}. Re-run with --force after reviewing the existing config."
        ) from exc
    if not schema_changed and not context_changed:
        return f"unchanged {config}"

    config.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return f"updated {config}"


def choose_profile(root: Path, requested: str | None) -> str:
    profiles = list_profiles(root)
    if requested:
        if requested not in profiles:
            raise SystemExit(f"Unknown profile {requested!r}. Available profiles: {', '.join(profiles) or '(none)'}")
        return requested
    if len(profiles) == 1:
        return profiles[0]
    raise SystemExit(
        "Profile is required because available profiles are ambiguous: "
        + (", ".join(profiles) if profiles else "(none)")
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Install a source-aligned OpenSpec profile.")
    parser.add_argument("--target", default=".", help="Repository root to configure. Defaults to current directory.")
    parser.add_argument("--profile", help="Profile name, for example prototype-ui.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing differing schema/runtime files.")
    args = parser.parse_args()

    root = skill_root()
    profile = choose_profile(root, args.profile)
    profile_dir = root / "references" / "profiles" / profile
    profile_data = read_simple_yaml(profile_dir / "profile.yaml")
    schema_name = profile_data.get("schema_name")
    schema_dir_name = profile_data.get("schema_dir", "schema")
    if not schema_name:
        raise SystemExit(f"Profile {profile!r} is missing schema_name in profile.yaml")

    repo_root = Path(args.target).resolve()
    openspec_dir = repo_root / "openspec"
    schema_src = profile_dir / schema_dir_name
    schema_dst = openspec_dir / "schemas" / schema_name
    config_template = profile_dir / "config.yaml"
    runtime_src = root / "references" / "agent-runtime"
    runtime_dst = openspec_dir / "agent-runtime"

    if not schema_src.exists():
        raise SystemExit(f"Missing profile schema directory: {schema_src}")
    if not runtime_src.exists():
        raise SystemExit(f"Missing agent-runtime reference directory: {runtime_src}")

    openspec_dir.mkdir(parents=True, exist_ok=True)
    results = [
        copy_dir(schema_src, schema_dst, args.force),
        *copy_runtime(runtime_src, runtime_dst, args.force),
        sync_config(openspec_dir, schema_name, config_template, args.force),
    ]
    print(f"profile: {profile}")
    print(f"schema: {schema_name}")
    for result in results:
        print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
