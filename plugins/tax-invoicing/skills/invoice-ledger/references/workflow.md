# Mutation workflow

## Invoice preparation

- Verify canonical client, currency, unit, rate, description, GST, superannuation, deductions and totals.
- Create or update a draft only after an explicit live instruction.
- Do not issue or send unless that action is explicitly authorised.

## Issue or send

- Re-read the draft from the operational system.
- Verify Invoice Ref, client, currency, line items, totals, issue date, terms and due date.
- Issue or send only after an explicit live instruction.
- Read back the resulting identifier and status before updating the workbook.

## Payment entry

1. Verify Invoice Ref, canonical client, currency, invoice total, outstanding balance, existing operational payments and spreadsheet payments.
2. Reject or review any duplicate composite key.
3. Require an explicit live instruction to add the payment.
4. Write the operational system first.
5. Verify payment ID, receipt/reference and new balance.
6. Add one `Invoice Payments` row per verified payment.
7. Update invoice summary fields and read both ranges back.

Editing or removing an existing payment requires separate explicit confirmation. Never infer missing payment details.

## Recovery

If the operational write succeeds but spreadsheet write fails, or the reverse, create a TODO with the confirmed side, failed side, identifiers and next action. Never retry a mutation without re-reading both systems.
