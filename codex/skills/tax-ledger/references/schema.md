# Ledger schema

Use a flat transaction table with these columns unless the target tab has an explicitly approved schema:

| Column | Meaning |
|---|---|
| Date | Supplier document or transaction date |
| Vendor | Supplier name |
| Category | Water, energy, internet, council rates, insurance, repairs, registration, software, and similar |
| Description | Concise purpose |
| Amount | Full GST-inclusive total paid or payable |
| GST treatment | Supplier GST information plus whether a credit is claimed |
| GST shown | GST stated on evidence, for information; blank when unsupported |
| GST credit claimed | Credit claimed in the ledger; use zero for post-cancellation rental expenses under the recorded tax profile |
| Tax claim amount | Expense amount carried for tax review; use the full GST-inclusive amount for post-cancellation rental expenses |
| Evidence | Accountant-accessible Drive link |
| Evidence status | Complete, Missing, Inadequate, or Login required |
| Evidence action | Concise retrieval action when evidence is not complete |
| Reference | Invoice, receipt, account, or transaction reference |
| Due or paid date | Relevant settlement date |
| Property | Property or business scope |
| Transaction status | Review, Reviewed, or Auto |
| Source email ID | Gmail message ID for duplicate prevention |
| Notes | Exceptions and user decisions |

Transaction status and evidence status are independent. Reviewing a transaction must not change its evidence status unless the evidence itself was checked.

For `GST treatment`, use `Not claimable` when GST may be included but no GST credit is claimed under the recorded tax profile. Do not combine it with `N/A`. Use `N/A` only when GST genuinely does not apply to the transaction.

## Evidence retrieval batch

For every row whose evidence status is not `Complete`, produce a combined batch list containing:

| Field | Meaning |
|---|---|
| Vendor | Supplier to contact or log into |
| Date | Relevant document, transaction, or payment date |
| Reference | Account, invoice, receipt, or transaction identifier |
| Amount | Amount needed to identify the document |
| Evidence status | Missing, Inadequate, or Login required |
| Required document | Receipt, tax invoice, bill, statement, or other evidence needed |
| Retrieval action | Portal, email, supplier contact, or other next action |

Do not insert section-heading rows into the transaction table. Preserve existing user tabs unless asked to migrate or replace them.
