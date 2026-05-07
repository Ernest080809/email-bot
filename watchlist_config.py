"""Persistent watchlist configuration stored in config.json."""

from __future__ import annotations

import json
import os
import uuid
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any

CONFIG_PATH = Path(os.getenv("CONFIG_PATH", "config.json"))


@dataclass
class Watchlist:
    name: str
    brand_ids: list[int] = field(default_factory=list)
    search_text: str = ""
    price_min: float | None = None
    price_max: float | None = None
    catalog_ids: list[int] = field(default_factory=list)
    status_ids: list[int] = field(default_factory=list)  # condition filter
    enabled: bool = True
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])

    def matches(self, item: dict[str, Any]) -> bool:
        """True when this watchlist's filters match the item (client-side guard)."""
        try:
            price = float(item.get("price", 0))
        except (TypeError, ValueError):
            price = 0.0
        if self.price_min is not None and price < self.price_min:
            return False
        if self.price_max is not None and price > self.price_max:
            return False
        return True

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Watchlist":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


@dataclass
class Config:
    country: str = "fr"
    poll_interval: int = 30        # seconds between polls per watchlist
    watchlists: list[Watchlist] = field(default_factory=list)
    admin_chat_id: int | None = None

    # ── Persistence ────────────────────────────────────────────────────────────

    def save(self) -> None:
        data = {
            "country": self.country,
            "poll_interval": self.poll_interval,
            "admin_chat_id": self.admin_chat_id,
            "watchlists": [w.to_dict() for w in self.watchlists],
        }
        CONFIG_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False))

    @classmethod
    def load(cls) -> "Config":
        if not CONFIG_PATH.exists():
            return cls()
        try:
            data = json.loads(CONFIG_PATH.read_text())
            watchlists = [Watchlist.from_dict(w) for w in data.get("watchlists", [])]
            return cls(
                country=data.get("country", "fr"),
                poll_interval=data.get("poll_interval", 30),
                admin_chat_id=data.get("admin_chat_id"),
                watchlists=watchlists,
            )
        except Exception:
            return cls()

    # ── Watchlist helpers ──────────────────────────────────────────────────────

    def get_watchlist(self, wl_id: str) -> Watchlist | None:
        return next((w for w in self.watchlists if w.id == wl_id), None)

    def add_watchlist(self, wl: Watchlist) -> None:
        self.watchlists.append(wl)
        self.save()

    def remove_watchlist(self, wl_id: str) -> bool:
        before = len(self.watchlists)
        self.watchlists = [w for w in self.watchlists if w.id != wl_id]
        if len(self.watchlists) < before:
            self.save()
            return True
        return False

    def toggle_watchlist(self, wl_id: str) -> bool | None:
        wl = self.get_watchlist(wl_id)
        if wl is None:
            return None
        wl.enabled = not wl.enabled
        self.save()
        return wl.enabled
