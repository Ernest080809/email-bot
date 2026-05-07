#!/usr/bin/env python3
"""Entry point: runs the Telegram bot and Vinted sniper concurrently."""

from __future__ import annotations

import asyncio
import logging
import os
import signal
import sys

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def _require(var: str) -> str:
    value = os.getenv(var)
    if not value:
        sys.exit(f"ERROR: {var} is not set. Check your .env file.")
    return value


async def main() -> None:
    token = _require("TELEGRAM_BOT_TOKEN")
    country = os.getenv("VINTED_COUNTRY", "fr")
    poll_interval = int(os.getenv("POLL_INTERVAL", "30"))

    from watchlist_config import Config
    from sniper import VintedSniper
    from telegram_bot import SniperBot

    config = Config.load()

    # Apply env-level overrides (don't override persistent user choices)
    if config.country == "fr" and country != "fr":
        config.country = country
    if config.poll_interval == 30 and poll_interval != 30:
        config.poll_interval = poll_interval

    bot = SniperBot(token=token, config=config)
    sniper = VintedSniper(config=config, notify=bot.notify)

    # Graceful shutdown
    loop = asyncio.get_running_loop()
    stop_event = asyncio.Event()

    def _shutdown(*_: object) -> None:
        logger.info("Shutdown signal received.")
        stop_event.set()

    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, _shutdown)

    logger.info("Starting Vinted Designer Sniper…")

    await bot.run()
    sniper_task = sniper.start()

    logger.info("Bot and sniper running. Press Ctrl+C to stop.")

    await stop_event.wait()

    logger.info("Stopping…")
    sniper.stop()
    sniper_task.cancel()
    await bot.stop()
    logger.info("Goodbye.")


if __name__ == "__main__":
    asyncio.run(main())
