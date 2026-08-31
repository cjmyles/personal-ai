---
name: manage-personal-tasks
description: "Manage Craig's personal tasks on the live Trello Personal Todo board. Use for requests such as what should I do next, prioritise my day or week, add or update a task, mark a task complete, record that a task is waiting on someone, review deadlines, or organise the personal backlog."
---

# Manage Personal Tasks

Use Trello as the source of truth for personal tasks. Keep durable workflow rules here, but always get current cards and statuses from the live board.

## Board

- Board name: `Personal Todo`
- Board URL: `https://trello.com/b/HnE7NxLs/personal-todo`
- Workspace: `Personal Workspace`

Resolve the board and its lists through the connected Trello tools at the start of each task. Do not hard-code internal board, list, card, or label IDs because they can change.

## Lists

Use these lists in this order:

1. `Inbox`: Unprocessed tasks captured quickly.
2. `Today / Now`: The small set Craig intends to work on now or today.
3. `This Week`: Committed work for the current week.
4. `Next`: Actionable tasks that are not committed for this week.
5. `Waiting`: Outcomes owned by someone else or blocked by an external response.
6. `Projects and Decisions`: Multi-step outcomes, reviews, and decisions that need thought or decomposition.
7. `Scheduled`: Tasks intentionally deferred until a real date or trigger.
8. `Completed`: Finished tasks retained as a record.

Treat list position as meaningful. Keep the most important or time-sensitive card near the top of each active list.

## Labels

Apply the smallest useful set of existing labels:

- `Finance & Tax` — Green
- `Insurance` — Yellow
- `Life & Career` — Orange
- `Health` — Red
- `Work & Products` — Purple
- `Property` — Blue
- `Personal Admin` — Sky
- `Systems & Automation` — Black

Do not create a new label when an existing one describes the task adequately.

## Read Before Acting

1. Read the live board before answering a status or prioritisation question.
2. Search current and completed cards before creating a card to avoid duplicates.
3. Treat Trello as authoritative when it conflicts with remembered conversation context.
4. Read the relevant card description, checklist, comments, due date, and position before changing it.
5. Use another connected source, such as sent email, only when the user asks for verification or when verification is necessary to make the requested update accurately.

## Decide What Is Next

When asked what to do next:

1. Check `Today / Now` first.
2. Identify overdue items, hard deadlines, financial consequences, health risks, or tasks that unblock other work.
3. Check `This Week`, then follow-ups in `Waiting`, then `Next`.
4. Recommend one primary action and, when useful, one short alternative.
5. Explain the recommendation briefly using urgency, impact, effort, and dependency.
6. Ask about available time or energy only when it would materially change the recommendation.

Keep `Today / Now` deliberately small. Do not move a large batch there merely because the items matter.

## Create or Update Tasks

- Create a new task in `Inbox` unless the user clearly assigns urgency, timing, or status that requires another list.
- Use a concise, outcome-oriented card title.
- Put relevant context, the next action, dependencies, names, and links in the card description or checklist.
- Use one card per outcome. Use a checklist for closely related steps instead of fragmenting an outcome across many cards.
- Add only relevant labels.
- Add a due date only for a genuine deadline, appointment, review date, or agreed follow-up.
- Preserve useful existing context when updating a card.
- Avoid storing unnecessary sensitive health, financial, tax, insurance, estate, or identity details in Trello.

## Track Responsibility and Status

For tasks Craig can act on, keep the card in an active list that reflects its priority.

When responsibility passes to another person:

1. Move the card to `Waiting`.
2. Record who or what Craig is waiting on, the expected outcome, and when the request was made.
3. Add a real follow-up date when one is known or useful.
4. Keep the task open until the outcome is received and reviewed.

When Craig reports completion:

1. Find the matching live card.
2. Confirm ambiguity only if multiple cards plausibly match.
3. Update any final checklist or context that is useful for the record.
4. Move the card to `Completed`.

Do not treat sending a request as completion when the desired outcome is still outstanding; use `Waiting` instead.

## Mutations and Reporting

- Make only changes that are within the user's request.
- If the user asks only for advice or status, do not mutate Trello.
- After a mutation, state exactly what was created, changed, moved, or completed.
- If a requested mutation cannot be performed through the available Trello connection, explain the limitation and give a concise manual fallback.


## Desktop and Mobile Use

This skill must work from ChatGPT Work on desktop and mobile without Craig's laptop being on. For ordinary todo management, rely on the connected Trello app or Trello-capable tools, not local files, browser tabs, OneNote, or this Codex desktop session.

Use local browser, Gmail, files, or repo access only when the user explicitly asks to verify or action something that requires those sources. If those sources are unavailable in a cloud/mobile chat, explain the limitation and continue with Trello-only task management where possible.

