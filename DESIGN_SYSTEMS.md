# HTML Slides Design Systems — 完整合辑（20 套）

> 20 套 HTML Slides 模板的设计规范总集，分三批：冷静克制/轻盈/高端留白（7 套）、色彩鲜明（7 套）、绘画风格（6 套）。
> 每套包含 YAML design tokens + 设计理念 + 色彩/字体/版式/组件规则 + Do/Don't + Coding Agent 提示词。
> 将对应章节交给 AI coding agent，即可按规范生成一致风格的幻灯片。
>
> **技术栈**：纯 HTML + CSS + vanilla JS，1280×720（16:9），方向键翻页，transform scale 自适应，Google Fonts CDN，零依赖，单文件自包含。

---

## 总目录

### 第一批 · 冷静克制 / 轻盈 / 高端留白

| 编号 | 名称 | 方向 | 核心特征 | HTML 文件 |
|---|---|---|---|---|
| 01 | Systems（蓝图技术感） | 冷静克制 | 栅格底纹·等宽字体·赤陶色·零圆角 | `03-systems.html` |
| 02 | 静 Sei（日式禅意） | 冷静克制 | 宣纸米白·宋体大字·朱红印章·禅意留白 | `04-sei.html` |
| 03 | Soft Space（温暖柔和） | 轻盈 | 奶油底·灰粉圆斑·柔阴影·圆角卡片 | `05-soft-space.html` |
| 04 | Light as Air（通透梦幻） | 轻盈 | 磨砂玻璃·蓝紫渐变·光球·通透 | `06-light-as-air.html` |
| 05 | Breathe（清新自然） | 轻盈 | 纯白·鼠尾草绿·线描叶子·自然清新 | `07-breathe.html` |
| 06 | ESSENTIAL（画廊极简） | 高端留白 | 纯白·极细衬线·深蓝小方块·70%留白 | `08-essential.html` |
| 07 | Noir（暗夜奢雅） | 高端留白 | 纯黑·香槟金·角线·暗夜奢雅 | `09-noir.html` |

### 第二批 · 色彩鲜明 / 风格化强烈

| 编号 | 名称 | 方向 | 核心特征 | HTML 文件 |
|---|---|---|---|---|
| 08 | Brutal（新粗野主义） | 色彩鲜明 | 4px 黑描边·硬投影·三原色·零圆角 | `11-brutal.html` |
| 09 | Neon（合成波霓虹） | 色彩鲜明 | 霓虹粉/电光青·深紫渐变·透视网格·辉光 | `12-neon.html` |
| 10 | Pop!（波普艺术） | 色彩鲜明 | 亮黄底·半调网点·爆炸星·对话气泡 | `13-pop.html` |
| 11 | Electric（大胆渐变） | 色彩鲜明 | 橙→粉→紫 mesh·磨砂玻璃·超粗白字 | `14-electric.html` |
| 12 | Memphis（孟菲斯后现代） | 色彩鲜明 | 奶油底·亮粉青黄·波浪线·棋盘格 | `15-memphis.html` |
| 13 | Punk（瑞士朋克） | 色彩鲜明 | 黑白红·旋转错位·破碎网格·竖排文字 | `16-punk.html` |
| 14 | Tropic（热带热力） | 色彩鲜明 | 深青底·珊瑚橙黄·大太阳·大圆角 | `17-tropic.html` |

### 第三批 · 绘画风格（中西方）

| 编号 | 名称 | 方向 | 核心特征 | HTML 文件 |
|---|---|---|---|---|
| 15 | Mineral Strata（青绿矿物层叠） | 绘画风格 | 石青/石绿水平色带·泥金细线·几何三角山 | `21-mineral-strata.html` |
| 16 | Iron Line & Halo（敦煌铁线圆光） | 绘画风格 | 土红/泥金金属渐变·铁线曲线·同心圆光环 | `22-iron-line-halo.html` |
| 17 | Cobalt Circles（青花钴蓝同心圆） | 绘画风格 | 钴蓝五色阶·同心圆·海水纹边带 | `23-cobalt-circles.html` |
| 18 | Nouveau（新艺术运动） | 绘画风格 | 森林绿/暖金·双层金线框·角花纹章 | `24-nouveau.html` |
| 19 | Deco（装饰艺术） | 绘画风格 | 深夜蓝/金·旭日放射·Chevron·绝对对称 | `25-deco.html` |
| 20 | Ukiyo-e（浮世绘） | 绘画风格 | 靛蓝/朱红印章·富士三角·波浪带 | `26-ukiyo-e.html` |

---
---

# 第一批 · 冷静克制 / 轻盈 / 高端留白

---

## 01 · Systems（蓝图技术感）

> HTML 文件：`03-systems.html`

```yaml
color:
  background: "#F6F5F2"
  foreground: "#1A1A1A"
  muted: "#8A8580"
  accent: "#B85C38"
  accent_soft: "rgba(184, 92, 56, 0.10)"
  line: "rgba(26, 26, 26, 0.12)"
  grid: "rgba(26, 26, 26, 0.035)"
typography:
  heading: "JetBrains Mono 700, letter-spacing -0.02em"
  body: "Inter 300, line-height 1.6-1.7"
  label: "JetBrains Mono 700, uppercase, letter-spacing 0.18em"
```

**气质**：蓝图式的技术文档美学。像工程师的方格笔记本：精确、冷静、毫不含糊。所有元素对齐到 32px 栅格，间距是 32 的倍数。

**色彩**：暖灰底 `#F6F5F2` + 32px 极淡栅格线；赤陶色 `#B85C38` 仅用于分隔线、列表方点、标签、数字，面积不超过 5%。禁止渐变、阴影、彩色背景块。

**字体**：标题/标签 JetBrains Mono 等宽 700，字距紧凑；正文 Inter 300。

**版式**：严格左对齐（结尾页角标除外）；双栏用 1px 线条分隔形成表格感；章节页右下角放 200px 半透明数字；结尾页四角 L 形角标。

**组件**：赤陶色 8px 方块列表标记；无圆角无阴影 1px 描边卡片。

**Do / Don't**：
- Do 用 1px 线条分隔，不用阴影；间距落在 32px 栅格上
- Don't 加圆角；赤陶色不超过画面 5%；不居中排版

**Agent 提示词**：
> 所有颜色、字体、间距必须使用上述 token，禁止自行发明颜色或圆角。背景叠加 32px 栅格线。强调色 #B85C38 仅用于线条、方点和小标记。所有卡片 1px 实线描边，无阴影无圆角。正文 Inter 300，标题标签 JetBrains Mono 700。

---

## 02 · 静 Sei（日式禅意）

> HTML 文件：`04-sei.html`

```yaml
color:
  background: "#F5F2EB"
  foreground: "#1A1A1A"
  muted: "#8C867B"
  accent: "#B33A2A"
typography:
  heading: "Noto Serif SC 500, letter-spacing 0.04em"
  display: "Noto Serif SC 900, 160px, letter-spacing 0.1em"
  body: "Noto Sans SC 300, line-height 1.8-2.0"
```

