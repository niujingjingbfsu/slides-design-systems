---
name: Cobalt Circles
version: 1.0.0
category: painterly-abstract
tags: [chinese, blue-white-porcelain, cobalt, concentric-circles, monochrome, minimal]

color:
  background: "#FFFFFF"
  foreground: "#1A2A3A"
  cobalt: "#1B4B8A"
  cobalt_2: "#4A7FB5"
  cobalt_3: "#8AB0D5"
  cobalt_4: "#C5D9EC"
  cobalt_5: "#E8F0F8"
  muted: "#6B7D8F"

typography:
  heading:
    family: "Noto Serif SC, serif"
    weight: 900
    letter_spacing: "0.05-0.08em"
  body:
    family: "Noto Serif SC, serif"
    weight: 400
  en:
    family: "Josefin Sans, sans-serif"
    weight: 600
    letter_spacing: "0.25-0.4em"
  scale:
    display: "120px"
    h1: "80px"
    h2: "40px"
    body: "15px"
    caption: "11px"

spacing:
  slide_padding: "56px 80px"
  gap_large: "28px"
  gap_medium: "24px"

radius:
  base: "0px"
  circle: "50%"

shadow:
  none: true

border:
  width: "1px"
  style: "solid"
  color: "#8AB0D5"
---

# Cobalt Circles（青花·钴蓝同心圆）— Design Specification

## 气质

青花瓷的抽象转译。不画瓷瓶、不画缠枝莲，而抽取两个核心语法：**同心圆构图**（瓷盘的圆形格式）和**分水色阶**（钴蓝浓淡渐变）。纯白底上，钴蓝圆环从中心向外扩散、由浓渐淡，像瓷釉上最淡的一笔分水。底部有青花海水纹边饰。单色体系靠明度变化建立层次——瑞士国际主义的骨，中国瓷器的魂。

## 色彩规则

- **背景**：纯白 `#FFFFFF`，像瓷釉。
- **钴蓝** `#1B4B8A`：最深的"头浓"，主标题、实心圆、关键数据。
- **钴蓝 2-4** `#4A7FB5` / `#8AB0D5` / `#C5D9EC`：由浓到淡的分水色阶，用于同心圆外环、辅助线、边框。
- **钴蓝 5** `#E8F0F8`：最淡的底色，可用于浅填充。
- **禁止**：第二色相（红、黄、绿等）、渐变背景、灰色。
- 整套系统只有钴蓝一个色相，层次完全靠明度（5 个色阶）。

## 字体规则

- 中文标题用 **Noto Serif SC 900**，字距 0.05-0.08em，钴蓝色。
- 英文用 **Josefin Sans 600**，大写 + 0.25-0.4em 字距，钴蓝 2（中蓝）。
- 正文用 Noto Serif SC 400，行高 1.8。
- 标签用小号大写英文，钴蓝 2。

## 版式规则

- **同心圆系统**：每页有 3-6 个同心圆（SVG `<circle>`），从画面中心或偏心位置向外扩散，线宽递减、颜色由浓到淡。圆环可被画面边缘裁切。
- 最内一环可用钴蓝低透明度填充（`opacity: 0.06`），像瓷盘中心。
- **海水纹边带**：底部 32px 高钴蓝色带，上面有白色叠浪弧线（3 层 Q 贝塞尔弧线，透明度递减），顶部有白色半透明 1.5px 边线模拟瓷釉口沿。
- 顶部 4px 钴蓝细线。
- 卡片：白底 + 1px 钴蓝 3 边框 + `::before` 内嵌 0.5px 钴蓝 4 框（双层框，像瓷器的弦纹）。
- 卡片图标用同心圆：外环 2px 钴蓝 + 中环 1px 钴蓝 2 + 中心实心钴蓝圆。
- 双栏：一栏钴蓝底白字，一栏白底钴蓝字。
- 大量留白——瓷白即虚空。

## 组件模式

- **同心圆**：SVG `<circle cx cy r fill="none" stroke="#1B4B8A" stroke-width="2"/>`，外层用更淡的蓝和更细的线，如 r=340 stroke=#1B4B8A width=2 → r=290 stroke=#4A7FB5 width=1.5 → r=240 stroke=#8AB0D5 width=1 → r=190 stroke=#C5D9EC width=1。
- **海水纹边带**：CSS `background-image: url("data:image/svg+xml,...")` 重复 SVG，3 层白色波浪弧线（opacity 0.85/0.4/0.2），钴蓝底 + 白色顶部边线。
- **双层框卡片**：1px `#8AB0D5` 外框 + `::before` 0.5px `#C5D9EC` 内框（offset 8px）。
- **环形图标**：48px 圆，2px 钴蓝外环 + 1px 钴蓝 2 中环 + 8px 实心钴蓝圆心。
- **实心圆点**：10px 钴蓝圆形，用于角落装饰。

## Do / Don't

- **Do** 只用钴蓝一个色相，靠 5 个明度色阶建立层次。
- **Do** 每页有同心圆元素，由浓到淡向外扩散。
- **Do** 底部海水纹用白色叠浪弧线，不是几何回纹。
- **Don't** 不要画瓷器、莲花、缠枝、龙纹等具象纹样。
- **Don't** 不要引入第二色相（红色印章也不行——保持单色纯粹）。
- **Don't** 不要使用圆角（圆形除外）、渐变背景、阴影。

## 实现注意事项

- 字体栈：`'Noto Serif SC', 'Cormorant Garamond', Georgia, serif`。
- 页脚在 `bottom: 32px; height: 32px`，nav-hint 在 `bottom: 4px`（在底部青花波浪装饰边框内，故意低对比度）。
- 钴蓝色 `#1B4B8A`，白底，青花波浪纹在底部。
- 同心圆装饰用 SVG circle，钴蓝细线。
- 卡片有 1px 钴蓝边框，无填充或极浅蓝填充。
- 不要引入其他颜色。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景纯白。只用钴蓝 #1B4B8A 一个色相，配合 #4A7FB5/#8AB0D5/#C5D9EC/#E8F0F8 四个淡色阶。每页有 SVG 同心圆，由内向外颜色渐淡、线宽递减。底部 32px 钴蓝色带配白色三层叠浪弧线（海水纹，data URI SVG），顶部 4px 钴蓝线。中文标题 Noto Serif SC 900，英文 Josefin Sans 大写。卡片白底+双层钴蓝边框，零圆角。禁止第二色相、具象纹样、渐变背景。
