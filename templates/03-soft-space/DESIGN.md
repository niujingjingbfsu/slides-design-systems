---
name: Soft Space
version: 1.0.0
category: light-airy
tags: [warm, cream, rounded, soft-shadow, cards, friendly]

color:
  background: "#FAF6EF"
  foreground: "#3D3530"
  muted: "#9A8F86"
  accent: "#E8D5D0"
  accent_deep: "#D4A574"
  card: "#FFFFFF"
  accent_rose: "#E8D5D0"
  blob_opacity: "0.15-0.5"

typography:
  heading:
    family: "Plus Jakarta Sans, -apple-system, sans-serif"
    weight: 700
    letter_spacing: "-0.02em"
  display:
    family: "Plus Jakarta Sans, -apple-system, sans-serif"
    weight: 800
    letter_spacing: "-0.03em"
  body:
    family: "Plus Jakarta Sans, -apple-system, sans-serif"
    weight: 400
  scale:
    display: "88px"
    h1: "44px"
    h2: "24px"
    body: "14px"
    caption: "11px"

spacing:
  baseline: "8px"
  slide_padding: "64px 80px"
  gap_large: "48px"
  gap_medium: "24px"
  gap_small: "12px"

radius:
  base: "20px"
  card: "20px"
  pill: "100px"
  icon: "14px"

shadow:
  card: "0 8px 32px rgba(61, 53, 48, 0.06), 0 2px 8px rgba(61, 53, 48, 0.04)"
  card_lg: "0 20px 60px rgba(61, 53, 48, 0.08), 0 4px 16px rgba(61, 53, 48, 0.05)"
---

# Soft Space — Design Specification

## 气质

温暖、柔和、亲切。像午后阳光照进奶油色房间。所有边角都是圆润的，所有阴影都是弥散柔和的，色彩来自奶油、灰粉和浅赭石，不使用任何冷色或硬边。

## 色彩规则

- **背景**：暖奶油 `#FAF6EF`。
- **前景**：深棕灰 `#3D3530`，正文用 `#8A817A`。
- **主强调**：灰粉 `#E8D5D0`，用于圆形色块、标签底色、柔和装饰。
- **次强调**：浅赭石 `#D4A574`，用于小圆点、价格数字、重点标记。
- **卡片**：纯白 `#FFFFFF`，带柔和双层阴影。
- **装饰圆斑**：大号模糊圆形（灰粉/赭石），透明度 15%-50%，漂浮在背景层。
- **禁止**：冷色调（蓝、绿、紫）、硬边描边、高饱和色。

## 字体规则

- 全程使用 **Plus Jakarta Sans**，圆润几何无衬线。
- 标题字重 700-800，字距 -0.02em 至 -0.03em。
- 正文字重 400，行高 1.6-1.7。
- 可用细体（300）做副标题形成柔和对比。

## 版式规则

- 封面：大标题左对齐，灰粉圆斑从标题后方透出，右侧可放浮动玻璃小卡片。
- 内容页：三栏卡片网格，每卡有圆角图标块 + 标题 + 说明。
- 双栏页：两张大圆角卡片，其中一张可用深棕灰底（`#3D3530`）配奶油色文字做反转。
- 数据页：四栏白色圆角卡片，每卡一个彩色大数字。

## 组件模式

- **卡片**：20px 圆角，白色底，双层柔和阴影，padding 32-40px。
- **标签**：100px 胶囊形，灰粉半透明底，深棕灰文字。
- **图标块**：48px 圆角方块（14px 圆角），淡彩色底，放 emoji 或简单符号。
- **圆斑**：120-420px 正圆，灰粉或赭石，低透明度，位于内容层下方（z-index: 0）。
- **按钮**：100px 胶囊，深棕灰底奶油色文字，带大柔和阴影。

## Do / Don't

- **Do** 给所有容器加 20px 圆角。
- **Do** 使用双层柔和阴影营造悬浮感。
- **Do** 用圆斑和色块增加温暖氛围。
- **Don't** 不要使用 0px 圆角或 1px 硬描边。
- **Don't** 不要使用冷色系颜色。
- **Don't** 不要使用深色背景（除了单张反转卡片）。

## 实现注意事项

- **必须**确保 `.slide` 有 `transform: translate(-50%, -50%)`，否则内容会跑到右下角。
- 字体栈：`'Plus Jakarta Sans', 'Noto Sans SC', sans-serif`。
- 柔和渐变背景 + 大圆角卡片，卡片有轻微阴影。
- 装饰性圆形 blob 必须 `pointer-events: none` 且 z-index 低于内容。
- 整体色调温暖，不要引入冷色。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景为奶油色 `#FAF6EF`，所有卡片为白色 20px 圆角配双层柔和阴影。主色是灰粉 `#E8D5D0` 和赭石 `#D4A574`。字体全程 Plus Jakarta Sans。所有按钮和标签使用 100px 胶囊圆角。背景层可加低透明度彩色圆斑装饰。禁止使用冷色、硬边和高饱和色。
