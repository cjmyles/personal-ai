# Private run state and linked review

Use the existing recurring Personal Todo card titled `Reconcile monthly project costs` (or its saved successor), linked to the current Project Finances ledger. Inspect descriptions and dedicated checklists; search active and completed cards before any create. Store these private records on that card, not in source control:

- Ledger URL; related partner-agreement and cost-reduction task URLs.
- Automation ID and current user-approved recurrence/timezone for recovery; the automation app remains authoritative for its timing.
- Linked reminders block required by Personal Todo, including event/series IDs and stable occurrence markers.
- Compact `Project reconciliation state` JSON with `schema_version`, `last_run_started_utc`, `last_successful_period`, `periods` (period, complete/partial, missing evidence, source keys, verified change summary), and `last_result` (concise output plus source links).

Default previous complete calendar month; also read every unresolved period, even outside the latest window. A retry skips verified existing expense keys but rechecks pending items and changed records. A successfully saved partial result does not advance `last_successful_period` past an unresolved earlier period. Initialise it as null if historical completion is not established.

Save only after required Notion/Trello/Calendar writes and read-backs. Re-read and merge concurrent state; never erase another run's progress. On a partial write, record which counterpart succeeded and stable keys for repair. If state save fails, report it and do not claim the period is complete. Keep card history timestamped. Keep machine state concise: retain the latest 12 completed period summaries and all unresolved ones, with older detailed reconciliation history preserved in Notion before pruning state. Never silently truncate history to fit a connector limit.

Review dates are bookkeeping targets, not supplier payment or partner settlement deadlines. Reuse matching events or an explicitly authorised monthly series. For a completed occurrence, modify that instance only; never silence or mark the entire future series Done. Roll the same card to the next verified occurrence. If incomplete, preserve the period/blockers and surface them at the next review rather than treating an attempted run as completion. Daily Briefing can show the linked review and missing evidence; it must not duplicate the monthly ledger job.
