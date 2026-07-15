---
name: tax-ledger
description: Use when processing Australian tax receipts and invoices from configured email into file storage and spreadsheet ledgers, running dry runs or financial-year reconciliations, preserving or retrieving evidence, applying email labels, or archiving processed tax email. Loads personal systems, resources, tax facts, suppliers, checks, and actions from a private Tax Ledger Configuration workbook while enforcing duplicate checks, separate transaction and evidence statuses, GST review, and explicit authorisation before mutations.
---

# Tax Ledger

Use this skill for a configuration-backed, review-first tax-record workflow. Use the systems recorded in the private configuration workbook. Do not introduce a database unless explicitly requested.

## Required references

- Read [configuration.md](references/configuration.md) at the start of every run.
- Read [workflow.md](references/workflow.md) before processing or archiving email.
- Read [schema.md](references/schema.md) before creating or changing ledger rows.
- Read [tax-profile.md](references/tax-profile.md) before applying configured tax facts or GST instructions.
- Read [supplier-rules.md](references/supplier-rules.md) when classifying suppliers, scopes, categories, evidence, or GST.
- Read [annual-checks.md](references/annual-checks.md) when checking completeness for a financial year or preparing a tax return.

## Workflow

1. Load configuration and establish scope and mode.
   - Locate and validate `Tax Ledger Configuration` using `configuration.md`.
   - Resolve systems, workflow actions, labels, resources, tax facts, supplier mappings, recurring checks, and FY overrides from the workbook.
   - Treat inspect, review, dry run, audit, or report requests as read-only.
   - Treat explicit requests to add rows, upload evidence, label, or archive as authorisation only for those actions.
   - Never delete email or evidence.
2. Find candidates broadly.
   - Use configured email labels as signals, not the sole source of truth.
   - Also search configured suppliers, scopes, addresses, account references, and terms such as invoice, receipt, bill, rates, levy, renewal, and payment.
   - For a requested transaction-date window, use at least the configured search buffer and never less than two days on both sides.
   - Filter buffered results by the supplier's document, transaction, or payment date; do not use Gmail arrival date as the transaction date.
   - Include unlabelled likely tax items in the review report.
3. Prevent duplicates.
   - Compare source message ID, supplier reference, date, amount, and existing evidence link against the ledger.
   - Treat several emails about one charge as one transaction.
4. Preserve evidence.
   - Use the configured file-storage system and verified FY resources.
   - Store evidence beneath the financial year, scope, and generic ledger category it belongs to: `Tax Ledger/<FY>/<scope>/<category>/` unless the configuration specifies an equivalent hierarchy.
   - Use category folders only. Keep supplier names in filenames; do not create supplier subfolders unless the user explicitly requests them.
   - Keep a separate `Original email files` folder inside each financial-year scope folder, with matching category subfolders. Never reuse an evidence folder from another financial year.
   - Verify the target folder's financial-year ancestry before uploading. If the matching FY folder is not configured, stop and ask before creating folders or saving evidence.
   - Save an original attached invoice or receipt when present.
   - When no attachment exists, save the original RFC 822 email as `.eml` and use the email client's native Print/Save as PDF flow to preserve the rendered message.
   - Do not create an extracted-text, rewritten, or AI-formatted email PDF. If native printing is unavailable, retain the `.eml` and report that the convenient PDF copy could not be produced.
   - Do not fabricate or rewrite a supplier receipt. A generated summary is not source evidence.
   - Track evidence status independently from transaction review status.
   - Mark evidence as `Complete`, `Missing`, `Inadequate`, or `Login required`.
   - Produce one batch retrieval list for every `Missing`, `Inadequate`, or `Login required` item.
   - Link accountant-accessible stored evidence from the ledger, not the private email message.
5. Extract and classify.
   - Populate the standard schema and use the supplier document as the primary source.
   - Calculate GST only when the evidence supports it. Flag uncertainty rather than guessing.
6. Write and verify.
   - Use one transaction per row in a flat table.
   - Preserve unrelated tabs, formatting, formulas, and user data.
   - Read back the written range and verify evidence links before reporting success.
7. Organise Gmail last.
   - Apply the processed label only after evidence and ledger verification succeed.
   - Archive only after the user has reviewed the entries or explicitly instructs archiving.
   - Archive means remove Inbox; never trash the message.
8. Reconcile annual expectations when requested.
   - Compare the ledger against each applicable active check in the configuration workbook using `annual-checks.md`.
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
