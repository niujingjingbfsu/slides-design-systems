# Slides Design Systems

> 20 套精心设计的 HTML 演示文稿模板，每套都是一套完整的设计系统——从色彩、字体到装饰语法全部锁定。
> 零依赖、单文件、浏览器直接打开，也可作为 Claude Code / Cursor / Codex 等 AI 编程助手的 Skill 使用。

## 为什么做这个项目

大多数 AI 生成的幻灯片都长一个样：紫渐变、Inter 字体、圆角卡片。这个项目提供 20 套**有明确审美主张**的设计系统，AI 照抄 token 就能生成视觉一致的幻灯片，不再"自由发挥"。

## 特性

- **零依赖** — 每个模板是单个 HTML 文件，内联 CSS/JS，无需 npm 或构建工具
- **20 套设计系统** — 涵盖冷静克制、轻盈、高端留白、色彩鲜明、绘画风格五大方向
- **DESIGN.md 规范** — 每套模板附带 YAML design tokens + 设计规则 + Do/Don't + Agent 提示词
- **16:9 固定画布** — 1280×720 设计尺寸，`transform: scale()` 自适应任何屏幕
- **键盘导航** — ← → 方向键、Space、Home/End
- **7 个标准版式** — 封面、章节、三栏内容、双栏、金句、四栏数据、结尾
- **Google Fonts** — 每套精选独特字体，拒绝 Arial/Inter 通用脸

## 风格画廊

### 冷静克制 / 轻盈 / 高端留白

| 01 Systems | 02 静 Sei | 03 Soft Space | 04 Light as Air |
|:---:|:---:|:---:|:---:|
| ![Systems](templates/01-systems/preview.png) | ![Sei](templates/02-sei/preview.png) | ![Soft Space](templates/03-soft-space/preview.png) | ![Light as Air](templates/04-light-as-air/preview.png) |
| 蓝图技术感 | 日式禅意 | 温暖柔和 | 通透梦幻 |

| 05 Breathe | 06 ESSENTIAL | 07 Noir |
|:---:|:---:|:---:|
| ![Breathe](templates/05-breathe/preview.png) | ![ESSENTIAL](templates/06-essential/preview.png) | ![Noir](templates/07-noir/preview.png) |
| 清新自然 | 画廊极简 | 暗夜奢雅 |

### 色彩鲜明 / 风格化强烈

| 08 Brutal | 09 Neon | 10 Pop! | 11 Electric |
|:---:|:---:|:---:|:---:|
| ![Brutal](templates/08-brutal/preview.png) | ![Neon](templates/09-neon/preview.png) | ![Pop](templates/10-pop/preview.png) | ![Electric](templates/11-electric/preview.png) |
| 新粗野主义 | 合成波霓虹 | 波普艺术 | 大胆渐变 |

| 12 Memphis | 13 Punk | 14 Tropic |
|:---:|:---:|:---:|
| ![Memphis](templates/12-memphis/preview.png) | ![Punk](templates/13-punk/preview.png) | ![Tropic](templates/14-tropic/preview.png) |
| 孟菲斯后现代 | 瑞士朋克 | 热带热力 |

### 绘画风格（中西方）

| 15 Mineral Strata | 16 Iron Line & Halo | 17 Cobalt Circles |
|:---:|:---:|:---:|
| ![Mineral Strata](templates/15-mineral-strata/preview.png) | ![Iron Line & Halo](templates/16-iron-line-halo/preview.png) | ![Cobalt Circles](templates/17-cobalt-circles/preview.png) |
| 青绿矿物层叠 | 敦煌铁线圆光 | 青花钴蓝同心圆 |

| 18 Nouveau | 19 Deco | 20 Ukiyo-e |
|:---:|:---:|:---:|
| ![Nouveau](templates/18-nouveau/preview.png) | ![Deco](templates/19-deco/preview.png) | ![Ukiyo-e](templates/20-ukiyo-e/preview.png) |
| 新艺术运动 | 装饰艺术 | 浮世绘 |

## 快速开始

### 直接使用

1. 浏览上方画廊，选一套喜欢的风格
2. 打开对应目录的 `example.html`，浏览器直接预览
3. 复制该文件，替换内容即可

### 作为 AI Skill 使用

将本项目放入你的 Skill 目录（如 `.claude/skills/slides-design-systems/`），然后对 AI 说：

> "帮我做一份关于 [主题] 的 slides，用 Noir 风格"

AI 会读取 `SKILL.md`，按照工作流：先确认需求 → 生成风格预览 → 选定后读取对应 `DESIGN.md` → 生成完整幻灯片。

也可以让 AI 推荐风格：

> "我要做一个 15 页的产品发布演讲，帮我选 3 个风格看看"

### 手动指定设计系统

每套模板的 `DESIGN.md` 末尾都有一段「Agent 提示词」，可以直接复制给 AI：

```
请读取 templates/07-noir/DESIGN.md，按照规范生成一份关于 [主题] 的 HTML 幻灯片。
```

## 项目结构

```
slides-design-systems/
├── SKILL.md                    # AI Skill 入口（工作流、规则、模板索引）
├── DESIGN_SYSTEMS.md           # 20 套设计规范合辑（一份文件看全部）
├── README.md
├── LICENSE
└── templates/
    ├── index.json              # 20 套模板的结构化元数据
    ├── 01-systems/
    │   ├── example.html        # 可运行的演示模板（7 个版式）
    │   ├── DESIGN.md           # 设计规范（YAML tokens + 规则 + Agent 提示词）
    │   └── preview.png         # 封面截图
    ├── 02-sei/
    └── ... (共 20 套)
```

## DESIGN.md 是什么

每套模板目录下的 `DESIGN.md` 是一份给 AI 编程助手读的视觉规范文件，包含：

- **YAML front matter** — 机器可读的 design tokens（色彩、字体、间距、圆角、阴影、边框）
- **设计理念** — 这套风格的气质和主张
- **色彩/字体/版式/组件规则** — 具体怎么用、怎么不用
- **Do / Don't** — 明确的允许和禁止
- **Agent 提示词** — 可直接复制给 AI 的指令

AI 读取后会严格遵守这些 token，不会自行发明颜色或字体。

## 技术规格

| 项目 | 规格 |
|------|------|
| 画布尺寸 | 1280×720（16:9） |
| 自适应 | `transform: scale()` 整体缩放，内容不重排 |
| 字体 | Google Fonts CDN |
| 依赖 | 无（纯 HTML + CSS + vanilla JS） |
| 导航 | ← → / Space / Home / End |
| 版式 | 每套 7 页：封面/章节/三栏/双栏/金句/四栏数据/结尾 |
| 浏览器 | Chrome / Edge / Safari / Firefox 现代版本 |

## 自定义

- **改颜色**：编辑 HTML 中 `:root` 的 CSS 变量
- **改字体**：替换 `<head>` 中的 Google Fonts 链接和 `--font-*` 变量
- **加页面**：复制一个 `.slide` section，修改内容即可
- **改内容**：直接编辑 HTML 中的文字

## License

MIT — 可自由使用、修改、分发，商用无妨。
