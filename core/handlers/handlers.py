import openai
import string
import random
import datetime
import replace
from aiogram import types, Router, F
from aiogram.filters.command import Command
from main import dp, bot
from services.services import create, delete, read, id_finder, get_all_user_id
from keyboards.keyboard import get_keyboard
from keyboards.inline_kb import get_p2p_keyboard
from services.services import get_user, get_order, create_payment, create_order


router  = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    try:
        user_id = message.from_user.id
        username = message.from_user.first_name
        create(user_id, username)
        await message.answer(f"Здравствуйте, {username}!\nЭтот бот умеет отвечать на любые ваши вопросы с помощью нейросетки.\nТакже у вас есть пробный период до 00:00 завтрашнего дня.\nДля получение листа команд воспользуйтесь коммандой\n/commands")
    except:
        await message.answer(f"Здравствуйте, {username}!\nЭтот бот умеет отвечать на любые ваши вопросы с помощью нейросетки.\nТакже у вас есть пробный период до 00:00 завтрашнего дня.\nдля получение листа команд воспользуйтесь коммандой\n/commands")



@router.message(Command("update"))
async def start(message: types.Message):
    access = message.from_user.id
    if access == 1691108875:
        try:
            message_text = message.text
            text_for_update = replace.replace(message_text, {"/update": "Update!\n"})
            text_for_update = text_for_update.replace(" ","",1)

            all_user_id = get_all_user_id()

            for user_id in all_user_id:
                await bot.send_message(chat_id=user_id[0],text=text_for_update)


        except Exception as ex:
            print(ex)
            await message.answer("err")
    else:
        await message.answer("У вас нет доступа.")


@router.message(Command("commands"))
async def start(message: types.Message):
    try:
        access = message.from_user.id
        await message.answer("Вот!",reply_markup=get_keyboard(access=access))
    except:
        print('err')


@router.message(Command("info"))
async def send_create(message: types.Message):

    await message.answer("Этот бот отвечает на любые ваши вопросы, но для его использования необходимо оформить подписку.\nСоздать заказ можно коммандой\n/extend")


'''@router.message(Command("register"))
async def send_create(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.first_name
    create(user_id, username)
    await message.answer(f"Добавили вас в базу, {username}!")'''

@router.message(Command("read"))
async def send_read(message: types.Message):
    user_id = message.from_user.id
    if user_id == 1691108875:
        await message.reply(str(read()))
    else:
        await message.reply("У вас не доступа.")

@router.message(Command("subscribe"))
async def p2p_handler(message: types.Message):
    user = get_user(message.chat.id)
    order = get_order(user[0].id)
    if order and order.status != "PAID":
        await message.answer("Заказ уже создан")
    else:
        letters_and_digits = string.ascii_lowercase + string.digits
        rand_string = "".join(random.sample(letters_and_digits,10))
        quickpay =create_payment(rand_string)
        print(quickpay)
        create_order(rand_string, user[0].id)
        p2p_keyboard = get_p2p_keyboard(quickpay.redirected_url)
        await message.answer(
            text= 'Преобрести подписку можно по кнопке ниже.',
            reply_markup= p2p_keyboard,
        )





@router.message()
async def send(message : types.Message):
    user_date = get_user(message.chat.id)
    now = datetime.date.today()
    if (user_date == None) or (now > user_date[0].up_date):
        await message.answer('Купите подписку')
        return
    elif user_date != None:
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