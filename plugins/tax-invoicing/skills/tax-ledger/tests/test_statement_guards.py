import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from statement_guards import archive_gate, match_gate


class StatementGuardsTest(unittest.TestCase):
    def setUp(self):
        self.statement = dict(statement_balanced=True, settled=True,
            merchant_verified=True, references_compatible=True,
            unique_candidate=True, period_verified=True, conflict=False,
            already_linked=False, kind="purchase", currency="USD",
            original_amount="100.00", aud_amount="151.25",
            transaction_date="2026-06-30", posting_date="2026-07-02")
        self.ledger = dict(currency="USD", original_amount="100",
            aud_amount="150", payment_date="2026-06-30", lodged=False)
        self.policy = dict(max_posting_days=7, max_fx_difference_fraction="0.10")

    def test_unique_match_across_fy_posting_boundary(self):
        self.assertTrue(match_gate(self.statement, self.ledger, self.policy)[0])

    def test_fifty_aud_is_not_one_hundred_usd(self):
        self.statement.update(currency="AUD", original_amount=50, aud_amount=50)
        self.assertFalse(match_gate(self.statement, self.ledger, self.policy)[0])

    def test_ambiguous_conflicting_pending_incomplete_and_replayed(self):
        for key, value in [("unique_candidate", False), ("conflict", True),
                           ("settled", False), ("statement_balanced", False),
                           ("already_linked", True), ("references_compatible", False)]:
            with self.subTest(key=key):
                s = dict(self.statement, **{key: value})
                self.assertFalse(match_gate(s, self.ledger, self.policy)[0])

    def test_amount_currency_fx_and_dates_must_agree(self):
        for key, value in [("original_amount", 50), ("currency", "EUR"),
                           ("aud_amount", 50), ("posting_date", "2026-08-02"),
                           ("transaction_date", "2026-06-01")]:
            with self.subTest(key=key):
                self.assertFalse(match_gate(dict(self.statement, **{key: value}),
                                            self.ledger, self.policy)[0])

    def test_missing_evidence_fails_closed(self):
        for key in self.statement:
            s = dict(self.statement)
            del s[key]
            with self.subTest(key=key):
                self.assertFalse(match_gate(s, self.ledger, self.policy)[0])

    def test_invalid_numbers_and_missing_policy(self):
        for amount in ["NaN", "Infinity", -5, "bad", None]:
            self.assertFalse(match_gate(dict(self.statement, aud_amount=amount),
                                        self.ledger, self.policy)[0])
        self.assertFalse(match_gate(self.statement, self.ledger, {})[0])

    def test_refunds_split_payments_and_lodged_returns_need_review(self):
        for kind in ["refund", "repayment", "split", "fee"]:
            self.assertFalse(match_gate(dict(self.statement, kind=kind),
                                        self.ledger, self.policy)[0])
        self.assertFalse(match_gate(self.statement, dict(self.ledger, lodged=True),
                                    self.policy)[0])

    def test_archive_payment_gate(self):
        ready = dict(authorised=True, evidence_verified=True, reconciled=True,
                     other_actions_resolved_or_safely_tracked=True)
        self.assertFalse(archive_gate())
        self.assertFalse(archive_gate(**ready))
        self.assertFalse(archive_gate(**ready, reminder_verified=True))
        self.assertFalse(archive_gate(**ready, archive_before_payment_approved=True))
        self.assertTrue(archive_gate(**ready, full_payment_confirmed=True))
        self.assertTrue(archive_gate(**ready, issuer_confirms_nothing_due=True))
        self.assertTrue(archive_gate(**ready, reminder_verified=True,
                                    archive_before_payment_approved=True))
        self.assertFalse(archive_gate(**dict(ready, reconciled=False),
                                     full_payment_confirmed=True))


if __name__ == "__main__":
    unittest.main()
