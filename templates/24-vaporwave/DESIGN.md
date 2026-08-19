---
name: Vaporwave
version: 1.0.0
category: digital-aesthetic
tags: [vaporwave, neon, 80s, retro-future, synthwave, grid, gradient, glow]

color:
  background: "linear-gradient(180deg, #2D1B5E, #1A0B2E, #0D0520)"
  foreground: "#FFFFFF"
  pink: "#FF71CE"
  cyan: "#01CDFE"
  purple: "#B967FF"
  yellow: "#FFFB96"
  green: "#05FFA1"
  dark: "#1A0B2E"

typography:
  heading:
    family: "Orbitron, Noto Serif SC, sans-serif"
    weight: 900
    letter_spacing: "0.02-0.04em"
  body:
    family: "Noto Serif SC, Orbitron, serif"
    weight: 400
  scale:
    display: "88px"
    h1: "80px"
    h2: "44px"
    body: "15px"
    caption: "10px"

spacing:
  slide_padding: "64px 80px"
  gap_large: "24px"
  gap_medium: "16px"

radius:
  base: "0px"

shadow:
  neon: "0 0 20px var(--pink)"

border:
  width: "1px"
  style: "solid"
  color: "rgba(255,113,206,0.3)"
---

# Vaporwave — Design Specification

## 气质

蒸汽波美学的抽象转译。粉/青/紫霓虹渐变、透视网格地平线、落日与棕榈树剪影、扫描线、发光文字。80 年代复古未来主义——数字时代的怀旧与反讽。

## 色彩规则

- **背景**：深紫渐变 `#2D1B5E → #1A0B2E → #0D0520`。
- **霓虹三色**：粉 `#FF71CE`、青 `#01CDFE`、紫 `#B967FF`。
- **点缀**：黄 `#FFFB96`、绿 `#05FFA1`。
- 文字白色 + `text-shadow` 霓虹发光。
- **禁止**：实色卡片、无发光的彩色文字、暖色渐变。

## 字体规则

- 英文用 **Orbitron 900**，几何未来感。
- 中文用 **Noto Serif SC**，与 Orbitron 的几何感形成对比。
- 标签用小号大写 + 0.3-0.5em 字距 + 青色发光。

## 版式规则

- **透视网格**：底部 SVG 网格，粉色纵向线 + 青色横向线，低透明度。
- **扫描线**：全站覆盖 `repeating-linear-gradient` 扫描线。
- **毛玻璃卡片**：`rgba(255,255,255,0.06)` + `backdrop-filter: blur()` + 霓虹边框。
- 双栏用粉/青半透明背景。
- 底部半透明栏 + 模糊效果。

## 实现注意事项

- 字体栈：`'Orbitron', 'Noto Serif SC', sans-serif`。
- **卡片必须用毛玻璃半透明**（`rgba(255,255,255,0.06-0.12)` + `backdrop-filter: blur(4-8px)`），禁止实色白卡片。
- 霓虹发光用 `text-shadow` 和 `box-shadow`，不要用 `filter: drop-shadow`（性能差）。
- 透视网格用 SVG 绘制，`preserveAspectRatio="none"` 拉伸。
- 扫描线 z-index: 50，`pointer-events: none`。
- 底部栏高 50px，`rgba(13,5,32,0.7)` + `backdrop-filter: blur(8px)`。
- content-area padding-bottom 72px，nav-hint/counter 在 `bottom: 62px`。
- 所有容器 `overflow: hidden`。
- 棕榈树剪影用内联 SVG，不要用图片或 emoji。

## 给 Coding Agent 的提示

> 背景深紫渐变 #2D1B5E→#0D0520。霓虹粉 #FF71CE、青 #01CDFE、紫 #B967FF。底部透视网格（SVG），全站扫描线。英文 Orbitron 900，中文 Noto Serif SC。卡片毛玻璃半透明 + 霓虹边框 + 发光。底部半透明模糊栏。禁止实色卡片、暖色渐变。
