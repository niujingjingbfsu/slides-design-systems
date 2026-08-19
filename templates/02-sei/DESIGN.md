---
name: 静 (Sei)
version: 1.0.0
category: calm-restrained
tags: [zen, japanese, minimal, serif, chinese, editorial]

color:
  background: "#F5F2EB"
  foreground: "#1A1A1A"
  muted: "#8C867B"
  accent: "#B33A2A"
  line: "rgba(26, 26, 26, 0.15)"

typography:
  heading:
    family: "Noto Serif SC, Songti SC, SimSun, serif"
    weight: 500
    letter_spacing: "0.04em"
  display:
    family: "Noto Serif SC, Songti SC, serif"
    weight: 900
    letter_spacing: "0.1em"
  body:
    family: "Noto Sans SC, -apple-system, sans-serif"
    weight: 300
  scale:
    display: "160px"
    h1: "88px"
    h2: "42px"
    body: "14px"
    caption: "11px"

spacing:
  baseline: "8px"
  slide_padding: "72px 96px"
  gap_large: "64px"
  gap_medium: "32px"
  gap_small: "16px"

radius:
  base: "0px"
  seal: "2-3px"

shadow:
  none: true

border:
  width: "1px"
  style: "solid"
  color: "rgba(26, 26, 26, 0.15)"
  hairline: true

progress_bar:
  height: "56px"
  background: "transparent"
  border_top: "1px solid var(--line)"
  section_label:
    font: "var(--font-serif)"
    size: "12px"
    weight: "700"
    color: "var(--muted)"
    letter_spacing: "0.3em"
  page_number:
    font: "var(--font-sans)"
    size: "13px"
    weight: "700"
    color: "var(--muted)"
    letter_spacing: "0.15em"
  segments:
    shape: "circle"
    size: "10px"
    gap: "5px"
    section_gap: "30px"
    future: "faint fill; w=10px, h=10px"
    past: "medium fill"
    current: "var(--accent) fill; w=14px, h=14px"

---

# 静 (Sei) — Design Specification

## 气质

日式禅意极简。米白宣纸为底，墨黑大字为骨，朱红印章为魂。画面追求"间"（ま）——留白不是空无，而是呼吸。整套模板只用三色，元素极少，每一处存在都经过慎重考量。

## 色彩规则

- **背景**：宣纸米白 `#F5F2EB`，纯净无纹理。
- **前景**：墨黑 `#1A1A1A`。正文用 `#4A453E`，辅助文字用 `#8C867B`。
- **强调色**：朱红 `#B33A2A`，**仅用于**印章和极小的标记。绝不用作线条、文字或大面积色块。
- **禁止**：渐变、阴影、第二种强调色、装饰性图形。

## 字体规则

- 标题用 **Noto Serif SC**（思源宋体），字重 500，字距 0.04em。
- 封面大字用字重 900，字号 160px，字距 0.1em，追求书法的庄重感。
- 正文用 **Noto Sans SC**（思源黑体），字重 300，行高 1.8-2.0。
- 中文排版使用全角标点，字距宽松，不挤不散。

## 版式规则

- 留白占画面约 **70%**，内容集中但不局促。
- 封面：印章 + 大字居中，两侧细线对称，右侧可加竖排英文标签。
- 章节页：大号衬线标题左对齐，右下角放一个 280px 的半透明大字（"間"等）作为气息。
- 内容页：左侧宋体引导文（20px，行高 2），右侧要点列表，朱红圆点标记。
- 数据页：三栏等宽，竖线分隔，数字用宋体细体（300 weight），单位用朱红。

## 组件模式

- **印章**：44px 朱红方块，圆角 2-3px，内有白色篆字风格汉字，是唯一的"装饰"。
- **分隔线**：1px 墨色细线，长度克制，不贯穿全屏。
- **列表**：朱红 6px 圆点 + 宋体小标题 + 黑体说明。
- **金句页**：居中大号宋体，朱红引号「」，引用来源用小号大写英文。

## Do / Don't

- **Do** 让留白占据画面大部分面积。
- **Do** 使用宋体大字建立东方书卷气。
- **Do** 用朱红印章作为唯一的视觉焦点。
- **Don't** 不要加任何阴影、渐变或纹理。
- **Don't** 不要让朱红色出现在印章以外的元素上。
- **Don't** 不要使用圆角卡片或现代 UI 组件。
- **Don't** 不要把画面填满，克制是第一原则。

## 实现注意事项

- 已有完整 CJK 字体栈（Noto Serif SC + Noto Sans SC），不需要额外添加。
-  en 字体是 Cormorant Garamond，中文用 Noto Serif SC，风格协调。
- 大量留白是设计核心，不要用卡片或色块填充空间。
- 装饰元素（圆、线、留白）用 SVG 实现，不要用 emoji 或图片。
- 页脚文字深色，无 bottom-band。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景固定为 `#F5F2EB`，文字为墨黑，唯一的强调色是朱红 `#B33A2A` 且只用于印章元素。标题用 Noto Serif SC，正文用 Noto Sans SC 300。所有分隔线为 1px 实线，无圆角无阴影。每页留白不少于 60%。印章是 44px 朱红方块带白色汉字。不要添加任何额外颜色或装饰元素。
