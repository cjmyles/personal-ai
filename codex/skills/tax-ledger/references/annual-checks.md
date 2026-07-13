# Annual tax-return checks

Use these expectations to reconcile a financial year after transaction processing. They are completeness checks, not tax advice and not substitutes for source evidence.

## Method

For each applicable check:

1. Count distinct transactions after duplicate matching by supplier reference, date, amount, and source email ID.
2. Compare the count and covered periods with the expectation.
3. Report `Pass`, `Review`, or `Not applicable`.
4. List missing periods, possible duplicates, irregular amounts, incomplete evidence, and any reason the expectation changed.
5. Do not create a missing transaction without source evidence.

Use `Review` when the count differs, periods overlap, service started or ended during the year, billing frequency changed, or evidence is incomplete. A matching count does not override other transaction or evidence reviews.

## Wentworth St

| Check | Expected for a full year | Match rule | Review triggers |
|---|---:|---|---|
| Belong internet | 12 monthly charges | One distinct Belong internet charge for each month from July through June | Missing or repeated month; more or fewer than 12 charges; service start, cancellation, credit, refund, or billing-cycle change; material amount variation; incomplete evidence |
| EnergyAustralia electricity | 4 quarterly bills | Four distinct electricity bills whose service periods provide continuous coverage through the financial year | Missing or repeated period; more or fewer than 4 bills; a gap or overlap between service periods; account or billing-frequency change; credit, refund, or irregular charge; incomplete evidence |
| EnergyAustralia gas | 4 quarterly bills | Four distinct gas bills whose service periods provide continuous coverage through the financial year | Missing or repeated period; more or fewer than 4 bills; a gap or overlap between service periods; account or billing-frequency change; credit, refund, or irregular charge; incomplete evidence |

## Results

Keep annual-check results separate from the flat transaction tables. When a spreadsheet check tab is authorised, use one row per check with:

| Field | Meaning |
|---|---|
| Financial year | FY being reconciled |
| Scope | Property or business scope |
| Check | Human-readable expectation |
| Expected | Expected count or condition |
| Found | Distinct qualifying records found |
| Coverage | Months or periods represented |
| Status | Pass, Review, or Not applicable |
| Exceptions | Missing periods, duplicates, irregular values, or changed circumstances |
| Last checked | Date the reconciliation was run |

Only change an expectation after checking the supplier arrangement or recording a user decision. Preserve the reason for any effective-dated change.
