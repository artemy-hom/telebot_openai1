from aiogram import types
from aiogram.filters.command import Command
from keyboards.keyboard import get_keyboard
from main import dp, bot
from yoomoney import Client
from services.services import get_order, get_user, plus_month, make_order_paid
from config.config import get_config


config = get_config()




@dp.callback_query(lambda call: call.data == "check_payment")
async def check_payment(call: types.CallbackQuery):
    user = get_user(call.message.chat.id)
    order = get_order(user[0].id)
    if order.status == "PENDING":
        client = Client(config.ACCESS_TOKEN)
        history = client.operation_history(label=order.order_title)
        try:
            operation = history.operations[-1]
            if operation.status == "success":
                plus_month(user[0])
                make_order_paid(order)
                await call.message.answer("success")
        except:
            await call.message.answer("Чтобы проверить оплату нужно сначала оплатить")
    else:
        await call.message.answer('Уже оплачено')

