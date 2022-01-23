from ast import For
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DATETIME, Column, Integer, String, ForeignKey, create_engine, Table, Boolean
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

user_days = Table('user_days', Base.metadata,
                  Column('user_id', Integer, ForeignKey('users.id')),
                  Column('day_id', Integer, ForeignKey('days.id')))


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    days = relationship('Day', backref='user',
                        cascade='all', secondary=user_days)


class Day(Base):
    __tablename__ = 'days'
    id = Column(Integer, primary_key=True)

    hours = relationship('Hour', backref="day", cascade='all')


class Hour(Base):
    __tablename__ = 'hours'
    id = Column(Integer, primary_key=True)

    day_id = Column(Integer, ForeignKey='days.id')

    efficiency = Column(Integer)


engine = create_engine('sqlite:///database.db', echo=False)
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()


def new_user(name):
    user = User(name=name)
    session.add(user)
    session.commit()
    return user


def add_day(user: User):
    day = Day()
    user.days.append(day)
    session.add(user, day)
    session.commit()
    return day


def add_hour(day: Day, efficiency: int):
    hour = Hour(efficiency=efficiency)
    day.hours.append(hour)
    session.add(day, hour)
    session.commit()
    return hour
