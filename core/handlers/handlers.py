import openai
from aiogram import types, Router, F
from aiogram.filters.command import Command
from main import dp
from services.services import create, delete, read, id_finder
from keyboards.keyboard import get_keyboard


router  = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    username = message.from_user.first_name
    await message.answer(f"Здравствуйте, {username}!\nЭтот бот умеет отвечать на любые ваши вопросы с помощью нейросетки\nдля получение листа команд воспользуйтесь коммандой\n/commands")


@router.message(Command("commands"))
async def start(message: types.Message):
    await message.answer("Вот!",reply_markup=get_keyboard())


@router.message(Command("info"))
async def send_create(message: types.Message):

    await message.answer("Для использования этого бота, необходимо зарегестрироваться командой /register")


@router.message(Command("register"))
async def send_create(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.first_name
    create(user_id, username)
    await message.answer(f"Добавили вас в базу, {username}!")


@router.message(Command("delete"))
async def send_delete(message: types.Message):
    user_id = message.from_user.id
    delete(user_id)
    await message.answer("Удаляем вас из базы.")


@router.message(Command("read"))
async def send_read(message: types.Message):
    user_id = message.from_user.id
    if user_id == 1691108875:
        await message.reply(str(read()))
    else:
        await message.reply("У вас не доступа.")

@router.message()
async def send(message : types.Message):
    command_list = ["/start",
                    "/register",
                    "/info",
                    "/commands",
                    "/read",
                    "/delete"
                    ]
    

    an_user_id = message.from_user.id
    id_finder(an_user_id = an_user_id)

    try:
        index_commands = command_list.index(message.text)
    except:
        if id_finder(an_user_id) != None:
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
        else:
            await message.answer("Зарегестрируйтесь командой\n/register")


# Using this function I tested how can I get the user ID
# NOTE ask the teacher how can i use this function