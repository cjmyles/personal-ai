# Live configuration

Use a supplied configuration URL, otherwise find the unique exact-title `Tax Ledger Configuration` Google Sheet. Read metadata and bounded ranges. If ambiguous or inaccessible, stop affected writes rather than falling back to bundled personal facts.

Read `Systems`, `Workflow`, `Gmail Labels`, `Tax Profile`, `FY Resources`, `FY Overrides`, `Validation` and the relevant supplier/check rows. For statement work also read `Statement Controls`. Inspect exact destination tab headers, validation and current rows before writes. A Review flag blocks only the operations affected by its unresolved setting; do not infer missing settings from historic examples.

Keep account aliases (masked identifiers only), thresholds, mappings, evidence folders, financial-year dates, apportionments, tax rules and task destinations here or in FY-specific configuration, not in the skill. Apply effective-dated FY overrides ahead of shared defaults; unresolved overlaps need review. Configuration never grants authority beyond the live user instruction.

For statement work, `Statement Controls` uses Setting / Value / Status / Notes. It identifies the run mode, alert threshold/currency, matching date and FX tolerances, archive gate, supporting tab names, evidence path policy and budget destination. Unknown account details, amounts or dates remain unset until sourced. Never store credentials, full card numbers or access tokens.
