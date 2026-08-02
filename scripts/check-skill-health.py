#!/usr/bin/env python3
"""Report maintainability signals for portable project skills."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER_PATTERN = re.compile(r"\{[A-Za-z_][A-Za-z0-9_ -]*\}")


def split_body(content: str) -> str:
    if not content.startswith("---"):
        return content
    parts = content.split("---", 2)
    return parts[2] if len(parts) == 3 else content


def discover_skills(path: Path) -> list[Path]:
    if (path / "SKILL.md").is_file():
        return [path]
    if not path.is_dir():
        return []
    return sorted(child for child in path.iterdir() if child.is_dir() and (child / "SKILL.md").is_file())


def is_broken_link(skill_dir: Path, target: str) -> bool:
    target = target.strip().strip("<>").split("#", 1)[0]
    if not target or target.startswith(("http://", "https://", "mailto:")):
        return False
    return not (skill_dir / target).resolve().exists()


def assess(skill_dir: Path, allow_placeholders: bool) -> dict:
    content = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    body = split_body(content)
    words = len(body.split())
    markers: list[dict[str, str]] = []

    if words > 3500:
        markers.append({"level": "review", "reason": f"large body (~{words} words); consider moving detail to references/"})
    for section in ("## Scope", "## Procedure", "## Verification"):
        if section not in body:
            markers.append({"level": "review", "reason": f"missing recommended section: {section}"})
    if "## Handoff" not in body:
        markers.append({"level": "info", "reason": "no Handoff section; fine for a terminal skill"})
    broken = [target for target in LINK_PATTERN.findall(content) if is_broken_link(skill_dir, target)]
    if broken:
        markers.append({"level": "stale", "reason": f"broken relative links: {', '.join(broken)}"})
    if not allow_placeholders and PLACEHOLDER_PATTERN.search(body):
        markers.append({"level": "stale", "reason": "contains unresolved placeholders"})

    return {"name": skill_dir.name, "path": str(skill_dir), "words": words, "markers": markers}


def main() -> int:
    parser = argparse.ArgumentParser(description="Check portable skills for size, missing sections, links, and stale placeholders.")
    parser.add_argument("path", help="A skill directory or directory containing direct skill children")
    parser.add_argument("--allow-placeholders", action="store_true", help="Ignore placeholders in reusable templates")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    skills = discover_skills(Path(args.path).resolve())
    if not skills:
        print("No skill directories found.", file=sys.stderr)
        return 1
    reports = [assess(skill, args.allow_placeholders) for skill in skills]

    if args.json:
        print(json.dumps({"skills": reports}, ensure_ascii=False, indent=2))
    else:
        print(f"{'Skill':<30} {'Words':>7}  Signals")
        print("-" * 72)
        for report in reports:
            markers = report["markers"]
            summary = "; ".join(marker["reason"] for marker in markers) if markers else "healthy"
            print(f"{report['name']:<30} {report['words']:>7}  {summary}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
