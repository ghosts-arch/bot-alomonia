# coding : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

from typing import Optional
from dataclasses import dataclass
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
    composite,
    object_session,
)


class Base(DeclarativeBase):

    __abstract__ = True

    @classmethod
    def set_database(cls, database):
        cls._database = database

    def save(self):
        with self._database.Session() as session:
            session.add(self)
            session.commit()


# one-to-one relation with User


class User(Base):

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    discord_id: Mapped[int] = mapped_column(unique=True)
    points: Mapped[int] = mapped_column(default=0)


class AdventCalendarBox(Base):

    __tablename__ = "advent_calendar_box"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    day: Mapped[int] = mapped_column()
    category: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    link: Mapped[str] = mapped_column()
    clues: Mapped[str] = mapped_column()
