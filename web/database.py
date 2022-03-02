import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

# from config import DATABASE

DATABASE = {
    'drivername': 'postgresql',
    'host': 'db',
    'port': '5432',
    'username': 'postgres',
    'password': 'postgres',
    'database': 'postgres'
}


DeclarativeBase = declarative_base()


class info_event(DeclarativeBase):
    __tablename__ = 'info_event'

    id = Column(Integer, primary_key=True)
    quantity = Column('quantity', Integer)
    created_at = Column('created_at', DateTime(timezone=True))


def init():
    engine = create_engine(URL(**DATABASE))
    DeclarativeBase.metadata.create_all(engine)
    print('Init database', flush=True)


def get_session():
    engine = create_engine(URL(**DATABASE))
    Session = sessionmaker(bind=engine)
    return Session()


def add_new_record():
    new_event = info_event()
    new_event.quantity = 1
    new_event.created_at = datetime.datetime.now()
    session.add(new_event)
    session.commit()


def get_all_event():
    for post in session.query(info_event):
        print(post.__dict__)


init()
session = get_session()
