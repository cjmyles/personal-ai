---
name: git-worktree
description: "Use when the user asks to create, move, inspect, or clean up a separate git worktree, especially for Codex implementation work that should not interfere with an existing checkout. Enforces the user's default of disposable /private/tmp/solar-* worktrees unless a persistent location is explicitly requested."
---

# Git Worktree

Use this skill when the user asks for a new worktree, separate checkout, isolated branch, or moving work out of the current repo checkout.

## Defaults

- Default disposable Codex worktrees go under `/private/tmp/solar-<short-task-name>`.
- Do not create sibling worktrees under `/Users/craig/dev/mvai` unless the user explicitly asks for a persistent local checkout.
- Use a `codex/` branch prefix unless the user requests a different branch name or prefix.
- Start from the latest `origin/main` when the user asks for fresh work.

## Workflow

1. Inspect current state.
- Run `git status -sb` in the current checkout.
- Run `git worktree list` to avoid path or branch collisions.
- Do not modify, stash, reset, or clean the current checkout unless the user explicitly asks.

2. Pick the target path.
- Use `/private/tmp/solar-<short-task-name>` for disposable agent work.
- If the target path exists, choose a clear variant or ask when the intended reuse is ambiguous.
- Use a persistent project-parent directory only when the user explicitly asks for it.

3. Prepare the base.
- Fetch `origin/main` before creating a fresh worktree from latest main.
- If network or authentication is unavailable, report that and either use the best available local base or ask, depending on risk.

4. Create the worktree.
- Prefer `git worktree add -b <branch> <path> origin/main` for a fresh branch.
- If the branch already exists, do not overwrite it. Choose another branch name or ask.
- Request escalation when needed for git refs, worktree metadata, or paths outside the writable root.

5. Verify and report.
- Run `git status -sb` in the new worktree.
- Run `git worktree list` if useful to confirm placement.
- Report the final path, branch, and base.

## Guardrails

- Never create disposable worktrees inside the repo directory.
- Never create worktrees in `/Users/craig/dev/mvai` by assumption.
- Never remove a worktree unless it is clean or the user explicitly confirms the cleanup.
- Never use destructive commands such as `git reset --hard` or `git clean` to make worktree setup easier.
