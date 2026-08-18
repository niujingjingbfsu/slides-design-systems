#!/usr/bin/env python3
"""
Add overflow safeguards to all templates and fix 15-mineral-strata footer overlap.

Safeguards added to every template:
1. box-sizing: border-box on all elements
2. min-height: 0 on flex children that contain grids/cards (prevents flex overflow)
3. overflow: hidden on content containers (safety net against clipping)
4. overflow-wrap: break-word on text (prevents long unbroken text from overflowing)
5. Fix 15-mineral-strata content-area padding-bottom to account for 100px footer
"""
import os, re

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates')

SAFEGUARD_CSS = """
  /* === Content overflow safeguards === */
  *, *::before, *::after { box-sizing: border-box; }
  .slide > * { min-width: 0; min-height: 0; }
  .slide .body, .slide .cols, .slide .cards, .slide .metrics,
  .slide .content-area, .slide .content, .slide .grid { min-height: 0; }
  .slide .card, .slide .col, .slide .metric { overflow: hidden; }
  .slide p, .slide li, .slide h1, .slide h2, .slide h3, .slide h4,
  .slide blockquote, .slide span, .slide div {
    overflow-wrap: break-word; word-break: break-word;
  }
"""

def fix_mineral_strata(html):
    """Fix 15-mineral-strata: content-area needs padding-bottom >= 100px footer + gap."""
    # Base content-area: padding: 56px 80px -> padding: 56px 80px 110px
    html = html.replace(
        '.content-area { position: relative; z-index: 2; padding: 56px 80px; flex: 1; display: flex; flex-direction: column; }',
        '.content-area { position: relative; z-index: 2; padding: 56px 80px 110px; flex: 1; display: flex; flex-direction: column; overflow: hidden; }'
    )
    # content-slide: padding: 72px 80px 72px -> padding: 72px 80px 110px
    html = html.replace(
        '.content-slide .content-area { padding: 72px 80px 72px; }',
        '.content-slide .content-area { padding: 72px 80px 110px; }'
    )
    # two-col: padding: 72px 80px 72px -> padding: 72px 80px 110px
    html = html.replace(
        '.two-col .content-area { padding: 72px 80px 72px; }',
        '.two-col .content-area { padding: 72px 80px 110px; }'
    )
    # data-slide: padding: 72px 80px 72px -> padding: 72px 80px 110px
    html = html.replace(
        '.data-slide .content-area { padding: 72px 80px 72px; }',
        '.data-slide .content-area { padding: 72px 80px 110px; }'
    )
    return html

def fix_cobalt_circles(html):
    """Fix 17-cobalt-circles: footer at bottom:32px with 32px height = needs 64px+ gap."""
    # Base content-area: padding: 56px 80px -> padding: 56px 80px 72px
    html = html.replace(
        '.content-area { position: relative; z-index: 2; padding: 56px 80px; flex: 1; display: flex; flex-direction: column; }',
        '.content-area { position: relative; z-index: 2; padding: 56px 80px 72px; flex: 1; display: flex; flex-direction: column; overflow: hidden; }'
    )
    return html

def fix_iron_line_halo(html):
    """Fix 16-iron-line-halo: add overflow:hidden to content-area."""
    html = html.replace(
        '.content-area { position: relative; z-index: 2; padding: 56px 80px; flex: 1; display: flex; flex-direction: column; margin-top: 16px; margin-bottom: 16px; }',
        '.content-area { position: relative; z-index: 2; padding: 56px 80px; flex: 1; display: flex; flex-direction: column; margin-top: 16px; margin-bottom: 16px; overflow: hidden; }'
    )
    return html

def add_safeguards(html):
    """Add safeguard CSS before </style>."""
    if 'Content overflow safeguards' in html:
        return html  # Already added
    
    # Add safeguards right before the closing </style> tag
    html = html.replace('</style>', SAFEGUARD_CSS + '\n</style>', 1)
    return html

def main():
    for name in sorted(os.listdir(TEMPLATES_DIR)):
        path = os.path.join(TEMPLATES_DIR, name, 'example.html')
        if not os.path.isfile(path):
            continue
        
        with open(path, 'r') as f:
            html = f.read()
        
        original = html
        
        # Add global safeguards
        html = add_safeguards(html)
        
        # Template-specific fixes
        if name == '15-mineral-strata':
            html = fix_mineral_strata(html)
        elif name == '16-iron-line-halo':
            html = fix_iron_line_halo(html)
        elif name == '17-cobalt-circles':
            html = fix_cobalt_circles(html)
        
        if html != original:
            with open(path, 'w') as f:
                f.write(html)
            print(f'Fixed {name}')
        else:
            print(f'No changes needed for {name}')

if __name__ == '__main__':
    main()
