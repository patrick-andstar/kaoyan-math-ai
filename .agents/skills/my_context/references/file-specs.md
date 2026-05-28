# File Specs

These are the default formal context files under `context/current/` and what each should contain.

## `context/current/README.md`

Purpose:
- entry point for a new reader

Should contain:
- one-sentence project definition
- current phase
- recommended reading order
- last updated date
- short note on current priority

Should not contain:
- full logs
- long decision history
- duplicated details from all other files

---

## `context/current/01-当前状态.md`

Purpose:
- current state snapshot

Should contain:
- current phase
- completed items
- in-progress items
- current blockers
- latest important change
- next recommended action

Update when:
- progress changes the current working state
- priorities change
- blockages change

This is one of the most frequently updated files.

---

## `context/current/02-决策记录.md`

Purpose:
- preserve important decisions and reasons

Preferred structure for each entry:
- date
- decision
- context
- reason
- alternatives considered
- consequences

Update when:
- a meaningful choice is made
- a former approach is rejected
- a new rule or constraint is adopted

Important:
- do not mix casual thoughts with real decisions
- do not omit the reason
- default to append-only
- if correction is necessary, add a revision or superseding entry instead of erasing history

---

## `context/current/03-执行计划.md`

Purpose:
- medium-range execution plan

Should contain:
- current objectives
- prioritized task list
- dependencies
- milestones
- definition of done where useful

Update when:
- work order changes
- a new phase begins
- priorities or dependencies shift

Do not use this file as a daily log.

---

## `context/current/05-风险与问题.md`

Purpose:
- track uncertainty, blockers, and failure risks

Should contain:
- open questions
- known risks
- assumptions needing validation
- possible causes of rework
- external dependencies

Preferred structure:
- issue/risk
- impact
- status
- owner or next action if known

Update when:
- a meaningful risk appears
- uncertainty becomes important enough to preserve

Resolved items should normally be marked closed or resolved, not deleted.

---

## `context/current/06-交接说明.md`

Purpose:
- handoff file for another session, tool, or agent

Must contain:
- current state in 1–3 sentences
- files to read first
- immediate next action
- things not to repeat
- biggest current risk or unknown
- optional recommended tool behavior

This file should be the fastest way for a new agent to resume work.

Use when:
- switching tools
- pausing work
- ending a meaningful session
- asking another AI to continue

This is the most important continuity file.

---

## `context/snapshots/YYYY-MM-DD-HHMM/`

Purpose:
- preserve a recoverable copy of the formal context before important changes

Should typically contain copies of:
- `README.md`
- `01-当前状态.md`
- `02-决策记录.md`
- `03-执行计划.md`
- `05-风险与问题.md`
- `06-交接说明.md`

Create when:
- Level 3 or Level 4 updates are being applied
- multiple formal files will change
- a structural cleanup is about to happen
- the conversation budget is estimated below 10%

This is the protection layer, not the main working layer.

---

# Minimal survival set

If the user cannot maintain the full cockpit, preserve at least:
- `context/current/01-当前状态.md`
- `context/current/02-决策记录.md`
- `context/current/06-交接说明.md`

These three preserve most continuity value.

---

# Drafting rule

When asked to generate content:
- prefer sections or patch-ready blocks
- match the file’s purpose
- do not repeat the same information across all files
- put each piece of information in the file where it belongs best
- prefer incremental edits over full rewrites
- preserve meaning during structural cleanup
