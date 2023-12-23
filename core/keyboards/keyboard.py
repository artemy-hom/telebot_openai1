from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def get_keyboard(access):
    if access == 1691108875:
                kb = [
            [KeyboardButton(text="/extend")],
            [KeyboardButton(text="/info")],
            [KeyboardButton(text="/read")],
            [KeyboardButton(text="/update")]
        ]
        

    else:
        kb = [
            [KeyboardButton(text="/extend")],
            [KeyboardButton(text="/info")]
        ]

    keyboard = ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
    return keyboard