---
name: write-craig-email
description: Draft, review, reply to, forward, or send email on Craig's behalf using his preferred voice, formatting, sign-off, and approval boundaries. Use whenever Craig asks to write or act on an email; do not use for merely reading or summarising email.
---

# Email

Write natural, concise email that sounds like Craig and fits the recipient and context.

## Style

- Use British English.
- Use first-person singular when referring to Craig or work Craig has done. Do not write `we` unless Craig is genuinely speaking for a group and the context requires it.
- Prefer direct, conversational language over formal or generic business phrasing.
- Preserve any wording, introduction, tone, recipient, subject, or sign-off Craig explicitly supplies.
- Unless Craig specifies otherwise, end on separate lines with:

  `Best,`

  `Craig`

## Formatting

- For HTML-capable email, use Trebuchet MS throughout the authored message. Wrap the body in `<div style="font-family:'Trebuchet MS',Arial,sans-serif;">...</div>` and use simple email-safe HTML.
- When the email tool supports multipart MIME, include both a readable `text/plain` alternative and the Trebuchet MS `text/html` version.
- A plain-text message cannot specify a font. Do not claim Trebuchet MS was preserved when only plain text was sent.
- Avoid decorative layouts, excessive emphasis, tracking pixels, external images, or elaborate signatures unless Craig asks for them.

## Drafting and sending

- Ground replies in the actual thread when it is available. Preserve the subject and reply context rather than starting an unrelated conversation.
- Do not invent recipients, addresses, attachments, commitments, dates, facts, or outcomes.
- Drafting, reviewing, or revising does not authorise sending. Create or update an unsent draft when Craig asks for a draft.
- Send only when Craig explicitly instructs sending, or explicitly approves the specific draft for sending.
- Before sending, verify the final recipients, subject, message content, reply context, and attachments. If a material field is unknown, stop and ask for it.
- After sending, report the recipient, subject, and whether the send succeeded. Do not imply delivery or a reply unless verified.

## Replies, added recipients and quoted history

- Treat conversation threading and visible quoted history as separate checks. A reply reference or matching subject does not include earlier message bodies for a newly added recipient.
- When adding someone to an existing exchange, preserve the original reply context, verify To/CC, and include the relevant prior correspondence in both plain-text and HTML bodies. Quote accurately with sender/date context; omit unrelated history and do not expose unrelated private material.
- Only say "below", "attached" or similar when the referenced material is actually present in the outgoing message.
- For replies that add recipients or depend on earlier correspondence, create and read back an unsent draft before sending. Verify its thread ID against the source conversation, reply headers where available, recipients, and quoted content. Existing authorisation to send covers this verification step; do not ask again merely because a draft was used.
- After sending, read back the sent message and verify its thread ID, recipients and relevant quoted content. A SENT label proves sending, not correct threading or included history. A missing thread ID in a filtered response is inconclusive; fetch the message or conversation before reporting a threading failure.
- If threading or history is wrong, explain the verified issue accurately. Do not send another correction without authorisation.
