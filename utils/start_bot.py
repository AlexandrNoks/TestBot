import logging
from datetime import datetime
from aiogram import Dispatcher
import calendar

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.config import GROUP_ID, ADMIN_ID,CHANNEL_ID
from loader import bot


name_weekday = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
date_now = calendar.weekday(int(datetime.today().strftime("%Y")), int(datetime.today().strftime("%m")),
                            int(datetime.today().strftime("%d")))

for i in range(len(name_weekday)):
    if i == date_now:
        res_date = name_weekday[i]


async def on_startup_notify(dp: Dispatcher):
    try:
        start_button_admin = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Перейти..", request_id=-1001978690583),
                    KeyboardButton(text="Отправить в чат", request_id=1400170440)
                ],
                [
                    KeyboardButton(text="Написать ученику в л/с"),
                    KeyboardButton(text="Создать опрос"),
                    KeyboardButton(text="Запросить контакт")
                ]
            ], resize_keyboard=True)
        start_chat_button = ReplyKeyboardMarkup(row_width=1, keyboard=[[KeyboardButton(text="Запустить",request_id=GROUP_ID)]],resize_keyboard=True)
        start_channel_button = ReplyKeyboardMarkup(row_width=1, keyboard=[[KeyboardButton(text="Запустить",request_id=CHANNEL_ID)]],resize_keyboard=True)
        await bot.send_message(ADMIN_ID,'Бот Запущен и готов к работе', reply_markup=start_button_admin)
        await bot.send_message(GROUP_ID,f"{datetime.today().strftime('%d.%m.%Y')}", reply_markup=start_chat_button)
        # await bot.send_message(CHANNEL_ID,f"{datetime.today().strftime('%d.%m.%Y')}", reply_markup=start_channel_button)
    except Exception as err:
        logging.exception(err)


