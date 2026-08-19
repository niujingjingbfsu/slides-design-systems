#!/usr/bin/env python3
"""
Fix missing CSS semicolons across all templates.

The bug: many declarations were written as:
  font-family: var(--font-display) font-size: 48px;
The missing semicolon between var(...) and font-size causes the browser
to parse both as one invalid font-family value, dropping font-size too.

This script finds all such patterns and inserts the missing semicolons.
Also fixes:
- Missing semicolons after custom property declarations (--font-display: ...)
- Missing semicolons in html, body { ... font-family: var(...) overflow: hidden }
- Replaces Fredoka with Outfit in 14-tropic for better CJK coordination
- Adds margin-bottom to cards/cols/metrics containers for footer spacing
"""
import re, os

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates')

def fix_missing_semicolons(css_text):
    """Fix missing semicolons between CSS declarations on the same line."""
    # Pattern: after var(--xxx) or a value, followed by a property name and colon
    # e.g. "var(--font-display) font-size: 48px" -> "var(--font-display); font-size: 48px"
    # e.g. "sans-serif\n    --font-body:" -> "sans-serif;\n    --font-body:"
    
    # Fix 1: Missing semicolon after var(...) before next property
    # Match: var(--xxx) followed by space and a property name:
    css_text = re.sub(
        r'(var\(--[a-z-]+\))\s+([a-z-]+\s*:)',
        r'\1; \2',
        css_text
    )
    
    # Fix 2: Missing semicolon after a value (like sans-serif, #fff, 48px, etc.)
    # before a property name on the same line, but NOT inside var() or url()
    # This handles cases like: "sans-serif text-transform: uppercase"
    # or "#fff font-size: 22px" or "40px margin-bottom: 12px"
    css_text = re.sub(
        r'([;{}]\s*[a-z-]+\s*:\s*[^;{}]+?)\s+([a-z-]+\s*:)',
        lambda m: m.group(1) + '; ' + m.group(2) if not m.group(1).rstrip().endswith(';') else m.group(0),
        css_text
    )
    
    # Fix 3: Custom properties missing trailing semicolon before next custom property
    # e.g. "--font-display: 'Fredoka', sans-serif\n    --font-body:"
    def fix_custom_props(text):
        lines = text.split('\n')
        result = []
        for i, line in enumerate(lines):
            stripped = line.strip()
            # Check if this is a custom property line without trailing semicolon
            if re.match(r'--[a-z-]+\s*:', stripped) and not stripped.rstrip().endswith(';') and not stripped.rstrip().endswith('{'):
                # Check if next non-empty line looks like another property or closing brace
                line = line.rstrip() + ';'
            result.append(line)
        return '\n'.join(result)
    
    css_text = fix_custom_props(css_text)
    
    # Fix 4: "font-family: var(--xxx) overflow: hidden" pattern
    # Already handled by Fix 1, but let's also catch non-var patterns
    # e.g. "font-family: sans-serif overflow: hidden"
    css_text = re.sub(
        r'(font-family\s*:\s*[^;{}]+?)\s+(overflow\s*:)',
        r'\1; \2',
        css_text
    )
    
    return css_text

def fix_tropic_font(html):
    """Replace Fredoka with Outfit for better CJK coordination in Tropic."""
    # Update Google Fonts URL: replace Fredoka with Outfit
    html = html.replace(
        'family=Fredoka:wght@400;600;700&family=Inter:wght@400;600;800&family=Noto+Sans+SC',
        'family=Outfit:wght@400;500;600;700;800&family=Inter:wght@400;600;800&family=Noto+Sans+SC'
    )
    # Update font variable
    html = html.replace(
        "--font-display: 'Fredoka', 'Noto Sans SC', sans-serif",
        "--font-display: 'Outfit', 'Noto Sans SC', sans-serif"
    )
    return html

def add_footer_spacing(html):
    """Add margin/padding between content and footer in flex layouts."""
    # Add a global rule: footer gets margin-top: 24px (in addition to auto)
    # This creates a gap between the last content element and the footer
    if '/* Footer spacing fix */' not in html:
        spacing_css = """
  /* Footer spacing fix */
  .slide > .footer { margin-top: 24px; flex-shrink: 0; }
  .slide > .cards, .slide > .cols, .slide > .metrics, .slide > .body { flex-shrink: 1; min-height: 0; }
"""
        html = html.replace('</style>', spacing_css + '\n</style>', 1)
    return html

def main():
    for name in sorted(os.listdir(TEMPLATES_DIR)):
        path = os.path.join(TEMPLATES_DIR, name, 'example.html')
        if not os.path.isfile(path):
            continue
        
        with open(path, 'r') as f:
            html = f.read()
        
        original = html
        
        # Fix missing semicolons
        html = fix_missing_semicolons(html)
        
        # Template-specific fixes
        if name == '14-tropic':
            html = fix_tropic_font(html)
        
        # Add footer spacing to all templates
        html = add_footer_spacing(html)
        
        if html != original:
            with open(path, 'w') as f:
                f.write(html)
            print(f'Fixed {name}')
        else:
            print(f'No changes needed for {name}')

if __name__ == '__main__':
    main()
