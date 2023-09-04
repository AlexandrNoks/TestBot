from aiogram.dispatcher.filters.state import StatesGroup,State


class GetContact(StatesGroup):
    user_name = State()
    user_phone = State()


class UserStatus(StatesGroup):
    user_status = State()
    user_left = State()
    user_kick = State()
    user_member = State()
    user_ban = State()
    user_unban = State()
    user_del = State()