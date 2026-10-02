---
name: project-cost-reconciliation
description: Reconcile shared project expenses, supplier invoices, actual AUD payments and partner contributions; allocate costs by project, update the private Project Finances ledger and calculate settlement balances. Use for monthly project-cost reviews, Neon/Vercel reconciliation, partner balances and retries after missing evidence. Supports authorised live scheduled runs and read-only previews.
---

# Project Cost Reconciliation

Keep Notion's private **Project Finances** page as the ledger. Use one linked Personal Todo card for recurring reconciliation and separate existing cards for partner agreement or cost-reduction work. Never store financial records, account identifiers, balances or credentials in this package.

## Required sources

Read [reconciliation.md](references/reconciliation.md) and [run-state.md](references/run-state.md) every run. Before task/reminder changes, also load the current canonical Personal Todo skill and its `references/linked-reminders.md` from `cjmyles/personal-ai`, under `plugins/personal-todo/skills/personal-todo/`.

The standard run uses the connected GitHub, personal Gmail, Notion, Trello and personal Google Calendar apps. Resolve personal account identity from the live connections; never use a work mailbox by accident. Use private configuration on the recurring card and the live ledger for project ownership, allocation rules and source links. Supplier dashboards/exports are supplementary evidence, not an assumed connection.

## Run workflow

1. Establish mode and period. A scheduled run under Craig's explicit setup authorisation may reconcile verified evidence into existing records. An explicit preview/audit/review-only request must not write. Default to the previous complete calendar month in Craig's timezone and revisit unresolved older periods from saved state. Freeze a run-start UTC timestamp.
2. Read the live ledger, recurring card, dedicated Trello checklists and saved state. Search active/completed cards and relevant calendar dates to avoid duplicates. Do not replace current facts with remembered balances. Discover the current allocation agreements; label assumptions still awaiting partner agreement.
3. Search all personal received/sent/archived mail for the relevant suppliers, invoices, receipts, refunds and contributions; paginate fully and read material bodies/attachments. Search around the service period and into the payment month through run start. Do not equate invoice date with usage period. Follow explicit known evidence links. Include final invoices arriving after month-end.
4. Match supplier accounts/organisations and named projects to the ledger. Use a project-level usage/cost export when a bill spans projects. An organisation recap is not a project allocation. Prefer connected billing APIs or saved exports. In an interactive run, a specifically authorised signed-in browser can help; inspect which browser/tab is actually accessible. Never assume a local or built-in session is shared with a cloud task. In unattended runs, record missing access/export as a blocker and continue independent records; do not request credentials or repeatedly launch login.
5. Apply the evidence and calculation rules in reconciliation.md. Produce a proposed change set with stable keys, paid/pending distinction and settlement calculations. The bundled calculator is an optional arithmetic check, not proof of source evidence.
6. In live mode, re-read before writing. Preserve unrelated content, prior entries and history; apply only evidenced additions/corrections. Update the existing Notion ledger first and read it back. Link corrected/superseded records instead of silently deleting history. Then update the recurring Trello card and relevant existing agreement/cost-reduction tasks with a verified local timestamp, source links, outstanding evidence and responsibility. Never close an agreement task merely because arithmetic is complete.
7. Reconcile the linked Calendar occurrence and next review under the linked-reminders contract. Mark only a fully reconciled period's review Done and disable only its alerts; keep the recurring card open. If a period is blocked, retain it in pending periods and keep its status visible even when the next monthly review is scheduled. Do not mark incomplete periods complete or mute their alerts as if completed. Preserve future reminders and manually changed dates. Verify card/event pairs and save state last.
8. Report briefly: period, verified paid additions by project, partner balances/direction, assumptions, missing evidence, next action, and saves that failed. Say 'recorded balance excluding pending costs' when incomplete. Do not infer notification delivery from a successful scheduled run.

## Boundaries

This workflow authorises bookkeeping and private task/reminder updates only. Do not pay, renew, transfer money, send partner emails, issue invoices, change supplier plans or tax/BAS records, or change allocation agreements. Reference records already processed by Tax Ledger rather than counting them again as extra expenses. Creating this skill does not change the approval rules of Tax Ledger or Invoice Ledger.

## Scheduled invocation and recovery

The event prompt is only:

> Read https://github.com/cjmyles/personal-ai/blob/main/plugins/tax-invoicing/skills/project-cost-reconciliation/SKILL.md through the connected GitHub app and run the reconciliation, loading its required skills and references from the same repository. If the canonical instructions cannot be read, report that failure rather than using remembered or stale instructions.

Cadence/time live in the scheduled-event app; the private task/calendar mirror the chosen review date. Do not maintain a second schedule file in the repository. Before creating/recreating an event, inspect existing events and successfully read each required connected app. A scheduled execution must never create another automation. Changing timing in one system is a discrepancy to reconcile explicitly, not permission to overwrite a manual change.
