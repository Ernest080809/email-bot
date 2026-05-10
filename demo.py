#!/usr/bin/env python3
"""
Vinted Designer Sniper — Interactive Terminal Demo
Run with: python demo.py
No API keys or Telegram token required.
"""

import time
import random
import sys
import os

# ── ANSI colours ──────────────────────────────────────────────────────────────
R  = "\033[0m"       # reset
B  = "\033[1m"       # bold
DIM = "\033[2m"      # dim
RED   = "\033[91m"
GRN   = "\033[92m"
YLW   = "\033[93m"
BLU   = "\033[94m"
MAG   = "\033[95m"
CYN   = "\033[96m"
WHT   = "\033[97m"
BG_BLK = "\033[40m"

def clr():
    os.system("cls" if os.name == "nt" else "clear")

def slow(text: str, delay: float = 0.03) -> None:
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def pause(s: float = 1.0) -> None:
    time.sleep(s)

def hr(char="━", width=52, color=DIM):
    print(f"{color}{char * width}{R}")

def header():
    print(f"\n{BG_BLK}{B}{WHT}  🔍 VINTED DESIGNER SNIPER — DEMO  {R}\n")

# ── Mock data ─────────────────────────────────────────────────────────────────

MOCK_ITEMS = [
    {
        "id": 10001,
        "title": "Gucci Ace High Top Sneakers White Leather",
        "brand":  "Gucci",
        "price":  "€ 285",
        "retail": "€ 750",
        "size":   "43 EU",
        "condition": "Very good condition",
        "seller": "luigi_vintage",
        "rating": "99%",
        "location": "Milano, Italy",
        "url":    "https://www.vinted.it/items/10001",
        "photo":  "👟",
    },
    {
        "id": 10002,
        "title": "Christian Louboutin So Kate Pumps 120mm Black",
        "brand":  "Christian Louboutin",
        "price":  "€ 420",
        "retail": "€ 745",
        "size":   "38 EU",
        "condition": "New without tags",
        "seller": "parisienne_mode",
        "rating": "100%",
        "location": "Paris, France",
        "url":    "https://www.vinted.fr/items/10002",
        "photo":  "👠",
    },
    {
        "id": 10003,
        "title": "Moncler Maya Short Down Jacket Navy Blue Size M",
        "brand":  "Moncler",
        "price":  "€ 650",
        "retail": "€ 1 350",
        "size":   "M",
        "condition": "Very good condition",
        "seller": "stef_archive",
        "rating": "97%",
        "location": "Zürich, Switzerland",
        "url":    "https://www.vinted.de/items/10003",
        "photo":  "🧥",
    },
    {
        "id": 10004,
        "title": "Balenciaga Triple S Sneakers Grey Pink US10",
        "brand":  "Balenciaga",
        "price":  "€ 310",
        "retail": "€ 895",
        "size":   "44 EU / US10",
        "condition": "Good condition",
        "seller": "hype_archive_de",
        "rating": "96%",
        "location": "Berlin, Germany",
        "url":    "https://www.vinted.de/items/10004",
        "photo":  "👟",
    },
    {
        "id": 10005,
        "title": "Louis Vuitton Neverfull MM Damier Ebene Tote",
        "brand":  "Louis Vuitton",
        "price":  "€ 890",
        "retail": "€ 1 680",
        "size":   "One Size",
        "condition": "New with tags",
        "seller": "lux_resell_paris",
        "rating": "100%",
        "location": "Lyon, France",
        "url":    "https://www.vinted.fr/items/10005",
        "photo":  "👜",
    },
    {
        "id": 10006,
        "title": "Stone Island Shadow Project Jacket AW21 Size L",
        "brand":  "Stone Island",
        "price":  "€ 480",
        "retail": "€ 1 200",
        "size":   "L",
        "condition": "Very good condition",
        "seller": "archiveldn",
        "rating": "98%",
        "location": "London, UK",
        "url":    "https://www.vinted.co.uk/items/10006",
        "photo":  "🧥",
    },
]

WATCHLISTS = [
    {"name": "Gucci Shoes",       "brands": ["Gucci"],            "price": "€100–€600",  "country": "🇮🇹 vinted.it"},
    {"name": "Louboutin Heels",   "brands": ["Christian Louboutin"], "price": "€200–€700", "country": "🇫🇷 vinted.fr"},
    {"name": "Moncler Jackets",   "brands": ["Moncler"],          "price": "€400–€1500", "country": "🇩🇪 vinted.de"},
    {"name": "Hype Sneakers",     "brands": ["Balenciaga","Off-White","Supreme"], "price": "€150–€900", "country": "🇩🇪 vinted.de"},
    {"name": "LV Bags",           "brands": ["Louis Vuitton"],    "price": "€500–€3000", "country": "🇫🇷 vinted.fr"},
]

# ── Screens ───────────────────────────────────────────────────────────────────

def screen_welcome():
    clr()
    header()
    slow(f"{B}Welcome to the Vinted Designer Sniper demo!{R}", 0.02)
    print()
    print(f"{DIM}This demo simulates what happens when you run the bot.")
    print(f"No real data is fetched — everything shown is example data.{R}")
    print()
    print(f"  {CYN}→{R} The bot monitors Vinted every 30 seconds")
    print(f"  {CYN}→{R} You get a Telegram message the moment a new item appears")
    print(f"  {CYN}→{R} Tap one button to buy instantly")
    print()
    input(f"{DIM}Press Enter to continue…{R} ")

