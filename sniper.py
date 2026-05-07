"""Monitoring loop: polls Vinted and pushes new items to a callback."""

from __future__ import annotations

import asyncio
import logging
from collections import defaultdict
from typing import Any, Awaitable, Callable

from vinted_api import VintedAPI
from watchlist_config import Config, Watchlist

logger = logging.getLogger(__name__)

# Callback type: receives watchlist + item dict
NotifyCallback = Callable[[Watchlist, dict[str, Any]], Awaitable[None]]


class VintedSniper:
    """Polls every enabled watchlist on a configurable interval."""

    # How many seen item IDs to keep per watchlist (prevents unbounded growth)
    MAX_SEEN = 2000

    def __init__(self, config: Config, notify: NotifyCallback) -> None:
        self.config = config
        self.notify = notify
        self._seen: defaultdict[str, set[int]] = defaultdict(set)
        self._api = VintedAPI(config.country)
        self._running = False

    # ── Control ────────────────────────────────────────────────────────────────

    def start(self) -> asyncio.Task:  # type: ignore[type-arg]
        self._running = True
        return asyncio.create_task(self._loop(), name="sniper-loop")

    def stop(self) -> None:
        self._running = False

    def reload_api(self) -> None:
        """Recreate API client when country changes."""
        self._api = VintedAPI(self.config.country)

    # ── Main loop ──────────────────────────────────────────────────────────────

    async def _loop(self) -> None:
        logger.info("Sniper started. Polling every %ds.", self.config.poll_interval)
        while self._running:
            active = [w for w in self.config.watchlists if w.enabled]
            if not active:
                await asyncio.sleep(5)
                continue

            for wl in active:
                if not self._running:
                    break
                await self._poll(wl)
                # Small gap between watchlists to avoid hammering the API
                await asyncio.sleep(2)

            await asyncio.sleep(self.config.poll_interval)

    async def _poll(self, wl: Watchlist) -> None:
        try:
            items = await asyncio.to_thread(self._fetch, wl)
        except Exception as exc:
            logger.warning("[%s] Poll error: %s", wl.name, exc)
            return

        seen = self._seen[wl.id]
        new_items = []

        for item in items:
            iid = item.get("id")
            if iid is None or iid in seen:
                continue
            if not wl.matches(item):
                continue
            new_items.append(item)
            seen.add(iid)

        # Trim memory
        if len(seen) > self.MAX_SEEN:
            self._seen[wl.id] = set(list(seen)[-self.MAX_SEEN :])

        # Seed mode: on the very first poll don't notify (just learn what's there)
        if not self._seeded(wl.id) and items:
            logger.info("[%s] Seeded with %d existing items.", wl.name, len(seen))
            self._mark_seeded(wl.id)
            return

        for item in new_items:
            logger.info("[%s] NEW: %s – %s", wl.name, item.get("title"), item.get("price"))
            try:
                await self.notify(wl, item)
            except Exception as exc:
                logger.error("[%s] Notify failed: %s", wl.name, exc)

    def _fetch(self, wl: Watchlist) -> list[dict[str, Any]]:
        return self._api.get_items(
            brand_ids=wl.brand_ids or None,
            catalog_ids=wl.catalog_ids or None,
            search_text=wl.search_text or None,
            price_from=wl.price_min,
            price_to=wl.price_max,
            status_ids=wl.status_ids or None,
            per_page=96,
        )

    # ── Seed tracking ──────────────────────────────────────────────────────────

    _seeded_ids: set[str] = set()

    def _seeded(self, wl_id: str) -> bool:
        return wl_id in self._seeded_ids

    def _mark_seeded(self, wl_id: str) -> None:
        self._seeded_ids.add(wl_id)
