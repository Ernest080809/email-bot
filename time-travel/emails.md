# Time Travel — emails

Eight moments from sign-up to the drop. Sent with **Shopify Email** (Marketing → Campaigns; the welcome
email as an automation). English, short, calm: no exclamation marks, no emojis, dates as `14.01.2027 · 19:00 CET`.

House rules for every email:
- The pattern is the subject, not the people. No faces, no models.
- Never "authentic". Never call the tree of life "Slavic". No politics.
- Only real numbers (35 pairs, 100 pairs, 001–100). Never "only X left" unless the stock really says so.
- No product photos until the sample exists. The pre-order email may show it **only if the sample is done**.
- One button per email. It always goes to the page: `https://novalife.store/pages/time-travel`
  (short form `novalife.store/timetravel`), or on key days to the product.

## Segments (Customers → Segments → Create segment)

| Name | Query |
|---|---|
| TT · waitlist | `customer_tags CONTAINS 'time-travel-waitlist' OR number_of_orders > 0` |
| TT · inner circle | `customer_tags CONTAINS 'inner-circle' OR customer_tags CONTAINS 'found-key'` |
| TT · waitlist without inner circle | `(customer_tags CONTAINS 'time-travel-waitlist' OR number_of_orders > 0) AND customer_tags NOT CONTAINS 'inner-circle' AND customer_tags NOT CONTAINS 'found-key'` |
| TT · no pre-order yet | add `AND products_purchased(id: PRODUCT_ID) = false` to a segment above (PRODUCT_ID = the pre-order product) |

Why `number_of_orders > 0`: Shopify's sign-up form does not add tags to someone who is already a customer.
Past buyers who join the waitlist would be missing otherwise — and they are the warmest people you have.
Shopify Email only ever sends to people who agreed to marketing, so this does not reach anyone who said no.

## Overview

| # | When (Berlin) | Subject | Segment | Button |
|---|---|---|---|---|
| E0 | right after sign-up (automation) | Your key is reserved. | new waitlist subscriber | Back to the field |
| E1 | Thu 19.11.2026 · 19:00 CET | Chapter II: the star woke up | waitlist | See chapter II |
| E2 | Thu 17.12.2026 · 19:00 CET | Chapter III: the harvest | waitlist | See the door |
| E3 | Wed 13.01.2027 · 19:00 CET | Tomorrow, 18:00 CET. | waitlist (two versions) | Back to the field |
| E4a | Thu 14.01.2027 · 17:00 CET | Your key. | inner circle | Use your key |
| E4b | Thu 14.01.2027 · 18:00 CET | Your key. | waitlist without inner circle | Use your key |
| E5 | Thu 04.03.2027 · 19:00 CET | Chapter V: the tree | waitlist | See chapter V |
| E6 | Thu 15.04.2027 · 19:00 CEST | One week. | waitlist | Back to the field |
| E7a | Thu 22.04.2027 · 17:00 CEST | The door is open. For you. | inner circle | Enter |
| E7b | Thu 22.04.2027 · 18:00 CEST | The door is open. For you. | waitlist without inner circle | Enter |
| E7c | Thu 22.04.2027 · 19:00 CEST | The door is open. | all subscribers | Enter |

```
[Sign-up on the page] --> E0 (now)
        |
        v
  E1 Chapter II (19.11) --> E2 Chapter III (17.12) --> E3 Reminder (13.01)
                                                          |
                         inner circle / found key? --yes--> E4a 17:00 --+
                                                          |             |
                                                          no            |
                                                          v             |
                                                       E4b 18:00 <------+  (bought the pre-order → leave the pre-order emails)
                                                          |
                                                          v
                         E5 Chapter V (04.03) --> E6 One week (15.04) --> E7a/E7b/E7c (22.04) --> [end]
```

---

## E0 · Welcome — "Your key is reserved."

**When:** right after sign-up. Shopify Email → Automations → *Welcome new subscriber*; in its Shopify Flow add the
condition *customer tags contain `time-travel-waitlist`*. With double opt-in it goes out after the confirmation click.
**Purpose:** confirm, give the two dates, make the golden key and the personal link known.

