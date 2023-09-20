from asyncpg import UniqueViolationError

from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Column,String,sql,BigInteger
from data.db_schedule import dict_schedule_weekday


class ReedLesson(TimedBaseModel):
    __tablename__ = "schedule"
    user_id = Column(BigInteger,primary_key=True)
    user_name = Column(String(250))
    weekday = Column(String(100))
    time_lesson = Column(String(250))
    user_phone = Column(String(500))



class ScheduleToday(TimedBaseModel):
    id = Column(BigInteger,primary_key=True)
    time_lesson = Column(String(100))
    name_pupil = Column(String(500))

    query: sql.select