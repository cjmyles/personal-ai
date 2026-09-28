---
name: tv-movies
description: Track Craig's films and TV shows he wants to watch, is watching or has watched. Use when adding titles to his watchlist, recording viewing progress or ratings, listing watched or unwatched titles, choosing what to watch next, or checking where to stream a tracked title. Includes a starter catalogue of 100 TV shows from Craig's supplied NYT checklist image.
---
# TV & Movies

Use the Google spreadsheet named `TV & Movies` in the `ChatGPT` folder in Craig's connected Google Drive as the sole viewing record. Read its live data through the connected Google Drive/Sheets service before answering or updating viewing history. Do not use GitHub data files, bundled snapshots or conversation memory as a substitute. If the spreadsheet is unavailable, say so and do not claim an update was saved. Read `references/data-guide.md` for discovery, tabs, columns and source details.

## Track viewing

Accept natural requests such as “Add this film”, “I've watched The Wire”, “I'm on season 2 episode 4 of Slow Horses”, “Drop this”, and “What should I watch tonight?”. Resolve the title from the conversation where clear. Ask a short question only when ambiguity would change the record. Keep film remakes and different TV adaptations separate.

Use these statuses: `Unconfirmed`, `Want to watch`, `Watching`, `Watched`, `Paused`, `Dropped`, `Not interested`. Starter catalogue membership does not imply interest or previous viewing. Never infer that Craig has watched a title because he discussed it, requested a stream or identified an actor.

Record only explicitly supplied progress, ratings, viewing dates and opinions. Leave unknown cells blank. Preserve the user's rating scale and wording. Distinguish the date an update was recorded from when viewing occurred. For relative dates, use Craig's current timezone, defaulting to Asia/Ho_Chi_Minh when unspecified.

For “on episode 4”, preserve that wording without claiming episode 4 is completed. For “finished season 1”, record season completion without marking the whole series watched. Keep season-specific starter entries (True Detective season 1 and Beef season 1) scoped to that season. Use `Watched` for an explicit whole-title completion; it does not automatically mean future episodes are watched. Preserve history when a title is restarted or rewatched. Remove a title only when asked to remove it; “not interested” should retain it with that status.

For every update, read spreadsheet metadata and the relevant current rows, locate titles by stable ID rather than remembered row numbers, then make only the requested cell changes. Preserve unrelated records and user edits. Append a History row containing the timestamp, title ID and user-stated change. Validate unique IDs and allowed statuses. Preserve the native table, filters and dropdowns when adding rows, and extend its range to cover them. Re-read changed rows and history before claiming success. If concurrent edits affect the same field, preserve them and resolve the conflict before writing. If saving fails, say exactly which part could not be saved. Never recreate or overwrite the workbook to make a small update.

Keep `My rating` separate from `IMDb rating`. Record Craig's rating and exact opinions only when supplied; preserve his scale. For films, look up the matching IMDb title when adding an entry and record its verified score out of 10, canonical IMDb link and successful `Rating checked on` date. The same fields support TV titles, but never substitute a series-wide score for a season or episode score without labelling the scope. Verify title, year and director when needed to avoid remakes or namesakes. Leave unverified scores and their check dates blank; do not guess, substitute an unweighted mean or treat unavailable as zero. Refresh scores on request or when using them for recommendations, and never overwrite My rating with an external score.

## Answer and recommend

Use short British English answers with no emojis. Default lists to title, type and relevant status or progress. Provide totals when useful; do not dump the entire catalogue unless asked. Keep starter-list rank distinct from Craig's priority or rating. Offer small batches when helping him classify the starter catalogue; do not demand answers for 100 titles at once.

When recommending, prioritise confirmed interests and explicit ratings; explain each choice briefly. Exclude watched, dropped and not-interested titles by default unless a rewatch is requested. Label unconfirmed catalogue suggestions as suggestions, not as items Craig has chosen. Do not add recommendations to his wanted list without his instruction.

Avoid plot spoilers, twists, endings and episode details beyond confirmed progress unless explicitly requested. Use premise, tone, genre and approximate commitment where verified. Do not infer preferences from other personal circumstances.

For streaming availability, release dates, current seasons or other changing facts, verify with live sources and provide links. Establish the viewing country from current conversation; ask if unclear because travel and VPN use can make residence unreliable. Distinguish subscription, rental and purchase, and do not promise VPN compatibility. Never treat the dates or “present” labels in the starter image as current facts. If a fact cannot be verified, say so.
