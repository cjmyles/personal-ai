# Run state

Keep persistent processing state on the same live Trello board in one card titled `Daily Briefing — run state`, labelled `Systems & Automation`. Search active and completed cards before creating it. Create it in `Projects and Decisions` only during the first authorised live run, never during preview or skill publication. If more than one state card exists, report the ambiguity without merging or deleting records. Exclude it from daily task recommendations.

Use the Personal Todo dedicated checklist reader and timestamped history rules for this card too. Preserve manual notes and history. Store a compact machine-readable JSON block in its description with these fields:

```json
{
  "schema_version": 1,
  "timezone": "Asia/Ho_Chi_Minh",
  "last_successful_window_end_utc": null,
  "last_run_id": null,
  "processed_events": [],
  "last_briefing": null
}
```

- Use the run start in UTC as the fixed email window end. Advance `last_successful_window_end_utc` to that value only after complete window coverage, required card writes and read-backs succeed. Messages arriving later belong to the next run.
- Record processed events as message ID, card ID and source timestamp tuples. Keep entries from the most recent 30 days; keep lasting event markers in the affected cards' histories. Do not store email bodies, tokens or unnecessary personal details in state.
- Derive `last_run_id` from the local date and run start. Store the concise prepared briefing and source links in `last_briefing` so a retry can recover it without repeating mutations. Do not claim this proves a notification was delivered.
- Re-read the state immediately before updating it; merge newly observed event tuples, never move the checkpoint backwards and never overwrite newer concurrent state. If another run has advanced the checkpoint, use its result where appropriate and avoid repeating updates. Do not assume the connector offers atomic locking.
- On partial failure, retain the previous successful checkpoint. Verified card-level email markers make already completed writes safe to skip on retry. Do not falsely record failed writes as processed.
- On preview, unavailable state or failed state save, disclose that the checkpoint was not advanced. Never use an untracked local file as a persistent fallback. If state cannot be read or created, continue read-only and report that automatic reconciliation was skipped.
