# Tax & Invoicing

Bundles two separate skills with their complete supporting references:

- **Tax Ledger**: Review receipts, invoices and monthly card statements; preserve source evidence; maintain financial-year records; match actual AUD settlements conservatively; flag missing expenses and unusual spending; track statement repayment separately.
- **Invoice Ledger**: Reconcile operational invoices and payments, maintain workbook joins and carry out explicitly authorised invoice actions.

The plugin supplies workflow instructions, not service credentials or new connectors. Connect Gmail and Google Drive for tax records. Invoice Ledger reads the private Tax Ledger Configuration Sheet and requires access to the configured invoice system or its exports. Cloud tasks must have the relevant connections available; local browser sessions do not travel with this package.

Start with a read-only dry run in a fresh task. Existing skill approval boundaries remain unchanged.

Statement reconciliation reads `Statement Controls` in the private Tax Ledger Configuration workbook. Personal thresholds and account details stay there, not in this package. `Card Statements` and `Card Transactions` are supporting audit tabs, not additional tax-expense totals. On-demand processing never pays a bill or starts an automation. Unpaid statement emails stay in Inbox unless a verified payment reminder exists and the user explicitly approves archiving.

Run the statement safety regressions with `python3 -m unittest discover -s plugins/tax-invoicing/skills/tax-ledger/tests -v` from the repository root.

These skill folders are the canonical repository sources. The repository installer also supports installing them as standalone skills.
