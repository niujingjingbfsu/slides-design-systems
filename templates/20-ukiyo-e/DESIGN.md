---
name: Ukiyo-e
version: 1.0.0
category: painterly
tags: [japanese, ukiyo-e, indigo, red-seal, wave, fuji, woodblock]

color:
  background: "#F2EAD8"
  foreground: "#1A1A1A"
  indigo: "#1B3A6B"
  indigo_light: "#2C5F8A"
  red: "#C8362C"
  paper: "#F2EAD8"
  muted: "#6B6355"

typography:
  heading:
    family: "Shippori Mincho, Noto Serif JP, serif"
    weight: 700-800
    letter_spacing: "0.05-0.1em"
  body:
    family: "Noto Serif SC, serif"
    weight: 400
  en:
    family: "Shippori Mincho, serif"
    weight: 600
    letter_spacing: "0.2em"
  scale:
    display: "110px"
    h1: "72px"
    h2: "36px"
    body: "15px"
    caption: "12px"

spacing:
  slide_padding: "56px 80px"
  gap_large: "28px"
  gap_medium: "24px"

radius:
  base: "0px"

shadow:
  none: true

border:
  width: "1-2px"
  style: "solid"
  color: "#1B3A6B"

progress_bar:
  height: "56px"
  background: "var(--bg)"
  border_top: "1px solid rgba(30,50,100,0.15)"
  section_label:
    font: "var(--font-cn)"
    size: "12px"
    weight: "700"
    color: "var(--muted)"
    letter_spacing: "0.25em"
  page_number:
    font: "var(--font-cn)"
    size: "16px"
    weight: "700"
    color: "var(--indigo, #1E3468)"
    letter_spacing: "0.1em"
  segments:
    shape: "line"
    size: "5px"
    gap: "5px"
    section_gap: "24px"
    future: "faint fill; w=32px, h=5px"
    past: "medium fill"
    current: "var(--indigo, #1E3468) fill"

---

# Ukiyo-e（浮世绘）— Design Specification

## 气质

浮世绘木版画的平面装饰感。和纸暖米色底 + 靛蓝主色 + 朱红印章色。富士山用极简三角形 + 雪顶白线表现，波浪用重复的弧形线带（青海波），朱红印章作为签名式点缀。Shippori Mincho 明朝体有雕版感。平面化、无透视、轮廓线清晰——北斋漫画的构图逻辑。

## 色彩规则

- **背景**：和纸米 `#F2EAD8`，可带极淡的纸纹。
- **靛蓝** `#1B3A6B`：主标题、山形、波浪、边框、主要文字——木版画的"蓝"。
- **浅靛** `#2C5F8A`：辅助线、波浪第二层、次要文字。
- **朱红** `#C8362C`：印章、小面积强调——全页只出现 1-2 处。
- **禁止**：渐变色、高饱和多色、无靛蓝的页面。
- 朱红是"印章色"，只做小方块/小圆点，不做大色块。

## 字体规则

- 标题用 **Shippori Mincho 700-800**（日本明朝体，有雕版感），靛蓝色。
- 正文用 **Noto Serif SC 400**，行高 1.8。
- 英文/标签用 Shippori Mincho 600，大写 + 0.2em 字距。
- 印章内文字用小号白字或反白。

## 版式规则

- **木刻双线框**：外层 2px 靛蓝（距边 20px）+ 内层 0.5px 靛蓝（距边 28px）。
- **富士山**：封面/章节页放置极简三角形 SVG（靛蓝填充 + 顶部白色雪顶折线），可大可小。
- **波浪带**：底部或侧边放置 2-3 层重复弧形线（青海波 pattern），靛蓝/浅靛，像《神奈川冲浪里》的浪尖。
- **朱红印章**：每页右下角或标题旁放置 28-40px 朱红方块（可带白色边框），内有白色汉字或字母——像版画家的落款。
- 卡片：和纸底 + 1px 靛蓝边框，无圆角。
- 双栏用靛蓝竖线分隔。
- 金句页：靛蓝大字，旁配朱红印章。
- 数据四栏：数字用 Shippori Mincho 大字靛蓝，下方浅靛波浪线装饰。

## 组件模式

- **富士山**：SVG `<polygon points="0,200 150,20 300,200" fill="#1B3A6B"/>` + 雪顶 `<polyline points="100,80 150,20 200,80" fill="none" stroke="#F2EAD8" stroke-width="6"/>`。
- **波浪**：SVG `<path d="M0 40 Q20 20 40 40 Q60 60 80 40..." stroke="#1B3A6B" fill="none" stroke-width="2"/>`，重复 2-3 层不同透明度。
- **印章**：`<div style="width:36px;height:36px;background:#C8362C;display:flex;align-items:center;justify-content:center;color:#F2EAD8;font-size:14px;">印</div>`，可加 2px 白色边框。
- **双线框**：`border: 2px solid #1B3A6B` + `::before` inset 8px 的 0.5px 靛蓝框。
- **卡片**：`background: rgba(255,255,255,0.3); border: 1px solid #1B3A6B;`。

## Do / Don't

- **Do** 每页必须有靛蓝元素和木刻边框。
- **Do** 朱红只做印章大小的小面积点缀。
- **Do** 所有图形平面化、轮廓清晰、无渐变无阴影。
- **Don't** 不要画写实的富士山照片或复杂风景。
- **Don't** 不要让朱红大面积出现——它是印章不是主色。
- **Don't** 不要使用圆角、渐变、阴影、3D 效果。

## 实现注意事项

- 字体栈：`'Noto Serif JP', 'Shippori Mincho', 'Noto Serif SC', serif`。日文字体已覆盖中文字符。
- 浮世绘风格用 SVG 实现（波浪、山、云的简化线条），不要用图片。
- 暖纸色 `#F5E6D3`，靛蓝 `#2D4A6E` + 朱红 `#C8402C`。
- 装饰元素（波浪、山）在背景层，z-index 低于内容。
- 页脚深色文字，无 bottom-band。
- 整体风格是平面色块 + 粗轮廓线，不要渐变和阴影。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景和纸米 #F2EAD8。主色靛蓝 #1B3A6B，朱红 #C8362C 只做小印章。每页有木刻双线框（2px+0.5px 靛蓝）。封面有极简 SVG 三角形富士山（靛蓝填充+白色雪顶线），底部有 2-3 层靛蓝弧形波浪线。右下角朱红方形印章内白色汉字。标题 Shippori Mincho 明朝体靛蓝色。所有图形平面化，禁止渐变、圆角、阴影、写实风景。
