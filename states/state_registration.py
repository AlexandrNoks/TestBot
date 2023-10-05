from aiogram.fsm.state import StatesGroup, State


class ReedLesson(StatesGroup):
    user_id = State()
    user_name = State()
    direction = State()
    weekday = State()
    time_lesson = State()
    user_phone = State()

class Direction(StatesGroup):
    name_direction = State()


class Registered(StatesGroup):
    user_id = State()
    your_name = State()
    direction = State()
    name_children = State()
    age_children = State()
    your_phone = State()


class StartRegistered(StatesGroup):
    register_name = State()
    register_phone = State()
    register_direction = State()
    finish_register_direction = State()