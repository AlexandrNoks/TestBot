import logging
from aiogram import types, F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder
from states.state_registration import ReedLesson,Registered
from middlewares.weekend import WeekendMessageMiddleware
from filters.chat_member import ChatMemberFilter
from keyboards.start_bot_btn import to_ask_bot
from loader import dp,bot
# from utils.db_api import lesson_commands as commands
from data.config import GROUP_URL, CHANNEL_URL, GROUP_ID

router = Router()
router.message.filter(ChatMemberFilter(chat_member='left'))
router.message.middleware(WeekendMessageMiddleware())
dict_directions = ["Voc","Dan","Har"]
list_direction = ["Вокал","Танцы","Хариография"]
directions = dict(zip(dict_directions,list_direction))
keys_time = ["A","B","C","D","F","G","H","I","G"]
eng_weekday = ['Mo','Tu','We','Th','Fr']
time_lesson = ['11:00-11:50','12:10-13:00','13:20-14:10','14:30-15:20','15:40-16:30','16:50-17:40','18:00-18:50','19:10-20:00','20:20-21:10']
weekdays = ['Пн','Вт','Ср','Чт','Пт']
user_data = {}
freedate = []

@router.message(CommandStart())
async def new_user(message: types.Message, state: FSMContext):
    try:
        # await commands.add_user(user_id=message.from_user.id,your_name=message.from_user.first_name)
        # you_like_lesson = InlineKeyboardBuilder()
        # user_data = message.from_user.id
        # await state.update_data(user_id=user_data)
        # await state.set_state(Registered.user_id.state)
        # data = await state.get_data()
        # user = data.get("user_id")
        # if user == message.from_user.id:
        #     you_like_lesson.add (
        #         InlineKeyboardButton(text="Да", callback_data="newpupilYes"),
        #         InlineKeyboardButton(text="Нет",callback_data="newpupilNo")
        #     )
        #     await message.answer("Если Вам понравилось у нас, нажмите Да если Нет",reply_markup=you_like_lesson.as_markup())
        # else:
        await bot.send_message(message.from_user.id,f"Здравствуйте, чем могу помочь?",reply_markup=to_ask_bot)
    except Exception:
        logging.info("Что-то пошло не так, попробуйте снова")


@dp.callback_query(F.data.startswith("Ask"))
async def reed_lesson(call: types.CallbackQuery, state: FSMContext):
    choice_weekday = InlineKeyboardBuilder()
    choice_time = InlineKeyboardBuilder()

    if call.data == "AskReedLesson":
        freedate.append(call.message.from_user.id)
        for day in range(len(weekdays)):
            choice_weekday.add(InlineKeyboardButton(text=f"{weekdays[day]}",callback_data=f"AskDay{eng_weekday[day]}"))
        await call.message.answer(f"Выберете день",reply_markup=choice_weekday.as_markup())
    if call.data.startswith("Ask"):
        for i in range(len(eng_weekday)):
            if call.data == f"AskDay{eng_weekday[i]}":
                freedate.append(eng_weekday[i])
                for i in range(len(time_lesson)):
                    choice_time.row(InlineKeyboardButton(text=f"{time_lesson[i]}",callback_data=f"AskTime{keys_time[i]}"))
                freedate.append(time_lesson[i])
                await call.message.answer(f"Выберете Время",reply_markup=choice_time.as_markup())
        await call.message.answer("Пришлите свой номер телефона")
    await state.set_state(ReedLesson.your_phone.state)


@router.message(ReedLesson.your_phone)
async def final_save_reedlesson(message: types.Message,state: FSMContext):
    your_phone = message.text
    freedate.append(your_phone)
    start_chat_button = ReplyKeyboardMarkup(row_width=1, keyboard=[[KeyboardButton(text="Запустить",request_id=GROUP_ID)]],resize_keyboard=True)
    await state.update_data(your_phone=your_phone)
    data = await state.get_data()
    data_phone = data.get("your_phone")
    # await message.answer(f"Спасибо {message.from_user.first_name}, вы записаны!\nДля уточнения иформации мы свяжемся с Вами по указанному номеру {data_phone}",reply_markup=start_chat_button)
    # await commands.add_reed(user_id=freedate[0],weekday=freedate[1],timelesson=freedate[2],phone=freedate[3])
    # await commands.get_user(user_id=freedate[0])
    # await message.answer(f"Добавил {user_lesson}")
    await message.answer(f"Добавил {data_phone}")
    # for item in freedate:
    #     await message.answer(f"{item}")
    await state.clear()


@dp.callback_query(F.data.startswith("This"))
async def start_command(call: types.CallbackQuery, state: FSMContext):
    if call.data == "ThisChannel":
        link_channel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Канал", callback_data="EnterChannel", url=CHANNEL_URL)]])
        await call.message.answer("Зайти на наш канал",reply_markup=link_channel)
    elif call.data == "ThisContact":
        await call.message.answer("СК «Олимпийский» ул. Новая 17\nБЦ «Премьер» ул. Терешковой 263/2\nтел. 29-10-28")
    await state.set_state(ReedLesson.time_lesson.state)


@dp.callback_query(F.data.startswith('newpupil'))
async def new_pupil_yes_no(call: types.CallbackQuery):
    # user = await commands.select_user(user_id=call.message.from_user.id)
    come_group = InlineKeyboardBuilder()
    register_now = InlineKeyboardButton(text="Пройти регистрацию",callback_data="registerNow")
    register_later = InlineKeyboardButton(text="Пройти регистрацию позже",callback_data="registerLater")
    come_group.add(register_now)
    come_group.add(register_later)
    if call.data == "newpupilYes":
        welcome_group = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Группа школы",url=GROUP_URL)]])
        await call.message.answer(f"Добро пожаловать в нашу группу!",reply_markup=welcome_group)
    elif call.data == "newpupilNo":
        link_channel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Наш Канал", callback_data="EnterChannel", url=CHANNEL_URL)]])
        await call.message.answer(f"Очень жаль, надеюсь вы  скоро передумаете,\nесли хотите получать новости о нас подпишитесь на наш телеграм канал",reply_markup=link_channel)


@dp.callback_query(F.data.startswith("AskThis"))
async def get_contact(call: types.CallbackQuery):
    if call.data == "ThisChannel":
        link_channel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Канал", callback_data="EnterChannel", url=CHANNEL_URL)]])
        await call.message.answer("Зайти на наш канал",reply_markup=link_channel)
    elif call.data == "ThisContact":
        await call.message.answer("СК «Олимпийский» ул. Новая 17\nБЦ «Премьер» ул. Терешковой 263/2\nтел. 29-10-28")













