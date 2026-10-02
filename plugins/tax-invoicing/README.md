# Tax & Invoicing

Bundles three separate skills with their complete supporting references:

- **Tax Ledger**: Review receipts, invoices and monthly card statements; preserve source evidence; maintain financial-year records; match actual AUD settlements conservatively; flag missing expenses and unusual spending; track statement repayment separately.
- **Project Cost Reconciliation**: Reconcile verified supplier costs by project, actual AUD settlements and partner contributions; maintain the private Notion ledger and linked monthly Trello/Calendar reviews. Scheduled runs load the canonical skill through GitHub and retain missing evidence as pending.
- **Invoice Ledger**: Reconcile operational invoices and payments, maintain workbook joins and carry out explicitly authorised invoice actions.

The plugin supplies workflow instructions, not service credentials or new connectors. Connect Gmail and Google Drive for tax records. Invoice Ledger reads the private Tax Ledger Configuration Sheet and requires access to the configured invoice system or its exports. Cloud tasks must have the relevant connections available; local browser sessions do not travel with this package.

Start with a read-only dry run in a fresh task. Existing skill approval boundaries remain unchanged.

Statement reconciliation reads `Statement Controls` in the private Tax Ledger Configuration workbook. Personal thresholds and account details stay there, not in this package. `Card Statements` and `Card Transactions` are supporting audit tabs, not additional tax-expense totals. On-demand processing never pays a bill or starts an automation. Unpaid statement emails stay in Inbox unless a verified payment reminder exists and the user explicitly approves archiving.

Run the statement safety regressions with `python3 -m unittest discover -s plugins/tax-invoicing/skills/tax-ledger/tests -v` from the repository root.

These skill folders are the canonical repository sources. The repository installer also supports installing them as standalone skills.

Project Cost Reconciliation requires GitHub, personal Gmail, Notion, Trello and Google Calendar. Supplier billing exports or authorised interactive dashboard access may be needed to finish a period. The workflow does not assume a browser session will be available to a scheduled cloud run. Cadence is managed in the app; the skill contains the recovery invocation and rules, without a duplicate schedule file.
