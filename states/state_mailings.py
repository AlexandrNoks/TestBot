from aiogram.dispatcher.filters.state import StatesGroup,State


class MailingChat(StatesGroup):
    text_mailing = State()
    photo_mailing = State()
    video_mailing = State()


class Schedule(StatesGroup):
    direction = State()
    date = State()
    time_lesson = State


