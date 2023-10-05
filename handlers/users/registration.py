from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder

from data.database import create_table
from filters.chat_member import ChatMemberFilter
from filters.chat_type import ChatTypeFilter
from middlewares.weekend import WeekendMessageMiddleware
from states.state_registration import Registered
from loader import dp,bot
from data.config import CHANNEL_URL

router = Router()
router.message.filter(ChatTypeFilter(chat_type='private'))
router.message.filter(ChatMemberFilter(chat_member='left'))
router.message.middleware(WeekendMessageMiddleware())
# router.message.filter(F.chat.type.in_({'member'}))
dict_directions = ["Voc","Dan","Har"]
list_direction = ["Вокал","Танцы","Хариография"]
directions = dict(zip(dict_directions,list_direction))
keys_time = ["A","B","C","D","F","G","H","I","G"]
eng_weekday = ['Mo','Tu','We','Th','Fr']
time_lesson = ['11:00-11:50','12:10-13:00','13:20-14:10','14:30-15:20','15:40-16:30','16:50-17:40','18:00-18:50','19:10-20:00','20:20-21:10']
weekdays = ['Пн','Вт','Ср','Чт','Пт']


@dp.callback_query(F.data.startswith("Registration"))
async def register_direction(call: types.CallbackQuery, state: FSMContext):
    direction_button = InlineKeyboardBuilder()
    if call.data == "Registration":
        for direction in directions:
            direction_button.row(InlineKeyboardButton(text=f"{directions[direction]}",callback_data=f"Dir{direction}"))
        await call.message.answer(f"Выберете направление:",reply_markup=direction_button.as_markup())
        await state.set_state(Registered.direction.state)


@dp.callback_query(F.data.startswith("Dir"))
async def register_name_children(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(direction=call.data)
    await call.message.answer("Пришлите имя ребенка")
    await state.set_state(Registered.name_children.state)


@dp.message(Registered.name_children)
async def register_age_children(message: types.Message, state: FSMContext):
    answer_name = message.text
    await state.update_data(name_children=answer_name)
    await message.answer("Пришлите возраст ребенка")
    await state.set_state(Registered.age_children.state)


@dp.message(Registered.age_children)
async def register_phone(message: types.Message, state: FSMContext):
    answer_age = message.text
    await state.update_data(age_children=answer_age)
    await message.answer("Пришлите свой номер телефона")
    await state.set_state(Registered.your_phone.state)


@dp.message(Registered.your_phone)
async def finish_register(message: types.Message,state: FSMContext):
    connection = create_table("database.db")
    cursor = connection.cursor()
    link_channel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Канал", callback_data="EnterChannel", url=CHANNEL_URL)]])
    await state.update_data(your_phone=message.text)
    user = await bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id)
    user_status = user.status
    data = await state.get_data()
    data_user_id = message.from_user.id
    data_user_status = user_status.value
    data_user_name = message.from_user.first_name
    data_direction = data.get("direction")
    data_name_children = data.get("name_children")
    data_age_children = data.get("age_children")
    data_your_phone = data.get("your_phone")
    cursor.execute("""
            INSERT INTO registration (user_id,user_status, your_name, direction, name_children, age_children, your_phone) VALUES (?,?,?,?,?,?,?)""",
                   (data_user_id,data_user_status,data_user_name,data_direction,data_name_children,data_age_children,data_your_phone))
    await message.answer(f"Спасибо Вы зарегистированы!{data_user_id}\n{data_user_status}\n{data_user_name}\n{data_direction}\n{data_name_children}\n{data_age_children}\n{data_your_phone} Просим Вас подписаться на наш канал", reply_markup=link_channel)
    connection.commit()
    connection.close()