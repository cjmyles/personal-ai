# Publishing personal configuration

When Craig asks to update a repository-backed skill or plugin, completion includes validating, committing, pushing, refreshing the marketplace, installing the updated plugin and comparing installed files with the published source. Keep any standalone installation of the changed skill synchronised as well. Do not say "updated" or "done" if only local files changed; report the exact blocked step and remaining unpublished work.

Before publishing, inspect local and remote changes. Preserve unrelated work and do not publish it without authorisation. Reconcile published changes into the primary checkout so a completed update is not left as a stale local diff. Verify the final Git status and report any remaining uncommitted or unpushed changes explicitly.

The global customisation file is tracked at `codex/global/AGENTS.md`; the live copy is normally `/Users/craig/.codex/AGENTS.md`. When asked to save or publish settings changes, use `codex/scripts/sync-instructions.py capture` to preview and `capture --write` to copy into Git, then review, commit and push. To activate an intentional repository change, use `apply` to preview and `apply --write` to update the live copy. These commands run only when invoked; nothing watches settings automatically. Explain the outcome in plain language rather than assuming Craig will run scripts.
