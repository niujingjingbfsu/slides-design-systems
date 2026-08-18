---
name: Punk
version: 1.0.0
category: bold-colorful
tags: [swiss-punk, black-white-red, experimental, rotated, broken-grid]

color:
  background: "#FFFFFF"
  foreground: "#000000"
  red: "#E63946"
  muted: "#666666"

typography:
  heading:
    family: "Inter, -apple-system, sans-serif"
    weight: 900
    letter_spacing: "-0.04em to -0.05em"
    text_transform: "uppercase"
  mono:
    family: "JetBrains Mono, monospace"
    weight: 700
  body:
    family: "Inter, -apple-system, sans-serif"
    weight: 500
  scale:
    display: "180px"
    h1: "110px"
    h2: "48px"
    body: "14px"
    caption: "12px"

spacing:
  slide_padding: "56px 72px"
  gap_large: "48px"
  gap_medium: "32px"

radius:
  base: "0px"

shadow:
  none: true

border:
  width: "3px"
  style: "solid"
  color: "#000000"
---

# Punk — Design Specification

## 气质

瑞士朋克/新浪潮平面设计。只用黑、白、红三色，但通过旋转、遮挡、重叠和破碎的网格制造紧张感。像 1977 年的朋克海报——激进、raw、充满对抗性。字体越粗越好，网格就是用来打破的。

## 色彩规则

- **背景**：纯白 `#FFFFFF`。
- **前景**：纯黑 `#000000`。
- **红色** `#E63946`：唯一强调色，用于色带、色块、数字、关键词。
- 红色以**几何块面**出现（竖条、横带、整格），不是小面积点缀。
- **禁止**：其他颜色、渐变、灰色装饰、圆角。

## 字体规则

- 标题用 **Inter Black 900**，全大写，字距极紧（-0.04em 至 -0.05em），字号极大（封面 180px）。
- 可用 `-webkit-text-stroke: 4px #000; color: transparent` 做空心大字。
- 标签和编号用 **JetBrains Mono 700**，大写 + 0.2-0.3em 字距。
- 正文用 Inter 500-900，不要用细体。
- 竖排文字：`writing-mode: vertical-rl`，用于红色色带上的标签。

## 版式规则

- **红色色带/色块切割画面**：顶部横条、侧边竖条、贯穿中部的横带，制造断裂感。
- **旋转元素**：红色色块旋转 ±15 度，部分遮挡标题，制造冲突。
- **竖排文字**：红色竖条上的白色文字用 `writing-mode: vertical-rl`。
- **破碎网格**：内容故意错位、不对齐，列表用 3px 黑线分隔而非卡片。
- 章节页：左侧红色竖条 + 大标题，右下角旋转 90 度的等宽文字。
- 金句页：红色横带贯穿画面中部，白色大字用 `mix-blend-mode: difference` 反色。
- 数据页：四栏用 3px 黑线分隔，其中一栏红底白字、一栏黑底白字。

## 组件模式

- **红色色带**：绝对定位的红色矩形，可贯穿全宽/全高，或旋转 15 度斜切画面。
- **竖排标签**：红色竖条 + `writing-mode: vertical-rl` 白色大写文字 + 0.3em 字距。
- **描边空心字**：`-webkit-text-stroke: 4px #000; color: transparent;`。
- **列表**：无卡片，用 3px 黑色横线分隔行，编号用等宽红色字体。
- **反色金句**：红色横带 + 白色文字 `mix-blend-mode: difference`。
- **数据格**：3px 黑线分隔的网格，隔栏换红/黑底。

## Do / Don't

- **Do** 用红色几何块面切割画面。
- **Do** 让元素旋转、遮挡、重叠，制造紧张感。
- **Do** 使用竖排文字和等宽编号。
- **Don't** 不要使用第四种颜色。
- **Don't** 不要使用圆角、渐变、阴影。
- **Don't** 不要让所有元素整齐对齐——错位是核心语言。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。只用黑白红三色（红 #E63946）。标题 Inter Black 900 全大写极紧字距，封面 180px。用红色色带/色块切割画面，元素可旋转 15 度、互相遮挡。竖排文字用 writing-mode: vertical-rl。列表用 3px 黑线分隔，不用卡片。金句用红色横带+mix-blend-mode:difference 反色。禁止圆角、渐变、阴影、第四色。网格要被打破。
