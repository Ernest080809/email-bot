# Curated luxury / designer brand database for Vinted
# Brand IDs are consistent across all Vinted country domains.
# Use `search_brand()` in vinted_api.py to discover additional brand IDs.

LUXURY_BRANDS: dict[str, int] = {
    # ── Footwear / Sneakers ────────────────────────────────────────────────
    "Christian Louboutin":   2476,
    "Jimmy Choo":            560,
    "Manolo Blahnik":        2422,
    "Giuseppe Zanotti":      2543,
    # ── French houses ─────────────────────────────────────────────────────
    "Gucci":                 362,
    "Louis Vuitton":         104,
    "Dior":                  2009,
    "Chanel":                82,
    "Hermès":                246,
    "Givenchy":              1079,
    "Balmain":               432,
    "Valentino":             1064,
    "Saint Laurent":         2178,
    "Celine":                2099,
    "Loewe":                 3234,
    "Jacquemus":             3889,
    "Ami Paris":             3820,
    # ── Italian houses ────────────────────────────────────────────────────
    "Prada":                 213,
    "Moncler":               1289,
    "Versace":               1246,
    "Fendi":                 2058,
    "Bottega Veneta":        2045,
    "Dolce & Gabbana":       197,
    "Moschino":              572,
    "Missoni":               571,
    "Brunello Cucinelli":    3063,
    "Zegna":                 4012,
    # ── British houses ────────────────────────────────────────────────────
    "Burberry":              226,
    "Alexander McQueen":     2127,
    "Vivienne Westwood":     880,
    "Paul Smith":            616,
    "Stella McCartney":      878,
    # ── American / global ─────────────────────────────────────────────────
    "Tom Ford":              4282,
    "Ralph Lauren":          88,
    "Polo Ralph Lauren":     88,
    "Coach":                 167,
    "Marc Jacobs":           486,
    "Michael Kors":          3055,
    "Tory Burch":            2614,
    # ── Streetwear / hype ─────────────────────────────────────────────────
    "Balenciaga":            2048,
    "Off-White":             4706,
    "Stone Island":          5699,
    "Supreme":               2946,
    "Palm Angels":           5291,
    "Vetements":             4321,
    "Fear of God":           5012,
    "Amiri":                 5934,
    "Rhude":                 6103,
    # ── Avant-garde ───────────────────────────────────────────────────────
    "Rick Owens":            3261,
    "Maison Margiela":       3066,
    "Comme des Garçons":     2966,
    "Yohji Yamamoto":        1098,
    "Issey Miyake":          487,
    "Acne Studios":          3002,
    "Jil Sander":            476,
    "Lemaire":               4559,
    # ── Outerwear specialists ──────────────────────────────────────────────
    "Canada Goose":          3068,
    "Moose Knuckles":        5441,
    "Mackage":               4113,
    # ── Sportswear / lifestyle ─────────────────────────────────────────────
    "Nike":                  53,
    "Adidas":                14,
    "Puma":                  84,
    "New Balance":           3061,
    "Converse":              221,
    "Vans":                  204,
    "Asics":                 304,
    "Salomon":               2415,
    "On Running":            5765,
    "Jordan":                53,
    # ── Preppy / smart casual ──────────────────────────────────────────────
    "Ralph Lauren":          88,
    "Polo Ralph Lauren":     88,
    "Tommy Hilfiger":        97,
    "Calvin Klein":          78,
    "Lacoste":               1002,
    "Hugo Boss":             2237,
    "Armani":                156,
    "Emporio Armani":        158,
    "Giorgio Armani":        156,
    "Diesel":                198,
    "Levi's":                384,
    # ── Outdoor / technical ───────────────────────────────────────────────
    "The North Face":        3305,
    "Patagonia":             3019,
    "Arc'teryx":             4250,
    "Barbour":               2301,
    "CP Company":            2562,
}

# Vinted catalog IDs for broad category filtering
CATALOG_IDS: dict[str, int] = {
    "Women's clothes":       4,
    "Men's clothes":         5,
    "Women's shoes":         16,
    "Men's shoes":           17,
    "Women's bags":          1199,
    "Men's bags":            19,
    "Accessories":           1181,
    "Jewellery":             306,
    "Watches":               2562,
    "Sportswear":            76,
}

# Vinted condition / status IDs
CONDITIONS: dict[str, int] = {
    "New with tags":         6,
    "New without tags":      1,
    "Very good condition":   2,
    "Good condition":        3,
    "Satisfactory":          4,
}

# Convenience groups
CONDITION_GROUPS: dict[str, list[int]] = {
    "mint":    [6, 1],
    "good":    [6, 1, 2],
    "any":     [6, 1, 2, 3, 4],
}
