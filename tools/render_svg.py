"""Пересобирает PNG из SVG-исходников схем в images/.

Схемы рисуются в SVG, в документах используется PNG рядом с исходником.
Скрипт открывает каждый SVG в headless Chrome или Edge и сохраняет снимок
того же размера.

    python tools/render_svg.py                       # все SVG в images/
    python tools/render_svg.py images/project/X.svg  # отдельные файлы

Путь к браузеру можно задать переменной окружения CHROME.
"""
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BROWSERS = [
    os.environ.get('CHROME', ''),
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
    '/usr/bin/google-chrome',
    '/usr/bin/chromium',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
]


def find_browser():
    for b in BROWSERS:
        if b and Path(b).exists():
            return b
    sys.exit('Не найден Chrome или Edge. Укажите путь в переменной CHROME.')


def size(svg_text):
    m = re.search(r'<svg[^>]*\bwidth="(\d+)"[^>]*\bheight="(\d+)"', svg_text)
    if not m:
        sys.exit('У корневого <svg> должны быть атрибуты width и height в пикселях.')
    return int(m.group(1)), int(m.group(2))


def render(browser, svg_path):
    svg_text = svg_path.read_text(encoding='utf-8')
    w, h = size(svg_text)
    png_path = svg_path.with_suffix('.png')
    html = ('<!doctype html><html><head><meta charset="utf-8">'
            '<style>html,body{margin:0;padding:0;background:#fff}</style>'
            '</head><body>' + svg_text + '</body></html>')
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / 'page.html'
        page.write_text(html, encoding='utf-8')
        subprocess.run([
            browser, '--headless=new', '--disable-gpu', '--hide-scrollbars',
            '--force-device-scale-factor=1', f'--window-size={w},{h}',
            f'--screenshot={png_path}', page.as_uri(),
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f'{png_path.relative_to(ROOT)}  {w}x{h}')


def main():
    browser = find_browser()
    files = [Path(a).resolve() for a in sys.argv[1:]] or sorted((ROOT / 'images').rglob('*.svg'))
    for f in files:
        render(browser, f)


if __name__ == '__main__':
    main()
