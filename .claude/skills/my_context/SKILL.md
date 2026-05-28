---
name: my_context
description: Use when the user wants to preserve, update, or hand off project context across Claude Project, Claudian, Codex CLI, or other AI tools; for generating formal context files, deciding what context documents to update, and writing handoff-quality summaries that let a new agent continue the work.
---

# My Context

This skill turns chat context into durable, reusable project context.

Use this skill when the user wants to:
- preserve context across sessions or tools
- continue work in Claude Project, Claudian, Codex CLI, or similar tools
- generate or update markdown context files
- create handoff summaries
- maintain a formal project context layer
- decide which context documents should be updated after a conversation
- produce prompts that another AI can use to continue the work

## Core standard

Do not optimize for a short summary.

Optimize for this standard:

> A person or agent who has never seen the project should be able to read the output and continue the work with minimal confusion.

The output must preserve:
- current state
- key decisions
- important constraints
- unresolved issues
- next actions
- references to relevant files or materials

## Default storage model

Unless the user specifies otherwise, store outputs inside the current project folder using this structure:

```text
context/
├─ current/
│  ├─ README.md
│  ├─ 01-当前状态.md
│  ├─ 02-决策记录.md
│  ├─ 03-执行计划.md
│  ├─ 05-风险与问题.md
│  └─ 06-交接说明.md
└─ snapshots/
   └─ YYYY-MM-DD-HHMM/
```

Interpret the “current project folder” as the folder the current conversation belongs to.

Do not default to a global handoff pool when a project-local folder is available.

## Formal context layer

Treat `context/current/` as the formal context layer.

It must remain:
- stable
- low-noise
- easy to hand off
- safe for CLI-first continuation

Treat `context/snapshots/` as the historical protection layer.

It exists to:
- preserve previous formal states
- reduce accidental loss of context quality
- support rollback and auditability
- make structural cleanups safer

## Conversation budget safeguard

If the current conversation is nearing exhaustion and the remaining message/context budget is estimated to be below 10%, automatically invoke this skill's handoff workflow even if the user did not explicitly ask for a summary.

In that situation:
1. classify the update as at least Level 4
2. generate a handoff-quality context bridge
3. prioritize `context/current/06-交接说明.md`
4. include the minimum additional updates needed for continuity, usually `context/current/01-当前状态.md` and `context/current/02-决策记录.md`
5. create a snapshot before major formal updates when possible
6. optimize for safe continuation in the next session or tool

Do not wait until context is fully exhausted if continuity would be at risk.

## Default operating model

Treat context as an external asset, not as memory inside a chat.

Preferred pattern:

1. infer what changed in the conversation
2. classify the update level
3. decide which formal files should change
4. draft only the needed markdown updates
5. create a snapshot before important formal edits when needed
6. if useful, generate a handoff prompt for another AI/tool

## First task: classify the update

Before drafting files, classify the conversation using `references/update-levels.md`.

Return:
- the update level
- why it fits
- which files should be updated

Do not recommend full-file rewrites unless the project has materially changed.

## Default formal file set

When using the project-local formal storage model, the default maintained set under `context/current/` is:

- `README.md`
- `01-当前状态.md`
- `02-决策记录.md`
- `03-执行计划.md`
- `05-风险与问题.md`
- `06-交接说明.md`

You may also generate `04-工作日志.md` or `99-资料索引.md` if the user explicitly wants them, but they are not required for every formal update.

Read `references/file-specs.md` for the role of each file and what each should contain.

## Output modes

Choose the smallest useful output.

### Mode 1: update decision only
Use when the user asks what should be updated.
Output:
- update level
- target files
- concise rationale

### Mode 2: markdown drafts or patch-ready sections
Use when the user wants content to paste into files.
Output:
- update level
- target files
- markdown sections for each file

### Mode 3: handoff package
Use when the user wants to switch tools or resume later.
Output:
- update level
- recommended reading order for the next tool
- `context/current/06-交接说明.md` draft
- optional updates for `context/current/01-当前状态.md` and `context/current/02-决策记录.md`
- tool-specific prompt using `references/prompt-templates.md`

## Writing rules

