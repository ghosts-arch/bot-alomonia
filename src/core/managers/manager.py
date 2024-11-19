# coding : utf-8
# Python 3.10.12
# ----------------------------------------------------------------------------

from abc import ABC, abstractmethod
import datetime
import asyncio
import logging

logger = logging.getLogger(__name__)


class Manager(ABC):

    def __init__(self, client):
        self.__client = client

    @abstractmethod
    async def callback(self, *args, **kwargs):
        pass

    async def run(self):

        date = datetime.datetime.now()
        if date.hour >= 7:  # 5h UTC => 7h TZ Paris
            date += datetime.timedelta(days=1)
        date = date.replace(hour=7, minute=0, second=0)

        delay = (date - datetime.datetime.now()).total_seconds()

        while True:
            await asyncio.sleep(delay=delay)
            delay = datetime.timedelta(days=1).total_seconds()
            await self.callback()

    def start(self):
        logger.info(f"Start {self.__class__.__name__} manager.")
        self.__client.loop.create_task(self.run())
