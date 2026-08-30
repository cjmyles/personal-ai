#!/bin/sh
set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
destination="${CODEX_HOME:-$HOME/.codex}/skills"
backup_root="$destination/.personal-ai-backups/$(date +%Y%m%d-%H%M%S)"

"$repo_root/codex/scripts/validate.sh"
mkdir -p "$destination"

for skill in "$repo_root"/codex/skills/* "$repo_root"/plugins/*/skills/*; do
  [ -d "$skill" ] || continue
  name=$(basename "$skill")
  target="$destination/$name"
  if [ -e "$target" ]; then
    mkdir -p "$backup_root"
    cp -R "$target" "$backup_root/$name"
    rm -rf "$target"
  fi
  cp -R "$skill" "$target"
  echo "Installed $name"
done

echo "Legacy craig-* skills were left untouched."
