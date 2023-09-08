from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

bot = Bot("6354133817:AAE6nVek50btKjABewy1wmSz1-Q99bJOadU")
dp = Dispatcher(bot=bot)

@dp.message(Command("start"))

async def start(message: types.Message):
    await message.answer(f'привет')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())