def screen_watchlists():
    clr()
    header()
    print(f"{B}📋 Your Active Watchlists{R}\n")
    hr()
    for i, wl in enumerate(WATCHLISTS, 1):
        brands = ", ".join(wl["brands"])
        print(f"  {GRN}●{R} {B}{wl['name']}{R}")
        print(f"    Brands : {brands}")
        print(f"    Price  : {wl['price']}")
        print(f"    Market : {wl['country']}")
        if i < len(WATCHLISTS):
            print()
    hr()
    print(f"\n{DIM}Polling every 30 seconds per watchlist.{R}")
    print()
    input(f"{DIM}Press Enter to start the sniper…{R} ")

def screen_sniper_start():
    clr()
    header()
    print(f"{GRN}{B}▶ Sniper started{R}")
    print()
    items_display = [
        ("Gucci Shoes",     "🇮🇹 vinted.it"),
        ("Louboutin Heels", "🇫🇷 vinted.fr"),
        ("Moncler Jackets", "🇩🇪 vinted.de"),
        ("Hype Sneakers",   "🇩🇪 vinted.de"),
        ("LV Bags",         "🇫🇷 vinted.fr"),
    ]
    for name, country in items_display:
        slow(f"  {DIM}[SEED]{R} {name} ({country}) — loading existing items…", 0.01)
        time.sleep(0.3)
    print()
    slow(f"{GRN}✓ All watchlists seeded. Watching for NEW items only.{R}", 0.02)
    print()
    input(f"{DIM}Press Enter to simulate finding a new item…{R} ")

def screen_notification(item: dict, watchlist_name: str):
    clr()
    header()

    # Simulate "checking" animation
    print(f"{DIM}Polling Vinted…{R}")
    for wl_name in [wl["name"] for wl in WATCHLISTS]:
        sys.stdout.write(f"  {DIM}checking {wl_name}…{R}  ")
        sys.stdout.flush()
        time.sleep(0.25)
        if wl_name == watchlist_name:
            print(f"\r  {YLW}● {wl_name} — {B}NEW ITEM FOUND!{R}          ")
            time.sleep(0.3)
        else:
            print(f"\r  {DIM}✓ {wl_name} — nothing new{R}          ")

    print()
    pause(0.4)

    # The notification card
    print(f"{YLW}{B}{'─'*52}{R}")
    print(f"{RED}{B}  🔥 NEW DESIGNER DROP  —  {watchlist_name}{R}")
    print(f"{YLW}{B}{'─'*52}{R}")
    print()
    print(f"  {item['photo']}  {B}{item['title']}{R}")
    print()
    print(f"  {'💰'} Price      {GRN}{B}{item['price']}{R}  {DIM}(Retail {item['retail']}){R}")
    print(f"  {'🏷️ '} Brand      {B}{item['brand']}{R}")
    print(f"  {'📏'} Size       {item['size']}")
    print(f"  {'✨'} Condition  {item['condition']}")
    print(f"  {'👤'} Seller     @{item['seller']}  ⭐ {item['rating']} positive")
    print(f"  {'📍'} Location   {item['location']}")
    print()
    print(f"  {DIM}⚡ Act fast — designer pieces sell in minutes!{R}")
    print()
    hr("─")
    print(f"  {CYN}{B}[ ⚡ BUY NOW ]{R}   {DIM}→ {item['url']}{R}")
    print(f"  {DIM}[ 👁  View Item ]   → {item['url']}{R}")
    hr("─")
    print()

def screen_outro():
    clr()
    header()
    print(f"{B}That's what every notification looks like on your phone.{R}\n")
    print(f"When you tap {CYN}{B}⚡ BUY NOW{R} in Telegram it opens Vinted")
    print(f"directly on the listing — one tap to buy if you're logged in.\n")
    hr()
    print(f"\n{B}To set up the real bot:{R}\n")
    print(f"  1. Get a Telegram bot token from @BotFather")
    print(f"  2. Add it to your .env file")
    print(f"  3. Run:  {CYN}python run_sniper.py{R}")
    print(f"  4. Send {CYN}/add{R} in Telegram to create your first watchlist\n")
    print(f"  Or deploy to Railway (free) so it runs 24/7 from your phone.\n")
    hr()
    print(f"\n{DIM}Demo complete. Press Enter to exit.{R}")
    input()

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    try:
        screen_welcome()
        screen_watchlists()
        screen_sniper_start()

        # Show 3 notifications with a brief pause between each
        alerts = [
            (MOCK_ITEMS[0], "Gucci Shoes"),
            (MOCK_ITEMS[1], "Louboutin Heels"),
            (MOCK_ITEMS[2], "Moncler Jackets"),
        ]
        for item, wl_name in alerts:
            screen_notification(item, wl_name)
            if item != alerts[-1][0]:
                input(f"{DIM}Press Enter to simulate the next alert…{R} ")

        screen_outro()

    except KeyboardInterrupt:
        print(f"\n\n{DIM}Demo stopped.{R}\n")

if __name__ == "__main__":
    main()
