from aiogram.fsm.context import FSMContext
from aiogram import types, F, Router
from aiogram.filters import Command

from TestBot.keyboards.start_bot_btn import start_button_admin
from TestBot.utils.db_api.db_messages import active
import asyncio
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton,ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from TestBot.utils.db_api import quick_commands as commands
from TestBot.filters.chat_type import ChatTypeFilter
from TestBot.filters.chat_member import ChatMemberFilter
from datetime import datetime
from TestBot.loader import dp, bot
from TestBot.data import config
from TestBot.data.config import ADMIN_ID, CHANNEL_URL, BOT_URL, ADMIN_URL
from TestBot.states.state_chat import GetContact
from TestBot.utils.misc.throttling import rate_limit
from TestBot.middlewares.weekend import WeekendMessageMiddleware
from TestBot.middlewares.violation import ForbiddenWordsMiddleware
router = Router()
router.message.filter(ChatTypeFilter(chat_type='supergroup'))
router.message.filter(ChatMemberFilter(chat_member='member'))
router.message.middleware(ForbiddenWordsMiddleware())
router.message.middleware(WeekendMessageMiddleware())
# message_date = datetime.today().strftime('%d.%m.%Y')
# message_time = datetime.today().strftime('%H:%M')
# my_time = datetime.hour


@rate_limit(limit=10, key="Написать педагогу")
@router.message(F.text == "Написать педагогу")
async def mailing_chat(message: types.Message, state: FSMContext):
    await message.answer("Напишите текст сообщение или нажмите Перейти  в чат с педагогом")
    await state.set_state(GetContact.user_text.state)


@router.message(GetContact.user_text)
async def correspondent_for_to_admin(message: types.Message, state: FSMContext):
    correspondent_with_admin = InlineKeyboardBuilder()
    correspondent_with_admin.add(InlineKeyboardButton(text="Перейти в чата с педагог",url=ADMIN_URL))
    await state.update_data(user_text=message.text)
    data = await state.get_data()
    user_text = data.get("user_text")
    await bot.send_message(ADMIN_ID,f"Сообщение от пользователя\n{user_text}")
    await message.answer(f"Ваше сообщение отправлено педагогу если хотите в личную переписку нажмите Перейти",reply_markup=correspondent_with_admin.as_markup())
    await state.clear()


@rate_limit(limit=10, key="Узнать расписание")
@router.message(F.text == "Узнать расписание")
async def schedule_chat(message: types.Message):
    await bot.send_message(message.from_user.id,f"Расписание на сегодня")


@rate_limit(limit=10, key="Перейти...")
@router.message(F.text == "Перейти...")
async def cross_link_button(message: types.Message):
    urls_button = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Канал", url=CHANNEL_URL),
        InlineKeyboardButton(text="Написать боту",url=BOT_URL)
    ]])
    await message.answer("Перейти",reply_markup=urls_button)


@router.message(Command('active'))
async def get_message(message: types.Message):
    await active.set_bind(config.POSTGRES_URL)
    await active.gino.create_all()

@router.message(F.text)
async def violation_chat(message: types.Message):
    not_answer = message.reply_to_message
    who_you = message.from_user.is_bot
    if who_you == False and not_answer == None:
        await commands.add_message(message_id=message.message_id,user_id=message.from_user.id)
    if message.text == "stop":
        data = await commands.select_all_message()
        await bot.send_message(ADMIN_ID,f"Всего зарегистировано {str(len(data)-1)} сообщений")
        await active.gino.drop_all()














