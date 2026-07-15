# Evidence and processing workflow

## Selection

Search the configured financial-year and scope labels, then expand using configured suppliers, account numbers, addresses, identifiers, financial-document terms, and recurring checks.

For a requested transaction-date window:

- Search Gmail with at least a two-day buffer before and after the requested dates. Expand it when a supplier is known to deliver documents later.
- Filter results using the supplier's invoice, receipt, transaction, service, or payment date, according to the date represented by the ledger entry.
- Do not exclude a transaction because its email arrived outside the requested window. Include a 1 July payment when its receipt arrived on 2 July.

Report three groups: process, needs review, and ignored. Explain ambiguous exclusions briefly.

## Evidence precedence

1. Original supplier invoice or receipt attachment.
2. Supplier-hosted invoice downloaded from a link.
3. Original email saved as `.eml`, plus a PDF created with the email client's native Print/Save as PDF flow.
4. Bank record or other corroboration when supplier evidence is unavailable.

Never substitute an AI-written receipt or extracted-text PDF for source evidence. For email-only evidence, retain the `.eml` for authenticity and use the email client's native print rendering for convenient accountant access. Load the message's normal rendered content before printing. If native printing is unavailable, keep the `.eml` and report the missing convenient PDF rather than manufacturing one.

## Financial-year folder isolation

Store evidence only within the financial year containing the transaction date. Use the configured hierarchy, normally:

```text
Tax Ledger/
  <FY>/
    <scope>/
      <category>/
      Original email files/
        <category>/
```

Create equivalent scope and category folders under each FY only when authorised. Use generic ledger categories for folder names. Keep the supplier in the filename, not in another folder level: save `YYYY-MM-DD Supplier - Tax invoice.pdf` in `<scope>/<category>/`, not `<scope>/<category>/<supplier>/`. Save readable evidence in the category folder and original `.eml` files in the matching category beneath `Original email files`.

Before uploading, verify that the target folder is descended from the correct FY folder. Never use an FY27 folder for an FY26 transaction, or vice versa. Do not create or reorganise Drive folders without explicit user authorisation.

## Naming

Use `YYYY-MM-DD Supplier - Description.ext`. Keep names stable after linking them in the ledger.

## Evidence status and retrieval

Assess evidence independently for every transaction. Use `Complete` only when source evidence is saved in Drive and linked. Use `Login required` when the email identifies a document but authentication prevents retrieval.

At the end of each run, combine all non-complete evidence into one retrieval batch. Group portal logins by supplier where useful, but retain one line per transaction so each recovered document can be matched and its status updated.

After the user supplies a document, save it, verify the relevant details, update the Drive link, and change evidence status to `Complete`. Do not change transaction status unless the user also approves the transaction.

## Order of mutations

1. Save available evidence to Drive; otherwise record the evidence status and retrieval action.
2. Add or update the ledger row.
3. Read back and verify the row, evidence status, and any evidence link or retrieval action.
4. Apply configured email labels.
5. Archive only after review or explicit instruction.

If a step fails, stop before later steps and report the partial state.
