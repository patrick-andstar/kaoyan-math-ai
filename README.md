# kaoyan-math-ai

一个面向考研数学一复习的 Obsidian 本地知识库。它把高等数学、线性代数、概率论与数理统计的知识点、方法、题型、思维导图、PDF 原始资料、OCR 草稿、AI 整理笔记和模板工作流放在同一个仓库里，目标是减少重复抄写，把复习重心放到理解、回顾、复盘和知识连接上。

![README preview](fig/README.png)

## 项目简介

`kaoyan-math-ai` 不是单纯的资料堆放处，而是一个持续迭代的考研数学复习系统：

- 用 Markdown 保存可检索、可链接、可长期维护的数学笔记。
- 用 Obsidian 双向链接串起章节、知识点、方法和题型。
- 用思维导图作为章节入口，帮助从整体结构回到具体卡片。
- 用 AI 与 OCR 辅助处理 PDF、扫描资料和课程内容。
- 用模板统一基础知识、方法、补充知识、错题和同类题汇总的写法。

如果你想把数学复习资料从“散乱 PDF + 截图 + 手写笔记”逐步整理成一个可搜索、可回顾、可继续扩展的本地知识库，这个项目就是为这种工作流准备的。

## 适合谁使用

这个仓库比较适合：

- 正在准备考研数学一，希望系统整理高数、线代、概率论的人。
- 喜欢用 Obsidian、Markdown、双链和思维导图做长期复习的人。
- 希望用 AI/OCR 减少机械抄写，把更多时间放到理解和复盘上的人。
- 想参考一套“数学笔记 + PDF 入库 + 模板 + 插件配置”的完整 Obsidian 工作流的人。

它不太适合只想下载一套完整标准答案、直接刷题背题的人。仓库更强调“整理、连接、回顾”的过程。

## 仓库内容与目录结构

```text
.
├─ README.md
├─ AGENTS.md
├─ fig/
│  └─ README.png
├─ 数一/
│  ├─ 1 高数/
│  ├─ 2 线代/
│  └─ 3 概率论/
├─ 张宇/
│  ├─ source/
│  ├─ split/
│  └─ ai笔记/
├─ 模版文件夹/
├─ tools/
├─ tests/
├─ .obsidian/
└─ .obsidian（配置）.zip
```

主要目录说明：

- `数一/`：数学一主体笔记，包含高数、线代、概率论与数理统计。
- `张宇/source/`：原始 PDF 资料存放区。
- `张宇/split/`：按讲次拆分后的 PDF，便于按章节入库和复习。
- `张宇/ai笔记/`：AI 辅助整理后的笔记与 OCR 草稿。
- `模版文件夹/`：基础知识、方法、思维导图、错题、补充知识、同类题目汇总等模板。
- `tools/`：PaddleOCR 调用脚本和使用说明。
- `tests/`：OCR 工具相关测试。
- `fig/`：README 展示图片和公共图片资源。
- `.obsidian/`：Obsidian 仓库配置、主题、插件和 CSS snippets。

## 新手快速开始

