from asyncpg import UniqueViolationError

from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Column,String,sql,BigInteger
from data.db_schedule import dict_schedule_weekday


class ReedLesson(TimedBaseModel):
    __tablename__ = "schedule"
    number = Column(BigInteger,primary_key=True)
    weekday = Column(String(100))
    time_lesson = Column(String(250))
    name_children = Column(String(250))
    age_children = Column(BigInteger,nullable=False)
    two_week_day = Column(String(250))




class ScheduleToday(TimedBaseModel):
    id = Column(BigInteger,primary_key=True)
    time_lesson = Column(String(100))
    name_pupil = Column(String(500))

    query: sql.select