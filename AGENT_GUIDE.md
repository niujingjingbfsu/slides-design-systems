# Agent Implementation Guide — HTML Slides Design Systems

> **Read this before generating or modifying any deck.** Every rule below exists because a real deck broke without it. These are not style preferences — they are invariants.

---

## 1. CSS Syntax (silent failures are the worst kind)

### 1.1 Every declaration MUST end with a semicolon

```css
/* WRONG — browser silently discards BOTH declarations */
font-family: var(--font-display) font-size: 48px;

/* RIGHT */
font-family: var(--font-display); font-size: 48px;
```

This bug is invisible in DevTools (the property just doesn't appear) and has caused headings to render at wrong sizes/weights across 9 templates simultaneously.

### 1.2 Every `var()` MUST have a closing parenthesis

```css
/* WRONG — everything after this point in the rule is discarded */
color: var(--red;

/* RIGHT */
color: var(--red);
```

### 1.3 Use `:where()` for overridable base styles

Never use bare element selectors or `:not(.class)` for universal resets — they contribute specificity that template-level rules cannot override without `!important`.

```css
/* WRONG — specificity 0,1,1; beats single-class rules */
.slide :not(.card) { margin: 0; }

/* RIGHT — specificity 0; any class can override */
.slide :where(:not(.card)) { margin: 0; }
```

### 1.4 `box-sizing: border-box` MUST be set globally

```css
*, *::before, *::after { box-sizing: border-box; }
```

---

## 2. Slide Stage (the 1280×720 invariant)

### 2.1 Every slide MUST be centered with translate(-50%, -50%)

```css
.deck { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; }
.slide { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 1280px; height: 720px; }
```

Omitting `translate(-50%,-50%)` causes the slide to render from the center point outward, showing only the bottom-right quarter. This has happened in 3 templates.

### 2.2 Content MUST live inside a padding-protected area

Never position content at the very edge of the 1280×720 canvas. Every slide type needs:
- Top padding ≥ its top decorative band height + 20px
- Bottom padding ≥ its footer height + 20px
- Left/right padding ≥ 60px (80px for spacious systems)

---

## 3. Footer and Bottom Bands (the #1 source of bugs)

### 3.1 Footer height MUST match bottom-band height for EACH slide type

If a template has colored bottom bands that vary by slide type, the footer height must vary too:

```css
.footer { position: absolute; bottom: 0; height: 100px; }  /* base = title/closing */
.section-slide .footer { height: 60px; }                    /* matches 60px band */
.content-slide .footer,
.two-col .footer,
.data-slide .footer,
.quote-slide .footer { height: 50px; }                      /* matches 50px band */
```

### 3.2 Every slide type with a bottom-band div MUST have a CSS rule

If the HTML contains `<div class="bottom-band">`, there MUST be a matching CSS rule:

```css
.quote-slide .bottom-band {
  position: absolute; bottom: 0; left: 0; right: 0;
  height: 50px; background: var(--band-color); z-index: 0;
}
```

A bottom-band div without CSS renders as an invisible zero-height element, leaving white footer text on a light background. This has happened.

### 3.3 Checklist when adding ANY new slide type

When creating a new slide layout (e.g., `.timeline-slide`), you MUST define all four:

1. `.new-slide .bottom-band` — height + background
2. `.new-slide .footer` — matching height
3. `.new-slide .content-area` — padding-bottom ≥ footer height + 20px
4. `.deck:has(.new-slide.active) .nav-hint, .deck:has(.new-slide.active) .counter` — position above footer

### 3.4 nav-hint and counter MUST sit above the footer

```css
/* For slides with 50px footer: */
.deck:has(.content-slide.active) .nav-hint,
.deck:has(.content-slide.active) .counter { bottom: 64px; }
```

Never let `bottom: Xpx` on nav-hint/counter be less than the footer's top edge (footer bottom + height).

### 3.5 Footer text color MUST contrast with its background

- White/light footer text → MUST have a dark/colored bottom-band behind it
- Dark footer text → MUST sit on a light background
- Verify this for EVERY slide type, not just the cover

---

## 4. Typography (CJK is not Latin)

### 4.1 CJK fonts MUST be included

Every template MUST load a CJK web font and include it in the font-family stack:

| System type | CJK font |
|---|---|
| Sans-serif (Inter, Sora, Manrope, Outfit, etc.) | `'Noto Sans SC'` |
| Serif (Cormorant, Playfair, etc.) | `'Noto Serif SC'` |
| Japanese (02-sei, 20-ukiyo-e) | `'Noto Serif JP'` / `'Shippori Mincho'` |

```html
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700;900&display=swap" rel="stylesheet">
```

```css
font-family: 'Inter', 'Noto Sans SC', sans-serif;
```

### 4.2 CJK headings need larger line-height

| Element | Latin display font | CJK text |
|---|---|---|
| h1 (cover) | 0.9–1.0 | **1.15–1.2** |
| h2 (page title) | 1.0–1.1 | **1.18–1.25** |
| Body | 1.5–1.7 | 1.7–1.9 |

Chinese characters are square and fill the em-box; line-height 0.82–0.9 causes adjacent lines to touch or overlap.

### 4.3 CJK headings need heavy font-weight

Chinese characters look thin at weights below 700. Set `font-weight: 900` for h1/h2 when the primary font is a CJK fallback.

### 4.4 Decorative English fonts MUST have CJK fallback

Fonts like Anton, Archivo Black, Orbitron, Fredoka, Limelight do NOT contain Chinese glyphs. The browser falls back to the next font in the stack — if that's a system default, it looks wrong.

```css
/* WRONG — Chinese falls back to system serif/sans randomly */
font-family: 'Anton', sans-serif;

/* RIGHT */
font-family: 'Anton', 'Noto Sans SC', sans-serif;
```

### 4.5 English and Chinese fonts MUST be visually compatible

Pair fonts with similar character:
- Geometric sans (Sora, Outfit, Manrope) → Noto Sans SC
- Elegant serif (Cormorant, Playfair) → Noto Serif SC
- **Do NOT** pair rounded/friendly fonts (Fredoka) with sharp CJK fonts — use Outfit instead

### 4.6 Long text MUST wrap safely

```css
overflow-wrap: break-word; word-break: break-word;
```

---

## 5. Layout and Overflow

### 5.1 Flex children need min-height: 0

```css
.content-area { display: flex; flex-direction: column; }
.content-area > * { min-height: 0; }  /* allows children to shrink instead of overflowing */
```

Without this, flex children with long content will overflow the slide boundary instead of being clipped or sized correctly.

### 5.2 Cards and containers need overflow: hidden

```css
.card, .col, .metric { overflow: hidden; }
```

### 5.3 Grid label columns MUST be wide enough

```css
/* WRONG — "LEVEL 1" wraps to "LEV EL 1" */
grid-template-columns: 40px 1fr;

/* RIGHT */
grid-template-columns: 90px 1fr;
```

Labels that should not break need `white-space: nowrap`.

### 5.4 Content lists MUST span full width

When using `<ul><li>` for content rows, the list must fill the content area. Do not constrain it to a narrow grid column.

### 5.5 Cards on gradient/colorful backgrounds MUST NOT be solid white

```css
/* WRONG — white card on gradient looks broken */
background: #fff;

/* RIGHT — frosted glass */
background: rgba(255,255,255,0.12);
backdrop-filter: blur(12px);
border: 1px solid rgba(255,255,255,0.2);
```

### 5.6 Decorative elements MUST NOT overlap text

- Set `pointer-events: none` on all decorative elements
- Use `z-index` to keep decorations behind content (z-index: 0-1) and text above (z-index: 2+)
- Verify at every slide type — a decoration that's clear on the cover may overlap a title on a content slide

---

## 6. Content Length Limits (at 1280×720 design size)

These are maximums for the standard 7 layouts. If content exceeds these, split the slide or reduce text — never shrink font below these minimums.

| Element | Max Chinese chars | Min font-size |
|---|---|---|
| Cover h1 (120px) | 8 per line, 2 lines | 80px |
| Page h2 (38-44px) | 16 per line, 2 lines | 32px |
| Card title | 8 | 22px |
| Card body | 25 per line, 3 lines | 14px |
| Data value | 8 chars (incl. unit) | 40px |
| Data label | 16 | 12px |
| Quote | 50 chars total | 36px |
| Footer item | 20 chars | 12px |
| Eyebrow/label | 30 chars | 12px |

---

## 7. Verification Checklist (run before delivery)

For EVERY slide type in the deck (not just the cover), verify:

- [ ] No text is cut off at any edge
- [ ] No text overlaps other text, cards, or decorative elements
- [ ] Footer text is readable (check contrast against its background)
- [ ] All colored bands/borders render at the correct height and color
- [ ] nav-hint and counter do not overlap footer content
- [ ] Content fills the slide appropriately (not crammed in one corner)
- [ ] CJK text renders in the intended font (not a system fallback)
- [ ] CJK headings have adequate line-height (lines don't touch)
- [ ] No horizontal scrollbar appears
- [ ] Google Fonts `<link>` URLs are correct and load
- [ ] All `var()` references resolve to defined custom properties
- [ ] No CSS declaration is missing a semicolon (especially between `font-family` and `font-size`)
- [ ] Every slide type with a bottom-band div has a matching CSS rule
- [ ] Decorative elements stay behind content (z-index)

### Screenshot verification

After generating a deck, take screenshots of EVERY slide (not just the cover) using Chrome headless:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu \
  --screenshot="slide-N.png" \
  --window-size=1280,720 --force-device-scale-factor=2 \
  --hide-scrollbars \
  "file:///path/to/deck.html#N"
```

Visually inspect each screenshot. Bugs that are invisible in code review (missing bands, font fallback, overlap) are obvious in screenshots.

---

## 8. Modifying Templates

When changing a template's `example.html`:

1. The change applies to the template itself AND all generated examples
2. After modifying template CSS, regenerate all example decks
3. Re-screenshot all slide types of the modified template
4. If the change affects a universal rule (footer, stage, fonts), check ALL 20 templates
5. Do not hardcode colors or fonts that should be design tokens — use CSS variables

---

## 9. Progress System (mandatory for all decks)

Every deck MUST include a progress indicator so viewers always know: total pages, current page, current section, and section boundaries.

### 9.1 Standard page structure

```
1. Cover        (title-slide — special layout)
2. Section 01   (section-slide — chapter divider)
3. Content page (content-slide)
4. Content page (two-col)
5. Section 02   (section-slide — SAME layout as slide 2, different number/title)
6. Data page    (data-slide)
7. Section 03   (section-slide — SAME layout as slide 2)
8. Quote page   (quote-slide)
9. Closing      (closing-slide — special layout)
```

**Rules:**
- Every `<section>` MUST have a `data-section="Section Name"` attribute
- All section divider pages MUST use the same layout within a template — only the number, title, and accent decoration change
- Cover and closing are special layouts, not section dividers
- If content requires fewer sections, use fewer — but every section MUST have a divider page

### 9.2 Progress bar HTML (identical in every slide)

```html
<div class="progress-bar">
  <div class="progress-strip"></div>
  <span class="pb-section"></span>
  <span class="pb-page"></span>
</div>
```

This replaces any old `.footer`, `.counter`, or `.page-num` elements. Do not keep both.

### 9.3 Progress bar CSS requirements

The structure is universal; the visual form adapts to each template's design language.

**Mandatory properties:**
```css
.progress-bar {
  position: absolute; bottom: 0; left: 0; right: 0;
  height: 56px; display: flex; align-items: center; justify-content: space-between;
  padding: 0 60px; z-index: 50;
}
.progress-strip {
  position: absolute; top: -8px; left: 50%; transform: translateX(-50%);
  display: flex; align-items: center;
}
.progress-strip .seg { margin: 0 4px; transition: all 0.25s; }
.progress-strip .seg.seg-gap { margin-left: 4px; }  /* uniform spacing — do NOT use larger gaps for section boundaries, it looks fragmented */
.slide { padding-bottom: 80px !important; }           /* prevent content overlap */
```

**Segment visibility MINIMUMS (these have caused bugs):**
- Future segments: background opacity ≥ 0.18 on light bg, ≥ 0.12 on dark bg; minimum size 8px in any dimension
- Past segments: background opacity ≥ 0.35 on light bg, ≥ 0.4 on dark bg
- Current segment: MUST use the template's accent color; MUST be visually larger or brighter than past segments
- Segments MUST NOT be thinner than 2px or smaller than 8px — they become invisible at presentation scale
- If using lines (2-3px tall), they MUST be visually separated from any border line on `.progress-bar` (use `top: -8px` minimum)

**Shape choices by template personality:**
- Geometric/technical (Systems, Brutal, Punk, Bauhaus): blocks
- Minimal/luxury (Essential, Noir, Deco): thin lines or diamonds
- Playful/rounded (Soft Space, Tropic, Pop, Wes Anderson): dots or pills
- Neon/retro (Neon, Vaporwave): glowing lines
- Japanese/Chinese (Sei, Mineral Strata, Ukiyo-e): dots or small squares

### 9.4 JavaScript (use this exact pattern)

```javascript
const slides = document.querySelectorAll('.slide');
const total = slides.length;
let current = 0;
slides.forEach((s, i) => { if (s.classList.contains('active')) current = i; });

function buildProgress() {
  // CRITICAL: build ALL segments for EACH strip — do NOT append one seg per slide
  const sections = Array.from(slides).map(s => s.dataset.section || '');
  document.querySelectorAll('.progress-strip').forEach(strip => {
    let lastSection = null;
    sections.forEach((section, i) => {
      const seg = document.createElement('div');
      seg.className = 'seg';
      if (lastSection !== null && section !== lastSection) seg.classList.add('seg-gap');
      strip.appendChild(seg);
      lastSection = section;
    });
  });
}

function updateUI(idx) {
  const sectionName = slides[idx].dataset.section || '';
  const pageStr = String(idx + 1).padStart(2, '0') + ' / ' + String(total).padStart(2, '0');
  document.querySelectorAll('.progress-bar').forEach(bar => {
    bar.querySelector('.pb-section').textContent = sectionName;
    bar.querySelector('.pb-page').textContent = pageStr;
  });
  document.querySelectorAll('.progress-strip').forEach(strip => {
    strip.querySelectorAll('.seg').forEach((seg, i) => {
      seg.classList.toggle('current', i === idx);
      seg.classList.toggle('past', i < idx);
    });
  });
}

function show(i) {
  slides[current].classList.remove('active');
  current = (i + total) % total;
  slides[current].classList.add('active');
  updateUI(current);
}
// ... keyboard navigation ...
buildProgress();
updateUI(current);
```

**Known bug to avoid:** The first implementation iterated over slides and appended one segment to each slide's own strip per iteration, resulting in only ONE segment per strip instead of ALL segments. The correct pattern builds the full segment list from a sections array and populates every strip with all segments.

### 9.5 Section naming

- Cover: template name or short tagline (e.g., "SYSTEMS", "靜")
- Content sections: short Chinese or English names (e.g., "框架", "数据", "哲思")
- Closing: "END", "THANK YOU", or equivalent
- Names should be 2-6 characters; they appear in the bottom-left at 12px

### 9.6 What NOT to do

- Do NOT show two page numbers (e.g., big center number + right-side counter) — pick one location
- Do NOT let the progress strip blend into a border line (2px line on top of 1px border = invisible)
- Do NOT use opacity below 0.12 for future segments — they disappear
- Do NOT forget `padding-bottom` on `.slide` — content will overlap the progress bar
- Do NOT keep old `.footer` elements alongside `.progress-bar` — duplicate info
- Do NOT hide nav-hint outside the slide boundary — use `display: none` if not needed

### 9.7 Templates with decorative bottom elements

Some templates have their own decorative elements at the bottom (colored bands, SVG borders, wave patterns). The progress bar MUST NOT overlap these. Two strategies:

**Strategy A — Integrate into the band** (e.g., 15-mineral-strata): If the template has a colored bottom band, make `.progress-bar` background transparent, use light text on the dark band, and set its height to match the band height per slide type. The progress strip sits at the top edge of the band.

**Strategy B — Position above the decoration** (e.g., 16-iron-line-halo): If the template has a decorative border (32px SVG wave, etc.), set `.progress-bar { bottom: <decoration-height>px; }` so it sits above the decoration on the slide background. Increase `.slide { padding-bottom }` accordingly.

**Always remove old navigation elements**: Before adding the progress system, scan for and remove any pre-existing `.bottom-bar`, `.counter`, `.footer`, `.page-num`, `.page-indicator` elements — they will overlap with the new progress bar. The migration script handles `.footer`/`.counter`/`.page-num` but templates may use custom class names (e.g., vaporwave's `.bottom-bar`).

**Checklist before finishing a template:**
1. No old bottom-bar/counter/footer elements remain in the HTML
2. Progress bar does not overlap any decorative bottom band/border
3. Progress segments are clearly visible (not blending into lines or patterns)
4. Text colors have sufficient contrast against whatever is behind the progress bar
5. Verify on cover, section, content, data, quote, and closing slides — band heights may differ

### 9.8 Consistent frame across middle pages

Cover and closing slides may have special layouts (larger bands, centered content). But ALL middle pages — section, content, two-col, data, quote — MUST share identical decorative frame dimensions:

- Top band / border height: same value across all middle page types
- Bottom band / border height: same value across all middle page types
- Top decorative line position: same value
- Bottom decorative line position: same value
- Content area padding (top/bottom/left/right): same value

If a template has `.section-slide .bottom-band { height: 60px }` but `.content-slide .bottom-band { height: 50px }`, the frame will visibly "jump" when navigating. Standardize to one value (typically the content slide's value, since it's the most common).

Section pages are exempt from content alignment (they are centered by design), but their frame must match.

### 9.9 Aesthetic constraints (beauty is mandatory)

A progress bar that meets all functional specs can still be ugly. These rules prevent that.

**Hard rules (never violate):**
1. **No border-top.** A `border-top` spanning the slide width creates a visible horizontal line that cuts across the design. Use `border-top: none` on all templates — light and dark alike. The progress bar needs no separation line; it floats on the slide.
2. **No background container.** The progress bar is not a "bar" — it's floating text and segments at the bottom of the slide. Set `background: transparent` (or omit it entirely) and `border-top: none`. Never give the progress bar its own background color, even if it matches the slide — a redundant background is a bug waiting to happen when the slide color changes. If text feels hard to read, fix the text color, don't add a background band.
3. **Progress segments must match the template's primary shape language.** If the template uses circles (soft-space, light-as-air), use circles. If it uses sharp squares (brutal, punk), use squares. Never import a shape that doesn't exist elsewhere in the template.
4. **Progress bar visual weight ≤ 15% of content area.** The progress bar is navigation chrome, not a design feature. It should be noticed when needed, invisible when not.
5. **Colors must come from the template's palette.** No generic gray. Use the template's accent color for "current", muted foreground for "past", and a very faint version of foreground for "future".
6. **Typography must match.** Section label and page number must use fonts already defined in the template (display font for page number if the template has one, body font for section label).

**Soft rules (strongly recommended):**
- No background, no border — the progress bar is floating chrome, not a container. Choose text and segment colors that work directly on the slide background.
- The "current" segment should be 20-40% larger than future segments, with the template's accent color.
- If the template has a signature effect (offset shadow in Memphis, glow in neon, gold shimmer in deco), apply it subtly to the current segment.
- Page number format: current page in accent color, total in muted color (e.g., `<span class="cur">03</span> / 09`).

**Verification checklist (must pass before considering done):**
- [ ] Screenshot the cover, one content page, and one section page
- [ ] Progress bar does not draw the eye away from content
- [ ] Segments are clearly visible but not dominant
- [ ] No heavy full-width lines
- [ ] Colors and shapes match the template's design language
- [ ] No overlap with decorative elements (bands, borders, patterns)
- [ ] Page number and section label are legible

**Reference:** Each template's `DESIGN.md` has a `progress_bar:` section with exact tokens. Read it first. If implementing a new template, write the `progress_bar:` spec BEFORE writing CSS — design it as part of the system, not as an afterthought.

## 10. Aesthetic Quality (avoid ugly, don't enforce rigid)

These are NOT pixel-perfect rules. They are things to LOOK AT and JUDGE after filling content. If something looks off, fix it. The goal is to avoid common aesthetic failures, not to enforce a uniform grid.

### 10.1 Visual self-check (look at every screenshot)

After generating a deck, screenshot EVERY page and ask these questions:

**Typography:**
- Does the title have enough breathing room? (Lines of Chinese text should never touch each other.)
- Is the body text readable? (Line height should feel generous, not cramped.)
- Do Chinese and English fonts look like they belong together? (Sharp Chinese + rounded English = jarring. Match the visual weight.)
- Is there a clear hierarchy? (Title > subtitle > body > caption — you should be able to tell at a glance what's most important.)

**Spacing:**
- Is there enough space between text and the edges of cards/blocks? (Text touching a border or color block always looks bad.)
- Is the whitespace intentional? (Empty space on one side of the slide is fine if it's a deliberate layout choice. It's bad if content just didn't fill the space.)
- Do related elements sit close together, and unrelated elements have more space? (Proximity = grouping.)

**Balance:**
- Does the page feel weighted to one side for no reason? (Asymmetry is fine if it's intentional. A list that only fills 40% of the width with empty space on the right is not.)
- Do cards/columns have similar visual weight? (One giant card next to a tiny one looks unbalanced unless it's a deliberate focal point.)
- Is the content vertically centered or top-aligned consistently? (Don't mix alignment within the same page type.)

**Color and decoration:**
- Do decorative elements enhance or distract? (A shape overlapping text = distract. A shape in a corner = enhance.)
- Is the accent color used sparingly? (Accent on everything = accent on nothing.)
- Does the progress bar feel like part of the design? (If it looks like it was pasted on at the end, redesign it.)

**Consistency across pages:**
- When flipping between pages, does the content area "jump"? (Cover/closing can be special. All middle pages should have consistent frame and content start position.)
- Do cards look the same across pages? (Same padding, same border radius, same shadow.)
- Does the same type of element (label, metric, tag) look the same everywhere?

### 10.2 Minimum spacing principles (soft, not rigid)

These are guidelines, not hard rules. Use judgment.

- **Text inside a card**: at least the font size of the body text as padding (e.g., 14px text → ≥16px padding).
- **Title to next element**: at least 1.5× the title's line height.
- **Section label to title**: small gap (8-12px). Title to body: larger gap (24-36px).
- **Card to card**: at least the card's internal padding.
- **Content to progress bar / footer**: at least 24px clear space.
- **Chinese headings**: line-height ≥ 1.2 (never below 1.1). English display headings can go tighter (0.9-1.0), but Chinese cannot.

If content is longer than expected, let the layout adapt (reduce font size slightly, increase card height) rather than cramming. Never let text touch a border.

### 10.3 When in doubt, simplify

If a page feels "off" but you can't pinpoint why:
1. Remove one decorative element.
2. Increase the largest gap by 8px.
3. Reduce the number of colors by one.
4. Make the title slightly smaller.

Most "ugly" slides have too much going on, not too little.

### 10.4 The Five Don'ts (read before writing any HTML)

These are the most common aesthetic failures. Check every page against these.

**① 不乱 — No visual chaos**
- One alignment per page. If the title is left-aligned, don't center the body. If the page is centered, don't left-align a card.
- Spacing follows a rhythm. Gaps should be multiples of a base unit (8px or 12px). Random gaps (13px, 27px, 41px) feel chaotic.
- No more than 3 font sizes on a page. Title, body, caption — that's enough. If you need a 4th, you're probably over-designing.
- Grid lines should be invisible but felt. Elements should line up with each other even if there's no visible grid.

**② 不花 — No visual noise**
- Max 3 colors per page (background + text + accent). A 4th color needs a reason.
- Max 2 font families per page. Decorative display font + body font. A 3rd font is almost always unnecessary.
- Pick ONE effect style. If you use shadows, don't also use gradients AND borders AND glows. One effect per page.
- Decorative elements: 2-5 per page is enough. More than that and they compete with content.
- No rainbow text, no gradient text on busy backgrounds, no neon colors unless the template is neon-themed.

**③ 不杂 — No inconsistency**
- Same component = same style everywhere. If card A has 24px padding and 8px radius, card B on the next page should too.
- Same level = same treatment. All h2s look the same. All labels look the same. All metrics look the same.
- Don't mix icon styles (line icons + filled icons on the same page).
- Don't mix border radii (a 4px card next to a 24px card looks like two different designs).
- If a template uses serif headings, don't switch to sans-serif headings on one page.

**④ 不丑 — No ugly elements**
- Text must never touch a border, a color block edge, or another text element. Minimum clear space = the font size of that text.
- No orphaned single characters (a Chinese title where one character drops to its own line). Adjust font size or width.
- No stretched/squashed images. Keep aspect ratios.
- No low-contrast text. If you can't read it at a glance, it's too low contrast.
- No lorem ipsum or placeholder text left in. Every word should be real content.
- No broken icons, missing images, or default browser styling (blue underlined links, etc.).

**⑤ 不空 — No empty pages**
- Content should occupy at least 50% of the content area. If it's less, either enlarge the content, add a relevant visual (quote, metric, illustration), or split into two pages.
- Whitespace is good — but it should be deliberate. A title in the top-left corner with 70% empty space below is not "minimalist", it's unfinished.
- If a page has only a title and one line of text, it probably needs either more content or to be merged with another page.
- Data pages with only 1 metric look sparse. Use at least 2-3, or make the single metric very large and prominent.

**Quick test:** After finishing a page, squint at it (or zoom out to 50%). If you can't tell what's the most important element, or if your eye bounces around with no clear path, the page needs simplification.
