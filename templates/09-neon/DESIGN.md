---
name: Neon
version: 1.0.0
category: bold-colorful
tags: [synthwave, neon, retro-future, dark, glow, grid]

color:
  background_gradient: "linear-gradient(180deg, #1A0533 0%, #0D0221 60%, #05010F 100%)"
  foreground: "#FFFFFF"
  muted: "#8B7FB0"
  pink: "#FF2E97"
  cyan: "#00F0FF"
  purple: "#B026FF"

typography:
  heading:
    family: "Orbitron, sans-serif"
    weight: 700-900
    letter_spacing: "0.02em"
  body:
    family: "JetBrains Mono, monospace"
    weight: 400
  scale:
    display: "120px"
    h1: "80px"
    h2: "26px"
    body: "13px"
    caption: "11px"

spacing:
  slide_padding: "56px 72px"
  gap_large: "28px"
  gap_medium: "24px"

radius:
  base: "0px"
  card: "0px"

shadow:
  glow_pink: "0 0 10px #FF2E97, 0 0 20px #FF2E97, 0 0 40px rgba(255,46,151,0.5)"
  glow_cyan: "0 0 10px #00F0FF, 0 0 20px #00F0FF, 0 0 40px rgba(0,240,255,0.5)"
  card: "0 0 20px rgba(255,46,151,0.15)"

border:
  card: "1px solid rgba(255,46,151,0.4)"
  card_cyan: "1px solid rgba(0,240,255,0.4)"
---

# Neon — Design Specification

## 气质

合成波/复古未来主义。深紫黑的夜幕下，霓虹粉和电光青发光，透视网格延伸向地平线。像 1984 年的未来想象——电子、迷幻、怀旧又前卫。

## 色彩规则

- **背景**：深紫到黑的垂直线性渐变（`#1A0533` → `#0D0221` → `#05010F`）。
- **霓虹粉** `#FF2E97`：用于标题发光、强调文字、边框、太阳。
- **电光青** `#00F0FF`：用于标签、数据、次要发光、网格线。
- **紫色** `#B026FF`：辅助氛围色。
- 所有发光文字必须有 `text-shadow` 霓虹辉光（至少两层：10px + 20px）。
- **禁止**：暖色、柔和色、纯白背景、无发光的彩色文字。

## 字体规则

- 标题用 **Orbitron**，字重 700-900，几何未来感。
- 正文和标签用 **JetBrains Mono** 等宽字体，大写 + 0.15-0.4em 字距。
- 标题可用粉到青的渐变文字（`background-clip: text`）+ drop-shadow 发光。
- 标签前可加 `//` 或 `[ ]` 等终端符号。

## 版式规则

- 每页底部有**透视网格地板**：CSS perspective 变换的水平/垂直线条，粉色和青色半透明。
- 封面右上角有**条纹太阳**：粉到橙渐变圆形，下半部被水平条纹切割。
- 背景可加白色星点（2px 圆点 + box-shadow 发光）。
- 内容卡片：半透明深紫底 + 1px 霓虹色描边 + 发光阴影，零圆角。
- 金句和章节页居中对称。
- 数据页四栏卡片，奇数粉色发光数字，偶数青色发光数字。

## 组件模式

- **网格地板**：`perspective(400px) rotateX(60deg)`，`background-image` 双线网格，粉色水平 + 青色垂直。
- **太阳**：180px 圆形，粉橙渐变，`box-shadow` 大范围粉色辉光，`::after` 用 repeating-linear-gradient 做条纹切割。
- **卡片**：`rgba(26,5,51,0.6)` 底 + `backdrop-filter: blur(8px)` + 1px 霓虹描边 + 发光阴影。
- **发光文字**：`text-shadow: 0 0 10px [color], 0 0 20px [color], 0 0 40px [color]/0.5`。
- **星点**：绝对定位的 2px 白色圆点 + `box-shadow: 0 0 4px #fff`。

## Do / Don't

- **Do** 所有霓虹色文字必须带 text-shadow 辉光。
- **Do** 每页加透视网格地板（可调整透明度）。
- **Do** 用等宽字体做标签和数据，增强终端感。
- **Don't** 不要使用圆角。
- **Don't** 不要使用柔和色或暖色。
- **Don't** 不要让霓虹色脱离深色背景单独使用。

## 实现注意事项

- 字体栈：`'Orbitron', 'JetBrains Mono', 'Noto Sans SC', sans-serif`。Orbitron 用于英文标题，中文回退 Noto Sans SC 700。
- **CSS 声明之间不能漏分号**。
- 深色背景 `#0A0A1A` + 霓虹发光效果（`text-shadow` / `box-shadow` with cyan/magenta）。
- 网格地平线用 CSS 或 SVG 实现。
- 霓虹边框卡片不要填充实色背景，用透明/半透明深色。
- 页脚青色/品红色文字在深色背景上。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景固定为深紫到黑的渐变。霓虹粉 #FF2E97 和电光青 #00F0FF 是仅有的两个强调色，所有彩色文字必须带 text-shadow 辉光（至少 0 0 10px 和 0 0 20px 两层）。标题用 Orbitron 700-900，正文标签用 JetBrains Mono 等宽大写。每页底部加 perspective 透视网格。卡片为半透明深紫底+1px霓虹描边+发光阴影，零圆角。封面加条纹太阳和星点。
