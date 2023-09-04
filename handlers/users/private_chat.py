from datetime import datetime
from aiogram import types
from aiogram.dispatcher.filters import Command, CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardRemove
from aiogram.utils.markdown import hide_link
from filters import IsPrivateChat,IsUserLeftChat,IsNewUser,IsUserGroup,IsUserBanned
from aiogram.dispatcher.filters import ChatTypeFilter

from loader import dp,bot
from data.config import ADMIN_ID, time_bun_sec, users_log, GROUP_ID, WORDS, GROUP_URL,CHANNEL_ID
from states import GetContact,UserStatus, MailingChat, Registered
from keyboards.mailing_btn import mailing_btn
from keyboards.private_btn import to_ask_bot
from utils.db_api import quick_commands as commands
from utils.misc.throttling import rate_limit


@rate_limit(limit=10, key="Написать педагогу")
@dp.message_handler(IsUserGroup(),ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP]),text="Написать педагогу")
async def mailing_chat(message: types.Message):
    user_answer = message.text
    await bot.send_message(ADMIN_ID,f"{user_answer}")

@rate_limit(limit=10, key="Узнать расписание")
@dp.message_handler(IsUserGroup(),ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP]),text="Узнать расписание")
async def schenali_chat(message: types.Message):
    await bot.send_message(GROUP_ID,f"Расписание на сегодня",message_thread_id=message.from_user.id)


@dp.message_handler(IsUserLeftChat(),ChatTypeFilter(chat_type=types.ChatMemberStatus.LEFT))
async def user_kick_chat(message: types.Message):
    user_name = types.User.get_current(no_error=True)
    await bot.send_message(message.from_user.id,f"{user_name['first_name']} Вы были удалены из чата.")

@dp.message_handler(IsUserLeftChat(),ChatTypeFilter(chat_type=types.ChatMemberStatus.LEFT))
async def user_left_chat(message: types.Message):
    user_name = types.User.get_current(no_error=True)
    await bot.send_message(message.from_user.id,f"Здравствуйте,Вы вышли из чата")

@dp.message_handler(IsUserBanned(),ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP]))
async def banned_user(message: types.Message):
    user_name = bot.get_current(no_error=True)
    if datetime.now().time() < (datetime.now() + time_bun_sec).time():
        await message.answer(f"{user_name['first_name']} Время бана не закончилось! {datetime.now().time()} {(datetime.now() + time_bun_sec).time()}\nДождитесь завершения бана!")
    else:
        await message.answer(f"Hello! {message.from_user.first_name} Поздравляю ты разбанен! Заходи https://t.me/+xxep96iuXxk3ZDky")
# Пользователь разбанен
@dp.callback_query_handler(text_contains="uban")
async def call_kick_user_chat(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if data in choose_user:
            await bot.uban_chat_member(chat_id=GROUP_ID,user_id=choose_user[data],revoke_messages=True)
        await call.message.answer(f"{data} Поздравляю, ты разбанин")
        await UserStatus.user_unban.set()
# Получить фото и переслать в канал
@dp.message_handler(ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP]),content_types=types.ContentTypes.PHOTO)
async def send_photo(message: types.Message):
    await message.photo[-1].download(destination_dir="media/")
    # await dp.bot.send_photo(chat_id=6567576,photo=InputFile())



@dp.message_handler(IsPrivateChat(),ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def message_user(message: types.Message):
    for word in WORDS:
        if message.text in word:
            await bot.delete_message(message.chat.id, message.message_id)


