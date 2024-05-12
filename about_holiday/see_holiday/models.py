from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Holiday(Base):
    __tablename__ = 'holiday'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    slug = Column(String)
    id_month = Column(Integer, ForeignKey('monthes.id'))
    id_day = Column(Integer, ForeignKey('days.id'))


class Month(Base):
    __tablename__ = 'monthes'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    count_days = Column(Integer)


class Day(Base):
    __tablename__ = 'days'
    id = Column(Integer, primary_key=True)
