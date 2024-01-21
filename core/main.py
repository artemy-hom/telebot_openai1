import asyncio

import openai
from aiogram import Bot, Dispatcher
from tockens import openai_tocken


# Bot & openai tockens
bot_tocken = "6354133817:AAE6nVek50btKjABewy1wmSz1-Q99bJOadU"
openai.api_key = openai_tocken


bot = Bot(bot_tocken)
dp = Dispatcher(bot=bot)


async def main():
    from handlers import dp
    from handlers.handlers import router
    dp.include_router(router)
    await dp.start_polling(bot)





if __name__ == "__main__":
    asyncio.run(main())