import logging
from datetime import datetime
from aiogram import Dispatcher
import calendar
from TestBot.keyboards.start_bot_btn import start_button_user,start_button_admin
from TestBot.data.config import GROUP_ID, ADMIN_ID
from TestBot.loader import bot


name_weekday = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
date_now = calendar.weekday(int(datetime.today().strftime("%Y")), int(datetime.today().strftime("%m")),
                            int(datetime.today().strftime("%d")))

for i in range(len(name_weekday)):
    if i == date_now:
        res_date = name_weekday[i]


async def on_startup_notify(dp: Dispatcher):
    try:
        await bot.send_message(ADMIN_ID,'Бот Запущен и готов к работе', reply_markup=start_button_admin)
        await bot.send_message(GROUP_ID,f"{datetime.today().strftime('%d.%m.%Y')}", reply_markup=start_button_user)
    except Exception as err:
        logging.exception(err)


