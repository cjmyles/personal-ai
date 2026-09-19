# Personal AI

Source-controlled personal AI configuration.

## Global Codex instructions

`codex/global/AGENTS.md` tracks the global customisation file, normally `~/.codex/AGENTS.md`. It is stored below `global/` so it does not become this repository's own root instructions. Only this file is synced, not the rest of `.codex`.

After editing customisation in Codex settings, run `python3 codex/scripts/sync-instructions.py capture` to preview the changes, then repeat with `--write` to copy them into the repository. Review, commit and push the changed file to save the new version.

After pulling an intentional change from Git, run `python3 codex/scripts/sync-instructions.py apply` to preview it, then repeat with `--write` to update the live Codex file. The script honours `CODEX_HOME`, backs up an existing destination before overwriting it, and verifies the copy. Sync is manual: it does not watch settings, resolve conflicts, commit or push. If both copies changed, reconcile the preview before copying.

## Skills and plugins

- `codex/skills/`: Personal Codex skills using generic, portable names.
- `plugins/`: Personal plugins that package reusable skills for ChatGPT Work and Codex.
- `.agents/plugins/marketplace.json`: Repository marketplace for installing personal plugins.
- `codex/scripts/validate.sh`: Validates every repository skill.
- `codex/scripts/install.sh`: Installs standalone and plugin-packaged skills into `$CODEX_HOME/skills` without removing legacy skills.

Run `./codex/scripts/validate.sh`, then `./codex/scripts/install.sh`.

The installer backs up an existing skill with the same generic name before replacing it. Legacy `craig-*` skills remain installed until removed deliberately.

The `fpl-draft` plugin is the canonical home of the `manage-fpl-draft` skill. Install the repository marketplace, then install `fpl-draft@personal` to expose it as a plugin.

The `tax-invoicing` plugin is the canonical home of `tax-ledger` and `invoice-ledger`, including all supporting references. It packages the workflows together; Gmail, Google Drive and the configured invoicing service still require their own access.

The `craig-email` plugin contains the `write-craig-email` skill for drafting and sending email in Craig's preferred voice and Trebuchet MS formatting. It uses the available email integration rather than bundling credentials or a mail connector.

Use short, descriptive Title Case display names for every skill and plugin. Omit “Craig” and “Manage” prefixes. Give a plugin and its single main skill the same display name. Preserve existing machine identifiers to keep installed plugins, saved prompts and integrations working.

The `document-style-guide` plugin is the canonical home of the `document-style-guide` skill. It covers document structure, references, appendices, minimal editing and readable paragraph spacing in all assistant replies.

## FPL Draft workflow assets

The [FPL Draft skill](plugins/fpl-draft/skills/manage-fpl-draft/SKILL.md) reads live Draft league data and official team news, records decisions and outcomes in [Google Sheets](https://docs.google.com/spreadsheets/d/1JrauLxOESM6MO--1jzzkNhR7J4GtN97QjAWRxKKfQ1E/edit), and maintains one concise [Notion dashboard](https://app.notion.com/p/3e0fc8ce55dd81598575e2ac1f649d4d). The [reporting contract](plugins/fpl-draft/skills/manage-fpl-draft/references/reporting-and-learning.md) documents ownership, schedules, data schemas and failure handling. Reports adapt to live gameweek deadlines; team changes always require Craig’s explicit approval.
