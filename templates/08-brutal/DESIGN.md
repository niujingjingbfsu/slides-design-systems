---
name: Brutal
version: 1.0.0
category: bold-colorful
tags: [neo-brutalism, bold, borders, hard-shadows, primary-colors, raw]

color:
  background: "#FFFFFF"
  foreground: "#000000"
  red: "#E63946"
  yellow: "#FFD93D"
  blue: "#2563EB"
  green: "#22C55E"

typography:
  heading:
    family: "Archivo Black, sans-serif"
    weight: 400
    letter_spacing: "-0.02em"
    text_transform: "uppercase"
  body:
    family: "Inter, -apple-system, sans-serif"
    weight: 600
  scale:
    display: "130px"
    h1: "48px"
    h2: "24px"
    body: "14px"
    caption: "13px"

spacing:
  slide_padding: "56px 72px"
  gap_large: "28px"
  gap_medium: "24px"
  gap_small: "12px"

radius:
  base: "0px"

shadow:
  card: "8px 8px 0 #000"
  card_sm: "4px 4px 0 #000"
  card_lg: "12px 12px 0 #000"
  blur: "0"

border:
  width: "4px"
  style: "solid"
  color: "#000000"

progress_bar:
  height: "56px"
  background: "var(--black, #111)"
  border_top: "none"
  section_label:
    font: "var(--font-sans)"
    size: "12px"
    weight: "700"
    color: "rgba(255,255,255,0.7)"
    letter_spacing: "0.25em"
  page_number:
    font: "var(--font-sans)"
    size: "16px"
    weight: "700"
    color: "var(--yellow, #FFD600)"
    letter_spacing: "0.1em"
  segments:
    shape: "line"
    size: "6px"
    gap: "5px"
    section_gap: "22px"
    future: "faint fill; 1px solid rgba(255,255,255,0.25); w=40px, h=6px"
    past: "medium fill; rgba(255,255,255,0.5)"
    current: "var(--yellow, #FFD600) fill; var(--yellow, #FFD600)"

---

# Brutal — Design Specification

## 气质

新粗野主义。厚黑边框、硬边投影、三原色，像大字报一样直接生猛。没有圆角、没有渐变、没有柔和阴影——每个元素都像用剪刀剪出来再贴上去的，带着手工拼贴的 raw 感。

## 色彩规则

- **背景**：纯白 `#FFFFFF`。
- **前景**：纯黑 `#000000`，所有描边和文字都是纯黑。
- **强调色**：红 `#E63946`、黄 `#FFD93D`、蓝 `#2563EB`，直接从颜料管里挤出来的原色。
- 彩色用于：卡片底色、圆形/三角形等几何形状、标签、数字。
- **禁止**：渐变色、柔和色、透明度过渡、灰色系。

## 字体规则

- 标题用 **Archivo Black**，全大写，字距 -0.02em，字号极大（封面 130px）。
- 正文用 **Inter**，字重 600-800，不要用细体。
- 标签用大写 + 0.05-0.1em 字距。
- 可用 `-webkit-text-stroke: 3px #000` 给文字加黑描边（空心字效果）。

## 版式规则

- 所有容器必须有 **4px 黑色描边 + 硬投影**（8px 右下偏移，0 模糊，纯黑）。
- 零圆角，零渐变，零柔和阴影。
- 封面：左侧大标题，右侧堆叠彩色几何形状（方块、圆形、三角形），都带描边和投影。
- 内容页：三栏卡片，每卡不同底色（黄/白/红），形成强烈节奏。
- 双栏页：一张白底一张黑底反转。
- 金句页：黄色卡片带 1-2 度微旋转 + 红色硬投影，像贴上去的纸条。
- 元素可以微旋转（1-3 度）增加手工感。

## 组件模式

- **卡片**：4px 黑描边 + 8px 硬投影，padding 28px，零圆角。
- **标签**：黑底白字或彩色底黑字，4px 描边，padding 6-8px 16-20px。
- **几何形状**：方块（4px 描边+投影）、圆形（border-radius:50%+描边）、三角形（CSS border 三角 + drop-shadow）。
- **按钮**：彩色底 + 4px 黑描边 + 6px 硬投影。

## Do / Don't

- **Do** 给每个元素加 4px 黑描边和硬投影。
- **Do** 使用红/黄/蓝三原色，越直接越好。
- **Do** 让卡片用不同底色形成撞色节奏。
- **Don't** 不要使用任何圆角。
- **Don't** 不要使用 box-shadow blur（模糊），投影必须是硬边。
- **Don't** 不要使用渐变或柔和色。
- **Don't** 不要使用细字体。

## 实现注意事项

- 字体栈：`'Archivo Black', 'Inter', 'Noto Sans SC', sans-serif`。Archivo Black 用于英文标题，中文回退 Noto Sans SC 900。
- **CSS 声明之间不能漏分号**，特别是 `font-family` 和 `font-size` 之间。
- 粗黑边框（3-4px solid #000）+ 偏移阴影（`box-shadow: 6px 6px 0 #000`），不要用柔和阴影。
- 高饱和黄/红/蓝色块，不要渐变。
- 内容页用 3 列卡片网格，卡片有粗黑边框。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。所有元素必须有 4px 纯黑描边和硬投影（8px 8px 0 #000，零模糊）。零圆角。背景纯白。标题用 Archivo Black 全大写。强调色只用红 #E63946、黄 #FFD93D、蓝 #2563EB。卡片用不同底色撞色。禁止渐变、柔和阴影、细字体。元素可微旋转 1-3 度增加手工感。
