#!/usr/bin/env python3
"""Generate 20 themed versions of the Feishu Agent presentation."""
from bs4 import BeautifulSoup, NavigableString, Tag
import os, re, copy

CONTENT = {
    'title': {
        'tag': 'FEISHU · AGENT IN MEETING',
        'h1': '聊着天，<br>把活干了',
        'subtitle': '在飞书会议里，边聊边干，是一种怎样的体验？',
        'meta': ['飞书 AI Friendly', '产品经理 · 晶泾', '客户共创 · 2026'],
    },
    'section': {
        'label': '01 · 框架',
        'h2': '先看一个框架',
        'bignum': '02',
    },
    'content': {
        'eyebrow': 'THREE LEVELS',
        'h2': '会议里和 AI 协同，有三个 Level',
        'lead': '',  # no lead paragraph
        'cards': [
            {'tag': 'LEVEL 1', 'h3': '会后总结', 'p': '开完会后，AI 总结纪要和待办——人类处理待办'},
            {'tag': 'LEVEL 2', 'h3': 'Agent 代办', 'p': '开完会后，Agent 总结纪要和待办——Agent 主动处理待办'},
            {'tag': 'LEVEL 3', 'h3': '边聊边干', 'p': 'Agent 加入会议，会上直接处理待办——边聊边干'},
        ],
    },
    'twocol': {
        'eyebrow': 'LEVEL 3 是什么感觉',
        'h2': '不用等会开完',
        'cols': [
            {'tag': '01', 'h3': '提问，秒答', 'p': '数据、进展、结论，问出口的瞬间就有答案', 'spec': ''},
            {'tag': '02', 'h3': '说需求，秒执行', 'p': '一句话交代清楚，Agent 会上就动手', 'spec': ''},
        ],
    },
    'quote': {
        'blockquote': '找一个舒服漂亮的地方，喝着咖啡，聊着天，让想法碰撞出火花，剩下的，交给 Agent。',
        'cite': '未来的工作方式 · 2026',
    },
    'data': {
        'eyebrow': '03 · 实录',
        'h2': '边聊边干，长这样',
        'metrics': [
            {'tag': '销售额', 'value': '5.6', 'unit': '万元', 'label': '华东地区 7 月销售额，风衣类卖得最好'},
            {'tag': '交付', 'value': '分钟', 'unit': '级', 'label': '全国销售数据 HTML 报表，会还没开完已上线'},
            {'tag': '跳出', 'value': '0', 'unit': '次', 'label': 'JD 全文直接贴进会中弹幕，当场就能读'},
            {'tag': '跃迁', 'value': '3', 'unit': 'Level', 'label': '从会后排待办到会上直接执行，三级跃迁'},
        ],
    },
    'closing': {
        'h2': '想体验<br>Level 3?',
        'p': '用飞书扫码加入「智能体会」早鸟体验群',
        'btn': '立即体验',
    },
}

def set_inner_html(el, html):
    """Replace element's inner HTML."""
    if el is None:
        return
    el.clear()
    # Parse fragment and append children individually
    fragment = BeautifulSoup(f'<div>{html}</div>', 'html.parser').find('div')
    for child in list(fragment.children):
        el.append(child)

def set_text(el, text):
    """Set element text, preserving no children."""
    if el is None:
        return
    el.string = text

def find_by_class(section, patterns):
    for pat in patterns:
        for el in section.find_all(class_=re.compile(pat, re.I)):
            # Skip elements inside footer
            if el.find_parent(class_='footer'):
                continue
            return el
    return None

def find_direct_children_by_class(parent, pat):
    """Find direct children of parent matching class pattern."""
    return [c for c in parent.find_all(recursive=False) if c.get('class') and any(re.search(pat, ' '.join(c.get('class', [])), re.I) for pat in [pat])]

