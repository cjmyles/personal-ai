# Personal AI

Source-controlled personal AI configuration.

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
