# encode : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import discord
from src.core.client import LuneaMoon
from src.core.interaction import Context, Interaction
from src.core.embeds import ErrorEmbed, Embed


class ApplicationCommand(Interaction):

    def __init__(self) -> None:
        self.name = "show_advent_calandar_boxes"
        self.description = "show advent calandar boxes (mod only)"
        self.adminstration_channel_only = True
        self.moderator_only = True

    async def run(self, client: LuneaMoon, context: Context):
        boxes = client.database.get_advent_calendar_boxes()
        if not boxes:
            error_embed = ErrorEmbed(
                description="Il n'y a aucune case dans le calendrier de l'avant."
            )
            await context.send(embed=error_embed)

        calandar_boxes_embed = Embed(title="Calendrier de l'avant de Alomonia")
        for box in boxes:
            calandar_boxes_embed.add_field(
                name=f"jour {box.day}) {box.description} | {box.category}",
                value=f"indices : {box.clues}\nlien  : {box.link}",
                inline=False,
            )
        await context.send(embed=calandar_boxes_embed)
