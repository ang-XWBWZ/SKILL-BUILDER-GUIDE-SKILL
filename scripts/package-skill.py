#!/usr/bin/env python3
"""Package a canonical skill directory as a distributable ZIP archive."""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path


def package_skill(skill_dir: str | Path, output_dir: str | Path = ".") -> Path:
    """Create ``<output_dir>/<skill-name>.zip`` and return its path.

    The output directory is created when absent. It must be outside the source skill
    directory so an existing archive cannot be included in itself.
    """
    source = Path(skill_dir).resolve()
    output = Path(output_dir).resolve()

    if not source.is_dir():
        raise FileNotFoundError(f"skill directory does not exist: {source}")
    if not (source / "SKILL.md").is_file():
        raise ValueError(f"skill directory is missing SKILL.md: {source}")
    if output == source or source in output.parents:
        raise ValueError("output directory must be outside the skill directory")

    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"{source.name}.zip"
    excluded_parts = {"__pycache__"}

    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for path in sorted(source.rglob("*")):
            if not path.is_file() or excluded_parts.intersection(path.parts) or path.suffix == ".pyc":
                continue
            arcname = path.relative_to(source.parent).as_posix()
            zip_file.write(path, arcname)

    return archive


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if not 1 <= len(args) <= 2:
        print("Usage: python package-skill.py <skill_dir> [output_dir]", file=sys.stderr)
        return 1

    try:
        archive = package_skill(args[0], args[1] if len(args) == 2 else ".")
    except (OSError, ValueError) as error:
        print(f"Packaging failed: {error}", file=sys.stderr)
        return 1

    print(f"Packaged: {archive}")
    with zipfile.ZipFile(archive) as zip_file:
        for info in zip_file.infolist():
            print(f"  {info.file_size:>8}  {info.filename}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
