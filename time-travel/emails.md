# Time Travel — emails

Ten moments from sign-up to the drop. Sent with **Shopify Email** (Marketing → Campaigns; the welcome
email as an automation). English, short, calm: no exclamation marks, no emojis, dates as `01.02.2027 · 19:00 CET`.
Dates follow the Drop Docket: pre-order **Mon 01.02.2027 · 19:00 CET**, drop **Thu 24.06.2027 · 19:00 CEST**.
No emails during the Abitur pause (22.03.–09.05.2027).

House rules for every email:
- The pattern is the subject, not the people. No faces, no models.
- Never "authentic". Never call the tree of life "Slavic". Say "eight-point star". No politics.
- Only real numbers (35 pairs at €149, 100 pairs numbered 001–100). "[Y] of 35 left" only with the number from Shopify.
- No product photos before the sample gate (05.01.2027).
- One button per email. It goes to the page `https://novalife.store/pages/time-travel`
  (short form `novalife.store/timetravel`), or on key days to the product.
- Footer line: `Novalife · Berlin · @novalife.store`

## Segments (Customers → Segments → Create segment)

| Name | Query |
|---|---|
| TT · waitlist | `customer_tags CONTAINS 'time-travel-waitlist' OR number_of_orders > 0` |
| TT · inner circle | `customer_tags CONTAINS 'inner-circle' OR customer_tags CONTAINS 'found-key'` |
| TT · waitlist without inner circle | `(customer_tags CONTAINS 'time-travel-waitlist' OR number_of_orders > 0) AND customer_tags NOT CONTAINS 'inner-circle' AND customer_tags NOT CONTAINS 'found-key'` |
| TT · no pre-order yet | add `AND products_purchased(id: PRODUCT_ID) = false` to a segment above (PRODUCT_ID = the jeans) |

Why `number_of_orders > 0`: Shopify's sign-up form does not add tags to someone who is already a customer.
Past buyers who join the waitlist would be missing otherwise — and they are the warmest people you have.
Shopify Email only ever sends to people who agreed to marketing, so this reaches nobody who said no.

## Overview

| # | When (Berlin) | Subject | Segment | Button |
|---|---|---|---|---|
| E0 | right after sign-up (automation) | Your key is reserved. | new waitlist subscriber | Back to the field |
| E1 | Thu 19.11.2026 · 19:00 CET | Chapter II: the star woke up | waitlist | See chapter II |
| E2 | Thu 17.12.2026 · 19:00 CET | Chapter III: the harvest | waitlist | See the door |
| E3 | Thu 14.01.2027 · 19:00 CET | Chapter IV: light in the windows | waitlist | Back to the field |
| E4 | Sun 31.01.2027 · 19:00 CET | Tomorrow, 18:00 CET. | waitlist (two versions) | Back to the field |
| E5a | Mon 01.02.2027 · 17:00 CET | Your key. | inner circle | Use your key |
| E5b | Mon 01.02.2027 · 18:00 CET | Your key. | waitlist without inner circle | Use your key |
| E6 | Thu 04.03.2027 · 19:00 CET | Chapter V: the tree | waitlist | See chapter V |
| E7 | Thu 20.05.2027 · 19:00 CEST | €149 until Sunday. | waitlist + no pre-order yet | Pre-order |
| E8 | Thu 17.06.2027 · 19:00 CEST | One week. | waitlist | Back to the field |
| E9a | Thu 24.06.2027 · 17:00 CEST | The door is open. For you. | inner circle | Enter |
| E9b | Thu 24.06.2027 · 18:00 CEST | The door is open. For you. | waitlist without inner circle | Enter |
| E9c | Thu 24.06.2027 · 19:00 CEST | The door is open. | all subscribers | Enter |

```
[Sign-up on the page] --> E0 (now)
        |
        v
  E1 Ch. II (19.11) --> E2 Ch. III (17.12) --> E3 Ch. IV (14.01) --> E4 Reminder (31.01)
                                                                         |
                                     inner circle / found key? --yes--> E5a 17:00 --+
                                                                         |          |
                                                                         no         |
                                                                         v          |
                                                                     E5b 18:00 <----+
                                                                         |
                    E6 Ch. V (04.03) --> [Abitur pause, no emails] --> E7 €149 ends (20.05, only without pre-order)
                                                                         |
                                                                         v
                                                   E8 One week (17.06) --> E9a/E9b/E9c (24.06) --> [end]
```

---

## E0 · Welcome — "Your key is reserved."

