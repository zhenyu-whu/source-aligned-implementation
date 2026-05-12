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
        update_config(openspec_dir, schema_name),
    ]
    print(f"profile: {profile}")
    print(f"schema: {schema_name}")
    for result in results:
        print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
