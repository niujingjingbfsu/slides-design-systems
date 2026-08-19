---
name: Tropic
version: 1.0.0
category: bold-colorful
tags: [tropical, teal, coral, yellow, rounded, summer, energetic]

color:
  background: "#0A3D3D"
  foreground: "#FFFFFF"
  coral: "#FF6B47"
  yellow: "#FFD23F"
  teal_light: "#14A098"
  muted: "rgba(255,255,255,0.7)"

typography:
  heading:
    family: "Fredoka, sans-serif"
    weight: 700
    letter_spacing: "-0.02em"
  body:
    family: "Inter, -apple-system, sans-serif"
    weight: 500-600
  scale:
    display: "130px"
    h1: "100px"
    h2: "30px"
    body: "14px"
    caption: "12px"

spacing:
  slide_padding: "64px 80px"
  gap_large: "28px"
  gap_medium: "24px"

radius:
  base: "24px"
  card: "24px"
  pill: "100px"
  icon: "18px"
  lg: "28px"

shadow:
  sun_glow: "0 0 100px rgba(255,210,63,0.3)"
  card: "none"

progress_bar:
  height: "56px"
  background: "var(--cream, #FFF8F0)"
  border_top: "2px solid var(--ink, #2D1B0E)"
  section_label:
    font: "var(--font-sans)"
    size: "12px"
    weight: "700"
    color: "rgba(45,27,14,0.6)"
    letter_spacing: "0.25em"
  page_number:
    font: "var(--font-sans)"
    size: "16px"
    weight: "700"
    color: "var(--coral, #FF6B4A)"
    letter_spacing: "0.1em"
  segments:
    shape: "circle"
    size: "10px"
    gap: "5px"
    section_gap: "26px"
    future: "faint fill; 2px solid rgba(45,27,14,0.2); w=10px, h=10px"
    past: "medium fill; rgba(45,27,14,0.4)"
    current: "var(--coral, #FF6B4A) fill; var(--coral, #FF6B4A); w=14px, h=14px"

---

# Tropic — Design Specification

## 气质

热带热力。深青色的丛林夜幕下，珊瑚橙和亮黄色像日落一样燃烧。圆润饱满的字体、大圆角卡片、热带叶子剪影——热烈、能量充沛、充满夏日感。撞色强烈但因为深青底的衬托而不显杂乱。

## 色彩规则

- **背景**：深青 `#0A3D3D`（不是黑色，带绿调的深色）。
- **前景**：纯白 `#FFFFFF`。
- **珊瑚橙** `#FF6B47`：主强调色，卡片底、CTA、叶子、数字。
- **亮黄** `#FFD23F`：太阳、标签底、高亮、次强调。
- **浅青** `#14A098`：第三卡片色、芯片标签。
- **辅助文字**：`rgba(255,255,255,0.7)`。
- **禁止**：冷色调蓝色、紫色、灰色调、浅色背景。

## 字体规则

- 标题用 **Fredoka**，圆润几何无衬线，字重 700，字距 -0.02em。
- 封面标题中的字母 "O" 可用珊瑚橙圆形替代（`display: inline-block; width: 0.9em; height: 0.9em; border-radius: 50%; background: #FF6B47`）。
- 正文用 **Inter**，字重 500-600。
- 标签用大写 + 0.08em 字距 + 半透明胶囊。

## 版式规则

- 封面右侧有**大太阳**：380px 亮黄圆形，带 100px 黄色辉光，配合珊瑚橙/黄色热带叶子 SVG 剪影。
- 叶子用 SVG path 绘制，珊瑚橙/黄色填充，深青色叶脉，可旋转 20 度叠加。
- 内容卡片：24px 大圆角，无描边，底色轮换（珊瑚/黄/半透明白）。
- 双栏页：一张半透明玻璃卡 + 一张亮黄实色卡（深青文字）。
- 金句页：背景一个大珊瑚色半透明圆形，白色圆润大字，黄色强调词。
- 数据页四栏大圆角卡片，四色轮换（珊瑚/黄/浅青/半透明白）。
- 按钮：珊瑚橙底 + 100px 胶囊圆角。

## 组件模式

- **太阳**：300-380px 圆形，`background: #FFD23F`，`box-shadow: 0 0 100px rgba(255,210,63,0.3)`，z-index: 0。
- **热带叶**：SVG path 绘制的龟背竹/棕榈叶剪影，珊瑚橙或黄色填充，可旋转叠加。
- **卡片**：24px 圆角，无描边，彩色或半透明白底（`rgba(255,255,255,0.1)` + 2px 白色半透明描边）。
- **胶囊标签**：`rgba(255,255,255,0.15)` + 100px 圆角，前面带黄色小圆点。
- **芯片**：100px 胶囊，珊瑚/黄/浅青三色轮换。
- **字母 O 替代**：标题中的 O 用珊瑚橙圆形 span 替代。

## Do / Don't

- **Do** 深青底是基础，珊瑚和黄是火焰。
- **Do** 用大圆角（24px+）和圆润字体。
- **Do** 加太阳和热带叶子 SVG 剪影。
- **Don't** 不要使用零圆角或尖锐形状。
- **Don't** 不要使用冷色（蓝、紫）。
- **Don't** 不要用浅色背景。

## 实现注意事项

- 字体栈：`'Outfit', 'Noto Sans SC', sans-serif`。**禁止用 Fredoka**——圆润字体和尖锐中文字体不协调。
- **CSS 声明之间不能漏分号**。
- 深青色背景 `#0D3B33`，卡片用橙/黄/青高饱和色，圆角 24px。
- **卡片与页脚间距必须 ≥ 20px**，不要紧贴。
- **标题与卡片间距必须 ≥ 32px**。
- 装饰 emoji（🔥☀️🌿等）只在卡片内使用，不要放在标题旁。
- 页脚白色文字在深青色背景上。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景固定为深青色 #0A3D3D。强调色为珊瑚橙 #FF6B47 和亮黄 #FFD23F。标题用 Fredoka 700 圆润字体，字母 O 可用珊瑚橙圆形替代。卡片 24px 大圆角无描边，底色轮换珊瑚/黄/半透明白。封面加 380px 黄色太阳（带辉光）和 SVG 热带叶子剪影。按钮 100px 胶囊。禁止冷色、零圆角、浅色背景。
