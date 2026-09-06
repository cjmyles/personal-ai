---
name: invoice-ledger
description: Reconcile operational invoices and payments with configured financial-year spreadsheets, prepare or issue invoices, record verified payments, maintain Logbook and invoice joins, and validate BAS fields. Use for invoice dry runs, Invoicely export reconciliation, invoice creation or sending, payment entry, status checks, cross-financial-year routing, and recovery after partial system updates.
---

# Invoice Ledger

Use the configured invoice system as the operational source and the configured financial-year workbook as the reporting record. Keep personal clients, URLs, tax facts, resources, aliases and exceptions in `Tax Ledger Configuration`, never in this skill.

## Required references

- Read [configuration.md](references/configuration.md) before every run.
- Read [workflow.md](references/workflow.md) before preparing, issuing, sending or changing a payment.
- Read [schema.md](references/schema.md) before reading or writing Logbook, Invoices, Invoice Payments, BAS Summary, Checks or TODO.

## Workflow

1. Load configuration and establish scope.
   - Locate the single exact `Tax Ledger Configuration` workbook.
   - Resolve invoice system, financial year, workbook, tab identifiers, Client Mappings, Invoice Status Mappings, Tax Profile, FY Resources and FY Overrides.
   - Treat inspect, reconcile, report, audit and dry-run requests as read-only.
2. Gather operational records.
   - Prefer configured CSV or XLS exports for bulk reconciliation.
   - Otherwise use the configured authenticated invoice system.
   - Read invoice identifiers, clients, currency, dates, totals, status, outstanding balance, payments and receipt/reference values.
3. Reconcile using stable keys.
   - Use `Invoice Ref` as the stable spreadsheet join key.
   - Apply effective-dated Client Mappings before comparing client names.
   - Allow cross-FY Logbook lookup only when FY Resources or FY Overrides explicitly permits it.
   - Compare amounts, dates, currency, status, balance, payment identifiers and BAS fields.
4. Prevent duplicates and silent overwrites.
   - Match payments by operational payment ID when present.
   - Otherwise compare Invoice Ref, payment date, amount, currency and reference as a composite key.
   - Never infer a missing payment date, amount, currency, identifier or reference.
   - Record mismatches as `Review`; do not choose one system silently.
5. Perform authorised mutations in order.
   - Require an explicit live instruction to prepare an invoice.
   - Require an explicit live instruction to issue or send an invoice.
   - Require an explicit live instruction to record a payment.
   - Require separate explicit confirmation to edit or remove an existing payment.
   - For payment writes, verify Invoice Ref, client, currency, outstanding balance, existing payments and spreadsheet state first.
   - Write the operational invoice system first, verify receipt and balance, then update the spreadsheet and read it back.
6. Recover safely.
   - If only one system succeeds, add a configured TODO containing the verified state and required recovery action.
   - Do not report both systems aligned until both readbacks succeed.

## Accounting safeguards

- Load effective-dated accounting basis and GST treatment from Tax Profile and FY Overrides.
- Mark unresolved accounting basis or tax dates `Review`; do not infer them.
- Preserve GST actually invoiced even when it conflicts with the tax profile, and flag the conflict.
- Keep issue date, due date and every payment date separately.
- Do not treat operational status alone as proof of payment.

## Output

Keep reports concise: matched, mismatched, missing references, duplicate risks, mutations performed, recovery TODOs and unresolved configuration.