**When:** right after sign-up. Shopify Email → Automations → *Welcome new subscriber*; in its Shopify Flow add the
condition *customer tags contain `time-travel-waitlist`*. With double opt-in it goes out after the confirmation click.
**Purpose:** confirm, give the date, make the golden key and the personal link known.

Subject options: `Your key is reserved.` · `The door is closed. You have a key.` · `Time Travel: you are on the list`
Preheader: `Pre-order 01.02.2027 — for you at 18:00 CET, an hour before everyone.`

> The door is closed. Your key is reserved.
>
> **01.02.2027 · 18:00 CET** — one hour before everyone else, we send you the key to the pre-order. 35 pairs at the pre-order price.
>
> Until then the house changes. A new chapter opens every few weeks, always on a Thursday at 19:00. The next one: 19.11.2026.
>
> Somewhere near the path there is a golden key. Whoever finds it gets in at 17:00.
> Your key image and your personal link wait at the door — on the phone or laptop you signed up with. Three friends through your link, and you get in at 17:00 too.
>
> **[Back to the field]**
>
> Novalife · Berlin · @novalife.store

---

## E1 · Chapter II — "The star woke up."

**When:** Thu 19.11.2026 · 19:00 CET · **Segment:** TT · waitlist
**Purpose:** first reason to come back; teach that the house changes.

Subject options: `Chapter II: the star woke up` · `Look above the door` · `Something changed at the izba`
Preheader: `Chapter II of Time Travel is open.`

> Above the door there is an eight-point star, cut into the carved frame.
> Tonight it started to glow.
>
> Every chapter adds one pattern to the house. Every pattern is part of Time Travel.
>
> **[See chapter II]**
>
> Pre-order: 01.02.2027 · 18:00 CET for you.

---

## E2 · Chapter III — "The harvest."

**When:** Thu 17.12.2026 · 19:00 CET · **Segment:** TT · waitlist
**Purpose:** second return visit; push the personal link before the holidays.

Subject options: `Chapter III: the harvest` · `Three ears of wheat on the door` · `The door changed`
Preheader: `Six weeks until the pre-order.`

> Three ears of wheat, tied together, painted on a red band across the door.
> The harvest is in.
>
> Six weeks until the pre-order. If three friends join through your link, you get in at 17:00 instead of 18:00.
> Your link waits for you at the door.
>
> **[See the door]**

---

## E3 · Chapter IV — "Light in the windows."

**When:** Thu 14.01.2027 · 19:00 CET · **Segment:** TT · waitlist
**Purpose:** the sample gate is behind you — first real look is allowed now. Build up to the pre-order.

Subject options: `Chapter IV: light in the windows` · `Someone is home` · `18 days`
Preheader: `The pre-order opens on 01.02.2027.`

> There is light in the windows now.
>
> In 18 days the pre-order opens: 01.02.2027, 18:00 CET for you.
>
> *(If the sample is approved: one close-up of the embroidery. The pattern, not a person.)*
>
> **[Back to the field]**

---

## E4 · Reminder — "Tomorrow, 18:00 CET."

**When:** Sun 31.01.2027 · 19:00 CET · two versions:
inner circle (`17:00` in the copy) and waitlist without inner circle (`18:00`).
**Purpose:** make sure nobody misses the hour.

Subject options: `Tomorrow, 18:00 CET.` · `Your key arrives tomorrow` · `24 hours`
Preheader: `The pre-order opens for you one hour before everyone else.`

> Tomorrow the pre-order opens. 35 pairs at €149.
>
> Your key arrives by email at **18:00 CET** — one hour before everyone else. No account needed, the link is the key.
>
> **[Back to the field]**

---

## E5 · The key — "Your key."

**When:** Mon 01.02.2027 · **E5a 17:00 CET** to TT · inner circle, **E5b 18:00 CET** to TT · waitlist without inner circle.
**Purpose:** the money moment. The button goes straight to the pre-order product.
**Shopify:** publish the product at 17:00 but keep it out of menus and collections until 19:00
(the page shows its *Pre-order* button from 19:00 by itself).

Subject options: `Your key.` · `The pre-order is open — for you` · `17:00. Your key.` (E5a) / `18:00. Your key.` (E5b)
Preheader: `One hour before everyone else. 35 pairs at €149.`

> The pre-order is open — for you, before everyone else.
>
> **35 pairs at €149.** After that, and from 24.05., €169.
> Delivery: by 30.06.2027 at the latest, planned for early June.
> At 19:00 CET it opens for everyone.
>
> **[Use your key]**
>
> (Please keep this link to yourself until 19:00.)

---

## E6 · Chapter V — "The tree."

