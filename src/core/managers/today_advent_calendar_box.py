import asyncio
import datetime
import discord


from ..embeds import Embed, ErrorEmbed
from .manager import Manager


class TodayAdventCalendarBoxManager(Manager):

    def __init__(self, client):
        super().__init__(client)
        self.__client = client

    async def callback(self):
        try:
            today_advent_calendar_box = (
                self.__client.database.get_today_advent_calendar_box()
            )
        except Exception as err:
            return ErrorEmbed(description=f"{err}")
        # #selfcare (test) - a laisser pour l'instant
        advent_calendar_channel = await self.__client.fetch_channel(1308571886267138088)

        if not advent_calendar_channel:
            raise Exception("recurent_channel is None")

        if not isinstance(advent_calendar_channel, discord.TextChannel):
            raise Exception("birthdays_channel is not a TextChannel")

        await advent_calendar_channel.send(
            embed=Embed(
                title=f"Jour {today_advent_calendar_box.day} du calendrier de l'avant de Alomnia",
                description=f"Voilà l'indice du jour : || {today_advent_calendar_box.clues} ||. \nA vous de jouer !",
            )
        )
