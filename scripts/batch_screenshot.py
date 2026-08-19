#!/usr/bin/env python3
"""Batch screenshot all templates - page 1 (cover) and page 5 (section 02)."""
import os, subprocess, re
from bs4 import BeautifulSoup

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
OUT_DIR = '/tmp/progress-check'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

os.makedirs(OUT_DIR, exist_ok=True)

templates = sorted([d for d in os.listdir(TEMPLATES_DIR) if os.path.isdir(os.path.join(TEMPLATES_DIR, d))])

for name in templates:
    html_path = os.path.join(TEMPLATES_DIR, name, 'example.html')
    if not os.path.exists(html_path):
        continue

    with open(html_path) as f:
        html = f.read()

    # Page 1 (cover) - use as-is (first slide is active)
    for page_idx, page_name in [(0, 'p1'), (4, 'p5')]:
        soup = BeautifulSoup(html, 'html.parser')
        slides = soup.find_all('section', class_='slide')
        for i, s in enumerate(slides):
            if i == page_idx:
                s['class'] = [c for c in s.get('class', []) if c != 'active'] + ['active']
            else:
                s['class'] = [c for c in s.get('class', []) if c != 'active']

        tmp_path = f'/tmp/{name}_{page_name}.html'
        with open(tmp_path, 'w') as f:
            f.write(str(soup))

        out_png = os.path.join(OUT_DIR, f'{name}_{page_name}.png')
        subprocess.run([
            CHROME, '--headless', '--disable-gpu',
            f'--screenshot={out_png}',
            '--window-size=1280,720',
            '--force-device-scale-factor=2',
            '--hide-scrollbars',
            f'file://{tmp_path}'
        ], capture_output=True, timeout=15)
        print(f'  {name} {page_name}')

print('Done')
