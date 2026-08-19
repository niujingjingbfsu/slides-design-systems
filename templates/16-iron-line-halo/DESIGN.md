---
name: Iron Line & Halo
version: 1.0.0
category: painterly-abstract
tags: [chinese, dunhuang, iron-line, halo, gold, earth-tones, curves]

color:
  background: "#F0E4D0"
  foreground: "#2A1F14"
  red: "#B85C38"
  ochre: "#C4956A"
  azurite: "#3A6B8C"
  gold: "#D4A843"
  gold_bright: "#E8C868"
  gold_deep: "#9A7B1A"
  muted: "#7A6B54"

typography:
  heading:
    family: "Noto Serif SC, serif"
    weight: 900
    letter_spacing: "0.08em"
  body:
    family: "Noto Serif SC, serif"
    weight: 400
  en:
    family: "Cormorant Garamond, Georgia, serif"
    weight: 600-700
    letter_spacing: "0.3-0.4em"
  scale:
    display: "120px"
    h1: "80px"
    h2: "40px"
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
  width: "1px"
  style: "solid"
  color: "#D4A843"
---

# Iron Line & Halo（敦煌·铁线圆光）— Design Specification

## 气质

敦煌壁画的抽象转译。不画飞天佛像，而抽取两个核心视觉语法：**铁线描**（粗细均匀、力透纸背的流动曲线）和**圆光**（同心圆光环）。铁线成为贯穿版面的分隔与动势，圆光成为内容容器和视觉焦点。土红暖底 + 泥金线条 + 大地色系，有壁画的沉着华丽，但没有任何宗教人物形象。

## 色彩规则

- **背景**：暖米色 `#F0E4D0`，带极淡的颗粒质感（多层 radial-gradient 模拟壁画肌理）。
- **土红** `#B85C38`：主标题、强调色块、铁线主脉——洞窟墙壁的颜色。
- **泥金** `#D4A843`（亮部 `#E8C868`，深部 `#9A7B1A`）：圆光环、装饰线、边饰、英文标签——必须有金属渐变感。
- **石青** `#3A6B8C`：辅助点缀，只用于边饰和小面积对比。
- **赭石** `#C4956A`：辅助色。
- **禁止**：高饱和冷色、纯白背景、无金色的页面。

## 字体规则

- 中文标题用 **Noto Serif SC 900**，字距 0.08em，土红色。
- 英文用 **Cormorant Garamond 600-700**，大写 + 0.3-0.4em 字距，泥金色。
- 正文用 Noto Serif SC 400，行高 1.8。
- 金色文字和线条必须有**金属渐变**（linear-gradient 从 #E8C868 到 #9A7B1A），不能是平涂金色。

## 版式规则

- **铁线曲线**：每页有 1-3 条 SVG 贝塞尔曲线（`Q` 二次贝塞尔），从画面一侧蜿蜒至另一侧，土红（低透明度粗线）+ 泥金（中透明度细线）叠加，形成飘带的抽象动势。
- **圆光环**：泥金渐变描边的同心圆（2-4 层），作为视觉焦点或内容容器，线宽从外到内递减。
- **忍冬纹边带**：上下各 32px 高装饰带，由重复的弧形 + 圆点组成（SVG path），泥金色，底色为极淡的金色/石青透明色。
- 卡片：半透明白底 `rgba(255,255,255,0.35)` + 1px 泥金描边 + 内嵌 0.5px 描边（双层框）。
- 双栏：一栏土红底白字，一栏半透明白底。
- 金句页：土红大字 + 金色强调词。

## 组件模式

- **铁线**：SVG `<path d="M-20 80 Q200 200 400 280 Q600 360 500 500..." stroke="#B85C38" stroke-width="10" fill="none" opacity="0.1"/>`，叠加一条金色 `stroke="#D4A843" stroke-width="3" opacity="0.55"`。
- **圆光**：SVG `<circle>` 多层，外层用 `stroke="url(#goldGrad)"` 金属渐变 3-3.5px，内层递减。
- **金属渐变**：`<linearGradient><stop offset="0%" stop-color="#E8C868"/><stop offset="100%" stop-color="#9A7B1A"/></linearGradient>`。
- **忍冬纹边带**：32px 高 SVG，重复 `Q` 弧形 + `<circle>` 圆点，泥金填充。
- **双层框卡片**：外框 1px 泥金 + `::before` 内框 0.5px 泥金（offset 6px）。
- **金色装饰线**：标题下方 120px 宽泥金渐变线 + 菱形端点。

## Do / Don't

- **Do** 每页必须有可见的泥金元素（光环、铁线、边饰或文字）。
- **Do** 金色用线性渐变模拟金属感，不要平涂。
- **Do** 铁线用土红粗线 + 泥金细线叠加。
- **Don't** 不要画佛像、飞天、菩萨、供桌等宗教形象。
- **Don't** 不要使用圆角、box-shadow。
- **Don't** 不要让金色变成土黄色——必须有明暗渐变。

## 实现注意事项

- 字体栈：`'Noto Serif SC', 'Cormorant Garamond', Georgia, serif`。
- **nav-hint/counter 必须在 `bottom: 40px`**，不能在 `bottom: 8px`——底部 32px 是装饰波浪纹边框区域，页脚文字在其中，nav-hint 必须在边框上方。
- 铁线描用 SVG path，1.5-2px 线宽，朱红 `#B85C38` + 泥金 `#D4A843`。
- 圆光（同心圆）用 SVG circle，泥金细线，低透明度。
- 暖绢底色 `#F2E8D5`，不要用纯白。
- 页脚朱红/泥金文字在装饰边框内。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景暖米色 #F0E4D0 带极淡颗粒。每页有 SVG 贝塞尔铁线曲线（土红低透明粗线 + 泥金渐变细线叠加）和泥金同心圆光环（金属渐变描边，2-4层）。上下有 32px 忍冬纹弧形圆点装饰带。中文标题 Noto Serif SC 900 土红色，英文 Cormorant Garamond 大写泥金色。金色必须用 linear-gradient(#E8C868→#9A7B1A) 模拟金属感。卡片半透明白底+双层泥金描边。禁止画宗教人物、圆角、阴影。