Subject options: `Your key is reserved.` · `The door is closed. You have a key.` · `Time Travel: you are on the list`
Preheader: `Pre-order 14.01.2027 — for you at 18:00 CET, an hour before everyone.`

> The door is closed. Your key is reserved.
>
> **14.01.2027 · 18:00 CET** — one hour before everyone else, we send you the key to the pre-order. 35 pairs.
>
> Until then the house changes. A new chapter opens every few weeks, always on a Thursday at 19:00. The next one: 19.11.2026.
>
> Somewhere in the field there is a golden key. Whoever finds it gets in at 17:00.
> Your key image and your personal link wait at the door — on the phone or laptop you signed up with. Three friends through your link, and you get in at 17:00 too.
>
> **[Back to the field]**
>
> Novalife · Berlin

---

## E1 · Chapter II — "The star woke up."

**When:** Thu 19.11.2026 · 19:00 CET · **Segment:** TT · waitlist
**Purpose:** first reason to come back; teach that the house changes.

Subject options: `Chapter II: the star woke up` · `Look above the door` · `Something changed at the izba`
Preheader: `Chapter II of Time Travel is open.`

> Above the door there is a star with eight points, cut into the carved frame.
> Tonight it started to glow.
>
> Every chapter adds one pattern to the house. Every pattern is part of Time Travel.
>
> **[See chapter II]**
>
> Pre-order: 14.01.2027 · 18:00 CET for you.

---

## E2 · Chapter III — "The harvest."

**When:** Thu 17.12.2026 · 19:00 CET · **Segment:** TT · waitlist
**Purpose:** second return visit; push the personal link before the holidays.

Subject options: `Chapter III: the harvest` · `Three ears of wheat on the door` · `The door changed`
Preheader: `Four weeks until the pre-order.`

> Three ears of wheat, tied together, painted on a red band across the door.
> The harvest is in.
>
> Four weeks until the pre-order. If three friends join through your link, you get in at 17:00 instead of 18:00.
> Your link waits for you at the door.
>
> **[See the door]**

---

## E3 · Reminder — "Tomorrow, 18:00 CET."

**When:** Wed 13.01.2027 · 19:00 CET · two versions:
inner circle (`17:00` in the copy) and waitlist without inner circle (`18:00`).
**Purpose:** make sure nobody misses the hour. If the sample is done, this is the first look.

Subject options: `Tomorrow, 18:00 CET.` · `Your key arrives tomorrow` · `24 hours`
Preheader: `The pre-order opens for you one hour before everyone else.`

> Tomorrow the pre-order opens. 35 pairs.
>
> Your key arrives by email at **18:00 CET** — one hour before everyone else. No account needed, the link is the key.
>
> *(Only if the sample exists: one photo of the pattern, close up. Not on a person.)*
>
> **[Back to the field]**

---

## E4 · The key — "Your key."

**When:** Thu 14.01.2027 · **E4a 17:00 CET** to TT · inner circle, **E4b 18:00 CET** to TT · waitlist without inner circle.
**Purpose:** the money moment. The button goes straight to the pre-order product.
**Shopify:** publish the product at 17:00 but keep it out of menus and collections until 19:00
(the page shows its *Pre-order* button from 19:00 by itself). Fill in price and delivery before sending.

Subject options: `Your key.` · `The pre-order is open — for you` · `17:00. Your key.` (E4a) / `18:00. Your key.` (E4b)
Preheader: `One hour before everyone else. 35 pairs.`

> The pre-order is open — for you, before everyone else.
>
> 35 pairs. Pre-order price: **€[149]**. Delivery: **[month year]**.
> At 19:00 CET it opens for everyone.
>
> **[Use your key]**
>
> (Please keep this link to yourself until 19:00.)

---

## E5 · Chapter V — "The tree."

