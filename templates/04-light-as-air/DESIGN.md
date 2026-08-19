---
name: Light as Air
version: 1.0.0
category: light-airy
tags: [glassmorphism, gradient, ethereal, floating, lavender, blur]

color:
  background_gradient: "linear-gradient(135deg, #FFFFFF 0%, #EEF1FA 45%, #E4E9F8 100%)"
  foreground: "#1E2A5E"
  muted: "#6B7A99"
  glass: "rgba(255, 255, 255, 0.45)"
  glass_border: "rgba(255, 255, 255, 0.7)"
  lavender: "#B8C0E8"
  sky: "#A8D8E8"
  blush: "#E8D0E8"
  indigo: "#1E2A5E"

typography:
  heading:
    family: "Sora, -apple-system, sans-serif"
    weight: 600
    letter_spacing: "-0.025em"
  display:
    family: "Sora, -apple-system, sans-serif"
    weight: 700
    letter_spacing: "-0.035em"
  body:
    family: "Sora, -apple-system, sans-serif"
    weight: 300
  scale:
    display: "92px"
    h1: "44px"
    h2: "26px"
    body: "14px"
    caption: "11px"

spacing:
  baseline: "8px"
  slide_padding: "64px 80px"
  gap_large: "48px"
  gap_medium: "24px"
  gap_small: "16px"

radius:
  base: "24px"
  card: "24px"
  pill: "100px"
  lg: "32px"

shadow:
  card: "0 8px 32px rgba(30, 42, 94, 0.08)"
  card_lg: "0 24px 64px rgba(30, 42, 94, 0.12)"
  button: "0 12px 32px rgba(30, 42, 94, 0.25)"

glass:
  background: "rgba(255, 255, 255, 0.45)"
  backdrop_filter: "blur(20px) saturate(1.4)"
  border: "1px solid rgba(255, 255, 255, 0.7)"
---

# Light as Air — Design Specification

## 气质

通透、梦幻、失重。磨砂玻璃卡片漂浮在淡蓝紫渐变之上，彩色光球在背景中弥散。深度来自模糊和光线，不来自厚重的阴影或边框。整体感觉像呼吸一样轻。

## 色彩规则

- **背景**：135deg 渐变，白 → `#EEF1FA` → `#E4E9F8`。
- **前景**：深靛蓝 `#1E2A5E`，正文用 `#6B7A99`。
- **氛围色**：薰衣草紫 `#B8C0E8`、天空蓝 `#A8D8E8`、淡粉紫 `#E8D0E8`，用于模糊光球和图标底色。
- **玻璃面**：`rgba(255,255,255,0.45)` + `backdrop-filter: blur(20px) saturate(1.4)` + 1px 白色半透明描边。
- **标题渐变**：大号标题可用深靛蓝到薰衣草紫的渐变文字（`-webkit-background-clip: text`）。
- **禁止**：纯色不透明背景、硬边描边、暖色为主色。

## 字体规则

- 全程使用 **Sora**，几何感无衬线。
- 标题字重 600-700，字距 -0.025em 至 -0.035em。
- 正文字重 300，行高 1.6-1.7。
- 标签用大写 + 0.12em 字距，前面加一个渐变小圆点。

## 版式规则

- 封面：左侧大标题，右侧浮动玻璃小卡片（220px 宽，显示数字+标签）。
- 章节页：居中大玻璃卡片（圆角 32px），内含编号、标题、描述。
- 内容页：三栏玻璃卡片，每卡有渐变图标块 + 标题 + 说明。
- 双栏页：左玻璃卡 + 右深靛蓝实色卡（`#1E2A5E` → `#3A4A8E` 渐变）形成虚实对比。
- 金句页：居中大玻璃卡片，引号内可用渐变文字强调关键词。

## 组件模式

- **玻璃卡片**：24px 圆角，半透明白底，20px 模糊，1px 白色描边，柔和阴影。
- **光球**：200-500px 正圆，薰衣草/天蓝/粉紫，`blur(40px)`，透明度 25%-50%，位于内容层下方。
- **实心卡**：深靛蓝渐变底，白色文字，用于需要聚焦的 featured 内容。
- **图标块**：56px 圆角方块（18px 圆角），渐变色半透明底。
- **按钮**：100px 胶囊，深靛蓝底白字，带靛蓝色发光阴影。

## Do / Don't

- **Do** 所有卡片使用磨砂玻璃效果（backdrop-filter blur）。
- **Do** 在背景层放置多个模糊光球营造氛围。
- **Do** 用渐变文字点缀标题关键词。
- **Don't** 不要使用不透明的白色卡片（必须半透明+模糊）。
- **Don't** 不要使用 0px 圆角或硬边框。
- **Don't** 不要让光球遮挡内容（z-index 始终在内容下方）。

## 实现注意事项

- **必须**确保 `.slide` 有 `transform: translate(-50%, -50%)`，否则内容会跑到右下角。
- 字体栈：`'Sora', 'Noto Sans SC', sans-serif`。
- 渐变背景 + 毛玻璃卡片（`backdrop-filter: blur()`），不要用实色卡片。
- 装饰性浮动形状必须 `pointer-events: none`。
- 整体色调是粉紫蓝梦幻渐变，不要引入暖色。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景必须是白到淡蓝紫的 135deg 渐变。所有卡片使用 `rgba(255,255,255,0.45)` + `backdrop-filter: blur(20px)` 磨砂玻璃效果，24px 圆角，1px 白色半透明描边。背景层放 2-3 个 blur(40px) 的彩色光球（薰衣草紫/天蓝/粉紫）。字体用 Sora。深靛蓝 `#1E2A5E` 用于文字和实心卡片。禁止不透明卡片和硬边。
