---
name: Mineral Strata
version: 1.0.0
category: painterly-abstract
tags: [chinese, blue-green-landscape, mineral-colors, gold-line, geometric, strata]

color:
  background: "#F5F0E6"
  foreground: "#1A2A3A"
  azurite: "#2E5A88"
  malachite: "#4A8B6F"
  gold: "#DAA520"
  gold_deep: "#8B6914"
  gold_soft: "#DAA520"
  gold_light: "rgba(184,134,11,0.3)"
  gold_shimmer: "linear-gradient(90deg, #8B6914, #B8860B, #DAA520, #B8860B, #8B6914)"
  gold_ink: "linear-gradient(180deg, #DAA520, #B8860B, #8B6914, #B8860B)"
  muted: "#6B6352"

typography:
  heading:
    family: "Noto Serif SC, serif"
    weight: 900
    letter_spacing: "0.05-0.08em"
  body:
    family: "Noto Serif SC, serif"
    weight: 400
  en:
    family: "Cormorant Garamond, Georgia, serif"
    weight: 600
    letter_spacing: "0.2-0.35em"
  scale:
    display: "120px"
    h1: "80px"
    h2: "40px"
    body: "15px"
    caption: "12px"

spacing:
  slide_padding: "56px 80px"
  gap_large: "32px"
  gap_medium: "24px"

radius:
  base: "0px"

shadow:
  none: true

border:
  width: "2-3px"
  style: "solid"
  color: "#DAA520"

progress_bar:
  height: "50px"
  background: "transparent"
  border_top: "none"
  section_label:
    font: "var(--font-cn)"
    size: "12px"
    weight: "700"
    color: "rgba(245,240,230,0.75)"
    letter_spacing: "0.25em"
  page_number:
    font: "var(--font-en)"
    size: "16px"
    weight: "700"
    color: "var(--gold)"
    letter_spacing: "0.1em"
  segments:
    shape: "line"
    size: "4px"
    gap: "5px"
    section_gap: "24px"
    future: "light fill; w=36px, h=4px"
    past: "medium fill"
    current: "solid var(--gold) #B8860B fill; h=4px (same as other segments, no taller block, no glow)"

---

# Mineral Strata（青绿·矿物层叠）— Design Specification

## 气质

青绿山水的抽象转译。不画山，而以石青、石绿的水平色带模拟远山的层叠结构，以泥金细线勾勒分界，以极简几何三角形指代山峰。矿物色的沉稳华贵 + 现代主义的几何克制，像展开一幅手卷，但画面中没有一笔是在"画山水"。

## 色彩规则

- **背景**：暖绢白 `#F5F0E6`，不是纯白，带绢本质感。
- **石青** `#2E5A88`：上方色带、主标题、关键文字——最远最高的颜色。
- **石绿** `#4A8B6F`：下方色带，托住全局——最近最沉的颜色。
- **泥金（敦煌赤金）** `#B8860B`（深 `#8B6914` / 柔 `#DAA520`）：暗暖带红棕调，像千年氧化的金粉。含蓄的矿物金渐变文字（gold-ink）+ 微妙光泽金线（gold-shimmer），只做线和字，不做面。进度条当前段与其他段等高（4px），不用突出色块，不发光。
- **禁止**：渐变色、高饱和色、冷灰、大面积金色块。

## 字体规则

- 中文标题用 **Noto Serif SC 900**，字距 0.05-0.08em，字号极大（封面 120px）。
- 英文用 **Cormorant Garamond**，大写 + 0.2-0.35em 字距，金色。
- 正文用 Noto Serif SC 400，行高 1.8。
- 标签用小号宋体，石青色。

## 版式规则

