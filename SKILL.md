---
name: slides-design-systems
description: Create distinctive HTML presentations from 25 curated design systems — from calm minimalism to bold color to painterly and cinematic styles. Use when the user wants to build a presentation, slides, or a deck with strong visual identity. Helps non-designers pick a style through visual previews rather than abstract choices.
---

# Slides Design Systems

Create zero-dependency HTML presentations using one of 25 hand-crafted design systems. Every deck is a single self-contained HTML file that runs in any browser.

## Core Principles

1. **Zero Dependencies** — Single HTML files with inline CSS/JS. No npm, no build tools, no frameworks.
2. **Show, Don't Tell** — Generate visual previews and let the user pick. People choose what they can see.
3. **25 Design Systems, Not 25 Themes** — Each system has its own typography, palette, decorative vocabulary, and component grammar. Mixing systems breaks the design; stay inside one.
4. **Fixed 16:9 Stage** — Every deck uses a 1280×720 slide canvas scaled as a whole to the viewport via `transform: scale()`. Slides stay 16:9 on every screen; content never reflows.
5. **Design Tokens Are Law** — Each system's `DESIGN.md` contains YAML front-matter tokens (colors, fonts, spacing, radius, shadow, border). Read them and obey them. Do not invent colors, fonts, or radii.
6. **Implementation Rules Are Mandatory** — Read `AGENT_GUIDE.md` before generating any deck. It contains CSS syntax rules, footer/band invariants, CJK typography rules, content length limits, and a verification checklist — all derived from real bugs. Each template's `DESIGN.md` also has a "实现注意事项" section with template-specific gotchas. Skip them and the deck will break.

## The 25 Design Systems

| # | Slug | Name | Mood | Scheme | Best For |
|---|------|------|------|--------|----------|
| 01 | `systems` | Systems（蓝图技术感） | Calm | Light | Technical talks, documentation, engineering reviews |
| 02 | `sei` | 静 Sei（日式禅意） | Calm | Light | Cultural topics, keynotes, reflective talks |
| 03 | `soft-space` | Soft Space（温暖柔和） | Airy | Light | Friendly pitches, team updates, wellness |
| 04 | `light-as-air` | Light as Air（通透梦幻） | Airy | Light | Creative briefs, design reviews, product vision |
| 05 | `breathe` | Breathe（清新自然） | Airy | Light | Sustainability, health, nature topics |
| 06 | `essential` | ESSENTIAL（画廊极简） | Luxury | Light | Luxury brands, art, editorial, high-end pitches |
| 07 | `noir` | Noir（暗夜奢雅） | Luxury | Dark | Premium launches, evening talks, awards |
| 08 | `brutal` | Brutal（新粗野主义） | Bold | Light | Creative manifestos, design declarations, punk pitches |
| 09 | `neon` | Neon（合成波霓虹） | Bold | Dark | Tech launches, gaming, cyberpunk, music |
| 10 | `pop` | Pop!（波普艺术） | Bold | Light | Marketing, fun events, comic-style energy |
| 11 | `electric` | Electric（大胆渐变） | Bold | Gradient | Brand launches, high-energy keynotes, festivals |
| 12 | `memphis` | Memphis（孟菲斯后现代） | Bold | Light | Creative workshops, design education, playful topics |
| 13 | `punk` | Punk（瑞士朋克） | Bold | Light | Social topics, anti-establishment, raw energy |
| 14 | `tropic` | Tropic（热带热力） | Bold | Dark | Travel, lifestyle, summer, tropical brands |
| 15 | `mineral-strata` | Mineral Strata（青绿矿物层叠） | Painterly | Light | Cultural heritage, art history, Eastern aesthetics |
| 16 | `iron-line-halo` | Iron Line & Halo（敦煌铁线圆光） | Painterly | Warm | Cultural topics, museum, historical narratives |
| 17 | `cobalt-circles` | Cobalt Circles（青花钴蓝同心圆） | Painterly | Light | Art, ceramics, minimalist Eastern design |
| 18 | `nouveau` | Nouveau（新艺术运动） | Painterly | Warm | Elegant brands, art nouveau, ornamental design |
| 19 | `deco` | Deco（装饰艺术） | Painterly | Dark | Gatsby-era luxury, architecture, formal events |
| 20 | `ukiyo-e` | Ukiyo-e（浮世绘） | Painterly | Warm | Japanese culture, woodblock art, narrative talks |
| 21 | `wes-anderson` | Wes Anderson（韦斯·安德森） | Cinematic | Light | Quirky brand talks, storytelling, editorial with charm |
| 22 | `bauhaus` | Bauhaus（包豪斯） | Art Movement | Light | Design education, functionalism, modernist manifestos |
| 23 | `risograph` | Risograph（孔版印刷） | Print Craft | Light | Zine culture, independent publishing, DIY aesthetics |
| 24 | `vaporwave` | Vaporwave（蒸汽波） | Digital Aesthetic | Dark | Retro-tech, internet culture, synthwave keynotes |
| 25 | `wong-kar-wai` | Wong Kar-wai（王家卫） | Cinematic | Dark | Emotional storytelling, film, moody brand narratives |