**气质**：日式禅意极简。米白宣纸为底，墨黑大字为骨，朱红印章为魂。留白占约 70%，"间"（ま）是核心。

**色彩**：宣纸米白 `#F5F2EB`；墨黑 `#1A1A1A`；朱红 `#B33A2A` 仅用于 44px 印章方块（圆角 2-3px，内白色篆字），绝不用作线条或文字。

**字体**：标题 Noto Serif SC，封面 900/160px；正文 Noto Sans SC 300，行高 1.8-2.0。

**版式**：封面印章+大字居中；章节页左对齐大标题+右下角半透明大字；内容页左宋体引导文+右朱红圆点列表；金句页居中大号宋体+朱红引号「」。

**Do / Don't**：
- Do 留白不少于 60%；朱红只做印章
- Don't 加阴影、渐变、纹理、圆角卡片、填满画面

**Agent 提示词**：
> 背景 #F5F2EB，文字墨黑，唯一强调色朱红 #B33A2A 且只用于 44px 印章方块（白色汉字）。标题 Noto Serif SC，正文 Noto Sans SC 300。所有分隔线 1px 实线，无圆角无阴影。每页留白不少于 60%。不要添加任何额外颜色或装饰。

---

## 03 · Soft Space（温暖柔和）

> HTML 文件：`05-soft-space.html`

```yaml
color:
  background: "#FAF6EF"
  foreground: "#3D3530"
  muted: "#9A8F86"
  accent: "#E8D5D0"
  accent_deep: "#D4A574"
  card: "#FFFFFF"
typography:
  heading: "Plus Jakarta Sans 700-800, letter-spacing -0.02em to -0.03em"
  body: "Plus Jakarta Sans 400, line-height 1.6-1.7"
radius:
  base: "20px"
  pill: "100px"
shadow:
  card: "0 8px 32px rgba(61,53,48,0.06), 0 2px 8px rgba(61,53,48,0.04)"
```

**气质**：温暖、柔和、亲切。午后阳光照进奶油色房间。所有边角圆润，阴影弥散柔和。

**色彩**：暖奶油 `#FAF6EF`；灰粉 `#E8D5D0` 主强调；浅赭石 `#D4A574` 次强调；白色卡片；大号模糊圆斑（15%-50% 透明度）漂浮背景层。禁止冷色、硬边、高饱和。

**字体**：全程 Plus Jakarta Sans，标题 700-800，正文 400。

**版式**：封面大标题+灰粉圆斑透出+浮动玻璃小卡；三栏圆角卡片网格；双栏一白一深棕灰反转；四栏白色圆角卡片+彩色大数字。

**组件**：20px 圆角白色卡片+双层柔阴影；100px 胶囊标签；48px 圆角图标块；120-420px 彩色圆斑（z-index:0）。

**Do / Don't**：
- Do 所有容器 20px 圆角；双层柔阴影；圆斑装饰
- Don't 0px 圆角或 1px 硬描边；冷色系；深色背景（单张反转卡除外）

**Agent 提示词**：
> 背景奶油色 #FAF6EF，所有卡片白色 20px 圆角配双层柔和阴影。主色灰粉 #E8D5D0 和赭石 #D4A574。字体全程 Plus Jakarta Sans。按钮标签 100px 胶囊圆角。背景层可加低透明度彩色圆斑。禁止冷色、硬边、高饱和。

---

## 04 · Light as Air（通透梦幻）

> HTML 文件：`06-light-as-air.html`

```yaml
color:
  background_gradient: "linear-gradient(135deg, #FFFFFF 0%, #EEF1FA 45%, #E4E9F8 100%)"
  foreground: "#1E2A5E"
  muted: "#6B7A99"
  glass: "rgba(255,255,255,0.45)"
  lavender: "#B8C0E8"
  sky: "#A8D8E8"
  blush: "#E8D0E8"
typography:
  heading: "Sora 600-700, letter-spacing -0.025em to -0.035em"
  body: "Sora 300, line-height 1.6-1.7"
radius:
  base: "24px"
  lg: "32px"
glass:
  background: "rgba(255,255,255,0.45)"
  backdrop_filter: "blur(20px) saturate(1.4)"
  border: "1px solid rgba(255,255,255,0.7)"
```

**气质**：通透、梦幻、失重。磨砂玻璃卡片漂浮在淡蓝紫渐变之上，彩色光球弥散。深度来自模糊和光线。

**色彩**：135deg 白→`#EEF1FA`→`#E4E9F8` 渐变；深靛蓝 `#1E2A5E` 文字；薰衣草/天蓝/粉紫氛围色用于模糊光球；玻璃面半透明白+blur(20px)。标题可用深靛蓝到薰衣草紫渐变文字。

**字体**：全程 Sora，标题 600-700，正文 300。

**版式**：封面左标题+右浮动玻璃卡；章节页居中 32px 圆角玻璃卡；三栏玻璃卡片；双栏一玻璃一深靛蓝实色；金句页渐变文字强调。

**组件**：24px 圆角玻璃卡（半透明+blur+白描边）；200-500px blur(40px) 光球（z-index:0）；深靛蓝渐变实色卡。

**Do / Don't**：
- Do 所有卡片磨砂玻璃效果；背景多个模糊光球；渐变文字点缀
- Don't 不透明白色卡片；0px 圆角或硬边框；光球遮挡内容

**Agent 提示词**：
> 背景白到淡蓝紫 135deg 渐变。所有卡片 rgba(255,255,255,0.45)+backdrop-filter:blur(20px) 磨砂玻璃，24px 圆角，1px 白色半透明描边。背景层放 2-3 个 blur(40px) 彩色光球。字体 Sora。深靛蓝 #1E2A5E 用于文字和实心卡片。禁止不透明卡片和硬边。

---

## 05 · Breathe（清新自然）

> HTML 文件：`07-breathe.html`

```yaml
color:
  background: "#FFFFFF"
  foreground: "#2D3D35"
  muted: "#8A9A8E"
  sage: "#A8C4A2"
  sage_deep: "#6B8F6B"
  sage_light: "#E8F0E6"
  sage_pale: "#F4F8F2"
typography:
  heading: "Manrope 700-800, letter-spacing -0.025em to -0.04em"
  body: "Manrope 400, line-height 1.7-1.8"
radius:
  base: "10px"
  card: "16-20px"
  pill: "100px"
shadow:
  none: true
```

**气质**：清新、干净、自然。纯白底上只有鼠尾草绿说话，手绘线描叶子和有机形状。留白充裕，行距宽松，无阴影。

**色彩**：纯白底；鼠尾草绿 `#A8C4A2` 主色；深绿 `#6B8F6B` 用于数字和强调；浅绿 `#E8F0E6`/`#F4F8F2` 用于标签底和卡片底。禁止第二种彩色、阴影、深色背景。

**字体**：全程 Manrope，标题 700-800，正文 400，行高 1.7-1.8。

