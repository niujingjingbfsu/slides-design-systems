---
name: Electric
version: 1.0.0
category: bold-colorful
tags: [gradient, mesh, bold, energetic, glass, modern]

color:
  background_gradient: "linear-gradient(135deg, #FF6B35 0%, #FF3D7F 40%, #7B2FF7 100%)"
  foreground: "#FFFFFF"
  muted: "rgba(255,255,255,0.7)"
  orange: "#FF6B35"
  pink: "#FF3D7F"
  purple: "#7B2FF7"

typography:
  heading:
    family: "Sora, -apple-system, sans-serif"
    weight: 800-900
    letter_spacing: "-0.025em to -0.04em"
  body:
    family: "Sora, -apple-system, sans-serif"
    weight: 400
  scale:
    display: "130px"
    h1: "96px"
    h2: "26px"
    body: "14px"
    caption: "12px"

spacing:
  slide_padding: "64px 80px"
  gap_large: "28px"
  gap_medium: "24px"

radius:
  base: "20px"
  card: "20px"
  pill: "100px"
  lg: "24px"

shadow:
  card: "0 8px 32px rgba(0,0,0,0.1)"
  button: "0 12px 40px rgba(0,0,0,0.2)"

glass:
  background: "rgba(255,255,255,0.12)"
  backdrop_filter: "blur(16px)"
  border: "1px solid rgba(255,255,255,0.2)"
---

# Electric — Design Specification

## 气质

大胆的高饱和 mesh 渐变。橙→粉→紫 135 度铺满整个画面，白色超粗字体压在上面，磨砂玻璃卡片漂浮其间。色彩激烈但排版干净——像音乐节海报一样有能量，但不失秩序。

## 色彩规则

- **背景**：135deg 三色渐变 `#FF6B35` → `#FF3D7F` → `#7B2FF7`，铺满全页。
- **前景**：纯白 `#FFFFFF`。
- **辅助文字**：`rgba(255,255,255,0.7)`。
- 背景层可加 2-3 个大尺寸模糊色块（blur 60px）增强 mesh 感，颜色用半透明的橙/紫/粉。
- **禁止**：纯色背景、深色文字、低饱和色。

## 字体规则

- 全程使用 **Sora**，几何无衬线。
- 标题字重 800-900，字距 -0.025em 至 -0.04em，全大写。
- 封面 display 字号 130px，用极紧字距和超粗字重压住强烈背景。
- 正文字重 400，行高 1.6-1.7。
- 标签用大写 + 0.08em 字距 + 半透明白底胶囊。

## 版式规则

- 背景层放 2-3 个 `blur(60px)` 的大彩色圆形（mesh blobs），增强渐变深度。
- 内容卡片用**磨砂玻璃**：`rgba(255,255,255,0.12)` + `backdrop-filter: blur(16px)` + 1px 白色半透明描边 + 20px 圆角。
- 双栏页：一张玻璃卡 + 一张纯白实色卡（紫色文字）形成虚实对比。
- 金句页：关键词可用白色半透明高亮块（`rgba(255,255,255,0.2)` + 圆角）。
- 数据页四栏玻璃卡片，白色大数字。
- 按钮：纯白底 + 紫色文字 + 100px 胶囊 + 柔和投影。

## 组件模式

- **Mesh blob**：300-500px 圆形，`border-radius: 50%`，`filter: blur(60px)`，半透明橙/紫/粉色，z-index: 0。
- **玻璃卡片**：`rgba(255,255,255,0.1)` + `blur(12-16px)` + 1px `rgba(255,255,255,0.18)` 描边 + 20px 圆角。
- **胶囊标签**：`rgba(255,255,255,0.15)` + blur + 1px 白色描边 + 100px 圆角，前面带白色发光小圆点。
- **白卡**：纯白底 + 深紫文字，用于需要最高对比度的 featured 内容。
- **按钮**：白底紫字，100px 胶囊，`0 12px 40px rgba(0,0,0,0.2)` 投影。

## Do / Don't

- **Do** 背景必须是橙→粉→紫的高饱和渐变。
- **Do** 用 blur(60px) 的 mesh blob 增加渐变层次。
- **Do** 卡片用磨砂玻璃效果，20px 圆角。
- **Don't** 不要在渐变背景上用深色文字。
- **Don't** 不要使用硬边描边或零圆角。
- **Don't** 不要降低渐变饱和度。

## 实现注意事项

- 字体栈：`'Sora', 'Noto Sans SC', sans-serif`。
- **双栏页右栏卡片禁止用纯白色**——在渐变背景上纯白块很突兀。必须用毛玻璃效果：`background: rgba(255,255,255,0.12); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.2);`
- 所有卡片在渐变背景上都用半透明毛玻璃，不要用实色。
- 渐变色是橙→粉→紫，不要引入其他色相。
- 大圆角（20-24px），不要直角。

## 常见陷阱与规避
- **Footer 必须贴底**：`.footer` 用 `margin-top: auto` 贴在幻灯片底部，不要用固定 `margin-top: 24px`（会导致 footer 跟着内容走）。同时加 `align-self: stretch` 确保在 `align-items: center` 的 section/closing 页也能撑满全宽。
- **z-index 层级规则用 `:where()`**：`.slide > *:not(:where(.blob)):not(:where(.footer))` 中的 `:where()` 优先级为 0，不会覆盖 `.float-card` 等装饰元素的 `position: absolute`。如果写成 `:not(.blob)` 不带 `:where()`，优先级 (0,3,0) 会盖过 `.title-slide .float-card` 的 (0,2,0)，导致绝对定位失效、元素被推到幻灯片外产生裁切阴影。
- **玻璃卡上的文字可读性**：`--muted: rgba(255,255,255,0.7)` 只适合短标签和单行描述。玻璃卡内的正文、列表项、多行文字应使用 ≥0.88 的白色不透明度，否则在亮渐变上难以辨认。
- **中英文混排对齐**：多列 meta 信息（如 VERSION/TEAM/AUTHOR）的 flex 容器必须设 `align-items: flex-start`，标签和值都要显式设 `line-height`（标签 `line-height: 1`，值 `line-height: 1.2-1.3`），否则 Sora（Latin）与 Noto Sans SC（CJK）字体度量差异会导致基线错位。
- **Footer 基线对齐**：`.footer` 设 `line-height: 1`，避免符号（◆ ■ 等）与文字在不同字体下基线不齐。
- **Grid 子项默认拉伸**：grid 布局中的卡片默认 `align-self: stretch` 会拉伸到行高。如果卡片只应包裹内容并垂直居中，显式设 `align-self: center`。
- **不要重复页码**：页码只在 `.footer` 内出现一次，不要额外加全局 `.counter` div，否则在 16:9 全屏时两个页码会重叠。

## 给 Coding Agent 的提示

> 请读取本 DESIGN.md。背景必须是 linear-gradient(135deg, #FF6B35, #FF3D7F, #7B2FF7) 高饱和渐变。加 2-3 个 blur(60px) 的半透明大圆形做 mesh 效果。所有文字白色，标题 Sora 800-900 全大写紧字距。卡片用磨砂玻璃 rgba(255,255,255,0.12)+blur(16px)+20px 圆角+白色半透明描边。双栏中一张可用纯白底紫字做对比。禁止深色文字和纯色背景。
