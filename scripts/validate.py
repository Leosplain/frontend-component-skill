#!/usr/bin/env python3
"""Check repository integrity without third-party dependencies.

Checks local inline Markdown links (not remote URLs or fragment anchors).
The core skill checksum records the reviewed SKILL.md bytes.
"""
import hashlib
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ".agents/skills/frontend-component/SKILL.md"
REQUIRED = (
    "README.md", "README.zh-TW.md", "LICENSE", "CONTRIBUTING.md",
    "docs/README.md", "docs/installation.md", "docs/examples.md", SKILL,
    ".agents/skills/frontend-component/agents/openai.yaml",
    ".agents/skills/frontend-component/references/design-notes.md",
    "scripts/skill.sha256", ".github/workflows/validate.yml",
)


def main():
    errors = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f"Missing required file: {name}")

    manifest = ROOT / "scripts/skill.sha256"
    skill = ROOT / SKILL
    if manifest.is_file() and skill.is_file():
        fields = manifest.read_text(encoding="utf-8").strip().split()
        if len(fields) != 2 or not re.fullmatch(r"[0-9a-f]{64}", fields[0]) or fields[1] != SKILL:
            errors.append("Invalid skill checksum manifest")
        elif hashlib.sha256(skill.read_bytes()).hexdigest() != fields[0]:
            errors.append("SKILL.md differs from the recorded checksum; review changes before updating the manifest")

    count = 0
    for doc in sorted(ROOT.rglob("*.md")):
        if ".git" in doc.relative_to(ROOT).parts:
            continue
        count += 1
        try:
            content = doc.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(f"Invalid UTF-8: {doc.relative_to(ROOT)}")
            continue
        # Ignore fenced examples and inline code before checking actual links.
        content = re.sub(r"^(`{3,}|~{3,})[^\n]*\n.*?^\1[^\n]*(?:\n|$)", "", content, flags=re.M | re.S)
        content = re.sub(r"`[^`\n]+`", "", content)
        for raw in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", content):
            target = raw.strip().split()[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (doc.parent / unquote(parsed.path)).resolve()
            try:
                destination.relative_to(ROOT)
            except ValueError:
                errors.append(f"Link leaves repository: {doc.relative_to(ROOT)} -> {target}")
                continue
            if not destination.exists():
                errors.append(f"Broken local link: {doc.relative_to(ROOT)} -> {target}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(REQUIRED)} required files, {count} Markdown files, local link targets, recorded SKILL.md checksum")
    print("Remote URLs, fragment anchors, and generated frontend behavior are not checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
