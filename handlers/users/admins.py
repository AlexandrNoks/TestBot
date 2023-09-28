from datetime import datetime
from aiogram import Router, F
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from data.db_schedule import dict_schedule
from data.poll_db import name_concert

from loader import dp,bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from keyboards.start_bot_btn import start_button_admin
from keyboards.mailing_btn import mailing_btn
from filters.chat_member import ChatMemberFilter
from data.config import *
from states import GetContact, UserStatus
# from utils.db_api import poll_commands as commands
from utils.db_api import quick_commands as commands
from middlewares.violation import ForbiddenWordsMiddleware


router = Router()
router.message.middleware(ForbiddenWordsMiddleware())
router.message.filter(ChatMemberFilter(chat_member="creator"))
name_contest = ""
# @router.message(F.text)
# async def mailing_chat(message: types.Message):
#     user_x = message.from_user.is_bot
#     message_x = message.reply_to_message
#     await message.answer(f"{message_x} ответ пользователю {user_x}")


@router.message(F.text == "Отправить в чат")
async def send_chat(message: types.Message):
    await bot.send_message(message.chat.id,f"Выберете посылку", reply_markup=mailing_btn)


@router.callback_query(F.data.startswith("mailing"))
async def mailing_chat(call: types.CallbackQuery):
    if call.data == "mailingSchedule":
        await bot.pin_chat_message(GROUP_ID,message_id=call.message.message_id)
        await bot.send_message(GROUP_ID, f"Рассписание на сегодня {datetime.today().strftime('%d.%m.%Y')}\n")
    if call.data == "mailingChannel":
        link_channel = InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(text="Ссылка на канал", callback_data="EnterChannel",url=CHANNEL_URL)]])
        await bot.send_message(GROUP_ID,f"Пригласить на канал:",reply_markup=link_channel)
    elif call.data == "mailingExit":
        await call.bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)


@router.message(F.text == "Перейти..")
async def go_to_group(message: types.Message):
    urls_button = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="Группа", url=GROUP_URL),
            InlineKeyboardButton(text="Канал", url=CHANNEL_URL),
            InlineKeyboardButton(text="Чат с ботом", url=BOT_URL)
        ]]
    )
    await message.answer("Перейти",reply_markup=urls_button)


@router.message(F.text == "Написать ученику в л/с")
async def message_user(message: types.Message):
    for user in users_log:
        message_choice = InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(text=f"@{user}", url='https://t.me/+xxep96iuXxk3ZDky')
            ]])
        await message.answer("Выбрать",reply_markup=message_choice)


# Команда начать опрос
@router.message(F.text == "Создать опрос")
async def start_poll(message: types.Message):
    choice_concert = InlineKeyboardBuilder()
    for concert in name_concert:
        choice_concert.add(InlineKeyboardButton(text=f"{concert} дата {'д.м.г.'}", callback_data=f"Poll{concert}"))
    await message.answer("Выбрать", reply_markup=choice_concert.as_markup())
    close_poll = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Закрыть опрос",callback_data="PollClose")]])
    await bot.send_message(ADMIN_ID,"Закрыть опрос", reply_markup=close_poll)


# Опрос
@router.callback_query(F.data.startswith("Poll"))
async def get_name_contest(call: types.CallbackQuery):
    for concert in name_concert:
        if call.data == f"Poll{concert}":
            await call.bot.send_poll(GROUP_ID,question=f"Опрос, Дата Состоится {concert}\n Выберите 'Да' если принимаете участие или 'Нет' если не будите участвовать",correct_option_id=1,
                                     options=["Да","Нет"], type="quiz", is_closed=False, is_anonymous=False, reply_markup=ReplyKeyboardRemove())
    if call.data == "PollClose":
        await bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
        # await bot.send_message(ADMIN_ID,"Готов к работе", reply_markup=start_button_admin)


# Голоса
@router.poll_answer()
async def date_answer(poll: types.PollAnswer):
    user_id = poll.user.id
    user_name = poll.user.first_name
    user_answer = poll.option_ids
    for i in user_answer:
        if i == 0:
            i = "Да"
            await commands.add_answer(user_id=user_id,user_name=user_name,user_answer=i)
        elif i == 1:
            i = "Нет"
            await commands.add_answer(user_id=user_id,user_name=user_name,user_answer=i)


# Получить номер телефона
@router.message(F.text == "Переписка с ботом")
async def go_to_group(message: types.Message):
    await message.answer("Готов к работе",reply_markup=start_button_admin)


# Итоги опроса
@router.message(Command("poll"))
async def data_poll(message: types.Message):
    data = await commands.select_all_answers()
    await message.answer(f"Итоги опроса:\n{data}")


# Команды
# Удалить пользователя из чата
@router.message(Command("kick"))
async def status_users(messege: types.Message):
    kick_chat_user = InlineKeyboardBuilder()
    for user in users_log:
         kick_chat_user.add(InlineKeyboardButton(text=f"@{user}", callback_data=f"kick{user}"))
    await messege.answer("Выбрать",reply_markup=kick_chat_user.as_markup())


@router.callback_query(F.data == "kick")
async def call_kick_user_chat(call: types.CallbackQuery,state: FSMContext):
    for user in users_log:
        if call.data == user:
            await bot.ban_chat_member(chat_id=GROUP_ID,user_id=choose_user[user],revoke_messages=True)
    await state.set_state(UserStatus.user_kick.state)


# Бан пользователя за нарушения
@router.message(Command("ban"))
async def ban_choose_user(message: types.Message, state: FSMContext) -> bot.ban_chat_member:
    ban_chat_user = InlineKeyboardBuilder()
    for user in users_log:
        ban_chat_user.add(InlineKeyboardButton(text=f"@{user}", callback_data=f"ban{user}"))
    await message.answer("Выбрать",reply_markup=ban_chat_user.as_markup())


@router.callback_query(ChatMemberFilter(chat_member=['banned']),F.data == "ban")
async def call_kick_user_chat(call: types.CallbackQuery, state: FSMContext):
    for user in choose_user:
        if call.data == user:
            await bot.ban_chat_member(chat_id=GROUP_ID,user_id=choose_user[user],revoke_messages=True)
            await call.message.answer(f"{user} Поздравляю, ты забанин на {int(time_bun_sec.seconds)}! лет")
    await state.set_state(UserStatus.user_ban.state)


#Разбанить пользователя
@router.message(Command("uban"),UserStatus.user_ban)
async def uban_user(message: types.Message, state:FSMContext) -> bot.unban_chat_member:
    data = await state.get_data()
    unban_chat_user = InlineKeyboardBuilder()
    if data['user_uban'] in choose_user:
        unban_chat_user.add(InlineKeyboardButton(text=f"Разбанить @{data}", callback_data=f"uban{data}"))
    await state.set_state(UserStatus.user_unban.state)


@router.callback_query(F.data == "uban")
async def call_kick_user_chat(call: types.CallbackQuery, state: FSMContext):
    if call.data in choose_user:
        await bot.uban_chat_member(chat_id=GROUP_ID,user_id=choose_user[call.data],revoke_messages=True)
    await call.message.answer(f"{call.data} Поздравляю, ты разбанин")
    await state.set_state(UserStatus.user_unban.state)


# Командаа Закрепить сообщение
@router.message(Command('pin'))
async def pin_message(message: types.Message):
    user_message = message.message_id
    await bot.pin_chat_message(GROUP_ID,message_id=user_message)

@router.message(Command('mes'))
async def get_message(message: types.Message):
    user_message = commands.select_all_message()
    await message.answer(f"Вот данные о новом сообщении {user_message}")







