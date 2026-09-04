import argparse
import importlib.util
import unittest
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).parents[1] / "scripts" / "fpl_draft_snapshot.py"
SPEC = importlib.util.spec_from_file_location("fpl_draft_snapshot", SCRIPT)
snapshot = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(snapshot)


class ImmediateFuture:
    def __init__(self, value):
        self.value = value

    def result(self):
        return self.value


class RecordingExecutor:
    instances = []

    def __init__(self, max_workers):
        self.max_workers = max_workers
        self.submissions = []
        self.__class__.instances.append(self)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def submit(self, function, *args):
        self.submissions.append((function, args))
        return ImmediateFuture(function(*args))


class SnapshotTests(unittest.TestCase):
    def setUp(self):
        RecordingExecutor.instances.clear()

    def test_cli_defaults_and_overrides(self):
        defaults = snapshot.build_parser().parse_args([])
        self.assertEqual(defaults.timeout, 20.0)
        self.assertEqual(defaults.max_workers, 16)

        supplied = snapshot.build_parser().parse_args(["--timeout", "4.5", "--max-workers", "7"])
        self.assertEqual(supplied.timeout, 4.5)
        self.assertEqual(supplied.max_workers, 7)

    def test_fetch_many_submits_every_endpoint_to_bounded_executor(self):
        with mock.patch.object(snapshot, "ThreadPoolExecutor", RecordingExecutor), mock.patch.object(
            snapshot, "fetch_json", side_effect=lambda path, timeout: (path, timeout)
        ):
            result = snapshot.fetch_many({"one": "/api/one", "two": "/api/two"}, 3.0, 16)

        executor = RecordingExecutor.instances[0]
        self.assertEqual(executor.max_workers, 2)
        self.assertEqual(len(executor.submissions), 2)
        self.assertEqual(result["one"], ("/api/one", 3.0))
        self.assertEqual(result["two"], ("/api/two", 3.0))

    def test_player_contains_full_names_stats_and_next_three_fixtures(self):
        fixtures = snapshot.next_fixtures_by_team(
            [
                {"id": 1, "event": 3, "team_h": 1, "team_a": 2, "kickoff_time": "2026-09-01T12:00:00Z"},
                {"id": 2, "event": 4, "team_h": 3, "team_a": 1, "kickoff_time": "2026-09-08T12:00:00Z"},
                {"id": 3, "event": 5, "team_h": 1, "team_a": 3, "kickoff_time": "2026-09-15T12:00:00Z"},
                {"id": 4, "event": 6, "team_h": 2, "team_a": 1, "kickoff_time": "2026-09-22T12:00:00Z"},
            ],
            3,
            {1: "Alpha United", 2: "Beta City", 3: "Gamma Town"},
            {1: "ALP", 2: "BET", 3: "GAM"},
        )
        player = snapshot.normalise_player(
            {
                "id": 10, "first_name": "Ada", "second_name": "Striker", "web_name": "Striker",
                "team": 1, "element_type": 4, "minutes": 450, "starts": 5,
                "goals_scored": 4, "assists": 3, "clean_sheets": 1, "bonus": 7,
                "expected_goals": "3.20", "expected_assists": "1.75", "total_points": 40,
            },
            {"status": "a"},
            {1: "Alpha United"},
            {1: "ALP"},
            {4: "FWD"},
            fixtures,
        )

        self.assertEqual(player["name"], "Ada Striker")
        self.assertEqual(player["team"], "Alpha United")
        self.assertEqual(
            {key: player[key] for key in ("minutes", "starts", "goals", "assists", "clean_sheets", "bonus", "xg", "xa")},
            {"minutes": 450, "starts": 5, "goals": 4, "assists": 3, "clean_sheets": 1, "bonus": 7, "xg": "3.20", "xa": "1.75"},
        )
        self.assertEqual(len(player["next_three_fixtures"]), 3)
        self.assertEqual(player["next_three_fixtures"][0]["opponent"], "Beta City")
        self.assertEqual(player["next_three_fixtures"][0]["venue"], "H")
        self.assertEqual(player["next_three_fixtures"][1]["venue"], "A")

    def test_registration_changes_prioritise_new_high_ranked_players(self):
        players = [
            {"id": 628, "name": "Bradley Barcola", "team": "Liverpool", "position": "MID", "draft_rank": 8},
            {"id": 10, "name": "Existing Player", "team": "New Club", "position": "FWD", "draft_rank": 50},
            {"id": 629, "name": "Lower Ranked Signing", "team": "Another Club", "position": "MID", "draft_rank": 200},
        ]
        previous = {
            "10": {"id": 10, "name": "Existing Player", "team": "Old Club", "position": "FWD"}
        }

        new_players, changed_players = snapshot.registration_changes(players, previous, True)

        self.assertEqual([player["id"] for player in new_players], [628, 629])
        self.assertEqual(changed_players[0]["player"]["id"], 10)
        self.assertEqual(
            changed_players[0]["changes"]["team"],
            {"from": "Old Club", "to": "New Club"},
        )
        self.assertEqual(snapshot.registration_changes(players, previous, False), ([], []))

    def test_fixture_and_squad_enrichment_include_live_state(self):
        fixture = snapshot.enrich_fixture(
            {"id": 9, "team_h": 1, "team_a": 2, "team_h_score": 2, "team_a_score": 1, "started": True, "minutes": 63},
            {1: "Alpha United", 2: "Beta City"},
            {1: "ALP", 2: "BET"},
        )
        squad = snapshot.enrich_squad(
            {"picks": [{"element": 10, "position": 1}]},
            {"10": {"id": 10, "name": "Ada Striker", "team": "Alpha United"}},
            {"10": {"stats": {"minutes": 63, "goals_scored": 1}}},
        )

        self.assertEqual(fixture["status"], "live")
        self.assertEqual(fixture["home_team"], "Alpha United")
        self.assertEqual((fixture["home_score"], fixture["away_score"]), (2, 1))
        self.assertEqual(squad["picks"][0]["player"]["name"], "Ada Striker")
        self.assertEqual(squad["picks"][0]["live"]["stats"]["minutes"], 63)

    def test_build_snapshot_fetches_both_concurrent_batches_and_exposes_live_data(self):
        bootstrap = {
            "elements": [{
                "id": 10, "first_name": "Ada", "second_name": "Striker", "team": 1,
                "element_type": 4, "status": "a", "draft_rank": 1,
            }],
            "teams": [{"id": 1, "name": "Alpha United", "short_name": "ALP"}],
            "element_types": [{"id": 4, "singular_name_short": "FWD"}],
            "fixtures": {},
        }
        event_payloads = {
            "league": {}, "entry": {}, "element_status": {"element_status": [{"element": 10, "status": "a"}]},
            "squad": {"picks": [{"element": 10}]}, "transactions": [], "trades": [],
            "fixtures": [{"id": 1, "team_h": 1, "team_a": 1, "started": False}],
            "live": {"elements": {"10": {"stats": {"minutes": 0}}}},
            "match_status": {"status": [{"event": 2, "points": "r"}]},
        }
        args = argparse.Namespace(
            entry_id=184598, league_id=35686, event_id=2, previous=None,
            output=None, pretty=False, timeout=5.0, max_workers=16,
        )

        with mock.patch.object(snapshot, "fetch_many", side_effect=[
            {"bootstrap": bootstrap, "game": {"current_event": 2}}, event_payloads
        ]) as fetch_many:
            result = snapshot.build_snapshot(args)

        self.assertEqual(fetch_many.call_count, 2)
        first_paths = fetch_many.call_args_list[0].args[0]
        second_paths = fetch_many.call_args_list[1].args[0]
        self.assertEqual(set(first_paths), {"bootstrap", "game"})
        self.assertTrue({"league", "entry", "element_status", "squad", "transactions", "trades", "fixtures", "live", "match_status"}.issubset(second_paths))
        self.assertEqual(result["match_status"]["status"][0]["event"], 2)
        self.assertEqual(result["current_squad"]["picks"][0]["player"]["name"], "Ada Striker")
        self.assertIn("live_scores", result)
        self.assertEqual(result["new_players_since_previous"], [])


if __name__ == "__main__":
    unittest.main()
