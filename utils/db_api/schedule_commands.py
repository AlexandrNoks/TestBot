from asyncpg import UniqueViolationError
from data.db_schedule import dict_schedule_weekday
from utils.db_api.schemas.schedule import ScheduleWeekday


async def weekly_schedule(num_day: int , time_lesson: str, name_pupil: str, one_weekday: str, two_weekday: str):
    try:
        i = 1
        for schedule in dict_schedule_weekday:
            i += 1
            lessons = ScheduleWeekday(num_day=i,time_lesson=schedule,name_pupil=dict_schedule_weekday[schedule][1][0],one_weekday=dict_schedule_weekday[schedule][1][1],two_weekday=dict_schedule_weekday[schedule][1][2])
            await lessons.create()
    except UniqueViolationError:
        print("Данные не добавлены")


