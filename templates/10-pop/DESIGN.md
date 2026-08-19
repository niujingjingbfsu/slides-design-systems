---
name: Pop!
version: 1.0.0
category: bold-colorful
tags: [pop-art, comic, halftone, yellow, primary-colors, fun]

color:
  background: "#FFE500"
  foreground: "#000000"
  red: "#E63946"
  blue: "#1D4E89"
  white: "#FFFFFF"

typography:
  heading:
    family: "Anton, sans-serif"
    weight: 400
    letter_spacing: "0.02em"
    text_transform: "uppercase"
  body:
    family: "Inter, -apple-system, sans-serif"
    weight: 700
  scale:
    display: "150px"
    h1: "100px"
    h2: "30px"
    body: "14px"
    caption: "12px"

spacing:
  slide_padding: "56px 72px"
  gap_large: "28px"
  gap_medium: "24px"

radius:
  base: "0px"
  bubble: "24px"

shadow:
  bubble: "8px 8px 0 #E63946"
  button: "6px 6px 0 #000"

border:
  width: "4px"
  style: "solid"
  color: "#000000"
---

# Pop! — Design Specification

## 气质

波普艺术/漫画风。亮黄色底，红色半调网点（Ben-Day dots），粗黑描边，爆炸星形气泡。像 Lichtenstein 的画——热闹、夸张、快乐，视觉冲击力极强。

## 色彩规则

- **背景**：亮黄 `#FFE500`，这是主色调，不是强调色。
- **前景**：纯黑 `#000000`。
- **红** `#E63946`：半调网点、爆炸星、卡片底色、强调文字。
- **蓝** `#1D4E89`：几何形状、卡片底色。
- **白**：卡片底、描边文字填充。
- **禁止**：渐变色、柔和色、灰色、低饱和色。

## 字体规则

- 标题用 **Anton**，压缩粗体无衬线，全大写，字号极大（封面 150px）。
- 空心字效果：白色填充 + 3-4px 黑色 `-webkit-text-stroke`。
- 正文用 **Inter**，字重 700-900。
- 标签用大写 + 0.05-0.1em 字距。

## 版式规则

- 四角加**红色半调网点**（Ben-Day dots）：`radial-gradient(circle, red 2px, transparent 2.5px)`，16px 间距，用 mask 渐变淡出。
- 所有形状带 **4px 黑描边**。
- 封面：大标题 + 右侧圆形/矩形/爆炸星组合。
- 金句页：白色对话气泡（24px 圆角 + 4px 黑描边 + 红色硬投影），带小尖角，微旋转 -1.5 度。
- 爆炸星（starburst）：用 `clip-path` 多边形做 10 角星，红底白字。
- 内容页三栏卡片，底色分别为白/蓝/红。
- 数据页四栏，白/蓝/黄/黑四色轮换。

## 组件模式

- **半调网点**：`background: radial-gradient(circle, #E63946 2px, transparent 2.5px); background-size: 16px 16px;`，配合 `-webkit-mask-image: linear-gradient()` 做边角淡出。
- **对话气泡**：白底 + 4px 黑描边 + 24px 圆角 + `::after`/`::before` 做尖角，8px 红色硬投影。
- **爆炸星**：`clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)`，红底白字。
- **描边字**：`-webkit-text-stroke: 3-4px #000; color: #fff; paint-order: stroke fill;`。
- **按钮**：蓝底白字 + 4px 黑描边 + 6px 硬投影。

## Do / Don't

- **Do** 大面积使用亮黄色底。
- **Do** 四角加红色半调网点。
- **Do** 用爆炸星和对话气泡增加漫画感。
- **Don't** 不要使用渐变或柔和阴影。
- **Don't** 不要使用细字体。
- **Don't** 不要让黄色只做小面积点缀——它是主角。

## 实现注意事项

- 字体栈：`'Anton', 'Inter', 'Noto Sans SC', sans-serif`。Anton 用于英文大标题，中文回退 Noto Sans SC 900。
- **CSS 声明之间不能漏分号**，特别是 `var()` 后。
- 高饱和黄/红/蓝/白四色，粗黑边框，波普圆点装饰。
- 圆点图案用 CSS `radial-gradient` 实现。
- 卡片颜色交替使用，不要全部同色。
- 页脚深色文字在黄色背景上。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景固定为亮黄色 #FFE500。所有形状带 4px 纯黑描边。标题用 Anton 全大写，可用白色填充+黑色 stroke 做空心字。四角加红色 Ben-Day 半调网点（radial-gradient 圆点 + mask 淡出）。金句用白色对话气泡（圆角+黑描边+红色硬投影+尖角）。强调色为红 #E63946 和蓝 #1D4E89。爆炸星用 clip-path 多边形。禁止渐变和柔和色。
