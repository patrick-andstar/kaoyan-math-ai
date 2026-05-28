# Prompt Templates

Adapt these templates to the user's project and target tool.

All examples below assume the formal project context lives under:

```text
context/
├─ current/
└─ snapshots/
```

Prefer using the files in `context/current/` as the primary handoff source.

---

## 1. Universal handoff prompt

Use when sending context to another AI.

```md
你现在要接手一个已有项目。请不要先泛泛总结，而是先基于我提供的上下文判断：

1. 当前项目处于什么状态
2. 已经做出的关键决策有哪些
3. 当前最优先的下一步是什么
4. 有哪些风险、未知项或不要重复做的事情
5. 如果你继续推进，应该先读取哪些文件

请以“可接续工作”为目标输出，不要只做摘要。输出时分成：
- 当前状态
- 关键决策
- 下一步
- 风险与未知项
- 建议先读文件
- 继续执行建议

下面是项目上下文：
[粘贴 context/current/README.md、01-当前状态.md、02-决策记录.md、03-执行计划.md、05-风险与问题.md、06-交接说明.md 中的相关内容]
```

---

## 2. Claude Project prompt

Use when starting or resuming a topic inside Claude Project.

```md
这是一个需要长期持续推进的主题。请把下面材料当作该 project 的核心上下文，而不是普通聊天背景。

你的任务不是复述摘要，而是：
- 快速理解项目目标与边界
- 明确当前状态与关键决策
- 避免重复已经完成的讨论
- 直接从“下一步最值得推进的点”继续

请先按以下顺序理解：
1. context/current/README.md
2. context/current/01-当前状态.md
3. context/current/02-决策记录.md
4. context/current/03-执行计划.md
5. context/current/06-交接说明.md

然后输出：
- 你对当前状态的判断
- 接下来最值得做的 1~3 件事
- 你还缺什么上下文
- 如继续本轮，请你建议的推进顺序

项目材料如下：
[粘贴内容]
```

---

## 3. Codex CLI prompt

Use when switching from discussion to execution.

```md
你现在作为执行型助手接手一个已有项目。请优先关注“从哪里继续做”，而不是重讲背景。

请基于以下上下文先完成：
1. 判断当前最应该先执行的动作
2. 标出不要重复做的事情
3. 指出需要先读取的关键文件
4. 如果存在不确定项，先列出阻塞点
5. 在没有额外信息时，采用最保守、最可继续的推进方式

请按以下格式输出：
- 当前状态
- 立即下一步
- 不要重复做的事
- 需要读取的文件
- 阻塞与风险
- 执行建议

默认先读：
- context/current/06-交接说明.md
- context/current/01-当前状态.md
- context/current/03-执行计划.md
- context/current/02-决策记录.md
- context/current/05-风险与问题.md

上下文如下：
[粘贴相关内容]
```

---

## 4. Claudian / Obsidian prompt

Use when the goal is to maintain markdown files in a vault.

```md
你现在在 Obsidian 项目仓中协助维护项目上下文。目标是把聊天中的有效上下文沉淀成可持续维护的 markdown 文件，而不是保留聊天本身。

该项目的正式上下文目录为：
- context/current/
- context/snapshots/

请先判断这次更新属于哪一类：
- 轻记录更新
- 状态更新
- 决策更新
- 交接更新

然后告诉我：
1. 应该更新 context/current/ 下的哪些文件
2. 每个文件建议新增或修改什么
3. 给出可直接粘贴的 markdown 内容
4. 如果属于重要更新，是否应先创建 context/snapshots/YYYY-MM-DD-HHMM/
5. 如果适合，补一个新的 context/current/06-交接说明.md

要求：
- 不要把所有信息塞进一个总结
- 按文件职责分配内容
- 默认增量更新，不随意整篇重写
- 目标是让未来的我或另一个 AI 看完后能继续工作

当前上下文如下：
[粘贴内容]
```

---

## 5. Conversation-to-context prompt

Use when converting a raw chat into formal context updates.

```md
请把下面这段对话转化为“正式项目上下文更新”，不要只输出摘要。

项目采用如下正式上下文结构：
- context/current/README.md
- context/current/01-当前状态.md
- context/current/02-决策记录.md
- context/current/03-执行计划.md
- context/current/05-风险与问题.md
- context/current/06-交接说明.md
- context/snapshots/YYYY-MM-DD-HHMM/

请先完成：
1. 判断这次属于哪个更新级别
2. 判断需要更新 context/current/ 下的哪些文件
3. 判断是否应先创建 snapshot
4. 提炼出可直接写入文件的 markdown 内容

输出格式：
- 更新级别
- 需要更新的文件
- 是否需要 snapshot 及原因
- 各文件建议写入内容
- 一份给下一位 AI 的交接说明

对话如下：
[粘贴聊天]
```

---

## 6. Handoff-summary prompt

Use when the user asks for a “summary” but actually needs continuity.

```md
请不要只做“简短总结”。

请把下面内容整理成一份“可交接、可继续工作”的 markdown 文档，标准是：
一个没有读过这些材料的人或 AI，看完之后就能继续推进。

默认以该项目的正式上下文层为目标：
- context/current/README.md
- context/current/01-当前状态.md
- context/current/02-决策记录.md
- context/current/03-执行计划.md
- context/current/05-风险与问题.md
- context/current/06-交接说明.md

至少覆盖：
- 这个项目/主题在做什么
- 当前做到哪了
- 已确定的关键决策
- 还没解决的问题
- 下一步最应该做什么
- 有哪些容易踩坑或不要重复做的事
- 如有必要，应先读哪些文件或资料

材料如下：
[粘贴内容]
```

---

# Usage note

When using these prompts:
- replace placeholders with actual content
- prefer the smallest set of relevant files
- if the task is tool switching, always include `context/current/06-交接说明.md`
- if the task involves reasoning about why, include `context/current/02-决策记录.md`
- if the task involves execution, include `context/current/01-当前状态.md` and `context/current/03-执行计划.md`
- if a major update is about to modify several formal files, consider creating `context/snapshots/YYYY-MM-DD-HHMM/` first
