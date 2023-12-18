from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_p2p_keyboard(url: str) -> InlineKeyboardMarkup:
    p2p_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text = "Оплатить",url=url),
             InlineKeyboardButton(text = "Проверить оплату", callback_data="check_payment")]
        ]
    )
    '''
    pay_btn = InlineKeyboardButton(text = "Оплатить",url=url)
    check_payment = InlineKeyboardButton(text = "Проверить оплату", callback_data="check_payment")

    p2p_keyboard.add(pay_btn)
    p2p_keyboard.add(check_payment)
    '''
    return p2p_keyboard