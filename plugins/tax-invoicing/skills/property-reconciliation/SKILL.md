---
name: property-reconciliation
description: Reconcile rental income, managing-agent statements, bank payouts and property expenses. Use for MadeComfy or Key Flickers payment checks, Wentworth St reconciliation, recurring property cashflow reviews and retries after missing evidence. Supports authorised live scheduled runs and read-only previews.
---

# Property Reconciliation

Maintain a private reconciliation record for each configured property, linked to its existing Personal Todo card. Verify income completeness, agent deductions and actual receipts separately. Keep private amounts, account identifiers, source links and run state out of this package.

## Required sources

Read [reconciliation.md](references/reconciliation.md) and [run-state.md](references/run-state.md) every run. Load the current canonical Personal Todo skill and its `references/linked-reminders.md` from `cjmyles/personal-ai/plugins/personal-todo/skills/personal-todo/` before task or reminder changes.

Use connected GitHub, personal Gmail, Notion, Trello and personal Google Calendar. Resolve Craig's personal accounts from live connection metadata. Discover configured properties from existing reconciliation cards on the Personal Todo board; use their saved ledger links. Supplier dashboards, bank exports and existing tax workbooks are evidence sources when accessible, not assumed connections. Never rely on a local browser session in a cloud run.

## Run workflow

1. Establish mode and freeze a run-start UTC timestamp. Honour preview/review-only as no-write. Craig's explicit recurring setup authorises verified bookkeeping and private task/reminder updates. Default to the previous complete calendar month in the property's jurisdiction; also revisit every unresolved older period. Use Craig's current stated timezone for review reminders.
2. Read the live property record, recurring card, dedicated checklists and saved state. Search active/completed cards before creating anything. Preserve separate fee-negotiation, repairs and payment tasks. Do not infer an empty checklist from the general card response.
3. Search received, sent and archived personal email by agent, property/unit reference and relevant suppliers. Paginate fully; read material bodies and attachments, including complete extraction when previews are truncated. Search the period, prior carry-forwards and subsequent payments through run start. Record statement dates, booking/check-in cut-offs and collection cut-offs separately; do not apply last month's cut-offs automatically.
4. Apply reconciliation.md. Match reservation-level income, deductions, carry-forwards and owner payouts to independent evidence where available. Report statement-to-bank match separately from completeness/fee validation. A low payout alone is not proof of underpayment. Missing bank evidence, booking exports or agreed fee terms must remain explicit blockers.
5. In live mode, re-read destinations before writing. Update the existing Notion reconciliation record with evidenced rows/corrections, stable keys, source links and unresolved questions, then verify by reading it back. Preserve unrelated content and previous findings. Reference existing tax-ledger records; do not copy them into tax totals or change tax treatment.
6. Update the same Trello card and applicable existing related cards with a verified timestamp, findings, missing evidence and next action. Update checklist items only when their specific outcome is evidenced. Keep the recurring card open. Reconcile the current Calendar review instance and next occurrence under linked-reminders.md; never mark the entire future series Done or silence future alerts.
7. Save compact state last, after read-backs. Retain unresolved periods across rollovers and report partial saves for repair. If an app is unavailable, complete independent checks and report the exact missing source/save; do not fabricate findings or erase pending state.
8. Deliver a concise result: period, statement payout, bank receipts, verified difference, income/fee completeness status, material property expenses, outstanding evidence and next action. Do not claim scheduled notification delivery from configuration or a successful run.

## Boundaries

Do not pay bills, transfer money, send emails to agents, change contracts or pricing, lodge tax returns, alter tax/BAS records or initiate new automations during an unattended run. Draft any unresolved agent query for Craig's review. Keep repairs/negotiations open until their own outcomes are confirmed. Use signed-in browser access only in an interactive task with explicit site intent; if unavailable, record the export needed.

## Recovery invocation

Keep the automation prompt as a pointer to this canonical workflow:

> Read https://github.com/cjmyles/personal-ai/blob/main/plugins/tax-invoicing/skills/property-reconciliation/SKILL.md through the connected GitHub app and run the reconciliation, loading its required skills and references from the same repository. If the canonical instructions cannot be read, report that failure rather than using remembered or stale instructions.

Manage cadence in the automation app. Keep property configuration and recovery IDs in private Trello records; do not add a duplicate schedule file to the repository.
