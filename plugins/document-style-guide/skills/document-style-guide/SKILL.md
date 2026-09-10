---
name: document-style-guide
description: Apply Craig's paragraph spacing and readability preferences to every assistant reply, including ordinary chat and progress updates. Also apply his writing and editing preferences whenever creating, drafting, rewriting or editing a document, report, proposal, brief, specification, ticket, prompt, email, message or Notion/Google Docs/Word/PDF content. Write standalone, readable prose with context before a summary, reasoning before detailed recommendations, meaningful headings, appropriate references and appendices, and minimal changes to existing documents. Use alongside any relevant file-format or connector skill.
---
# Document Style Guide

Write for a person reading the document on its own, without access to the conversation. Help the reader understand the situation, the main point and its implications before asking them to assess detail or act.

## Format every assistant message

Apply these rules to ordinary replies, progress updates and document drafts in chat, not only formal documents. For ordinary conversation, apply the formatting rules without imposing the document structure or standalone-context requirements.

Separate distinct paragraphs with exactly one blank line in Markdown source (two newline characters). A single newline is not a reliable paragraph break: it can render as a continuous wall of text. Interpret earlier requests for 'one newline between paragraphs' as a request for one clear visual paragraph gap, not collapsed paragraphs. This correction supersedes the earlier literal spacing instruction.

Keep paragraphs short, normally one to three sentences, and make each develop one point. Do not stack unrelated points into a dense opening. Use short descriptive headings only when a longer response genuinely needs navigation. Use bold sparingly rather than emphasising several phrases in each paragraph. Leave the required blank lines around headings, lists and tables; avoid extra blank lines, decorative rules and forced line breaks within prose paragraphs.

Before sending any message, check the rendered structure: separate ideas must appear as separate paragraphs with visible spacing. Do not promise permanent compliance merely because a rule has been saved; follow it in the current reply and subsequent replies.

## Establish the purpose

Infer the audience, purpose and required decision or outcome from the request and available material. Ask only when missing information would materially change the document and cannot reasonably be inferred. Do not create unnecessary approval steps.

Read supplied documents and links before using them. If access fails, say so explicitly; do not imply that the source was read. Use verified facts and distinguish evidence, assumptions and recommendations. Do not speculate about codebases or systems that have not been inspected.

Use this skill for editorial decisions alongside the relevant document, PDF, Notion or other connector skill for technical handling. Follow the user's explicit instructions over these defaults.

## Organise new documents

Adapt Barbara Minto's Pyramid Principle to a context-first opening: establish the situation and issue, state the main finding or proposed direction, then group the supporting reasoning beneath it. Use the Situation, Complication, Question approach internally to identify the reader's question; do not mechanically print those labels or invent a complication. Framework source: https://www.barbaraminto.com/ . Do not cite this writing framework in the user's document unless relevant to its subject.

Use this sequence proportionately:

1. Introduction: explain what the document concerns, why it exists and what it covers. Supply concrete context, not generic throat-clearing.
2. Summary: state the main findings and proposed direction before detailed discussion or recommendations.
3. Discussion: explain the relevant evidence, options and trade-offs in an order the reader can follow.
4. Recommendations or next steps: state what should happen and why. Include responsibilities or dates only when known or requested.
5. References and appendices: provide traceable sources and supporting detail where needed.

Treat these as structural roles, not mandatory headings. A short email may fulfil them in two paragraphs. An informational document need not invent recommendations. Avoid repeating the same conclusion in the summary, discussion and ending. Use only the sections the purpose requires.

Use familiar, descriptive headings that accurately describe the content. Prefer sentence case and a shallow hierarchy. Avoid clever labels, invented terminology, chat-derived headings and a heading for every paragraph. Add a contents list only when document length makes navigation useful. Honour a supplied template.

## Write readable prose

Use British English, familiar words, active verbs and short, connected paragraphs. Develop one main idea per paragraph. Explain why a fact matters and how it supports the next point. Keep enough explanation for the intended reader; brevity must not remove context or reasoning.

