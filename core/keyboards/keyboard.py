from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def get_keyboard():
    kb = [
        [KeyboardButton(text="/register")],
        [KeyboardButton(text="/info")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
    return keyboard