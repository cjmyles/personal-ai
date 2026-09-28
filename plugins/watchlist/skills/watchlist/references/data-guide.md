# Viewing record

Use the native Google spreadsheet named `TV & Movies` in the `ChatGPT` folder in Craig's connected Google Drive as the sole source of truth.

Discover it through Google Drive search with the exact name and native spreadsheet MIME type. Confirm its parent is the ChatGPT folder and its tabs and headers match below. If more than one matches, ask Craig which to use. Never create a replacement on a failed search. Keep private spreadsheet IDs and URLs out of this public repository.
Read metadata on each request to resolve current tab names, sheet IDs, table ranges and headers. Do not rely on cached row numbers. The initial tabs are `Watchlist` and `History`.

## Source

The starter catalogue was transcribed from Craig's supplied image, “The New York Times: The 100 Best TV Shows of the 21st Century”, on 26 September 2026. All visible checkboxes were empty. Its source ID is `nyt-image-2026-09-26`. Preserve the displayed order as Source rank; it is not Craig's ranking. The source has not been independently checked against the publisher. Omit displayed run dates because they may be stale. The image contains TV shows only; add films as Craig requests them.

## Schema

Watchlist contains one row per title with these columns:

| Column | Meaning |
| --- | --- |
| Title | Film or TV title |
| Type | TV or Film |
| Status | Unconfirmed, Want to watch, Watching, Watched, Paused, Dropped or Not interested |
| Progress | User wording, including only confirmed season, episode or completion details |
| Rating | User's value and scale, or exact wording if the scale is unknown |
| Notes | User statements, with separate notes on separate lines |
| Release year | Disambiguating year when known |
| Scope | series, film or a named season |
| Source rank | Starter catalogue order, blank for other entries |
| Added at | Record creation date |
| Updated at | Last record update date |
| ID | Unique stable title ID, retained through sorting and renaming |
| Source ID | Source identifier, blank when none applies |

Leave unknown cells blank. Dates describe record maintenance, never assumed viewing dates. Use ISO dates or timestamps and Craig's timezone, defaulting to Asia/Ho_Chi_Minh. Preserve the user's rating scale and wording.

History contains Recorded at, Title ID and Change. Append rather than overwrite it. Include viewing dates only when supplied. Preserve history for restarts and rewatches. New entries need no source rank. Keep Unconfirmed distinct from Want to watch.

## Updates

Use connected Google Sheets tools to read and write bounded ranges. Match columns by the current headers. Use literal text for titles, notes and progress so user wording cannot become a formula. For new titles, check existing title, type, scope and year before inserting to avoid duplicates. Create a unique stable ID. Preserve table dropdowns and extend the table range after insertion. Update the record and append its history in one batch where possible, then read both back. Do not assume a failed or timed-out write did nothing: check before retrying to avoid duplicate rows or events.

Do not maintain a JSON file or a second viewing database in the skill repository.
