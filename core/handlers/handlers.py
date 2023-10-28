from aiogram import types
from aiogram.filters.command import Command
from main import dp
from services.services import create, delete, read

"""@dp.message()
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
"""

# Using this function I tested how can I get the user ID
# NOTE ask the teacher how can i use this function


@dp.message(Command("start"))
async def send_create(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.first_name
    create(user_id, username)
    await message.answer(f"Добавили вас в базу, {username}!")


@dp.message(Command("delete"))
async def send_delete(message: types.Message):
    user_id = message.from_user.id
    delete(user_id)
    await message.answer("Удаляем вас из базы.")


@dp.message(Command("read"))
async def send_read(message: types.Message):
    user_id = message.from_user.id
    if user_id == 1691108875:
        await message.reply(str(read()))
    else:
        await message.reply("У вас не доступа.")
