# Ledger schema

Use a flat transaction table with these columns unless the target tab has an explicitly approved schema:

| Column | Meaning |
|---|---|
| Date | Supplier document or transaction date |
| Vendor | Supplier name |
| Category | Water, energy, internet, council rates, insurance, repairs, registration, software, and similar |
| Description | Concise purpose |
| Amount | GST-inclusive total paid or payable |
| GST treatment | GST included, GST-free, input taxed, mixed, or review |
| GST amount | Supported GST amount; blank when unsupported |
| Amount ex GST | Amount less supported GST |
| Evidence | Accountant-accessible Drive link |
| Reference | Invoice, receipt, account, or transaction reference |
| Due or paid date | Relevant settlement date |
| Property | Property or business scope |
| Status | Review, Reviewed, or Auto |
| Source email ID | Gmail message ID for duplicate prevention |
| Notes | Exceptions and user decisions |

Do not insert section-heading rows into the transaction table. Preserve existing user tabs unless asked to migrate or replace them.