**版式**：大 padding（72px 96px）；封面左标题+右 320px 线描叶子 SVG；章节页左对齐+大圆斑+小叶子；内容页左引导文（关键词鼠尾草绿高亮下划线）+右叶子图标列表；双栏一白一淡绿；四栏淡绿底卡片+进度条。

**组件**：100px 胶囊标签（浅绿底深绿字+绿圆点）；SVG 线描叶子（1.5px 鼠尾草绿描边无填充）；有机形状（不规则 border-radius）；4px 进度条；荧光笔高亮（linear-gradient 透明 60%→浅绿 60%）。

**Do / Don't**：
- Do 纯白底+鼠尾草绿一个色系；SVG 线描叶子；宽松行距
- Don't 任何阴影；绿色以外彩色；深色背景

**Agent 提示词**：
> 背景纯白，唯一颜色鼠尾草绿系（#A8C4A2/#6B8F6B/#E8F0E6/#F4F8F2）。字体全程 Manrope，行高 1.7-1.8。无阴影。装饰用 SVG 线描叶子（1.5px 描边无填充）和有机形状。卡片 16-20px 圆角，白底或淡绿底。禁止第二种彩色或阴影。

---

## 06 · ESSENTIAL（画廊极简）

> HTML 文件：`08-essential.html`

```yaml
color:
  background: "#FFFFFF"
  foreground: "#0A0A0A"
  muted: "#999999"
  faint: "#CCCCCC"
  accent: "#1A3A5C"
typography:
  heading: "Cormorant Garamond 300, letter-spacing -0.01em to -0.015em"
  italic: "Cormorant Garamond 300 italic"
  body: "Inter 300"
  label: "Inter 400, uppercase, letter-spacing 0.2em"
  scale:
    display: "168px"
    h1: "120px"
radius:
  base: "0px"
shadow:
  none: true
```

**气质**：画廊级极简。纯白空间中极细衬线体是绝对主角，一个深蓝色小方块是唯一色彩。70% 以上留白，设计自信来自删去一切可有可无之物。

**色彩**：纯白底；近黑 `#0A0A0A`；深蓝 `#1A3A5C` 仅用于 7-10px 小方块、数字单位、个别强调词，面积不超过 1%。禁止渐变、阴影、色块填充、圆角。

**字体**：标题/数字 Cormorant Garamond Light 300（灵魂字体）；斜体 300 用于强调词（唯一"装饰"）；正文/标签 Inter Light 300，标签大写+0.2em 字距。Display 120-168px，用字号而非粗细建立层级。绝对不用 bold。

**版式**：留白≥70%；封面左对齐 168px 大标题；章节页 120px 标题+80px 黑色短横线；内容页 1fr 1.2fr 双栏（左衬线引导文 26px light，右编号列表）；金句页 120px 灰色大引号+56px 衬线金句+深蓝强调词；数据页衬线 96px light 数字+深蓝斜体单位。无卡片，内容直接放白底。

**组件**：7-10px 深蓝实心方块；1px #CCCCCC 短横线（40-80px）；衬线编号；10px 大写 Inter 页脚。

**Do / Don't**：
- Do 衬线细体承载所有重量；斜体替代加粗；留白≥70%
- Don't bold；圆角/阴影/渐变；卡片或色块容器；深蓝超过 1%

**Agent 提示词**：
> 背景纯白，文字近黑，唯一强调色深蓝 #1A3A5C 且只用于 7-10px 小方块和个别文字。所有标题 Cormorant Garamond 300（极细），强调用 italic 300，绝对不用 bold。正文标签 Inter 300，标签大写+0.2em 字距。无圆角无阴影无卡片。每页留白 70% 以上。分隔线只用 1px #CCCCCC。

---

## 07 · Noir（暗夜奢雅）

> HTML 文件：`09-noir.html`

```yaml
color:
  background: "#0A0A0A"
  foreground: "#FFFFFF"
  muted: "#666666"
  gold: "#C9A96E"
  gold_dim: "rgba(201,169,110,0.3)"
  line: "rgba(255,255,255,0.08)"
typography:
  heading: "Cormorant Garamond 300, letter-spacing 0.02-0.08em"
  italic: "Cormorant Garamond 300 italic, color #C9A96E"
  body: "Inter 300, 13px, line-height 1.8"
  label: "Inter 400, uppercase, letter-spacing 0.25-0.4em"
radius:
  base: "0px"
shadow:
  none: true
```

**气质**：暗夜奢雅。纯黑是舞台，白色衬线是追光，香槟金是低语。四角 L 形角线像画框，居中对称、元素极少、字距宽松——高级定制邀请函。

**色彩**：纯黑 `#0A0A0A`；纯白文字；香槟金 `#C9A96E` 仅用于斜体强调词、短横线、角线、章节编号，绝不大面积填充。禁止渐变、阴影、发光（glow）、圆角。

**字体**：标题 Cormorant Garamond Light 300，字距 0.02-0.08em；金色斜体 300 做唯一色彩强调；正文 Inter Light 300/13px；标签 Inter 400 大写+0.25-0.4em 字距。

**版式**：每页四角 32px L 形金色半透明角线（标志元素，距边 40px）；封面居中对称（Edition 标签+140px 大标题+金色渐变横线）；章节页金色斜体章节号+大标题；内容页三栏等宽居中（罗马数字+金色短线+标题+说明）；双栏两张 1px 描边卡片（一白一金边）；金句页金色大引号+白色衬线金句。

**组件**：32px L 形角线 `rgba(201,169,110,0.3)`；60px 金色渐变横线（透明→金→透明）；无圆角 1px 描边卡片 padding 48px；5px 金色圆点；衬线 40px 罗马数字。

**Do / Don't**：
- Do 每页四角 L 形角线；金色斜体唯一色彩强调；居中对称
- Don't 金色大面积填充；发光/阴影/渐变背景；粗体或圆角；左对齐核心内容

**Agent 提示词**：
> 背景纯黑 #0A0A0A，文字白色，唯一强调色香槟金 #C9A96E（只用于斜体词、细线和角线）。每页四角必须有 32px L 形 rgba(201,169,110,0.3) 描边。标题 Cormorant Garamond 300，强调用金色 italic 300。标签 Inter 大写+0.3em 字距。无圆角无阴影无渐变。内容居中对称。金色横线用透明渐变收尾。

---
---

# 第二批 · 色彩鲜明 / 风格化强烈

---

## 08 · Brutal（新粗野主义）

> HTML 文件：`11-brutal.html`

```yaml
color:
  background: "#FFFFFF"
  foreground: "#000000"
  red: "#E63946"
  yellow: "#FFD93D"
  blue: "#2563EB"
typography:
  heading: "Archivo Black, uppercase, letter-spacing -0.02em, display 130px"
  body: "Inter 600-800"
radius:
  base: "0px"
shadow:
  card: "8px 8px 0 #000"
border:
  width: "4px solid #000"
```

**气质**：厚黑边框、硬边投影、三原色，像大字报一样直接生猛。每个元素像剪刀剪出来贴上去的，带手工拼贴 raw 感。