**Mood groups:** Calm/Restrained (01-02), Light/Airy (03-05), High-end Whitespace (06-07), Bold & Colorful (08-14), Painterly (15-20), Cinematic & Art Movement (21-25).

## Fixed Stage Rules

These invariants apply to EVERY slide:

- Every deck has a viewport wrapper filling the browser window (`display: flex; align-items: center; justify-content: center`).
- Every slide is a fixed **1280×720** stage (`position: absolute; width: 1280px; height: 720px`).
- The stage scales uniformly: `@media (max-aspect-ratio: 16/9) { transform: scale(calc(100vw / 1280)); }` and the inverse for tall viewports.
- Content never reflows for phones; it scales down (letterboxing is fine).
- Use fixed internal measurements at the 1280×720 design size.
- Slide switching uses `display: none/flex` on `.slide` with an `.active` class.
- Navigation: ← → arrow keys, Space, Home, End.
- Include `prefers-reduced-motion` support when adding animations.

## Workflow

### Phase 1: Understand the Need

Ask (all at once, in one concise message):

1. **Purpose** — Pitch / Teaching / Conference talk / Internal presentation / Other
2. **Length** — Short (5-10) / Medium (10-20) / Long (20+)
3. **Content** — All ready / Rough notes / Topic only
4. **Density** — Low density (speaker-led, big type, few words) / High density (reading-first, self-contained detail)
5. **Mood preference** (optional) — Calm / Bold / Painterly / Surprise me

If the user has content, ask them to share it. If they name a specific template number or style, honor it directly and skip to Phase 3.

### Phase 2: Style Discovery (Show, Don't Tell)

Based on the user's purpose and mood, pick **3 candidate systems** that are genuinely different from each other:

- If the user gave a mood, pick from that group + one wildcard from another group.
- If no mood, pick one calm, one bold, one wildcard.
- For conservative/high-stakes decks, favor calm/luxury systems.
- For expressive/creative decks, include at least one bold or painterly system.

For each candidate, **read that template's `DESIGN.md`** from `templates/<slug>/DESIGN.md` and generate a single-slide title preview as a self-contained HTML file. The preview must:

- Use the real design tokens (fonts, colors, decorative elements) from that system's DESIGN.md.
- Look like a real first slide of the user's deck (use their actual title/topic), not a diagnostic card.
- Follow the fixed 1280×720 stage rules.
- Never render internal labels like "Option A", "preview", "template name", or workflow text on the slide itself.

Save previews to `.slides-previews/` and open them for the user. Present the three options by name and ask which they prefer (or "mix elements").

### Phase 3: Generate the Full Deck

Once the user picks a system:

