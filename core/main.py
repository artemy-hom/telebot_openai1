import asyncio

import openai
from aiogram import Bot, Dispatcher

# --------
# Не забывай коментить идиотина
# А то потом опять забудешь зачем всё это делал 💀💀💀
# --------

# Bot & openai tockens
bot_tocken = "6354133817:AAE6nVek50btKjABewy1wmSz1-Q99bJOadU"
openai.api_key = "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"


bot = Bot(bot_tocken)
dp = Dispatcher(bot=bot)


async def main():
    from handlers import dp

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
