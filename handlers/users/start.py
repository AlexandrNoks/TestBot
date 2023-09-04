import logging
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart,ChatTypeFilter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hide_link

from data.schedule import time_lesson
from data.time_schedule import schedule
from keyboards.private_btn import to_ask_bot
from loader import dp,bot
from aiogram.dispatcher import FSMContext
from utils.db_api import quick_commands as commands
from states import Registered
from data.config import GROUP_URL


dict_directions = ["Vocal","Dance","Hariography"]
list_direction = ["Вокал","Танцы","Хариография"]
directions = dict(zip(list_direction,dict_directions))


@dp.message_handler(CommandStart(),ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def new_user(message: types.Message,state: FSMContext):
    try:
        user = await commands.select_user(user_id=message.from_user.id)
        if user.status == 'active':
            await message.answer(f"Ты уже зарегистирован! Заходи в группу {hide_link(GROUP_URL)}")
        else:
            await commands.add_user(user_id=message.from_user.id,your_name=message.from_user.first_name)
            user = await commands.select_user(user_id=message.from_user.id)
            await bot.send_message(message.from_user.id,f"Здравствуйте, чем могу помочь? {user.user_id}",reply_markup=to_ask_bot)
            async with state.proxy() as data:
                data["user_id"] = message.from_user.id
    except Exception:
        logging.info("Что-то пошло не так, попробуйте снова")


@dp.callback_query_handler(text_contains="Ask")
async def choose_direction(call: types.CallbackQuery,state: FSMContext):
    keys_time = ["a","b","c","d","f","g","i","j","q","l"]
    message_choice = InlineKeyboardMarkup()
    time_lesson= InlineKeyboardMarkup()
    if call.data == "AskReedLesson":
        for direct in directions:
            message_choice.row(InlineKeyboardButton(text=f"{direct}", callback_data=f"Choose{direct}"))
        await call.message.answer(f"Выбрать", reply_markup=message_choice)
    elif call.data == "AskSchedule":
        for lesson in schedule[:5]:
                time_lesson.row(InlineKeyboardButton(text=f"{lesson}",callback_data=f"Choose{keys_time[:5]}"))
        for lesson in schedule[5:]:
                time_lesson.row(InlineKeyboardButton(text=f"{lesson}",callback_data=f"Choose{keys_time[5:]}"))


        await call.message.answer("Рассписание")
    elif call.data == "AskContact":
        await call.message.answer("СК «Олимпийский» ул. Новая 17\nБЦ «Премьер» ул. Терешковой 263/2\nтел. 29-10-28")


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













