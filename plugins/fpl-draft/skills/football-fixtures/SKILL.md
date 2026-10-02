---
name: football-fixtures
description: Verify the next senior men's first-team fixture for Arbroath, Tottenham and Scotland with competition, venue order and local kick-off time. Use for Daily Football Briefing Upcoming fixtures or standalone next-game requests, without a maximum look-ahead window.
---

# Football Fixtures


Include the next scheduled match for each of Arbroath FC, Tottenham Hotspur and Scotland senior men's first teams in every full daily briefing, with no maximum look-ahead window. Verify fresh official club, competition or association fixture listings; do not infer the next match from league fixtures alone. Include the opponent, home/away, competition, date and kick-off in the resolved reporting timezone, with a direct source link. Include all first-team competitions, including friendlies; the Thrillr eligibility exclusions do not apply to this fixture section. If no fixture or kick-off is confirmed, say so rather than guessing. Keep this to one compact row per team, and identify postponements or changed kick-off times. Omit it in explicit deadline-check mode.


Use the exact heading `## Upcoming fixtures` and table `Game | Competition | Date`. Game is a direct source link labelled `Home team vs Away team`, so venue is clear without Team/Opponent columns. Date includes weekday, local calendar date and kick-off; name the resolved reporting timezone once above the table. Convert across midnight and daylight-saving changes correctly. Order by kickoff. Retain one next game per followed team; if two followed teams meet, use one shared row. Do not show past results or outcome hints. If a fixture is postponed, look for the next confirmed match and explain the change briefly. Do not create calendar events or alter schedules.
