# Viewing record

The authoritative record is `plugins/watchlist/skills/watchlist/references/watchlist.json` on `main` in `cjmyles/personal-ai`. Fetch it fresh for each request. The file bundled with an installed skill is a snapshot and may be stale. Keep installations pointed at the same GitHub record rather than maintaining separate viewing histories. This repository is public; store only watchlist information Craig requests, never credentials or unrelated personal details.

## Source

The starter catalogue was transcribed from Craig's supplied image, “The New York Times: The 100 Best TV Shows of the 21st Century”, on 26 September 2026. All visible checkboxes were empty. Preserve the displayed order as `source_rank`; it is not Craig's ranking. The source has not been independently checked against the publisher. Omit displayed run dates because they are unnecessary for tracking and may be stale. The image contains TV shows only; add films as Craig requests them.

## Schema

The top-level object contains `schema_version`, `sources`, `titles` and `events`. Each title has a stable `id`, `title`, `type` (`tv` or `film`), optional disambiguating `release_year`, `scope` (`series`, `film` or a named season), `source_id`, `source_rank`, `status`, `progress`, `rating`, `notes`, `added_at` and `updated_at`.

Use null for unknown values. Store progress as an object with user wording and only confirmed season, episode or completion fields. Store a rating with both value and scale, or the user's raw wording if the scale is unknown. Notes must represent user statements, not invented preferences. Added and updated dates describe record maintenance, never assumed viewing dates.

Append events with `recorded_at`, `title_id` and `change`; include viewing dates only when supplied. Preserve stable IDs, source provenance and existing events. New entries need no source rank. Keep all statuses distinct, especially `unconfirmed` versus `want_to_watch`.
