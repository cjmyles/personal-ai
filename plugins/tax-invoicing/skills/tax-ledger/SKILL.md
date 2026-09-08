---
name: tax-ledger
description: Process Australian tax receipts, invoices and monthly bank or credit-card statements into configured Drive evidence and FY spreadsheets. Use for statement reconciliation, actual-AUD matching, missing expenses, spending review, repayment tracking, dry runs, evidence retrieval and authorised email labelling or archiving. Keeps reconciliation, evidence, tax review and repayment independent.
---

# Tax Ledger

Use this skill for a configuration-led, review-first tax-record workflow. Keep the configured mail, Drive and spreadsheet systems; do not introduce a database unless explicitly requested.

## Configuration first

Read [configuration.md](references/configuration.md) at the start of every run. Live `Tax Ledger Configuration` and effective FY overrides are authoritative for personal details, systems, tax treatment, suppliers, folders and policies. Bundled historical personal references are not a current source of truth and must never override live configuration. Missing or conflicting settings require review, not a guessed tax rule.

For bank/card statements, statement-available notices, actual-AUD reconciliation, unusual-spending checks or card-repayment tracking, also read [statement-reconciliation.md](references/statement-reconciliation.md). Its payment/archive gate overrides the general processed-email rule below. An implementation request does not authorise bank payments or scheduling an automation.

## Required references

- Read [workflow.md](references/workflow.md) before processing or archiving email.
- Read [schema.md](references/schema.md) before creating or changing ledger rows.
- Read [tax-profile.md](references/tax-profile.md) before classifying GST, Australian rental income, or Australian rental expenses.
- Read [supplier-rules.md](references/supplier-rules.md) when classifying suppliers or GST.
- Read [annual-checks.md](references/annual-checks.md) when checking completeness for a financial year or preparing a tax return.
- Read [connected-resources.md](references/connected-resources.md) when locating current Gmail labels, Drive folders, or spreadsheets.

## Workflow

1. Establish scope and mode.
   - Treat inspect, review, dry run, audit, or report requests as read-only.
   - Treat explicit requests to add rows, upload evidence, label, or archive as authorisation only for those actions.
   - Never delete email or evidence.
2. Find candidates broadly.
   - Use Gmail labels as signals, not the sole source of truth.
   - Also search known suppliers, property addresses, account references, and terms such as invoice, receipt, bill, rates, levy, renewal, and payment.
   - For a requested transaction-date window, search Gmail with at least a two-day buffer on both sides so delayed receipts are not missed.
   - Filter buffered results by the supplier's document, transaction, or payment date; do not use Gmail arrival date as the transaction date.
   - Include unlabelled likely tax items in the review report.
3. Prevent duplicates.
   - Compare Gmail message ID, supplier reference, date, amount, and existing evidence link against the ledger.
   - Treat several emails about one charge as one transaction.
4. Preserve evidence.
   - Store evidence beneath the financial year it belongs to: `Tax Ledger/<FY>/<scope>/`.
   - Keep a separate `Original email files` folder inside each financial-year scope folder. Never reuse an evidence folder from another financial year.
   - Verify the target folder's financial-year ancestry before uploading. If the matching FY folder is not configured, stop and ask before creating folders or saving evidence.
   - Save an original attached invoice or receipt when present.
   - When no attachment exists, save the original RFC 822 email as `.eml` and a readable PDF rendered from its original HTML or plain-text body.
   - Do not fabricate or rewrite a supplier receipt. A generated summary is not source evidence.
   - Track evidence status independently from transaction review status.
   - Mark evidence as `Complete`, `Missing`, `Inadequate`, or `Login required`.
   - Produce one batch retrieval list for every `Missing`, `Inadequate`, or `Login required` item.
   - Link the accountant-accessible Drive evidence from the ledger, not the private Gmail message.
5. Extract and classify.
   - Populate the standard schema and use the supplier document as the primary source.
   - Translate supported foreign-currency amounts into AUD using the rules in `references/schema.md`; do not require a card or bank statement solely to perform the conversion.
   - Calculate GST only when the evidence supports it. Flag uncertainty rather than guessing.
6. Write and verify.
   - Use one transaction per row in a flat table.
   - Preserve unrelated tabs, formatting, formulas, and user data.
   - Read back the written range and verify evidence links before reporting success.
7. Organise Gmail last.
   - Apply the processed label only after evidence and ledger verification succeed.
   - Archive only after the user has reviewed the entries or explicitly instructs archiving.
   - Archive means remove Inbox; never trash the message.
   - For statement emails, reconciliation does not prove repayment. Keep Inbox until the statement payment is confirmed, or a verified actionable payment reminder/task exists and the user explicitly approves archiving despite outstanding payment.
8. Reconcile annual expectations when requested.
   - Compare the ledger against each applicable check in `annual-checks.md`.
   - Report expected, found, missing, duplicate, needs review, and not applicable counts separately.
   - Treat a failed count as a prompt to investigate, not proof that a transaction is missing.
   - Keep check results separate from transaction rows; do not invent transactions to satisfy an expectation.

## Transaction review states

- `Review`: Transaction classification, amount, treatment, or inclusion still requires human approval.
- `Reviewed`: The user approved the row.
- `Auto`: High-confidence recurring treatment, still subject to later accountant review.

Transaction approval does not imply that evidence is complete. When the user says they reviewed the rows and says "do it", change only the applicable transaction status from `Review` to `Reviewed` after confirming their identity.

## Evidence states

- `Complete`: Suitable source evidence is saved in Drive and linked.
- `Missing`: No suitable source evidence was found.
- `Inadequate`: Evidence exists but lacks material information or is only a generated summary.
- `Login required`: The document is behind an authenticated supplier portal and the user must retrieve it.

Never infer evidence status from transaction status or vice versa.

## Guardrails

- Do not present bookkeeping classification as tax or legal advice.
- Treat the tax profile as user-supplied instructions for this ledger, not a general rule for another taxpayer.
- Do not claim the ATO will accept evidence with certainty; explain record-keeping risks and suggest accountant confirmation for ambiguity.
- Do not infer a service address from a billing address when they conflict. Use a recorded user decision and note it.
- Do not expose private email contents or identifiers unnecessarily in summaries.
- Keep user-facing reports short: processed, transaction review, evidence retrieval batch, ignored, and failures.
