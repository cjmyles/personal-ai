#!/usr/bin/env python3
"""Arithmetic check of already verified AUD project records; JSON stdin/output."""
import json
import sys
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal('0.01')

def calculate(data):
    shares = {p: Decimal(str(v)) for p, v in data['shares'].items()}
    if not shares or any(v < 0 for v in shares.values()) or sum(shares.values()) != 1:
        raise ValueError('Shares must be nonnegative and sum to one')
    net = dict.fromkeys(shares, Decimal(0))
    total = Decimal(0)
    seen = set()
    pending = 0
    for kind in ('expenses', 'transfers'):
        for row in data.get(kind, []):
            key = (kind, row['id'])
            if key in seen:
                raise ValueError('Duplicate record ID: ' + str(key))
            seen.add(key)
            if row.get('status') != 'paid':
                pending += 1
                continue
            if row.get('currency') != 'AUD':
                raise ValueError('Actual AUD settlement required')
            amount = Decimal(str(row['amount']))
            if not amount.is_finite() or amount != amount.quantize(CENT):
                raise ValueError('Amount must be finite AUD cents')
            if kind == 'expenses':
                if row['payer'] not in shares:
                    raise ValueError('Unknown payer')
                total += amount
                net[row['payer']] += amount
            else:
                if amount < 0 or row['from'] == row['to'] or any(row[p] not in shares for p in ('from', 'to')):
                    raise ValueError('Invalid transfer')
                net[row['from']] += amount
                net[row['to']] -= amount
    fair = {p: (total * weight).quantize(CENT, rounding=ROUND_HALF_UP) for p, weight in shares.items()}
    # Assign the rounding residual to the largest share, alphabetical tie-break.
    residual_party = sorted(shares, key=lambda p: (-shares[p], p))[0]
    fair[residual_party] += total - sum(fair.values())
    credits = {p: net[p] - fair[p] for p in shares}
    if sum(net.values()) != total or sum(credits.values()) != 0:
        raise ValueError('Unbalanced records')
    fmt = lambda d: {p: format(v, '.2f') for p, v in d.items()}
    return {'total_paid_aud': format(total, '.2f'), 'net_contributions_aud': fmt(net),
            'fair_shares_aud': fmt(fair), 'credits_aud': fmt(credits),
            'pending_records_excluded': pending}

if __name__ == '__main__':
    print(json.dumps(calculate(json.load(sys.stdin)), indent=2))
