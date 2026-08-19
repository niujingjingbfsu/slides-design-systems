---
name: Memphis
version: 1.0.0
category: bold-colorful
tags: [memphis, postmodern, geometric, playful, 80s, squiggles]

color:
  background: "#F5F0E8"
  foreground: "#000000"
  pink: "#FF6B9D"
  cyan: "#00C9C9"
  yellow: "#FFD93D"
  red: "#FF4757"

typography:
  heading:
    family: "Archivo Black, sans-serif"
    weight: 400
    letter_spacing: "0"
    text_transform: "uppercase"
  body:
    family: "Inter, -apple-system, sans-serif"
    weight: 600
  scale:
    display: "120px"
    h1: "96px"
    h2: "28px"
    body: "14px"
    caption: "12px"

spacing:
  slide_padding: "56px 72px"
  gap_large: "28px"
  gap_medium: "24px"

radius:
  base: "0px"
  circle: "50%"

shadow:
  card_pink: "12px 12px 0 #FF6B9D"
  none: true

border:
  width: "3-4px"
  style: "solid"
  color: "#000000"

progress_bar:
  height: "56px"
  background: "transparent"
  border_top: "none"
  section_label:
    font: "var(--font-sans)"
    size: "11px"
    weight: "700"
    color: "rgba(0,0,0,0.4)"
    letter_spacing: "0.3em"
  page_number:
    font: "var(--font-display)"
    size: "14px"
    weight: "900"
    color: "var(--black, #222)"
    letter_spacing: "0.05em"
    current_color: "var(--pink, #FF6B9D)"
  segments:
    shape: "circle"
    size: "10px"
    gap: "5px"
    section_gap: "26px"
    future: "#fff fill; 2px solid var(--black, #222); w=10px, h=10px"
    past: "var(--black, #222) fill"
    current: "var(--pink, #FF6B9D) fill; var(--black, #222); w=14px, h=14px; shadow: 3px 3px 0 var(--black, #222)"

---

# Memphis — Design Specification

## 气质

孟菲斯后现代主义。奶油色底上散落着亮粉、青、黄的几何图形，黑色波浪线和棋盘格穿插其间。1980 年代米兰的反叛精神—— playful、喧闹、拒绝严肃，但每个元素的位置都有节奏。

## 色彩规则

- **背景**：暖奶油 `#F5F0E8`（不是纯白，带一点温度）。
- **前景**：纯黑 `#000000`。
- **亮粉** `#FF6B9D`：主强调色，圆形、卡片底、文字。
- **青** `#00C9C9`：三角形、卡片底、文字描边。
- **黄** `#FFD93D`：方块、标签底、高亮背景。
- **红** `#FF4757`：小圆点、点缀。
- **禁止**：渐变色、柔和色、灰色调、零色彩的页面。

## 字体规则

- 标题用 **Archivo Black**，全大写，字号大（封面 120px）。
- 可用 `-webkit-text-stroke: 3px #000` 做空心字（青色填充）。
- 正文用 **Inter**，字重 600-800。
- 标签用大写，可微旋转（±1-2 度）。

## 版式规则

- 画面中**散落几何装饰**：圆形（4px 黑描边）、三角形（CSS border 三角 + drop-shadow）、旋转方块（4px 黑描边，rotate 15-20deg）。
- **黑色波浪线**（squiggles）：SVG path `Q` 贝塞尔曲线，3px 黑色描边，round linecap，散落在各处。
- **棋盘格**：`conic-gradient` 或 `repeating-conic-gradient` 做 20px 黑白棋盘，4px 黑描边框。
- 装饰元素可微旋转，位置随意但有节奏，不要对称排列。
- 内容卡片：4px 黑描边，零圆角，底色轮换（粉/青/黄）。
- 金句页：白色卡片 + 4px 黑描边 + 12px 粉色硬投影 + 微旋转 -1 度。
- 双栏页：白底 + 黑底反转。

## 组件模式

- **波浪线**：`<svg viewBox="0 0 80 20"><path d="M0 10 Q10 0 20 10 T40 10 T60 10 T80 10" stroke="#000" stroke-width="3" fill="none" stroke-linecap="round"/></svg>`，可旋转 45 度。
- **棋盘格**：`background: conic-gradient(#000 25%, #fff 0 50%, #000 0 75%, #fff 0); background-size: 20px 20px;` + 4px 黑描边。
- **圆形装饰**：`border-radius: 50%` + 4px 黑描边 + 彩色填充。
- **三角形**：`border-left/right: 50px solid transparent; border-bottom: 90px solid [color]` + `filter: drop-shadow(3px 3px 0 #000)`。
- **旋转方块**：4px 黑描边 + `transform: rotate(15deg)`。
- **卡片**：4px 黑描边，零圆角，彩色底，padding 28px。

## Do / Don't

- **Do** 每页至少散落 3-5 个几何装饰元素。
- **Do** 用黑色波浪线和棋盘格增加孟菲斯签名感。
- **Do** 让装饰元素微旋转，打破对称。
- **Don't** 不要使用渐变或柔和阴影。
- **Don't** 不要让装饰元素排成直线或对称。
- **Don't** 不要使用纯白背景——必须是奶油色。

## 实现注意事项

- 字体栈：`'Archivo Black', 'Inter', 'Noto Sans SC', sans-serif`。
- **CSS 声明之间不能漏分号**。
- 装饰元素（圆形、三角形、波浪线、棋盘格）用 SVG 实现，必须 `pointer-events: none`。
- **装饰元素不能遮挡标题文字**——注意 z-index 层级和位置。
- 粉/青/黄三色 + 黑色粗边框，不要用其他颜色。
- 卡片有轻微偏移（`transform: rotate(-1deg)` 等），但不要超过 2 度。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景固定为奶油色 #F5F0E8。每页散落亮粉/青/黄的几何形状（圆形、三角形、旋转方块，都带 3-4px 黑描边）和黑色 SVG 波浪线。可加黑白棋盘格方块。标题用 Archivo Black 全大写。卡片 4px 黑描边零圆角，底色轮换粉/青/黄。金句白卡+粉色硬投影+微旋转。禁止渐变、柔和阴影、纯白背景。
