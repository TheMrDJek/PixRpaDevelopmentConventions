"""Пересобирает содержание в каждом файле docs/ и реестр правил docs/rules-index.md.

Запуск из корня репозитория:  python tools/build_docs.py
Проверка без записи (для CI):  python tools/build_docs.py --check
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
INDEX = os.path.join(DOCS, "rules-index.md")
RULE = re.compile(r"^## ([A-Z]+-\d+)\. (.+)$")
LEVEL = re.compile(r"^\*\*Уровень:\*\* (MUST|SHOULD|MAY)\b")
SECTIONS = [
    ("01-conventions", "Соглашения"),
    ("02-guidelines", "Рекомендации по написанию скриптов"),
    ("03-robot-lifecycle", "Жизненный цикл робота"),
    ("04-master", "PIX Master"),
]


def slug(title, seen):
    """Якорь заголовка по правилам GitHub."""
    s = re.sub(r"[^\w\- ]", "", title.strip().lower()).replace(" ", "-")
    n = seen.get(s, 0)
    seen[s] = n + 1
    return s if n == 0 else f"{s}-{n}"


def code_mask(lines):
    mask, in_code = [], False
    for line in lines:
        if line.strip().startswith("```"):
            mask.append(True)
            in_code = not in_code
            continue
        mask.append(in_code)
    return mask


def parse(path):
    """Возвращает (заголовки уровня 2 с якорями, правила)."""
    lines = open(path, encoding="utf-8").read().split("\n")
    mask = code_mask(lines)
    seen, headings, rules = {}, [], []
    for i, line in enumerate(lines):
        if mask[i]:
            continue
        m = re.match(r"^(#{1,6}) (.*)$", line)
        if not m:
            continue
        anchor = slug(m.group(2), seen)
        if len(m.group(1)) != 2 or m.group(2) == "Содержание":
            continue
        level = None
        rm = RULE.match(line)
        if rm:
            for nxt in lines[i + 1:i + 4]:
                lm = LEVEL.match(nxt)
                if lm:
                    level = lm.group(1)
                    break
            if not level:
                sys.exit(f"{path}: у правила {rm.group(1)} нет строки «**Уровень:**»")
            rules.append((rm.group(1), rm.group(2), level, anchor))
        headings.append((m.group(2), anchor, level))
    return headings, rules


def build_toc(path):
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"\n## Содержание\n.*?(?=\n## )", "", text, flags=re.S)
    tmp = path + ".tmp"
    open(tmp, "w", encoding="utf-8", newline="\n").write(text)
    headings, rules = parse(tmp)
    os.remove(tmp)
    if not headings:
        return text, rules
    toc = ["## Содержание", ""]
    for title, anchor, level in headings:
        toc.append(f"- [{title}](#{anchor})" + (f" — {level}" if level else ""))
    lines = text.split("\n")
    mask = code_mask(lines)
    first = next(i for i, l in enumerate(lines) if not mask[i] and l.startswith("## "))
    lines[first:first] = toc + [""]
    return "\n".join(lines), rules


def build_index(all_rules):
    out = [
        "# Реестр правил",
        "",
        "Сводный список всех правил с идентификаторами и уровнями обязательности. "
        "Уровни описаны в [README](../README.md#уровни-обязательности).",
        "",
        "Ссылайтесь на правило по идентификатору, например в комментарии к Pull Request: «нарушено EXC-03».",
        "",
        "> Файл генерируется командой `python tools/build_docs.py`. Не редактируйте его вручную.",
        "",
    ]
    for folder, title in SECTIONS:
        rows = [r for r in all_rules if r[0].startswith(folder + "/")]
        if not rows:
            continue
        out += [f"## {title}", "", "| ID | Уровень | Правило | Раздел |", "|----|---------|---------|--------|"]
        for rel, section, rid, name, level, anchor in rows:
            out.append(f"| {rid} | {level} | [{name}]({rel}#{anchor}) | [{section}]({rel}) |")
        out.append("")
    return "\n".join(out)


def main():
    check = "--check" in sys.argv
    changed, all_rules, ids = [], [], {}
    files = sorted(p for p in glob.glob(os.path.join(DOCS, "**", "*.md"), recursive=True) if p != INDEX)
    for path in files:
        rel = os.path.relpath(path, DOCS).replace("\\", "/")
        text, rules = build_toc(path)
        text = re.sub(r"\n{3,}", "\n\n", text).rstrip("\n") + "\n"
        section = text.split("\n", 1)[0].lstrip("# ").strip()
        for rid, name, level, anchor in rules:
            if rid in ids:
                sys.exit(f"Идентификатор {rid} повторяется: {ids[rid]} и {rel}")
            ids[rid] = rel
            all_rules.append((rel, section, rid, name, level, anchor))
        if open(path, encoding="utf-8").read() != text:
            changed.append(rel)
            if not check:
                open(path, "w", encoding="utf-8", newline="\n").write(text)
    index = build_index(all_rules)
    if not os.path.exists(INDEX) or open(INDEX, encoding="utf-8").read() != index:
        changed.append("rules-index.md")
        if not check:
            open(INDEX, "w", encoding="utf-8", newline="\n").write(index)
    if check and changed:
        sys.exit("Содержание или реестр устарели, запустите python tools/build_docs.py:\n  " + "\n  ".join(changed))
    print(f"Правил: {len(all_rules)}. Обновлено файлов: {len(changed)}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
