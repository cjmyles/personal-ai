# Reports and decision learning

## Connected assets

- Google Sheet: `1JrauLxOESM6MO--1jzzkNhR7J4GtN97QjAWRxKKfQ1E` — https://docs.google.com/spreadsheets/d/1JrauLxOESM6MO--1jzzkNhR7J4GtN97QjAWRxKKfQ1E/edit
- Notion dashboard: `3e0fc8ce-55dd-8159-8575-e2ac1f649d4d` — https://app.notion.com/p/3e0fc8ce55dd81598575e2ac1f649d4d
- Legacy Library tracker: `libfile_579f567e31908191a001d1e369f3e01f`, `/D-Raft-player-tracker.md`. Historical context only after migration on 19 September 2026; do not maintain a second current tracker.

The Sheet is the canonical structured record. Notion is one ordinary page, not a database: use direct page fetch and targeted text updates, avoiding database queries and repeated workspace searches. Read the existing page before editing. Use the Google Sheets skill for bounded reads and edits. Preserve manual notes, formulas, identities and older decisions.

## Select the report from live deadlines

Use [Daily Football Briefing](../../daily-football-briefing/SKILL.md) for the combined report and [Draft daily review](daily-review.md) for Draft report selection and deadline-check mode. Results and news each own a reusable delivery checkpoint in Runs. Scheduling is controlled only in the app. For an ad hoc request, answer the requested question using the analysis and record rules below.

## Sheet contract

Read metadata and exact headers first. Never recreate the workbook to refresh it. Read the smallest required ranges, batch changes and expand bounds only as data grows. All timestamps in columns labelled UTC are UTC; report deadlines to Craig in Vietnam time. Player IDs are season-specific: when the official season changes, explicitly separate the new season and re-resolve the league/entry before reusing records.

| Tab | Grain and update rule |
| --- | --- |
| Players | One row per current-season player ID. Current official ownership, Draft rank, previous-season points, season stats, fixtures and fitness; latest assessment, return stage, first-start outlook and dated evidence. Update changed values only. Preserve research fields and historical totals unless superseded. Unknown historical points stay blank, never zero. |
| Decisions | One immutable recommendation version per transfer, hold, watch or lineup decision. Store timestamp, GW, exact players (including IDs in the decision key), priority, rationale, evidence, risk, fallback and evaluation horizon before play. Record prospective versus retrospective basis. Changed advice gets a new version and reason, never rewrites the original reasoning. N:S contain one- and four-GW points comparisons; extend the existing blank-safe delta formulas when appending. T holds dated evidence and later review notes. |
| Transactions | One official transaction ID, league-wide. Preserve raw kind/result and actual priority. Accepted result `a` means completed; failed/skipped/pending are distinct. The API's `added` timestamp is a record timestamp, not proof of execution time. Pending browser-only requests use an explicitly pending key and status; reconcile to official IDs when processed. Cancellation is recorded separately, not as a completed move. |
| Lineups | One `season:GW:entry:slot:selection-version` record. Separate recommended, submitted-before-lock and official locked selection in Record basis. Preserve pre-autosub starters/bench; later fill final minutes/points and autosub outcome. Never label current public picks a future submitted XI unless the endpoint actually provides it. |
| Reviews | One GW result and concise evaluation. Separate player-points differences from points actually counted in Craig's XI and from head-to-head impact. Preserve unresolved gaps. |
| Runs | One report/checkpoint key with mode, checked time, delivered state and short material summary. Keep the latest transaction cursor and next due report here. Avoid routine no-change rows; retain enough delivery keys to prevent duplicate reports. |

Persist complete decisions in the Sheet; keep the Notion page short: current position/deadlines, actionable changes, squad rank/prior-season points, a small return watch and latest review. Change only affected rows or paragraphs. Never append daily reports or copy the entire Sheet into Notion. Link the Sheet for detail. A player being on the watchlist is not a recommendation or approval to release someone.

## Evaluate decisions without hindsight

Import verifiable transactions and historical results, but label reconstructed rationale `Retrospective backfill`; do not manufacture pre-match predictions. An unexecuted recommendation can be evaluated as a hypothetical only, never as an actual team gain. Capture actual user choices separately from assistant advice.

For each executed move, compare incoming and outgoing points in its first eligible GW and over that GW plus the next three official GWs, counting all fixtures in doubles and zero fixtures in blanks. Never use four calendar weeks. Fill comparisons only when both sides and scoring are final. For swaps made after a lock, begin at the next eligible GW. Keep actual selected points/automatic substitutions separate; a benched return did not improve that week's team score. Compare rejected alternatives only if they were genuinely obtainable at the decision time.

Assess minutes, starts, role and injury assumptions as well as points. One unlucky result does not prove a bad decision. Retain a stable core of proven players; use replaceable slots for genuine improvements and multi-week fixture opportunities. Weigh rank, prior-season scoring, role changes, rival demand and losing the outgoing player permanently. International breaks can reduce the number of matches missed by an injury stash; count missed fixtures, not just days. Claiming an early return and starting that player immediately are separate decisions.

Summarise recurring lessons with sample sizes in Reviews. This is an evidence log and calibration process, not a trained machine-learning model. Do not claim statistical learning from four retrospective examples. Propose changes to recommendation rules when repeated evidence supports them, record the rule version and evaluate future decisions separately. Do not automatically rewrite or publish the skill from a scheduled report.

## Sources and failures

Use official Draft data for market state. For history, try Draft element-summary, then official Classic FPL bootstrap and element-summary, matching player identity/code and season rather than assuming IDs agree. Prior totals inform rank but are not its definition. Club/manager reporting is primary for injury and role. Reddit and Win Your Draft League Substack are discovery/ranking inputs, not ownership or medical confirmation; read accessible current articles, verify factual claims, and disclose inaccessible/paywalled content without bypassing access controls.

If live ownership fails, do not assert availability or recommend a verified claim. If Sheets or Notion fails, continue useful read-only analysis and state precisely what was not persisted; do not create replacement assets. If authenticated access fails, public data may still support analysis, but do not claim pending requests were checked. Persisting analysis does not authorise waivers, transfers, trades, watchlist or lineup mutations.
