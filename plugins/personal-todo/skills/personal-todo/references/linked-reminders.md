# Linked reminders

## Authority and scope

Craig authorised a consistent Trello and personal Google Calendar reminder system on 29 September 2026. Maintain both for recurring bills, taxes, renewals and dated personal-admin or health reviews. This authority includes creating and updating private reminder events and corresponding cards; it does not authorise payments, policy changes, email sending or invitations. Honour review-only mode. Keep personal amounts, dates and identifiers in private Trello records, never in this repository.

Use one Trello card per obligation and one calendar event per confirmed occurrence. Keep Trello as the current obligation record and Calendar as its notification mirror. Existing personal calendar appointments and birthdays do not require duplicate task cards unless action is needed. Do not import unrelated work events or alter their reminders.

## Dates and evidence

Read the full notice and relevant attachment before recording a bill. Record amount/currency, billing period, actual payment deadline and its jurisdiction/timezone, payment method, evidence link, and status. Separate the legal/payment deadline from Craig's chosen work target. Preserve an earlier work commitment in the brief/list; never call it the bill deadline.

Use a confirmed bill deadline for the Trello due date. For a review or missing-notice check, label the date explicitly as a review date. Never invent a payment date or amount from a previous quarter. If a date is unknown, create a clearly labelled notice/renewal check in both systems; choose a sensible near-term review date and record it as assistant-selected. An annual notice may confirm several future instalments; record each occurrence on the same card and create matching events for them.

Distinguish outstanding, scheduled direct debit, paid, payment status unverified and awaiting notice. A scheduled debit, invoice, unread email or overdue card is not proof of payment or non-payment. For direct debit, use 'Check [bill] debit' rather than 'Pay [bill]' to avoid duplicate payment.

## Link and notify

1. Resolve the existing card, read its dedicated checklists, and search active/completed cards before creating a missing obligation card. Routine new verified personal bill/renewal cards are authorised under this reminder workflow; other unmatched email tasks remain proposals.
2. Discover the personal calendar, then look for an existing matching event using saved IDs, the Trello URL and bounded searches around both old and new dates. Read full details; do not match only on a common title. Reuse an unambiguous existing reminder; flag duplicates or conflicting manual dates instead of deleting them.
3. Create each deadline/review event as private, transparent, with no guests or conference. Use 09:00 in Craig's stated timezone and a 15-minute display duration for date-only reminders, recording the actual deadline date/timezone separately. Preserve any explicit source cutoff; choose an earlier reminder if needed to avoid passing that cutoff. Do not reinterpret 09:00 as a legal deadline.
4. Set notification overrides to seven days (10080 minutes) and two days (2880 minutes) before the event. If either has already passed but the event is still in the future, retain the upcoming notification and add an alert at event start; mention imminent items in today's briefing. For an already-past event, surface its unresolved status in the briefing; do not add a retroactive alert. If a new follow-up is needed, use a separate, clearly labelled future review occurrence without changing the historical deadline. Do not schedule an alert in the past or claim it was delivered.
5. Include the Trello URL and a stable marker `Personal Todo reminder: <card ID> | <occurrence key>` in the event description. An occurrence key identifies the bill period or review, not its mutable due date. Record calendar ID, event ID, event URL, occurrence key, reminder date, actual deadline/review date, status and source link in a compact `Linked reminders` JSON block on the card. Never store credentials or full bank/payment identifiers.
6. Re-read the card before saving, preserve concurrent edits/history, append a timestamped update, and read back both the event and card. Treat the pair as saved only when both match. Search for the marker on retry if event creation succeeded but the card save failed; do not create a duplicate. Keep partial failures visible and retry repair on subsequent runs.

## Reconcile each daily run

Inspect registered reminder cards independently of the email checkpoint, including future occurrences, completed current periods and unresolved repairs. Search new personal email and relevant attachments for notices, changed amounts/dates, receipts and failed debits. For existing registered providers, search by sender/account context as well as task title. Check for missing expected notices even when no new email arrived.

Update linked reminders when a verified deadline changes. Preserve unrelated calendar content and existing task priorities. If Craig manually changes or deletes a reminder in conflict with saved state, flag the discrepancy; do not silently recreate or overwrite his decision. A missing counterpart never counts as fully synchronised.

Include outstanding payments due within seven days, due today and unresolved past deadlines in the briefing. Describe past deadlines without payment evidence as 'payment status unverified', not definitely unpaid. On Mondays include the week's reminders with the calendar agenda. Avoid repeating one obligation in several sections.

On explicit confirmation or unambiguous receipt, mark only the matching period paid, retain dated payment history, prefix its event 'Paid' and disable its remaining alerts (`use_default: false`, empty overrides). Use 'Done' for completed reviews. Preserve the event as history; do not delete it or silence future instalments. Apply the same behaviour when completion is reported in an ordinary Personal Todo conversation.

Then roll the same obligation card to its next verified occurrence and keep it open in Scheduled; if the next deadline is unknown, create a labelled notice-check occurrence and retain the old paid record. Do not leave the old bill showing as overdue or copy its amount into a new payable demand. If the connector cannot reset completion/remove an obsolete due date, record the accurate current state, report the limitation and avoid claiming a completed rollover.

Report calendar/Trello access failures and unsaved pairs clearly. Do not advance the successful briefing checkpoint while a required reminder reconciliation remains incomplete. Never describe scheduled notifications as proof of device delivery.
