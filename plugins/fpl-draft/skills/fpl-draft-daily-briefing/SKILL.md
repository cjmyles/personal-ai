---
name: fpl-draft-daily-briefing
description: Deliver Craig's FPL Draft Daily Briefing using live league data, injury news, deadlines, recorded decisions, spoiler-free Thrillr ratings and the next Arbroath, Tottenham and Scotland fixtures. Use for the scheduled daily interaction, daily FPL updates and an explicitly requested deadline check. Delegate football analysis and persistence to FPL Draft.
---

# FPL Draft Daily Briefing

Load this skill and its required references from the current `main` branch of `cjmyles/personal-ai` through the connected GitHub app on every run. Resolve relative links against the referring file's repository directory. If canonical instructions cannot be read, report the failure rather than substituting remembered or stale instructions.

Read [FPL Draft](../fpl-draft/SKILL.md), [Reporting and learning](../fpl-draft/references/reporting-and-learning.md), [API reference](../fpl-draft/references/api.md) and [Injury-return waivers](../fpl-draft/references/injury-return-waivers.md). Use the main skill for league identity, live data, player assessment, paired recommendations and team-change permissions. Use the reporting contract for connected assets, record schemas, deduplication, evaluation and failure handling; do not maintain a second implementation here.

## Run mode and authority

Default every invocation to the full daily briefing regardless of its clock time, so changing the app's schedule does not silently change behaviour. Use the app/user-supplied timezone, otherwise Asia/Ho_Chi_Minh. Verify the current local date and time. Treat an authorised scheduled or manual briefing as permission to update the existing analysis Sheet and Notion dashboard, never to mutate the team. Honour preview/review-only requests by making no writes. Publication alone does not authorise a live briefing.

Only use deadline-check mode when explicitly requested. In that mode, skip unless a waiver or lineup deadline falls within the next 12 hours; report only material changes or a due report not previously delivered. Emit `::SKIP_COMPLETION::` when nothing is due or changed, and omit Thrillr. Do not infer this mode from evening timing or create another schedule.

## Select the report from live deadlines

Use official game/fixture data, not weekdays, to identify deadlines and completion. Consider both the ongoing/just-finished gameweek and the next gameweek, combining overlapping reports without duplication.

| Condition | Output |
| --- | --- |
| A completed GW lacks a final review | Final result, league position, transfer/lineup impact, rival releases and still-available standout players. Wait for official final scoring/autosubs; label any earlier summary provisional. |
| Waiver cutoff is within 24 hours and not passed | Prioritised player-in → player-out claims, role/minutes, reason, risk, fallback and deadline. Compare with actual pending pairs when authenticated; otherwise state pending claims were not checked. |
| Waivers processed and lineup lock within 24 hours | Verify completed transfers; give one legal XI, ordered bench, exact changes from current selection and reasons. Explain start versus cameo risk and legal autosub coverage. Check remaining free agents if a material gap exists. |
| GW underway with games or material news since last report | Brief head-to-head score, players/fixtures remaining for both managers, projected autosubs, and important injuries or selection surprises. Distinguish live, provisional and final points. Do not suggest changes to a locked XI. |
| Otherwise | Brief league-position/squad-news/return-radar update only when material. During international breaks continue injury/return and valuable availability checks, without routine fixture filler. |

Check the Runs tab before delivery. Use a deterministic report key `season:league:GW:mode:local-date`; final review uses `season:league:GW:final`. Store source/check timestamps and a short change summary, not the full report. Do not mark delivery successful until the report is ready and writes are confirmed. If persistence fails, report that limitation and avoid a false delivery/checkpoint marker. On retries, upsert by key instead of adding duplicates. Avoid routine no-change Sheet rows and Notion edits; always deliver a visible completion or coverage-gap status for a daily briefing.

At each daily briefing run, refresh live ownership, squad, deadlines and transactions. Compare the previous Players rows before updating them. Review all obtainable flagged players and previously injured players whose flag cleared, not just high-form names. Research positive return-stage changes and check Craig's injured players. Preserve source dates and uncertainty; do not claim exhaustive authoritative coverage if incomplete.

## Deliver the daily interaction

Use British English and concise, decision-led output. Always deliver a visible response for a daily briefing, including during international breaks and quiet days. Do not use `::SKIP_COMPLETION::` for a full daily briefing. When all checks succeed without material changes, say “Checked [local date, time]: no material changes to your squad, league transactions or verified player news.” Name only completed checks and disclose missing coverage instead of implying success. Do not repeat unchanged recommendations or include full tables unless requested. Present actual pending pairs before any proposed changes; if private claims cannot be read, say so. Distinguish assistant recommendations, user choices and official transactions.

