from asyncpg import UniqueViolationError

from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Column,String,sql,BigInteger
from data.db_schedule import dict_schedule_weekday


class ScheduleWeekday(TimedBaseModel):
    __tablename__ = "schedule"
    num_day = Column(BigInteger,primary_key=True)
    time_lesson = Column(String(250))
    name_pupil = Column(String(250))
    one_week_day = Column(String(250))
    two_week_day = Column(String(250))

    async def weekly_schedule(num_day: int , time_lesson: str, name_pupil: str, one_weekday: str, two_weekday: str):
        try:
            i = 1
            for schedule in dict_schedule_weekday:
                i += 1
                lessons = ScheduleWeekday(num_day=i,time_lesson=schedule,name_pupil=dict_schedule_weekday[schedule][1][0],one_weekday=dict_schedule_weekday[schedule][1][1],two_weekday=dict_schedule_weekday[schedule][1][2])
                await lessons.create()
        except UniqueViolationError:
            print("Данные не добавлены")


class ScheduleToday(TimedBaseModel):
    id = Column(BigInteger,primary_key=True)
    time_lesson = Column(String(100))
    name_pupil = Column(String(500))

    query: sql.select