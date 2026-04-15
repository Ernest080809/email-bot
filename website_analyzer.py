"""
website_analyzer.py
-------------------
Fetches a vintage fashion website, extracts product data and branding signals,
then uses Claude to produce a structured aesthetic analysis that drives the
personalised quiz and recommendation pipeline.
"""

import re
import json
import httpx
from bs4 import BeautifulSoup
from anthropic import Anthropic

client = Anthropic()

# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------

_UNWANTED_TAGS = {"script", "style", "noscript", "meta", "link", "head"}

def _fetch_html(url: str, timeout: int = 20) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }
    resp = httpx.get(url, headers=headers, timeout=timeout, follow_redirects=True)
    resp.raise_for_status()
    return resp.text


def _clean_text(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    for tag in soup.find_all(_UNWANTED_TAGS):
        tag.decompose()
    text = soup.get_text(separator=" ", strip=True)
    # collapse whitespace
    text = re.sub(r"\s+", " ", text)
    return text[:12000]  # cap at ~3 k tokens for context efficiency


def _extract_products(html: str, base_url: str) -> list[dict]:
    """
    Heuristic product extraction that works across common Shopify / WooCommerce
    / custom vintage shop layouts.
    """
    soup = BeautifulSoup(html, "lxml")
    products = []

    # Try JSON-LD structured data first (most reliable)
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "")
            items = data if isinstance(data, list) else [data]
            for item in items:
                if item.get("@type") in ("Product", "ItemList"):
                    if item["@type"] == "ItemList":
                        for el in item.get("itemListElement", []):
                            p = el.get("item", el)
                            products.append(_normalize_ld_product(p))
                    else:
                        products.append(_normalize_ld_product(item))
        except Exception:
            pass

    # Fallback: scrape common CSS patterns
    if not products:
        for card in soup.select(
            ".product, .product-card, .product-item, "
            "[class*='product'], article.type-product"
        )[:30]:
            name_el = card.select_one(
                "h2, h3, h4, .product-title, .product-name, [class*='title']"
            )
            price_el = card.select_one(
                ".price, .product-price, [class*='price'], ins .amount"
            )
            img_el = card.select_one("img")
            link_el = card.select_one("a[href]")

            name = name_el.get_text(strip=True) if name_el else ""
            price = price_el.get_text(strip=True) if price_el else ""
            image = img_el.get("src", img_el.get("data-src", "")) if img_el else ""
            link = link_el.get("href", "") if link_el else ""

            if name:
                products.append(
                    {
                        "name": name,
                        "price": price,
                        "image": _absolute(image, base_url),
                        "url": _absolute(link, base_url),
                        "description": "",
                        "category": "",
                    }
                )

    return products[:40]  # cap to avoid huge prompts


def _normalize_ld_product(p: dict) -> dict:
    offers = p.get("offers", {})
    if isinstance(offers, list):
        offers = offers[0] if offers else {}
    return {
        "name": p.get("name", ""),
        "price": str(offers.get("price", offers.get("priceRange", ""))),
        "image": (p.get("image") or [""])[0]
        if isinstance(p.get("image"), list)
        else p.get("image", ""),
        "url": p.get("url", offers.get("url", "")),
        "description": p.get("description", "")[:300],
        "category": p.get("category", ""),
    }


def _absolute(url: str, base: str) -> str:
    if not url:
        return ""
    if url.startswith("//"):
        return "https:" + url
    if url.startswith("http"):
        return url
    from urllib.parse import urljoin
    return urljoin(base, url)


