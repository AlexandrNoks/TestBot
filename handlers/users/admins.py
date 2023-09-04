from datetime import datetime

from aiogram import types

# from data.db_schedule import dict_schedule
from data.poll_db import name_concert

from loader import dp,bot
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardRemove
from aiogram.dispatcher.filters import ChatTypeFilter, Command
from keyboards.start_bot_btn import start_button_admin
from keyboards.mailing_btn import mailing_btn
from filters import IsAdminGroup
from data.config import *
from states import GetContact, UserStatus
from utils.db_api import poll_commands as commands


name_contest = ""


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE),text="Отправить в чат")
async def send_chat(message: types.Message):
    await bot.send_message(message.chat.id,"Выберете посылку", reply_markup=mailing_btn)


@dp.callback_query_handler(text_contains="mailing")
async def mailing_chat(call: types.CallbackQuery):
    schedule_day = ""
    await call.bot.send_message(GROUP_ID,f"Рассписание на {datetime.today().strftime('%d.%m.%Y')}")
    # if call.data == "mailingSchedule":
    #     await call.message.answer(f"Рассписание на {datetime.today().strftime('%d.%m.%Y')}")
    #     for schedule in dict_schedule:
    #         schedule_day += f"{schedule} {dict_schedule[schedule]}\n"
    #     await call.bot.send_message(GROUP_ID,schedule_day)
    if call.data == "mailingChannel":
        link_channel = InlineKeyboardMarkup(row_width=1).row(InlineKeyboardButton(text="Ссылка на канал", callback_data="EnterChannel",url=CHANNEL_URL))
        await call.message.answer(f"Пригласить на канал:",reply_markup=link_channel)
    elif call.data == "mailingExit":
        await call.bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE),text="Перейти..")
async def go_to_group(message: types.Message):
    urls_button = InlineKeyboardMarkup()
    url_group = InlineKeyboardButton(text="Группа", url=GROUP_URL)
    url_channel = InlineKeyboardButton(text="Канал", url=CHANNEL_URL)
    url_bot = InlineKeyboardButton(text="Чат с ботом", url=BOT_URL)
    urls_button.row(url_group,url_channel,url_bot)
    await message.answer("Перейти",reply_markup=urls_button)


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE),text="Написать ученику в л/с")
async def message_user(message: types.Message):
    message_choice = InlineKeyboardMarkup()
    for user in users_log:
        message_choice.row(InlineKeyboardButton(text=f"@{user}", url='https://t.me/+xxep96iuXxk3ZDky'))
    await message.answer("Выбрать",reply_markup=message_choice)


# Команда начать опрос
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE),text="Создать опрос")
async def start_poll(message: types.Message):
    message_choice = InlineKeyboardMarkup()
    for concert in name_concert:
        message_choice.row(InlineKeyboardButton(text=f"{concert} дата {'д.м.г.'}", callback_data=f"Poll{concert}"))
    message_choice.add(InlineKeyboardButton(text="Закрыть опрос",callback_data="PollClose"))
    await bot.send_message(ADMIN_ID,"Выбрать", reply_markup=message_choice)


# Опрос
@dp.callback_query_handler(text_contains="Poll")
async def get_name_contest(call: types.CallbackQuery, state: FSMContext):
    for concert in name_concert:
        if call.data == f"Poll{concert}":
            await call.bot.send_poll(GROUP_ID,question=f"Опрос, Дата Состоится {concert}\n Выберите 'Да' если принимаете участие или 'Нет' если не будите участвовать",correct_option_id=1,
                                     options=["Да","Нет"], type="quiz", is_closed=False, is_anonymous=False,reply_markup=ReplyKeyboardRemove())
    if call.data == "PollClose":
        await bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
        await bot.send_message(ADMIN_ID,"Готов к работе", reply_markup=start_button_admin)


