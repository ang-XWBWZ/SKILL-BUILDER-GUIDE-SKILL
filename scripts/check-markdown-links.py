#!/usr/bin/env python3
"""Check local Markdown links across a guide, template library, or project."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
URL_SCHEME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
SKIPPED_PARTS = {".git", "__pycache__"}


def strip_fenced_code(content: str) -> str:
    """Remove fenced code blocks so illustrative Markdown is not treated as a link."""
    visible: list[str] = []
    fence: str | None = None
    for line in content.splitlines(keepends=True):
        marker = line.lstrip()
        if marker.startswith(("```", "~~~")):
            current_fence = marker[:3]
            if fence is None:
                fence = current_fence
                continue
            if current_fence == fence:
                fence = None
                continue
        if fence is None:
            visible.append(line)
    return "".join(visible)


def markdown_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(None, 1)[0] if target else ""
    return unquote(target.split("#", 1)[0].split("?", 1)[0]).replace("\\", "/")


def resolve_local_target(markdown_file: Path, raw_target: str) -> Path | None:
    target = markdown_target(raw_target)
    if not target or target.startswith(("#", "//")) or URL_SCHEME_PATTERN.match(target):
        return None
    return (markdown_file.parent / target).resolve()


def markdown_files(root: Path) -> list[Path]:
    if root.is_file():
        return [root] if root.suffix.lower() == ".md" else []
    return sorted(
        path
        for path in root.rglob("*.md")
        if not SKIPPED_PARTS.intersection(path.parts)
    )


def find_broken_links(root: Path) -> list[tuple[Path, str]]:
    broken: list[tuple[Path, str]] = []
    for markdown_file in markdown_files(root):
        content = strip_fenced_code(markdown_file.read_text(encoding="utf-8"))
        for target in LINK_PATTERN.findall(content):
            resolved = resolve_local_target(markdown_file, target)
            if resolved is not None and not resolved.exists():
                broken.append((markdown_file, target))
    return broken


def main() -> int:
    parser = argparse.ArgumentParser(description="Check local Markdown links recursively.")
    parser.add_argument("path", nargs="?", default=".", help="Markdown file or directory to inspect")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.exists():
        print(f"Path does not exist: {root}", file=sys.stderr)
        return 1

    files = markdown_files(root)
    broken = find_broken_links(root)
    display_root = root if root.is_dir() else root.parent
    for markdown_file, target in broken:
        print(f"{markdown_file.relative_to(display_root)}: broken local link: {target}", file=sys.stderr)
    print(f"Checked {len(files)} Markdown file(s); {len(broken)} broken local link(s).")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
