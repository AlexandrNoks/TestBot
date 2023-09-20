
from datetime import datetime

from aiogram.fsm.state import StatesGroup, State


class PollContest(StatesGroup):
    name_concert = State()
    data_contest = State()


class PollChat(StatesGroup):
    answer_yes = State()
    answer_no = State()
