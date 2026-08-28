#!/usr/bin/env python3
"""Build a read-only, league-aware FPL Draft snapshot from public endpoints."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


BASE_URL = "https://draft.premierleague.com"
DEFAULT_ENTRY_ID = 184598
DEFAULT_LEAGUE_ID = 35686
STATUS_LABELS = {"a": "available", "o": "owned", "l": "locked"}


def fetch_json(path: str) -> Any:
    if not path.startswith("/api/") or ".." in path:
        raise ValueError(f"Refusing non-allowlisted path: {path}")
    request = urllib.request.Request(
        f"{BASE_URL}{path}",
        headers={"Accept": "application/json", "User-Agent": "manage-fpl-draft/1.0"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"GET {path} returned HTTP {exc.code}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"GET {path} failed: {exc.reason}") from exc


def records(payload: Any, *keys: str) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        for key in keys:
            value = payload.get(key)
            if isinstance(value, list):
                return [item for item in value if isinstance(item, dict)]
    return []


def iso_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def current_event(game: Any, bootstrap: Any) -> int:
    candidates: list[Any] = []
    if isinstance(game, dict):
        candidates.extend(
            [game.get("current_event"), game.get("current_event_id"), game.get("event")]
        )
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
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=dt.timezone.utc)
        return parsed
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

    is_currently_flagged = status not in {None, "a"}
    if is_currently_flagged and next_chance is not None and next_chance >= 75:
        score += 2
        signals.append(f"next-round chance is {next_chance}%")
    if (
        is_currently_flagged
        and next_chance is not None
        and this_chance is not None
        and next_chance > this_chance
    ):
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


def normalise_player(
    element: dict[str, Any],
    availability: dict[str, Any],
    team_names: dict[int, str],
    position_names: dict[int, str],
) -> dict[str, Any]:
    element_id = int(element["id"])
    availability_code = availability.get("status")
    return {
        "id": element_id,
        "name": element.get("web_name") or element.get("second_name") or str(element_id),
        "team": team_names.get(element.get("team"), element.get("team")),
        "position": position_names.get(element.get("element_type"), element.get("element_type")),
        "availability": STATUS_LABELS.get(availability_code, availability_code),
        "owner": availability.get("owner"),
        "in_accepted_trade": availability.get("in_accepted_trade", False),
        "status": element.get("status"),
        "chance_this": element.get("chance_of_playing_this_round"),
        "chance_next": element.get("chance_of_playing_next_round"),
        "news": element.get("news"),
        "news_added": element.get("news_added"),
        "news_updated": element.get("news_updated"),
        "news_return": element.get("news_return"),
        "form": element.get("form"),
        "points": element.get("total_points"),
        "draft_rank": element.get("draft_rank"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entry-id", type=int, default=DEFAULT_ENTRY_ID)
    parser.add_argument("--league-id", type=int, default=DEFAULT_LEAGUE_ID)
    parser.add_argument("--event-id", type=int)
    parser.add_argument("--previous", help="Previous snapshot JSON for change detection")
    parser.add_argument("--output", help="Write JSON to this file instead of stdout")
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    bootstrap = fetch_json("/api/bootstrap-static")
    game = fetch_json("/api/game")
    event_id = args.event_id or current_event(game, bootstrap)
    league = fetch_json(f"/api/league/{args.league_id}/details")
    entry = fetch_json(f"/api/entry/{args.entry_id}/public")
    element_status_payload = fetch_json(f"/api/league/{args.league_id}/element-status")
    squad = fetch_json(f"/api/entry/{args.entry_id}/event/{event_id}")
    transactions = fetch_json(f"/api/draft/league/{args.league_id}/transactions")
    trades = fetch_json(f"/api/draft/league/{args.league_id}/trades")
    fixtures = fetch_json(f"/api/event/{event_id}/fixtures")

    elements = records(bootstrap, "elements")
    teams = records(bootstrap, "teams")
    positions = records(bootstrap, "element_types")
    statuses = records(element_status_payload, "element_status", "elements")
    status_by_element = {str(item.get("element")): item for item in statuses}
    team_names = {int(team["id"]): team.get("short_name") or team.get("name") for team in teams}
    position_names = {
        int(position["id"]): position.get("singular_name_short") or position.get("singular_name")
        for position in positions
    }
    previous = load_previous(args.previous)

    players = [
        normalise_player(element, status_by_element.get(str(element.get("id")), {}), team_names, position_names)
        for element in elements
        if element.get("id") is not None
    ]
    for player in players:
        score, signals = injury_signals(player, previous.get(str(player["id"])))
        player["return_signal_score"] = score
        player["return_signals"] = signals

    available = [player for player in players if player.get("availability") == "available"]
    return_watch = [
        player
        for player in available
        if player.get("return_signal_score", 0) > 0 or player.get("status") in {"i", "d", "u", "s"}
    ]
    return_watch.sort(
        key=lambda player: (
            -int(player.get("return_signal_score") or 0),
            int(player.get("draft_rank") or 99999),
        )
    )

    squads_by_owner: dict[str, list[int]] = {}
    for player in players:
        owner = player.get("owner")
        if owner is not None:
            squads_by_owner.setdefault(str(owner), []).append(player["id"])

    output = {
        "generated_at": iso_now(),
        "source": BASE_URL,
        "read_only": True,
        "entry_id": args.entry_id,
        "league_id": args.league_id,
        "event_id": event_id,
        "entry": entry,
        "league": league,
        "current_squad": squad,
        "squads_by_owner": squads_by_owner,
        "players": players,
        "available_players": available,
        "injury_return_watch": return_watch,
        "transactions": transactions,
        "trades": trades,
        "fixtures": fixtures,
        "game": game,
    }
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