- Write in markdown.
- Be concrete.
- Prefer explicit next steps over vague advice.
- Separate facts, decisions, risks, and actions.
- Preserve uncertainty honestly.
- Do not invent progress, decisions, or evidence.
- Do not dump raw chat unless the user asks.
- Keep long-term formal files stable and low-noise.
- Distinguish confirmed facts from assumptions, proposals, and unresolved items.

## Update discipline

Default to incremental updates, not full rewrites.

Only rewrite an entire formal file when:
- the user explicitly asks for a rewrite
- the file has drifted badly and no longer serves its role
- the project structure has materially changed

Otherwise prefer:
- appending a decision entry
- replacing a small outdated section
- updating status blocks
- refining headings or section structure without changing meaning

## File-specific safety rules

### `context/current/01-当前状态.md`
- may be updated to reflect the real current state
- may replace outdated status text
- should keep the latest next action explicit

### `context/current/02-决策记录.md`
- default to append-only
- do not silently rewrite historical decisions
- if a correction is necessary, mark it as a revision or superseding decision
- preserve the reasoning trail

### `context/current/03-执行计划.md`
- may be reordered when priorities change
- explain meaningful plan changes

### `context/current/05-风险与问题.md`
- may update issue status
- resolved items should normally be marked closed or resolved, not deleted

### `context/current/06-交接说明.md`
- may be rewritten for freshness
- must always preserve: current state, immediate next action, what not to repeat, and biggest current risk or unknown

## Snapshot rules

Create a snapshot under `context/snapshots/YYYY-MM-DD-HHMM/` before important formal updates, especially when:
- the update is Level 3 or Level 4
- multiple formal files will change
- `README.md`, `01-当前状态.md`, `02-决策记录.md`, or `03-执行计划.md` will be structurally changed
- remaining conversation/context budget is estimated below 10%
- the workflow is about to switch tools or sessions

When creating a snapshot, prefer copying the current formal file set before changing it.

## Continuous improvement rule

Every formal modification should improve at least one of these qualities:
- handoff clarity
- execution readiness
- lower ambiguity
- lower duplication
- clearer separation between status, decisions, risks, and actions

If a change does not improve the formal context on at least one of these dimensions, do not make the change.

## Structural cleanup rule

If a formal file has become bloated, confusing, or internally repetitive, you may perform a structural cleanup.

When doing so:
1. create a snapshot first
2. preserve factual meaning
3. improve structure without hiding decision history
4. avoid rewriting unrelated content

## Reading order by tool

### Claude Project
Prefer:
1. `context/current/README.md`
2. `context/current/01-当前状态.md`
3. `context/current/02-决策记录.md`
4. `context/current/03-执行计划.md`
5. `context/current/06-交接说明.md`

### Codex CLI
Prefer:
1. `context/current/06-交接说明.md`
2. `context/current/01-当前状态.md`
3. `context/current/03-执行计划.md`
4. `context/current/02-决策记录.md`
5. `context/current/05-风险与问题.md`

### Claudian / Obsidian
Prefer:
1. `context/current/README.md`
2. `context/current/01-当前状态.md`
3. `context/current/06-交接说明.md`
4. read other files as needed

## When the user asks for prompts

Use `references/prompt-templates.md`.

Adapt prompts to:
- the target tool
- the current update level
- whether the user wants analysis, continuation, or execution

## When the user asks for file content

Use `references/file-specs.md`.

Draft only the sections that need change. Avoid regenerating all files unless asked.

## Good output shape

A strong response often looks like:

1. Update classification
2. Files to update
3. Markdown drafts
4. Optional handoff prompt

## Anti-patterns

Do not:
- produce a summary that omits next steps
- mix decisions into status without marking them
- bury risks inside logs
- rewrite formal files for minor changes
- treat all conversations as Level 4 handoffs
- over-document trivial chatter
- silently mutate formal context in ways that erase reasoning
- overwrite formal files when an incremental update would suffice

## Escalation principle

If the user is switching tools, pausing for later, or asks to keep context, bias toward producing a handoff-quality output.

If the conversation only adds minor progress, bias toward a smaller update.
