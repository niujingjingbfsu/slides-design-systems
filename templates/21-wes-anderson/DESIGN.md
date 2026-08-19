---
name: Wes Anderson
version: 1.0.0
category: film-cinematic
tags: [wes-anderson, symmetry, pastel, vintage, film, cream, centered]

color:
  background: "#F5E6D3"
  foreground: "#5C4A32"
  pink: "#E8B4B8"
  mint: "#A8C4B8"
  mustard: "#D4C896"
  gold: "#C4A265"
  brown_light: "#8B6F47"
  white: "#FBF7F0"

typography:
  heading:
    family: "Jost, Noto Serif SC, sans-serif"
    weight: 600
    letter_spacing: "0.02-0.04em"
  body:
    family: "Noto Serif SC, serif"
    weight: 400
  display:
    family: "Jost, Noto Serif SC, sans-serif"
    weight: "300-600"
    letter_spacing: "0.3-0.5em"
  scale:
    display: "96px"
    h1: "88px"
    h2: "44px"
    body: "15px"
    caption: "11px"

spacing:
  slide_padding: "72px 100px"
  gap_large: "28px"
  gap_medium: "20px"

radius:
  base: "0px"
  dot: "50%"

shadow:
  none: true

border:
  width: "1px"
  style: "solid"
  color: "#C4A265"

progress_bar:
  height: "56px"
  background: "var(--cream)"
  border_top: "1px solid var(--gold)"
  section_label:
    font: "var(--font-display)"
    size: "12px"
    weight: "700"
    color: "var(--brown-light)"
    letter_spacing: "0.25em"
  page_number:
    font: "var(--font-display)"
    size: "16px"
    weight: "700"
    color: "var(--brown)"
    letter_spacing: "0.1em"
  segments:
    shape: "circle"
    size: "10px"
    gap: "5px"
    section_gap: "26px"
    future: "faint fill; 1px solid rgba(92,74,50,0.2); w=10px, h=10px"
    past: "medium fill; rgba(92,74,50,0.4)"
    current: "var(--pink) fill; var(--pink); w=14px, h=14px"

---

# Wes Anderson — Design Specification

## 气质

韦斯·安德森电影美学的抽象转译。严格对称的构图、低饱和粉彩色系、复古画框与角标、Futura 式几何无衬线字体。像《布达佩斯大饭店》的粉色电梯、《月升王国》的童子军徽章——精致、怀旧、带一点冷幽默。

## 色彩规则

- **背景**：暖奶油色 `#F5E6D3`，不是纯白。
- **三粉彩**：灰粉 `#E8B4B8`、薄荷 `#A8C4B8`、芥末 `#D4C896`，用于色块、圆点、卡片强调。
- **金色** `#C4A265`：画框线、分隔线、角标。
- **棕色** `#5C4A32`：所有文字颜色。
- **禁止**：高饱和色、渐变色、深色背景、阴影。

## 字体规则

- 英文用 **Jost**（Futura 的 Google Fonts 替代），字重 300-600，大字距。
- 中文用 **Noto Serif SC**，与 Jost 的几何感搭配。
- 标签/页脚用小号大写字母 + 0.3-0.5em 字距。

## 版式规则

- **绝对对称**：所有内容水平居中，左右元素镜像。
- **复古画框**：每页有 1px 金色内边框 + 四角 L 形角标。
- **粉彩圆点**：作为装饰元素散落，低透明度，不遮挡内容。
- 卡片为白底 + 1px 金色边框，无圆角无阴影。
- 双栏用粉/薄荷实色背景。

## 组件模式

- **画框**：`position: absolute` 的 1px 金色边框，距边缘 28px。
- **角标**：四个 16px 的 L 形金色线条。
- **圆点**：`border-radius: 50%`，粉彩填充，opacity 0.5。
- **分隔线**：60-80px 宽，1px 金色，居中。
- **卡片**：白底 + 金色边框，顶部有彩色圆点。

## Do / Don't

- **Do** 保持严格对称，所有内容居中。
- **Do** 用粉彩色块和圆点做装饰。
- **Do** 用 Jost 大写字母做标签和页脚。
- **Don't** 不要用圆角、阴影、渐变。
- **Don't** 不要打破对称构图。
- **Don't** 不要用高饱和色或深色背景。

## 实现注意事项

- 字体栈：`'Jost', 'Noto Serif SC', sans-serif`。Jost 是 Futura 的 Google Fonts 替代，不要用其他无衬线字体。
- 页脚是深色文字在奶油色背景上，无 bottom-band。footer 高 40px，content-area padding-bottom 60px。
- nav-hint 在 `bottom: 52px`（footer 40px + 12px 间距）。
- 画框和角标用 `pointer-events: none`，z-index 5-6，内容 z-index 2。
- 粉彩圆点装饰必须 `pointer-events: none` 且 z-index 1，不能遮挡文字。
- 所有卡片/双栏/指标容器 `overflow: hidden`。
- 标签文字（card-num, col-num）加 `white-space: nowrap`。
- 数据页 4 列指标，第 2、3 个有粉彩背景。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景为暖奶油色 #F5E6D3。每页有 1px 金色 #C4A265 复古画框和四角 L 形角标。英文用 Jost（Futura 风格），中文用 Noto Serif SC。装饰元素为灰粉 #E8B4B8、薄荷 #A8C4B8、芥末 #D4C896 的半透明圆点。严格对称居中构图。卡片白底+金色边框无圆角无阴影。禁止渐变、阴影、高饱和色。
