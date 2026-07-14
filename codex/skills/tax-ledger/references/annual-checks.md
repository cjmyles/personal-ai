# Annual tax-return checks

Use these expectations to reconcile a financial year after transaction processing. They are completeness checks, not tax advice and not substitutes for source evidence.

## Method

For each applicable check:

1. Count distinct transactions after duplicate matching by supplier reference, date, amount, and source email ID.
2. Compare the count and covered periods with the expectation.
3. Report `Pass`, `Review`, or `Not applicable`.
4. List missing periods, possible duplicates, irregular amounts, incomplete evidence, and any reason the expectation changed.
5. Do not create a missing transaction without source evidence.

Use `Review` when the count differs, periods overlap, service started or ended during the year, billing frequency changed, or evidence is incomplete. A matching count does not override other transaction or evidence reviews.

## Financial-year boundaries

For every financial year, inspect the two weeks on both sides of the opening and closing 1 July boundaries. Compare the target ledger with the adjacent financial-year ledgers and source evidence. Assign each transaction using the supplier document, transaction, or payment date rather than the email arrival date, and report omissions, duplicates, or items filed in the wrong financial year.

Keep a `Financial-year boundary allocation` row in the annual-check results with status `Review` until both boundary windows have been reconciled. Do not create an adjacent-year ledger or invent a transaction when source evidence or the adjacent ledger is unavailable.

## Prior-year tax return preparation fee

For every financial year, check whether an accountant or registered tax agent issued or was paid an invoice during the target year for preparing the previous year's tax return. Search Gmail, Drive, and the existing ledger, then confirm any qualifying fee is recorded once using the supplier document or payment date and linked to suitable evidence.

Keep a `Prior-year tax return preparation fee` row in the annual-check results with status `Review` until the check is completed. Use `Pass` when the fee is found and recorded, and `Not applicable` only when no such fee was incurred in the target year. Do not treat an ATO income-tax assessment, tax payable balance, penalty, or interest charge as a tax-return preparation fee. Flag any uncertainty for accountant confirmation rather than creating a transaction.

## Personal business expenses

| Check | Expected for a full year | Match rule | Review triggers |
|---|---:|---|---|
| Apple iCloud | 12 monthly charges while the subscription is active | One distinct Apple iCloud charge for each active month | Missing or repeated month; subscription, plan, price, or Apple ID change; credit or refund; personal or mixed use; incomplete evidence |
| Optus mobile phone | 12 monthly bills while the service is active | One distinct Optus mobile bill for each active month | Missing or repeated month; service, plan, phone number, or price change; handset or device component; credit or refund; personal or mixed use; incomplete evidence |
| BizCover insurance | One active annual policy or a complete series of instalments covering the financial year | Match the policy schedule and tax invoice to the coverage period, then reconcile each payment once | Missing or overlapping coverage; renewal, cancellation, refund, policy, insurer, or payment-frequency change; incomplete evidence |

## Wentworth St

| Check | Expected for a full year | Match rule | Review triggers |
|---|---:|---|---|
| Belong internet | 12 monthly charges | One distinct Belong internet charge for each month from July through June | Missing or repeated month; more or fewer than 12 charges; service start, cancellation, credit, refund, or billing-cycle change; material amount variation; incomplete evidence |
| EnergyAustralia electricity | 4 quarterly bills | Four distinct electricity bills whose service periods provide continuous coverage through the financial year | Missing or repeated period; more or fewer than 4 bills; a gap or overlap between service periods; account or billing-frequency change; credit, refund, or irregular charge; incomplete evidence |
| EnergyAustralia gas | 4 quarterly bills | Four distinct gas bills whose service periods provide continuous coverage through the financial year | Missing or repeated period; more or fewer than 4 bills; a gap or overlap between service periods; account or billing-frequency change; credit, refund, or irregular charge; incomplete evidence |
| Sydney Water | 4 quarterly bills | Four distinct Sydney Water bills for the Wentworth St payment number, with one bill due in each quarter | Missing or repeated quarter; more or fewer than 4 bills; account change; failed payment, late fee, credit, refund, or irregular charge; incomplete evidence |
| Home contents insurance | One active policy covering the property through the financial year, or a complete series of instalments | Match the policy schedule and renewal to the Wentworth St address and coverage period, then reconcile each payment once | Missing or overlapping coverage; renewal, cancellation, refund, insurer, policy scope, or payment-frequency change; building, landlord, contents, private, or mixed-use ambiguity; incomplete evidence |
| STRA registration | A current registration or renewal for every period in which the property operated as short-term rental accommodation | Treat the invoice, payment confirmation, and renewal notice for one registration payment as one transaction | Registration or expiry gap; duplicate renewal; refund; property or registration-number mismatch; incomplete evidence |
| Northern Beaches Council rates | The annual rates notice and every required instalment or payment for the financial year | Match the annual notice, instalment notices, adjustments, and payments by property and account reference; use the source arrangement rather than assuming a fixed instalment count | Missing notice or required payment; duplicate; adjustment, refund, or account change; property mismatch; incomplete evidence |

## Results

Keep annual-check results separate from the flat transaction tables. When a spreadsheet check tab is authorised, use one row per check with:

| Field | Meaning |
|---|---|
| Financial year | FY being reconciled |
| Scope | Property or business scope |
| Check | Human-readable expectation |
| Expected | Expected count or condition |
| Found | Distinct qualifying records found |
| Coverage | Months or periods represented |
| Status | Pass, Review, or Not applicable |
| Exceptions | Missing periods, duplicates, irregular values, or changed circumstances |
| Last checked | Date the reconciliation was run |

Only change an expectation after checking the supplier arrangement or recording a user decision. Preserve the reason for any effective-dated change.
