---
name: Nouveau
version: 1.0.0
category: painterly
tags: [art-nouveau, gold-frame, floral, ornamental, serif, elegant]

color:
  background: "#F0E6D3"
  foreground: "#2D2A22"
  green: "#2D4A3E"
  gold: "#B8944F"
  purple: "#7D5A6E"
  cream: "#FAF5EA"
  muted: "#7A7060"

typography:
  heading:
    family: "Playfair Display, Georgia, serif"
    weight: 700-900
    letter_spacing: "0.02-0.05em"
  body:
    family: "Cormorant Garamond, Georgia, serif"
    weight: 400
  en:
    family: "Playfair Display, serif"
    weight: 700
    letter_spacing: "0.2em"
  scale:
    display: "100px"
    h1: "72px"
    h2: "36px"
    body: "16px"
    caption: "12px"

spacing:
  slide_padding: "72px 90px"
  gap_large: "32px"
  gap_medium: "24px"

radius:
  base: "0px"

shadow:
  none: true

border:
  width: "1-2px"
  style: "solid"
  color: "#B8944F"
---

# Nouveau（新艺术运动）— Design Specification

## 气质

Art Nouveau 的优雅与有机感。双层金线框包裹版面，四角有程式化的植物角花，中央可放置圆形纹章。深森林绿 + 暖金 + 暗紫的配色，Playfair Display 的高对比衬线体，像 1900 年巴黎世博会的海报——装饰性强但不浮夸，有机曲线克制使用。

## 色彩规则

- **背景**：暖象牙 `#F0E6D3`。
- **森林绿** `#2D4A3E`：主标题、深色文字、强调。
- **暖金** `#B8944F`：所有线条、边框、角花、装饰——系统的骨架。
- **暗紫** `#7D5A6E`：辅助点缀，用于章节号、小标签。
- **奶油白** `#FAF5EA`：卡片底色。
- **禁止**：高饱和色、冷灰、无金色的页面。

## 字体规则

- 英文标题用 **Playfair Display 700-900**，高对比衬线，字距 0.02-0.05em。
- 正文用 **Cormorant Garamond 400**，行高 1.8。
- 中文用 **Noto Serif SC**（如需要）。
- 标签/章节号用小号大写，暗紫色或金色。

## 版式规则

- **双层金线框**：外层 2px 金色（距边 24px），内层 0.5px 金色（距边 32px），包裹整个版面。
- **角花**：四角放置程式化植物 SVG 曲线（对称的 S 形卷草 + 叶片），金色。
- **圆形纹章**：封面/章节页中央或右侧放置金色同心圆纹章（3-4 层），可内含章节号。
- 内容区在框内，padding 72px 90px。
- 卡片：奶油白底 + 1px 金色边框，无圆角。
- 双栏用金色竖线分隔。
- 金句页：深绿大字居中，上下金色装饰线。

## 组件模式

- **双层框**：`border: 2px solid #B8944F` + `::before` 绝对定位 0.5px 金色内框（inset 8px）。
- **角花**：SVG `<path>` 绘制对称卷草曲线，金色 1.5px stroke，放在四角绝对定位。
- **纹章**：SVG `<circle>` 多层金色描边，中心可放数字或字母。
- **分隔线**：金色 1px 横线，两端带菱形或圆点装饰。
- **卡片**：`background: #FAF5EA; border: 1px solid #B8944F;`。

## Do / Don't

- **Do** 每页必须有金色边框和角花。
- **Do** 装饰曲线要有机、流畅、对称。
- **Don't** 不要使用几何直线、直角装饰（那是 Art Deco）。
- **Don't** 不要让装饰压过内容——角花和纹章是框架不是主体。
- **Don't** 不要使用圆角、阴影、渐变。

## 实现注意事项

- 字体栈：`'Playfair Display', 'Cormorant Garamond', 'Noto Serif SC', Georgia, serif`。
- **CSS 声明之间不能漏分号**。
- 新艺术运动装饰边框用 SVG path（对称曲线、植物藤蔓），必须 `pointer-events: none`。
- 暖米色背景 `#F0E6D3`，墨绿 `#2D4A3E` + 金色 `#B8860B`。
- 装饰边框不能遮挡内容，内容区需要足够 padding。
- 页脚深色文字，无 bottom-band。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景暖象牙 #F0E6D3。每页有双层金色线框（2px+0.5px #B8944F）和四角金色植物角花 SVG。封面有金色同心圆纹章。标题 Playfair Display 700 深森林绿 #2D4A3E，正文 Cormorant Garamond。卡片奶油白 #FAF5EA + 金色边框。暗紫 #7D5A6E 做小面积点缀。装饰用有机曲线，禁止几何直角、圆角、阴影。