**色彩**：纯白底+纯黑描边文字；红 `#E63946`/黄 `#FFD93D`/蓝 `#2563EB` 原色用于卡片底、几何形状、标签、数字。禁止渐变、柔和色、透明度过渡、灰色。

**字体**：标题 Archivo Black 全大写（封面 130px）；正文 Inter 600-800（不用细体）；可用 `-webkit-text-stroke: 3px #000` 空心字。

**版式**：所有容器 4px 黑描边+8px 硬投影（0 模糊纯黑）；零圆角；封面左标题+右堆叠彩色几何形状；三栏卡片不同底色（黄/白/红）撞色；双栏一白一黑反转；金句黄卡微旋转 1-2°+红色硬投影。

**组件**：4px 黑描边+硬投影卡片 padding 28px；黑底白字/彩底黑字标签 padding 6-8px 16-20px；方块/圆形/三角形几何形状（都带描边投影）；彩色底+4px 描边+6px 硬投影按钮。

**Do / Don't**：
- Do 每个元素 4px 黑描边+硬投影；三原色直接用；卡片不同底色撞色；微旋转 1-3°
- Don't 任何圆角；box-shadow blur；渐变或柔和色；细字体

**Agent 提示词**：
> 所有元素必须有 4px 纯黑描边和硬投影（8px 8px 0 #000，零模糊）。零圆角。背景纯白。标题 Archivo Black 全大写。强调色只用红 #E63946、黄 #FFD93D、蓝 #2563EB。卡片不同底色撞色。禁止渐变、柔和阴影、细字体。元素可微旋转 1-3 度。

---

## 09 · Neon（合成波霓虹）

> HTML 文件：`12-neon.html`

```yaml
color:
  background_gradient: "linear-gradient(180deg, #1A0533 0%, #0D0221 60%, #05010F 100%)"
  foreground: "#FFFFFF"
  pink: "#FF2E97"
  cyan: "#00F0FF"
  purple: "#B026FF"
typography:
  heading: "Orbitron 700-900"
  body: "JetBrains Mono 400, uppercase, letter-spacing 0.15-0.4em"
radius:
  base: "0px"
shadow:
  glow_pink: "0 0 10px #FF2E97, 0 0 20px #FF2E97, 0 0 40px rgba(255,46,151,0.5)"
  glow_cyan: "0 0 10px #00F0FF, 0 0 20px #00F0FF, 0 0 40px rgba(0,240,255,0.5)"
border:
  card: "1px solid rgba(255,46,151,0.4)"
```

**气质**：深紫黑夜幕下霓虹粉和电光青发光，透视网格延伸向 1984 年的未来。电子、迷幻、怀旧又前卫。

**色彩**：深紫到黑垂直渐变底；霓虹粉 `#FF2E97` 和电光青 `#00F0FF` 是仅有的两个强调色；所有发光文字必须有 text-shadow 辉光（至少两层 10px+20px）。禁止暖色、柔和色、纯白背景、无发光的彩色文字。

**字体**：标题 Orbitron 700-900；正文/标签 JetBrains Mono 等宽大写；标题可用粉到青渐变文字+drop-shadow 发光；标签前可加 `//` 或 `[ ]` 终端符号。

**版式**：每页底部 perspective 透视网格地板（粉色水平+青色垂直半透明线条）；封面右上角条纹太阳（粉橙渐变圆+水平条纹切割+大范围辉光）；白色星点（2px+box-shadow 发光）；半透明深紫底卡片+1px 霓虹描边+发光阴影，零圆角；数据页奇数粉色偶数青色发光数字。

**组件**：`perspective(400px) rotateX(60deg)` 网格地板；180px 条纹太阳（repeating-linear-gradient 切割）；`rgba(26,5,51,0.6)`+blur(8px)+霓虹描边卡片；发光文字 text-shadow 三层。

**Do / Don't**：
- Do 所有霓虹色文字带 text-shadow 辉光；每页透视网格；等宽字体标签
- Don't 圆角；柔和色或暖色；霓虹色脱离深色背景

**Agent 提示词**：
> 背景深紫到黑渐变。霓虹粉 #FF2E97 和电光青 #00F0FF 是仅有的强调色，所有彩色文字必须带 text-shadow 辉光（至少 0 0 10px 和 0 0 20px 两层）。标题 Orbitron 700-900，正文标签 JetBrains Mono 等宽大写。每页底部加 perspective 透视网格。卡片半透明深紫底+1px 霓虹描边+发光阴影，零圆角。封面加条纹太阳和星点。

---

## 10 · Pop!（波普艺术）

> HTML 文件：`13-pop.html`

```yaml
color:
  background: "#FFE500"
  foreground: "#000000"
  red: "#E63946"
  blue: "#1D4E89"
  white: "#FFFFFF"
typography:
  heading: "Anton, uppercase, display 150px"
  body: "Inter 700-900"
radius:
  base: "0px"
  bubble: "24px"
shadow:
  bubble: "8px 8px 0 #E63946"
border:
  width: "4px solid #000"
```

**气质**：亮黄色底、红色半调网点、粗黑描边、爆炸星形气泡。像 Lichtenstein 的画——热闹、夸张、快乐。

**色彩**：亮黄 `#FFE500` 是主色调（不是强调色）；纯黑描边；红 `#E63946` 用于半调网点、爆炸星、卡片底；蓝 `#1D4E89` 用于几何形状、卡片底。禁止渐变、柔和色、灰色、低饱和。

**字体**：标题 Anton 压缩粗体全大写（封面 150px）；空心字：白色填充+3-4px 黑色 `-webkit-text-stroke`；正文 Inter 700-900。

**版式**：四角红色 Ben-Day 半调网点（`radial-gradient(circle, red 2px, transparent 2.5px)` 16px 间距+mask 渐变淡出）；所有形状 4px 黑描边；金句白色对话气泡（24px 圆角+4px 黑描边+红色硬投影+尖角，微旋转 -1.5°）；爆炸星用 clip-path 10 角星红底白字；三栏卡片白/蓝/红底色；四栏数据白/蓝/黄/黑轮换。

**组件**：半调网点 radial-gradient+mask 淡出；对话气泡（圆角+黑描边+红色硬投影+::after 尖角）；clip-path 爆炸星多边形；`-webkit-text-stroke` 描边字；蓝底白字+4px 描边+6px 硬投影按钮。

**Do / Don't**：
- Do 大面积亮黄底；四角半调网点；爆炸星和对话气泡
- Don't 渐变或柔和阴影；细字体；黄色只做小面积点缀

**Agent 提示词**：
> 背景亮黄色 #FFE500。所有形状 4px 纯黑描边。标题 Anton 全大写，可用白色填充+黑色 stroke 空心字。四角加红色 Ben-Day 半调网点（radial-gradient 圆点+mask 淡出）。金句用白色对话气泡（圆角+黑描边+红色硬投影+尖角）。强调色红 #E63946 和蓝 #1D4E89。爆炸星用 clip-path 多边形。禁止渐变和柔和色。

