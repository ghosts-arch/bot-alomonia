# coding : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import hashlib
import io
import discord
import sqlalchemy
import os
from contextlib import contextmanager

from datetime import datetime
from sqlalchemy import (
    and_,
    select,
    Integer,
    cast,
    or_,
    case,
    func,
    union,
    union_all,
    case,
    delete,
    update,
)
from sqlalchemy.orm import sessionmaker

from .models import Base, User, AdventCalendarBox


class Database:

    def __init__(self):
        echo = bool(os.getenv("DEV_MODE"))
        self.engine = sqlalchemy.create_engine(
            "sqlite:///src/core/database/database.db",
            echo=echo,
        )
        Base.metadata.create_all(self.engine)
        Base.set_database(self)
        self.Session = sessionmaker(self.engine, expire_on_commit=False)

    @contextmanager
    def session_scope(self):
        session = self.Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()

    def get_user(self, discord_id: int):
        with self.session_scope() as session:
            stmt = select(User).where(User.discord_id == discord_id)
            user = session.scalars(statement=stmt).first()
        return user

    def get_top_users(self):
        with self.session_scope() as session:
            stmt = select(User).order_by(User.points.desc()).limit(25)
            users = session.scalars(statement=stmt).all()
        return users

    def create_user(self, discord_id: int):
        with self.session_scope() as session:
            user = User(discord_id=discord_id)
            session.add(user)

    def add_user_points(self, user: User, points: int):
        with self.session_scope() as session:
            user.points += points
            session.add(user)

    def remove_user_points(self, user: User, points: int):
        with self.session_scope() as session:
            user.points -= points
            session.add(user)

    def remove_points(self, discord_id: int, points: int):
        with self.session_scope() as session:
            user = self.get_user(discord_id=discord_id)
            if not user:
                user = self.create_user(discord_id=discord_id)
            user.points -= points
            session.commit()
        return user

    def get_advent_calendar_boxes(self):
        with self.session_scope() as session:
            statement = select(AdventCalendarBox)
            boxes = session.scalars(statement=statement).all()
            return boxes

    def get_today_advent_calendar_box(self):
        with self.session_scope() as session:
            statement = select(AdventCalendarBox).where(
                AdventCalendarBox.day == datetime.now().day
            )
            box = session.scalars(statement=statement).first()
        return box

    def get_advent_calendar_box_by_day(self, day: int):
        with self.session_scope() as session:
            statement = select(AdventCalendarBox).where(AdventCalendarBox.day == day)
            result = session.scalars(statement=statement).first()
        return result

    def delete_advent_calendar_box(self, day: int):
        with self.session_scope() as session:
            statement = delete(AdventCalendarBox).where(AdventCalendarBox.day == day)
            session.execute(statement)
            session.commit()

    def add_advent_calendar_box(
        self, day: int, category: str, description: str, link: str, clues: str
    ):
        with self.session_scope() as session:
            advent_calendar_box = AdventCalendarBox(
                day=day,
                category=category,
                description=description,
                link=link,
                clues=clues,
            )
            session.add(advent_calendar_box)

    def edit_advent_calent_box(
        self,
        day: int,
        category: str,
        description: str,
        link: str,
        clues: str,
    ):
        with self.session_scope() as session:
            statement = (
                update(AdventCalendarBox)
                .where(AdventCalendarBox.day == day)
                .values(
                    day=day,
                    category=category,
                    description=description,
                    link=link,
                    clues=clues,
                )
            )
            session.execute(statement=statement)

    def send_database(self):
        with io.open("src/core/database/database.db", mode="rb") as f:
            return discord.File(f)
