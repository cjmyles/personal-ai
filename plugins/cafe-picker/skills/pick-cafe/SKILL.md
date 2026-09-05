---
name: pick-cafe
description: "Pick, add, or update cafes for Craig using the lightweight Thao Dien Cafes Notion database. Use when Craig asks where to work from, wants a cafe suggestion, adds a cafe, or updates cafe notes."
---

# Pick Cafe

Use Craig's Notion cafe database as the decision layer and Google Maps links as the map layer.

## Data source

- Database: `Thao Dien Cafes`
- Database URL: `https://app.notion.com/p/490adfa3dc6a476ebe402a35d18133dd`
- Data source URL: `collection://bbf365ec-b28e-4e18-bc68-aa858b2b4747`

## Schema

Use only this lightweight first-version schema unless Craig asks to expand it:

- `Name`: Cafe name.
- `Status`: `Favourite`, `Want to try`, `Tried`, or `Avoid`.
- `Type`: `Laptop cafe`, `Local cafe`, `Brunch cafe`, or `Evening cafe`.
- `Area`: `Thao Dien`, `An Phu`, `District 2 nearby`, or `Other`.
- `Vibe tags`: Any of `Quiet`, `Comfortable`, `Pretty`, `Good coffee`, `Good food`, `Cheap`, `Reliable`.
- `Google Maps link`: Link for location and directions.
- `Last visited`: Optional date.
- `Notes`: Short free-text notes.

Do not require Craig to maintain detailed attributes like power sockets, Wi-Fi, table size, aircon, or seat comfort. If he gives that information naturally, capture it briefly in `Notes`; only add structured fields later if he asks.

## Picking logic

When Craig asks for a cafe recommendation:

1. Query the Notion database for usable cafes, excluding `Avoid` unless he explicitly asks.
2. Prefer one clear recommendation and one backup, not a long shortlist.
3. Match the current need:
   - Laptop work: prioritise `Laptop cafe`, `Quiet`, `Comfortable`, and `Reliable`.
   - Low decision energy: prioritise `Favourite` and `Reliable`.
   - Novelty: prioritise `Want to try`, but avoid places that look unsuitable for laptop work if he asked to work.
   - Weekend or relaxed visit: prioritise `Local cafe`, `Brunch cafe`, `Pretty`, `Good food`, or `Good coffee`.
4. If the database has too little information, say so and make the best pick from the known fields.
5. Include the Google Maps link when available.

Output format:

- `Pick`: One cafe and why.
- `Backup`: One alternative and why.
- `Note`: Any relevant uncertainty or missing data.

Keep the answer short. The goal is to reduce decision drag, not create another planning exercise.

## Adding or updating cafes

When Craig provides a cafe name, link, or feedback:

- Search the database first to avoid duplicates.
- Add new cafes with the minimum useful fields.
- Update existing cafes rather than creating duplicates.
- Use `Notes` for informal observations.
- Ask a clarifying question only if the missing field would materially change the record.

## Recommendation sourcing

For new cafe discovery, use current sources when available:

- Google Maps or web search for Thao Dien / An Phu cafes.
- Local blogs, Instagram, Reddit, expat groups, and recent review pages.
- Craig's own saved Google Maps lists when he exports or provides them.

Separate sourced facts from inference. Do not invent opening hours, laptop suitability, or amenities without evidence.