1. 安装 [Obsidian](https://obsidian.md/) 桌面端。
2. 下载或克隆本仓库到本地。
3. 打开 Obsidian，选择“打开本地文件夹作为仓库”。
4. 选择本项目根目录，也就是包含 `README.md`、`数一/`、`.obsidian/` 的文件夹。
5. 如果 Obsidian 提示是否信任该仓库、是否启用第三方插件，请确认你理解风险后再启用。
6. 打开 `数一/1 高数`、`数一/2 线代`、`数一/3 概率论` 开始浏览。
7. 新建笔记时优先使用 `模版文件夹/` 中的模板。

如果你是第一次使用 Obsidian，建议先确认左侧文件列表能看到 `数一/`、`张宇/`、`模版文件夹/`，再开始配置插件。

## Obsidian 基础配置

当前仓库自带 `.obsidian/` 配置，主要设置如下：

| 配置项 | 当前设置 | 说明 |
| --- | --- | --- |
| 主题 | `Blue Topaz` | 仓库已包含 Blue Topaz 主题。 |
| 附件路径 | `./fig` | 粘贴图片时默认进入当前目录下的 `fig` 文件夹。 |
| 新文件位置 | 当前文件夹 | 新建笔记会放在当前所在目录，适合按章节整理。 |
| 自动更新内部链接 | 已开启 | 移动或重命名笔记时，Obsidian 会尽量更新链接。 |
| 可读行宽限制 | 已关闭 | 页面宽度更适合长公式和大图。 |
| 显示不支持文件 | 已开启 | 便于在 Obsidian 里看到 PDF、图片等资料。 |

建议开启的核心插件：

- 文件列表：浏览仓库目录。
- 全局搜索：检索公式、概念和关键词。
- 快速切换：快速跳转笔记。
- 关系图谱：查看笔记连接。
- 反向链接：查看某个知识点被哪些笔记引用。
- 出链：检查当前笔记链接到哪里。
- 标签面板：按标签组织笔记。
- Properties：管理 frontmatter 属性。
- 页面预览：悬停预览内部链接。
- 模板：插入基础模板。
- Daily Notes：记录临时复习计划或日记。
- Outline：查看当前笔记标题结构。
- Canvas：画结构图或临时推理图。
- Bases：后续可做数据库式视图。

## 模板路径配置

仓库实际模板目录是：

```text
模版文件夹
```

如果你的 Obsidian 模板插件无法找到模板，请手动检查：

1. 打开 Obsidian 设置。
2. 进入“核心插件”并确认“模板”已开启。
3. 进入“模板”设置。
4. 将模板文件夹位置设置为 `模版文件夹`。

注意：当前仓库配置文件里可能保留了旧模板路径。这里不直接修改 `.obsidian/templates.json`，所以新手第一次打开时，最好手动确认模板路径。

## 已安装插件完整清单

当前 `.obsidian/community-plugins.json` 中启用的社区插件如下：

| 插件 | 插件 ID | 版本 | 用途 |
| --- | --- | --- | --- |
| Style Settings | `obsidian-style-settings` | 1.0.9 | 配合主题调整细节样式。 |
| Templater | `templater-obsidian` | 2.20.5 | 插入和扩展模板。 |
| Callout Manager | `callout-manager` | 1.1.1 | 管理 callout 样式。 |
| Clear Unused Images | `oz-clear-unused-images` | 1.1.1 | 清理未引用图片。 |
| Dataview | `dataview` | 0.5.68 | 动态查询、汇总笔记和题型。 |
| Paste image rename | `obsidian-paste-image-rename` | 1.6.1 | 粘贴图片时重命名。 |
| Mousewheel Image zoom | `mousewheel-image-zoom` | 1.0.24 | 用鼠标滚轮缩放图片。 |
| Mindmap NextGen | `obsidian-mindmap-nextgen` | 1.16.0 | 查看和维护思维导图。 |
| Git | `obsidian-git` | 2.38.3 | 版本管理和同步。 |
| floating toc | `floating-toc` | 2.7.1 | 悬浮目录，快速定位标题。 |
| Excalidraw | `obsidian-excalidraw-plugin` | 2.23.7 | 手绘图解、结构图和草稿图。 |
| Editing Toolbar | `editing-toolbar` | 4.0.8 | 提供类似文字编辑器的工具栏。 |
| Easy Typing | `easy-typing-obsidian` | 6.0.8 | 优化中文输入和编辑体验。 |

插件目录中还包含但未在启用列表中的插件：

| 插件 | 插件 ID | 版本 | 建议 |
| --- | --- | --- | --- |
| PKMer | `pkmer` | 1.0.8 | 按需启用，适合需要 PKMer 生态功能时使用。 |
| Claudian | `realclaudian` | 2.0.18 | 按需启用，用于在 Obsidian 中接入 AI 对话工作流。 |

## 必须启用插件与用途

如果你只想让仓库的核心体验正常工作，优先确认这些插件：

- Templater：模板驱动的笔记扩写会用到它。
- Dataview：同类题、错题、标签和动态汇总依赖它。
- Style Settings：用于配合 Blue Topaz 调整界面。
- Paste image rename：粘贴截图和公式图片时更容易管理。
- Mindmap NextGen：用于思维导图类笔记的查看体验。

如果你只浏览笔记，不写新内容，Templater 和 Paste image rename 可以暂时不管；如果你要继续扩写这个仓库，建议把上面这些都装好并启用。

## 推荐和增强插件

这些插件不是打开仓库的硬性条件，但会让复习和整理更顺手：

- Excalidraw：适合画函数图像、证明思路和章节结构图。
- Floating TOC：长笔记里快速跳转标题。
- Mousewheel Image Zoom：查看截图、公式图和思维导图时更舒服。
- Clear Unused Images：长期整理后清理无引用图片。
- Obsidian Git：如果你把仓库变成 Git 仓库，可以自动提交和同步。
- Easy Typing：中文输入时减少中英文标点、空格和编辑问题。
- Editing Toolbar：给不熟 Markdown 的新手提供可视化按钮。
- Callout Manager：统一管理 `warning`、`note`、`tip` 等 callout 样式。

## 主题、CSS snippets 与界面配置

当前仓库使用：

- 主题：Blue Topaz。
- CSS snippets：
  - `dataview biaogeliekuan.css`
  - `leizhibeijing.css`
  - `page-width.css`
  - `qingsezhi.css`
  - `ruby.css`
  - `tupianjuzhong.css`
  - `yincangbiaoti.css`

如果你只想使用笔记内容，不必完全复刻作者界面。建议先保证插件可用，再按自己的阅读习惯调整主题、字体和 snippets。

## 图片与附件管理

仓库附件路径配置为：

```text
./fig
```

推荐规则：

- 每个章节或笔记目录下可以有自己的 `fig/` 文件夹。
- 粘贴图片时用 Paste image rename 顺手改成可读文件名。
- 图片引用使用 Obsidian 语法，例如 `![[fig/example.png|550]]`。
- 不要随意移动图片目录，否则已有笔记里的图片链接可能失效。
- 定期用 Clear Unused Images 检查无引用图片，但清理前建议先备份。

## 模板使用方式

`模版文件夹/` 中包含这些常用模板：

- `基础知识模板.md`：定义、公式、定理、适用条件和易错点。
- `方法模板.md`：通用解题套路、识别信号和关键步骤。
- `思维导图模板.md`：章节入口和知识结构串联。
- `错题模板.md`：题干、解法、关键一步、复盘和举一反三。
- `补充知识模板.md`：证明、图解、扩展理解。
- `同类题目汇总模版.md`：按类型动态汇总题目。
- `数学 PDF 入库工作流.md`：把数学 PDF 整理进 Obsidian 的流程说明。

建议写新笔记时先选模板，再填内容。不要直接把 OCR 原文整段贴进正式笔记，最好整理成“定义/公式/方法/例题/易错点”的结构。

## OCR 与 AI 笔记工作流

OCR 工具位于：

```text
tools/paddleocr_client.py
tools/paddleocr_README.md
```

推荐流程：

1. 原始 PDF 放在 `张宇/source/`。
2. 按章节拆分后的 PDF 放在 `张宇/split/`。
3. OCR 中间结果和版面图片放在 `张宇/ai笔记/` 或对应任务目录。
4. 用 AI 辅助把 OCR 草稿整理成可复习的 Markdown 笔记。
5. 重要公式尽量改写为 LaTeX。
6. OCR 不清、公式无法确认、图片缺失时，在笔记中标记 `待确认`。
7. 最终把稳定内容沉淀到 `数一/` 的对应章节。

使用 PaddleOCR 时，token 应通过环境变量提供，不要写进脚本、笔记或公开提交记录。

## 版权与使用说明

本仓库主要用于个人学习、复习流程整理和 Obsidian 知识库实践。原始 PDF、课程资料、题目与图片的版权归原作者、课程方或出版方所有。请勿将受版权保护的资料用于未经授权的传播或商业用途。

## 致谢

本项目基于 [patrick-andstar/Lazy-Kaoyan-Library](https://github.com/patrick-andstar/Lazy-Kaoyan-Library) 修改而来，感谢原项目提供的仓库结构、Obsidian 工作流和考研资料整理思路。

同时感谢 PaddleOCR、Obsidian 社区插件生态，以及所有愿意分享学习方法和复习经验的人。

## 写在最后

复习不只是把题刷完，也是在不断打磨一个能帮助自己想清楚问题的系统。这个仓库希望把机械整理的时间压低一点，把理解、回顾和生活本身的空间留出来一点。
