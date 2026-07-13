---
name: quick-change
description: "Use when the user asks for a small, fast implementation change, especially UI spacing/copy/visual tweaks, and signals speed with phrases like quick, tiny change, small tweak, no tests, just do it, or keep this quick. Optimises for minimal context, minimal edits, and fast handoff."
---

# Quick Change

Use this skill when the user wants a fast, targeted change rather than a full investigation or validation loop.

## Operating Mode

- Prioritise speed and scope control.
- Read only the exact files or nearby code needed to make the change.
- Do not re-read broad project docs unless the request is ambiguous or safety-critical.
- Do not broaden the task into refactors, architecture cleanup, or neighbouring UX changes.
- Keep commentary minimal.

## Workflow

1. Locate the target quickly.
- Use `rg` or a narrow file read.
- Prefer existing component patterns and tokens.
- If the target is already known, skip repo-wide search.

2. Make the smallest viable edit.
- Use `apply_patch` for manual file edits.
- Keep changes tightly scoped to the requested behaviour.
- Do not change unrelated layout, data flow, copy, or state.

3. Validate only as requested.
- If the user says `no tests`, do not run tests.
- If the user says the UI is visually fine, do not take more screenshots.
- For native UI, use a simulator screenshot only when the user asks, when the project instruction cannot be waived, or when the visual result is otherwise impossible to reason about.

4. Stop at the requested endpoint.
- If the user asked only for the change, stop after the edit and report the file changed.
- If the user also asks to commit/push, hand off to the appropriate push skill workflow.

## Final Response

Keep it short: what changed, whether tests/screenshots were skipped or run, and any commit/push details if applicable.
