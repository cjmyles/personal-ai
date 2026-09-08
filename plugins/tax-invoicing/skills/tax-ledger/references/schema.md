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
| Evidence | Accountant-accessible Drive link displayed as `View evidence`, not as a raw URL |
| Evidence status | Complete, Missing, Inadequate, or Login required |
| Evidence action | Concise retrieval action when evidence is not complete; use `N/A` when evidence is `Complete` |
| Reference | Invoice, receipt, account, or transaction reference |
| Due or paid date | Relevant settlement date |
| Property | Property or business scope; omit when the tab already has one explicit scope |
| Transaction status | Review, Reviewed, or Auto |
| Source email ID | Gmail message ID for duplicate prevention |
| Notes | Material exceptions or user decisions not already encoded in the rules |

Transaction status and evidence status are independent. Reviewing a transaction must not change its evidence status unless the evidence itself was checked.

For `GST treatment`, use `Not claimable` when GST may be included but no GST credit is claimed under the recorded tax profile. Do not combine it with `N/A`. Use `N/A` only when GST genuinely does not apply to the transaction.

## Foreign-currency amounts

- Translate foreign-currency income and expenses into AUD rather than leaving `Amount` blank solely because the card or bank statement is unavailable.
- Use the actual AUD amount charged or received when reliable evidence already provides it.
- Otherwise, use the RBA daily exchange rate for the transaction or payment date. If the RBA did not publish a rate that day, use the most recent prior published RBA rate. For a currency the RBA does not publish, use a reasonable authoritative external source.
- For cash-basis items, use the payment or receipt date when known. If an item is unpaid or its payment date is unknown, an invoice-date conversion may be recorded as provisional for identification, but do not treat it as a cash-basis tax claim; keep it `Review` until payment status and date are established.
- Record the original amount and currency, exchange rate, rate date, source, and calculation in `Notes`. Round the AUD ledger amount to cents while retaining the full rate used in `Notes`.
- A card or bank statement is not required solely to convert a supported foreign-currency amount. Request one only when the source currency or date is ambiguous, reliable evidence conflicts, or card fees, refunds, dynamic currency conversion, or another adjustment could materially change the actual AUD amount.
- Foreign VAT, sales tax, or similar tax is not Australian GST. Record zero Australian GST credit and identify any foreign tax clearly in `Notes`.

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
