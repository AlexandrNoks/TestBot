from aiogram.fsm.state import StatesGroup, State


class ReedLesson(StatesGroup):
    weekday = State()
    time_lesson = State()

class Direction(StatesGroup):
    name_direction = State()


class Registered(StatesGroup):
    user_id = State()
    your_name = State()
    direction = State()
    your_phone = State()
    name_children = State()
    age_children = State()


class StartRegistered(StatesGroup):
    register_name = State()
    register_phone = State()
    register_direction = State()
    finish_register_direction = State()