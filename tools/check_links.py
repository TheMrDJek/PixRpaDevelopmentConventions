"""Проверяет относительные ссылки и якоря во всех .md файлах репозитория.

Запуск из корня репозитория:  python tools/check_links.py
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_docs import code_mask, slug  # noqa: E402


def anchors(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    mask = code_mask(lines)
    seen, result = {}, set()
    for i, line in enumerate(lines):
        m = re.match(r"^#{1,6} (.*)$", line)
        if m and not mask[i]:
            result.add(slug(m.group(1), seen))
    return result


def main():
    os.chdir(ROOT)
    broken = []
    for path in glob.glob("**/*.md", recursive=True):
        text = re.sub(r"```.*?```", "", open(path, encoding="utf-8").read(), flags=re.S)
        text = re.sub(r"`[^`\n]*`", "", text)  # примеры в инлайн-коде
        for m in re.finditer(r"\]\(([^)\s]+)\)", text):
            link = m.group(1)
            if re.match(r"^(https?:|mailto:)", link):
                continue
            target_path, _, anchor = link.partition("#")
            target = os.path.normpath(os.path.join(os.path.dirname(path), target_path)) if target_path else path
            if not os.path.exists(target):
                broken.append(f"{path}: нет файла {link}")
            elif anchor and target.endswith(".md") and anchor not in anchors(target):
                broken.append(f"{path}: нет якоря {link}")
    for b in broken:
        print(b)
    print(f"Битых ссылок: {len(broken)}")
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
