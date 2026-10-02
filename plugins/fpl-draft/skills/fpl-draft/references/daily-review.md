# Draft daily review

Use this contract for the Draft component of Daily Football Briefing and explicitly requested Draft deadline checks. Read the main FPL Draft skill and its reporting, API and injury-return references. Fetch live data and preserve all existing league verification, evaluation and team-change permissions.


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


## Present the Draft section

Use a distinct `## Draft` heading. Lead with what changed and its practical significance in short natural paragraphs. Keep analysis and necessary evidence, but omit routine operational narration. On quiet days briefly confirm the checks actually completed, with local date/time; never imply complete coverage when sources failed. Do not repeat unchanged recommendations. Include [Dashboard](https://app.notion.com/p/3e0fc8ce55dd81598575e2ac1f649d4d) in every full briefing's Draft section; link the Sheet only when detailed decisions/results add value.

When composed into Daily Football Briefing, match scores and outcome-revealing player detail belong only here, after the spoiler-free News, Results and Upcoming fixtures sections. Keep necessary FPL scoring distinct from real-match scorelines. Respect requests for a completely spoiler-free report throughout. Do not turn an entertainment rating into evidence for a claim.

If the user explicitly requests a deadline check, do this Draft review only when a waiver or lineup deadline is within 12 hours. Otherwise emit `::SKIP_COMPLETION::`. Inside that window deliver only material changes or an undelivered due report; skip if neither exists. Never infer deadline-check mode from the time of day.
