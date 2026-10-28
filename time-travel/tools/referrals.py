"""Counts Time Travel referrals and golden keys in a Shopify customer export.

Shopify admin → Customers → Export → All customers → "CSV for Excel, Numbers, or other spreadsheet programs".

    python3 time-travel/tools/referrals.py customers_export.csv
    python3 time-travel/tools/referrals.py customers_export.csv --min 3 --csv inner-circle.csv

Every sign-up from the page carries tags:
    key-XXXXXX   the person's own key number (it is also their referral code)
    ref-YYYYYY   the key number of the person whose link they came through
    found-key    they found the golden key in the field
Referrers with at least --min friends (and everyone with found-key) belong in the
inner circle: tag them `inner-circle` in Shopify, then the inner-circle email goes to
the segment  customer_tags CONTAINS 'inner-circle' OR customer_tags CONTAINS 'found-key'.
"""
import argparse
import collections
import csv
import sys


def tags_of(row: dict) -> list[str]:
    return [t.strip() for t in (row.get("Tags") or "").split(",") if t.strip()]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("export", help="customers_export.csv from Shopify")
    ap.add_argument("--min", type=int, default=3, help="friends needed for the inner circle (default 3)")
    ap.add_argument("--csv", help="also write the inner circle (email, key, friends, golden key) to this file")
    args = ap.parse_args()

    with open(args.export, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if rows and "Tags" not in rows[0]:
        sys.exit("No 'Tags' column — export the customers as CSV from Shopify admin.")

    owner: dict[str, str] = {}                                   # key code → email
    friends: dict[str, set[str]] = collections.defaultdict(set)  # key code → emails that came through it
    found: set[str] = set()
    waitlist = 0
    for row in rows:
        email = (row.get("Email") or "").strip().lower()
        if not email:
            continue
        tags = tags_of(row)
        lower = {t.lower() for t in tags}
        waitlist += "time-travel-waitlist" in lower
        if "found-key" in lower:
            found.add(email)
        for tag in tags:
            kind, _, code = tag.partition("-")
            if kind.lower() == "key" and code:
                owner[code.upper()] = email
            elif kind.lower() == "ref" and code:
                friends[code.upper()].add(email)

    # people cannot refer themselves
    for code, emails in friends.items():
        emails.discard(owner.get(code, ""))

    by_email = {email: code for code, email in owner.items()}
    qualified = sorted(((len(friends[c]), owner[c], c) for c in friends if c in owner and len(friends[c]) >= args.min), reverse=True)
    orphans = sorted(((len(e), c) for c, e in friends.items() if c not in owner and e), reverse=True)
    inner = {email for _, email, _ in qualified} | found

    print(f"Waitlist (time-travel-waitlist): {waitlist}")
    print(f"Sign-ups through a personal link: {sum(len(e) for e in friends.values())}")
    print(f"\nReferrers with {args.min}+ friends → inner circle ({len(qualified)}):")
    for n, email, code in qualified:
        print(f"  {email:<40} key {code[:3]}-{code[3:]}  {n} friends")
    print(f"\nFound the golden key → inner circle ({len(found)}):")
    for email in sorted(found):
        print(f"  {email}")
    if orphans:
        print("\nKey numbers nobody owns in this export (their owner signed up as an existing customer, so")
        print("Shopify did not save the key tag — ask them for their key number to credit them):")
        for n, code in orphans:
            print(f"  {code[:3]}-{code[3:]}  {n} friends")
    print(f"\nInner circle total: {len(inner)}")
    if inner:
        print("\nPaste into the search of Shopify admin → Customers, select all, Add tags → inner-circle:")
        print("  " + " OR ".join(f"email:{e}" for e in sorted(inner)))

    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["Email", "Key", "Friends", "Golden key"])
            for email in sorted(inner):
                code = by_email.get(email, "")
                w.writerow([email, f"{code[:3]}-{code[3:]}" if code else "", len(friends.get(code, ())) if code else 0, "yes" if email in found else ""])
        print(f"\nwrote {args.csv}")


if __name__ == "__main__":
    main()