1. **Read `AGENT_GUIDE.md`** in full. It contains mandatory CSS, layout, typography, and verification rules.
2. **Re-read that system's `templates/<slug>/DESIGN.md`** in full, including the "实现注意事项" section. Treat it as the design recipe.
3. **Read `templates/<slug>/example.html`** for the implementation reference (CSS variable structure, component patterns, decorative SVG).
4. Generate the complete presentation as a **single self-contained HTML file**:
   - All CSS inline in `<style>`, all JS inline in `<script>`.
   - Fonts via Google Fonts CDN with `<link rel="preconnect">`.
   - Define all design tokens as `:root` CSS variables copied from DESIGN.md.
   - Include the 7 standard slide layouts: **Cover, Section, Content (3-column), Two-column, Quote, Data (4-column), Closing**.
   - Add more layouts as needed, always using the same token system.
   - Every section gets a clear `/* === SECTION NAME === */` comment.
   - Navigation JS: arrow keys / Space / Home / End.
5. **Preserve the system's visual identity**: its fonts, palette, decorative vocabulary (borders, frames, circles, blobs, halos, etc.), spacing rhythm, and component grammar. Do not import patterns from other systems.
6. **Adapt content density** to the user's choice: low-density = one idea per slide, large type, generous space; high-density = structured grids, more self-contained detail.
7. After generating, run the **Verification Checklist** in `AGENT_GUIDE.md` §7 — screenshot EVERY slide type and check for overflow, overlap, footer contrast, and CJK font rendering.

### Phase 4: Delivery

1. Open the HTML file in the browser for the user.
2. Tell them: file location, style name, slide count, navigation keys.
3. Explain customization: edit `:root` CSS variables for colors, change the Google Fonts `<link>` for typography.
4. Offer revisions.

## Content Rules

- Never use Lorem Ipsum. Use the user's real content or write plausible placeholder copy in the deck's language.
- Each slide must have a clear purpose. If two slides say the same thing, merge them.
- Data slides need real numbers from the user; don't invent statistics.
- Quote slides need attribution.
- Keep text within its container — if it overflows, split the slide or reduce content, never shrink below readable size.

## Anti-AI-Slop Rules

Do NOT produce generic AI-presentation aesthetics:

- No purple/indigo gradients on white backgrounds unless the selected system explicitly calls for it.
- No generic Inter/Roboto/Arial unless the system's DESIGN.md specifies it.
- No interchangeable rounded-rectangle cards with soft shadows on every layout.
- No timid, evenly-distributed palettes — commit to the system's dominant colors and sharp accents.
- No decorative emoji unless the system (e.g. Memphis, Tropic) supports playful iconography.
- Every decorative element (frame, circle, blob, line, pattern) must come from the chosen system's vocabulary.

## File Structure

```
slides-design-systems/
├── SKILL.md                          # This file
├── AGENT_GUIDE.md                    # MANDATORY implementation rules & verification checklist
├── DESIGN_SYSTEMS.md                  # All 25 systems in one reference document
├── README.md
├── LICENSE
└── templates/
    ├── index.json                     # Compact metadata for all 25 systems
    ├── 01-systems/
    │   ├── example.html               # Working demo deck (7 layouts)
    │   ├── DESIGN.md                  # Design tokens + rules + 实现注意事项 + agent prompt
    │   └── preview.png                # Screenshot of the cover slide
    ├── 02-sei/
    │   ├── example.html
    │   ├── DESIGN.md
    │   └── preview.png
    └── ... (25 total)
```

## Reading Order (for agents)

1. Read this `SKILL.md` once.
2. In Phase 2, read only the `DESIGN.md` files of the 3 candidate systems.
3. In Phase 3, **read `AGENT_GUIDE.md` first**, then the chosen system's `DESIGN.md` (especially "实现注意事项") + `example.html` in full.
4. Do not read all 20 DESIGN.md files at once — it wastes context. Read on demand.
