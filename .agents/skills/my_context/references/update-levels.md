# Update Levels

Use these levels to decide how much of the formal project context should change.

## Level 1 — Light Record Update

Use when:
- the conversation produced small progress
- new information was gathered
- ideas were discussed but no major decision was made
- the project direction did not materially change

Typical updates:
- optionally `context/current/01-当前状态.md`
- optionally a work-log style note if the user keeps one

Goal:
- record what happened
- preserve useful details without disturbing stable documents

Output style:
- short
- factual
- low-noise

---

## Level 2 — State Update

Use when:
- a task was completed, started, paused, or re-prioritized
- the project moved into a new working state
- the main “where are we now?” answer changed

Typical file updates:
- `context/current/01-当前状态.md`
- `context/current/03-执行计划.md`

Goal:
- make current status legible
- make the next step obvious

Output should clarify:
- what is done
- what is in progress
- what is blocked
- what should happen next

---

## Level 3 — Decision Update

Use when:
- a meaningful choice was made
- a prior approach was rejected
- a new constraint appeared
- project scope or method changed
- a decision will affect future work

Typical file updates:
- `context/current/02-决策记录.md`
- often `context/current/01-当前状态.md`
- sometimes `context/current/README.md`

Goal:
- preserve the why
- prevent repeated debates or accidental reversals

Output should clarify:
- decision
- reason
- rejected alternatives
- consequence for future work

Before applying this update, prefer creating a snapshot of the current formal context.

---

## Level 4 — Handoff Update

Use when:
- the user wants to preserve context across tools
- the user wants to continue later
- the session is ending at an important checkpoint
- another person or agent should be able to continue
- the user asks for a summary to continue work

Typical file updates:
- `context/current/06-交接说明.md`
- usually `context/current/01-当前状态.md`
- often `context/current/02-决策记录.md`
- sometimes `context/current/03-执行计划.md`

Goal:
- let a new reader continue the work quickly and safely

Output should clarify:
- current project state
- what files to read first
- the next immediate action
- what not to repeat
- major risks or unknowns

Before applying this update, prefer creating a snapshot of the current formal context.

---

# Strong triggers

## Must classify at least Level 3 when:
- the team or user picked one approach over another
- a major workflow or operating rule was established
- scope changed in a way future work depends on

## Must classify at least Level 4 when:
- the user explicitly asks to preserve context
- the output is meant for another tool or future session
- the user wants a handoff-style summary
- remaining conversation/context budget is estimated below 10%

---

# Decision heuristic

Ask:
1. Did anything important change?
2. Does the project state need to be updated?
3. Was a meaningful decision made?
4. Will another tool or future session need to continue from this point?

Then choose the highest applicable level.

Do not inflate minor progress into a full handoff.

When uncertain between two levels:
- choose the lower one for routine progress
- choose the higher one for tool switching or work continuity
