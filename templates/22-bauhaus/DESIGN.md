---
name: Bauhaus
version: 1.0.0
category: art-movement
tags: [bauhaus, geometric, primary-colors, functional, black-lines, circles, triangles]

color:
  background: "#F5F1E8"
  foreground: "#111111"
  red: "#E63946"
  yellow: "#F4D35E"
  blue: "#1D3557"

typography:
  heading:
    family: "Inter, Noto Sans SC, sans-serif"
    weight: 900
    letter_spacing: "-0.02em"
  body:
    family: "Noto Sans SC, Inter, sans-serif"
    weight: 400
  scale:
    display: "104px"
    h1: "96px"
    h2: "44px"
    body: "15px"
    caption: "11px"

spacing:
  slide_padding: "64px 80px"
  gap_large: "24px"
  gap_medium: "16px"

radius:
  base: "0px"
  circle: "50%"

shadow:
  none: true

border:
  width: "3px"
  style: "solid"
  color: "#111111"

progress_bar:
  height: "60px"
  background: "transparent"
  border_top: "none"
  position: "strip inside the bar — top: 50%; transform: translateY(-50%); NOT negative top (dots would collide with card bottom borders)"
  slide_padding_bottom: "96px"
  segments:
    shape: "circle"
    size: "12px (current 16px)"
    gap: "5px"
    section_gap: "5px (uniform)"
    future: "rgba(0,0,0,0.1) fill; 2px solid rgba(0,0,0,0.2)"
    past: "var(--black) fill; var(--black) border"
    current: "var(--yellow) fill; var(--black) border; 3px 3px 0 var(--red) offset shadow (Bauhaus signature)"
  clickable: "yes — each segment jumps to its page; never set pointer-events:none"

---

# Bauhaus — Design Specification

## 气质

包豪斯设计语言的抽象转译。三原色（红/黄/蓝）+ 黑 + 米白，圆方三角几何元素，粗黑线条分割空间，无衬线粗体字。功能主义、理性、经典——每个元素都有其存在的理由。

## 色彩规则

- **背景**：暖米白 `#F5F1E8`。
- **三原色**：红 `#E63946`、黄 `#F4D35E`、蓝 `#1D3557`。
- **黑色** `#111`：线条、边框、文字、底部栏。
- **禁止**：渐变色、阴影、圆角（圆形元素除外）、中间色。

## 字体规则

- 英文用 **Inter 900**，紧字距 -0.02em。
- 中文用 **Noto Sans SC 900**。
- 标签用小号大写字母 + 0.3-0.5em 字距，黑底黄字或黑字。

## 版式规则

- **几何分割**：用粗黑线条（3-4px）和色块分割画面。
- **圆方三角**：圆形=红，方形=黄，三角形=蓝，贯穿全套。
- **黑色底栏**：每页底部 60px 黑底白字栏（封面 80px）。
- 卡片为米白底 + 3px 黑边框 + 8px 彩色顶边。
- 双栏用红/黄实色背景。

## 实现注意事项

- 字体栈：`'Inter', 'Noto Sans SC', sans-serif`。
- **底部黑栏高度**：普通页 60px，封面 80px。content-area padding-bottom 80px（封面 120px）。
- **nav-hint/counter 在 `bottom: 76px`**（60px 栏 + 16px 间距）；封面页在 `bottom: 96px`。
- 装饰几何元素必须 `pointer-events: none; z-index: 1`，内容 z-index 2+。
- 封面有红色左面板（380px 宽），注意内容区 padding-left: 460px。
- 数据页 4 列，颜色交替：米白/红/黄/蓝。
- 所有容器 `overflow: hidden`。

## 给 Coding Agent 的提示

> 背景米白 #F5F1E8。三原色红 #E63946、黄 #F4D35E、蓝 #1D3557，黑色 #111。粗黑线条和 3px 黑边框。圆=红、方=黄、三角=蓝。每页底部 60px 黑底白字栏。英文 Inter 900，中文 Noto Sans SC 900。禁止渐变、阴影、圆角。
