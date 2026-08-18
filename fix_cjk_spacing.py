#!/usr/bin/env python3
"""Fix CJK fonts, line-height, and spacing across all 20 templates."""
import os, re

# Categorize templates
SANS_TEMPLATES = [
    '01-systems', '03-soft-space', '04-light-as-air', '05-breathe',
    '08-brutal', '09-neon', '10-pop', '11-electric', '12-memphis',
    '13-punk', '14-tropic'
]
SERIF_TEMPLATES = [
    '06-essential', '07-noir', '18-nouveau', '19-deco'
]
# These already have CJK fonts: 02-sei, 15-mineral-strata, 16-iron-line-halo, 17-cobalt-circles, 20-ukiyo-e

CJK_SANS = "'Noto Sans SC'"
CJK_SERIF = "'Noto Serif SC'"
CJK_SANS_WEIGHTS = "400;500;700;900"
CJK_SERIF_WEIGHTS = "400;500;700;900"

def fix_template(name):
    path = f'templates/{name}/example.html'
    with open(path) as f:
        html = f.read()
    
    is_sans = name in SANS_TEMPLATES
    is_serif = name in SERIF_TEMPLATES
    cjk_font = CJK_SANS if is_sans else CJK_SERIF
    cjk_url_name = 'Noto+Sans+SC' if is_sans else 'Noto+Serif+SC'
    cjk_weights = CJK_SANS_WEIGHTS if is_sans else CJK_SERIF_WEIGHTS
    
    # 1. Add CJK font to Google Fonts URL (only for templates that don't already have it)
    if is_sans or is_serif:
        # Check if Noto Sans/Serif SC is already imported
        if cjk_url_name.replace('+', ' ') not in html and 'Noto Sans SC' not in html and 'Noto Serif SC' not in html:
            # Add before &display=swap
            html = html.replace(
                '&display=swap',
                f'&family={cjk_url_name}:wght@{cjk_weights}&display=swap'
            )
    
    # 2. Update font-family stacks to include CJK font
    if is_sans or is_serif:
        # Add CJK font after the primary font in font-family declarations
        # Pattern: 'Font Name', ... -> 'Font Name', 'Noto Sans SC', ...
        # Don't add if already present
        def add_cjk_to_fontfamily(match):
            prefix = match.group(1)  # e.g. font: or --font-sans:
            family = match.group(2)  # the font list
            if 'Noto Sans SC' in family or 'Noto Serif SC' in family or 'Noto Serif JP' in family:
                return match.group(0)
            # Add CJK font after the first quoted font name
            family = re.sub(
                r"('[^']+'|\"[^\"]+\")",
                lambda m: f"{m.group(1)}, {cjk_font}" if m.start() == 0 else m.group(0),
                family,
                count=1
            )
            return f'{prefix}{family}'
        
        # Match font-family: ... and --font-xxx: ...
        html = re.sub(
            r'((?:font-family|--font[\w-]*)\s*:\s*)([^;]+);',
            add_cjk_to_fontfamily,
            html
        )
    
    # 3. Fix h1 line-height (minimum 1.15 for CJK)
    def fix_h1_lineheight(match):
        rule = match.group(0)
        lh_match = re.search(r'line-height:\s*([\d.]+)', rule)
        if lh_match:
            lh = float(lh_match.group(1))
            if lh < 1.15:
                rule = rule[:lh_match.start(1)] + '1.15' + rule[lh_match.end(1):]
        return rule
    
    html = re.sub(r'h1\s*\{[^}]+\}', fix_h1_lineheight, html)
    # Also handle .title-slide h1
    html = re.sub(r'\.title-slide\s+h1\s*\{[^}]+\}', fix_h1_lineheight, html)
    
    # 4. Fix h2 line-height (minimum 1.15)
    def fix_h2_lineheight(match):
        rule = match.group(0)
        lh_match = re.search(r'line-height:\s*([\d.]+)', rule)
        if lh_match:
            lh = float(lh_match.group(1))
            if lh < 1.15:
                rule = rule[:lh_match.start(1)] + '1.15' + rule[lh_match.end(1):]
        return rule
    
    html = re.sub(r'h2\s*\{[^}]+\}', fix_h2_lineheight, html)
    html = re.sub(r'\.content-slide\s+h2\s*\{[^}]+\}', fix_h2_lineheight, html)
    html = re.sub(r'\.two-col\s+h2\s*\{[^}]+\}', fix_h2_lineheight, html)
    html = re.sub(r'\.data-slide\s+h2\s*\{[^}]+\}', fix_h2_lineheight, html)
    html = re.sub(r'\.section-slide\s+h2\s*\{[^}]+\}', fix_h2_lineheight, html)
    
    # 5. Fix specific layout issues
    if name == '13-punk':
        # Punk content slide: body uses 1fr 2fr grid, but lead is removed
        # Make it single column
        html = html.replace(
            '.content-slide .body { display: grid; grid-template-columns: 1fr 2fr; gap: 48px; flex: 1; }',
            '.content-slide .body { display: block; flex: 1; }'
        )
    
    # 6. Add global spacing improvements via injected CSS
    spacing_css = """
    /* CJK readability fixes */
    h1, h2, h3, h4 { line-height: 1.2; }
    .title-slide h1 { line-height: 1.18; font-weight: 900; }
    .section-slide h2 { font-weight: 900; }
    .content-slide h2, .two-col h2, .data-slide h2 { font-weight: 900; }
    .content-slide .header, .two-col .header, .data-slide .header { margin-bottom: 40px; }
    .content-slide .body { gap: 32px; }
    .two-col .cols { gap: 32px; }
    .data-slide .metrics { gap: 24px; }
    .content-slide ul { gap: 4px; }
    .content-slide li { padding: 20px 0; }
    .two-col .col { padding: 36px 40px; }
    .data-slide .metric { padding: 32px 28px; }
    .content-slide .card, .two-col .col { margin-bottom: 0; }
    """
    html = html.replace('</style>', spacing_css + '\n</style>')
    
    with open(path, 'w') as f:
        f.write(html)
    
    print(f'Fixed {name}')

# Fix all templates
for d in sorted(os.listdir('templates')):
    if os.path.isfile(f'templates/{d}/example.html'):
        fix_template(d)

print('\nAll templates fixed.')
