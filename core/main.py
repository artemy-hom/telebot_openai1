from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio
import openai

bot_tocken = "6354133817:AAE6nVek50btKjABewy1wmSz1-Q99bJOadU"
openai.api_key = "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"

bot = Bot(bot_tocken)
dp = Dispatcher(bot=bot)

@dp.message()
async def send(message : types.Message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
)

    await message.answer(response['choices'][0]['text'])


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
