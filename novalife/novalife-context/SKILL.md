---
name: "novalife-context"
description: "Load this skill the moment the word 'Novalife' appears anywhere in the user's message, in any context — branding, content planning, marketing copy, pricing, product descriptions, social media, supplier outreach, or casual mentions. Novalife is the user's denim/streetwear brand. This skill restores full brand context (founding story, materials, pricing, motto, positioning, changelog of recent updates) so the user never has to re-explain the brand from scratch in a new chat, and it actively tracks new or changed facts the user shares about Novalife so the brand knowledge keeps growing instead of staying frozen. Trigger even on indirect references like 'my brand', 'the denim thing', 'Time Travel', 'the drop', 'the docket' or 'my Berlin brand' if Novalife was mentioned earlier in the same conversation. Do not wait for the user to ask 'what is Novalife' — load proactively as soon as the name is used."
---

# Novalife Brand Context

## Why this exists

The user (Ernest Veskimäe) runs Novalife and works with Claude across many separate chats and Cowork sessions. Without this skill, every new chat starts blank and the user has to re-explain the brand from scratch. This skill has two jobs: (1) load the brand facts below the moment "Novalife" comes up, and (2) keep those facts current by tracking what the user says about the brand and helping fold it back in.

## Brand facts (treat as ground truth, most recent update wins)

**Overview:** Novalife is a streetwear brand from Berlin, founded 2023. It started with bleach customization: existing denim garments are individually bleached, turning them into one-off pieces. Since September 2026 Novalife also produces its own line. The first own drop is **Time Travel**, and it is the current focus.

- Founded: 2023
- Origin / base: Berlin
- Founder's situation: Abitur year 2026/27. Written exams roughly 07.04.–05.05.2027. Works on the drop about 1–2 hours a day, irregularly.

### Current focus: the Time Travel drop (Projekt Slavic)

