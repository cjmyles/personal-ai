# Configuration workbook

Use one private Google Sheet titled `Tax Ledger Configuration` as the source of truth for personal settings. Keep identifiers, tax facts, supplier decisions, labels, recurring checks, and financial-year exceptions out of the skill.

## Locate and validate

1. Use a configuration URL or spreadsheet ID supplied by the user.
2. Otherwise search Google Drive for the exact title `Tax Ledger Configuration`.
3. Continue automatically only when one exact match exists. Ask the user to choose when several exact matches exist. Do not create or mutate records when no configuration exists.
4. Read spreadsheet metadata before reading bounded ranges from the visible tabs.
5. Check the `Validation` tab before a run. Treat a relevant missing resource or ambiguous effective-dated rule as blocking automatic mutation. A non-blocking `Review` item may proceed only with the affected transaction or check also marked `Review`.
6. Verify every configured spreadsheet and Drive folder before writing. Confirm financial-year ancestry for evidence folders.

Do not store credentials, passwords, access tokens, or private keys in the workbook.

## Expected tabs

| Tab | Purpose |
|---|---|
| Systems | Maps email, file storage, spreadsheet, workflow, template, and other functions to configured systems and identifiers |
| Workflow | Defines search, evidence, ledger, label, archive, and prohibited-action policies |
| Gmail Labels | Holds configured label names and purposes when Gmail is the email system |
| Tax Profile | Holds user-supplied, effective-dated tax facts and ledger instructions |
| Supplier Mappings | Maps supplier patterns to scope, category, evidence rules, and classification notes |
| Recurring Checks | Holds annual completeness expectations shared across financial years |
| FY Resources | Holds financial-year spreadsheet and folder identifiers with scope and category |
| FY Overrides | Holds dated financial-year exceptions to shared settings |
| Validation | Shows configuration checks and unresolved issues |

Use exact visible headers rather than column positions when a workbook evolves. Preserve unknown columns.

## Effective dates and precedence

- Treat a blank `Effective from` as no lower bound and a blank `Effective to` as no upper bound.
- Select only active rows whose date range contains the supplier document, transaction, or payment date used by the ledger.
- Apply precedence in this order: matching `FY Overrides`, matching dated configuration row, matching undated default row, generic skill rule.
- If several active rows match at the same precedence, do not choose silently. Mark the result `Review` and report the overlap.
- Do not rewrite historical rows merely because the current default changes.

## Authority

The workbook describes desired behaviour but does not authorise mutations by itself. Require an explicitly authorised live run before uploading evidence, writing ledger rows, applying labels, or archiving email. Never interpret stored workflow policy as permission to delete records.

## Spreadsheet template

Read the configured spreadsheet-template identifier from `Systems`. Use it only when the user authorises creating a new financial-year ledger. Copy the template, rename the copy for the target FY, register its identifier in `FY Resources`, apply relevant recurring checks, and verify the copied schema before processing transactions.
