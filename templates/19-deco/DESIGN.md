---
name: Deco
version: 1.0.0
category: painterly
tags: [art-deco, gold, geometric, symmetry, dark, luxury, sunburst]

color:
  background: "#0B0F1A"
  foreground: "#E8D5A3"
  gold: "#C9A961"
  gold_bright: "#E8D5A3"
  gold_dim: "rgba(201,169,97,0.3)"
  navy: "#141B2E"
  muted: "#8A8070"

typography:
  heading:
    family: "Limelight, Georgia, serif"
    weight: 400
    letter_spacing: "0.08-0.15em"
  body:
    family: "Josefin Sans, sans-serif"
    weight: 300-400
  en:
    family: "Josefin Sans, sans-serif"
    weight: 600
    letter_spacing: "0.3em"
  scale:
    display: "110px"
    h1: "72px"
    h2: "36px"
    body: "15px"
    caption: "11px"

spacing:
  slide_padding: "64px 80px"
  gap_large: "32px"
  gap_medium: "24px"

radius:
  base: "0px"

shadow:
  none: true

border:
  width: "1-2px"
  style: "solid"
  color: "#C9A961"
---

# Deco（装饰艺术）— Design Specification

## 气质

Art Deco 的几何奢华。深夜蓝底 + 金色线条，绝对对称构图。旭日放射线（sunburst）从底部或中心发散，Chevron 角饰、阶梯金字塔、扇形装饰——1920 年代的摩天楼与爵士时代。Limelight 字体本身就是 Deco 宣言。华丽但冷峻，对称到强迫症。

## 色彩规则

- **背景**：深夜蓝 `#0B0F1A`，近黑但有蓝调。
- **金色** `#C9A961`：所有线条、边框、装饰、标题——系统的绝对主角。
- **亮金** `#E8D5A3`：标题文字、高亮、放射线。
- **暗金** `rgba(201,169,97,0.3)`：辅助线、背景装饰。
- **禁止**：任何彩色（红、蓝、绿等色相）、白色背景、无金色的页面。
- 整套系统只有深蓝底 + 金色，层次靠金色透明度。

## 字体规则

- 英文标题用 **Limelight**（Art Deco 标志性字体），字距 0.08-0.15em，亮金色。
- 正文/标签用 **Josefin Sans 300-400**，几何无衬线，大写 + 0.3em 字距。
- 中文用 **Noto Serif SC 900**（如需要）。
- 章节号用 Josefin Sans 大写，暗金色。

## 版式规则

- **绝对对称**：所有元素沿垂直中轴线对称，或左右镜像。
- **旭日放射线**：封面/章节页从底部中心或画面中心发散 20-40 条金色射线（JS 动态生成或 SVG），透明度从中心向外递减。
- **Chevron 角饰**：四角放置 V 形/人字形金色装饰（多层嵌套）。
- **阶梯金字塔**：底部或顶部放置 3-5 层递减的金色阶梯矩形。
- **双层框**：外层 2px 金色 + 内层 0.5px 金色（inset 10px）。
- 卡片：深蓝底 `#141B2E` + 1px 金色边框，无圆角。
- 数据四栏：金色竖线分隔，数字用 Limelight 大字。
- 金句页：居中对称，上下金色扇形装饰。

## 组件模式

- **旭日放射**：JS 循环生成 `<div>` 射线，`transform: rotate()` 从中心点发散，金色 1px，opacity 渐变。
- **Chevron**：SVG `<polyline points="0,20 20,0 40,20" stroke="#C9A961" fill="none"/>`，多层嵌套。
- **阶梯**：3-5 个 `<div>` 宽度递减（如 200px/160px/120px/80px），金色 1px 边框或填充，居中堆叠。
- **双层框**：`border: 2px solid #C9A961` + `::before` inset 10px 的 0.5px 金色框。
- **扇形装饰**：SVG `<path>` 绘制同心圆弧线，金色，位于标题上下。
- **卡片**：`background: #141B2E; border: 1px solid rgba(201,169,97,0.4);`。

## Do / Don't

- **Do** 每页必须绝对对称。
- **Do** 金色是唯一装饰色，靠透明度和线宽变化层次。
- **Do** 放射线、Chevron、阶梯是三大装饰母题。
- **Don't** 不要使用有机曲线（那是 Art Nouveau）。
- **Don't** 不要使用圆角、阴影、彩色。
- **Don't** 不要打破对称——除非是内容页的双栏，双栏也必须镜像对称。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景深夜蓝 #0B0F1A。所有装饰和文字用金色 #C9A961/#E8D5A3，靠透明度分层。每页绝对对称。封面有 JS 生成的旭日放射线（从中心发散 20-40 条金色射线），四角 Chevron 角饰，底部阶梯金字塔。标题 Limelight 字体亮金色，正文 Josefin Sans 大写。卡片深蓝底+金色边框。禁止有机曲线、圆角、彩色、阴影。
