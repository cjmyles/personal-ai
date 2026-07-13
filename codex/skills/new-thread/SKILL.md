---
name: new-thread
description: "Use when the user wants a ready-to-paste prompt for a new Codex thread that should continue the current discussion on a fresh branch from the latest origin/main."
---

# New Thread

Use this skill when the user wants a prompt for a new Codex thread.

## Goal

Produce a ready-to-paste prompt that tells the new Codex thread to:

- start from the latest `origin/main`
- create a new branch using the `codex/` prefix unless the user asked for a different name
- continue the work currently being discussed
- carry forward the important context, constraints, and success criteria

## Workflow

1. Base the prompt on the current discussion.
- Summarize the actual objective in plain language.
- Include the relevant architecture constraints, repo rules, and risks already identified.
- Include any specific files, branches, or prior exploratory work that matter.

2. Make the prompt execution-oriented.
- Tell the new Codex thread to inspect the current repo state and compare against any referenced branch if needed.
- Tell it what to implement, preserve, avoid, or clean up.
- Tell it not to blindly cherry-pick or copy work when selective reimplementation is safer.

3. Always include these branch instructions unless the user explicitly overrides them.
- Start from the latest `origin/main`.
- Create a new branch off it using a `codex/` prefix.

4. Include validation and handoff expectations.
- Ask for a short plan first when useful.
- Ask it to run relevant checks for touched areas.
- Ask for a final summary of what was changed, what was intentionally excluded, and any follow-up risks.
- Tell it not to commit unless the user explicitly asks.

## Output shape

- Default to a single paste-ready fenced code block.
- Keep the prompt concrete and specific to the current discussion.
- Prefer direct instructions over commentary.

## Guardrails

- Do not answer with a generic template if the current discussion provides enough context to be specific.
- Do not omit the `origin/main` and `codex/` branch requirements unless the user explicitly changes them.
- If there are important architectural concerns already identified, include them near the top of the prompt so the next thread sees them immediately.
