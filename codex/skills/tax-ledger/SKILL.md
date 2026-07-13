---
name: tax-ledger
description: Use when processing Australian tax receipts and invoices from Gmail into Google Drive and Google Sheets, running a dry run, checking missing FY records, preserving or retrieving evidence, applying Gmail labels, or archiving processed tax emails. Enforces duplicate checks, separate transaction and evidence statuses, personal tax-profile rules, GST review, and explicit confirmation before mailbox changes.
---

# Tax Ledger

Use this skill for Craig's review-first tax-record workflow. Keep Gmail, Drive, and Sheets as the operating system; do not introduce a database unless explicitly requested.

## Required references

- Read [workflow.md](references/workflow.md) before processing or archiving email.
- Read [schema.md](references/schema.md) before creating or changing ledger rows.
- Read [tax-profile.md](references/tax-profile.md) before classifying GST, Australian rental income, or Australian rental expenses.
- Read [supplier-rules.md](references/supplier-rules.md) when classifying suppliers or GST.
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
   - Save an original attached invoice or receipt when present.
   - When no attachment exists, save the original RFC 822 email as `.eml` and a readable PDF rendered from its original HTML or plain-text body.
   - Do not fabricate or rewrite a supplier receipt. A generated summary is not source evidence.
   - Track evidence status independently from transaction review status.
   - Mark evidence as `Complete`, `Missing`, `Inadequate`, or `Login required`.
   - Produce one batch retrieval list for every `Missing`, `Inadequate`, or `Login required` item.
   - Link the accountant-accessible Drive evidence from the ledger, not the private Gmail message.
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
