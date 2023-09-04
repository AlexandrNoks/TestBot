from aiogram.dispatcher.filters.state import StatesGroup,State


class Direction(StatesGroup):
    name_direction = State()


class Registered(StatesGroup):
    user_id = State()
    your_name = State()
    your_phone = State()
    direction = State()


class StartRegistered(StatesGroup):
    register_name = State()
    register_phone = State()
    register_direction = State()
    finish_register_direction = State()