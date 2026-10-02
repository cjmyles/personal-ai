---
name: daily-football-briefing
description: Deliver Craig's Daily Football Briefing with verified news, spoiler-free results and entertainment ratings, upcoming Arbroath/Tottenham/Scotland fixtures, and league-aware FPL Draft advice. Use for scheduled or requested daily football briefings, including the former Daily FPL or FPL Draft Daily Briefing.
---

# Daily Football Briefing

Read this skill and every required sibling/reference from current `main` in `cjmyles/personal-ai` through the connected GitHub app on every run. Resolve relative links from each file's repository directory. If canonical instructions cannot be read, report the failure rather than running remembered or stale instructions. For an explicitly requested offline development preview only, local candidate skills and supplied facts may be used: label the output a preview, do not claim live checks, and make no production writes or checkpoint advances.

## Compose specialist skills

Load all four components for a full briefing:

- [Football News](../football-news/SKILL.md): current verified stories and editorial significance.
- [Football Results](../football-results/SKILL.md): live Thrillr ratings for eligible completed games since the last successful briefing.
- [Football Fixtures](../football-fixtures/SKILL.md): the next match for each followed team, without a look-ahead limit.
- [FPL Draft](../fpl-draft/SKILL.md) and its [daily review](../fpl-draft/references/daily-review.md), [reporting and learning](../fpl-draft/references/reporting-and-learning.md), [API](../fpl-draft/references/api.md) and [injury-return](../fpl-draft/references/injury-return-waivers.md) references: live league analysis and existing records.

These are specialised skills in one Football plugin. Keep rules in their owning component; do not duplicate fetching or persistence implementations in this orchestration skill. Reuse relevant fetched evidence across sections while keeping entertainment ratings separate from Draft player assessment.

## Authority and run mode

Default to the full briefing regardless of clock time. Resolve date/time in the app/user-supplied timezone, otherwise Asia/Ho_Chi_Minh; capture run start once for cutoff calculations. An authorised scheduled or manual briefing permits minimal updates to the existing Sheet and Notion analysis assets, never team mutations. Preview/review-only requests make no writes or checkpoint advances. Publication alone does not authorise running the briefing.

Only an explicitly requested deadline check switches to the Draft-only 12-hour mode in the daily-review reference. Omit news/results/fixtures in that mode. Never create another schedule during a run.

## Editorial output

Use these exact level-two headings, in this order:

1. `## News`
2. `## Results`
3. `## Upcoming fixtures`
4. `## Draft`

Write like a concise football correspondent: lead News with the most consequential verified development, explain why it matters, and connect related stories naturally. Use British English, short paragraphs and specific facts. Do not write a tool log, a generic greeting, a breathless teaser or a list of disconnected headlines. Usually two to four brief stories suffice; include fewer on quiet days. Never manufacture a lead to fill space.

Keep News, Results and Upcoming fixtures spoiler-free: no scores, winners, scorers, decisive incidents, qualification outcomes or result hints, including copied source titles and link labels. Describe the best-rated games as viewing recommendations based on actual ratings; do not infer the sort of action from a rating. Put outcome-dependent analysis only in the clearly separated final Draft section. Avoid repeating a player-news paragraph in both News and Draft; put the practical team implication in Draft.

Use matching table conventions: Results is `Game | Competition | Rating`; Upcoming fixtures is `Game | Competition | Date`. Write `Home team vs Away team` in both, with game names linking to the match or official fixture source. Results has no date column; Date in Upcoming fixtures includes local date and kick-off time. State the reporting timezone once beside the fixture table, not in its heading. Display the verified rating scale in the Rating header or cells. Do not add a separate Match, Team or Opponent column.

Results starts with at most one short sentence identifying the highest-rated viewing options, then every newly eligible rating in descending order. Use the heading Results, not Thrillr; source attribution belongs in the game links. Do not show dated older matches again to fill a quiet day.

Draft gets a proper heading, a human explanation of the meaningful team implications, any urgent action/deadline, and a direct [Dashboard](https://app.notion.com/p/3e0fc8ce55dd81598575e2ac1f649d4d) link. Use tables for actual comparisons or claims when helpful, not routine status prose. Preserve all required risk/evidence details for actionable recommendations.

Always deliver a visible full briefing, even during international breaks. A quiet component gets one short honest status line. A failed component must not suppress useful independent sections; name the failed check briefly and never call it unchanged. Keep source/coverage limitations concise and specific. Do not repeat internal metadata, run mechanics or routine save narration.

## Delivery and records

Use the existing Sheet and ordinary Notion page from the reporting contract; no new database, workbook, tracker or report archive. Read Runs before composing to avoid repeated stories/ratings and duplicate Draft reviews. The Results skill owns `thrillr:last-successful-briefing`; the News skill owns `football-news:last-successful-briefing`. Preserve existing checkpoint identities and timestamps during migration. Full reports never go into Runs or Notion.

Finish source checks and prepare the response, then perform and verify required writes. Only then mark the corresponding report/checkpoint ready for delivery. Do not advance a failed component's checkpoint. On a retry upsert keys, do not append duplicates. Routine unchanged Draft checks need no history row; the reusable component checkpoint rows may advance to keep the next interval correct. If a write fails, continue the useful report and disclose what was not saved.

## Scheduling and compatibility

The app alone controls timing, frequency, timezone and enabled status. Do not mirror its schedule in repository files. Resolve the existing `Daily Football Briefing` event, or its previous title `FPL Draft Daily Briefing`, and update it in place when authorised; never create a duplicate. Preserve current timing unless Craig requests a change. The old skill path remains a redirect so saved prompts keep working.

Use this invocation when updating or recreating the event on request:

> Read https://github.com/cjmyles/personal-ai/blob/main/plugins/fpl-draft/skills/daily-football-briefing/SKILL.md through the connected GitHub app and run the briefing, loading its required skills and references from the same repository. If the canonical instructions cannot be read, report that failure rather than using remembered or stale instructions.
