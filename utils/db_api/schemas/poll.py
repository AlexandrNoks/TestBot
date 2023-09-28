from utils.db_api.db_polls import TimedBaseModel
from sqlalchemy import Column,String,sql,BigInteger


class PollUsers(TimedBaseModel):
    __tablename__ = "poll"
    user_id = Column(BigInteger,primary_key=True)
    user_name = Column(String(250))
    user_answer = Column(String(250))

    query: sql.select


