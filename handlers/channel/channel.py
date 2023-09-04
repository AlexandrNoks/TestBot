from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram import types
from loader import dp,bot
from data.config import CHANNEL_URL


@dp.callback_query_handler(text_contains="EnterChannel")
async def mailing_chat(call: types.CallbackQuery):
    mailing_channel = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Отправить фото"),
                KeyboardButton(text="Отправить Видео"),
                KeyboardButton(text="Отправить пост")
            ]
        ], resize_keyboard=True)

    await call.message.answer(f"Канал",reply_markup=mailing_channel)