---
name: native-production-ota
description: Use when the user asks to commit and push native app changes, raise and merge a PR, tag main, and publish an Expo/EAS OTA update to the production channel. Trigger on requests like "commit and push, raise a PR and merge it, tag main and do an OTA on production", "ship a production OTA from this PR", "release this native change via OTA", or similar workflows that combine PR publication, validation, merge, native OTA tagging, and production EAS Update.
---

# Native Production OTA

Use this as the end-to-end release workflow for 123STC native OTA changes. It composes the existing git PR workflow and native release rules into one sequence.

## Preconditions

- Read repo instructions first, especially `AGENTS.md` and `docs/engineering/ai-shared-instructions.md`.
- Read `docs/skills/native/native-release/SKILL.md` before publishing or tagging the OTA.
- Never publish the OTA from a dirty worktree.
- Do not run production migrations, database promotion, or Vercel production promotion unless the user explicitly asks.
- If the user says no tests, do not run checks; record that validation was intentionally skipped.

## Validation Scope

Pick the smallest validation that protects the release.

- Small native UI follow-up: run native lint plus a targeted simulator visual check or the smallest matching Maestro flow.
- Installer Jobs/calendar changes: run native lint and `pnpm run smoke:native:installer-job` unless a narrower existing smoke route directly covers the change.
- Capture/review/evidence/safe-area/footer changes: run native lint and `pnpm run smoke:native:capture-preview`.
- App update/version banner changes: run native lint and `pnpm run smoke:native:app-update-banner`.
- Broad native navigation, multiple smoke surfaces, release candidate, or uncertain blast radius: run `pnpm run smoke:native`.
- Run local CI with `pnpm run check:ci` when the user asks for local CI, a full release gate, or the change includes web/server/shared packages. For a narrow native-only OTA, prefer native lint plus the relevant native smoke unless the user asks for local CI.

Use Node 20/Corepack commands from the repo root:

```bash
source ~/.nvm/nvm.sh && nvm use 20 >/dev/null && corepack pnpm ...
```

## Workflow

1. Inspect state.
   - Run `git status -sb`, `git branch --show-current`, and review the diff.
   - Confirm the scope is only the intended release.

2. Validate before PR.
   - Run the selected local validation from **Validation Scope**.
   - For native smoke, start Metro when needed, then stop it before final handoff.
   - If Maestro fails with a clear XCUITest/simulator infrastructure error, rerun only the affected flow once before treating it as product failure.

3. Commit and push.
   - Stage only scoped files unless the user explicitly says all local changes.
   - Commit with a terse message.
   - Push the branch to origin.

4. Create a ready PR.
   - Use `.github/pull_request_template.md`.
   - Include validation run and any intentionally skipped checks.
   - Wait for GitHub/Vercel checks unless the user explicitly asks to merge without waiting.

5. Merge the PR.
   - Prefer the repo-supported merge method. If merge commits are disabled, squash merge.
   - After merge, switch to `main` and run `git pull --ff-only origin main`.
   - Confirm `git status -sb` is clean and `git log -1 --oneline` is the merged release commit.

6. Validate main.
   - Run the agreed release validation on `main`.
   - Do not repeat an unnecessarily broad suite just because a previous OTA used it; match the validation to the change and risk.

7. Publish production OTA.
   - Run:

```bash
source ~/.nvm/nvm.sh && nvm use 20 >/dev/null && corepack pnpm run update:native:production
```

   - Capture the EAS output: branch/channel, runtime version, platform list, update group ID, iOS update ID, Android update ID, commit, and dashboard URL.

8. Tag main.
   - Follow `docs/skills/native/native-release/SKILL.md`.
   - Use existing tag convention. Current 123STC production OTA tags are platform-specific:
     - `native-ios-1.0.0+9-ota.YYYY-MM-DD.N`
     - `native-android-1.0.0+10-ota.YYYY-MM-DD.N`
   - Increment `N` for multiple OTAs on the same date.
   - Create annotated tags on the OTA commit. Include EAS update group, runtime version, platform, platform update ID, and commit SHA.
   - Push the tags.

9. Final report.
   - Include PR URL, merge commit, validation results, EAS update group/dashboard, pushed tags, and clean worktree status.
   - Mention any user-owned follow-up such as production migrations or Vercel promotion.
