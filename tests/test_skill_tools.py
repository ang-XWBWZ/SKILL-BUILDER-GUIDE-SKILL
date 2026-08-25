"""Regression tests for local packaging and documentation-link tools."""

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


PACKAGER = load_script("package-skill.py", "skill_packager")
LINK_CHECKER = load_script("check-markdown-links.py", "markdown_link_checker")


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class SkillToolTests(unittest.TestCase):
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
