---
name: ESSENTIAL
version: 1.0.0
category: high-end-whitespace
tags: [gallery, serif, extreme-whitespace, luxury, minimal, editorial]

color:
  background: "#FFFFFF"
  foreground: "#0A0A0A"
  muted: "#999999"
  faint: "#CCCCCC"
  accent: "#1A3A5C"

typography:
  heading:
    family: "Cormorant Garamond, Times New Roman, serif"
    weight: 300
    letter_spacing: "-0.01em"
  display:
    family: "Cormorant Garamond, Times New Roman, serif"
    weight: 300
    letter_spacing: "-0.015em"
  italic:
    family: "Cormorant Garamond, Times New Roman, serif"
    weight: 300
    style: italic
  body:
    family: "Inter, -apple-system, sans-serif"
    weight: 300
  label:
    family: "Inter, -apple-system, sans-serif"
    weight: 400
    letter_spacing: "0.2em"
    text_transform: "uppercase"
  scale:
    display: "168px"
    h1: "120px"
    h2: "48px"
    h3: "32px"
    body: "14px"
    caption: "10px"

spacing:
  baseline: "8px"
  slide_padding: "80px 100px"
  gap_large: "80px"
  gap_medium: "48px"
  gap_small: "20px"
  whitespace_target: "70%"

radius:
  base: "0px"

shadow:
  none: true

border:
  hairline: "1px solid #CCCCCC"
  accent_width: "1px"

progress_bar:
  height: "56px"
  background: "transparent"
  border_top: "var(--faint)"
  section_label:
    font: "var(--font-sans)"
    size: "12px"
    weight: "700"
    color: "var(--muted)"
    letter_spacing: "0.25em"
  page_number:
    font: "var(--font-sans)"
    size: "16px"
    weight: "700"
    color: "var(--accent)"
    letter_spacing: "0.1em"
  segments:
    shape: "line"
    size: "2px"
    gap: "5px"
    section_gap: "24px"
    future: "faint fill; w=40px, h=2px"
    past: "medium fill"
    current: "var(--accent) fill; h=3px"

---

# ESSENTIAL — Design Specification

## 气质

画廊级极简。纯白空间中，极细衬线体是绝对主角，一个深蓝色小方块是唯一的色彩。每一页都像美术馆的白墙——70% 以上的面积留空，让存在的元素获得全部重量。设计的自信来自删去一切可有可无之物。

## 色彩规则

- **背景**：纯白 `#FFFFFF`。
- **前景**：近黑 `#0A0A0A`。辅助文字用 `#999999`，分隔线用 `#CCCCCC`。
- **唯一强调色**：深蓝 `#1A3A5C`，**仅用于**：7-10px 小方块、数字单位、个别强调词。面积不超过画面 1%。
- **禁止**：渐变、阴影、第二种强调色、色块填充、圆角。

## 字体规则

- 标题和数字用 **Cormorant Garamond Light 300**，这是整套设计的灵魂。
- **斜体（italic 300）**用于标题中的强调词，是唯一允许的"装饰"。
- 正文和标签用 **Inter Light 300**，标签大写 + 0.2em 字距 + 10px。
- 标题字距 -0.01em 至 -0.015em，极紧但不碰撞。
- Display 字号极大（120-168px），用字号而非粗细建立层级。

## 版式规则

- 每页留白不少于 **70%**。
- 封面：大标题左对齐（168px），顶部左右两侧放小号元信息，右侧可加一条 1px 深蓝竖线。
- 章节页：左对齐大标题（120px），上方小号深蓝章节编号，下方 80px 黑色短横线。
- 内容页：顶部标题 + 右侧页码标签，下方 1px 横线分隔；正文用 1fr 1.2fr 双栏，左栏衬线引导文（26px light），右栏编号列表。
- 双栏页：两栏之间 80px gap，无分隔线，每栏顶部有编号和标题。
- 金句页：大号引号（`#CCCCCC`，120px）+ 衬线金句（56px light），深蓝强调词。
- 数据页：三栏等宽，竖线分隔，数字用衬线 96px light，深蓝斜体单位。

## 组件模式

- **小方块**：7-10px 深蓝实心方块，出现在页脚标题前、结尾页中央、数据单位旁。
- **横线**：1px `#CCCCCC`，用于标题下方分隔，长度克制（40-80px）。
- **编号**：衬线体 18px，深蓝色，用于列表项前缀。
- **页脚**：10px 大写 Inter，`#999999`，左侧深蓝方块 + 模板名，右侧页码。
- **无卡片**：不使用任何卡片、容器或背景块。内容直接放在白底上。

## Do / Don't

- **Do** 让衬线细体承载所有视觉重量。
- **Do** 用斜体替代加粗来强调。
- **Do** 留白至少 70%。
- **Do** 深蓝小方块只用在需要眼睛停住的地方。
- **Don't** 不要使用粗体（bold）。
- **Don't** 不要使用圆角、阴影、渐变。
- **Don't** 不要使用卡片或色块容器。
- **Don't** 不要让深蓝色面积超过画面 1%。

## 实现注意事项

- 字体栈：`'Cormorant Garamond', 'Noto Serif SC', Georgia, serif`。
- **列表序号列宽必须 ≥ 90px**（如 `grid-template-columns: 90px 1fr`），否则 "LEVEL 1" 会断行成 "LEV EL 1"。序号加 `white-space: nowrap`。
- 极致留白是核心设计，内容只占左侧约 60% 宽度，右侧留白是故意的。
- 细线分隔（1px #E5E5E5），不要用粗线或色块。
- 页脚极简，小号大写字母，深色文字。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景纯白，文字近黑，唯一强调色是深蓝 `#1A3A5C` 且只用于 7-10px 小方块和个别文字。所有标题用 Cormorant Garamond 300（极细），强调用 italic 300，绝对不要用 bold。正文和标签用 Inter 300，标签大写+0.2em字距。无圆角无阴影无卡片。每页留白 70% 以上。分隔线只用 1px #CCCCCC。
