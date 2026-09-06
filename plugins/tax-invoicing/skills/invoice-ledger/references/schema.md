# Workbook schema

## Logbook

Use one row per date. Required join field: `Invoice Ref`. Resolve client aliases through configuration before comparison.

## Invoices

Keep one row per invoice. Preserve:

- Invoice Ref and operational invoice ID
- Client, description, time, unit, rate and currency context
- GST, superannuation, deductions and calculated totals
- Issue, due, paid and BAS fields
- Outstanding balance, reconciliation status and GST conflict

Do not use duplicate unlabeled calculation blocks. Preserve exceptional historical invoiced figures in notes or explicitly named fields.

## Invoice Payments

Use one row per payment:

| Field | Purpose |
|---|---|
| Invoice Ref | Stable workbook join key |
| Operational invoice ID | Invoice-system identifier |
| Client | Canonical configured client |
| Payment date | Verified operational date |
| Amount | Verified payment amount |
| Currency | Verified payment currency |
| Operational payment ID | Primary duplicate key |
| Receipt / reference | Operational evidence/reference |
| Payment status | Verified, Review or Reversed |
| Source | Export, operational UI or other configured source |
| Reconciliation status | Cross-system result |
| Notes | Material exception only |

## Checks and TODO

Keep validation results in `Checks`. Keep unresolved decisions and one-sided write recovery in `TODO`. Do not invent invoice or payment rows to satisfy a check.
