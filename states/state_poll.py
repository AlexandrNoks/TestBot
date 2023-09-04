from aiogram.dispatcher.filters.state import StatesGroup, State
from datetime import datetime



class PollContest(StatesGroup):
    name_concert = State()
    data_contest = State()


class PollChat(StatesGroup):
    answer_yes = State()
    answer_no = State()
