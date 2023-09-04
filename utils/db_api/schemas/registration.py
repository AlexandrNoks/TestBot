from sqlalchemy import Column,String,sql,BigInteger
from utils.db_api.db_gino import TimedBaseModel


class Registarion(TimedBaseModel):
    __tablename__ = "feedback"
    user_id = Column(BigInteger,primary_key=True)
    your_name = Column(String(250))
    your_phone = Column(String(250))
    direction = Column(String(250))


    query: sql.select
