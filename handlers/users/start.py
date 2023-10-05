import logging
from aiogram import types, F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder
from states.state_registration import ReedLesson
from middlewares.weekend import WeekendMessageMiddleware
from filters.chat_member import ChatMemberFilter
from filters.chat_type import ChatTypeFilter
from keyboards.start_bot_btn import to_ask_bot
from loader import dp,bot
from data.config import GROUP_URL, CHANNEL_URL, GROUP_ID
from data.registration import Registration
from data.recordlesson import RecordForLesson
# db = RecordForLesson("database.db")
db_reg = Registration("database.db")
db_rec = RecordForLesson("database.db")


router = Router()
router.message.filter(ChatTypeFilter(chat_type='private'))
router.message.filter(ChatMemberFilter(chat_member='left'))
router.message.middleware(WeekendMessageMiddleware())
keys_directions = ["Voc","Dan","Har"]
values_directions = ["Вокал","Танцы","Хариография"]
directions = dict(zip(keys_directions,values_directions))
keys_time = ["A","B","C","D","F","G","H","I","G"]
weekdays = ['Mo','Tu','We','Th','Fr']
time_lessons = ['11:00-11:50','12:10-13:00','13:20-14:10','14:30-15:20','15:40-16:30','16:50-17:40','18:00-18:50','19:10-20:00','20:20-21:10']
# weekdays = ['Пн','Вт','Ср','Чт','Пт']
user_data = {}
freedate = []


@router.message(CommandStart)
async def new_user(message: types.Message, state: FSMContext):
    try:
        # you_like_lesson = InlineKeyboardBuilder()
        # connection = db.create_table()
        # db.create_table()
        # connection = connection.cursor()
        # check = db.existing_user(message.from_user.id)
        # if check == False:
        #   you_like_lesson.add (
            #         InlineKeyboardButton(text="Пройти регистрацию", callback_data="Registration"),
            #         InlineKeyboardButton(text="Передумал",callback_data="AnswerNo")
            #     )
        #   await message.answer("Вы уже были у нас, надеюсь Вам понравилось, пройдите регистрацию чтобы мы добавили Вас в общий чат для родителей учеников!"
        #   ,reply_markup=you_like_lesson.as_markup())
        # else:
        await bot.send_message(message.from_user.id,f"Здравствуйте, чем могу помочь?",reply_markup=to_ask_bot)
    except Exception:
        logging.info("Что-то пошло не так, попробуйте снова")


# @dp.callback_query(F.data.startswith("Answer"))
# async def question_user(call: types.CallbackQuery, state: FSMContext):
# if call.data == "AnswerNo":
    # link_channel = InlineKeyboardMarkup(
    # inline_keyboard=[[InlineKeyboardButton(text="Ссылка на канал", callback_data="EnterChannel",url=CHANNEL_URL)]])
    # await call.message.answer("Очень жаль, подпишитесь на наш канал чтобы узнавать новости",replay_markup=link_channel)


# Записаться на урок
@dp.callback_query(F.data.startswith("Ask"))
async def reed_lesson(call: types.CallbackQuery, state: FSMContext):
    direction_button = InlineKeyboardBuilder()
    choice_weekday = InlineKeyboardBuilder()
    choice_time = InlineKeyboardBuilder()
    if call.data == "AskReedLesson":
        for direction in directions:
            direction_button.row(InlineKeyboardButton(text=f"{directions[direction]}", callback_data=f"AskCat{direction}"))
        await call.message.answer(f"Выберете направление",reply_markup=direction_button.as_markup())
    if call.data.startswith("AskCat"):
        for direction in directions:
            if call.data == f"AskCat{direction}":
                await state.update_data(direction=call.data[6:])
                for day in range(len(weekdays)):
                    choice_weekday.add(InlineKeyboardButton(text=f"{weekdays[day]}",callback_data=f"AskDay{weekdays[day]}"))
                await call.message.answer(f"Выберете день",reply_markup=choice_weekday.as_markup())
    if call.data.startswith("AskDay"):
        for days in weekdays:
            if call.data == f"AskDay{days}":
                await state.update_data(weekday=call.data[6:])
        for i in range(len(time_lessons)):
            choice_time.row(InlineKeyboardButton(text=f"{time_lessons[i]}",callback_data=f"AskTime{time_lessons[i]}"))
        await call.message.answer(f"Выберете время",reply_markup=choice_time.as_markup())
    if call.data.startswith("AskTime"):
        for times in time_lessons:
            if call.data == f'AskTime{times}':
                await state.update_data(time_lesson=call.data[7:])
                await call.message.answer("Пришлите номер телефона")
    await state.set_state(ReedLesson.user_phone.state)


# Получить номер телефона
@dp.message(ReedLesson.user_phone)
async def final_reedlesson(message: types.Message, state: FSMContext):
    # connection = db.create_table()
    # db.create_table()
    # connection = connection.cursor()
    data_phone = message.text
    await state.update_data(user_phone=data_phone)
    data = await state.get_data()
    data_user_id = message.from_user.id
    data_user_name = message.from_user.first_name
    data_direction = data.get("direction")
    data_weekday = data.get("weekday")
    data_time_lesson = data.get("time_lesson")
    data_user_phone = data.get("user_phone")
    # db.add_user(data_user_name,data_direction,data_weekday,data_time_lesson,data_user_phone)
    await message.answer(f"Данные добавлены\n{data_user_id}\n{data_user_name}\n{data_direction}\n{data_weekday}\n{data_time_lesson}\n{data_user_phone}")


@dp.callback_query(F.data.startswith("This"))
async def start_command(call: types.CallbackQuery, state: FSMContext):
    if call.data == "ThisChannel":
        link_channel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Канал", callback_data="EnterChannel", url=CHANNEL_URL)]])
        await call.message.answer("Зайти на наш канал",reply_markup=link_channel)
    elif call.data == "ThisContact":
        await call.message.answer("СК «Олимпийский» ул. Новая 17\nБЦ «Премьер» ул. Терешковой 263/2\nтел. 29-10-28")
    await state.set_state(ReedLesson.time_lesson.state)














