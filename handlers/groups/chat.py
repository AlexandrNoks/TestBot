from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import ChatTypeFilter,CommandStart
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# from data.db_schedule import dict_schedule
from filters import IsUserGroup
from datetime import datetime

from keyboards.group_btn import start_button_user
from loader import dp, bot
from data.config import WORDS, GROUP_ID, ADMIN_ID, GROUP_URL, CHANNEL_URL,BOT_URL
from states.state_chat import UserStatus
from utils.misc.throttling import rate_limit


# message_date = datetime.datetime.today().strftime('%d.%m.%Y')
# message_time = datetime.datetime.today().strftime('%H:%M')

# @dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.SUPERGROUP),text="Запустить")
# async def start_chat_user(message: types.Message):
#     schedule_day = ""
#     await message.answer(f"Рассписание на {datetime.today().strftime('%d.%m.%Y')}",  reply_markup=start_button_user)
#     for schedule in dict_schedule:
#         # print(f"{schedule} {dict_schedule[schedule]}
#         schedule_day += f"{schedule} {dict_schedule[schedule]}\n"
#     await message.answer(f"{schedule_day}",  reply_markup=start_button_user)


@rate_limit(limit=10, key="Написать педагогу")
@dp.message_handler(IsUserGroup(),ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP]),text="Написать педагогу")
async def mailing_chat(message: types.Message):
    user_answer = message.text
    await bot.send_message(ADMIN_ID,f"{user_answer}")


@rate_limit(limit=10, key="Узнать расписание")
@dp.message_handler(IsUserGroup(),ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP]),text="Узнать расписание")
async def schenali_chat(message: types.Message):
    await bot.send_message(GROUP_ID,f"Расписание на сегодня",message_thread_id=message.from_user.id)


@rate_limit(limit=10, key="Перейти...")
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.SUPERGROUP),text="Перейти...")
async def cross_link_button(message: types.Message):
    urls_button = InlineKeyboardMarkup()
    url_group = InlineKeyboardButton(text="Группа", callback_data="UrlGroup", url=GROUP_URL)
    url_channel = InlineKeyboardButton(text="Канал", callback_data="UrlChannel", url=CHANNEL_URL)
    url_bot = InlineKeyboardButton(text="Чат с ботом",callback_data="UrlBot", url=BOT_URL)
    urls_button.row(url_group,url_channel,url_bot)
    await message.answer("Перейти",reply_markup=urls_button)


@dp.message_handler(ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP]))
async def chat_echo(messege: types.Message):
    text_user = messege.text
    for word in WORDS:
        if text_user == word:
            await bot.delete_message(messege.chat.id,messege.message_id)


# Пользователь вышел сам
@dp.message_handler(ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP,types.ChatType.GROUP]),state=UserStatus.user_left)
async def left_user(messege: types.Message, state: FSMContext):
    user_answer = messege.text
    async with state.proxy() as data:
        data["user_left"] = user_answer
    await messege.reply(f"{messege.left_chat_member.get_mention(as_html=True)}, {messege.from_user.first_name} Покинул чат!")
    await UserStatus.user_kick.set()


