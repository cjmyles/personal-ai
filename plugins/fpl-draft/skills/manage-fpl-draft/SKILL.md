---
name: manage-fpl-draft
description: "Manage Craig's Premier League Fantasy Draft team with league-aware weekly analysis. Use for FPL Draft squad reviews, starting XI and bench order, waiver and free-agent recommendations, injury-return watchlists, player availability, rival squads, fixtures, transactions, trades, and waiver planning. This is Draft, not budget-based Fantasy Premier League: players are exclusive to one manager and recommendations must be based on who is actually obtainable in the league."
---

# Manage FPL Draft

Treat Premier League Fantasy Draft as a closed player market. A strong player who is owned by a rival is not a waiver recommendation. Prices, budgets, captaincy and ordinary FPL transfer logic do not apply.

## Craig's League

- Entry ID: `184598`
- League ID: `35686`
- League name: `D-Raft`
- Format: Head-to-head, six managers
- Transactions: Waivers, free agency and trades

Confirm these values from live data when possible because league membership and season identifiers can change.

## Start With Live Data

1. Use the signed-in in-app browser when the task needs Craig's current team, pending waivers, trade inbox or another authenticated view.
2. Use `scripts/fpl_draft_snapshot.py` for repeatable public league data. It retrieves allowlisted `GET` endpoints concurrently and includes enriched squads, season statistics, next-three fixtures, live scores and match status; it never authenticates or mutates the team.
3. Read `references/api.md` before inspecting the website or calling Draft endpoints directly.
4. Treat the live Draft site as authoritative for ownership, deadlines, accepted transactions and league rules.
5. Use current, authoritative football reporting for injury progress, training returns, suspensions and likely minutes when the Draft feed is unclear or stale. Separate reported facts from inference.

Example snapshot command:

```bash
python3 scripts/fpl_draft_snapshot.py --entry-id 184598 --league-id 35686 --pretty
```

Use `--timeout` to change the per-request timeout and `--max-workers` to bound concurrent requests (default `16`).

To spot improving injury signals, save snapshots and compare the newest one with the previous file:

```bash
python3 scripts/fpl_draft_snapshot.py --entry-id 184598 --league-id 35686 --previous previous.json --pretty
```

## Weekly Workflow

1. Establish the current gameweek, deadline, waiver processing time and whether free agency is open.
2. Determine whether an official Premier League transfer window is open or closed within the previous 72 hours. Only in that period, compare the newest snapshot with the preceding snapshot and review every player in `new_players_since_previous` and `changed_players_since_previous`, prioritised by Draft rank.
3. During that same transfer-window period, check official Premier League and club transfer announcements since the preceding review. Track credible imminent arrivals separately until they appear in the Draft player pool; registration lag is not a reason to omit them. Skip this signing sweep outside the window unless the user asks or the snapshot unexpectedly contains a new high-ranked player.
4. Retrieve Craig's squad, every rival squad available, player ownership/status, recent transactions and current pending requests where authenticated access permits.
5. Build the obtainable pool from players marked available. Keep locked and rival-owned players separate.
6. Review injuries, suspensions, expected minutes, fixture quality, role, set pieces, form and medium-term upside.
7. Read `references/injury-return-waivers.md` and produce an injury-return watchlist before ranking ordinary waiver options.
8. Recommend claims as paired moves: player in, player out, reason, timing, fallback and suggested waiver priority.
9. Recommend a starting XI and ordered bench after accounting for injury uncertainty and fixture timing.
10. Recheck late news close to the relevant deadline when the user asks for a final decision.

## New Signing Edge

Treat newly signed or newly registered players as a separate time-sensitive market only while an official Premier League transfer window is open and for 72 hours after it closes, allowing for Draft registration lag. Verify the season's official opening and closing dates rather than assuming them. Within that period, scan official transfer announcements and the Draft registration feed daily when practical; the ordinary Monday/Thursday injury cadence is insufficient. Outside it, do not run a routine signing scan. For every arrival:

