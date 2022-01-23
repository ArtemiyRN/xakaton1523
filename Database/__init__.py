import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DATETIME, Column, Integer, String, ForeignKey, create_engine, Table, Boolean
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "userinfo"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    actitve = Column(Boolean)

    active_timestamp = Column(Integer)

    start = Column(Integer)


class Programm(Base):
    __tablename__ = "programms"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    start = Column(Integer)

    active_timestamp = Column(Integer)


engine = create_engine('sqlite:///database.db', echo=False)
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()


def auth_user(name):
    user = User(name=name, active=False, active_timestamp=0, start=0)
    session.add(user)
    session.commit()
    return user


def active_user():
    user = session.query(User).first()[0]
    user.active = True
    user.start = dint(datetime.datetime.now().timestamp())
    session.add(user)
    session.commit()


def inactive_user():
    user = session.query(User).first()[0]
    user.active = False
    user.active_timestamp += int(datetime.datetime.now().timestamp()) - user.start
    user.start = 0
    session.add(user)
    session.commit()


def start_programm(name):
    programm = Programm(
        name=name, start=int(datetime.datetime.now().timestamp()), actitve_timestamp=0)
    session.add(programm)
    session.commit()
    return programm


def stop_programm(programm: Programm):
    programm.active_timestamp = int(datetime.datetime.now().timestamp()) - programm.start
    programm.start = 0
    session.add(programm)
    session.commit()
    return programm