**When:** Thu 04.03.2027 · 19:00 CET · **Segment:** TT · waitlist
**Purpose:** last email before the Abitur pause; keep the pre-order alive.

Subject options: `Chapter V: the tree` · `A tree appeared under the roof` · `Under the roof`
Preheader: `The pre-order is open. The door opens on 24.06.2027.`

> Under the roof, a carved tree with two birds facing it. The tree of life.
>
> The pre-order is open. On **24.06.2027** the door opens for everyone.
>
> *(If true: "[Y] of the 35 pairs at €149 are left." — only with the real number.)*
>
> **[See chapter V]**

---

## E7 · Last days at €149 — "€149 until Sunday."

**When:** Thu 20.05.2027 · 19:00 CEST · **Segment:** TT · waitlist + TT · no pre-order yet
**Purpose:** the price step on 24.05. is real urgency — use it once.
Skip this email if the 35 pairs at €149 are already gone.

Subject options: `€149 until Sunday.` · `The price changes on Monday` · `[Y] pairs at €149 left`
Preheader: `From 24.05. the pre-order costs €169.`

> The pre-order price ends on Sunday, 23.05.
> From Monday the jeans cost €169.
>
> [Y] of the 35 pairs at €149 are left. *(real number from Shopify)*
>
> **[Pre-order]**

---

## E8 · One week — "One week."

**When:** Thu 17.06.2027 · 19:00 CEST · **Segment:** TT · waitlist · same evening as chapter VI
**Purpose:** last build-up; the house is fully lit.

Subject options: `One week.` · `Every window is lit` · `24.06 · 19:00 CEST`
Preheader: `The door opens on Thursday. Your time: 18:00 CEST.`

> Every window is lit. Two lanterns hang by the door.
>
> In one week the door opens. **24.06.2027 · 18:00 CEST** for you, 19:00 for everyone.
>
> **[Back to the field]**

---

## E9 · Drop day — "The door is open."

**When:** Thu 24.06.2027 · **E9a 17:00 CEST** inner circle · **E9b 18:00 CEST** waitlist without inner circle ·
**E9c 19:00 CEST** all subscribers. The page opens its door by itself at 19:00 (`dropAt` in CONFIG).
**Purpose:** sell what the pre-order left of the 100 pairs, plus the zipper and the polo.

Subject options: `The door is open. For you.` (E9a/E9b) · `The door is open.` (E9c) · `001–100`
Preheader: `One hour before everyone else.` (E9c: `Time Travel is here.`)

> The door is open.
>
> The jeans NVL-TT-01, numbered up to 100 — what the pre-order left. €169.
> The zipper and the polo are inside too.
>
> **[Enter]**

Optional, only if pairs are really left the next evening: one last email to *TT · waitlist* with the real number from
the inventory ("12 pairs left"). Never estimate.

---

## Benchmarks (rough ranges to set targets — your own first sends become the baseline)

| Metric | Welcome (E0) | Chapters (E1–E3, E6, E8) | Key and price emails (E4, E5, E7, E9) |
|---|---|---|---|
| Open rate | 50–70 % | 35–55 % | 50–70 % |
| Click rate | 10–20 % | 5–12 % | 20–40 % |
| Unsubscribe | < 0.5 % | < 0.5 % | < 0.3 % |

Note: Apple Mail privacy makes open rates look higher than they are. Judge by clicks and orders.

## Exits and suppression

- Bought the pre-order → leave E7 (segment `products_purchased(id: PRODUCT_ID) = false`); they stay for the chapters and the drop.
- Unsubscribed or never confirmed double opt-in → Shopify does not send. Nothing to do.
- Nobody gets two emails on the same day, except the tier emails (each person only gets their own tier).

## A/B tests (Shopify Email: *A/B test subject line*, if available in your plan)

1. E1 subject: `Chapter II: the star woke up` vs `Look above the door` — winner by click rate after 4 hours.
2. E4 subject with time vs without: `Tomorrow, 18:00 CET.` vs `Your key arrives tomorrow`.
3. E0 button: `Back to the field` vs `Find the golden key` — winner by clicks; the second also shows in the page events (`tt_key_found`).

## What to track

- Sequence goal: pre-orders (35 at €149, then €169) and drop sales from waitlist people.
- Per email: open, click, unsubscribe (Shopify Email reports).
- On the page (custom pixel events): `tt_enter`, `tt_arrive`, `tt_waitlist_open`, `tt_signup`, `tt_key_found`, `tt_share`, `tt_copy_link`, `tt_cta`.
- Weekly: new sign-ups, sign-ups through personal links (`python3 time-travel/tools/referrals.py export.csv`).
