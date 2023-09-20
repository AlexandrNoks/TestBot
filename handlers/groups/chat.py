from aiogram.fsm.context import FSMContext
from aiogram import types, F, Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from filters.chat_type import ChatTypeFilter
from filters.chat_member import ChatMemberFilter
# from data.db_schedule import dict_schedule
from datetime import datetime

from keyboards.group_btn import start_button_user
from loader import dp, bot
from data.config import WORDS, GROUP_ID, ADMIN_ID, GROUP_URL, CHANNEL_URL, BOT_URL, CHANNEL_ID
from states.state_chat import UserStatus
from utils.misc.throttling import rate_limit
from middlewares.weekend import WeekendMessageMiddlewares
from middlewares.violation import ForbiddenWordls
from middlewares.activity_chat import ActivityChatMiddlewares


router = Router()
# router.message.filter(F.chat.type == "supergroup")
router.message.filter(ChatMemberFilter(chat_member=['supergroup','group']))
router.message.middleware(ForbiddenWordls())
router.message.middleware(WeekendMessageMiddlewares())
router.message.middleware(ActivityChatMiddlewares())
# message_date = datetime.today().strftime('%d.%m.%Y')
# message_time = datetime.today().strftime('%H:%M')
# my_time = datetime.hour

@router.message(F.text =='Запустить')
async def start_chat_user(message: types.Message):
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

@dp.message(ChatTypeFilter(chat_type=['private', 'supergroup']), F.photo)
async def photo_group(message: types.Message):
    file_ids = []
    photo_chat = bot.set_chat_photo()
    file_ids.append(photo_chat.photo[-1].file_id)
    await bot.send_photo(chat_id=GROUP_ID,photo=file_ids[-1])
    await bot.send_photo(chat_id=CHANNEL_ID,photo=file_ids[-1])


# Пользователь вышел сам
@router.message(UserStatus.user_left)
async def left_user(message: types.Message, state: FSMContext):
    user_answer = message.from_user.first_name
    data = await state.update_data(user_left=user_answer)
    await message.reply(f"{message.left_chat_member.get_mention(as_html=True)}, {data['user_left']} Покинул чат!")
    await state.set_state(UserStatus.user_left.state)


