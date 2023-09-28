from utils.db_api.db_messages import TimedBaseModel
from sqlalchemy import Column, BigInteger, sql


class Messages(TimedBaseModel):
    __tablename__ = "active"
    message_id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger)

    query: sql.select