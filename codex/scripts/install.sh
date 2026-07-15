#!/bin/sh
set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd)
destination="${CODEX_HOME:-$HOME/.codex}/skills"
backup_root="$destination/.personal-ai-backups/$(date +%Y%m%d-%H%M%S)"

mkdir -p "$destination"

install_skill() {
  skill=$1
  [ -d "$skill" ] || {
    echo "Skill not found: $skill" >&2
    exit 1
  }
  name=$(basename "$skill")
  target="$destination/$name"
  if [ -e "$target" ]; then
    mkdir -p "$backup_root"
    cp -R "$target" "$backup_root/$name"
    rm -rf "$target"
  fi
  cp -R "$skill" "$target"
  echo "Installed $name"
}

if [ "$#" -gt 1 ]; then
  echo "Usage: $0 [skill-name]" >&2
  exit 1
elif [ "$#" -eq 1 ]; then
  "$repo_root/codex/scripts/validate.sh" "$1"
  install_skill "$repo_root/codex/skills/$1"
else
  "$repo_root/codex/scripts/validate.sh"
  for skill in "$repo_root"/codex/skills/*; do
    [ -d "$skill" ] || continue
    install_skill "$skill"
  done
fi

echo "Legacy craig-* skills were left untouched."
