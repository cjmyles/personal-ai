#!/bin/sh
set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
validator="${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py"
venv="$repo_root/.venv"

if [ ! -f "$validator" ]; then
  echo "Skill validator not found: $validator" >&2
  exit 1
fi

if [ ! -x "$venv/bin/python3" ]; then
  python3 -m venv "$venv"
fi

if ! "$venv/bin/python3" -c 'import yaml' >/dev/null 2>&1; then
  "$venv/bin/python3" -m pip install -r "$repo_root/requirements.txt"
fi

validate_skill() {
  skill=$1
  [ -d "$skill" ] || {
    echo "Skill not found: $skill" >&2
    exit 1
  }
  "$venv/bin/python3" "$validator" "$skill"
}

if [ "$#" -gt 1 ]; then
  echo "Usage: $0 [skill-name]" >&2
  exit 1
elif [ "$#" -eq 1 ]; then
  validate_skill "$repo_root/codex/skills/$1"
else
  for skill in "$repo_root"/codex/skills/*; do
    [ -d "$skill" ] || continue
    validate_skill "$skill"
  done
fi
