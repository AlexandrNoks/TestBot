import logging
from filters.chat_type import ChatTypeFilter
from filters.chat_member import ChatMemberFilter
from aiogram import types, F
from aiogram.filters import CommandStart, Command, ChatMemberUpdatedFilter, LEFT
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder
from aiogram.utils.markdown import hide_link
from states.state_registration import ReedLesson,Registered
from keyboards.private_btn import to_ask_bot
from loader import dp,bot,reg_db
from utils.db_api import quick_commands as commands
from data.config import GROUP_URL, CHANNEL_URL, GROUP_ID
dict_directions = ["Voc","Dan","Har"]
list_direction = ["Вокал","Танцы","Хариография"]
directions = dict(zip(dict_directions,list_direction))
keys_time = ["A","B","C","D","F","G","H","I","G"]
eng_weekday = ['Mo','Tu','We','Th','Fr']
time_lesson = ['11:00-11:50','12:10-13:00','13:20-14:10','14:30-15:20','15:40-16:30','16:50-17:40','18:00-18:50','19:10-20:00','20:20-21:10']
weekdays = ['Пн','Вт','Ср','Чт','Пт']

user_data = {}
@dp.message(ChatTypeFilter(chat_type='private'),CommandStart())
async def new_user(message: types.Message, state: FSMContext):
    try:
        users = await bot.get_chat_member(chat_id=GROUP_ID,user_id=message.from_user.id)
        user = await commands.select_user(user_id=message.from_user.id)
        if user.status == 'active':
            await commands.select_user(user_id=message.from_user.id)
            await message.answer(f"Ты уже зарегистирован! Заходи в группу {hide_link(GROUP_URL)}")
        else:
            await commands.add_user(user_id=message.from_user.id,your_name=message.from_user.first_name)
        await bot.send_message(message.from_user.id,f"Здравствуйте, чем могу помочь? {users.status}",reply_markup=to_ask_bot)
        # await state.set_state(ReedLesson.weekday.state)
    except Exception:
        logging.info("Что-то пошло не так, попробуйте снова")


@dp.callback_query(F.data.startswith("Ask"))
async def start_command(call: types.CallbackQuery, state: FSMContext):
    if call.data == "AskReedLesson":
        choice_weekday = InlineKeyboardBuilder()
        for day in range(len(weekdays)):
            choice_weekday.add(InlineKeyboardButton(text=f"{weekdays[day]}",callback_data=f"AskDay{eng_weekday[day]}"))
        await call.message.answer(f"Выберете день",reply_markup=choice_weekday.as_markup())
    if call.data.startswith("Ask"):
        for i in range(len(eng_weekday)):
            if call.data == f"AskDay{eng_weekday[i]}":
                choice_time = InlineKeyboardBuilder()
                for i in range(len(time_lesson)):
                    choice_time.row(InlineKeyboardButton(text=f"{time_lesson[i]}",callback_data=f"AskTime{keys_time[i]}"))
                await call.message.answer(f"Выберете Время",reply_markup=choice_time.as_markup())
    if call.data[-1] in keys_time:
        await call.message.answer(f"Спасибо {call.message.from_user.first_name}, вы записаны!")
    if call.data == "AskThisChannel":
        link_channel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Канал", callback_data="EnterChannel", url=CHANNEL_URL)]])
        await call.message.answer("Зайти на наш канал",reply_markup=link_channel)
    elif call.data == "AskThisContact":
        await call.message.answer("СК «Олимпийский» ул. Новая 17\nБЦ «Премьер» ул. Терешковой 263/2\nтел. 29-10-28")
    await state.set_state(ReedLesson.time_lesson.state)


@dp.callback_query(F.data == "Register")
async def register(call: types.CallbackQuery, state: FSMContext):
    direction_button = InlineKeyboardBuilder()
    if call.data == "Register":
        for direction in directions:
            direction_button.row(InlineKeyboardButton(text=f"{directions[direction]}",callback_data=f"Dir{direction}"))
        await call.message.answer("Выберете направление:",reply_markup=direction_button.as_markup())
    if call.data[-3:] in directions.keys():
        await call.message.answer("Пришлите свой номер телефона")
    await state.set_state(Registered.your_phone.state)


@dp.message(F.text == Registered.your_phone)
async def register_phone(message: types.Message, state: FSMContext):
    answer_phone = message.text
    await state.update_data(user_phone=answer_phone)
    await message.answer("Пришлите имя ребенка")
    await state.set_state(Registered.name_children.state)


@dp.message(Registered.name_children)
async def register_name(message: types.Message, state: FSMContext):
    answer_name = message.text
    await state.update_data(name_children=answer_name)
    await message.answer("Пришлите возраст ребенка")
    await state.set_state(Registered.age_children.state)


@dp.message(Registered.age_children)
async def register_age(message: types.Message, state: FSMContext):
    answer_age = message.text
    await state.update_data(age_children=answer_age)
    await state.set_state(Registered.age_children.state)


@dp.message(Registered.age_children)
async def finish_register(message: types.Message,state: FSMContext):
    choice_phone = await state.get_data()
    await message.answer(f"Спасибо вы зарегистированы, наш менеджер свяжется с вами по номеру {choice_phone['your_phone']} который вы оставили")



@dp.message(Registered.user_id)
async def get_phone(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user = data.get("user_id")
    answer_user = message.text
    await commands.update_user_phone(user_id=user,choose_phone=answer_user)
    await message.answer(f"Спасибо. Му скоро свяжемся с Вами "
                         f"А пока просим Вас подписаться на наш канал {hide_link('https://t.me/testmychannel03')}")

@dp.callback_query(F.data.startswith("AskThis"))
async def get_contact(call: types.CallbackQuery):
    if call.data == "ThisChannel":
        link_channel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Канал", callback_data="EnterChannel", url=CHANNEL_URL)]])
        await call.message.answer("Зайти на наш канал",reply_markup=link_channel)
    elif call.data == "ThisContact":
        await call.message.answer("СК «Олимпийский» ул. Новая 17\nБЦ «Премьер» ул. Терешковой 263/2\nтел. 29-10-28")













