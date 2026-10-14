"""Builds time-travel/index.html from src/page.html.

Fonts from src/fonts are inlined as base64 so the page makes no request to
Google (GDPR) and stays one self-contained file you can paste into Shopify.

    python3 time-travel/build.py                # writes time-travel/index.html
    python3 time-travel/build.py --fragment X   # also writes the body-less fragment to X
"""
import base64
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent
FONTS = [
    ("Bodoni Moda", "normal", "400 700", "bodoni.woff2"),
    ("Bodoni Moda", "italic", "400 700", "bodoni-italic.woff2"),
    ("Manrope", "normal", "400 700", "manrope.woff2"),
    ("IBM Plex Mono", "normal", "400", "plex400.woff2"),
    ("IBM Plex Mono", "normal", "500", "plex500.woff2"),
]


def font_css() -> str:
    rules = []
    for family, style, weight, file in FONTS:
        data = base64.b64encode((ROOT / "src" / "fonts" / file).read_bytes()).decode()
        rules.append(
            f'@font-face{{font-family:"{family}";font-style:{style};font-weight:{weight};'
            f'font-display:swap;src:url(data:font/woff2;base64,{data}) format("woff2")}}'
        )
    return "\n".join(rules)


def main() -> None:
    src = (ROOT / "src" / "page.html").read_text()
    fragment = src.replace("/*FONTS*/", font_css())
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
