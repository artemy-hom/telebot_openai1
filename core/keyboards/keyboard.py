from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def get_keyboard():
    kb = [
        [KeyboardButton(text="/extend")],
        [KeyboardButton(text="/register")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
    return keyboard