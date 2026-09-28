---
name: watchlist
description: Track Craig's films and TV shows he wants to watch, is watching or has watched. Use when adding titles to his watchlist, recording viewing progress or ratings, listing watched or unwatched titles, choosing what to watch next, or checking where to stream a tracked title. Includes a starter catalogue of 100 TV shows from Craig's supplied NYT checklist image.
---
# Watchlist

Use the canonical viewing record in `cjmyles/personal-ai` on `main` at `plugins/watchlist/skills/watchlist/references/watchlist.json`. Fetch that file through the connected GitHub service or a current repository checkout before answering or updating viewing history. The bundled `references/watchlist.json` is a snapshot: use it only if GitHub is unavailable, explicitly report that it may be stale, and do not claim an update was saved. Never rely on conversation memory instead. Read `references/data-guide.md` for the schema and source details.

## Track viewing

Accept natural requests such as “Add this film”, “I've watched The Wire”, “I'm on season 2 episode 4 of Slow Horses”, “Drop this”, and “What should I watch tonight?”. Resolve the title from the conversation where clear. Ask a short question only when ambiguity would change the record. Keep film remakes and different TV adaptations separate.

Use these statuses: `unconfirmed`, `want_to_watch`, `watching`, `watched`, `paused`, `dropped`, `not_interested`. Starter catalogue membership does not imply interest or previous viewing. Never infer that Craig has watched a title because he discussed it, requested a stream or identified an actor.

Record only explicitly supplied progress, ratings, viewing dates and opinions. Leave unknown fields null. Preserve the user's rating scale and wording. Distinguish the date an update was recorded from when viewing occurred. For relative dates, use Craig's current timezone, defaulting to Asia/Ho_Chi_Minh when unspecified.

For “on episode 4”, preserve that wording without claiming episode 4 is completed. For “finished season 1”, record season completion without marking the whole series watched. Keep season-specific starter entries (True Detective season 1 and Beef season 1) scoped to that season. Use `watched` for an explicit whole-title completion; it does not automatically mean future episodes are watched. Preserve history when a title is restarted or rewatched. Remove a title only when asked to remove it; “not interested” should retain it with that status.

For every update, reread the latest file, make the minimum changes and append an event containing the timestamp, title ID and user-stated change. Validate JSON, unique IDs, valid statuses and preservation of unaffected records. Save the canonical file to GitHub, using the current file SHA or a non-forced branch update to prevent overwriting concurrent changes. Stage only intended watchlist changes when using a checkout; commit, push and verify the published content. Do not edit an installed plugin cache as the durable record. Refresh the bundled snapshot in any accessible standalone installation after a successful update, using the skill-creator workflow where applicable. The GitHub record remains authoritative if a snapshot refresh is unavailable. Do not claim persistence until verified. On a conflict, preserve both independent changes and ask only if the same field has incompatible edits. If saving fails, say the update could not be saved.

## Answer and recommend

Use short British English answers with no emojis. Default lists to title, type and relevant status or progress. Provide totals when useful; do not dump the entire catalogue unless asked. Keep starter-list rank distinct from Craig's priority or rating. Offer small batches when helping him classify the starter catalogue; do not demand answers for 100 titles at once.

When recommending, prioritise confirmed interests and explicit ratings; explain each choice briefly. Exclude watched, dropped and not-interested titles by default unless a rewatch is requested. Label unconfirmed catalogue suggestions as suggestions, not as items Craig has chosen. Do not add recommendations to his wanted list without his instruction.

Avoid plot spoilers, twists, endings and episode details beyond confirmed progress unless explicitly requested. Use premise, tone, genre and approximate commitment where verified. Do not infer preferences from other personal circumstances.

For streaming availability, release dates, current seasons or other changing facts, verify with live sources and provide links. Establish the viewing country from current conversation; ask if unclear because travel and VPN use can make residence unreliable. Distinguish subscription, rental and purchase, and do not promise VPN compatibility. Never treat the dates or “present” labels in the starter image as current facts. If a fact cannot be verified, say so.
