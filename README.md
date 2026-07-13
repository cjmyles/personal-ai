# Personal AI

Source-controlled personal AI configuration.

- `codex/skills/`: Personal Codex skills using generic, portable names.
- `codex/scripts/validate.sh`: Validates every repository skill.
- `codex/scripts/install.sh`: Installs repository skills into `$CODEX_HOME/skills` without removing legacy skills.

Run `./codex/scripts/validate.sh`, then `./codex/scripts/install.sh`.

The installer backs up an existing skill with the same generic name before replacing it. Legacy `craig-*` skills remain installed until removed deliberately.
