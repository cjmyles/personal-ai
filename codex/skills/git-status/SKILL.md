---
name: git-status
description: "Use when the user asks whether the current git worktree or branch has anything unstaged, staged but uncommitted, untracked, or committed locally but not pushed to the upstream branch."
---

# Git Status

Use this skill when the user wants a direct answer about whether the current repository is clean, committed, or fully pushed.

## Workflow

1. Inspect the current repository live.
- Run `git status -sb` first.
- If the current directory is not a git repository, say so directly.

2. Split the state into the categories the user actually cares about.
- Untracked files: `git ls-files --others --exclude-standard`
- Unstaged tracked changes: `git diff --name-only`
- Staged but uncommitted changes: `git diff --cached --name-only`
- Current branch: `git branch --show-current`
- Upstream branch: `git rev-parse --abbrev-ref --symbolic-full-name @{u}`
- Unpushed commits, if upstream exists: `git log --oneline @{u}..HEAD`

3. Answer in plain language.
- Say whether the worktree is clean or dirty.
- Say whether anything is staged but not committed.
- Say whether anything is committed locally but not pushed.
- If the branch has no upstream, state that clearly instead of implying push status is known.

## Guardrails

- Do not answer from memory or earlier turn state. Always run the git commands again.
- Keep the answer short unless the user asks for detail.
- If there are changed files, list the file paths under the correct category.
- If everything is clean and fully pushed, say that explicitly.
