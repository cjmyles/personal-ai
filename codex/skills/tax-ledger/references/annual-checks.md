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

## Configured checks

Load active expectations from the configuration workbook's `Recurring Checks` tab and apply any matching `FY Overrides`. Use the configured scope, supplier or category, frequency, expectation, match rule, and review triggers. Do not hardcode a supplier, property, count, or billing frequency in the skill.

For boundary checks, use the configured window around both financial-year boundaries and assign transactions using the supplier document, transaction, or payment date rather than email arrival date. Do not create an adjacent-year ledger or invent a transaction when evidence or an adjacent ledger is unavailable.

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

Only change an expectation after checking the supplier arrangement or recording an authorised user decision in the configuration workbook. Preserve the reason and effective dates.
