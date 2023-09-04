from aiogram import types
from aiogram.dispatcher import FSMContext
from datetime import datetime
from filters import *
from data.config import GROUP_ID, ADMIN_ID
from keyboards.start_bot_btn import start_button_admin
from loader import dp, bot
from states import Schedule


#Расписание
# @dp.message_handler(IsAdminGroup(),text="Рассписание", state=Schedule)
# async def mailing_text(message: types.Message, state: FSMContext):
    # await state.update_data(text=text_answer)
    # await MailingText.text.set()
    # data = await state.get_data()
    # text_answer = data.get("text_mailing")
    # await message.reply(f"Рассписание на сегодня {datetime.today().strftime('%d.%m.%Y')}\n")

@dp.callback_query_handler(text_contains="mailing")
async def to_share(call: types.CallbackQuery):
    if call.data == "mailingSchedule":
        await bot.send_message(GROUP_ID, f"Рассписание на сегодня {datetime.today().strftime('%d.%m.%Y')}\n")
    elif call.data == "mailingExit":
        await bot.send_message(ADMIN_ID,"Готов к работе", reply_markup=start_button_admin)

