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
  "$venv/bin/python3" -m pip install -r "$repo_root/requirements.txt"
fi

for skill in "$repo_root"/codex/skills/*; do
  [ -d "$skill" ] || continue
  "$venv/bin/python3" "$validator" "$skill"
done
