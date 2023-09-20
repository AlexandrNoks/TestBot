from aiogram import types,F
from aiogram.fsm.context import FSMContext
from datetime import datetime
from filters import *
from data.config import GROUP_ID, ADMIN_ID
from keyboards.start_bot_btn import start_button_admin
from loader import dp, bot
from states import Schedule


#Расписание
@dp.message(ChatTypeFilter(chat_type=['supergroup','group']), F.text == "Рассписание")
async def mailing_text(message: types.Message, state: FSMContext):
    await message.reply(f"Рассписание на сегодня {datetime.today().strftime('%d.%m.%Y')}\n")


