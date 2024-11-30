# encode : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import discord
from src.core.client import LuneaMoon
from src.core.interaction import Context, Interaction
from src.core.embeds import ErrorEmbed, Embed, SuccessEmbed
from src.core.managers import TodayAdventCalendarBoxManager


class ApplicationCommand(Interaction):

    def __init__(self) -> None:
        self.name = "manually_trigger"
        self.description = "emergency trigger if automatic message does not work"
        self.adminstration_channel_only = True
        self.moderator_only = True

    async def run(self, client: LuneaMoon, context: Context):
        todayAdventCalendarBoxManager = TodayAdventCalendarBoxManager(client=client)
        await todayAdventCalendarBoxManager.callback()
