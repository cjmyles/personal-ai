"""Read-only, fail-closed gates for evidence-backed statement reconciliation.

No network or ledger writes. Inputs must be derived from verified source evidence.
Run tests with: python3 -m unittest discover -s tests -v
"""
from datetime import date
from decimal import Decimal, InvalidOperation


def match_gate(statement, ledger, policy):
    """Return (allowed, reason) for an ordinary one-to-one replacement only."""
    for key in ("statement_balanced", "settled", "merchant_verified",
                "references_compatible", "unique_candidate", "period_verified"):
        if statement.get(key) is not True:
            return False, key
    if statement.get("conflict") is not False:
        return False, "conflict_not_excluded"
    if statement.get("already_linked") is not False:
        return False, "already_linked_or_unknown"
    if statement.get("kind") != "purchase":
        return False, "complex_allocation_review"
    try:
        if not statement.get("currency") or statement["currency"] != ledger["currency"]:
            return False, "original_currency_mismatch_or_missing"
        original = Decimal(str(statement["original_amount"]))
        if original != Decimal(str(ledger["original_amount"])) or original <= 0:
            return False, "original_amount_mismatch"
        actual = Decimal(str(statement["aud_amount"]))
        estimate = Decimal(str(ledger["aud_amount"]))
        lag = int(policy["max_posting_days"])
        tolerance = Decimal(str(policy["max_fx_difference_fraction"]))
        if lag < 0 or not (Decimal(0) <= tolerance < Decimal(1)):
            return False, "invalid_policy"
        if not all(x.is_finite() and x > 0 for x in (actual, estimate, original)):
            return False, "invalid_amount"
        transaction_date = date.fromisoformat(statement["transaction_date"])
        if transaction_date != date.fromisoformat(ledger["payment_date"]):
            return False, "transaction_date_mismatch"
        posting_date = date.fromisoformat(statement["posting_date"])
        if not 0 <= (posting_date - transaction_date).days <= lag:
            return False, "posting_date_outside_window"
        if statement["currency"] == "AUD" and actual != original:
            return False, "aud_amount_conflict"
        if abs(actual - estimate) / estimate > tolerance:
            return False, "fx_difference_review"
    except (KeyError, ValueError, TypeError, InvalidOperation, OverflowError):
        return False, "missing_or_invalid_source_or_policy"
    if ledger.get("lodged") is not False:
        return False, "lodged_or_unknown_return_review"
    return True, "unique_supported_match"


def archive_gate(*, authorised=False, evidence_verified=False,
                 reconciled=False, full_payment_confirmed=False,
                 issuer_confirms_nothing_due=False, reminder_verified=False,
                 archive_before_payment_approved=False,
                 other_actions_resolved_or_safely_tracked=False):
    """No defaults can authorise archiving or infer repayment."""
    return all(x is True for x in (
        authorised, evidence_verified, reconciled,
        other_actions_resolved_or_safely_tracked,
    )) and (
        full_payment_confirmed is True
        or issuer_confirms_nothing_due is True
        or (reminder_verified is True and archive_before_payment_approved is True)
    )
