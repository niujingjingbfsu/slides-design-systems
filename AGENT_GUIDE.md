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