- Record announcement date, Draft registration status, Draft rank, position and league availability
- Assess likely role, route to starts, recent minutes at the previous club and expected adaptation time
- Alert immediately when a high-upside player becomes available, particularly anyone entering the top 100 Draft ranks
- If already claimed, identify the successful manager and transaction time so the process failure is visible
- Never wait for an injury-focused review before surfacing a significant new signing

## Waiver Decisions

Rank obtainable players by marginal value over Craig's likely drop, not by reputation alone. Consider:

- Expected minutes over the next four to six gameweeks
- Role quality, set pieces and attacking or clean-sheet involvement
- Fixture run and postponement or rotation risk
- Scarcity by position and replacement quality in the free-agent pool
- Rival needs and likelihood that another manager will claim the player
- Craig's waiver priority and the opportunity cost of spending it now
- Stash cost: bench space, uncertainty and how long value may take to arrive

Prefer conditional recommendations when team news is unresolved. Give at least one fallback for an important claim. Do not recommend dropping a player without checking whether the move would leave a legal squad and whether the outgoing player is likely to be claimed immediately.

## Injury-Return Edge

The main edge is often claiming a valuable player before the Draft market fully reacts. Look for changes, not merely an injury flag:

- Return date moving nearer or becoming more specific
- Chance of playing increasing between snapshots
- Status improving from unavailable to doubtful or available
- Return to individual work, partial training, full training or the matchday squad
- Manager comments that clarify rehabilitation or expected minutes
- A substitute appearance followed by a plausible route to starts
- A favourable fixture run beginning near the expected return

Do not equate medical clearance with immediate fantasy value. Assess match fitness, competition for places, managed minutes, recurrence risk and whether the player still has the same role. Label speculative stashes clearly.

## Output

Lead with the decision. Identify every player with their current full club name and position. Do not rely on a badge, shirt image, abbreviation or earlier context to convey the club.

For a standard weekly review, present three compact tables before suggesting any paired moves. Add `New signings and registrations` as the first table only during the transfer-window monitoring period or when a material new player is detected:

- Conditional `New signings and registrations`: Every relevant arrival or newly registered player since the preceding review, including players not yet obtainable, with club, position, Draft rank, registration/ownership state, likely role and action timing.
1. `Craig's squad`: Player, Club, Position, recent form and minutes, next three fixtures with `(H)` or `(A)`, fitness or role, and `Hold`, `Monitor`, `Open to swap` or `Priority problem`.
2. `Available players`: Only genuinely obtainable players, with the same club, position, form, minutes and next-three-fixture fields, plus role risk and `Claim soon`, `Watch`, `Free-agency option` or `Avoid`.
3. `Injury-return radar`: Player, Club, Position, injury, expected return, individual/partial/full training or match involvement, evidence date and source, first-start outlook, and action timing.

Use full club names in the `Club` column. Opponent abbreviations are acceptable in the fixture column when each fixture still shows home or away. State the form window and data timestamp. Where the latest gameweek is unfinished, identify the affected players and treat their form as provisional.

Keep player assessment separate from replacement selection. Do not force player-in/player-out pairings in the initial review unless the user asks for moves or has identified expendable players. When paired waivers are requested, state:

1. `In`: Obtainable player.
2. `Out`: Craig's player to release.
3. `Priority`: Suggested order or whether to wait for free agency.
4. `Why now`: The time-sensitive edge, especially an improving injury signal.
5. `Risk`: Minutes, recurrence, rotation or evidence uncertainty.
6. `Fallback`: Next claim if the preferred player is taken.

Distinguish confirmed data, credible reporting and your inference. Include the data timestamp and flag anything that could change before the deadline.

## Safety

- Advice and read-only inspection do not authorise changes.
- Never submit, reorder or cancel waivers; add or release players; propose, accept or reject trades; change a line-up; or alter a watchlist without the user's explicit approval for that action.
- Before an approved mutation, restate the exact player in, player out, priority and affected gameweek, then verify the live page still matches.
- Never reveal, save or log bearer tokens, cookies or other session credentials.
- Prefer normal signed-in UI actions over replaying private write requests.
- If an endpoint or payload is uncertain, stop at a recommendation rather than experimenting against the live team.
