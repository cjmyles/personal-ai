---
name: git-pr
description: "Use when the user wants to create or update a pull request. Handles scoped or all-local PRs, fast/no-test PRs, and validated PRs. Trigger on `git-pr`, PR-ready requests, open/update PR, create a pull request, yeet this, yeet fast, yeet all, or similar requests that should publish commits and open or update a PR."
---

# Git PR

Use this skill when the user wants a PR opened or updated.

## Workflow

1. Inspect state and intent.
- Run `git status -sb` and review the diff before staging.
- Identify the current branch and check whether it already has an open PR. If it does, treat the request as instructions to update that existing PR on its existing head branch.
- Determine scope from the user's wording:
  - If the prompt is only `git-pr`, or otherwise does not say what to include, stop and ask the user whether to PR scoped changes or all local changes.
  - Use scoped changes when the user says this, scoped, current task, related changes, or equivalent.
  - Include all local changes only when the user says all, everything, include all local files, or equivalent.
- Determine validation from the user's wording:
  - If the prompt is only `git-pr`, or otherwise does not say fast/no-tests/tests, stop and ask the user whether to skip tests, run focused checks, or run full PR validation.
  - Skip tests when the user says fast, no tests, quick, just PR, or equivalent.
  - Run PR validation when the user asks for validation, full checks, PR checks, ready for review, or equivalent.
- For a bare skill invocation, ask both questions together before staging or validating.

2. Validate when not fast.
- Run the same validation path as the GitHub Actions PR workflow when one is available. In the Solar-App repo, run `pnpm install --frozen-lockfile`, then `pnpm run check:ci` before publishing unless there is a clear blocker.
- Run any focused tests that cover the changed behavior.
- In the Solar-App repo, include the smallest relevant native Maestro smoke flow when native changes are in scope and validation is not being skipped:
  - Run `pnpm run smoke:native:capture-preview` for capture, review, evidence guidance, location banner, sync footer, camera/review layout, or capture smoke screen changes.
  - Run `pnpm run smoke:native:installer-job` for installer access links, job overview, task list, questionnaire, component group navigation, or package task flow changes.
  - Run `pnpm run smoke:native:app-update-banner` for app update banner or version gating changes.
  - Run `pnpm run smoke:native` for broad native navigation changes, release-candidate work, or when multiple native smoke surfaces are touched.
- If validation is blocked by missing dependencies, sandbox limits, or environment setup, report that clearly in the final summary and PR body.
- When fast/no-test mode is requested, do not run tests or lint, and mention in the PR body and final response that validation was intentionally skipped.

3. Commit and push selected changes.
- For scoped PRs, stage only files related to the current request and leave unrelated local files alone.
- For all-local PRs, stage all local changes with `git add -A`.
- Generate a terse commit message; the user does not need to provide one.
- Push the current branch to `origin`. If updating an existing PR, push to that PR's existing head branch.
- Never force-push unless the user explicitly asks for it.

4. Open or update a non-draft PR.
- If a PR already exists for the branch, update that PR's title/body when useful and make sure it is ready for review.
- If no PR exists, open one against the repository default branch unless the user specified a base.
- Before creating or updating the PR body, read `.github/pull_request_template.md` when it exists and fill that template. Do not use a shorter ad hoc body unless the user explicitly asks.
- Make the PR ready for review by default, not draft, unless the user explicitly asks for draft.
- After pushing, inspect the PR checks and report their status. Do not call the PR clean while checks are pending.
- If the user has asked to create/switch to a new branch or continue the next task, do that immediately after local validation, commit, push, and PR creation/update. Do not wait for remote checks first unless the user explicitly asks to wait.
- If remote checks fail before the next task starts, inspect the failing job and fix it when practical. If the next task is already underway, surface the failure and ask whether to pause current work or handle the PR failure afterward.

## Guardrails

- Never include unrelated work in a scoped PR.
- Never create a second PR for a branch that already has an open PR unless the user explicitly asks for a new PR.
- Do not rebase by default. Rebase only when requested, needed to resolve a non-fast-forward push, or clearly required by the repo workflow.
- Never force-push unless the user explicitly asks for it.
- Summarize the branch, commit, PR URL, validation status, and any blockers at the end.
