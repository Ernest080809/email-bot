"""Telegram bot interface for the Vinted Designer Sniper."""

from __future__ import annotations

import asyncio
import logging
import os
from typing import Any

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Update,
)
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from brands import LUXURY_BRANDS, CATALOG_IDS, CONDITIONS, CONDITION_GROUPS
from vinted_api import VintedAPI
from watchlist_config import Config, Watchlist

logger = logging.getLogger(__name__)

# ── Conversation states ────────────────────────────────────────────────────────
(
    WL_NAME,
    WL_BRANDS,
    WL_SEARCH,
    WL_PRICE,
    WL_CONDITION,
    WL_CATEGORY,
    WL_CONFIRM,
    BRAND_SEARCH,
) = range(8)

CANCEL = "cancel"
DONE = "done"

# ── Helpers ────────────────────────────────────────────────────────────────────

def _chunk(lst: list, n: int) -> list[list]:
    return [lst[i : i + n] for i in range(0, len(lst), n)]


def _condition_label(ids: list[int]) -> str:
    if not ids:
        return "Any"
    rev = {v: k for k, v in CONDITIONS.items()}
    return ", ".join(rev.get(i, str(i)) for i in ids)


def _catalog_label(ids: list[int]) -> str:
    if not ids:
        return "All categories"
    rev = {v: k for k, v in CATALOG_IDS.items()}
    return ", ".join(rev.get(i, str(i)) for i in ids)


def _item_condition_label(item: dict[str, Any]) -> str:
    return item.get("status") or item.get("status_title") or "Unknown"


def _seller_rating(item: dict[str, Any]) -> str:
    user = item.get("user") or {}
    rating = user.get("feedback_reputation")
    if rating is None:
        return ""
    pct = int(float(rating) * 100)
    return f"⭐ {pct}% positive"


def _price_str(item: dict[str, Any]) -> str:
    try:
        price = float(item.get("price", 0))
        currency = item.get("currency") or "€"
        symbol = {"EUR": "€", "GBP": "£", "USD": "$", "PLN": "zł",
                  "CZK": "Kč", "HUF": "Ft", "RON": "lei"}.get(currency, currency)
        return f"{symbol}{price:,.2f}"
    except (TypeError, ValueError):
        return "?"


# ── Notification formatter ─────────────────────────────────────────────────────

def build_notification(wl: Watchlist, item: dict[str, Any], item_url: str) -> tuple[str, InlineKeyboardMarkup]:
    title = item.get("title", "Unknown item")
    brand = item.get("brand_title", "")
    price = _price_str(item)
    size = item.get("size_title") or item.get("size") or "—"
    condition = _item_condition_label(item)
    seller = (item.get("user") or {}).get("login", "?")
    rating = _seller_rating(item)
    location = item.get("city") or ""

    text = (
        f"🔥 *NEW DESIGNER DROP* — _{wl.name}_\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👜 *{_esc(title)}*\n"
        f"💰 *{price}*\n"
    )
    if brand:
        text += f"🏷️ Brand: {_esc(brand)}\n"
    text += (
        f"📏 Size: {_esc(size)}\n"
        f"✨ Condition: {_esc(condition)}\n"
        f"👤 Seller: @{_esc(seller)}"
    )
    if rating:
        text += f"  {rating}"
    text += "\n"
    if location:
        text += f"📍 {_esc(location)}\n"
    text += "━━━━━━━━━━━━━━━━━━━━\n⚡ _Act fast — designer pieces sell in minutes!_"

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⚡ BUY NOW", url=item_url),
                InlineKeyboardButton("👁 View Item", url=item_url),
            ],
        ]
    )
    return text, keyboard


def _esc(text: str) -> str:
    """Escape MarkdownV2 special chars."""
    for ch in r"\_*[]()~`>#+-=|{}.!":
        text = text.replace(ch, f"\\{ch}")
    return text


# ── Bot class ──────────────────────────────────────────────────────────────────

