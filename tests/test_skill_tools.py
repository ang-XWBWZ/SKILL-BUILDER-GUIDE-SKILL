"""Regression tests for the portable skill validation and packaging tools."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def load_script(filename: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, REPOSITORY_ROOT / "scripts" / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {filename}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_script("validate-skills.py", "skill_validator")
PACKAGER = load_script("package-skill.py", "skill_packager")
LINK_CHECKER = load_script("check-markdown-links.py", "markdown_link_checker")


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class SkillToolTests(unittest.TestCase):
    def test_parser_accepts_portable_frontmatter(self) -> None:
        fields, errors = VALIDATOR.parse_frontmatter(
            "name: sample-skill\n"
            "description: >-\n"
            "  Validate a portable skill when its structure and routing need checking.\n"
        )

        self.assertEqual("sample-skill", fields["name"])
        self.assertIn("Validate a portable skill", fields["description"])
        self.assertEqual([], errors)

    def test_parser_rejects_unindented_block_scalar(self) -> None:
        _, errors = VALIDATOR.parse_frontmatter(
            "name: sample-skill\n"
            "description: >-\n"
            "this line is not indented\n"
        )

        self.assertTrue(any("block scalar content must be indented" in error for error in errors))

    def test_parser_rejects_duplicate_and_unsupported_fields(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            skill_dir = Path(temporary_directory) / "sample-skill"
            write(
                skill_dir / "SKILL.md",
                "---\n"
                "name: sample-skill\n"
                "name: duplicate-skill\n"
                "description: Validate a skill with enough detail to avoid a short-description warning.\n"
                "runtime: proprietary\n"
                "---\n"
                "## Scope\n\n## Procedure\n\n## Verification\n",
            )

            _, errors, _ = VALIDATOR.validate_skill(skill_dir, False, False)

        self.assertTrue(any("duplicate frontmatter field" in error for error in errors))
        self.assertTrue(any("unsupported field" in error for error in errors))

    def test_project_layout_checks_inline_code_routes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            project_root = Path(temporary_directory)
            write(
                project_root / "AGENTS.md",
                "# Routes\n\n| Request | Skill |\n|---|---|\n"
                "| Orientation | `.agents/skills/sample-context/SKILL.md` |\n",
            )
            write(
                project_root / ".agents" / "skills" / "sample-context" / "SKILL.md",
                "---\n"
                "name: sample-context\n"
                "description: Navigate a sample project and verify its documented constraints.\n"
                "---\n"
                "## Scope\n\n## Procedure\n\n## Verification\n",
            )

            errors, _ = VALIDATOR.validate_project_layout(project_root)
            self.assertEqual([], errors)

            write(
                project_root / "AGENTS.md",
                "# Routes\n\n`./.agents/skills/sample-context/SKILL.md`\n",
            )
            errors, _ = VALIDATOR.validate_project_layout(project_root)
            self.assertEqual([], errors)

            write(
                project_root / "AGENTS.md",
                "# Routes\n\n` .agents/skills/missing/SKILL.md `\n",
            )
            errors, _ = VALIDATOR.validate_project_layout(project_root)

        self.assertTrue(any("routes to a missing path" in error for error in errors))

    def test_validator_ignores_markdown_links_inside_fenced_examples(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            skill_dir = Path(temporary_directory) / "sample-skill"
            write(
                skill_dir / "SKILL.md",
                "---\n"
                "name: sample-skill\n"
                "description: Validate a portable skill while allowing illustrative fenced Markdown.\n"
                "---\n"
                "## Scope\n\n## Procedure\n\n```markdown\n[example](missing.md)\n```\n\n## Verification\n",
            )

            _, errors, _ = VALIDATOR.validate_skill(skill_dir, False, False)

        self.assertEqual([], errors)

    def test_package_skill_creates_missing_output_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            skill_dir = root / "sample-skill"
            write(skill_dir / "SKILL.md", "---\nname: sample-skill\ndescription: Package a sample skill for distribution and testing.\n---\n")
            write(skill_dir / "references" / "guide.md", "# Guide\n")

            archive = PACKAGER.package_skill(skill_dir, root / "dist")

            self.assertTrue(archive.is_file())
            with zipfile.ZipFile(archive) as zip_file:
                self.assertEqual(
                    {"sample-skill/SKILL.md", "sample-skill/references/guide.md"},
                    set(zip_file.namelist()),
                )

    def test_package_skill_rejects_an_output_inside_the_skill(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            skill_dir = Path(temporary_directory) / "sample-skill"
            write(skill_dir / "SKILL.md", "---\nname: sample-skill\ndescription: Package a sample skill for distribution and testing.\n---\n")

            with self.assertRaises(ValueError):
                PACKAGER.package_skill(skill_dir, skill_dir / "dist")

    def test_link_checker_reports_only_missing_local_links(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            write(root / "target.md", "# Target\n")
            write(
                root / "README.md",
                "[valid](target.md)\n[external](https://example.com)\n[missing](missing.md)\n"
                "```markdown\n[example](not-a-real-link.md)\n```\n",
            )

            broken = LINK_CHECKER.find_broken_links(root)

        self.assertEqual(1, len(broken))
        self.assertEqual("missing.md", broken[0][1])


if __name__ == "__main__":
    unittest.main()
