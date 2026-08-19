---
name: Risograph
version: 1.0.0
category: print-craft
tags: [risograph, print, halftone, misregistration, fluorescent, independent-press, zine]

color:
  background: "#F8F4E9"
  foreground: "#111111"
  pink: "#FF6B9D"
  blue: "#4ECDC4"
  yellow: "#FFE66D"

typography:
  heading:
    family: "Noto Sans SC, Space Mono, sans-serif"
    weight: 900
  body:
    family: "Noto Sans SC, Space Mono, sans-serif"
    weight: 400
  mono:
    family: "Space Mono, Noto Sans SC, monospace"
    weight: 700
    letter_spacing: "0.25-0.3em"
  scale:
    display: "96px"
    h1: "88px"
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
  none: true

border:
  width: "2px"
  style: "solid"
  color: "#111111"
---

# Risograph — Design Specification

## 气质

孔版印刷（Risograph）美学的抽象转译。限定荧光色叠印、套色错位、网点质感、黑色边框、对位标记。像独立出版物、Zine、朋克海报——不完美的、手工感的、每一张都略有不同。

## 色彩规则

- **背景**：暖纸白 `#F8F4E9`。
- **三色叠印**：荧光粉 `#FF6B9D`、荧光青 `#4ECDC4`、荧光黄 `#FFE66D`。
- **黑色** `#111`：文字、边框、对位标记。
- 色块用 `mix-blend-mode: multiply` 模拟油墨叠印效果。
- **禁止**：渐变色、阴影、圆角、非限定色。

## 字体规则

- 英文等宽用 **Space Mono 700**，标签/页脚/数字。
- 中文用 **Noto Sans SC 900** 标题。
- 大标题用 `text-shadow` 模拟套色错位（粉/青双色偏移 2-3px）。

## 版式规则

- **网点质感**：全站覆盖 `radial-gradient` 圆点纹理，opacity 0.08。
- **对位标记**：四角十字线，印刷套色标记。
- **2px 黑边框**：所有卡片、标签、按钮。
- 标签为黑边框 + 荧光黄底。
- 双栏用粉/青实色背景。

## 实现注意事项

- 字体栈：标题 `'Noto Sans SC', 'Space Mono', sans-serif`；等宽 `'Space Mono', 'Noto Sans SC', monospace`。
- 套色错位效果只用于大标题（text-shadow），不要用于正文（影响可读性）。
- 色块装饰用 `mix-blend-mode: multiply` + `transform: translate()` 偏移 3-4px。
- 网点纹理用 CSS `radial-gradient(circle, rgba(0,0,0,0.08) 1px, transparent 1px); background-size: 4px 4px`。
- 对位标记用 `::before` 和 `::after` 画十字线。
- 页脚深色文字无 bottom-band，高 40px，content-area padding-bottom 64px。
- nav-hint 在 `bottom: 52px`。
- 所有容器 `overflow: hidden`。

## 给 Coding Agent 的提示

> 背景纸白 #F8F4E9。荧光粉 #FF6B9D、青 #4ECDC4、黄 #FFE66D 三色叠印，用 mix-blend-mode: multiply。大标题用 text-shadow 模拟套色错位。全站网点纹理 + 四角对位标记 + 2px 黑边框。英文 Space Mono，中文 Noto Sans SC 900。禁止渐变、阴影、圆角。
