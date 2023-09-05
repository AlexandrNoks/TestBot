import logging
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart,ChatTypeFilter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hide_link
from states.state_private import Schedule
# from data.schedule import time_lesson
from data.time_schedule import schedule
from keyboards.private_btn import to_ask_bot
from loader import dp,bot
from aiogram.dispatcher import FSMContext
from utils.db_api import quick_commands as commands
from states import Registered
from data.config import GROUP_URL, CHANNEL_URL

dict_directions = ["Vocal","Dance","Hariography"]
list_direction = ["Вокал","Танцы","Хариография"]
directions = dict(zip(list_direction,dict_directions))
keys_time = ["A","B","C","D","F","G","H","I","G"]
choice_time = InlineKeyboardMarkup()
eng_weekday = ['Mon','Tu','We','Th','Fr']
time_lesson = ['11:00-11:50','12:10-13:00','13:20-14:10','14:30-15:20','15:40-16:30','16:50-17:40','18:00-18:50','19:10-20:00','20:20-21:10']
weekdays = ['Пн','Вт','Ср','Чт','Пт']


@dp.message_handler(CommandStart(),ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def new_user(message: types.Message,state: FSMContext):
    try:
        # user = await commands.select_user(user_id=message.from_user.id)
        # if user.status == 'active':
        #     await message.answer(f"Ты уже зарегистирован! Заходи в группу {hide_link(GROUP_URL)}")
        # else:
        #     await commands.add_user(user_id=message.from_user.id,your_name=message.from_user.first_name)
        #     user = await commands.select_user(user_id=message.from_user.id)
        await bot.send_message(message.from_user.id,f"Здравствуйте, чем могу помочь?",reply_markup=to_ask_bot)
        async with state.proxy() as data:
            data["user_id"] = message.from_user.id
    except Exception:
        logging.info("Что-то пошло не так, попробуйте снова")


@dp.callback_query_handler(text_contains="Ask")
async def start_command(call: types.CallbackQuery,state: FSMContext):
    choice_weekday = InlineKeyboardMarkup()
    choice_time = InlineKeyboardMarkup()
    if call.data == "AskReedLesson":
        for day in range(len(weekdays)):
            choice_weekday.row(InlineKeyboardButton(text=f"{weekdays[day]}",callback_data=f"AskDay{eng_weekday[day]}"))
        await call.message.answer("Выберете день",reply_markup=choice_weekday)
    for weekday in range(len(eng_weekday)):
        if call.data == f"AskDay{eng_weekday[weekday]}":
            for i in range(len(time_lesson)):
                choice_time.row(InlineKeyboardButton(text=f"{time_lesson[i]}",callback_data=f"AskTime{keys_time[i]}"))
    await call.message.answer("Выберете Время",reply_markup=choice_time)
    for i in range(len(time_lesson)):
        if call.data == f"AskTime{keys_time[i]}":
            await call.message.answer(f"Да")



@dp.callback_query_handler(text_contains="This")
async def get_contact(call: types.CallbackQuery):
    if call.data == "ThisChannel":
        link_channel = InlineKeyboardMarkup(row_width=1).row(InlineKeyboardButton(text="Канал", callback_data="EnterChannel", url=CHANNEL_URL))
        await call.message.answer("Зайти на наш канал",reply_markup=link_channel)
    elif call.data == "ThisContact":
        await call.message.answer("СК «Олимпийский» ул. Новая 17\nБЦ «Премьер» ул. Терешковой 263/2\nтел. 29-10-28")

# @dp.callback_query_handler(text_contains="Day")
# async def choice_weekday(call: types.CallbackQuery):
#     eng_weekday = ['Mon','Tu','We','Th','Fr']
#     keys_time = ["A","B","C","D","F","G","H","I","G"]
#     message_choice = InlineKeyboardMarkup()
#     for day in eng_weekday:
#         if call.data == f"Day{day}":
#             for i in range(len(schedule)):
#                 try:
#                     message_choice.row(InlineKeyboardButton(text=f"{schedule[i]}",callback_data=f"WD{keys_time[i]}"))
#                 except IndexError:
#                     break
#     await call.message.answer("Рассписание",reply_markup=message_choice)

# @dp.callback_query_handler(text_contains="WD")
# async def choice_time_lesson(call: types.CallbackQuery):
#     eng_weekday = ['Mon','Tu','We','Th','Fr']
#     keys_time = ["A","B","C","D","F","G","H","I","G"]
#     message_choice = InlineKeyboardMarkup()
#     for times in schedule:
#         if call.data == f"WD{times}":
#             if
#             await call.message.answer("Рассписание",reply_markup=message_choice)


@dp.callback_query_handler(text_contains="Choose")
async def get_direction(call: types.CallbackQuery, state: FSMContext):
    await Registered.user_id.set()
    data = await state.get_data()
    user = data.get("user_id")
    for direct in directions:
        if call.data == f"Choose{direct}":
            await commands.update_user_direction(user_id=user,choose_direction=direct)
    await call.message.answer(f"{call.message.from_user.first_name},пришлите свой номер телефона")


@dp.message_handler(state=Registered.user_id)
async def get_phone(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data.get("user_id")
    answer_user = message.text
    await commands.update_user_phone(user_id=user,choose_phone=answer_user)
    await message.answer(f"Спасибо. Му скоро свяжемся с Вами "
                         f"А пока просим Вас подписаться на наш канал {hide_link('https://t.me/testmychannel03')}")













