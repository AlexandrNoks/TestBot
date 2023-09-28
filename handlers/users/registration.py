import logging
from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder
from states.state_registration import Registered
from loader import dp,bot
# from utils.db_api import quick_commands as commands
from data.config import CHANNEL_URL

router = Router()
router.message.filter(F.chat.type.in_({'member'}))
dict_directions = ["Voc","Dan","Har"]
list_direction = ["Вокал","Танцы","Хариография"]
directions = dict(zip(dict_directions,list_direction))
keys_time = ["A","B","C","D","F","G","H","I","G"]
eng_weekday = ['Mo','Tu','We','Th','Fr']
time_lesson = ['11:00-11:50','12:10-13:00','13:20-14:10','14:30-15:20','15:40-16:30','16:50-17:40','18:00-18:50','19:10-20:00','20:20-21:10']
weekdays = ['Пн','Вт','Ср','Чт','Пт']


@dp.callback_query(F.data.startswith("Register"))
async def register(call: types.CallbackQuery, state: FSMContext):
    direction_button = InlineKeyboardBuilder()
    for direction in directions:
        direction_button.row(InlineKeyboardButton(text=f"{directions[direction]}",callback_data=f"Dir{direction}"))
    await call.message.answer(f"Выберете направление:",reply_markup=direction_button.as_markup())
    await state.set_state(Registered.direction.state)


@dp.callback_query(F.data.startswith("newpupilYes"))
async def register(call: types.CallbackQuery, state: FSMContext):
    direction_button = InlineKeyboardBuilder()
    for direction in directions:
        direction_button.row(InlineKeyboardButton(text=f"{directions[direction]}",callback_data=f"Dir{direction}"))
    await call.message.answer(f"Выберете направление:",reply_markup=direction_button.as_markup())
    await state.set_state(Registered.direction.state)

@dp.callback_query(F.data.startswith("Dir"))
async def register(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(direction=call.data)
    await call.message.answer("Пришлите имя ребенка")
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
    await message.answer("Пришлите свой номер телефона")
    await state.set_state(Registered.your_phone.state)


@dp.message(Registered.your_phone)
async def finish_register(message: types.Message,state: FSMContext):
    link_channel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Канал", callback_data="EnterChannel", url=CHANNEL_URL)]])
    await message.answer(f"Спасибо Вы зарегистированы! Просим Вас подписаться на наш канал", reply_markup=link_channel)
