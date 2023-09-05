from aiogram.dispatcher.filters.state import StatesGroup,State

class FilterMessage(StatesGroup):
    message_del = State()

class GetContact(StatesGroup):
    user_status = State()
    user_name = State()
    user_phone = State()


class Price(StatesGroup):
    user_status = State()
    user_name = State()
    direction = State()
    one_day = State()
    ticket = State()

class Schedule(StatesGroup):
    weekday = State()
    time_lesson = State()