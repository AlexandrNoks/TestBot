from utils.db_api.db_reedlesson import TimedBaseModel
from sqlalchemy import Column, BigInteger, sql,String,Integer


class ReedLesson(TimedBaseModel):

    __tablename__ = "reedlesson"

    user_id = Column(BigInteger,primary_key=True)
    weekday = Column(String(100))
    timelesson = Column(String(100))
    phone = Column(String(100))


    query: sql.select