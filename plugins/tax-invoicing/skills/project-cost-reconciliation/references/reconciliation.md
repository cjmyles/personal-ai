# Evidence, allocation and balances

## Source of truth

Resolve the single private Notion page titled Project Finances using the recurring card's link or Notion search. Read its current policy and entries. If duplicates or conflicting agreements exist, report the ambiguity; do not select a convenient balance. The ledger records expenses and contributions, not revenue unless expressly recorded as such.

Record each expense's stable key, supplier, billing account/organisation, invoice/line ID, service period, named project, allocation basis/effective date, original currency/amount, paid date, actual AUD settlement, payer, status and evidence links. Store only necessary fields in private records. Avoid full card/bank numbers.

A stable expense key combines supplier + account/organisation + invoice ID + line/period + project allocation. Use payment/transaction IDs to distinguish split payments from duplicates. Without reliable IDs, match date, currency, amount, payer and reference, and flag ambiguous matches. An emailed receipt and card charge for the same expense are two evidence sources, not two expenses.

## Paid versus pending

- Interim usage recaps and estimates remain pending; do not enter them as paid invoices.
- An invoice alone proves a liability, not payment. A supplier paid receipt can verify payment in its currency, but does not establish the actual AUD card amount.
- Use actual AUD settlement from a transaction/statement or explicit user confirmation. A converted estimate is not a paid AUD cost. Keep verified foreign-currency payments pending AUD valuation until supported; do not guess FX.
- Store service period, invoice date and payment date separately. Detect overlap with amounts already recorded.
- Record refunds/credits only once against the related expense, with evidence and sign. Distinguish a pending supplier credit from money actually refunded.
- Keep future renewals and proposed purchases outside paid totals.

## Allocation

Read effective-dated rules from the ledger. For shared fixed subscriptions, use only the agreed account/period split; do not change it when projects are added or deleted without authority. Attribute metered charges using named-project evidence for that exact period. Explain how credits, free allowances, shared fees and tax were allocated and reconcile allocated totals back to the invoice and actual AUD charge.

Do not assume a Neon organisation is one project, add interim snapshots as independent charges, reuse a previous month's usage ratio for a new month, or assume compute-only ratios allocate storage/other charges correctly. If direct cost attribution is unavailable, label any authorised estimate explicitly and exclude unapproved estimates from final settlement claims. Prior historical estimates stay labelled; correct them only with evidence and an adjustment trail.

Round in AUD cents only after calculating allocation. Distribute rounding residual deterministically and disclose a material correction; the sum of project allocations must equal the allocatable paid charge. Keep unrelated project shares outside the partner ledgers.

## Partner balance arithmetic

For each project:

- Total paid project cost = verified allocated expenses less verified refunds.
- Net contribution per person = direct costs paid + transfers made to partners - transfers received from partners.
- Fair share = total cost × the recorded ownership/cost share.
- Credit = net contribution - fair share. Positive means owed money; negative means owes money.

Partner transfers do not increase expenses. Include costs paid directly by a partner as well as their transfers; do not treat either twice. Reconcile summed net contributions to total paid costs and summed credits to zero, allowing no unexplained residual. Do not describe a provisional 50/50 assumption as an agreed settlement demand.

`scripts/balances.py` accepts a JSON object with `shares`, `expenses` and `transfers`; all amounts must already be verified AUD. It rejects duplicate record IDs, unknown parties, invalid shares and unsupported currencies. Pending entries are omitted with a count. Keep the input/output private and inspect its totals; the script cannot validate invoices, allocation evidence or permission.
