from datetime import datetime
from aiogram import types, F
from filters.chat_type import ChatTypeFilter
from filters.chat_member import ChatMemberFilter
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardRemove
from aiogram.utils.markdown import hide_link

from loader import dp,bot
from data.config import ADMIN_ID, time_bun_sec, users_log, GROUP_ID, WORDS, GROUP_URL,CHANNEL_ID
from states import GetContact,UserStatus, MailingChat, Registered
from keyboards.mailing_btn import mailing_btn
from keyboards.private_btn import to_ask_bot
from utils.db_api import quick_commands as commands
from utils.misc.throttling import rate_limit


@rate_limit(limit=10, key="Написать педагогу")
@dp.message(ChatTypeFilter(chat_type=['private']),ChatMemberFilter(chat_member=['member']),F.text == "Написать педагогу")
async def mailing_chat(message: types.Message):
    user_answer = message.text
    await bot.send_message(ADMIN_ID,f"{user_answer}")

@rate_limit(limit=10, key="Узнать расписание")
@dp.message(ChatTypeFilter(chat_type=['private']),ChatMemberFilter(chat_member=['member']),F.text == "Узнать расписание")
async def schenali_chat(message: types.Message):
    await bot.send_message(message.from_user.id,f"Расписание на сегодня мне",message_thread_id=message.from_user.id)
#

@dp.message(ChatMemberFilter(chat_member=['left','restricted']))
async def user_kick_chat(message: types.Message):
    # user_name = types.User.get_current(no_error=True)
    await bot.send_message(message.from_user.id,f" Вы были удалены из чата.")

@dp.message(ChatMemberFilter(chat_member=['left','restricted']),ChatTypeFilter(chat_type=['private']))
async def user_left_chat(message: types.Message):
    user_name = types.User.get_current(no_error=True)
    await bot.send_message(message.from_user.id,f"Здравствуйте,Вы вышли из чата")

@dp.message(ChatMemberFilter(chat_member=['banned']),ChatTypeFilter(chat_type=['private']))
async def banned_user(message: types.Message):
    user_name = bot.get_current(no_error=True)
    if datetime.now().time() < (datetime.now() + time_bun_sec).time():
        await message.answer(f"{user_name['first_name']} Время бана не закончилось! {datetime.now().time()} {(datetime.now() + time_bun_sec).time()}\nДождитесь завершения бана!")
    else:
        await message.answer(f"Hello! {message.from_user.first_name} Поздравляю ты разбанен! Заходи https://t.me/+xxep96iuXxk3ZDky")
# Пользователь разбанен
@dp.callback_query(F.data == "uban")
async def call_kick_user_chat(call: types.CallbackQuery):
    if data in choose_user:
        await bot.uban_chat_member(chat_id=GROUP_ID,user_id=choose_user[data],revoke_messages=True)
    await call.message.answer(f"{data} Поздравляю, ты разбанин")
    await UserStatus.user_unban.state


# @dp.message(ChatTypeFilter(chat_type=['private']))
# async def message_user(message: types.Message):
#     for word in WORDS:
#         if message.text in word:
#             await bot.delete_message(message.chat.id, message.message_id)


