from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters import CommandStart
from db.connection import create, read, update, delete
import asyncio
import openai




#--------
#Не забывай коментить идиотина
#А то потом опять забудешь зачем всё это делал 💀💀💀
#--------

#Bot & openai tockens
bot_tocken = "6354133817:AAE6nVek50btKjABewy1wmSz1-Q99bJOadU"
openai.api_key = "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"


bot = Bot(bot_tocken)
dp = Dispatcher(bot=bot)

#Openai is still doesn't want to work 
#So it seems like I need to get tocken again, but how?
'''@dp.message()
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
'''

#Using this function I tested how can I get the user ID
#NOTE ask the teacher how can i use this function


@dp.message(Command('start'))
async def send_create(message : types.Message):
    user_id = message.from_user.id
    username = message.from_user.first_name 
    create(user_id, username)
    await message.answer(f'Добавили вас в базу, {username}!')

@dp.message(Command('delete'))
async def send_delete(message : types.Message):
    user_id = message.from_user.id
    delete(user_id)
    await message.answer(f'Удаляем вас из базы.')


@dp.message(Command('read'))
async def send_delete(message : types.Message):
    user_id = message.from_user.id
    if user_id == 1691108875:
        await message.reply(str(read()))
    else:
        await message.reply(f'У вас не доступа.')     




async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
