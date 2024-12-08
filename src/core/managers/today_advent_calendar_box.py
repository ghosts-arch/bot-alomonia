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

        if self.__client.config.get("MODE") == "production":
            advent_calendar_channel = await self.__client.fetch_channel(
                self.__client.config.get("ADVENT_CALENDAR_CHANNEL_ID")
            )
        else:
            advent_calendar_channel = await self.__client.fetch_channel(
                self.__client.config.get("TEST_CHANNEL_ID")
            )

        if not advent_calendar_channel:
            raise Exception("recurent_channel is None")

        if not isinstance(advent_calendar_channel, discord.TextChannel):
            raise Exception("birthdays_channel is not a TextChannel")

        match today_advent_calendar_box.category:
            case "movie":
                category = "🎬 Film"
            case "music":
                category = "🎵 Musique"
            case "video_game":
                category = "🎮 Jeu vidéo"
            case "_":
                print("error : unvalid category")
                return

        await advent_calendar_channel.send(
            content="@everyone",
            embed=Embed(
                title=f"Jour {today_advent_calendar_box.day} du calendrier de l'avant de Alomonia",
                description=f"Voilà les indices du jour :\n\n\t Catégorie : || {category} || \n\n Emojis : {" ".join([f'{c}' for c in list(today_advent_calendar_box.clues)])}\n\nA vous de jouer !",
            ).set_footer(
                text="Les énigmes du calendrier de l'avent sont générées par ChatGPT."
            ),
        )
