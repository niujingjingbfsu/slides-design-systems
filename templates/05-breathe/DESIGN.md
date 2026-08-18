---
name: Breathe
version: 1.0.0
category: light-airy
tags: [clean, sage-green, organic, nature, white, minimal]

color:
  background: "#FFFFFF"
  foreground: "#2D3D35"
  muted: "#8A9A8E"
  sage: "#A8C4A2"
  sage_deep: "#6B8F6B"
  sage_light: "#E8F0E6"
  sage_pale: "#F4F8F2"
  line: "rgba(45, 61, 53, 0.1)"

typography:
  heading:
    family: "Manrope, -apple-system, sans-serif"
    weight: 700
    letter_spacing: "-0.025em"
  display:
    family: "Manrope, -apple-system, sans-serif"
    weight: 800
    letter_spacing: "-0.04em"
  body:
    family: "Manrope, -apple-system, sans-serif"
    weight: 400
  scale:
    display: "104px"
    h1: "44px"
    h2: "24px"
    body: "14px"
    caption: "11px"

spacing:
  baseline: "8px"
  slide_padding: "72px 96px"
  gap_large: "56px"
  gap_medium: "24px"
  gap_small: "12px"
  line_height: 1.8

radius:
  base: "10px"
  card: "16-20px"
  pill: "100px"
  icon: "10-14px"

shadow:
  none: true
---

# Breathe — Design Specification

## 气质

清新、干净、自然。纯白底上只有一种鼠尾草绿说话，搭配手绘线描叶子和有机形状。像清晨的空气——留白充裕，行距宽松，不使用任何阴影。视觉上的安静来自色彩的极度克制和呼吸般的间距。

## 色彩规则

- **背景**：纯白 `#FFFFFF`。
- **前景**：深墨绿灰 `#2D3D35`，正文用 `#4A5D50`，辅助文字用 `#8A9A8E`。
- **主色**：鼠尾草绿 `#A8C4A2`，用于图标、线条、圆点、进度条、强调文字。
- **深色变体**：`#6B8F6B` 用于数字、标题中的强调词。
- **浅色变体**：`#E8F0E6`（标签底、图标底）和 `#F4F8F2`（卡片底、圆形装饰）。
- **禁止**：第二种彩色、阴影、渐变（有机形状除外）、深色背景。

## 字体规则

- 全程使用 **Manrope**，现代几何无衬线。
- 标题字重 700-800，字距 -0.025em 至 -0.04em。
- 正文字重 400，行高 1.7-1.8，比常规更宽松。
- 标签用大写 + 0.1em 字距，鼠尾草绿浅底 + 深绿文字。

## 版式规则

- 留白占比高，slide padding 大（72px 96px）。
- 封面：左侧大标题，右侧 320px 线描叶子 SVG，左上角有机形状色块。
- 章节页：左对齐标题，右上角大圆斑，右下角小叶子装饰。
- 内容页：左栏引导文（18px，行高 1.8，关键词用鼠尾草绿高亮下划线），右栏带叶子图标的要点列表。
- 双栏页：两张 20px 圆角卡片，一张白底带 1px 描边，一张淡鼠尾草绿底。
- 数据页：四栏淡绿底卡片（16px 圆角），深绿大数字 + 进度条。

## 组件模式

- **标签**：100px 胶囊，`#E8F0E6` 底，`#6B8F6B` 文字，前面一个绿色小圆点。
- **叶子图标**：36px 圆角方块（10px），`#E8F0E6` 底，放 emoji 或 SVG 叶子。
- **有机形状**：用 `border-radius: 60% 40% 50% 50% / 50% 60% 40% 50%` 创建不规则圆形，`#E8F0E6` 色。
- **线描叶子**：SVG 手绘风格，1.5px 鼠尾草绿描边，无填充，含叶脉线条。
- **进度条**：4px 高，`#E8F0E6` 底，`#A8C4A2` 填充。
- **高亮**：文字背景用 `linear-gradient(transparent 60%, #E8F0E6 60%)` 模拟荧光笔。

## Do / Don't

- **Do** 保持纯白底，只用鼠尾草绿一个色系。
- **Do** 用线描 SVG 叶子增加自然感。
- **Do** 行距和 padding 比常规更宽松。
- **Don't** 不要使用任何阴影。
- **Don't** 不要引入绿色以外的彩色。
- **Don't** 不要使用深色背景。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景纯白，唯一的颜色是鼠尾草绿系（`#A8C4A2` / `#6B8F6B` / `#E8F0E6` / `#F4F8F2`）。字体全程 Manrope，行高 1.7-1.8。无阴影。装饰元素使用 SVG 线描叶子（1.5px 描边无填充）和有机形状色块。卡片用 16-20px 圆角，白底或淡绿底。禁止引入第二种彩色或使用阴影。