---

## 11 · Electric（大胆渐变）

> HTML 文件：`14-electric.html`

```yaml
color:
  background_gradient: "linear-gradient(135deg, #FF6B35 0%, #FF3D7F 40%, #7B2FF7 100%)"
  foreground: "#FFFFFF"
  orange: "#FF6B35"
  pink: "#FF3D7F"
  purple: "#7B2FF7"
typography:
  heading: "Sora 800-900, uppercase, letter-spacing -0.025em to -0.04em, display 130px"
  body: "Sora 400"
radius:
  base: "20px"
  pill: "100px"
glass:
  background: "rgba(255,255,255,0.12)"
  backdrop_filter: "blur(16px)"
  border: "1px solid rgba(255,255,255,0.2)"
```

**气质**：橙→粉→紫高饱和 mesh 渐变铺满画面，白色超粗字+磨砂玻璃卡片。色彩激烈但排版干净，像音乐节海报有能量但不失秩序。

**色彩**：135deg 三色渐变铺满全页；纯白文字；辅助文字 `rgba(255,255,255,0.7)`；背景层 2-3 个 blur(60px) 大尺寸半透明彩色圆形增强 mesh 感。禁止纯色背景、深色文字、低饱和。

**字体**：全程 Sora，标题 800-900 全大写紧字距（封面 130px 超粗压住强烈背景），正文 400。

**版式**：背景层 mesh blobs（300-500px blur(60px) 半透明橙/紫/粉，z-index:0）；内容卡片磨砂玻璃（rgba(255,255,255,0.12)+blur(16px)+1px 白描边+20px 圆角）；双栏一玻璃卡一纯白实色卡（紫字）；金句关键词白色半透明高亮块；四栏玻璃卡片白色大数字；白底紫字 100px 胶囊按钮+柔投影。

**组件**：blur(60px) mesh blob；磨砂玻璃卡片 20px 圆角；半透明白底胶囊标签+白色发光小圆点；纯白底深紫字 featured 卡。

**Do / Don't**：
- Do 背景必须是橙→粉→紫高饱和渐变；blur(60px) mesh blob；磨砂玻璃卡片 20px 圆角
- Don't 渐变背景上用深色文字；硬边描边或零圆角；降低渐变饱和度

