from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_button_channel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Разместить пост", request_id=1400170440),
            KeyboardButton(text="Фото"),
            KeyboardButton(text="Видео"),
            KeyboardButton(text="Перейти"),
        ],
    ],
    resize_keyboard=True)