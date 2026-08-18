---
name: Mineral Strata
version: 1.0.0
category: painterly-abstract
tags: [chinese, blue-green-landscape, mineral-colors, gold-line, geometric, strata]

color:
  background: "#F5F0E6"
  foreground: "#1A2A3A"
  azurite: "#2E5A88"
  malachite: "#4A8B6F"
  gold: "#C4A35A"
  gold_light: "rgba(196,163,90,0.3)"
  muted: "#6B6352"

typography:
  heading:
    family: "Noto Serif SC, serif"
    weight: 900
    letter_spacing: "0.05-0.08em"
  body:
    family: "Noto Serif SC, serif"
    weight: 400
  en:
    family: "Cormorant Garamond, Georgia, serif"
    weight: 600
    letter_spacing: "0.2-0.35em"
  scale:
    display: "120px"
    h1: "80px"
    h2: "40px"
    body: "15px"
    caption: "12px"

spacing:
  slide_padding: "56px 80px"
  gap_large: "32px"
  gap_medium: "24px"

radius:
  base: "0px"

shadow:
  none: true

border:
  width: "1-2px"
  style: "solid"
  color: "#C4A35A"
---

# Mineral Strata（青绿·矿物层叠）— Design Specification

## 气质

青绿山水的抽象转译。不画山，而以石青、石绿的水平色带模拟远山的层叠结构，以泥金细线勾勒分界，以极简几何三角形指代山峰。矿物色的沉稳华贵 + 现代主义的几何克制，像展开一幅手卷，但画面中没有一笔是在"画山水"。

## 色彩规则

- **背景**：暖绢白 `#F5F0E6`，不是纯白，带绢本质感。
- **石青** `#2E5A88`：上方色带、主标题、关键文字——最远最高的颜色。
- **石绿** `#4A8B6F`：下方色带，托住全局——最近最沉的颜色。
- **泥金** `#C4A35A`：只做线，不做面——分隔线、山形轮廓、装饰圆环。
- **禁止**：渐变色、高饱和色、冷灰、大面积金色块。

## 字体规则

- 中文标题用 **Noto Serif SC 900**，字距 0.05-0.08em，字号极大（封面 120px）。
- 英文用 **Cormorant Garamond**，大写 + 0.2-0.35em 字距，金色。
- 正文用 Noto Serif SC 400，行高 1.8。
- 标签用小号宋体，石青色。

## 版式规则

- **水平色带系统**：页面被石青（上）、绢白（中，内容区）、石绿（下）三条水平带分割，泥金细线分隔。
- 色带高度可变化：封面/结尾用宽带（80-100px），内容页用窄带（50px）。
- **几何山形**：底部放置 2-3 个极简三角形（SVG polygon），石青/石绿填充 + 泥金 1.5px 描边，只有轮廓没有皴法。
- **同心圆装饰**：泥金细线绘制的 2-3 层同心圆，作为"日/月"的抽象符号，低透明度。
- 内容区居中或左对齐，大量留白（云雾即留白）。
- 页脚放在石绿色带内，白色/半透明白色文字。

## 组件模式

- **色带**：绝对定位的 `position: absolute; left:0; right:0;` 矩形，石青或石绿填充，高度 50-100px。
- **金线**：`height: 1px; background: #C4A35A;`，位于色带边缘。
- **山形**：SVG `<polygon>`，如 `points="680,200 820,40 960,200"`，石青填充 + 泥金描边。
- **同心圆**：SVG `<circle>` 多层，`fill: none; stroke: #C4A35A`，1-2px 线宽。
- **卡片**：半透明白底 `rgba(255,255,255,0.4)` + 2px 泥金 `border-top`，无圆角。
- **双栏**：一栏石青底白字，一栏半透明白底深字。

## Do / Don't

- **Do** 用水平色带组织版面，像手卷一样横向阅读。
- **Do** 山形只用几何三角形 + 金线轮廓，不画皴法。
- **Do** 金色只做细线，不做填充面。
- **Don't** 不要画真实的山水、云雾、树木、水波。
- **Don't** 不要使用圆角、渐变、阴影。
- **Don't** 不要让石青和石绿直接相邻——中间必须有绢白留白。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景为暖绢白 #F5F0E6。页面由石青 #2E5A88（上）和石绿 #4A8B6F（下）水平色带分割，泥金 #C4A35A 1px 细线分隔。底部放 2-3 个极简 SVG 三角形山形（石青/石绿填充+泥金描边）。中文标题 Noto Serif SC 900 大字距，英文 Cormorant Garamond 大写金色。卡片半透明白底+泥金顶部边框，零圆角。禁止画真实山水、渐变、圆角、阴影。
