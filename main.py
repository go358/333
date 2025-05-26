
import asyncio
import logging
import importlib
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from bot.config import BOT_TOKEN

dp = Dispatcher(storage=MemoryStorage())

modules = ["booking", "feedback", "chat", "admin_menu", "master_menu"]
for name in modules:
    mod = importlib.import_module(f"bot.handlers.{name}")
    dp.include_router(mod.router)

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
