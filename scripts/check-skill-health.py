#!/usr/bin/env python3
"""
Tier 2 — Skill health offline scanner.

Reads skill SKILL.md frontmatter and validates structure,
cross-references, and review dates. Pure stdlib, no LLM dependency.
Haiku (L0) execution.

Usage:
  python scripts/check-skill-health.py skills/
  python scripts/check-skill-health.py skills/ --json
  python scripts/check-skill-health.py skills/ --skill delegation
"""

import os
import sys
import re
import json
from datetime import datetime

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def parse_frontmatter(filepath):
    """Extract YAML frontmatter between --- markers. Returns dict of parsed fields."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    text = parts[1]

    fields = {}
    for key in ["name", "description", "model_tier", "skill_tier", "version",
                "status", "review_by"]:
        m = re.search(rf'^{key}:\s*(.+)', text, re.MULTILINE)
        if m:
            fields[key] = m.group(1).strip().strip('"').strip("'")

    return fields


def extract_cross_references(body_text):
    """Extract relative markdown links from SKILL.md body."""
    links = re.findall(r'\[([^\]]*)\]\(([^)]*)\)', body_text)
    refs = []
    for label, target in links:
        if target.startswith("http"):
            continue
        refs.append({"label": label, "target": target})
    return refs


def read_body(filepath):
    """Read SKILL.md body (content after frontmatter)."""
    if not os.path.exists(filepath):
        return ""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return content
    parts = content.split("---", 2)
    return parts[2] if len(parts) >= 3 else ""


def estimate_tokens(text):
    """Rough token estimate: words * 1.3 for English."""
    words = len(text.split())
    return int(words * 1.3)


def assess_skill(name, fields, skill_dir, body):
    """Apply health rules. Returns list of markers."""
    markers = []

    # Check required files
    skill_md = os.path.join(skill_dir, "SKILL.md")
    openai_yaml = os.path.join(skill_dir, "agents", "openai.yaml")

    if not os.path.exists(skill_md):
        markers.append({"skill": name, "level": "unstable",
                        "reason": "SKILL.md missing"})
        return markers

    if not os.path.exists(openai_yaml):
        markers.append({"skill": name, "level": "stale",
                        "reason": "agents/openai.yaml missing"})

    # Check review_by expiration
    review_by = fields.get("review_by", "")
    if review_by:
        try:
            review_date = datetime.strptime(review_by, "%Y-%m-%d")
            if review_date < datetime.now():
                markers.append({"skill": name, "level": "review",
                                "reason": f"review_by expired: {review_by}"})
        except ValueError:
            markers.append({"skill": name, "level": "stale",
                            "reason": f"review_by invalid format: {review_by}"})

    # Check cross-references
    refs = extract_cross_references(body)
    broken = []
    for ref in refs:
        target = ref["target"]
        # Remove anchors
        target_path = target.split("#")[0]
        if not target_path:
            continue
        full_path = os.path.normpath(os.path.join(skill_dir, target_path))
        if not os.path.exists(full_path):
            broken.append(target)

    if broken:
        markers.append({"skill": name, "level": "stale",
                        "reason": f"{len(broken)} broken cross-references",
                        "detail": broken})

    # Check token budget (hard fail)
    tokens = estimate_tokens(body)
    if tokens > 5000:
        markers.append({"skill": name, "level": "unstable",
                        "reason": f"body exceeds 5000 token budget (~{tokens}t) — must reduce"})

    # Check status
    status = fields.get("status", "")
    if status == "deprecated":
        markers.append({"skill": name, "level": "dormant",
                        "reason": "marked as deprecated"})
    elif status == "superseded":
        markers.append({"skill": name, "level": "dormant",
                        "reason": "marked as superseded"})
    elif status == "draft":
        markers.append({"skill": name, "level": "dormant",
                        "reason": "still in draft status"})

    # Check for forbidden fields in frontmatter
    with open(skill_md, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return markers
    fm_text = content.split("---", 2)[1] if len(content.split("---", 2)) >= 3 else ""

    forbidden = ["composes:", "composed_by:", "context_budget:", "trust_level:",
                 "requires_network:", "requires_file_write:", "compatibility:",
                 "allowed_tools:", "evolution:", "author:", "created_by:",
                 "maintained_by:", "generated_by:", "contact:"]
    found_forbidden = [f for f in forbidden if f in fm_text]
    if found_forbidden:
        markers.append({"skill": name, "level": "stale",
                        "reason": f"forbidden fields found: {found_forbidden}"})

    return markers


def scan_skills(skills_dir, target_skill=None):
    """Scan all skill directories and return health report."""
    all_markers = []
    skill_summaries = []

    for item in os.listdir(skills_dir):
        skill_dir = os.path.join(skills_dir, item)
        if not os.path.isdir(skill_dir):
            continue

        skill_md = os.path.join(skill_dir, "SKILL.md")
        if not os.path.exists(skill_md):
            continue

        if target_skill and item != target_skill:
            continue

        fields = parse_frontmatter(skill_md)
        body = read_body(skill_md)
        markers = assess_skill(item, fields, skill_dir, body)

        if markers:
            all_markers.extend(markers)

        tokens = estimate_tokens(body)
        skill_summaries.append({
            "name": item,
            "status": fields.get("status", "unknown"),
            "version": fields.get("version", "?"),
            "review_by": fields.get("review_by", ""),
            "tokens": tokens,
            "issues": len(markers),
        })

    return skill_summaries, all_markers


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Tier 2 — Skill health offline scanner")
    parser.add_argument("skills_dir", help="Path to skills/ directory")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--skill", help="Check only specified skill")
    args = parser.parse_args()

    summaries, markers = scan_skills(args.skills_dir, args.skill)

    if args.json:
        print(json.dumps({
            "scan_time": datetime.now().isoformat(),
            "skills_scanned": len(summaries),
            "summaries": summaries,
            "markers": [m for m in markers]
        }, ensure_ascii=False, indent=2))
        return

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"=== Skill Health Report ({now}) ===")
    print(f"Skills scanned: {len(summaries)}\n")

    print(f"{'Skill':<25} {'Status':>10} {'Version':>8} {'Tokens':>7} {'Issues':>7}")
    print("-" * 60)
    for s in summaries:
        print(f"{s['name']:<25} {s['status']:>10} {s['version']:>8} {s['tokens']:>7} {s['issues']:>7}")

    if not markers:
        print("\n[OK] No issues found. All skills healthy.")
        return

    for level, label in [
        ("unstable", "[FAIL] Unstable"),
        ("stale", "[WARN] Stale"),
        ("review", "[WARN] Needs Review"),
        ("dormant", "[INFO] Dormant"),
    ]:
        ms = [m for m in markers if m["level"] == level]
        if not ms:
            continue
        print(f"\n--- {label} ---")
        for m in ms:
            print(f"  [{m['skill']}] {m['reason']}")
            if m.get("detail"):
                for d in m["detail"]:
                    print(f"    - {d}")

    review_needed = [m for m in markers if m["level"] in ("unstable", "stale", "review")]
    if review_needed:
        print(f"\n---")
        print(f"{len(review_needed)} issue(s) need attention.")


if __name__ == "__main__":
    main()
