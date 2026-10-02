---
name: travel
description: Help the user plan and book travel, choose the correct passport, retrieve saved IDs and visas, manage reservations, check in and select free seats. Use whenever discussing booking flights, upcoming trips, travel documents, dual nationality, airline check-in or seating. Proactively remind the user which passport to use before booking and check-in.
---
# Travel

Prepare each journey using current bookings, original travel documents and official entry rules. Read references/preferences.md for instructions for resolving private preferences and documents. Follow the document-style-guide for any document deliverable.

## Find existing information first

Retrieve the itinerary, booking reference, passenger surname and operating-airline reference from connected email or existing booking records before asking the user. When asked to check in, carry out the authorised online check-in and seat selection end to end, rather than merely giving instructions. Establish dates, operating airline, flight numbers, connections, destination and return journey. Use the operating airline's local departure time for check-in deadlines.

Search available connected files for passports, visas and relevant IDs before asking the user to upload or repeat anything. Read the original document, including its image if scanned; do not fill identity fields from search captions, memory or inferred values. Use known file references first. If unavailable, search by document title and then identify the exact missing item. Do not claim access to every file or service.

Keep passport numbers, scans and full dates of birth out of this skill, source control and routine responses. Retrieve them only when needed from the authorised original. Follow the active permissions for transmitting documents to an airline; access is not blanket permission to send IDs elsewhere.

## Passport reminder before booking

Proactively give a short, journey-specific reminder before a booking is submitted and again when preparing check-in. Explain which passport to supply to the airline for destination admission, which to present to departure immigration, and whether both should be carried. For example, after checking current rules: 'For this UK trip, use your British passport for UK entry and airline document checks. Carry both passports and use the passport linked to your current visa at departure immigration.' Adapt to the actual itinerary.

Verify current official government guidance for every relevant destination and transit point, dual-national rules, visa or ETA linkage, passport validity and departure requirements. Use official UK and Australian guidance as the starting points for those countries. Do not apply the UK recommendation to every journey or silently replace the passport linked to an existing visa.

Distinguish booking name, nationality, passport number, issuing country, expiry, visa/ETA and airline advance passenger information. Match details to the selected original document. Changing nationality alone does not prove that check-in passport data has changed. If different passports are needed at departure and arrival, establish the handling from official or airline guidance and explain it briefly.

Treat the booking-time reminder as part of this conversational workflow. Do not claim background monitoring or a scheduled reminder exists. If a dated reminder is requested, create it with the available automation service and report whether it succeeded.

## Check-in and seats

Retrieve current seat assignments and the live seat map before recommending seat numbers. Consult an accurate aircraft-layout source such as AeroLOPA and the operating airline’s official map to assess cabin position, legroom, recline restrictions, lavatories and galleys. Match the exact configuration to the booking; an aircraft family alone is insufficient. Use external maps to assess seat quality, and the airline’s live map for availability and price. Apply this evidence in support conversations as well as direct seat selection. Verify operating aircraft and layout; letters alone do not prove aisle or window. Apply current trip instructions over saved defaults. Compare only seats available at the authorised price, verify the total is zero before saving a free change, and preserve an acceptable existing seat until the replacement is confirmed. Check exit-row eligibility requirements without inventing answers for the user.

After an authorised change, verify the saved result and report leg, seat number, aisle/window and charge. Distinguish requested, selected and confirmed seats. If support and Manage Booking disagree, state both observations with their source and time, then seek confirmation from the operating airline or check-in record; do not declare either settled without resolving the discrepancy.

For document blocks, record the exact message, inspect editable document fields and retry after verified corrections. Do not infer security targeting or a confirmed cause from dual nationality. If airline staff must intervene, contact support when authorised, request correction of the specific passenger-document record and ask whether online check-in can be released. Keep a concrete distinction between changes completed, unresolved errors and actions only airport staff can take.

If better free seats are unavailable, retain the best confirmed acceptable seats. Explain any verified remaining route, such as asking airport staff for a free reassignment; do not promise seats will open or repeatedly retry an unchanged block. Never imply a seat change, passport replacement, support request or check-in succeeded without evidence.

## Speak to support naturally

When authorised to speak on the user’s behalf, write short, natural first-person messages in their voice. Ask one focused question or make one concrete request at a time; provide booking details once and repeat constraints only when relevant. Avoid robotic summaries, capitalised demands and unnecessary technical questions. Answer direct questions about acting on behalf of the user honestly. Never invent personal experiences or verification answers.