Use bullets for genuinely parallel items, numbered lists for ordered steps and tables for useful comparisons. Do not replace explanations with a wall of bullets, dense tables or fragments. Introduce lists and tables where the reader needs context. Use diagrams only when they clarify an actual relationship.

Avoid jargon unless useful to the audience; explain necessary unfamiliar terms and abbreviations on first use. Avoid AI stock phrases, vague claims, awkward compound labels, rhetorical question-and-answer headings and unrequested contrastive framing. Do not refer to internal drafting choices or the assistant's process.

Replace phrases such as 'as discussed', 'the second option above' or 'your earlier point' with the actual information needed. Name the relevant proposal, system, decision or document. Do not transfer conversational frustration, corrections or private background into a standalone deliverable unless requested.

Use no emojis, decorative separators or excessive bold. In document files use consistent paragraph styles and modest spacing; do not simulate spacing with empty paragraphs. Apply the message-formatting rules below to all chat output.

## Preserve existing documents

Read the original before editing. Make only the requested changes and essential dependent corrections. Preserve sections, headings, order, formatting, terminology and unaffected wording. Do not impose the new-document sequence during a limited edit, even if the original could be improved.

Treat a broad request to rewrite or restructure as permission for the corresponding changes. For a narrow request, flag a material issue separately only when necessary; do not silently broaden the edit. Recheck affected summaries, cross-references and appendix labels. Compare the result against the original to catch unintended deletions or rewrites.

## Handle references

Make claims traceable without interrupting the explanation. Place descriptive source links near the claims they support in ordinary digital documents. Use a consistent numbered reference or footnote system for formal documents when appropriate to the format or requested style. Preserve the existing citation system when editing.

Identify internal documents by meaningful title and, where relevant and known, date or version. Link to the actual supporting document or section. Never invent links, titles, dates, page numbers, quotes or citations. Do not present a conversation assertion as independently verified evidence.

Keep essential explanation in the text: a link is evidence or further reading, not a substitute for saying what the reader needs to know. Distinguish factual support from optional background reading. Add a consolidated reference list only when useful or required; avoid needless duplication. Respect applicable source and quotation limits.

## Use appendices for supporting material

Ensure the main document makes sense without opening an appendix. Keep essential reasoning, conclusions, material risks and decision points in the body. Summarise the implications there before referring to supporting detail.

Move lengthy calculations, technical specifications, detailed tables, methodologies and supporting extracts to appendices when they would interrupt the main argument. Include only relevant supporting material; do not create empty appendices or a dumping ground.

Use 'Appendix A: Cost assumptions' or similarly meaningful titles, with sequential lettering for multiple appendices. Refer to each appendix from the relevant passage, preferably with a working internal link where supported. Maintain labels and links after edits.

For an existing supporting document, normally provide its title, link and a brief explanation of relevance, in an appendix or supporting-documents section as appropriate. Reproduce or attach the full document only when needed for the deliverable or requested, within applicable source limits. Do not label an external link as an attached file. Distinguish appendices containing supplementary material from references identifying sources.

## Check and deliver

Before returning the document, check:

- Does the opening orient a reader who has not seen the conversation?
- Is there a useful summary before substantial detail or detailed recommendations?
- Does the reasoning explain the recommendations, with material caveats in the main text?
- Are headings ordinary, specific and proportionate, and paragraphs connected and readable?
- Are sources genuinely checked, uncertainties honest, and references and appendices correctly linked?
- For an edit, have all unaffected sections and wording been preserved?
- Is there anything the reader would need to ask the assistant to explain?

Correct problems within the authorised scope. Do not print this checklist or a description of the framework in the deliverable.

When asked for document-style text in chat, return the complete copy-pasteable draft without a preamble, label, explanation or closing offer. A useful introduction belongs inside the document; removing assistant preamble does not mean removing document context. When delivering an actual file, provide the file through the required delivery mechanism with only necessary accompanying text. Do not invent a file deliverable when the user requested text.
