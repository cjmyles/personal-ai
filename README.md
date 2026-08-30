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
