# encode : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import discord
from src.core.client import LuneaMoon
from src.core.interaction import Context, Interaction
from src.core.embeds import ErrorEmbed, Embed, SuccessEmbed


class ApplicationCommand(Interaction):

    def __init__(self) -> None:
        self.name = "add_tokens"
        self.description = "rajouter des points à un utilisateur (mod only)"
        self.adminstration_channel_only = True
        self.moderator_only = True
        self.options = [
            {
                "name": "user",
                "description": "Utilisateur à qui rajouter des points",
                "type": 6,
                "required": True,
            },
            {
                "name": "points",
                "description": "nombre de points à rajouter",
                "type": 4,
                "required": True,
            },
        ]

    async def run(self, client: LuneaMoon, context: Context):
        member = await context.guild.fetch_member(context.options[0].get("value"))
        user = client.database.get_user(discord_id=member.id)
        if not user:
            client.database.create_user(discord_id=member.id)
            user = client.database.get_user(discord_id=member.id)
        """client.database.add_user_points(
            user=user, points=context.options[1].get("value")
        )"""
        user.points += context.options[1].get("value")
        user.save()
        embed = SuccessEmbed(
            description=f"{member.mention} a maintenant {user.points} points"
        )
        await context.send(embed=embed)
