from datetime import datetime
from aiogram import Router, F
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from data.db_schedule import dict_schedule
from data.poll_db import name_concert

from loader import dp,bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardRemove, BufferedInputFile
from filters.chat_type import ChatTypeFilter
from keyboards.start_bot_btn import start_button_admin
from keyboards.mailing_btn import mailing_btn
from filters.chat_member import ChatMemberFilter
from data.config import *
from states import GetContact, UserStatus
from utils.db_api import poll_commands as commands
from middlewares.violation import ForbiddenWordls


router = Router()
router.message.middleware(ForbiddenWordls())
router.message.filter()
name_contest = ""


@dp.message(ChatMemberFilter(chat_member=['creator','administrator']), F.text == "Отправить в чат")
async def send_chat(message: types.Message):
    await bot.send_message(message.chat.id,f"Выберете посылку", reply_markup=mailing_btn)


@dp.callback_query(F.data.startswith("mailing"))
async def mailing_chat(call: types.CallbackQuery):
    if call.data == "mailingSchedule":
        await bot.send_message(GROUP_ID, f"Рассписание на сегодня {datetime.today().strftime('%d.%m.%Y')}\n")
    if call.data == "mailingPhoto":
        file_ids = []
        with open('media/photos/file_20.jpg', 'rb') as image_from_buffer:
            photo_chat = await call.message.answer_photo(
                BufferedInputFile(
                    image_from_buffer.read(),filename='image_from_buffer.jpg'),caption='Изоброжение из буферобмена')
        file_ids.append(photo_chat.photo[-1].file_id)
        await bot.send_photo(chat_id=GROUP_ID,photo=file_ids[-1])
        await bot.send_photo(chat_id=CHANNEL_ID,photo=file_ids[-1])
    if call.data == "mailingVideo":
        file_ids = []
        with open('media/photos/test_3.mp4', 'rb') as video_from_buffer:
            video_chat = await call.message.answer_video(
                BufferedInputFile(
                    video_from_buffer.read(),filename='video_from_buffer.mp4'),caption='Видео из буферобмена')
        file_ids.append(video_chat.video.file_id)
        await bot.send_video(chat_id=GROUP_ID,video=file_ids[-1])
        await bot.send_video(chat_id=CHANNEL_ID,video=file_ids[-1])
    if call.data == "mailingChannel":
        link_channel = InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(text="Ссылка на канал", callback_data="EnterChannel",url=CHANNEL_URL)]])
        await call.message.answer(f"Пригласить на канал:",reply_markup=link_channel)
    elif call.data == "mailingExit":
        await call.bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)


@dp.message(ChatMemberFilter(chat_member=['creator','administrator']),F.text == "Перейти..")
async def go_to_group(message: types.Message):
    urls_button = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="Группа", url=GROUP_URL),
            InlineKeyboardButton(text="Канал", url=CHANNEL_URL),
            InlineKeyboardButton(text="Чат с ботом", url=BOT_URL)
        ]]
    )
    await message.answer("Перейти",reply_markup=urls_button)


@dp.message(ChatTypeFilter(chat_type=['private']),ChatMemberFilter(chat_member=['creator','administrator']),F.text == "Написать ученику в л/с")
async def message_user(message: types.Message):
    for user in users_log:
        message_choice = InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(text=f"@{user}", url='https://t.me/+xxep96iuXxk3ZDky')
            ]])
        await message.answer("Выбрать",reply_markup=message_choice)


# Команда начать опрос
@dp.message(ChatTypeFilter(chat_type=['private']),ChatMemberFilter(chat_member=['creator','administrator']),F.text == "Создать опрос")
async def start_poll(message: types.Message):
    choice_concert = InlineKeyboardBuilder()
    for concert in name_concert:
        choice_concert.add(InlineKeyboardButton(text=f"{concert} дата {'д.м.г.'}", callback_data=f"Poll{concert}"))
    await bot.send_message(ADMIN_ID,"Выбрать", reply_markup=choice_concert)
    close_poll = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Закрыть опрос",callback_data="PollClose")]])
    await bot.send_message(ADMIN_ID,"Закрыть опрос", reply_markup=close_poll)



# Опрос
@dp.callback_query(F.data.startswitch("Poll"))
async def get_name_contest(call: types.CallbackQuery, state: FSMContext):
    for concert in name_concert:
        if call.data == f"Poll{concert}":
            await call.bot.send_poll(GROUP_ID,question=f"Опрос, Дата Состоится {concert}\n Выберите 'Да' если принимаете участие или 'Нет' если не будите участвовать",correct_option_id=1,
                                     options=["Да","Нет"], type="quiz", is_closed=False, is_anonymous=False,reply_markup=ReplyKeyboardRemove())
    if call.data == "PollClose":
        await bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
        await bot.send_message(ADMIN_ID,"Готов к работе", reply_markup=start_button_admin)


