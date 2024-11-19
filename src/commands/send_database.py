# encode : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import discord
from src.core.client import LuneaMoon
from src.core.interaction import Context, Interaction


class ApplicationCommand(Interaction):

    def __init__(self) -> None:
        self.name = "database"
        self.description = "send database"
        self.adminstration_channel_only = True
        self.moderator_only = True

    async def run(self, client: LuneaMoon, context: Context):
        database = client.database.send_database()
        await context.send(file=database)
