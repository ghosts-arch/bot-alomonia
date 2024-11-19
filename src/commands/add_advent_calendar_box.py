# encode : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import discord
from src.core.client import LuneaMoon
from src.core.interaction import Context, Interaction
from src.core.embeds import ErrorEmbed, Embed
from src.core.ui.forms.add_advent_calendar_box_form import AddAdventCalendarBoxForm


class ApplicationCommand(Interaction):

    def __init__(self) -> None:
        self.name = "add_advent_calendar_box"
        self.description = "add a box to the calendar (mod only)"
        self.adminstration_channel_only = True
        self.moderator_only = True

    async def run(self, client: LuneaMoon, context: Context):
        add_advent_calendar_box = AddAdventCalendarBoxForm()
        return await context.interaction.response.send_modal(add_advent_calendar_box)
