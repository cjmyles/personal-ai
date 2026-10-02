# Private configuration and run state

Use the existing property reconciliation card (initially Wentworth St Reconciliation). Read dedicated checklists. Keep the following private configuration on the card:

- Property identity, jurisdiction/timezone, agent/payer aliases and source references.
- Reconciliation Notion page URL and related task/source-workbook links.
- Automation ID and recovery timing; the automation app is authoritative for cadence.
- Linked reminders JSON under the Personal Todo contract, with calendar IDs, event/series IDs, URLs, stable occurrence keys, review dates and status.
- Property reconciliation state JSON: schema_version, last_run_started_utc, last_successful_period, periods (period, status, checks, missing_evidence, source_keys, verified_changes), last_result and pending_repairs.

Initialise last_successful_period as null unless complete historical verification exists. Read all unresolved periods on every run. Stable keys prevent duplicate records on retries, but recheck revised statements and unresolved evidence. A partial save or partial period never advances successful completion past an unresolved earlier period.

Write the Notion record first, verify, then the Trello/Calendar pair and verify, then save state. Re-read and merge concurrent changes. Record partial successes and stable IDs for repair rather than repeating creates. Report failed state saves. Retain 12 completed summaries and all pending periods; archive older detail in the linked Notion record before pruning compact state. Preserve dated card history; never truncate it to fit a limit.

Review dates are administrative targets, not rent due dates or supplier payment deadlines. For a recurring series, update only the completed instance, preserve future notifications and manual changes, and roll the open card to the next actual review. Keep unresolved periods visible on the card when rolling forward. Use seven-day and two-day notifications, with the linked-reminders imminent-event rule for the first review. The Daily Briefing can surface this card and reminders; it should not duplicate the full monthly reconciliation.
