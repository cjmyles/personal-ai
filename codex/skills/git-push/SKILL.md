---
name: git-push
description: "Use when the user asks to commit and push local changes. Handles scoped or all-local pushes, fast/no-test pushes, and validated pushes. Trigger on `git-push`, commit-and-push requests, push all, push fast, no-test push, or similar requests that should publish commits without opening a PR."
---

# Git Push

Use this skill to commit and push without opening a PR.

## Workflow

1. Inspect state and intent.
- Run `git status -sb`.
- Determine scope from the user's wording:
  - If the prompt is only `git-push`, or otherwise does not say what to include, stop and ask the user whether to push scoped changes or all local changes.
  - Use scoped changes when the user says this, scoped, current task, related changes, or equivalent.
  - Include all local changes only when the user says all, everything, include all local files, or equivalent.
- Determine validation from the user's wording:
  - If the prompt is only `git-push`, or otherwise does not say fast/no-tests/tests, stop and ask the user whether to skip tests, run focused checks, or run full validation.
  - Skip tests when the user says fast, no tests, quick, just push, or equivalent.
  - Run the smallest useful focused validation when the user asks for tests or the change is obviously high-risk.
  - Run broader validation only when explicitly requested.
  - In the Solar-App repo, when validation is requested or a native change is obviously high-risk, include the smallest relevant native Maestro smoke flow: `pnpm run smoke:native:capture-preview` for capture/review/layout changes, `pnpm run smoke:native:installer-job` for installer job package navigation/task changes, `pnpm run smoke:native:app-update-banner` for update banner changes, or `pnpm run smoke:native` for broad native release coverage.
- For a bare skill invocation, ask both questions together before staging or validating.

2. Commit the selected changes.
- For scoped pushes, review the relevant diff enough to identify files related to the current request and stage only those files.
- For all-local pushes, stage all local changes with `git add -A`.
- Generate a terse commit message; the user does not need to provide one.
- If there are no selected changes to commit, say that clearly and continue to push only if the branch has unpushed commits.

3. Push.
- Push the current branch to `origin`.
- Never force-push unless the user explicitly asks for it.

## Defaults

- Bare `git-push`: ask for scope and validation mode before staging.
- Explicit scope and validation supplied: proceed with the requested mode.
- Default commit message: generated terse summary.
- Default branch: current branch.

## Final Response

Report the branch, commit, push result, validation status, and whether unrelated local files were included or left alone.
