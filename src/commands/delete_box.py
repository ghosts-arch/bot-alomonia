# encode : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import random

from src.core.ui.views import DeleteAdventCalendarBoxView
from src.core.client import LuneaMoon
from src.core.interaction import Interaction, Context
from src.core.embeds import Embed, ErrorEmbed


class ApplicationCommand(Interaction):

    def __init__(self) -> None:
        self.name = "delete_box"
        self.moderator_only = True
        self.description = "delete an advent calendar box (mod only)"
        self.options = [
            {
                "name": "day",
                "description": "jour de la case a supprimer",
                "type": 4,
                "required": True,
            },
        ]

    async def run(self, client: LuneaMoon, context: Context) -> None:
        day = context.options[0].get("value")
        if not day:
            return
        box = client.database.get_advent_calendar_box_by_day(day=day)
        if not box:
            error_embed = ErrorEmbed(
                description="Cette case n'existes pas.",
            )
            return await context.send(embed=error_embed)
        embed = Embed(
            title="Confirmation",
            description=f"Êtes-vous sûr de vouloir supprimer la case du jour {box.day}?",
        )
        view = DeleteAdventCalendarBoxView(advent_calendar_box=box)

        await context.interaction.response.send_message(embed=embed, view=view)