class SniperBot:
    def __init__(self, token: str, config: Config) -> None:
        self.token = token
        self.config = config
        self._api = VintedAPI(config.country)
        self.app: Application = (
            Application.builder().token(token).build()
        )
        self._register_handlers()

    # ── Registration ───────────────────────────────────────────────────────────

    def _register_handlers(self) -> None:
        app = self.app
        add_conv = ConversationHandler(
            entry_points=[CommandHandler("add", self.cmd_add_start)],
            states={
                WL_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.wl_got_name)],
                WL_BRANDS: [
                    CallbackQueryHandler(self.wl_brand_toggle, pattern=r"^b:"),
                    CallbackQueryHandler(self.wl_brand_search, pattern=r"^bsearch$"),
                    CallbackQueryHandler(self.wl_brands_done, pattern=r"^bdone$"),
                    MessageHandler(filters.TEXT & ~filters.COMMAND, self.wl_brand_search_text),
                ],
                WL_SEARCH: [
                    MessageHandler(filters.TEXT & ~filters.COMMAND, self.wl_got_search),
                    CallbackQueryHandler(self.wl_skip_search, pattern=r"^skip_search$"),
                ],
                WL_PRICE: [
                    MessageHandler(filters.TEXT & ~filters.COMMAND, self.wl_got_price),
                    CallbackQueryHandler(self.wl_skip_price, pattern=r"^skip_price$"),
                ],
                WL_CONDITION: [
                    CallbackQueryHandler(self.wl_condition_toggle, pattern=r"^c:"),
                    CallbackQueryHandler(self.wl_condition_done, pattern=r"^cdone$"),
                ],
                WL_CATEGORY: [
                    CallbackQueryHandler(self.wl_category_toggle, pattern=r"^cat:"),
                    CallbackQueryHandler(self.wl_category_done, pattern=r"^catdone$"),
                ],
                WL_CONFIRM: [
                    CallbackQueryHandler(self.wl_confirm_save, pattern=r"^wlsave$"),
                    CallbackQueryHandler(self.wl_confirm_cancel, pattern=r"^wlcancel$"),
                ],
            },
            fallbacks=[CommandHandler("cancel", self.cmd_cancel)],
            per_user=True,
        )

        app.add_handler(add_conv)
        app.add_handler(CommandHandler("start", self.cmd_start))
        app.add_handler(CommandHandler("status", self.cmd_status))
        app.add_handler(CommandHandler("watchlist", self.cmd_watchlist))
        app.add_handler(CommandHandler("remove", self.cmd_remove))
        app.add_handler(CommandHandler("toggle", self.cmd_toggle))
        app.add_handler(CommandHandler("interval", self.cmd_interval))
        app.add_handler(CommandHandler("country", self.cmd_country))
        app.add_handler(CommandHandler("brands", self.cmd_brands))
        app.add_handler(CommandHandler("cancel", self.cmd_cancel))
        app.add_handler(CommandHandler("test", self.cmd_test))
        # Watchlist quick-action buttons from notifications
        app.add_handler(CallbackQueryHandler(self.cb_watchlist_action, pattern=r"^wl:"))

    # ── Auth guard ─────────────────────────────────────────────────────────────

    def _is_admin(self, update: Update) -> bool:
        uid = update.effective_user.id if update.effective_user else None
        if self.config.admin_chat_id is None:
            # First user to /start becomes admin
            return True
        return uid == self.config.admin_chat_id

    async def _require_admin(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
        if not self._is_admin(update):
            await update.effective_message.reply_text("⛔ Unauthorized.")
            return False
        return True

    # ── /start ─────────────────────────────────────────────────────────────────

    async def cmd_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = update.effective_user
        chat_id = update.effective_chat.id

        if self.config.admin_chat_id is None:
            self.config.admin_chat_id = chat_id
            self.config.save()
            welcome_suffix = "\n\n✅ You are now the *admin* of this bot."
        else:
            welcome_suffix = ""

        await update.message.reply_text(
            f"👋 *Vinted Designer Sniper* — Welcome, {user.first_name}!{welcome_suffix}\n\n"
            "I monitor Vinted for luxury & designer pieces and alert you *instantly* "
            "when something new drops.\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "*Commands*\n"
            "/add — Create a new watchlist\n"
            "/watchlist — View & manage watchlists\n"
            "/status — Bot & sniper status\n"
            "/test — Preview latest items for all watchlists\n"
            "/brands — Search Vinted brand IDs\n"
            "/country `<code>` — Switch country (fr/de/uk/es/it…)\n"
            "/interval `<seconds>` — Set poll interval (min 15s)\n"
            "/remove `<id>` — Delete a watchlist\n"
            "/toggle `<id>` — Enable / pause a watchlist\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "Start with */add* to create your first watchlist.",
            parse_mode=ParseMode.MARKDOWN,
        )

    # ── /status ────────────────────────────────────────────────────────────────

    async def cmd_status(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        wls = self.config.watchlists
        active = sum(1 for w in wls if w.enabled)
        lines = [
            "📊 *Sniper Status*",
            f"• Country: `{self.config.country}`",
            f"• Poll interval: `{self.config.poll_interval}s`",
            f"• Watchlists: {len(wls)} total, {active} active",
        ]
        await update.message.reply_text("\n".join(lines), parse_mode=ParseMode.MARKDOWN)

    # ── /watchlist ─────────────────────────────────────────────────────────────

    async def cmd_watchlist(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        wls = self.config.watchlists
        if not wls:
            await update.message.reply_text(
                "No watchlists yet. Use /add to create one.", parse_mode=ParseMode.MARKDOWN
            )
            return

        lines = ["📋 *Your Watchlists*\n"]
        for wl in wls:
            status = "🟢" if wl.enabled else "🔴"
            brand_names = ", ".join(
                next((k for k, v in LUXURY_BRANDS.items() if v == bid), str(bid))
                for bid in wl.brand_ids
            ) or "—"
            price_range = "any price"
            if wl.price_min is not None or wl.price_max is not None:
                lo = f"€{wl.price_min}" if wl.price_min is not None else "€0"
                hi = f"€{wl.price_max}" if wl.price_max is not None else "∞"
                price_range = f"{lo}–{hi}"
            lines.append(
                f"{status} *{wl.name}* `[{wl.id}]`\n"
                f"  Brands: {brand_names}\n"
                f"  Price: {price_range}\n"
                f"  Keywords: {wl.search_text or '—'}\n"
                f"  Condition: {_condition_label(wl.status_ids)}\n"
                f"  Category: {_catalog_label(wl.catalog_ids)}\n"
            )

        keyboard = []
        for wl in wls:
            lbl = "⏸ Pause" if wl.enabled else "▶️ Resume"
            keyboard.append(
                [
                    InlineKeyboardButton(lbl, callback_data=f"wl:toggle:{wl.id}"),
                    InlineKeyboardButton("🗑 Remove", callback_data=f"wl:remove:{wl.id}"),
                ]
            )

        await update.message.reply_text(
            "\n".join(lines),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    # ── /remove & /toggle ──────────────────────────────────────────────────────

    async def cmd_remove(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not await self._require_admin(update, context):
            return
        if not context.args:
            await update.message.reply_text("Usage: /remove <watchlist_id>")
            return
        wid = context.args[0]
        if self.config.remove_watchlist(wid):
            await update.message.reply_text(f"✅ Watchlist `{wid}` removed.", parse_mode=ParseMode.MARKDOWN)
        else:
            await update.message.reply_text(f"❌ Watchlist `{wid}` not found.", parse_mode=ParseMode.MARKDOWN)

    async def cmd_toggle(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not await self._require_admin(update, context):
            return
        if not context.args:
            await update.message.reply_text("Usage: /toggle <watchlist_id>")
            return
        wid = context.args[0]
        result = self.config.toggle_watchlist(wid)
        if result is None:
            await update.message.reply_text(f"❌ Watchlist `{wid}` not found.", parse_mode=ParseMode.MARKDOWN)
        else:
            state = "▶️ enabled" if result else "⏸ paused"
            await update.message.reply_text(
                f"Watchlist `{wid}` is now *{state}*.", parse_mode=ParseMode.MARKDOWN
            )

    # ── /interval ──────────────────────────────────────────────────────────────

    async def cmd_interval(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not await self._require_admin(update, context):
            return
        if not context.args or not context.args[0].isdigit():
            await update.message.reply_text("Usage: /interval <seconds> (minimum 15)")
            return
        secs = max(15, int(context.args[0]))
        self.config.poll_interval = secs
        self.config.save()
        await update.message.reply_text(f"✅ Poll interval set to `{secs}s`.", parse_mode=ParseMode.MARKDOWN)

    # ── /country ───────────────────────────────────────────────────────────────

    async def cmd_country(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not await self._require_admin(update, context):
            return
        from vinted_api import COUNTRY_DOMAINS
        if not context.args or context.args[0].lower() not in COUNTRY_DOMAINS:
            codes = " | ".join(sorted(COUNTRY_DOMAINS.keys()))
            await update.message.reply_text(f"Usage: /country <code>\nAvailable: {codes}")
            return
        self.config.country = context.args[0].lower()
        self.config.save()
        self._api = VintedAPI(self.config.country)
        await update.message.reply_text(
            f"✅ Country set to `{self.config.country}`.", parse_mode=ParseMode.MARKDOWN
        )

    # ── /brands ────────────────────────────────────────────────────────────────

    async def cmd_brands(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if context.args:
            query = " ".join(context.args)
            await update.message.reply_text(f"🔍 Searching Vinted for brand: *{query}*…", parse_mode=ParseMode.MARKDOWN)
            results = await asyncio.to_thread(self._api.search_brand, query)
            if not results:
                await update.message.reply_text("No brands found.")
                return
            lines = ["*Brand search results:*\n"]
            for b in results[:15]:
                lines.append(f"• `{b['id']}` — {b.get('title', '?')}")
            await update.message.reply_text("\n".join(lines), parse_mode=ParseMode.MARKDOWN)
        else:
            # Show curated luxury brands
            lines = ["*Curated luxury brand IDs:*\n"]
            for name, bid in list(LUXURY_BRANDS.items())[:30]:
                lines.append(f"• `{bid}` — {name}")
            lines.append("\n_Use /brands <name> to search for more._")
            await update.message.reply_text("\n".join(lines), parse_mode=ParseMode.MARKDOWN)

    # ── /test ──────────────────────────────────────────────────────────────────

    async def cmd_test(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        wls = [w for w in self.config.watchlists if w.enabled]
        if not wls:
            await update.message.reply_text("No active watchlists. Create one with /add.")
            return
        await update.message.reply_text(f"🔍 Fetching latest items for {len(wls)} watchlist(s)…")
        for wl in wls[:3]:  # cap to avoid spam
            items = await asyncio.to_thread(
                self._api.get_items,
                **{
                    "brand_ids": wl.brand_ids or None,
                    "catalog_ids": wl.catalog_ids or None,
                    "search_text": wl.search_text or None,
                    "price_from": wl.price_min,
                    "price_to": wl.price_max,
                    "status_ids": wl.status_ids or None,
                    "per_page": 3,
                },
            )
            if not items:
                await update.message.reply_text(f"*{wl.name}*: No items found.", parse_mode=ParseMode.MARKDOWN)
                continue
            for item in items[:2]:
                await self._send_item(update.effective_chat.id, wl, item)
                await asyncio.sleep(0.5)

    # ── /cancel ────────────────────────────────────────────────────────────────

    async def cmd_cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        context.user_data.clear()
        await update.message.reply_text("❌ Cancelled.")
        return ConversationHandler.END

    # ── Watchlist creation conversation ────────────────────────────────────────

    async def cmd_add_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        if not await self._require_admin(update, context):
            return ConversationHandler.END
        context.user_data.clear()
        context.user_data["wl"] = {
            "brand_ids": [],
            "catalog_ids": [],
            "status_ids": [],
        }
        await update.message.reply_text(
            "🆕 *New Watchlist* — Step 1/6\n\nGive this watchlist a name "
            "(e.g. *Gucci Shoes*, *Moncler Jackets*, *Louboutin Heels*):",
            parse_mode=ParseMode.MARKDOWN,
        )
        return WL_NAME

    async def wl_got_name(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        name = update.message.text.strip()
        if not name:
            await update.message.reply_text("Please enter a valid name.")
            return WL_NAME
        context.user_data["wl"]["name"] = name

        # Build brand keyboard
        kb = self._brand_keyboard(context.user_data["wl"]["brand_ids"])
        await update.message.reply_text(
            "🏷️ *Step 2/6 — Brands*\n\nSelect the brands to monitor. "
            "Tap to toggle (✅ = selected).\nYou can also type a brand name to search Vinted.",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=kb,
        )
        return WL_BRANDS

    def _brand_keyboard(self, selected: list[int]) -> InlineKeyboardMarkup:
        brands = list(LUXURY_BRANDS.items())[:24]  # show top 24
        rows = []
        for chunk in _chunk(brands, 2):
            row = []
            for name, bid in chunk:
                tick = "✅ " if bid in selected else ""
                row.append(InlineKeyboardButton(f"{tick}{name}", callback_data=f"b:{bid}"))
            rows.append(row)
        rows.append(
            [
                InlineKeyboardButton("🔍 Search brand…", callback_data="bsearch"),
                InlineKeyboardButton("✔️ Done", callback_data="bdone"),
            ]
        )
        return InlineKeyboardMarkup(rows)

    async def wl_brand_toggle(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.callback_query.answer()
        bid = int(update.callback_query.data.split(":")[1])
        selected: list[int] = context.user_data["wl"]["brand_ids"]
        if bid in selected:
            selected.remove(bid)
        else:
            selected.append(bid)
        await update.callback_query.edit_message_reply_markup(
            reply_markup=self._brand_keyboard(selected)
        )
        return WL_BRANDS

    async def wl_brand_search(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.callback_query.answer()
        context.user_data["_brand_search"] = True
        await update.callback_query.message.reply_text("Type a brand name to search Vinted:")
        return WL_BRANDS

    async def wl_brand_search_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        if not context.user_data.get("_brand_search"):
            # Treat any free text in BRANDS state as a search
            context.user_data["_brand_search"] = True
        context.user_data["_brand_search"] = False
        query = update.message.text.strip()
        results = await asyncio.to_thread(self._api.search_brand, query)
        if not results:
            await update.message.reply_text("No brands found. Try again or tap *Done*.", parse_mode=ParseMode.MARKDOWN)
            return WL_BRANDS
        selected = context.user_data["wl"]["brand_ids"]
        rows = []
        for b in results[:10]:
            tick = "✅ " if b["id"] in selected else ""
            rows.append(
                [InlineKeyboardButton(f"{tick}{b['title']} ({b['id']})", callback_data=f"b:{b['id']}")]
            )
        rows.append([InlineKeyboardButton("✔️ Done", callback_data="bdone")])
        await update.message.reply_text(
            f"Results for *{query}*:", parse_mode=ParseMode.MARKDOWN, reply_markup=InlineKeyboardMarkup(rows)
        )
        return WL_BRANDS

    async def wl_brands_done(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.callback_query.answer()
        await update.callback_query.message.reply_text(
            "🔑 *Step 3/6 — Keywords*\n\nEnter search keywords "
            "(e.g. `high top`, `1955 bag`, `parka`) or tap *Skip*.\n\n"
            "_Keywords narrow results further within the selected brands._",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⏭ Skip", callback_data="skip_search")]]
            ),
        )
        return WL_SEARCH

    async def wl_got_search(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        context.user_data["wl"]["search_text"] = update.message.text.strip()
        await self._ask_price(update)
        return WL_PRICE

    async def wl_skip_search(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.callback_query.answer()
        context.user_data["wl"]["search_text"] = ""
        await self._ask_price(update.callback_query)
        return WL_PRICE

    async def _ask_price(self, target: Any) -> None:
        text = (
            "💶 *Step 4/6 — Price Range*\n\nEnter `min max` in EUR "
            "(e.g. `100 800`), just `min` (e.g. `200`), or tap *Skip* for any price."
        )
        kb = InlineKeyboardMarkup([[InlineKeyboardButton("⏭ Skip", callback_data="skip_price")]])
        if hasattr(target, "message"):
            await target.message.reply_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=kb)
        else:
            await target.reply_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=kb)

    async def wl_got_price(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        parts = update.message.text.strip().split()
        try:
            if len(parts) == 2:
                context.user_data["wl"]["price_min"] = float(parts[0])
                context.user_data["wl"]["price_max"] = float(parts[1])
            elif len(parts) == 1:
                context.user_data["wl"]["price_min"] = float(parts[0])
                context.user_data["wl"]["price_max"] = None
            else:
                raise ValueError
        except ValueError:
            await update.message.reply_text("Please enter `min max` or just `min` (numbers only).", parse_mode=ParseMode.MARKDOWN)
            return WL_PRICE
        await self._ask_condition(update.message)
        return WL_CONDITION

    async def wl_skip_price(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.callback_query.answer()
        context.user_data["wl"]["price_min"] = None
        context.user_data["wl"]["price_max"] = None
        await self._ask_condition(update.callback_query.message)
        return WL_CONDITION

    async def _ask_condition(self, message: Any) -> None:
        rows = []
        for name, cid in CONDITIONS.items():
            rows.append([InlineKeyboardButton(f"⬜ {name}", callback_data=f"c:{cid}")])
        rows.append([InlineKeyboardButton("✔️ Done (any condition)", callback_data="cdone")])
        await message.reply_text(
            "✨ *Step 5/6 — Condition*\n\nSelect acceptable conditions (tap to toggle):",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(rows),
        )

    async def wl_condition_toggle(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.callback_query.answer()
        cid = int(update.callback_query.data.split(":")[1])
        selected: list[int] = context.user_data["wl"]["status_ids"]
        if cid in selected:
            selected.remove(cid)
        else:
            selected.append(cid)
        # Rebuild keyboard with ticks
        rev = {v: k for k, v in CONDITIONS.items()}
        rows = []
        for name, c in CONDITIONS.items():
            tick = "✅" if c in selected else "⬜"
            rows.append([InlineKeyboardButton(f"{tick} {name}", callback_data=f"c:{c}")])
        rows.append([InlineKeyboardButton("✔️ Done", callback_data="cdone")])
        await update.callback_query.edit_message_reply_markup(InlineKeyboardMarkup(rows))
        return WL_CONDITION

    async def wl_condition_done(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.callback_query.answer()
        await self._ask_category(update.callback_query.message)
        return WL_CATEGORY

    async def _ask_category(self, message: Any) -> None:
        rows = []
        for name, cid in CATALOG_IDS.items():
            rows.append([InlineKeyboardButton(f"⬜ {name}", callback_data=f"cat:{cid}")])
        rows.append([InlineKeyboardButton("✔️ Done (all categories)", callback_data="catdone")])
        await message.reply_text(
            "📁 *Step 6/6 — Category*\n\nSelect categories (optional):",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(rows),
        )

    async def wl_category_toggle(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.callback_query.answer()
        cid = int(update.callback_query.data.split(":")[1])
        selected: list[int] = context.user_data["wl"]["catalog_ids"]
        if cid in selected:
            selected.remove(cid)
        else:
            selected.append(cid)
        rev = {v: k for k, v in CATALOG_IDS.items()}
        rows = []
        for name, c in CATALOG_IDS.items():
            tick = "✅" if c in selected else "⬜"
            rows.append([InlineKeyboardButton(f"{tick} {name}", callback_data=f"cat:{c}")])
        rows.append([InlineKeyboardButton("✔️ Done", callback_data="catdone")])
        await update.callback_query.edit_message_reply_markup(InlineKeyboardMarkup(rows))
        return WL_CATEGORY

    async def wl_category_done(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.callback_query.answer()
        wld = context.user_data["wl"]
        # Build confirmation message
        brand_names = ", ".join(
            next((k for k, v in LUXURY_BRANDS.items() if v == bid), str(bid))
            for bid in wld.get("brand_ids", [])
        ) or "Any"
        lo = wld.get("price_min")
        hi = wld.get("price_max")
        price_str = (
            "Any" if lo is None and hi is None
            else f"€{lo or 0}–€{hi}" if hi else f"€{lo}+"
        )
        lines = [
            "📋 *Confirm Watchlist*\n",
            f"*Name:* {wld.get('name')}",
            f"*Brands:* {brand_names}",
            f"*Keywords:* {wld.get('search_text') or '—'}",
            f"*Price:* {price_str}",
            f"*Condition:* {_condition_label(wld.get('status_ids', []))}",
            f"*Category:* {_catalog_label(wld.get('catalog_ids', []))}",
        ]
        kb = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✅ Save", callback_data="wlsave"),
                    InlineKeyboardButton("❌ Cancel", callback_data="wlcancel"),
                ]
            ]
        )
        await update.callback_query.message.reply_text(
            "\n".join(lines), parse_mode=ParseMode.MARKDOWN, reply_markup=kb
        )
        return WL_CONFIRM

    async def wl_confirm_save(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.callback_query.answer("Saving…")
        wld = context.user_data["wl"]
        wl = Watchlist(
            name=wld.get("name", "Unnamed"),
            brand_ids=wld.get("brand_ids", []),
            search_text=wld.get("search_text", ""),
            price_min=wld.get("price_min"),
            price_max=wld.get("price_max"),
            catalog_ids=wld.get("catalog_ids", []),
            status_ids=wld.get("status_ids", []),
        )
        self.config.add_watchlist(wl)
        context.user_data.clear()
        await update.callback_query.message.reply_text(
            f"✅ Watchlist *{wl.name}* `[{wl.id}]` created!\n\n"
            "The sniper is now watching for new items. You'll get notified instantly.",
            parse_mode=ParseMode.MARKDOWN,
        )
        return ConversationHandler.END

    async def wl_confirm_cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        await update.callback_query.answer()
        context.user_data.clear()
        await update.callback_query.message.reply_text("❌ Watchlist creation cancelled.")
        return ConversationHandler.END

    # ── Inline button handler (watchlist list) ─────────────────────────────────

    async def cb_watchlist_action(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        q = update.callback_query
        await q.answer()
        parts = q.data.split(":")  # wl:action:id
        action = parts[1]
        wid = parts[2]

        if action == "toggle":
            result = self.config.toggle_watchlist(wid)
            if result is None:
                await q.message.reply_text("Watchlist not found.")
            else:
                state = "▶️ enabled" if result else "⏸ paused"
                await q.message.reply_text(
                    f"Watchlist `{wid}` is now *{state}*.", parse_mode=ParseMode.MARKDOWN
                )
        elif action == "remove":
            if self.config.remove_watchlist(wid):
                await q.message.reply_text(f"🗑 Watchlist `{wid}` removed.", parse_mode=ParseMode.MARKDOWN)
            else:
                await q.message.reply_text("Watchlist not found.")

    # ── Item notification ──────────────────────────────────────────────────────

    async def _send_item(self, chat_id: int, wl: Watchlist, item: dict[str, Any]) -> None:
        url = self._api.item_url(item)
        text, keyboard = build_notification(wl, item, url)
        photo_url = self._api.item_photo_url(item)

        try:
            if photo_url:
                await self.app.bot.send_photo(
                    chat_id=chat_id,
                    photo=photo_url,
                    caption=text,
                    parse_mode=ParseMode.MARKDOWN_V2,
                    reply_markup=keyboard,
                )
            else:
                await self.app.bot.send_message(
                    chat_id=chat_id,
                    text=text,
                    parse_mode=ParseMode.MARKDOWN_V2,
                    reply_markup=keyboard,
                    disable_web_page_preview=False,
                )
        except Exception as exc:
            logger.warning("send_photo failed (%s), trying text-only", exc)
            try:
                # Fallback: plain text without markdown
                plain = (
                    f"NEW ITEM — {wl.name}\n"
                    f"{item.get('title','?')}\n"
                    f"Price: {_price_str(item)}\n"
                    f"Brand: {item.get('brand_title','?')}\n"
                    f"Size: {item.get('size_title','?')}\n"
                    f"Condition: {_item_condition_label(item)}\n"
                    f"{url}"
                )
                await self.app.bot.send_message(chat_id=chat_id, text=plain, reply_markup=keyboard)
            except Exception as exc2:
                logger.error("Notification completely failed: %s", exc2)

    async def notify(self, wl: Watchlist, item: dict[str, Any]) -> None:
        """Called by the sniper when a new item is found."""
        if self.config.admin_chat_id is None:
            logger.warning("No admin chat ID set — cannot notify.")
            return
        await self._send_item(self.config.admin_chat_id, wl, item)

    # ── Run ────────────────────────────────────────────────────────────────────

    async def run(self) -> None:
        await self.app.initialize()
        await self.app.start()
        await self.app.updater.start_polling(drop_pending_updates=True)
        logger.info("Telegram bot started.")

    async def stop(self) -> None:
        await self.app.updater.stop()
        await self.app.stop()
        await self.app.shutdown()
