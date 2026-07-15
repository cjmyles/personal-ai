# Supplier rules

Load supplier patterns, scopes, categories, evidence rules, and classification notes from active rows on the configuration workbook's `Supplier Mappings` tab.

## Match and classify

1. Match the supplier name, sender domain, account reference, and document description against configured supplier patterns.
2. Resolve dated mappings and FY overrides using `configuration.md`.
3. Confirm the supplier document supports the configured scope and category. Configuration guides classification but does not replace source evidence.
4. Apply evidence and classification notes only to the matching supplier, scope, and effective period.
5. Treat several messages or documents for one charge as one transaction when their supplier reference, date, and amount agree.
6. Mark the transaction `Review` when no mapping matches, several mappings have equal precedence, the document contradicts the mapping, or private, mixed-use, capital, or GST treatment remains uncertain.

Do not add a new persistent supplier rule to the skill. Record an authorised reusable decision in the configuration workbook instead; use an FY override for a one-year exception.
