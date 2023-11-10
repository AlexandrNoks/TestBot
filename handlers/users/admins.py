from datetime import datetime
from aiogram import Router, F
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from TestBot.data import config
from TestBot.data.registration import Registration
from TestBot.filters.chat_type import ChatTypeFilter
from TestBot.loader import dp, bot, active
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from TestBot.keyboards.start_bot_btn import start_button_admin
from TestBot.keyboards.mailing_btn import mailing_btn
from TestBot.filters.chat_member import ChatMemberFilter
from TestBot.data.config import CHANNEL_URL, GROUP_ID, GROUP_URL, BOT_URL, users_log, choose_user, users_id, time_bun_sec
from TestBot.states import UserStatus
from TestBot.utils.db_api import quick_commands as commands
from TestBot.middlewares.violation import ForbiddenWordsMiddleware
db = Registration
router = Router()
router.message.filter(ChatTypeFilter(chat_type='private'))
router.message.middleware(ForbiddenWordsMiddleware())
router.message.filter(ChatMemberFilter(chat_member="member"))
name_contest = ""
name_concerts= ["Времена года","Праздник Победы","Улыбки"]

@router.message(F.text == "Отправить в чат")
async def send_chat(message: types.Message):
    await bot.send_message(message.chat.id, f"Выберете посылку", reply_markup=mailing_btn)


@router.callback_query(F.data.startswith("mailing"))
async def mailing_chat(call: types.CallbackQuery):
    if call.data == "mailingSchedule":
        await bot.pin_chat_message(GROUP_ID, message_id=call.message.message_id)
        await bot.send_message(GROUP_ID, f"Рассписание на сегодня {datetime.today().strftime('%d.%m.%Y')}\n")
    if call.data == "mailingChannel":
        link_channel = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="Ссылка на канал", callback_data="EnterChannel", url=CHANNEL_URL)]])
        await bot.send_message(GROUP_ID, f"Пригласить на канал:", reply_markup=link_channel)
    elif call.data == "mailingExit":
        await call.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


@router.message(F.text == "Перейти..")
async def go_to_group(message: types.Message):
    urls_button = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="Группа", url=GROUP_URL),
            InlineKeyboardButton(text="Канал", url=CHANNEL_URL),
            InlineKeyboardButton(text="Чат с ботом", url=BOT_URL)
        ]]
    )
    await message.answer("Перейти", reply_markup=urls_button)


@router.message(F.text == "Написать ученику в л/с")
async def message_user(message: types.Message):
    for user in users_log:
        message_choice = InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(text=f"@{user}", url='https://t.me/+xxep96iuXxk3ZDky')
            ]])
        await message.answer("Выбрать", reply_markup=message_choice)


@router.message(F.text == "Переписка с ботом")
async def go_to_group(message: types.Message):
    await message.answer("Готов к работе", reply_markup=start_button_admin)


# Команда начать опрос
@router.message(F.text == "Создать опрос")
async def start_poll(message: types.Message):
    choice_concert = InlineKeyboardBuilder()
    for concert in name_concerts:
        choice_concert.add(InlineKeyboardButton(text=f"{concert} дата {'д.м.г.'}", callback_data=f"Poll{concert}"))
    await message.answer("Выбрать", reply_markup=choice_concert.as_markup())


# Опрос
@router.callback_query(F.data.startswith("Poll"))
async def get_name_contest(call: types.CallbackQuery):
    close_poll = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Закрыть опрос", callback_data="PollClose")]])
    for concert in name_concerts:
        if call.data == f"Poll{concert}":
            await call.bot.send_poll(GROUP_ID,
                                     question=f"Опрос, Дата Состоится {concert}\n Выберите 'Да' если принимаете участие или 'Нет' если не будите участвовать",
                                     correct_option_id=1,
                                     options=["Да", "Нет"], type="quiz", is_closed=False, is_anonymous=False,
                                     reply_markup=close_poll)
    if call.data == "PollClose":
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        # await bot.send_message(ADMIN_ID,"Готов к работе", reply_markup=start_button_admin)


# Голоса
@router.poll_answer()
async def date_answer(poll: types.PollAnswer):
    await active.set_bind(config.POSTGRES_URL)
    await active.gino.create_all()
    user_id = poll.user.id
    user_name = poll.user.first_name
    user_answer = poll.option_ids
    for i in user_answer:
        if i == 0:
            i = "Да"
            await commands.add_answer(user_id=user_id, user_name=user_name, user_answer=i)
        elif i == 1:
            i = "Нет"
            await commands.add_answer(user_id=user_id, user_name=user_name, user_answer=i)


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
    await messege.answer("Выбрать", reply_markup=kick_chat_user.as_markup())


@router.callback_query(F.data.startswith("kick"))
async def call_kick_user_chat(call: types.CallbackQuery, state: FSMContext):
    # connection = db.create_table()
    # connection = connection.cursor()
    for user in choose_user:
        try:
            if call.data == f"kick{user}":
                # get_user = db.kick_user(user_id=choose_user[user])
                await bot.ban_chat_member(chat_id=GROUP_ID, user_id=choose_user[user], revoke_messages=True)
            await state.set_state(UserStatus.user_kick.state)
        except IndexError:
            break



# Бан пользователя за нарушения
@router.message(Command("ban"))
async def ban_choose_user(message: types.Message, state: FSMContext) -> bot.ban_chat_member:
    # connection = db.create_table()
    # connection = connection.cursor()
    ban_chat_user = InlineKeyboardBuilder()
    for user in choose_user:
        ban_chat_user.add(InlineKeyboardButton(text=f"@{user}", callback_data=f"ban{user}"))
    await message.answer("Выбрать", reply_markup=ban_chat_user.as_markup())


@router.callback_query(F.data.startswith("ban"))
async def call_ban_user_chat(call: types.CallbackQuery, state: FSMContext):
    # connection = db.create_table()
    # connection = connection.cursor()
    for user in choose_user:
        if call.data == f"ban{user}":
            # user_ban = db.baned_user(choose_user[user])
            await bot.ban_chat_member(chat_id=GROUP_ID, user_id=choose_user[user], revoke_messages=True)
            await call.message.answer(f"{user} Поздравляю, ты забанин на {int(time_bun_sec.seconds)}! лет")
    await state.set_state(UserStatus.user_ban.state)


# Разбанить пользователя
@router.message(Command("uban"), UserStatus.user_ban)
async def uban_user(message: types.Message, state: FSMContext) -> bot.unban_chat_member:
    unban_chat_user = InlineKeyboardBuilder()
    data = await state.get_data()
    user = data.get("user_id")
    await bot.uban_chat_member(chat_id=GROUP_ID, user_id=user, revoke_messages=True)
    # user_ban = db.baned_user(choose_user[user])
    await message.answer(f"Ты разбанен")


 # Командаа Закрепить сообщение
@router.message(Command('pin'))
async def pin_message(message: types.Message):
    user_message = message.message_id
    await bot.pin_chat_message(GROUP_ID, message_id=user_message)