# Голоса
@dp.poll_answer()
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
@dp.message(ChatTypeFilter(chat_type=['private']),ChatMemberFilter(chat_member=['creator','administrator']), F.text == "Запросить контакт", GetContact.user_phone)
async def request_contact(message: types.Message, state: FSMContext):
    get_contact = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отправить свой номер тел",request_contact=True)]],resize_keyboard=True)
    await message.answer_contact("Пришлите номер телефона",message.from_user.first_name, reply_markup=get_contact)
    await state.set_state(GetContact.user_phone.state)


@dp.message(ChatTypeFilter(chat_type=['private']),ChatMemberFilter(chat_member=['creator','administrator']),GetContact.user_phone)
async def request_contact(message: types.Message, state: FSMContext):
    user_text = message.text
    data = await state.get_data()
    data["user_phone"] = user_text
    await message.answer(f"Спасибо, {message.from_user.first_name} Ваш номер телефона: {data['user_phone']}",message.from_user.first_name)


@dp.message(ChatTypeFilter(chat_type=['private']),ChatMemberFilter(chat_member=['creator','administrator']),F.text == "Переписка с ботом")
async def go_to_group(message: types.Message):
    await message.answer("Готов к работе",reply_markup=start_button_admin)


# Итоги опроса
@dp.message(ChatTypeFilter(chat_type=['private']),ChatMemberFilter(chat_member=['creator','administrator']),Command("poll"))
async def data_poll(message: types.Message):
    data = await commands.select_all_answers()
    await message.answer(f"Итоги опроса:\n{data}")


# Команды
# Удалить пользователя из чата
@dp.message(ChatTypeFilter(chat_type=['private']),ChatMemberFilter(chat_member=['creator','administrator']),Command("kick"))
async def status_users(messege: types.Message):
    kick_chat_user = InlineKeyboardBuilder()
    for user in users_log:
         kick_chat_user.add(InlineKeyboardButton(text=f"@{user}", callback_data=f"kick{user}"))
    await messege.answer("Выбрать",reply_markup=kick_chat_user.as_markup())


@dp.callback_query(F.data == "kick")
async def call_kick_user_chat(call: types.CallbackQuery,state: FSMContext):
    for user in users_log:
        if call.data == user:
            await bot.ban_chat_member(chat_id=GROUP_ID,user_id=choose_user[user],revoke_messages=True)
    await state.set_state(UserStatus.user_kick.state)


# Бан пользователя за нарушения
@dp.message(ChatTypeFilter(chat_type=['private']),ChatMemberFilter(chat_member=['creator','administrator']),Command("ban"))
async def ban_choose_user(message: types.Message, state: FSMContext) -> bot.ban_chat_member:
    ban_chat_user = InlineKeyboardBuilder()
    for user in users_log:
        ban_chat_user.add(InlineKeyboardButton(text=f"@{user}", callback_data=f"ban{user}"))
    await message.answer("Выбрать",reply_markup=ban_chat_user.as_markup())


@dp.callback_query(ChatMemberFilter(chat_member=['banned']),F.data == "ban")
async def call_kick_user_chat(call: types.CallbackQuery, state: FSMContext):
    for user in choose_user:
        if call.data == user:
            await bot.ban_chat_member(chat_id=GROUP_ID,user_id=choose_user[user],revoke_messages=True)
            await call.message.answer(f"{user} Поздравляю, ты забанин на {int(time_bun_sec.seconds)}! лет")
    await state.set_state(UserStatus.user_ban.state)


#Разбанить пользователя
@dp.message(ChatMemberFilter(chat_member=['creator','administrator']),ChatTypeFilter(chat_type=['private']),Command("uban"),UserStatus.user_ban)
async def uban_user(message: types.Message, state:FSMContext) -> bot.unban_chat_member:
    data = await state.get_data()
    unban_chat_user = InlineKeyboardBuilder()
    if data['user_uban'] in choose_user:
        unban_chat_user.add(InlineKeyboardButton(text=f"Разбанить @{data}", callback_data=f"uban{data}"))
    await state.set_state(UserStatus.user_unban.state)

@dp.callback_query(ChatMemberFilter(chat_member=['member']), F.data == "uban")
async def call_kick_user_chat(call: types.CallbackQuery, state: FSMContext):
    if call.data in choose_user:
        await bot.uban_chat_member(chat_id=GROUP_ID,user_id=choose_user[call.data],revoke_messages=True)
    await call.message.answer(f"{call.data} Поздравляю, ты разбанин")
    await state.set_state(UserStatus.user_unban.state)


# Командаа Закрепить сообщение
@dp.message(Command('pin'))
async def pin_message(message: types.Message):
    user_message = message.message_id
    await bot.pin_chat_message(GROUP_ID,message_id=user_message)