def process_template(template_dir, output_path):
    with open(template_dir + '/example.html') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    sections = soup.find_all('section', class_='slide')
    if len(sections) != 7:
        print(f'  WARNING: found {len(sections)} sections, expected 7')
        return False

    # --- Slide 1: Title ---
    s = sections[0]
    c = CONTENT['title']

    tag_el = find_by_class(s, ['section-tag', 'eyebrow', r'\btag\b', 'kicker', 'badge', 'pill', 'label'])
    if tag_el:
        set_text(tag_el, c['tag'])

    h1 = s.find('h1')
    if h1:
        # If h1's only child is a styled span (e.g. neon-grad), put title inside it
        tag_children = [c for c in h1.children if isinstance(c, Tag)]
        text_outside = ''.join(str(c) for c in h1.children if isinstance(c, NavigableString)).strip()
        if len(tag_children) == 1 and not text_outside:
            set_inner_html(tag_children[0], c['h1'])
        else:
            set_inner_html(h1, c['h1'])

    sub = (s.find('p', class_=lambda x: x and 'subtitle' in x)
           or s.find(class_=re.compile(r'\bsub(title)?\b', re.I))
           or s.find('p'))
    if sub:
        set_text(sub, c['subtitle'])

    meta_el = find_by_class(s, [r'\bmeta\b'])
    if meta_el:
        spans = meta_el.find_all('span')
        for i, span in enumerate(spans):
            if i < len(c['meta']):
                strong = span.find('strong')
                if strong:
                    set_text(strong, c['meta'][i])
                else:
                    set_text(span, c['meta'][i])

    # --- Slide 2: Section ---
    s = sections[1]
    c = CONTENT['section']

    label_el = find_by_class(s, ['section-label', r'\bnum\b', 'chapter', 'kicker', r'\blabel\b'])
    if label_el:
        set_text(label_el, c['label'])

    h2 = s.find('h2')
    if h2:
        set_text(h2, c['h2'])

    bignum = find_by_class(s, ['big-num', 'bignum', 'huge-num'])
    if bignum:
        set_text(bignum, c['bignum'])

    # --- Slide 3: Content (3 cards) ---
    s = sections[2]
    c = CONTENT['content']

    eyebrow = find_by_class(s, ['eyebrow', r'\btag\b', 'kicker', r'\blabel\b'])
    if eyebrow:
        set_text(eyebrow, c['eyebrow'])

    h2 = s.find('h2')
    if h2:
        set_text(h2, c['h2'])

    # Remove lead paragraph if present
    lead = s.find(class_=re.compile(r'lead', re.I))
    if lead:
        lead.decompose()

    # Find card-like containers - try multiple strategies
    cards = s.find_all(class_=re.compile(r'\bcard\b', re.I))
    if not cards:
        cards = s.find_all('li')
    if not cards:
        # Try items/blocks within a body/content container
        body = s.find(class_=re.compile(r'body|content|cards|items|grid', re.I))
        if body:
            cards = body.find_all(recursive=False)
    if not cards:
        cards = s.find_all(class_=re.compile(r'item|block|feature', re.I))

    # Replace first 3 cards, remove extras
    for i, card in enumerate(cards):
        if i >= 3:
            card.decompose()
            continue
        cc = c['cards'][i]
        # Find tag/number element
        tag = card.find(class_=re.compile(r'tag|num|index|label', re.I))
        if tag:
            set_text(tag, cc['tag'])
        # Find heading
        h3 = card.find(['h3', 'h4', 'strong'])
        if h3:
            set_text(h3, cc['h3'])
        # Find description paragraph or last text node
        p = card.find('p')
        if p:
            set_text(p, cc['p'])
        else:
            # For <li> with strong + text, replace remaining text
            for child in card.children:
                if isinstance(child, NavigableString) and child.strip():
                    child.replace_with(cc['p'])
                    break

    # --- Slide 4: Two column ---
    s = sections[3]
    c = CONTENT['twocol']

    eyebrow = find_by_class(s, ['eyebrow', r'\btag\b', 'kicker', r'\blabel\b'])
    if eyebrow:
        set_text(eyebrow, c['eyebrow'])

    h2 = s.find('h2')
    if h2:
        set_text(h2, c['h2'])

    # Find column containers
    cols_wrapper = s.find(class_=re.compile(r'\bcols\b', re.I))
    if cols_wrapper:
        cols = [c for c in cols_wrapper.find_all(recursive=False) if isinstance(c, Tag)]
    else:
        cols = s.find_all(class_=re.compile(r'\bcol\b', re.I))

    for i, col in enumerate(cols[:2]):
        if i >= len(c['cols']):
            break
        cc = c['cols'][i]
        tag = col.find(class_=re.compile(r'tag|num|col-num|label|index', re.I))
        if tag:
            set_text(tag, cc['tag'])
        h3 = col.find('h3')
        if h3:
            set_text(h3, cc['h3'])
        p = col.find('p')
        if p:
            set_text(p, cc['p'])
        spec = col.find(class_=re.compile(r'spec|meta|detail', re.I))
        if spec and cc['spec']:
            set_text(spec, cc['spec'])
        elif spec:
            spec.decompose()
        # Remove extra lists and paragraphs within columns (leftover template content)
        for ul in col.find_all(['ul', 'ol']):
            ul.decompose()
        # Keep only the first <p> (main description), remove extras
        all_p = col.find_all('p')
        for extra_p in all_p[1:]:
            extra_p.decompose()

    # --- Slide 5: Quote ---
    s = sections[4]
    c = CONTENT['quote']

    bq = s.find('blockquote')
    if bq:
        set_text(bq, c['blockquote'])

    cite = s.find('cite')
    if cite:
        set_text(cite, c['cite'])

    # --- Slide 6: Data (metrics) ---
    s = sections[5]
    c = CONTENT['data']

    eyebrow = find_by_class(s, ['eyebrow', r'\btag\b', 'kicker', r'\blabel\b'])
    if eyebrow:
        set_text(eyebrow, c['eyebrow'])

    h2 = s.find('h2')
    if h2:
        set_text(h2, c['h2'])

    metrics = s.find_all(class_=re.compile(r'\bmetric\b', re.I))
    # Filter out the container itself (class="metrics")
    metrics = [m for m in metrics if m.name == 'div' and m.get('class') and 'metric' in m.get('class', []) and 'metrics' not in m.get('class', [])]
    if not metrics:
        metrics = s.find_all(class_=re.compile(r'\bstat\b', re.I))
    if not metrics:
        metrics = s.find_all(class_=re.compile(r'\bitem\b', re.I))

    # Only populate as many metrics as the template has (no cloning)
    for i, metric in enumerate(metrics[:4]):
        if i >= len(c['metrics']):
            # Hide extra metric slots
            metric.decompose()
            continue
        mc = c['metrics'][i]
        tag = metric.find(class_=re.compile(r'tag|label$', re.I))
        if tag:
            set_text(tag, mc['tag'])
        val = metric.find(class_=re.compile(r'value|num|big', re.I))
        if val:
            unit = val.find(class_=re.compile(r'unit', re.I))
            if unit:
                set_text(unit, mc['unit'])
                # Replace text before unit
                for child in list(val.children):
                    if isinstance(child, NavigableString):
                        child.replace_with(mc['value'] + ' ')
                        break
            else:
                set_text(val, f"{mc['value']} {mc['unit']}" if mc['unit'] else mc['value'])
        label = metric.find(class_=re.compile(r'label|desc', re.I))
        if label:
            set_text(label, mc['label'])
        else:
            p = metric.find('p')
            if p:
                set_text(p, mc['label'])

    # --- Slide 7: Closing ---
    s = sections[6]
    c = CONTENT['closing']

    h2 = s.find('h2')
    if h2:
        set_inner_html(h2, c['h2'])

    p = s.find('p')
    if p:
        set_text(p, c['p'])

    btn = s.find(class_=re.compile(r'btn|button', re.I))
    if btn:
        set_text(btn, c['btn'])

    # Update page title
    title = soup.find('title')
    if title:
        set_text(title, '聊着天，把活干了 — Slides Design Systems')

    # Fix: quote-slide with align-items:flex-start causes footer to not stretch
    style = soup.find('style')
    if style and style.string and '.quote-slide' in style.string and 'flex-start' in style.string:
        style.string = style.string.replace(
            '</style>',
            '.quote-slide .footer { width: 100%; align-self: stretch; }\n</style>'
        )

    # Update footer text
    for footer in soup.find_all(class_='footer'):
        for span in footer.find_all('span'):
            text = span.get_text(strip=True)
            if not text:
                continue
            # Skip page counter spans (e.g. "01 / 07")
            if re.match(r'\d{2}\s*/\s*\d{2}', text):
                continue
            # Skip decorative/ornament/cn-label spans
            span_classes = ' '.join(span.get('class', []))
            if re.search(r'ornament|deco|dot|icon|sep|line|\bcn\b', span_classes, re.I):
                continue
            # Skip spans containing a dot indicator
            if span.find('span', class_='dot'):
                # This is the template name span with a dot - replace its text
                for child in list(span.children):
                    if isinstance(child, NavigableString) and child.strip():
                        child.replace_with(' FEISHU AGENT')
                        break
                continue
            # Other text spans in footer
            if not re.search(r'\d{2}\s*/', text):
                set_text(span, 'FEISHU AGENT')

    # ---- Post-processing: remove leftover decorative text ----

    # Title slide: remove English decorative labels
    s1 = sections[0]
    for cls in ['en-term', r'\ben\b', 'vertical-text', 'edition', 'subtitle-en',
                'rotated', r'\bvert\b', 'chip', r'\bdesc\b', 'monogram',
                'starburst', 'pow', 'burst']:
        for el in s1.find_all(class_=re.compile(cls, re.I)):
            if el.find_parent(class_='footer'):
                continue
            el.decompose()
    # Remove stat blocks on title slide (hex colors, numeric specs)
    for stat in s1.find_all(class_=re.compile(r'\bstat\b|\blbl\b|\bnum\b', re.I)):
        if stat.find_parent(class_='footer'):
            continue
        stat.decompose()
    # Remove any remaining <p> on title slide that isn't our subtitle
    for p in s1.find_all('p'):
        if '在飞书会议里' not in p.get_text():
            p.decompose()

    # Section slide: remove decorative text
    s2 = sections[1]
    for cls in ['vertical-text', 'edition', 'en-term', r'\ben\b', 'subtitle-en',
                'desc', 'rotated', r'\bvert\b', 'chapter-label', r'\blabel\b']:
        for el in s2.find_all(class_=re.compile(cls, re.I)):
            el.decompose()
    # Remove any <p> description in section slide
    for p in s2.find_all('p'):
        p.decompose()

    # Content slide: remove lead paragraphs and decorative labels
    s3 = sections[2]
    for el in s3.find_all(['p', 'div'], class_=re.compile(r'lead|desc|intro|section-desc', re.I)):
        el.decompose()
    for cls in ['en-term', 'pill', 'chip', 'stat', 'lbl', 'price', r'\bbig\b', 'pow', 'burst']:
        for el in s3.find_all(class_=re.compile(cls, re.I)):
            el.decompose()
    # Remove any standalone <p> in content slide that isn't inside a card
    for p in s3.find_all('p'):
        if not p.find_parent(class_=re.compile(r'card|col|item|li|metric', re.I)):
            p_text = p.get_text(strip=True)
            if p_text and not any(kw in p_text for kw in ['开完会后', 'Agent 加入']):
                p.decompose()
    # Remove list items that aren't our Level content
    for li in s3.find_all('li'):
        li_text = li.get_text(strip=True)
        if not any(kw in li_text for kw in ['开完会后', 'Agent 加入', '会后总结', 'Agent 代办', '边聊边干']):
            li.decompose()
    # Remove empty ul elements left behind
    for ul in s3.find_all('ul'):
        if not ul.find_all('li'):
            ul.decompose()

    # Two-col slide: remove spec/meta text and decorative labels
    s4 = sections[3]
    for el in s4.find_all(['p', 'div', 'span', 'em', 'small', 'li'],
                           class_=re.compile(r'spec|meta|detail|stat|lbl|pill|chip|from|origin|price|big', re.I)):
        if el.find_parent(class_='footer'):
            continue
        el.decompose()
    # Remove standalone <p> and <li> in two-col that aren't inside columns
    for tag in ['p', 'li']:
        for el in s4.find_all(tag):
            if not el.find_parent(class_=re.compile(r'\bcol\b', re.I)):
                el.decompose()
    # Remove empty ul elements
    for ul in s4.find_all('ul'):
        if not ul.find_all('li'):
            ul.decompose()
    # Remove decorative pow/burst elements
    for el in s4.find_all(class_=re.compile(r'pow|burst|starburst|big', re.I)):
        el.decompose()

    # Data slide: remove decorative labels (but keep metric contents)
    s6 = sections[5]
    for cls in ['en-term', 'pill', 'chip']:
        for el in s6.find_all(class_=re.compile(cls, re.I)):
            if el.find_parent(class_=re.compile(r'metric')):
                continue
            el.decompose()
    # Fix "3Level" concatenation: add space between value text and unit
    for metric in s6.find_all(class_=re.compile(r'\bmetric\b|\bstat\b|\bitem\b', re.I)):
        val = metric.find(class_=re.compile(r'value|num|big', re.I))
        if val:
            unit = val.find(class_=re.compile(r'unit', re.I))
            if unit:
                # Insert a space text node before the unit if not present
                prev = unit.previous_sibling
                if prev and isinstance(prev, NavigableString) and not prev.endswith(' '):
                    prev.replace_with(prev.rstrip() + ' ')

    # Closing slide: remove decorative starbursts and monograms
    s7 = sections[6]
    for el in s7.find_all(class_=re.compile(r'starburst|pow|burst|monogram', re.I)):
        el.decompose()

    # Fix h1 if it still contains original English text
    h1 = s1.find('h1')
    if h1 and '聊着天' not in h1.get_text():
        set_inner_html(h1, CONTENT['title']['h1'])

    with open(output_path, 'w') as f:
        f.write(str(soup))
    return True

# Generate all 20 versions
os.makedirs('examples/feishu-agent', exist_ok=True)
success = 0
errors = []
for d in sorted(os.listdir('templates')):
    src = f'templates/{d}'
    if not os.path.isfile(f'{src}/example.html'):
        continue
    name = d
    dst = f'examples/feishu-agent/{name}.html'
    try:
        if process_template(src, dst):
            success += 1
        else:
            errors.append(name)
    except Exception as e:
        errors.append(f'{name}: {e}')
        import traceback; traceback.print_exc()

print(f'\nDone: {success}/20 generated')
if errors:
    print('Errors:', errors)
