# encode : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import random

from src.core.ui.forms import EditAdventCalendarBoxForm
from src.core.client import LuneaMoon
from src.core.interaction import Interaction, Context
from src.core.embeds import Embed, ErrorEmbed


class ApplicationCommand(Interaction):

    def __init__(self) -> None:
        self.name = "edit_advent_calendar_box"
        self.moderator_only = True
        self.description = "edit an advent calendar box (mod only)"
        self.options = [
            {
                "name": "day",
                "description": "jour de la case a editer",
                "type": 4,
                "required": True,
            },
        ]

    async def run(self, client: LuneaMoon, context: Context) -> None:

        day = context.options[0].get("value")
        print(day)
        if not day:
            return
        box = client.database.get_advent_calendar_box_by_day(day=day)
        edit_recurent_message_form = EditAdventCalendarBoxForm(advent_calendar_box=box)
        return await context.interaction.response.send_modal(edit_recurent_message_form)
