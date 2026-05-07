"""Vinted public catalog API client.

Browsing / searching does not require a Vinted account.
A valid session cookie is obtained automatically by visiting the homepage.
"""

from __future__ import annotations

import logging
import random
import time
from typing import Any

import requests
from requests import Session

logger = logging.getLogger(__name__)

# ── Country domains ────────────────────────────────────────────────────────────
COUNTRY_DOMAINS: dict[str, str] = {
    "fr": "vinted.fr",
    "de": "vinted.de",
    "uk": "vinted.co.uk",
    "es": "vinted.es",
    "it": "vinted.it",
    "pl": "vinted.pl",
    "nl": "vinted.nl",
    "be": "vinted.be",
    "pt": "vinted.pt",
    "cz": "vinted.cz",
    "lt": "vinted.lt",
    "lv": "vinted.lv",
    "at": "vinted.at",
    "se": "vinted.se",
    "fi": "vinted.fi",
    "ro": "vinted.ro",
    "hu": "vinted.hu",
    "sk": "vinted.sk",
    "gr": "vinted.gr",
}

_USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
]


class VintedAPI:
    """Thin wrapper around Vinted's undocumented public catalog API."""

    SESSION_TTL = 3600  # refresh cookie every hour

    def __init__(self, country: str = "fr") -> None:
        self.country = country.lower()
        self.domain = COUNTRY_DOMAINS.get(self.country, "vinted.fr")
        self.base_url = f"https://www.{self.domain}"
        self.api_url = f"{self.base_url}/api/v2"
        self._session: Session = requests.Session()
        self._session_ts: float = 0.0
        self._ua = random.choice(_USER_AGENTS)
        self._init_session()

    # ── Session management ─────────────────────────────────────────────────────

    def _init_session(self) -> None:
        self._session.headers.update(
            {
                "User-Agent": self._ua,
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "DNT": "1",
                "Referer": self.base_url + "/",
            }
        )
        self._refresh_cookie()

    def _refresh_cookie(self) -> None:
        try:
            resp = self._session.get(self.base_url, timeout=15)
            resp.raise_for_status()
            self._session_ts = time.time()
            logger.debug("Vinted session cookie refreshed.")
        except Exception as exc:
            logger.warning("Cookie refresh failed: %s", exc)

    def _ensure_session(self) -> None:
        if time.time() - self._session_ts > self.SESSION_TTL:
            self._refresh_cookie()

    # ── Item search ────────────────────────────────────────────────────────────

    def get_items(
        self,
        *,
        brand_ids: list[int] | None = None,
        catalog_ids: list[int] | None = None,
        search_text: str | None = None,
        price_from: float | None = None,
        price_to: float | None = None,
        status_ids: list[int] | None = None,
        order: str = "newest_first",
        per_page: int = 96,
        page: int = 1,
    ) -> list[dict[str, Any]]:
        """Return a list of item dicts matching the given filters."""
        self._ensure_session()

        params: dict[str, Any] = {
            "order": order,
            "per_page": per_page,
            "page": page,
        }
        if brand_ids:
            params["brand_ids[]"] = brand_ids
        if catalog_ids:
            params["catalog_ids[]"] = catalog_ids
        if search_text:
            params["search_text"] = search_text
        if price_from is not None:
            params["price_from"] = price_from
        if price_to is not None:
            params["price_to"] = price_to
        if status_ids:
            params["status_ids[]"] = status_ids

        for attempt in range(3):
            try:
                resp = self._session.get(
                    f"{self.api_url}/catalog/items",
                    params=params,
                    timeout=20,
                )
                if resp.status_code in (401, 403):
                    self._refresh_cookie()
                    continue
                resp.raise_for_status()
                data = resp.json()
                return data.get("items", [])
            except requests.RequestException as exc:
                logger.warning("Attempt %d failed: %s", attempt + 1, exc)
                time.sleep(2 ** attempt)
        return []

    # ── Brand search ───────────────────────────────────────────────────────────

    def search_brand(self, name: str) -> list[dict[str, Any]]:
        """Search Vinted brands by name, return list of {id, title} dicts."""
        self._ensure_session()
        try:
            resp = self._session.get(
                f"{self.api_url}/brands",
                params={"search_text": name, "per_page": 20},
                timeout=15,
            )
            resp.raise_for_status()
            return resp.json().get("brands", [])
        except Exception as exc:
            logger.error("Brand search failed: %s", exc)
            return []

    # ── Item detail ────────────────────────────────────────────────────────────

    def get_item(self, item_id: int) -> dict[str, Any]:
        """Fetch full detail for a single item."""
        self._ensure_session()
        try:
            resp = self._session.get(
                f"{self.api_url}/items/{item_id}",
                timeout=15,
            )
            resp.raise_for_status()
            return resp.json().get("item", {})
        except Exception as exc:
            logger.error("Item fetch failed: %s", exc)
            return {}

    # ── Helpers ────────────────────────────────────────────────────────────────

    def item_url(self, item: dict[str, Any]) -> str:
        url = item.get("url", "")
        if url:
            return url
        return f"{self.base_url}/items/{item['id']}"

    def item_photo_url(self, item: dict[str, Any]) -> str | None:
        photo = item.get("photo") or {}
        return photo.get("url") or photo.get("full_size_url")
