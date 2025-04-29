import asyncio
import logging
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import get_envs
from aiogram import Bot
from handlers import register_all_handlers
dp = Dispatcher()
env = get_envs()
TOKEN = env.token

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    register_all_handlers(dp)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    asyncio.run(main())
