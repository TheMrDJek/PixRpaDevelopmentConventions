"""Выгружает листы images/diagrams.drawio в PNG.

Все схемы лежат листами одного файла draw.io. Имя листа задает, куда идет
картинка: лист «template / TEMPLATE-02-states» выгружается в
images/template/TEMPLATE-02-states.png.

    python tools/export_diagrams.py              # все листы
    python tools/export_diagrams.py template     # листы, чье имя начинается с этой строки

Нужен draw.io Desktop. Путь к нему можно задать переменной окружения DRAWIO.
"""
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'images' / 'diagrams.drawio'

CANDIDATES = [
    os.environ.get('DRAWIO', ''),
    r'C:\Program Files\draw.io\draw.io.exe',
    os.path.expandvars(r'%LOCALAPPDATA%\Programs\draw.io\draw.io.exe'),
    '/Applications/draw.io.app/Contents/MacOS/draw.io',
    '/usr/bin/drawio',
    '/opt/drawio/drawio',
]


def find_drawio():
    for c in CANDIDATES:
        if c and Path(c).exists():
            return c
    sys.exit('Не найден draw.io Desktop. Укажите путь в переменной DRAWIO.')


def pages():
    text = SOURCE.read_text(encoding='utf-8')
    names = [unescape(n) for n in re.findall(r'<diagram\b[^>]*\bname="([^"]*)"', text)]
    for i, name in enumerate(names, 1):
        section, sep, stem = name.partition(' / ')
        if not sep:
            sys.exit(f'Лист «{name}»: имя должно быть вида «<раздел> / <файл>».')
        yield i, name, ROOT / 'images' / section / f'{stem}.png'


def export(drawio, index, out):
    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([drawio, '--export', '--format', 'png', '--page-index', str(index), '--border', '10',
                    '--output', str(out), str(SOURCE)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return out


def main(prefixes):
    drawio = find_drawio()
    todo = [(i, out) for i, name, out in pages() if not prefixes or name.startswith(tuple(prefixes))]
    if not todo:
        sys.exit('Нет листов с таким началом имени.')
    with ThreadPoolExecutor(max_workers=4) as pool:
        for out in pool.map(lambda j: export(drawio, *j), todo):
            print(out.relative_to(ROOT).as_posix())


if __name__ == '__main__':
    main(sys.argv[1:])
