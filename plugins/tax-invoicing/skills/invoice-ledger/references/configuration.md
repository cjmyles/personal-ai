# Configuration

Use one private Google Sheet titled `Tax Ledger Configuration` as the source of truth.

## Discovery

1. Use a supplied configuration URL or ID.
2. Otherwise search for the exact title.
3. Continue only when one exact match exists.
4. Read metadata, then bounded ranges from visible tabs.
5. Check `Validation` before mutation.

## Required configuration

- `Systems`: invoice platform, workbook system and workflow skill.
- `Workflow`: read, prepare, issue/send, payment, readback and recovery boundaries.
- `Client Mappings`: source aliases to canonical and operational client names.
- `Invoice Status Mappings`: operational status to spreadsheet status rules.
- `Tax Profile`: effective-dated accounting basis and GST instructions.
- `Recurring Checks`: invoice, payment, BAS and FY validation checks.
- `FY Resources`: workbook and relevant tab identifiers.
- `FY Overrides`: dated exceptions and permitted cross-FY joins.

Configuration describes behaviour but never authorises a mutation by itself. Do not store credentials or access tokens in it.
