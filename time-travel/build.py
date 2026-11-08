"""Builds time-travel/index.html from src/page.html.

Fonts from src/fonts are inlined as base64 so the page makes no request to
Google (GDPR). Also writes shopify/ (template + assets) for the Shopify theme.

    python3 time-travel/build.py                # writes time-travel/index.html
    python3 time-travel/build.py --fragment X   # also writes the body-less fragment to X
"""
import base64
import json
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).parent
FONTS = [
    ("Bodoni Moda", "normal", "400 700", "bodoni.woff2"),
    ("Bodoni Moda", "italic", "400 700", "bodoni-italic.woff2"),
    ("Manrope", "normal", "400 700", "manrope.woff2"),
    ("IBM Plex Mono", "normal", "400", "plex400.woff2"),
    ("IBM Plex Mono", "normal", "500", "plex500.woff2"),
]
# share preview (og:image): absolute URL on Shopify, a sibling file for the stand-alone page
OG_SHOPIFY = """<meta property="og:url" content="{{ canonical_url }}">
<link rel="canonical" href="{{ canonical_url }}">
<meta property="og:image" content="{{ 'time-travel-og.jpg' | asset_url | prepend: 'https:' }}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:image" content="{{ 'time-travel-og.jpg' | asset_url | prepend: 'https:' }}">"""
OG_LOCAL = '<meta property="og:image" content="og-image.jpg">'


def font_css() -> str:
    rules = []
    for family, style, weight, file in FONTS:
        data = base64.b64encode((ROOT / "src" / "fonts" / file).read_bytes()).decode()
        rules.append(
            f'@font-face{{font-family:"{family}";font-style:{style};font-weight:{weight};'
            f'font-display:swap;src:url(data:font/woff2;base64,{data}) format("woff2")}}'
        )
    return "\n".join(rules)


def build_shopify(fragment: str) -> None:
    """Shopify caps Liquid templates at 256 KB, so ship a small template plus two theme assets.

    shopify/templates/page.time-travel.liquid  markup only, links the assets via asset_url
    shopify/layout/time-travel.liquid          the same page as a layout, for the home page
    shopify/templates/index.json               home page template that uses that layout (replaces the theme's)
    shopify/assets/time-travel.css             fonts (inlined) + styles
    shopify/assets/time-travel.js              the scene (ES module, three.js via import map)
    shopify/assets/time-travel-og.jpg          share preview (copied from og-image.jpg)

    {{ content_for_header }} keeps Shopify analytics, customer-event pixels and the cookie banner working.
    """
    head, body = fragment.split("<!--BODY-->", 1)
    styles = re.findall(r"<style>(.*?)</style>", head, re.S)
    meta = re.sub(r"<style>.*?</style>", "", head, flags=re.S).strip().replace("<!--OG-->", OG_SHOPIFY)
    module = re.search(r'<script type="module">(.*?)</script>', body, re.S)
    markup = body[: module.start()].rstrip()
    out = ROOT / "shopify"
    (out / "assets").mkdir(parents=True, exist_ok=True)
    (out / "templates").mkdir(parents=True, exist_ok=True)
    (out / "assets" / "time-travel.css").write_text("\n".join(x.strip() for x in styles) + "\n")
    (out / "assets" / "time-travel.js").write_text(module.group(1).strip() + "\n")
    if (ROOT / "og-image.jpg").exists():
        shutil.copyfile(ROOT / "og-image.jpg", out / "assets" / "time-travel-og.jpg")
    template = (
        "{% layout none %}\n<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        f"{meta}\n{{{{ content_for_header }}}}\n{{{{ 'time-travel.css' | asset_url | stylesheet_tag }}}}\n</head>\n<body>{markup}\n"
        "<script type=\"module\" src=\"{{ 'time-travel.js' | asset_url }}\"></script>\n</body>\n</html>\n"
    )
    (out / "templates" / "page.time-travel.liquid").write_text(template)
    # Home page: a JSON template cannot be swapped for a Liquid one without deleting it, so it points to a
    # layout that is this page; content_for_layout (an empty Custom Liquid section) is rendered hidden.
    (out / "layout").mkdir(exist_ok=True)
    layout = template.replace("{% layout none %}\n", "", 1).replace("</body>", "<div hidden>{{ content_for_layout }}</div>\n</body>", 1)
    (out / "layout" / "time-travel.liquid").write_text(layout)
    index = {"layout": "time-travel", "sections": {"main": {"type": "custom-liquid", "settings": {"custom_liquid": "", "padding_top": 0, "padding_bottom": 0}}}, "order": ["main"]}
    (out / "templates" / "index.json").write_text(json.dumps(index, indent=2) + "\n")
    size = len(template.encode()) / 1024
    assert size < 256, "Liquid template over Shopify's 256 KB limit"
    print("wrote", out, f"(template {size:.0f} KB)")


def main() -> None:
    src = (ROOT / "src" / "page.html").read_text()
    fragment = src.replace("/*FONTS*/", font_css())
    build_shopify(fragment)
    fragment = fragment.replace("<!--OG-->", OG_LOCAL)
    head, body = fragment.split("<!--BODY-->", 1)
    doc = (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        f"{head}</head>\n<body>{body}</body>\n</html>\n"
    )
    for marker in ("{{", "{%"):
        assert marker not in doc, f"{marker} would be parsed by Shopify Liquid"
    (ROOT / "index.html").write_text(doc)
    print("wrote", ROOT / "index.html", f"{len(doc) / 1024:.0f} KB")
    if "--fragment" in sys.argv:
        out = pathlib.Path(sys.argv[sys.argv.index("--fragment") + 1])
        out.write_text(fragment.replace("<!--BODY-->", ""))
        print("wrote", out)


if __name__ == "__main__":
    main()
