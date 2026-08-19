---
name: Wong Kar-wai
version: 1.0.0
category: cinema
tags: [wong-kar-wai, cinematic, moody, bokeh, film-grain, vignette, warm, nostalgia, handwritten]

color:
  background: "#1A0E0A"
  foreground: "#FFF0DC"
  amber: "#E8A040"
  red: "#C83020"
  green: "#2A8060"
  muted: "rgba(255,200,150,0.5)"

typography:
  heading:
    family: "Noto Serif SC, serif"
    weight: 900
    letter_spacing: "0.06-0.08em"
  body:
    family: "Noto Serif SC, serif"
    weight: 400
  accent:
    family: "Ma Shan Zheng, cursive"
    weight: 400
  scale:
    display: "96px"
    h1: "88px"
    h2: "44px"
    body: "15px"
    caption: "11px"

spacing:
  slide_padding: "72px 100px"
  gap_large: "28px"
  gap_medium: "16px"

radius:
  base: "0px"

shadow:
  glow: "0 0 30px rgba(200,80,40,0.3)"

border:
  width: "1px"
  style: "solid"
  color: "rgba(255,200,150,0.2)"
---

# Wong Kar-wai — Design Specification

## 气质

王家卫电影美学的抽象转译。暗暖底色、红绿对比色 wash、失焦光斑、胶片颗粒、暗角、光线条纹。衬线宋体 + 手写体点缀——情绪、暧昧、怀旧、时间感。

## 色彩规则

- **背景**：深暖黑 `#1A0E0A`。
- **三色 wash**：红 `#C83020`、绿 `#2A8060`、琥珀 `#E8A040`，用 `radial-gradient` 低透明度叠加。
- **文字**：暖白 `#FFF0DC`，辅助文字用 `rgba(255,200,150,0.3-0.5)`。
- 手写体用琥珀色 `#E8A040` + 暖光发光。
- **禁止**：实色卡片、硬边框、冷色调、高饱和荧光色。

## 字体规则

- 中文用 **Noto Serif SC**，标题 900，正文 400。
- **Ma Shan Zheng**（马善政手写体）仅用于关键词点缀，不用于整句。
- 标签用小号字 + 0.3-0.5em 字距，暖白低透明度。

## 版式规则

- **色彩 wash**：每页 2-3 个 `radial-gradient` 色块叠加，营造电影色彩氛围。
- **失焦光斑**：3-5 个 `border-radius: 50%` + `filter: blur(30px)` 的圆形。
- **胶片颗粒**：SVG `feTurbulence` 噪点纹理，opacity 0.1。
- **暗角**：`box-shadow: inset 0 0 180px 60px rgba(0,0,0,0.6)`。
- **光线条纹**：1-2 条斜向渐变细线，`filter: blur(1px)`。
- 卡片无边框，仅顶部 1px 暖色线 + 40px 短色线。
- 双栏用红/绿半透明背景 + 左侧 2px 色线。

## 实现注意事项

- 字体栈：`'Noto Serif SC', serif`；手写体 `'Ma Shan Zheng', cursive`。
- **Ma Shan Zheng 只用于 2-4 字关键词**（如"相遇""火花""框架"），不用于整句或标题主体。
- 色彩 wash 透明度控制在 0.12-0.35，不能影响文字可读性。
- 光斑 blur 至少 30px，直径 100-240px，opacity 通过 rgba alpha 控制。
- 颗粒用内联 SVG data URI，不要用外部图片。
- 暗角 z-index: 40，颗粒 z-index: 50，都要 `pointer-events: none`。
- 页脚无 bottom-band，暖白低透明度文字，高 40px。
- content-area padding-bottom 64px，nav-hint/counter 在 `bottom: 52px`。
- 所有容器 `overflow: hidden`。
- 卡片背景用 `rgba(255,240,220,0.04)`，几乎透明。

## 给 Coding Agent 的提示

> 背景深暖黑 #1A0E0A。红绿琥珀三色 radial-gradient wash 叠加。失焦光斑（blur 30px）+ 胶片颗粒（SVG noise）+ 暗角 + 光线条纹。中文 Noto Serif SC 900，Ma Shan Zheng 手写体仅点缀关键词。卡片无边框，仅顶部暖色细线。暖白文字。禁止实色卡片、硬边框、冷色。