- **Drop:** Thursday, **24 June 2027, 19:00** (waitlist early access 18:00). Moved on 13.10.2026 from 22 April because of the Abitur. All three products launch together. Delivery promise for pre-orders: "by 30.06.2027 at the latest, planned early June".
- **Theme "Projekt Slavic":** the shared core of Slavic textile tradition (rhombus, eight-pointed star / Alatyr, zigzag, tree of life, harvest), not one national tradition. No politics in the brand. Language rule: *the pattern is the subject, not the people.* Never claim "authentic". Never call the tree of life "Slavic". Outwardly say "eight-point star", not "Alatyr".
- **Hero product:** 100 embroidered jeans NVL-TT-01 from one factory (Turkey or Portugal, chosen around 26.10.2026), numbered 001–100. Straight leg, 12 oz rigid 100 % cotton, vintage wash, honest sizing W30–W38 (the label is the real waist in inches). **€169**, pre-order **€149** for 35 pairs; after no. 035 a second tier (nos. 036–060) at €169.
- **Design v1.7 without B (since 11.10.2026):** the sickle (Serp) and its stubble field are cut everywhere. Five visible elements remain: A cross-stitch band along the right front pocket, E fully embroidered coin pocket, B2 three wheat ears on a red band with 9 hand-set gold threads on the left back pocket, C eight-pointed star on the right back pocket, D tree-of-life patch. Four embroidery zones at the factory (A, E, B2, C), ~28,000 stitches (gate ≤ 28,000).
- **Patch D:** natural linen, **76 × 67 mm**, 4 copper rivets, worn as the **rear belt loop** (sewn and riveted only left and right, open top and bottom, the belt runs behind it). Artwork = the user's own tree image, keeps the letters "NL", at most 4 thread colours. Bought in, not factory-embroidered. Origin of the tree image still to be confirmed.
- **Zipper (€139):** zip hoodie from a blank, natural white recommended (sketch says white). Front = medallion from grandma's carpet (embroidered is the recommendation, chenille only with a tiny MOQ), bands, eight-pointed star as the brand signature.
- **Polo (€79):** piqué polo from a blank, white/natural white. Chest logo decided 16.10.2026: a **cross-stitch tree with branches instead of arms**, single colour red, no letters (like a Ralph Lauren logo, but from nature ornament).
- Zipper and polo are embroidered by a Berlin embroidery shop on demand (no MOQ). Open: an eight-point-star button (price and MOQ asked at the factories).
- **Order of work (the user's rule, sharpened 17.10.2026):** first designs, factory and samples, completely. **Sample gate Tue 05.01.2027:** the jeans PP sample, the zipper and the polo have arrived as single pieces and the user has approved all three in writing. Only after that: website, Shopify, payments, legal texts and bureaucracy (Gewerbe registration 06.01., tax questionnaire 07.01., LUCID). Marketing runs the whole time.
- **Key dates:** proto 03.12.2026 · zipper and polo approved 19.12. · PP 04.01.2027 · sample gate 05.01. · shop block 06.–31.01. · **pre-order opens Mon 01.02.2027, 19:00** (list 18:00) · measuring evenings 03.02. and 10.02. · threshold Mon 15.02. (≥ 10 pre-orders paid out, forecast ≥ 32) · deposit 18.02. · Abi pause 22.03.–09.05. (no tasks, autopilot posts) · goods ready 14.05. · countdown from 31.05. · drop 24.06.
- **Bureaucracy status:** no Gewerbe yet (as of 13.10.2026). IHK founder consultation requested from 01.11.; registration only after the sample gate. If the user is under 18, registration needs parents and the family court, which takes weeks; age not yet confirmed.
- **Money:** own budget €4,500; capital need ~€9,125; the gap (~€4,625) is financed by pre-orders. Jeans unit cost ~€59.90 (estimate until the real stitch count). Only money that has actually been paid out counts for any payment.
- **Marketing:** daily short videos (TikTok, Reels, Shorts; English hook with a German line), build-in-public series "Day X", waitlist with source tags. **REWIND:** 20 stunt videos with reverse, freeze, bullet-time and clone tricks; #01 is the G-Klasse reverse stunt with the father's car, #11 continues it on pre-order day. Each video carries a code word for attribution. Safety first: the car only ever drives backwards.
- **Where the details live:** repository `novalife/time-travel/rev6` (weeks JSON, `strategie.md`, research files), the daily plan "Time Travel Drop Docket" (artifact) and the doc "REWIND · Video-Bibel" (Claude Docs). For anything about the drop, read these first; they change faster than this skill.

### Working rules the user set

- Never send, post or delete anything without an explicit "yes". The two Gmail drafts to Hidrock and Lapiztola must not go out. No address scraping.
- Never tick docket checkboxes without asking.
- Never store anyone's ethnic origin next to a name or email.
- In the docket, tasks are only appended or turned into a note in place, unless the user explicitly asks for a re-plan.
- Talk to the user in German, short and concrete, as an honest mentor who analyses whether an idea is worth it.

### Original line: bleach customization

**Product:**
- Base material: denim pieces from established brands — primarily Levi's, Dolce & Gabbana, Diesel, and Armani.
- Technique: bleach customization. Each piece gets a unique, non-reproducible pattern.
- Result: every piece is one of a kind — no two are exactly alike.
- Price range: approx. €50–70 per piece.

**Brand philosophy:**
Motto: "We sell stories. Not just denim." Every piece carries its own story — from the original garment to the individual bleach treatment. Novalife positions itself deliberately against anonymous mass production: it's not selling a product, it's selling a piece with a history.

**Positioning:**
- Segment: custom/upcycled streetwear — a niche between vintage resale and designer denim. With Time Travel, also own-production embroidered denim built on textile ornament.
- Distribution: social-media driven (TikTok/Instagram), Shopify shop with waitlist, aiming for an international audience (content produced in English).
- Differentiation: recognizable brand bases combined with hands-on customization (bleach line); researched textile ornament and a hand-set detail on every piece (Time Travel).

**Legal note (trademark, bleach line):** Because real, purchased branded goods are being altered, the first-sale doctrine generally applies — the customization itself is not legally problematic. Always frame it as "customization" in marketing, never as a collaboration or official partnership with Levi's, D&G, Diesel, or Armani.

**Known constraints / open strategic questions:**
- Time is the main bottleneck (Abitur, 1–2 hours a day).
- The bleach line is bottlenecked by manual labor. Open scaling decision: build a team/process so bleaching happens without the founder directly, or stay deliberately small and exclusive. Parked behind the drop.

## Changelog

- 2026-10-17: Drop moved to 24.06.2027 (Abitur), pre-order now 01.02.2027. Sickle cut, design v1.7 without B, Patch D as 76 × 67 mm belt loop with the user's tree and "NL". Zipper and polo designs, polo logo (red cross-stitch tree). Unit cost ~€59.90. New order of work with the sample gate on 05.01.2027, no Gewerbe yet. REWIND video series. Working rules added.
- 2026-10-07: Added the Time Travel drop (own production, Projekt Slavic, products, prices, dates, design v1.7, money logic, where the source documents live). Bleach line kept as the original product line. Update mechanism changed to the skill proposal card.
- 2026-06-26: Initial version created.

## What to do with this

1. Treat the facts above as ground truth. Don't ask the user to re-confirm basics already covered here (e.g. don't ask "what year was Novalife founded").
2. For anything about the Time Travel drop, read the project documents named above first.
3. Use the context to inform whatever the user is actually asking for (content plans, outreach emails, pricing questions, brand copy, etc.) — don't just recite this back unless the user explicitly asks "what is Novalife" or similar.
4. **Actively listen for updates.** Whenever the user mentions something about Novalife that is new, more specific, or contradicts a fact above (a new price, a new product, a new date, a new strategic decision), treat that as a candidate update — don't silently ignore it and don't just go along with it for one conversation only.
5. When you notice at least one real update during a conversation, say so explicitly before the conversation wraps up (or whenever it's a natural moment) and offer to update this skill, e.g.: "Ich hab mitgeschrieben: [neue Fakten]. Soll ich den Novalife-Skill damit aktualisieren?"
6. **Be honest about the mechanism.** A skill is a static file; nothing updates itself in the background. To update it, edit the "Brand facts" and "Changelog" sections (add a dated changelog line) and propose the complete new version with the skill proposal card. The user saves it. Don't imply the file rewrites itself with zero action on their end.
