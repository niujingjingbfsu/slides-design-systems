---
name: Noir
version: 1.0.0
category: high-end-whitespace
tags: [luxury, black, gold, serif, dark-mode, ceremonial]

color:
  background: "#0A0A0A"
  foreground: "#FFFFFF"
  muted: "#666666"
  gold: "#C9A96E"
  gold_dim: "rgba(201, 169, 110, 0.3)"
  line: "rgba(255, 255, 255, 0.08)"

typography:
  heading:
    family: "Cormorant Garamond, Times New Roman, serif"
    weight: 300
    letter_spacing: "0.02-0.08em"
  italic:
    family: "Cormorant Garamond, Times New Roman, serif"
    weight: 300
    style: italic
    color: "#C9A96E"
  body:
    family: "Inter, -apple-system, sans-serif"
    weight: 300
  label:
    family: "Inter, -apple-system, sans-serif"
    weight: 400
    letter_spacing: "0.25-0.4em"
    text_transform: "uppercase"
  scale:
    display: "140px"
    h1: "96px"
    h2: "48px"
    h3: "32px"
    body: "13px"
    caption: "10px"

spacing:
  baseline: "8px"
  slide_padding: "72px 100px"
  gap_large: "64px"
  gap_medium: "48px"
  gap_small: "20px"

radius:
  base: "0px"

shadow:
  none: true

border:
  hairline: "1px solid rgba(255, 255, 255, 0.08)"
  gold_dim: "1px solid rgba(201, 169, 110, 0.3)"
  corner_mark: "32px L-shape, rgba(201, 169, 110, 0.3)"
---

# Noir — Design Specification

## 气质

暗夜奢雅。纯黑是舞台，白色衬线是追光，香槟金是低语。四角的 L 形角线像画框，把每一页装裱成仪式感极强的画面。居中对称、元素极少、字距宽松——像高级定制品牌的邀请函。

## 色彩规则

- **背景**：纯黑 `#0A0A0A`，不是深灰，是接近绝对的黑。
- **前景**：纯白 `#FFFFFF`。正文用 `rgba(255,255,255,0.7)`，辅助文字用 `#666666`。
- **金色**：香槟金 `#C9A96E`，**仅用于**：斜体强调词、短横线、角线、小标记、章节编号。绝不用作大面积填充或文字底色。
- **金色半透明**：`rgba(201,169,110,0.3)` 用于角线和边框。
- **禁止**：渐变、阴影、第二种彩色、圆角、发光效果（glow）。

## 字体规则

- 标题用 **Cormorant Garamond Light 300**，字距宽松（0.02-0.08em），营造仪式感。
- **金色斜体 300** 用于标题中的关键词，是唯一的色彩强调方式。
- 正文用 **Inter Light 300**，字号 13px，行高 1.8。
- 标签用 Inter 400，大写，字距 0.25-0.4em，金色或灰色。
- 数字用衬线体 300，单位用金色斜体。

## 版式规则

- **四角角线**：每页四角都有 32px 的 L 形金色半透明描边，是这套模板的标志元素。
- 封面：居中对称，顶部左右两侧小号标签，中央"Edition"标签 + 大标题（140px）+ 金色渐变横线 + 副标题。
- 章节页：居中，金色斜体章节号 + 大标题 + 金色短横线 + 描述。
- 内容页：三栏等宽网格，1px 半透明白线分隔，每栏居中：罗马数字 + 金色短线 + 标题 + 说明。
- 双栏页：两张居中卡片，1px 描边（其中一张用金色半透明描边），内含标签 + 标题 + 说明 + 底部规格。
- 金句页：居中，金色大引号 + 白色衬线金句（金色斜体强调）+ 金色横线 + 出处。
- 数据页：三栏居中，竖线分隔，衬线大数字 + 金色斜体单位。
- 结尾页：居中，金色 monogram + 大标题 + 金色横线 + 结束语。

## 组件模式

- **角线**：32px L 形，`rgba(201,169,110,0.3)`，1px，四角各一，距边缘 40px。
- **金色横线**：60px 宽，1px 高，`linear-gradient(90deg, transparent, #C9A96E, transparent)`，居中。
- **卡片**：无圆角，1px 描边（白色半透明或金色半透明），padding 48px，居中文字。
- **金色圆点**：5px 正圆，页脚标题前。
- **罗马数字**：衬线 40px，金色，用于内容页编号。

## Do / Don't

- **Do** 每页都加四角 L 形角线。
- **Do** 用金色斜体做唯一的色彩强调。
- **Do** 居中对称排版，字距宽松。
- **Do** 金色横线用渐变透明收尾。
- **Don't** 不要使用金色填充大面积区域。
- **Don't** 不要使用发光、阴影或渐变背景。
- **Don't** 不要使用粗体或圆角。
- **Don't** 不要左对齐内容页的核心元素（以居中为主）。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景纯黑 `#0A0A0A`，文字白色，唯一强调色是香槟金 `#C9A96E`（只用于斜体词、细线和角线）。每页四角必须有 32px L 形 `rgba(201,169,110,0.3)` 描边。标题用 Cormorant Garamond 300，强调用金色 italic 300。标签用 Inter 大写+0.3em字距。无圆角无阴影无渐变。内容以居中对称为主。金色横线用透明渐变收尾。
