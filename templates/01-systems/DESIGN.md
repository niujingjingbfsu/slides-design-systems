---
name: Systems
version: 1.0.0
category: calm-restrained
tags: [technical, blueprint, monospace, grid, documentation]

color:
  background: "#F6F5F2"
  foreground: "#1A1A1A"
  muted: "#8A8580"
  accent: "#B85C38"
  accent_soft: "rgba(184, 92, 56, 0.10)"
  line: "rgba(26, 26, 26, 0.12)"
  grid: "rgba(26, 26, 26, 0.035)"

typography:
  heading:
    family: "JetBrains Mono, ui-monospace, SF Mono, Menlo, monospace"
    weight: 700
    letter_spacing: "-0.02em"
  body:
    family: "Inter, -apple-system, sans-serif"
    weight: 300
  mono:
    family: "JetBrains Mono, ui-monospace, monospace"
  scale:
    display: "96px"
    h1: "44px"
    h2: "22px"
    body: "15px"
    caption: "11px"

spacing:
  baseline: "32px"
  slide_padding: "64px 80px"
  gap_large: "48px"
  gap_medium: "24px"
  gap_small: "12px"

radius:
  base: "0px"
  card: "0px"
  pill: "0px"

shadow:
  none: true

border:
  width: "1px"
  style: "solid"
  color: "rgba(26, 26, 26, 0.12)"
  hairline: true
---

# Systems — Design Specification

## 气质

蓝图式的技术文档美学。像工程师的方格笔记本：精确、冷静、毫不含糊。所有元素对齐到 32px 栅格，间距是 32 的倍数，不使用任何任意值。

## 色彩规则

- **背景**：暖灰 `#F6F5F2`，叠加 32px 栅格线（极淡，3.5% 透明度），提供结构感但不干扰阅读。
- **前景**：近黑 `#1A1A1A`，正文用 `#3A3733`，辅助文字用 `#8A8580`。
- **强调色**：赤陶色 `#B85C38`，**仅用于**：分隔线、列表方点、标签标记、数字。绝不用作大面积填充或按钮底色。
- **禁止**：渐变、阴影、彩色背景块。

## 字体规则

- 标题和标签使用 **JetBrains Mono** 等宽字体，字重 700，字距紧凑（-0.02em）。
- 正文使用 **Inter**，字重 300，行高 1.6-1.7。
- 等宽字体承载结构感，无衬线字体承载阅读舒适度，二者不混用。
- 标签使用大写 + 0.18em 字距，前面加一条 24px 赤陶色短线。

## 版式规则

- 所有元素**严格左对齐**，不使用居中对齐（结尾页的角标除外）。
- 内容页采用 1fr 1fr 双栏：左侧引导文，右侧要点列表。
- 双栏对比用 1px 线条分隔（不是 gap），形成表格感。
- 数据页用三栏等宽网格，竖线分隔，数字用等宽大字。

## 组件模式

- **列表项**：赤陶色 8px 方块 + 等宽小标题 + 无衬线说明文字。
- **卡片**：无圆角、无阴影、1px 描边，像表格单元格。
- **章节页**：右下角放大号半透明数字（200px，10% 透明度赤陶色）。
- **结尾页**：四角加 L 形 1px 描边，形成工程图纸的角标感。

## Do / Don't

- **Do** 用 1px 线条分隔区域，不用阴影。
- **Do** 让所有间距落在 32px 栅格上。
- **Do** 用等宽字体的大写标签建立技术感。
- **Don't** 不要给任何元素加圆角。
- **Don't** 不要让赤陶色占据超过画面 5% 的面积。
- **Don't** 不要使用居中排版（结尾页除外）。

## 实现注意事项

- 字体栈：`'JetBrains Mono', 'Inter', 'Noto Sans SC', monospace`，Mono 用于英文标签和数据，Inter 用于正文，Noto Sans SC 用于中文。
- 网格背景用 CSS `background-image: linear-gradient(...)` 实现，不要用图片。
- 橙色强调色 `#D4541E` 只用于关键数字、分隔线和 hover 状态，不要大面积使用。
- 数据页是 3 列指标，不要放第 4 个指标。
- 页脚是深色文字在浅色背景上，不需要 bottom-band。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。所有颜色、字体、间距必须使用上述 token，禁止自行发明颜色或圆角。背景必须叠加 32px 栅格线。强调色 `#B85C38` 仅用于线条、方点和小标记。所有卡片和容器使用 1px 实线描边，无阴影无圆角。正文用 Inter 300，标题和标签用 JetBrains Mono 700。