Continue useful read-only analysis if persistence fails, report the failed asset, and never falsely mark a run saved or create replacement assets. Apply the main skill's injury-return scan and transfer-window signing sweep; a quiet day must not suppress new Thrillr ratings.

## Thrillr ratings

Check Craig’s site https://www.itsathrillr.com/ on every daily briefing run, including international breaks. Include new ratings for completed English Premier League matches and senior first-team competitive international football (e.g. Nations League, World Cup/continental tournaments and their qualifiers). Exclude all friendlies, youth/age-group matches including U23/Olympic age-restricted football, reserves/B teams and other club competitions. Verify competition and senior-team identity; do not infer eligibility from a country name alone.

Read the live public site, not cached search snippets. The public HTML includes match ratings, match links and a date filter (/?date=YYYY-MM-DD); fetch full HTML with public GET if web extraction fails. Use the last successfully delivered full briefing's cutoff from Runs as the start of the match window, ending at this run's start time. Include only eligible matches completed within that window; newly published or revised ratings for older matches do not qualify. Fetch the date-filter pages needed to cover that interval, including overnight matches, rather than using a rolling 72-hour lookback. Verify match completion timing where the boundary matters; do not treat a rating publication date as the match date. If there is no reliable checkpoint, use the preceding 24 hours and state that fallback briefly. Read the site’s actual final rating and scale; do not invent a score or denominator, replace it with a prediction, or treat a live/provisional rating as final. If access or final ratings are unavailable, say so briefly.

Place a compact “Thrillr — spoiler-free ratings” section before any Draft performance/news that could reveal match events. Show each newly rated eligible match, local match date, exact site rating and direct match link, highest rating first. Include all eligible new ratings, without imposing an unrequested minimum rating. Reveal no result, winner, scoreline, scorer, incident or outcome hint in this section. Keep it separate from FPL player assessments: entertainment ratings are not evidence for player quality or waiver recommendations. Use existing Runs headers and short Material summary notes to remember delivered match IDs/URLs and ratings; no new tab, full-report append or Notion expansion. On retries avoid duplicate ratings. After successful delivery, upsert one reusable `thrillr:last-successful-briefing` checkpoint in Runs using its existing headers: Checked UTC is the run-start cutoff, Report delivered is Yes, and Material summary holds compact delivered match IDs/ratings. Advance it even when there are no eligible games, so quiet days do not widen the next report's window. This single checkpoint is an exception to avoiding no-change rows; do not append daily no-change history. Failed Thrillr checks or undelivered reports must not advance it. If persistence is unavailable, disclose that the cutoff could not be saved.

When there are no new eligible ratings, add only “Thrillr: no new eligible ratings.” alongside the daily completion confirmation or Draft update. A quiet Draft day must not suppress new Thrillr ratings. Explicit deadline checks do not run the Thrillr review.

## Next fixtures

Include the next scheduled match for each of Arbroath FC, Tottenham Hotspur and Scotland senior men's first teams in every full daily briefing, with no maximum look-ahead window. Verify fresh official club, competition or association fixture listings; do not infer the next match from league fixtures alone. Include the opponent, home/away, competition, date and kick-off in the resolved reporting timezone, with a direct source link. Include all first-team competitions, including friendlies; the Thrillr eligibility exclusions do not apply to this fixture section. If no fixture or kick-off is confirmed, say so rather than guessing. Keep this to one compact row per team, and identify postponements or changed kick-off times. Omit it in explicit deadline-check mode.

## Scheduling

Keep all workflow instructions in this skill and its references. Manage frequency, run time, timezone and enabled status only in the app; do not mirror them in a repository schedule file. Resolve the existing automation by the title `FPL Draft Daily Briefing` before updating it, and never create a duplicate. Reading or publishing this skill does not authorise a run or schedule change.

To recreate a deleted event when Craig requests it, verify required connector access, use the title above and the invocation below, and use Craig's chosen timing in the app. Do not infer the latest schedule from repository history. A repository edit does not change a live event.

> Read https://github.com/cjmyles/personal-ai/blob/main/plugins/fpl-draft/skills/fpl-draft-daily-briefing/SKILL.md through the connected GitHub app and run the briefing, loading its required skills and references from the same repository. If the canonical instructions cannot be read, report that failure rather than using remembered or stale instructions.
