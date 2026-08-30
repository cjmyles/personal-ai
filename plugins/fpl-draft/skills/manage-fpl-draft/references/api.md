# Premier League Fantasy Draft Data

Base URL: `https://draft.premierleague.com`

The Draft API is used by the official site but is not a stable, documented public developer API. Recheck behaviour when the site changes.

## Public Read Endpoints

| Purpose | Method and path | Useful fields |
| --- | --- | --- |
| Player and team metadata | `GET /api/bootstrap-static` | `elements`, `teams`, `element_types`; player `status`, `news`, `news_return`, playing chances, form and rank |
| Current game state | `GET /api/game` | Current event, deadlines and game state |
| Entry profile | `GET /api/entry/{entry}/public` | Entry name, manager and league references |
| League and standings | `GET /api/league/{league}/details` | League settings, entries, standings and waiver information |
| Ownership and availability | `GET /api/league/{league}/element-status` | `element`, `owner`, `status`, `in_accepted_trade` |
| Entry gameweek squad | `GET /api/entry/{entry}/event/{event}` | Picks, points and gameweek state |
| League transactions | `GET /api/draft/league/{league}/transactions` | Player in/out, entry, event, kind, priority, result and timestamps |
| League trades | `GET /api/draft/league/{league}/trades` | Trade history and status |
| Fixtures | `GET /api/event/{event}/fixtures` | Kick-off, teams, status and scores |
| Live player scores | `GET /api/event/{event}/live` | Gameweek stats, points and explain data |
| Player history | `GET /api/element-summary/{element}` | Past and future fixtures and player history |
| Match status | `GET /api/pl/event-status` | Data checked and match status |

Element-status values observed on the official site:

- `a`: Available to claim
- `o`: Owned
- `l`: Locked

Treat the server response as authoritative if new values appear.

## Signed-In Read Endpoints

| Purpose | Method and path |
| --- | --- |
| Signed-in season and entry state | `GET /api/bootstrap-dynamic` |
| Current private team | `GET /api/entry/{entry}/my-team` |
| Pending and historical entry transactions | `GET /api/draft/entry/{entry}/transactions` |
| Current trades | `GET /api/draft/entry/{entry}/trades/current` |
| Trades awaiting approval | `GET /api/draft/entry/{entry}/trades/for-approval` |

The official site injects an `X-API-Authorization: Bearer ...` header from its signed-in account session. Use the browser's existing session. Never copy the token into a skill, script, note, terminal command or response.

## Write Endpoints Observed in Normal UI

These are listed so read-only inspection can recognise them. Do not call them merely to test a payload.

| Action | Observed request |
| --- | --- |
| Save line-up | `POST /api/entry/{entry}/my-team` |
| Free-agent move | `POST /api/draft/entry/{entry}/free-agency` |
| Submit waivers | `POST /api/draft/entry/{entry}/waivers` |
| Watchlist change | `POST /api/watchlist/{entry}` |
| Trade actions | `POST` or `DELETE` under `/api/draft/entry/{entry}/trades/...` |

Write payloads and CSRF/session behaviour can change. Only use the normal signed-in UI after explicit user approval for the exact mutation.

## Response Joins

- Join player IDs from `element-status`, picks and transactions to `bootstrap-static.elements.id`.
- Join team IDs to `bootstrap-static.teams.id`.
- Join `owner` to league entry IDs to reconstruct rival squads.
- A recommendation pool contains only `status == "a"`; display locked players separately.
- Use transactions to understand recent claims, drops and rival intent.
- Use repeated snapshots to identify improving injury and availability signals.
