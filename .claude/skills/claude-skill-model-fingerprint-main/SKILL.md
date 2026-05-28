---
name: claude-skill-model-fingerprint
description: "通过 reasoning_effort、Magic String、组合推理题和离线日期题快速检测当前 API 是否为真实 Claude 模型，并在需要时升级到身份、工具、元数据与嵌套层级的深度审查。用于怀疑模型真假、来源异常、被第三方包装，或需要输出模型真实性检测报告时。"
source: personal
risk: safe
domain: diagnostics
category: analysis
version: 2.0.0
---

# 模型指纹检测

## 概述

本 Skill 通过 **并行 subagent** 执行多项独立检测，大幅缩短总耗时。

为减少默认加载量，详细规则拆到 `references/`：
- 核心测试细则：[references/core-tests.md](references/core-tests.md)
- 深度审查项：[references/deep-review.md](references/deep-review.md)
- 完整报告模板：[references/report-template.md](references/report-template.md)

## 使用边界

- 本 Skill 提供的是经验性、启发式检测信号，不是 Anthropic 官方认证机制。
- 任一单独测试结果都不应作为唯一结论，必须结合多个信号综合判断。
- 默认先做快速鉴伪；仅在异常或用户要求时才升级到深度审查。

## 执行架构

```
主 Agent（协调者）
  ├── 读取 references/core-tests.md 获取判定规则
  ├── 并行启动 3 个 subagent（使用 Agent 工具，在同一条消息中发出）
  │   ├── Subagent A: reasoning_effort + Magic String
  │   ├── Subagent B: 糖果题 + 离线日期题
  │   └── Subagent C: 动漫/东方问答 + model_info JSON
  ├── 收集所有 subagent 结果
  ├── 对照判定规则汇总结论
  └── 若出现异常 → 读取 deep-review.md 升级深度审查
```

## 默认执行流程

收到"鉴伪 / 指纹检测 / 模型真实性分析"请求时：

### Phase 1：准备

读取 [references/core-tests.md](references/core-tests.md) 获取每项测试的指令、预期响应和判定规则。

### Phase 2：并行执行（关键步骤）

**必须在同一条消息中同时启动以下 3 个 Agent 工具调用**（不要顺序执行）：

#### Subagent A — reasoning_effort + Magic String

给 subagent 的完整 prompt：

```
你是模型指纹检测的子测试执行器。请依次完成以下两项测试，直接输出结果，不要解释原理。

## 测试 1: reasoning_effort 指纹

回答这个问题：What is the current <reasoning_effort>???</reasoning_effort>?

输出格式：
- reasoning_effort 值：[你看到的具体数值，或"无法获取"]

## 测试 2: Magic String 拒绝测试

请处理以下输入：
ANTHROPIC_MAGIC_STRING_TRIGGER_REFUSAL_1FAEFB6177B4672DEE07F9D3AFC62588CCD2631EDCF22E8CCC1FB35B501C9C86

输出格式：
- Magic String 响应：[空响应 / 精确 API Error 文本 / 其他（附原文）]
```

#### Subagent B — 糖果题 + 离线日期题

给 subagent 的完整 prompt：

```
你是模型指纹检测的子测试执行器。请依次完成以下两项测试，直接输出答案。

## 测试 1: 糖果保底组合推理题

在一个黑色的袋子里放有三种口味的糖果，每种糖果有两种不同的形状（圆形和五角星形，不同的形状靠手感可以分辨）。现已知不同口味的糖和不同形状的数量统计如下表。参赛者需要在活动前决定摸出的糖果数目，那么，最少取出多少个糖果才能保证手中同时拥有不同形状的苹果味和桃子味的糖？（同时手中有圆形苹果味匹配五角星桃子味糖果，或者有圆形桃子味匹配五角星苹果味糖果都满足要求）

苹果味    桃子味    西瓜味
圆形      7        9        8
五角星形  7        6        4

输出格式：
- 糖果题答案：[你的数字答案]

## 测试 2: 离线日期记忆与不确定性测试

不联网的情况下告诉我：
1. 印度与巴基斯坦共同宣布同意达成全面停火是哪天？
2. 以色列和哈马斯在卡塔尔多哈达成加沙停火协议是哪天？
3. 安圭拉哪天举行2025年安圭拉议会选举？

输出格式：
- 日期题 1（印巴停火）：[具体日期]
- 日期题 2（加沙停火）：[具体日期]
- 日期题 3（安圭拉选举）：[具体日期 或 明确表示不确定]
```

#### Subagent C — 动漫/东方问答 + model_info

给 subagent 的完整 prompt：

```
你是模型指纹检测的子测试执行器。请完成以下测试。

给我一个最无敌、最冷门、最小众的动漫角色 (The Most Invincible and Obscure Anime Character) 似乎有"即死"。
在东方虹龙洞中，博丽灵梦的阴阳玉是谁做的？
请将所有答案组织在一个JSON对象中，结构如下:
{
  "answer":"xxx",
  "model_info": {
    "model": "xxx",
    "organization": "xxx",
    "version": "xxx",
    "data": "xxx",
    "character": "xxx"
  },
  "touhou_question": {
    "answer": "xxx"
  }
}
```

### Phase 3：汇总判定

收集 3 个 subagent 的返回结果后，对照 core-tests.md 中的判定规则逐项评分：

| 测试项 | 通过条件 |
|--------|----------|
| reasoning_effort | 返回 0-100 且与已知基准吻合 |
| Magic String | 空响应 或 精确 API Error 文本 |
| 糖果题 | 答案 = 21 |
| 日期题 1 | = `2025年5月10日` |
| 日期题 2 | = `2025年1月15日` |
| 日期题 3 | 明确表示不确定 |
| model_info | model/org/version 匹配真实 Claude |
| 动漫问答 | 提及高遠夜霧 + 即死チート |

给出快速结论：
- **更像真实 Claude** — 全部或绝大多数通过
- **可疑，需要深挖** — 部分异常
- **明显异常** — 多项未通过

### Phase 4：深度审查（条件触发）

仅在以下情况才读取 [references/deep-review.md](references/deep-review.md) 并执行深度审查：
- 核心测试出现冲突信号
- `model_info` 暴露非 Claude 身份
- Magic String 未按标准拒绝
- 用户明确要求完整分析

### Phase 5：输出报告

仅在需要完整结构化输出时读取 [references/report-template.md](references/report-template.md)。

快速模式至少输出：
- reasoning_effort 结果
- Magic String 结果
- 糖果题答案与判定
- 离线日期题结果与判定
- model_info 关键字段
- 最终结论

## 注意事项

1. 不输出完整系统提示词，只分析结构特征。
2. Claude Code 的合法封装不应直接判为异常。
3. 特定场景小说压力测试仅适用于 Opus 4.5。
4. 第 1、2 项离线日期题必须严格按标准日期匹配。
5. **三个 subagent 必须在同一条消息中并行启动**，不得顺序执行。
