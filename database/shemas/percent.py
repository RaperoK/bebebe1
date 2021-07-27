from sqlalchemy import Column, BigInteger, Integer, ARRAY, sql

from database.database import TimedBaseModel


class Percent(TimedBaseModel):
    __tablename__ = 'percent'

    id = Column(BigInteger, primary_key=True)
    percents = Column(ARRAY(Integer))

    query: sql.Select
