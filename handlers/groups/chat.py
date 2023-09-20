from aiogram.fsm.context import FSMContext
from aiogram import types, F, Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from filters.chat_type import ChatTypeFilter
from filters.filter_group import ActivityChat
# from data.db_schedule import dict_schedule
from datetime import datetime

from keyboards.group_btn import start_button_user
from loader import dp, bot
from data.config import WORDS, GROUP_ID, ADMIN_ID, GROUP_URL, CHANNEL_URL,BOT_URL
from states.state_chat import UserStatus
from utils.misc.throttling import rate_limit
from middlewares.weekend import WeekendMessageMiddlewares
from middlewares.violation import ForbiddenWordls


router = Router()
# router.message.filter(F.chat.type == "supergroup")
router.message.filter(ActivityChat(chat_type="supergroup"))
router.message.middleware(ForbiddenWordls())
# message_date = datetime.today().strftime('%d.%m.%Y')
# message_time = datetime.today().strftime('%H:%M')
# my_time = datetime.hour

@router.message(F.text)
async def start_chat_user(message: types.Message):
    schedule_day = ""
    await message.answer(f"Рассписание только на завтра {datetime.today().strftime('%d.%m.%Y')}",  reply_markup=start_button_user)


@rate_limit(limit=10, key="Написать педагогу")
@router.message(F.text == "Написать педагогу")
async def mailing_chat(message: types.Message):
    user_answer = message.text
    await bot.send_message(ADMIN_ID,f"{user_answer}")


@rate_limit(limit=10, key="Узнать расписание")
@router.message(F.text == "Узнать расписание")
async def schenali_chat(message: types.Message):
    await bot.send_message(GROUP_ID,f"Расписание на сегодня",message_thread_id=message.from_user.id)


@rate_limit(limit=10, key="Перейти...")
@router.message(F.text == "Перейти...")
async def cross_link_button(message: types.Message):
    urls_button = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Группа", callback_data="UrlGroup", url=GROUP_URL),
        InlineKeyboardButton(text="Канал", callback_data="UrlChannel", url=CHANNEL_URL),
        InlineKeyboardButton(text="Чат с ботом",callback_data="UrlBot", url=BOT_URL)
    ]])
    await message.answer("Перейти",reply_markup=urls_button)


@router.message(F.text)
async def chat_echo(message: types.Message):
    text_user = message.text
    for word in WORDS:
        if text_user == word:
            await bot.delete_message(message.chat.id,message.message_id)
    if text_user == "Запустить":
        if datetime.now().hour < 17:
            await message.answer(f"Добрый день! {message.from_user.first_name}")
        else:
            await message.answer("Добрый вечер!")


# Пользователь вышел сам
@router.message(UserStatus.user_left)
async def left_user(message: types.Message, state: FSMContext):
    user_answer = message.from_user.first_name
    data = await state.update_data(user_left=user_answer)
    await message.reply(f"{message.left_chat_member.get_mention(as_html=True)}, {data['user_left']} Покинул чат!")
    await state.set_state(UserStatus.user_left.state)