def _extract_brand_signals(html: str) -> dict:
    """Pull colours, fonts, taglines from meta/CSS."""
    soup = BeautifulSoup(html, "lxml")
    signals: dict = {}

    # Page title / tagline
    title = soup.find("title")
    signals["page_title"] = title.get_text(strip=True) if title else ""

    desc = soup.find("meta", attrs={"name": "description"})
    signals["meta_description"] = desc.get("content", "") if desc else ""

    og_title = soup.find("meta", property="og:title")
    og_desc = soup.find("meta", property="og:description")
    signals["og_title"] = og_title.get("content", "") if og_title else ""
    signals["og_description"] = og_desc.get("content", "") if og_desc else ""

    # Inline colour hints
    inline_styles = " ".join(
        tag.get("style", "") for tag in soup.find_all(style=True)
    )
    hex_colors = re.findall(r"#[0-9a-fA-F]{3,6}", inline_styles)
    signals["color_hints"] = list(set(hex_colors))[:10]

    # Nav / menu items reveal category vocabulary
    nav_links = [
        a.get_text(strip=True)
        for a in soup.select("nav a, header a, .menu a, .navigation a")
        if a.get_text(strip=True)
    ]
    signals["navigation"] = list(set(nav_links))[:20]

    return signals


# ---------------------------------------------------------------------------
# Claude analysis
# ---------------------------------------------------------------------------

_ANALYSIS_SYSTEM = """\
You are an expert fashion analyst specialising in vintage and second-hand clothing.
You receive scraped content from a vintage fashion e-commerce website and must
return a JSON object that captures the shop's unique aesthetic, target customer,
style vocabulary, and product catalogue in enough detail to power a personalised
style quiz and product recommendation engine.

Return ONLY valid JSON – no prose, no markdown fences.
"""

_ANALYSIS_SCHEMA = """\
{
  "shop_name": "string",
  "tagline": "string",
  "aesthetic_summary": "2-3 sentence description of the overall aesthetic",
  "era_focus": ["list of fashion eras or decades featured, e.g. '70s', '90s grunge'"],
  "style_keywords": ["8-12 single-word or short-phrase descriptors of the shop's style"],
  "colour_palette": ["4-6 dominant colours or colour families"],
  "target_customer_profile": "description of the ideal customer persona",
  "unique_selling_points": ["list of what makes this shop distinct"],
  "product_categories": ["list of product categories found"],
  "products": [
    {
      "name": "string",
      "price": "string",
      "image": "url or empty string",
      "url": "url or empty string",
      "description": "string",
      "category": "string",
      "style_tags": ["3-5 style/era tags for this product"]
    }
  ],
  "quiz_themes": {
    "occasion_options": ["5 occasion-style options specific to this shop"],
    "aesthetic_options": ["5 sub-aesthetic options pulled from this shop's vocabulary"],
    "era_options": ["5 era/decade preferences relevant to this shop's inventory"],
    "fit_options": ["5 silhouette/fit preferences visible in this shop's products"],
    "colour_mood_options": ["5 colour-mood options aligned with this shop's palette"]
  }
}
"""

def analyze_website(url: str) -> dict:
    """
    Main entry point.  Returns the structured analysis dict.
    Raises on network or Claude errors.
    """
    html = _fetch_html(url)
    page_text = _clean_text(html)
    brand_signals = _extract_brand_signals(html)
    products = _extract_products(html, url)

    prompt = f"""
Website URL: {url}

--- BRAND SIGNALS ---
{json.dumps(brand_signals, indent=2)}

--- SCRAPED PAGE TEXT (first 12 000 chars) ---
{page_text}

--- RAW PRODUCTS FOUND ({len(products)}) ---
{json.dumps(products, indent=2)}

---
Using all of the above, return the JSON object matching exactly this schema:
{_ANALYSIS_SCHEMA}

Important rules:
- Populate the `products` array with the real items found; add style_tags to each.
- quiz_themes must be completely tailored to THIS shop – do not use generic fashion terms.
- All options in quiz_themes should feel native to this store's specific vibe and inventory.
""".strip()

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=_ANALYSIS_SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = response.content[0].text.strip()
    # Strip any accidental markdown fences
    raw = re.sub(r"^```json\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    analysis = json.loads(raw)

    # Merge in any products the LLM may have dropped
    if not analysis.get("products") and products:
        analysis["products"] = products

    return analysis
