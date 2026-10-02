# Publishing personal configuration

When Craig asks to update a repository-backed skill or plugin, completion includes validating, committing, pushing, refreshing the marketplace, installing the updated plugin and comparing installed files with the published source. Keep any standalone installation of the changed skill synchronised as well. Do not say "updated" or "done" if only local files changed; report the exact blocked step and remaining unpublished work.

Before publishing, inspect local and remote changes. Preserve unrelated work and do not publish it without authorisation. Reconcile published changes into the primary checkout so a completed update is not left as a stale local diff. Verify the final Git status and report any remaining uncommitted or unpushed changes explicitly.

The global customisation file is tracked at `codex/global/AGENTS.md`; the live copy is normally `/Users/craig/.codex/AGENTS.md`. When asked to save or publish settings changes, use `codex/scripts/sync-instructions.py capture` to preview and `capture --write` to copy into Git, then review, commit and push. To activate an intentional repository change, use `apply` to preview and `apply --write` to update the live copy. These commands run only when invoked; nothing watches settings automatically. Explain the outcome in plain language rather than assuming Craig will run scripts.

## Plugin and skill names and icons

Use short, descriptive Title Case display names. Give each single-skill plugin and its skill the same display name. Use an umbrella name for a multi-skill plugin and specific names for its skills. Use matching lowercase hyphenated plugin identifiers, skill invocation names and directory names: personal-todo, cafe-picker, email-assistant, fpl-draft, tv-movies and document-style-guide. Tax & Invoicing uses tax-invoicing with tax-ledger and invoice-ledger skills. Update manifests, marketplace entries, prompts and references together when renaming. Keep the main SKILL.md heading consistent with the skill display name.

The approved display names are Café Picker, Email Assistant, Personal Todo, Document Style Guide, FPL Draft and TV & Movies. Personal Todo contains Personal Todo and Daily Briefing (`daily-briefing`). Tax & Invoicing contains Tax Ledger, Invoice Ledger and Project Cost Reconciliation.

Explicitly configure both `interface.logo` and `interface.composerIcon` in every personal plugin manifest, and both `interface.icon_small` and `interface.icon_large` in every packaged skill's `agents/openai.yaml`. Use identical artwork for a plugin and its skills, including multi-skill plugins. Keep paths relative to the plugin or skill root, make every referenced asset available inside its package, and verify matching copies have identical contents.

Preserve approved artwork, including the existing Café Picker and FPL Draft icons. TV & Movies uses the approved smiling popcorn character on a coral rounded tile. For new artwork, favour the softly shaded rounded-square style used by Email Assistant, Personal Todo and Document Style Guide. Generate a preview and obtain approval before replacing established artwork.

Standalone developer skills under `codex/skills/` retain their existing display names and remain icon-free as a consistent group. Validate names, icon references and asset consistency before publishing future plugin or skill changes.