- **水平色带系统**：页面被石青（上）、绢白（中，内容区）、石绿（下）三条水平带分割，泥金细线分隔。
- 色带高度可变化：封面/结尾用宽带（80-100px），内容页用窄带（50px）。
- **几何山形**：底部放置 2-3 个极简三角形（SVG polygon），石青/石绿填充 + 泥金 1.5px 描边，只有轮廓没有皴法。
- **同心圆装饰**：泥金细线绘制的 2-3 层同心圆，作为"日/月"的抽象符号，低透明度。
- 内容区居中或左对齐，大量留白（云雾即留白）。
- 页脚放在石绿色带内，白色/半透明白色文字。

## 组件模式

- **色带**：绝对定位的 `position: absolute; left:0; right:0;` 矩形，石青或石绿填充，高度 50-100px。
- **金线**：`height: 2px; background: gold-shimmer (linear-gradient 90deg, #8B6914 → #B8860B → #DAA520 → #B8860B → #8B6914);`，暗暖赤金的微妙光泽渐变，位于色带边缘。
- **金色文字**：`background: gold-ink (linear-gradient 180deg, #DAA520 → #B8860B → #8B6914 → #B8860B); -webkit-background-clip: text; -webkit-text-fill-color: transparent;`，所有金色文字（标签、编号、英文副标题、页码）均用暗暖赤金渐变，不用纯色，也不用亮金/纯金高光。
- **山形**：SVG `<polygon>`，如 `points="680,200 820,40 960,200"`，石青填充 + 泥金描边。
- **同心圆**：SVG `<circle>` 多层，`fill: none; stroke: #DAA520`，1-2px 线宽。
- **卡片**：半透明白底 `rgba(255,255,255,0.4)` + 3px 泥金 `border-top`，无圆角。
- **双栏**：一栏石青底白字，一栏半透明白底深字。

## Do / Don't

- **Do** 用水平色带组织版面，像手卷一样横向阅读。
- **Do** 山形只用几何三角形 + 金线轮廓，不画皴法。
- **Do** 金色只做细线，不做填充面。
- **Don't** 不要画真实的山水、云雾、树木、水波。
- **Don't** 不要使用圆角、渐变、阴影。
- **Don't** 不要让石青和石绿直接相邻——中间必须有绢白留白。

## 实现注意事项

- 字体栈：`'Noto Serif SC', 'Cormorant Garamond', Georgia, serif`。
- **每一种 slide type 都必须有对应的 `.bottom-band` CSS 规则**（position + background + height）。HTML 里有 div 不等于 CSS 里有样式。
- **页脚高度必须按版式匹配**：封面/结尾 100px，章节 60px，内容/双栏/数据/金句 50px。
- **nav-hint/counter 在短页脚版式上必须上移**到 `bottom: 64px`。
- 泥金色是 `#DAA520`（不是 `#C4A35A`），只做线不做面。
- 石青 `#2E5A88`、石绿 `#4A8B6F`、绢白 `#F5F0E6`。
- 山形只用 SVG polygon 几何三角形 + 泥金描边，不画皴法。
- 新增 slide type 时必须同时定义：bottom-band、footer 高度、content-area padding、nav-hint 位置。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景为暖绢白 #F5F0E6。页面由石青 #2E5A88（上）和石绿 #4A8B6F（下）水平色带分割，泥金（敦煌赤金）#B8860B 2px 微妙光泽渐变线（gold-shimmer，深金#8B6914→赤金#B8860B→柔金#DAA520，暗暖带红棕调，不用亮金/纯金）分隔。底部放 2-3 个极简 SVG 三角形山形（石青/石绿填充+泥金描边）。中文标题 Noto Serif SC 900 大字距，英文 Cormorant Garamond 大写暗暖赤金渐变文字（gold-ink，不用纯色也不用亮金高光）。所有金色文字（标签、编号、页码）均用 gold-ink 赤金渐变。进度条当前段与其他段等高（4px），不用突出色块。卡片半透明白底+3px 泥金顶部边框，零圆角。禁止画真实山水、渐变（除金色赤金渐变外）、圆角、阴影、亮金属效果、进度条色块。
