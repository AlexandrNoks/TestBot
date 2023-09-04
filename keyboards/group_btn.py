from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_button_user = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Написать педагогу"),
            KeyboardButton(text="Узнать рассписание"),
            KeyboardButton(text="Перейти...")
        ],
    ],
    resize_keyboard=True)