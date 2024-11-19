# encode : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import discord
from src.core.client import LuneaMoon
from src.core.interaction import Context, Interaction
from src.core.embeds import ErrorEmbed, Embed, SuccessEmbed


class ApplicationCommand(Interaction):

    def __init__(self) -> None:
        self.name = "leaderboard"
        self.description = "tableau des scores"

    async def run(self, client: LuneaMoon, context: Context):
        top_users = client.database.get_top_users()
        embed = Embed(title="Leaderboard")
        for i, user in enumerate(top_users):
            member = await context.guild.fetch_member(user.discord_id)
            embed.add_field(
                name=f"{i + 1}. {member.name}",
                value=f"{user.points} points",
                inline=False,
            )
        await context.send(embed=embed)
