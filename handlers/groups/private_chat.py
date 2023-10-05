from datetime import datetime
from aiogram import types, F,Router
from filters.chat_type import ChatTypeFilter
from filters.chat_member import ChatMemberFilter
from middlewares.violation import ForbiddenWordsMiddleware
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardRemove
from aiogram.utils.markdown import hide_link
from loader import dp,bot
from data.config import ADMIN_ID, time_bun_sec, users_log, GROUP_ID, WORDS, GROUP_URL,CHANNEL_ID
from middlewares.weekend import WeekendMessageMiddleware
from states import GetContact,UserStatus, MailingChat, Registered
from keyboards.mailing_btn import mailing_btn
from keyboards.start_bot_btn import to_ask_bot
# from utils.db_api import quick_commands as commands
from utils.misc.throttling import rate_limit
router = Router()
router.message.filter(ChatTypeFilter(chat_type='supergroup'))



@router.message(ChatMemberFilter(chat_member='restricted'))
async def user_kick_chat(message: types.Message):
    await bot.send_message(message.from_user.id,f" Вы были удалены из чата.")


@router.message(ChatMemberFilter(chat_member='restricted'))
async def user_left_chat(message: types.Message):
    # user_name = types.User.get_current(no_error=True)
    await bot.send_message(message.from_user.id,f"Вы вышли из чата")


@router.message(ChatMemberFilter(chat_member='banned'))
async def banned_user(message: types.Message):
    user_name = bot.get_current(no_error=True)
    if datetime.now().time() < (datetime.now() + time_bun_sec).time():
        await message.answer(f"{user_name['first_name']} Время бана не закончилось! {datetime.now().time()} {(datetime.now() + time_bun_sec).time()}\nДождитесь завершения бана!")
    else:
        await message.answer(f"Hello! {message.from_user.first_name} Поздравляю ты разбанен! Заходи https://t.me/+xxep96iuXxk3ZDky")
# Пользователь разбанен
# @dp.callback_query(F.data == "uban")
# async def call_kick_user_chat(call: types.CallbackQuery):
#     if data in choose_user:
#         await bot.uban_chat_member(chat_id=GROUP_ID,user_id=choose_user[data],revoke_messages=True)
#     await call.message.answer(f"{data} Поздравляю, ты разбанин")
#     await UserStatus.user_unban.state