# Голоса
@dp.poll_answer_handler()
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
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), text="Запросить контакт", state=GetContact.user_phone)
async def request_contact(message: types.Message, state: FSMContext):
    get_contact = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отправить свой номер тел",request_contact=True)]],resize_keyboard=True)
    await message.answer_contact("Пришлите номер телефона",message.from_user.first_name, reply_markup=get_contact)
    await GetContact.user_phone.set()


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=GetContact.user_phone)
async def request_contact(message: types.Message, state: FSMContext):
    user_text = message.text
    async with state.proxy() as data:
        data["user_phone"] = user_text
    await message.answer(f"Спасибо, {message.from_user.first_name} Ваш номер телефона: {user_text}",message.from_user.first_name)


@dp.message_handler(ChatTypeFilter(chat_type=[types.ChatType.SUPERGROUP,types.ChatType.GROUP]),text="Переписка с ботом")
async def go_to_group(message: types.Message):
    await message.answer("Готов к работе",reply_markup=start_button_admin)


# Итоги опроса
@dp.message_handler(text="/poll")
async def data_poll(message: types.Message):
    data = await commands.select_all_answers()
    await message.answer(f"Итоги опроса:\n{data}")

# Команды
# Удалить пользователя из чата
@dp.message_handler(IsAdminGroup(),ChatTypeFilter(chat_type=types.ChatType.PRIVATE),Command("kick", prefixes="/"))
async def status_users(messege: types.Message):
    message_choice = InlineKeyboardMarkup()
    for user in users_log:
        message_choice.row(InlineKeyboardButton(text=f"@{user}", callback_data=f"kick{user}"))
    await messege.answer("Выбрать",reply_markup=message_choice)


@dp.callback_query_handler(text_contains="kick")
async def call_kick_user_chat(call: types.CallbackQuery):
    for user in users_log:
        if call.data == user:
            await bot.ban_chat_member(chat_id=GROUP_ID,user_id=choose_user[user],revoke_messages=True)
    await UserStatus.user_kick.set()


# Бан пользователя за нарушения
@dp.message_handler(IsAdminGroup(),ChatTypeFilter(chat_type=types.ChatType.PRIVATE),Command("ban", prefixes="/"))
async def ban_choose_user(message: types.Message, state: FSMContext) -> bot.ban_chat_member:
    message_choice = InlineKeyboardMarkup()
    for user in users_log:
        message_choice.row(InlineKeyboardButton(text=f"@{user}", callback_data=f"ban{user}"))
    await message.answer("Выбрать",reply_markup=message_choice)


@dp.callback_query_handler(text_contains="ban")
async def call_kick_user_chat(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        for user in choose_user:
            if call.data == user:
                await bot.ban_chat_member(chat_id=GROUP_ID,user_id=choose_user[user],revoke_messages=True)
                await call.message.answer(f"{user} Поздравляю, ты забанин на {int(time_bun_sec.seconds)}! лет")
        await UserStatus.user_ban.set()


#Разбанить пользователя
@dp.message_handler(IsAdminGroup(),ChatTypeFilter(chat_type=types.ChatType.PRIVATE),Command("uban", prefixes="/"),state=UserStatus.user_ban)
async def uban_user(message: types.Message, state:FSMContext) -> bot.unban_chat_member:
    async with state.proxy() as data:
        if data in choose_user:
            message_choice = InlineKeyboardMarkup()
            message_choice.row(InlineKeyboardButton(text=f"Разбанить @{data}", callback_data=f"uban{data}"))
        await UserStatus.user_unban.set()


@dp.callback_query_handler(text_contains="uban")
async def call_kick_user_chat(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if data in choose_user:
            await bot.uban_chat_member(chat_id=GROUP_ID,user_id=choose_user[data],revoke_messages=True)
        await call.message.answer(f"{data} Поздравляю, ты разбанин")
        await UserStatus.user_unban.set()


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def message_user(message: types.Message):
    for word in WORDS:
        if message.text in word:
            await bot.delete_message(message.chat.id, message.message_id)








