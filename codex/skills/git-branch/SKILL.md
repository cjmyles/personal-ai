---
name: git-branch
description: "Use when the user asks to create a fresh git branch from the latest main/default branch, especially with a random codex/word-word-word branch name. Handles fetching, updating the base branch, choosing an available codex branch name from a large word pool, and switching to the new branch while preserving unrelated user work."
---

# Git Branch

Use this skill when the user wants a low-ceremony branch setup before starting work.

## Workflow

1. Inspect the repository and worktree.
- Run `git status -sb` first.
- If the current directory is not a git repository, say so directly.
- If there are uncommitted changes, do not reset or discard them. If switching branches or pulling would be risky, stop and ask whether to stash, commit, or keep working from the current branch.

2. Find the base branch.
- Prefer `main` when it exists locally or at `origin/main`.
- Otherwise, use the repository default branch from `refs/remotes/origin/HEAD` when available.
- Fetch `origin` before deciding whether the local base is current.

3. Update the base safely.
- Switch to the base branch if the worktree allows it.
- Fast-forward only with `git pull --ff-only`.
- If fast-forwarding fails, do not merge implicitly. Report the blocker and ask how to proceed.

4. Create a random branch name.
- Use the format `codex/<word>-<word>-<word>` unless the user requested a different prefix or exact format. Three words are preferred because repeated two-word names collide too easily.
- Do not pick words from memory. Generate candidates from a large local word source when available, such as `/usr/share/dict/words`, using `shuf`/`awk`/`sort` or another simple shell pipeline. If no dictionary exists, use another broad source available on the machine, not a small hand-picked list.
- Use simple lowercase dictionary words with no digits, punctuation, apostrophes, proper nouns, or offensive terms. Prefer words 4-10 characters long so branch names stay readable.
- Check availability with `git branch --list <branch>` and `git ls-remote --heads origin <branch>` when network access is available.
- If the candidate exists locally or remotely, choose another generated candidate. Try at least several generated candidates before falling back to a manually chosen name.

5. Create and switch to the branch.
- Run `git checkout -b <branch>` from the updated base branch.
- Do not set upstream or push unless the user explicitly asks.
- Report the branch name and base commit.

## Guardrails

- Never use `git reset --hard`, `git checkout -- <path>`, or any destructive cleanup unless the user explicitly asks.
- Never overwrite or revert user changes to make branch creation easier.
- Avoid broad shell scripts for the workflow; run the git commands directly so each step is visible and failures are easy to explain.
- If the user asks for "latest main", use live git state instead of relying on earlier context.
