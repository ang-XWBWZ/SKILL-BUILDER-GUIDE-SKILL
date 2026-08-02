#!/usr/bin/env python3
"""Validate portable project skills without a runtime-specific dependency."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FIELD_PATTERN = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$")
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER_PATTERN = re.compile(r"\{[A-Za-z_][A-Za-z0-9_ -]*\}")
PORTABLE_FIELDS = {"name", "description"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def split_frontmatter(content: str) -> tuple[str | None, str]:
    lines = content.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, content
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "".join(lines[1:index]), "".join(lines[index + 1 :])
    return None, content


def parse_fields(frontmatter: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    lines = frontmatter.splitlines()
    index = 0
    while index < len(lines):
        match = FIELD_PATTERN.match(lines[index])
        if not match:
            index += 1
            continue
        key, value = match.groups()
        value = value.strip()
        if value in {">", ">-", "|", "|-"}:
            continuation: list[str] = []
            index += 1
            while index < len(lines):
                candidate = lines[index]
                if candidate and not candidate[0].isspace() and FIELD_PATTERN.match(candidate):
                    index -= 1
                    break
                if candidate.strip():
                    continuation.append(candidate.strip())
                index += 1
            value = " ".join(continuation)
        fields[key] = value.strip().strip("\"'")
        index += 1
    return fields


def resolve_link(skill_dir: Path, target: str) -> Path | None:
    target = target.strip().strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    target = target.split("#", 1)[0]
    return (skill_dir / target).resolve()


def validate_links(skill_dir: Path, content: str) -> list[str]:
    errors: list[str] = []
    for target in LINK_PATTERN.findall(content):
        resolved = resolve_link(skill_dir, target)
        if resolved is not None and not resolved.exists():
            errors.append(f"broken relative link: {target}")
    return errors


def validate_skill(
    skill_dir: Path,
    allow_placeholders: bool,
    allow_name_mismatch: bool,
) -> tuple[dict, list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    result = {"path": str(skill_dir), "name": skill_dir.name}

    if not skill_md.is_file():
        return result, ["missing SKILL.md"], warnings

    try:
        content = read_text(skill_md)
    except UnicodeDecodeError:
        return result, ["SKILL.md must be UTF-8"], warnings

    frontmatter, body = split_frontmatter(content)
    if frontmatter is None:
        return result, ["SKILL.md must start with a closed frontmatter block"], warnings

    fields = parse_fields(frontmatter)
    result["name"] = fields.get("name", skill_dir.name)
    unknown_fields = sorted(set(fields) - PORTABLE_FIELDS)
    if unknown_fields:
        errors.append("portable frontmatter contains unsupported field(s): " + ", ".join(unknown_fields))

    name = fields.get("name", "")
    if not name:
        errors.append("frontmatter is missing name")
    elif not NAME_PATTERN.fullmatch(name):
        errors.append("name must contain lowercase letters, digits, and hyphens only")
    elif name != skill_dir.name and not allow_name_mismatch:
        errors.append(f"name '{name}' does not match directory '{skill_dir.name}'")

    description = fields.get("description", "")
    if not description:
        errors.append("frontmatter is missing description")
    elif len(description) < 30:
        warnings.append("description is very short; state both outcome and trigger context")

    errors.extend(validate_links(skill_dir, content))
    if not allow_placeholders and PLACEHOLDER_PATTERN.search(body):
        errors.append("unresolved placeholder found; use --allow-placeholders only for reusable templates")

    for section in ("## Scope", "## Procedure", "## Verification"):
        if section not in body:
            warnings.append(f"recommended section missing: {section}")

    return result, errors, warnings


def discover_skills(path: Path) -> list[Path]:
    if (path / "SKILL.md").is_file():
        return [path]
    if not path.is_dir():
        return []
    return sorted(child for child in path.iterdir() if child.is_dir() and (child / "SKILL.md").is_file())


def validate_project_layout(project_root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    agents_md = project_root / "AGENTS.md"
    skills_dir = project_root / ".agents" / "skills"

    if not agents_md.is_file():
        errors.append("project layout is missing AGENTS.md")
    if not skills_dir.is_dir():
        errors.append("project layout is missing .agents/skills/")
    elif not discover_skills(skills_dir):
        warnings.append(".agents/skills/ contains no skills")

    if agents_md.is_file():
        try:
            agents_content = read_text(agents_md)
        except UnicodeDecodeError:
            errors.append("AGENTS.md must be UTF-8")
        else:
            for target in LINK_PATTERN.findall(agents_content):
                target = target.strip().strip("<>").split("#", 1)[0]
                if target.startswith(".agents/") and not (project_root / target).exists():
                    errors.append(f"AGENTS.md routes to a missing path: {target}")
    return errors, warnings


def format_human(results: list[tuple[dict, list[str], list[str]]], layout_errors: list[str], layout_warnings: list[str]) -> None:
    for result, errors, warnings in results:
        status = "FAIL" if errors else "OK"
        print(f"[{status}] {result['name']} ({result['path']})")
        for item in errors:
            print(f"  error: {item}")
        for item in warnings:
            print(f"  warning: {item}")
    for item in layout_errors:
        print(f"[FAIL] project layout: {item}")
    for item in layout_warnings:
        print(f"[WARN] project layout: {item}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate portable SKILL.md files and an optional .agents project layout.")
    parser.add_argument("path", nargs="?", default=".", help="A skill directory or a directory containing direct skill children")
    parser.add_argument("--project-root", help="Validate AGENTS.md and .agents/skills/ at this project root")
    parser.add_argument("--allow-placeholders", action="store_true", help="Allow template placeholders in SKILL.md bodies")
    parser.add_argument(
        "--allow-name-mismatch",
        action="store_true",
        help="Allow a source package directory whose install-time name differs from its skill name",
    )
    parser.add_argument("--json", action="store_true", help="Emit a machine-readable report")
    args = parser.parse_args()

    target = Path(args.path).resolve()
    skills = discover_skills(target)
    results: list[tuple[dict, list[str], list[str]]] = []
    layout_errors: list[str] = []
    layout_warnings: list[str] = []

    if not skills:
        layout_errors.append(f"no skill directories found at {target}")
    else:
        results = [
            validate_skill(skill, args.allow_placeholders, args.allow_name_mismatch)
            for skill in skills
        ]

    if args.project_root:
        layout_errors, layout_warnings = validate_project_layout(Path(args.project_root).resolve())

    all_errors = layout_errors + [error for _, errors, _ in results for error in errors]
    all_warnings = layout_warnings + [warning for _, _, warnings in results for warning in warnings]

    if args.json:
        print(json.dumps({
            "skills": [
                {"skill": result, "errors": errors, "warnings": warnings}
                for result, errors, warnings in results
            ],
            "layout_errors": layout_errors,
            "layout_warnings": layout_warnings,
            "error_count": len(all_errors),
            "warning_count": len(all_warnings),
        }, ensure_ascii=False, indent=2))
    else:
        format_human(results, layout_errors, layout_warnings)
        print(f"\nSummary: {len(results)} skill(s), {len(all_errors)} error(s), {len(all_warnings)} warning(s)")

    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