**Agent 提示词**：
> 背景必须是 linear-gradient(135deg, #FF6B35, #FF3D7F, #7B2FF7) 高饱和渐变。加 2-3 个 blur(60px) 半透明大圆形做 mesh。所有文字白色，标题 Sora 800-900 全大写紧字距。卡片磨砂玻璃 rgba(255,255,255,0.12)+blur(16px)+20px 圆角+白色半透明描边。双栏中一张可用纯白底紫字。禁止深色文字和纯色背景。

---

## 12 · Memphis（孟菲斯后现代）

> HTML 文件：`15-memphis.html`

```yaml
color:
  background: "#F5F0E8"
  foreground: "#000000"
  pink: "#FF6B9D"
  cyan: "#00C9C9"
  yellow: "#FFD93D"
  red: "#FF4757"
typography:
  heading: "Archivo Black, uppercase, display 120px"
  body: "Inter 600-800"
radius:
  base: "0px"
shadow:
  card_pink: "12px 12px 0 #FF6B9D"
border:
  width: "3-4px solid #000"
```

**气质**：奶油底上散落亮粉青黄几何图形，黑色波浪线和棋盘格穿插。1980 年代米兰的反叛精神——playful、喧闹、拒绝严肃。

**色彩**：暖奶油 `#F5F0E8`（不是纯白）；纯黑描边；亮粉 `#FF6B9D` 主强调；青 `#00C9C9`；黄 `#FFD93D`；红 `#FF4757` 小点缀。禁止渐变、柔和色、灰色调、纯白背景。

**字体**：标题 Archivo Black 全大写（封面 120px）；可用 `-webkit-text-stroke: 3px #000` 空心字（青色填充）；正文 Inter 600-800；标签可微旋转 ±1-2°。

**版式**：散落几何装饰（圆形/三角形/旋转方块，都带 3-4px 黑描边）；黑色 SVG 波浪线 squiggles（3px Q 贝塞尔 round linecap）；20px 黑白棋盘格（conic-gradient）+4px 黑描边框；装饰微旋转、不对称排列；卡片 4px 黑描边零圆角，底色轮换粉/青/黄；金句白卡+4px 描边+12px 粉色硬投影+微旋转 -1°；双栏白底黑底反转。

**组件**：SVG 波浪线 `<path d="M0 10 Q10 0 20 10 T40 10...">`；conic-gradient 棋盘格；border-radius:50%+描边彩色圆；CSS border 三角形+drop-shadow；rotate(15deg) 方块。

**Do / Don't**：
- Do 每页至少 3-5 个几何装饰；黑色波浪线和棋盘格；微旋转打破对称
- Don't 渐变或柔和阴影；装饰排成直线或对称；纯白背景

**Agent 提示词**：
> 背景奶油色 #F5F0E8。每页散落亮粉/青/黄几何形状（圆形、三角形、旋转方块，都带 3-4px 黑描边）和黑色 SVG 波浪线。可加黑白棋盘格方块。标题 Archivo Black 全大写。卡片 4px 黑描边零圆角，底色轮换粉/青/黄。金句白卡+粉色硬投影+微旋转。禁止渐变、柔和阴影、纯白背景。

---

## 13 · Punk（瑞士朋克）

> HTML 文件：`16-punk.html`

```yaml
color:
  background: "#FFFFFF"
  foreground: "#000000"
  red: "#E63946"
  muted: "#666666"
typography:
  heading: "Inter Black 900, uppercase, letter-spacing -0.04em to -0.05em, display 180px"
  mono: "JetBrains Mono 700, uppercase, letter-spacing 0.2-0.3em"
  body: "Inter 500-900"
radius:
  base: "0px"
shadow:
  none: true
border:
  width: "3px solid #000"
```

**气质**：只用黑白红三色，通过旋转、遮挡、重叠和破碎网格制造紧张感。1977 年朋克海报——激进、raw、充满对抗性。字体越粗越好，网格就是用来打破的。

**色彩**：纯白底+纯黑字；红色 `#E63946` 是唯一强调色，以几何块面出现（竖条、横带、整格），不是小面积点缀。禁止其他颜色、渐变、灰色装饰、圆角。

**字体**：标题 Inter Black 900 全大写极紧字距（封面 180px）；`-webkit-text-stroke: 4px #000; color: transparent` 空心大字；标签/编号 JetBrains Mono 700 大写+0.2-0.3em；正文 Inter 500-900；竖排文字 `writing-mode: vertical-rl`。

**版式**：红色色带/色块切割画面（顶部横条、侧边竖条、贯穿中部横带）；红色色块旋转 ±15° 部分遮挡标题；红色竖条上白色竖排文字；内容故意错位不对齐，列表用 3px 黑线分隔而非卡片；金句红色横带贯穿中部+白色大字 `mix-blend-mode: difference` 反色；数据四栏 3px 黑线分隔，隔栏红底/黑底白字。

**组件**：绝对定位红色矩形（可旋转 15° 斜切）；竖排标签 writing-mode: vertical-rl；4px 描边空心字；3px 黑线分隔的无卡片列表；mix-blend-mode:difference 反色金句。

**Do / Don't**：
- Do 红色几何块面切割画面；元素旋转遮挡重叠；竖排文字和等宽编号
- Don't 第四种颜色；圆角/渐变/阴影；所有元素整齐对齐——错位是核心

**Agent 提示词**：
> 只用黑白红三色（红 #E63946）。标题 Inter Black 900 全大写极紧字距，封面 180px。用红色色带/色块切割画面，元素可旋转 15 度、互相遮挡。竖排文字 writing-mode: vertical-rl。列表用 3px 黑线分隔，不用卡片。金句红色横带+mix-blend-mode:difference 反色。禁止圆角、渐变、阴影、第四色。网格要被打破。

---

## 14 · Tropic（热带热力）

> HTML 文件：`17-tropic.html`

```yaml
color:
  background: "#0A3D3D"
  foreground: "#FFFFFF"
  coral: "#FF6B47"
  yellow: "#FFD23F"
  teal_light: "#14A098"
  muted: "rgba(255,255,255,0.7)"
typography:
  heading: "Fredoka 700, letter-spacing -0.02em, display 130px"
  body: "Inter 500-600"
radius:
  base: "24px"
  pill: "100px"
  lg: "28px"
shadow:
  sun_glow: "0 0 100px rgba(255,210,63,0.3)"
```

**气质**：深青丛林夜幕下，珊瑚橙和亮黄像日落燃烧。圆润饱满字体、大圆角卡片、热带叶子剪影——热烈、能量充沛、夏日感。

**色彩**：深青 `#0A3D3D`（带绿调深色，不是黑色）；纯白文字；珊瑚橙 `#FF6B47` 主强调；亮黄 `#FFD23F` 次强调；浅青 `#14A098` 第三色。禁止冷色蓝紫、灰色调、浅色背景。

**字体**：标题 Fredoka 圆润 700（字距 -0.02em）；标题字母 "O" 可用珊瑚橙圆形替代（inline-block 0.9em 圆形）；正文 Inter 500-600。

**版式**：封面右侧 380px 亮黄太阳（100px 黄色辉光）+珊瑚/黄热带叶子 SVG 剪影（可旋转 20° 叠加）；卡片 24px 大圆角无描边，底色轮换珊瑚/黄/半透明白；双栏一半透明玻璃一亮黄实色（深青字）；金句大珊瑚色半透明圆+白色圆润大字+黄色强调；四栏大圆角卡片四色轮换；珊瑚橙底 100px 胶囊按钮。

**组件**：300-380px 黄色太阳+box-shadow 辉光；SVG 龟背竹/棕榈叶剪影（珊瑚/黄填充，深青花脉）；24px 圆角无描边卡片；半透明白胶囊标签+黄圆点；标题字母 O 珊瑚橙圆形替代。

**Do / Don't**：
- Do 深青底是基础，珊瑚和黄是火焰；大圆角 24px+；太阳和热带叶子
- Don't 零圆角或尖锐形状；冷色蓝紫；浅色背景

**Agent 提示词**：
> 背景深青色 #0A3D3D。强调色珊瑚橙 #FF6B47 和亮黄 #FFD23F。标题 Fredoka 700 圆润字体，字母 O 可用珊瑚橙圆形替代。卡片 24px 大圆角无描边，底色轮换珊瑚/黄/半透明白。封面加 380px 黄色太阳（带辉光）和 SVG 热带叶子剪影。按钮 100px 胶囊。禁止冷色、零圆角、浅色背景。

---
---

# 第三批 · 绘画风格（中西方）

---

## 15 · Mineral Strata（青绿矿物层叠）

> HTML 文件：`21-mineral-strata.html`

```yaml
color:
  background: "#F5F0E6"
  foreground: "#1A2A3A"
  azurite: "#2E5A88"
  malachite: "#4A8B6F"
  gold: "#C4A35A"
typography:
  heading: "Noto Serif SC 900, letter-spacing 0.05-0.08em"
  body: "Noto Serif SC 400, line-height 1.8"
  en: "Cormorant Garamond 600, uppercase, letter-spacing 0.2-0.35em, gold"
```

**气质**：青绿山水的抽象转译。石青、石绿水平色带模拟远山层叠，泥金细线勾勒分界，极简几何三角形指代山峰。矿物色沉稳华贵+现代主义几何克制，像展开手卷但没有一笔在"画山水"。

**色彩**：暖绢白 `#F5F0E6`；石青 `#2E5A88`（上色带、主标题）；石绿 `#4A8B6F`（下色带托底）；泥金 `#C4A35A` 只做线不做面。禁止渐变、高饱和、冷灰、大面积金色块。

**版式**：页面被石青（上）、绢白（中）、石绿（下）三条水平带分割，泥金 1px 细线分隔；底部 2-3 个极简 SVG 三角形山形（石青/石绿填充+泥金 1.5px 描边，无皴法）；泥金细线同心圆作为"日/月"抽象符号低透明度；卡片半透明白底+2px 泥金 border-top，零圆角；页脚在石绿色带内。

**Do / Don't**：
- Do 水平色带组织版面像手卷；山形只用几何三角+金线；金色只做细线
- Don't 画真实山水云雾树木；圆角/渐变/阴影；石青和石绿直接相邻（中间必须绢白留白）

**Agent 提示词**：
> 背景暖绢白 #F5F0E6。页面由石青 #2E5A88（上）和石绿 #4A8B6F（下）水平色带分割，泥金 #C4A35A 1px 细线分隔。底部放 2-3 个极简 SVG 三角形山形。中文标题 Noto Serif SC 900 大字距，英文 Cormorant Garamond 大写金色。卡片半透明白底+泥金顶部边框，零圆角。禁止画真实山水、渐变、圆角、阴影。

---

## 16 · Iron Line & Halo（敦煌铁线圆光）

> HTML 文件：`22-iron-line-halo.html`

```yaml
color:
  background: "#F0E4D0"
  foreground: "#2A1F14"
  red: "#B85C38"
  gold: "#D4A843"
  gold_bright: "#E8C868"
  gold_deep: "#9A7B1A"
typography:
  heading: "Noto Serif SC 900, letter-spacing 0.08em, red"
  body: "Noto Serif SC 400, line-height 1.8"
  en: "Cormorant Garamond 600-700, uppercase, letter-spacing 0.3-0.4em, gold"
```

**气质**：敦煌壁画的抽象转译。抽取铁线描（均匀流动曲线）和圆光（同心圆光环）两个核心语法。土红暖底+泥金线条+大地色系，有壁画沉着华丽感，无宗教人物。

**色彩**：暖米色 `#F0E4D0`（带极淡颗粒质感）；土红 `#B85C38`（主标题、铁线主脉）；泥金 `#D4A843`（亮部 `#E8C868`，深部 `#9A7B1A`）用于圆光环、装饰线、边饰，**必须有金属渐变感**；石青 `#3A6B8C` 辅助点缀。禁止高饱和冷色、纯白背景、无金色页面。

**字体**：中文标题 Noto Serif SC 900 字距 0.08em 土红色；英文 Cormorant Garamond 600-700 大写 0.3-0.4em 泥金色；金色文字和线条必须用 `linear-gradient(#E8C868→#9A7B1A)` 金属渐变，不平涂。

**版式**：每页 1-3 条 SVG 贝塞尔铁线曲线（土红低透明粗线 stroke-width 10 opacity 0.1 + 泥金渐变细线 stroke-width 3 opacity 0.55 叠加）；泥金金属渐变描边同心圆光环（2-4 层，线宽外粗内细）；上下 32px 忍冬纹边带（重复弧形+圆点，泥金色，底色极淡金色透明）；卡片半透明白底+1px 泥金描边+内嵌 0.5px 双层框；标题下方泥金渐变装饰线+菱形端点。

**Do / Don't**：
- Do 每页必须有可见泥金元素；金色用线性渐变模拟金属感；铁线土红粗线+泥金细线叠加
- Don't 画佛像飞天等宗教形象；圆角/box-shadow；金色变成土黄色（必须明暗渐变）

**Agent 提示词**：
> 背景暖米色 #F0E4D0 带极淡颗粒。每页有 SVG 贝塞尔铁线曲线（土红低透明粗线+泥金渐变细线叠加）和泥金同心圆光环（金属渐变描边 2-4 层）。上下有 32px 忍冬纹弧形圆点装饰带。中文标题 Noto Serif SC 900 土红色，英文 Cormorant Garamond 大写泥金色。金色必须用 linear-gradient(#E8C868→#9A7B1A)。卡片半透明白底+双层泥金描边。禁止画宗教人物、圆角、阴影。

---

## 17 · Cobalt Circles（青花钴蓝同心圆）

> HTML 文件：`23-cobalt-circles.html`

```yaml
color:
  background: "#FFFFFF"
  foreground: "#1A2A3A"
  cobalt: "#1B4B8A"
  cobalt_2: "#4A7FB5"
  cobalt_3: "#8AB0D5"
  cobalt_4: "#C5D9EC"
  cobalt_5: "#E8F0F8"
typography:
  heading: "Noto Serif SC 900, letter-spacing 0.05-0.08em, cobalt"
  body: "Noto Serif SC 400, line-height 1.8"
  en: "Josefin Sans 600, uppercase, letter-spacing 0.25-0.4em, cobalt-2"
```

**气质**：青花瓷的抽象转译。抽取同心圆构图（瓷盘圆形格式）和分水色阶（钴蓝浓淡渐变）。纯白底上钴蓝圆环由浓渐淡向外扩散，底部青花海水纹边饰。单色体系靠明度变化建立层次——瑞士国际主义的骨，中国瓷器的魂。

**色彩**：纯白 `#FFFFFF`；钴蓝 `#1B4B8A`（最深"头浓"，主标题、实心圆）；钴蓝 2-4 `#4A7FB5`/`#8AB0D5`/`#C5D9EC`（分水色阶，外环、辅助线、边框）；钴蓝 5 `#E8F0F8`（最淡底色）。**只有钴蓝一个色相**，5 个明度色阶建立全部层次。禁止第二色相、渐变背景、灰色。

**字体**：中文标题 Noto Serif SC 900 字距 0.05-0.08em 钴蓝色；英文 Josefin Sans 600 大写 0.25-0.4em 钴蓝 2。

**版式**：每页 3-6 个 SVG 同心圆（由内向外颜色渐淡、线宽递减，最内一环可低透明度填充）；底部 32px 钴蓝色带+白色三层叠浪弧线（海水纹，data URI SVG，opacity 0.85/0.4/0.2）+顶部白色 1.5px 边线模拟瓷釉口沿；顶部 4px 钴蓝细线；卡片白底+1px 钴蓝 3 边框+内嵌 0.5px 钴蓝 4 双层框（弦纹）；环形图标（外环+中环+实心圆心）。

**Do / Don't**：
- Do 只用钴蓝一个色相靠 5 个明度色阶分层；每页同心圆由浓到淡；底部海水纹白色叠浪弧线
- Don't 画瓷器莲花缠枝等具象纹样；引入第二色相（包括红色印章）；圆角（圆形除外）/渐变背景/阴影

**Agent 提示词**：
> 背景纯白。只用钴蓝 #1B4B8A 一个色相，配合 #4A7FB5/#8AB0D5/#C5D9EC/#E8F0F8 四个淡色阶。每页有 SVG 同心圆，由内向外颜色渐淡、线宽递减。底部 32px 钴蓝色带配白色三层叠浪弧线（海水纹），顶部 4px 钴蓝线。中文标题 Noto Serif SC 900，英文 Josefin Sans 大写。卡片白底+双层钴蓝边框，零圆角。禁止第二色相、具象纹样、渐变背景。

---

## 18 · Nouveau（新艺术运动）

> HTML 文件：`24-nouveau.html`

```yaml
color:
  background: "#F0E6D3"
  foreground: "#2D2A22"
  green: "#2D4A3E"
  gold: "#B8944F"
  purple: "#7D5A6E"
  cream: "#FAF5EA"
typography:
  heading: "Playfair Display 700-900, letter-spacing 0.02-0.05em, green"
  body: "Cormorant Garamond 400, line-height 1.8"
  en: "Playfair Display 700, uppercase, letter-spacing 0.2em"
```

**气质**：Art Nouveau 的优雅有机感。双层金线框包裹版面，四角程式化植物角花，中央圆形纹章。深森林绿+暖金+暗紫，Playfair Display 高对比衬线体。装饰性强但不浮夸，有机曲线克制使用。

**色彩**：暖象牙 `#F0E6D3`；森林绿 `#2D4A3E`（主标题、深色文字）；暖金 `#B8944F`（所有线条、边框、角花、装饰——系统骨架）；暗紫 `#7D5A6E`（章节号、小标签点缀）；奶油白 `#FAF5EA`（卡片底）。禁止高饱和色、冷灰、无金色页面。

**字体**：英文标题 Playfair Display 700-900 高对比衬线；正文 Cormorant Garamond 400；中文用 Noto Serif SC。

**版式**：双层金线框（外层 2px 金色距边 24px+内层 0.5px 金色距边 32px）；四角金色植物角花 SVG（对称 S 形卷草+叶片）；封面/章节页金色同心圆纹章（3-4 层）；卡片奶油白+1px 金色边框；双栏金色竖线分隔；金句页深绿大字居中+上下金色装饰线。

**Do / Don't**：
- Do 每页金色边框和角花；装饰曲线有机流畅对称
- Don't 几何直线直角装饰（那是 Art Deco）；装饰压过内容；圆角/阴影/渐变

**Agent 提示词**：
> 背景暖象牙 #F0E6D3。每页有双层金色线框（2px+0.5px #B8944F）和四角金色植物角花 SVG。封面有金色同心圆纹章。标题 Playfair Display 700 深森林绿 #2D4A3E，正文 Cormorant Garamond。卡片奶油白+金色边框。暗紫 #7D5A6E 小面积点缀。装饰用有机曲线，禁止几何直角、圆角、阴影。

---

## 19 · Deco（装饰艺术）

> HTML 文件：`25-deco.html`

```yaml
color:
  background: "#0B0F1A"
  foreground: "#E8D5A3"
  gold: "#C9A961"
  gold_bright: "#E8D5A3"
  gold_dim: "rgba(201,169,97,0.3)"
typography:
  heading: "Limelight, letter-spacing 0.08-0.15em, gold-bright"
  body: "Josefin Sans 300-400, line-height 1.8"
  en: "Josefin Sans 600, uppercase, letter-spacing 0.3em"
```

**气质**：Art Deco 的几何奢华。深夜蓝底+金色线条，绝对对称。旭日放射线、Chevron 角饰、阶梯金字塔——1920 年代摩天楼与爵士时代。华丽但冷峻，对称到强迫症。

**色彩**：深夜蓝 `#0B0F1A`（近黑有蓝调）；金色 `#C9A961`（所有线条、边框、装饰、标题——绝对主角）；亮金 `#E8D5A3`（标题文字、高亮、放射线）；暗金 `rgba(201,169,97,0.3)`（辅助线、背景装饰）。**只有深蓝底+金色**，层次靠金色透明度。禁止任何彩色色相、白色背景、无金色页面。

**字体**：标题 Limelight（Art Deco 标志性字体）字距 0.08-0.15em 亮金色；正文/标签 Josefin Sans 300-400 几何无衬线大写+0.3em 字距；中文 Noto Serif SC 900。

**版式**：绝对对称（所有元素沿垂直中轴线对称或左右镜像）；旭日放射线（从中心发散 20-40 条金色射线，JS 动态生成，透明度递减）；四角 Chevron V 形角饰（多层嵌套）；底部/顶部 3-5 层递减阶梯金字塔；双层框（2px 金色+0.5px 金色 inset 10px）；卡片深蓝 `#141B2E`+1px 金色边框；数据四栏金色竖线分隔+Limelight 大数字。

**Do / Don't**：
- Do 每页绝对对称；金色是唯一装饰色靠透明度和线宽变化；放射线/Chevron/阶梯三大母题
- Don't 有机曲线（那是 Art Nouveau）；圆角/阴影/彩色；打破对称

**Agent 提示词**：
> 背景深夜蓝 #0B0F1A。所有装饰和文字用金色 #C9A961/#E8D5A3，靠透明度分层。每页绝对对称。封面有 JS 生成的旭日放射线（20-40 条金色射线），四角 Chevron 角饰，底部阶梯金字塔。标题 Limelight 亮金色，正文 Josefin Sans 大写。卡片深蓝底+金色边框。禁止有机曲线、圆角、彩色、阴影。

---

## 20 · Ukiyo-e（浮世绘）

> HTML 文件：`26-ukiyo-e.html`

```yaml
color:
  background: "#F2EAD8"
  foreground: "#1A1A1A"
  indigo: "#1B3A6B"
  indigo_light: "#2C5F8A"
  red: "#C8362C"
typography:
  heading: "Shippori Mincho 700-800, letter-spacing 0.05-0.1em, indigo"
  body: "Noto Serif SC 400, line-height 1.8"
  en: "Shippori Mincho 600, uppercase, letter-spacing 0.2em"
```

**气质**：浮世绘木版画的平面装饰感。和纸暖米底+靛蓝主色+朱红印章色。富士山极简三角形+雪顶白线，波浪重复弧形线带，朱红印章落款。平面化、无透视、轮廓线清晰——北斋漫画的构图逻辑。

**色彩**：和纸米 `#F2EAD8`；靛蓝 `#1B3A6B`（主标题、山形、波浪、边框——木版画的"蓝"）；浅靛 `#2C5F8A`（辅助线、波浪第二层）；朱红 `#C8362C`（印章、小面积强调——全页只出现 1-2 处，只做印章大小不做大色块）。禁止渐变、高饱和多色、无靛蓝页面。

**字体**：标题 Shippori Mincho 700-800（日本明朝体雕版感）靛蓝色；正文 Noto Serif SC 400；印章内白色小号汉字。

**版式**：木刻双线框（外层 2px 靛蓝距边 20px+内层 0.5px 靛蓝距边 28px）；封面/章节页极简 SVG 三角形富士山（靛蓝填充+顶部白色雪顶折线）；底部/侧边 2-3 层重复弧形波浪线青海波（靛蓝/浅靛）；每页朱红方形印章（28-40px，内白色汉字）；卡片和纸底+1px 靛蓝边框；数据四栏 Shippori Mincho 大数字+浅靛波浪线装饰。

**Do / Don't**：
- Do 每页靛蓝元素和木刻边框；朱红只做小面积印章；所有图形平面化轮廓清晰
- Don't 画写实富士山照片或复杂风景；朱红大面积出现；圆角/渐变/阴影/3D

**Agent 提示词**：
> 背景和纸米 #F2EAD8。主色靛蓝 #1B3A6B，朱红 #C8362C 只做小印章。每页有木刻双线框（2px+0.5px 靛蓝）。封面有极简 SVG 三角形富士山（靛蓝填充+白色雪顶线），底部 2-3 层靛蓝弧形波浪线。右下角朱红方形印章内白色汉字。标题 Shippori Mincho 明朝体靛蓝色。所有图形平面化，禁止渐变、圆角、阴影、写实风景。

---
---

# 通用技术约定

所有 20 套模板共享以下技术规范：

- **画布**：1280×720px（16:9），`transform: scale()` 自适应视口（`@media (max-aspect-ratio: 16/9)` 按宽度缩放，否则按高度）
- **导航**：← → 方向键翻页，Space 下一页，Home/End 跳首尾
- **字体**：Google Fonts CDN，`<link rel="preconnect">` 预连接
- **结构**：每套 7 个版式——封面 / 章节 / 内容（三栏）/ 双栏 / 金句 / 数据（四栏）/ 结尾
- **CSS**：`:root` CSS 变量定义全部 design token，组件类名复用
- **JS**：vanilla JS，零依赖，`keydown` 事件监听，`display: flex/none` 切换 active slide
- **文件**：单文件自包含 HTML，可直接双击打开或分享，无需构建

## 如何使用

1. 选择需要的风格编号
2. 将该章节的完整规范（或对应单独的 `.DESIGN.md` 文件）提供给 Coding Agent（Cursor / Copilot / Claude Code 等）
3. Agent 读取 YAML tokens（色彩、字体、间距、圆角、阴影、边框）和 Markdown 规范
4. 按规范生成或修改 HTML/React/任何前端代码
5. 每套末尾的「Agent 提示词」可直接作为 prompt 使用