**When:** Thu 04.03.2027 · 19:00 CET · **Segment:** TT · waitlist (+ `TT · no pre-order yet` variant if you want a different last line)
**Purpose:** bring the drop back into focus after the pre-order.

Subject options: `Chapter V: the tree` · `A tree appeared under the roof` · `Seven weeks`
Preheader: `The drop: 22.04.2027 · 19:00 CEST.`

> Under the roof, a carved tree with two birds facing it. The tree of life.
>
> On **22.04.2027** the door opens: 100 pairs, numbered 001 to 100.
> The waitlist gets in at 18:00 CEST, the inner circle at 17:00.
>
> *(If true: "The 35 pre-order pairs are gone." — only with the real number.)*
>
> **[See chapter V]**

---

## E6 · One week — "One week."

**When:** Thu 15.04.2027 · 19:00 CEST · **Segment:** TT · waitlist
**Purpose:** last build-up; the house is fully lit.

Subject options: `One week.` · `Every window is lit` · `22.04 · 19:00 CEST`
Preheader: `The door opens on Thursday. Your time: 18:00 CEST.`

> Every window is lit. Two lanterns hang by the door.
>
> In one week the door opens. 100 pairs, numbered 001 to 100.
> **22.04.2027 · 18:00 CEST** for you. 19:00 for everyone.
>
> **[Back to the field]**

---

## E7 · Drop day — "The door is open."

**When:** Thu 22.04.2027 · **E7a 17:00 CEST** inner circle · **E7b 18:00 CEST** waitlist without inner circle ·
**E7c 19:00 CEST** all subscribers. The page opens its door by itself at 19:00 (`dropAt` in CONFIG).
**Purpose:** sell the 100 pairs.

Subject options: `The door is open. For you.` (E7a/E7b) · `The door is open.` (E7c) · `001–100`
Preheader: `100 pairs, numbered. One hour before everyone else.` (E7c: `100 pairs, numbered.`)

> The door is open.
>
> 100 pairs of NVL-TT-01, numbered 001 to 100. **€[169]**.
>
> **[Enter]**

Optional, only if pairs are really left the next evening: one last email to *TT · waitlist* with the real number from
the inventory ("12 pairs left"). Never estimate.

---

## Benchmarks (rough ranges to set targets — your own first sends become the baseline)

| Metric | Welcome (E0) | Chapters (E1, E2, E5, E6) | Key emails (E4, E7) |
|---|---|---|---|
| Open rate | 50–70 % | 35–55 % | 50–70 % |
| Click rate | 10–20 % | 5–12 % | 20–40 % |
| Unsubscribe | < 0.5 % | < 0.5 % | < 0.3 % |

Note: Apple Mail privacy makes open rates look higher than they are. Judge by clicks and orders.

## Exits and suppression

- Bought the pre-order → leave E3/E4 (segment `products_purchased(id: PRODUCT_ID) = false`); they stay for the chapters and the drop.
- Unsubscribed or never confirmed double opt-in → Shopify does not send. Nothing to do.
- Nobody gets two emails on the same day, except the drop day tiers (each person only gets their own tier email).

## A/B tests (Shopify Email: *A/B test subject line*, if available in your plan)

1. E1 subject: `Chapter II: the star woke up` vs `Look above the door` — winner by click rate after 4 hours.
2. E3 subject with time vs without: `Tomorrow, 18:00 CET.` vs `Your key arrives tomorrow`.
3. E0 button: `Back to the field` vs `Find the golden key` — winner by clicks; the second also shows in the page events (`tt_key_found`).

## What to track

- Sequence goal: pre-orders (35) and drop sales (100) from waitlist people.
- Per email: open, click, unsubscribe (Shopify Email reports).
- On the page (custom pixel events): `tt_enter`, `tt_arrive`, `tt_waitlist_open`, `tt_signup`, `tt_key_found`, `tt_share`, `tt_copy_link`, `tt_cta`.
- Weekly: new sign-ups, sign-ups through personal links (`python3 time-travel/tools/referrals.py export.csv`).
