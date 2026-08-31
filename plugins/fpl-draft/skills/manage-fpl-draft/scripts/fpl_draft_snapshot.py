#!/usr/bin/env python3
"""Build a read-only, league-aware FPL Draft snapshot from public endpoints."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

BASE_URL = "https://draft.premierleague.com"
DEFAULT_ENTRY_ID = 184598
DEFAULT_LEAGUE_ID = 35686
DEFAULT_TIMEOUT = 20.0
DEFAULT_MAX_WORKERS = 16
STATUS_LABELS = {"a": "available", "o": "owned", "l": "locked"}


def fetch_json(path: str, timeout: float = DEFAULT_TIMEOUT) -> Any:
    if not path.startswith("/api/") or ".." in path:
        raise ValueError(f"Refusing non-allowlisted path: {path}")
    request = urllib.request.Request(
        f"{BASE_URL}{path}",
        headers={"Accept": "application/json", "User-Agent": "manage-fpl-draft/1.0"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"GET {path} returned HTTP {exc.code}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"GET {path} failed: {exc.reason}") from exc


def fetch_many(paths: dict[str, str], timeout: float, max_workers: int) -> dict[str, Any]:
    """Fetch independent endpoints concurrently while preserving their labels."""
    if not paths:
        return {}
    with ThreadPoolExecutor(max_workers=min(max_workers, len(paths))) as executor:
        futures = {
            label: executor.submit(fetch_json, path, timeout)
            for label, path in paths.items()
        }
        return {label: future.result() for label, future in futures.items()}


def records(payload: Any, *keys: str) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        for key in keys:
            value = payload.get(key)
            if isinstance(value, list):
                return [item for item in value if isinstance(item, dict)]
    return []


def fixture_records(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if not isinstance(payload, dict):
        return []
    fixtures = payload.get("fixtures", payload)
    if isinstance(fixtures, list):
        return [item for item in fixtures if isinstance(item, dict)]
    if isinstance(fixtures, dict):
        flattened: list[dict[str, Any]] = []
        for value in fixtures.values():
            if isinstance(value, list):
                flattened.extend(item for item in value if isinstance(item, dict))
            elif isinstance(value, dict):
                flattened.append(value)
        return flattened
    return []


def iso_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def current_event(game: Any, bootstrap: Any) -> int:
    candidates: list[Any] = []
    if isinstance(game, dict):
        candidates.extend([game.get("current_event"), game.get("current_event_id"), game.get("event")])
    if isinstance(bootstrap, dict):
        for event in records(bootstrap.get("events", [])):
            if event.get("is_current"):
                candidates.append(event.get("id"))
    for value in candidates:
        try:
            event_id = int(value)
            if event_id > 0:
                return event_id
        except (TypeError, ValueError):
            pass
    raise RuntimeError("Could not determine the current gameweek; pass --event-id")


def parse_date(value: Any) -> dt.datetime | None:
    if not value or not isinstance(value, str):
        return None
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed if parsed.tzinfo else parsed.replace(tzinfo=dt.timezone.utc)
    except ValueError:
        try:
            return dt.datetime.strptime(value[:10], "%Y-%m-%d").replace(tzinfo=dt.timezone.utc)
        except ValueError:
            return None


def load_previous(path: str | None) -> dict[str, dict[str, Any]]:
    if not path:
        return {}
    with Path(path).open(encoding="utf-8") as handle:
        payload = json.load(handle)
    previous_players = payload.get("players", []) if isinstance(payload, dict) else []
    return {
        str(player.get("id")): player
        for player in previous_players
        if isinstance(player, dict) and player.get("id") is not None
    }


def chance(value: Any) -> int | None:
    try:
        return int(value) if value is not None else None
    except (TypeError, ValueError):
        return None


def injury_signals(player: dict[str, Any], previous: dict[str, Any] | None) -> tuple[int, list[str]]:
    score = 0
    signals: list[str] = []
    status = player.get("status")
    next_chance = chance(player.get("chance_next"))
    this_chance = chance(player.get("chance_this"))
    return_date = parse_date(player.get("news_return"))
    if return_date:
        days = (return_date - dt.datetime.now(dt.timezone.utc)).days
        if -7 <= days <= 21:
            score += 3
            signals.append("listed return is within three weeks")
        elif 21 < days <= 42:
            score += 1
            signals.append("listed return is within six weeks")
    is_flagged = status not in {None, "a"}
    if is_flagged and next_chance is not None and next_chance >= 75:
        score += 2
        signals.append(f"next-round chance is {next_chance}%")
    if is_flagged and next_chance is not None and this_chance is not None and next_chance > this_chance:
        score += 2
        signals.append("next-round chance exceeds this-round chance")
    if previous:
        previous_status = previous.get("status")
        previous_chance = chance(previous.get("chance_next"))
        if status == "a" and previous_status != "a":
            score += 5
            signals.append(f"status improved from {previous_status or 'unknown'} to available")
        if next_chance is not None and (previous_chance is None or next_chance > previous_chance):
            score += 4
            signals.append(f"next-round chance rose from {previous_chance} to {next_chance}%")
        old_return = parse_date(previous.get("news_return"))
        if old_return and return_date and return_date < old_return:
            score += 3
            signals.append("listed return date moved earlier")
        if player.get("news") and player.get("news") != previous.get("news"):
            score += 1
            signals.append("injury news changed since the previous snapshot")
    if status in {"i", "d", "u", "s"} and not signals:
        signals.append("unavailable or doubtful with no improving data signal yet")
    return score, signals


def fixture_status(fixture: dict[str, Any]) -> str:
    if fixture.get("finished"):
        return "finished"
    if fixture.get("finished_provisional"):
        return "provisional"
    if fixture.get("started") or int(fixture.get("minutes") or 0) > 0:
        return "live"
    return "scheduled"


def enrich_fixture(fixture: dict[str, Any], team_names: dict[int, str], short_names: dict[int, str]) -> dict[str, Any]:
    enriched = dict(fixture)
    home_id = fixture.get("team_h", fixture.get("home"))
    away_id = fixture.get("team_a", fixture.get("away"))
    enriched.update({
        "home_team": team_names.get(home_id, home_id),
        "home_team_short": short_names.get(home_id, home_id),
        "away_team": team_names.get(away_id, away_id),
        "away_team_short": short_names.get(away_id, away_id),
        "home_score": fixture.get("team_h_score", fixture.get("home_score")),
        "away_score": fixture.get("team_a_score", fixture.get("away_score")),
        "status": fixture_status(fixture),
    })
    return enriched


def next_fixtures_by_team(
    fixtures: list[dict[str, Any]], current_event_id: int,
    team_names: dict[int, str], short_names: dict[int, str],
) -> dict[int, list[dict[str, Any]]]:
    upcoming = [
        fixture for fixture in fixtures
        if int(fixture.get("event") or 0) >= current_event_id
        and not fixture.get("started") and not fixture.get("finished")
    ]
    upcoming.sort(key=lambda item: (
        int(item.get("event") or 999), item.get("kickoff_time") or item.get("time") or "",
        int(item.get("id") or 0),
    ))
    result: dict[int, list[dict[str, Any]]] = {}
    for fixture in upcoming:
        home_id = fixture.get("team_h", fixture.get("home"))
        away_id = fixture.get("team_a", fixture.get("away"))
        for team_id, opponent_id, venue in ((home_id, away_id, "H"), (away_id, home_id, "A")):
            if not isinstance(team_id, int) or len(result.get(team_id, [])) >= 3:
                continue
            result.setdefault(team_id, []).append({
                "event": fixture.get("event"), "fixture_id": fixture.get("id"),
                "kickoff_time": fixture.get("kickoff_time", fixture.get("time")),
                "opponent": team_names.get(opponent_id, opponent_id),
                "opponent_short": short_names.get(opponent_id, opponent_id), "venue": venue,
            })
    return result


def live_by_element(payload: Any) -> dict[str, dict[str, Any]]:
    elements = payload.get("elements", {}) if isinstance(payload, dict) else {}
    if isinstance(elements, dict):
        return {str(key): value for key, value in elements.items() if isinstance(value, dict)}
    return {
        str(item.get("id", item.get("element"))): item for item in records(elements)
        if item.get("id", item.get("element")) is not None
    }


def normalise_player(
    element: dict[str, Any], availability: dict[str, Any],
    team_names: dict[int, str], short_names: dict[int, str],
    position_names: dict[int, str], next_fixtures: dict[int, list[dict[str, Any]]],
) -> dict[str, Any]:
    element_id = int(element["id"])
    team_id = element.get("team")
    full_name = " ".join(
        part.strip() for part in (element.get("first_name") or "", element.get("second_name") or "")
        if part.strip()
    )
    availability_code = availability.get("status")
    return {
        "id": element_id, "name": full_name or element.get("web_name") or str(element_id),
        "web_name": element.get("web_name"), "team": team_names.get(team_id, team_id),
        "team_short_name": short_names.get(team_id, team_id),
        "position": position_names.get(element.get("element_type"), element.get("element_type")),
        "availability": STATUS_LABELS.get(availability_code, availability_code),
        "owner": availability.get("owner"),
        "in_accepted_trade": availability.get("in_accepted_trade", False),
        "status": element.get("status"),
        "chance_this": element.get("chance_of_playing_this_round"),
        "chance_next": element.get("chance_of_playing_next_round"),
        "news": element.get("news"), "news_added": element.get("news_added"),
        "news_updated": element.get("news_updated"), "news_return": element.get("news_return"),
        "form": element.get("form"), "points": element.get("total_points"),
        "draft_rank": element.get("draft_rank"), "minutes": element.get("minutes"),
        "starts": element.get("starts"), "goals": element.get("goals_scored"),
        "assists": element.get("assists"), "clean_sheets": element.get("clean_sheets"),
        "bonus": element.get("bonus"), "xg": element.get("expected_goals"),
        "xa": element.get("expected_assists"),
        "next_three_fixtures": next_fixtures.get(team_id, []),
    }


def enrich_squad(squad: Any, players: dict[str, dict[str, Any]], live: dict[str, dict[str, Any]]) -> Any:
    if not isinstance(squad, dict):
        return squad
    enriched = dict(squad)
    enriched["picks"] = []
    for pick in records(squad, "picks"):
        item = dict(pick)
        element_id = str(pick.get("element"))
        item["player"] = players.get(element_id)
        if element_id in live:
            item["live"] = live[element_id]
        enriched["picks"].append(item)
    return enriched


def positive_float(value: str) -> float:
    parsed = float(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return parsed


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return parsed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entry-id", type=int, default=DEFAULT_ENTRY_ID)
    parser.add_argument("--league-id", type=int, default=DEFAULT_LEAGUE_ID)
    parser.add_argument("--event-id", type=int)
    parser.add_argument("--previous", help="Previous snapshot JSON for change detection")
    parser.add_argument("--output", help="Write JSON to this file instead of stdout")
    parser.add_argument("--pretty", action="store_true")
    parser.add_argument("--timeout", type=positive_float, default=DEFAULT_TIMEOUT)
    parser.add_argument("--max-workers", type=positive_int, default=DEFAULT_MAX_WORKERS)
    return parser


def build_snapshot(args: argparse.Namespace) -> dict[str, Any]:
    base = fetch_many(
        {"bootstrap": "/api/bootstrap-static", "game": "/api/game"},
        args.timeout, args.max_workers,
    )
    bootstrap, game = base["bootstrap"], base["game"]
    event_id = args.event_id or current_event(game, bootstrap)
    payloads = fetch_many({
        "league": f"/api/league/{args.league_id}/details",
        "entry": f"/api/entry/{args.entry_id}/public",
        "element_status": f"/api/league/{args.league_id}/element-status",
        "squad": f"/api/entry/{args.entry_id}/event/{event_id}",
        "transactions": f"/api/draft/league/{args.league_id}/transactions",
        "trades": f"/api/draft/league/{args.league_id}/trades",
        "fixtures": f"/api/event/{event_id}/fixtures",
        "live": f"/api/event/{event_id}/live",
        "match_status": "/api/pl/event-status",
    }, args.timeout, args.max_workers)

    elements = records(bootstrap, "elements")
    teams = records(bootstrap, "teams")
    positions = records(bootstrap, "element_types")
    statuses = records(payloads["element_status"], "element_status", "elements")
    status_by_element = {str(item.get("element")): item for item in statuses}
    team_names = {int(team["id"]): team.get("name") for team in teams}
    short_names = {int(team["id"]): team.get("short_name") or team.get("name") for team in teams}
    position_names = {
        int(item["id"]): item.get("singular_name_short") or item.get("singular_name")
        for item in positions
    }
    next_fixtures = next_fixtures_by_team(
        fixture_records(bootstrap.get("fixtures", [])), event_id, team_names, short_names
    )
    previous = load_previous(args.previous)
    players = [
        normalise_player(element, status_by_element.get(str(element.get("id")), {}),
                         team_names, short_names, position_names, next_fixtures)
        for element in elements if element.get("id") is not None
    ]
    for player in players:
        score, signals = injury_signals(player, previous.get(str(player["id"])))
        player["return_signal_score"], player["return_signals"] = score, signals
    available = [player for player in players if player.get("availability") == "available"]
    return_watch = [
        player for player in available
        if player.get("return_signal_score", 0) > 0 or player.get("status") in {"i", "d", "u", "s"}
    ]
    return_watch.sort(key=lambda player: (
        -int(player.get("return_signal_score") or 0), int(player.get("draft_rank") or 99999)
    ))
    squads_by_owner: dict[str, list[int]] = {}
    for player in players:
        if player.get("owner") is not None:
            squads_by_owner.setdefault(str(player["owner"]), []).append(player["id"])
    players_by_id = {str(player["id"]): player for player in players}
    live_players = live_by_element(payloads["live"])
    fixtures = [enrich_fixture(item, team_names, short_names) for item in fixture_records(payloads["fixtures"])]
    return {
        "generated_at": iso_now(), "source": BASE_URL, "read_only": True,
        "entry_id": args.entry_id, "league_id": args.league_id, "event_id": event_id,
        "entry": payloads["entry"], "league": payloads["league"],
        "current_squad": enrich_squad(payloads["squad"], players_by_id, live_players),
        "squads_by_owner": squads_by_owner, "players": players,
        "available_players": available, "injury_return_watch": return_watch,
        "transactions": payloads["transactions"], "trades": payloads["trades"],
        "fixtures": fixtures, "live_scores": fixtures, "live": payloads["live"],
        "match_status": payloads["match_status"], "game": game,
    }


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    output = build_snapshot(args)
    if args.output:
        with Path(args.output).open("w", encoding="utf-8") as handle:
            json.dump(output, handle, indent=2 if args.pretty else None, ensure_ascii=False)
            handle.write("\n")
    else:
        json.dump(output, sys.stdout, indent=2 if args.pretty else None, ensure_ascii=False)
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
