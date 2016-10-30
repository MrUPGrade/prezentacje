from dictalchemy import make_class_dictable
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import TEXT, VARCHAR, INTEGER, BOOLEAN
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
make_class_dictable(Base)


class User(Base):
    __tablename__ = 'users'

    id = Column(INTEGER, primary_key=True)
    first_name = Column(VARCHAR(100))
    last_name = Column(VARCHAR(100))
    about_me = Column(TEXT)
    emails = relationship('Email')


class Email(Base):
    __tablename__ = 'emails'

    id = Column(INTEGER, primary_key=True)
    user_id = Column(INTEGER, ForeignKey('users.id'))
    address = Column(VARCHAR(200))
    is_primary = Column(BOOLEAN)


class BadUser(Base):
    __tablename__ = 'bad_users'

    id = Column(VARCHAR(36), primary_key=True)
    name = Column(VARCHAR(100))
    address = Column(VARCHAR(250))
    comment = Column(TEXT)


class GoodUser(Base):
    __tablename__ = 'good_users'

    id = Column(VARCHAR(36), primary_key=True)
    name = Column(VARCHAR(100))
    address = Column(VARCHAR(250))
    comment = Column(TEXT)


assoc_film_cinema = Table(
    'assoc_film_cinema', Base.metadata,
    Column('film_id', INTEGER, ForeignKey('film.id')),
    Column('cinema_id', INTEGER, ForeignKey('cinema.id'))
)


class Film(Base):
    __tablename__ = 'film'

    id = Column(INTEGER, primary_key=True)
    title = Column(TEXT)
    length = Column(INTEGER)


class Cinema(Base):
    __tablename__ = 'cinema'

    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT)
    address = Column(TEXT)
    films = relationship(
        'Film',
        secondary=assoc_film_cinema
    )


def session_factory():
    engine = create_engine('postgresql+pg8000://postgres:postgres@192.168.122.1:31000/dalopt',
                           echo=True)
    # echo=False)
    Session = sessionmaker(bind=engine)
    return Session()
