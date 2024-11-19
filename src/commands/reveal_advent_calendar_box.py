# encode : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import discord
from src.core.client import LuneaMoon
from src.core.interaction import Context, Interaction
from src.core.embeds import ErrorEmbed, Embed


class ApplicationCommand(Interaction):

    def __init__(self) -> None:
        self.name = "reveal_advent_calendar_box"
        self.description = "show today's advent calendar box (mod only)"
        # self.adminstration_channel_only = True
        self.moderator_only = True

    async def run(self, client: LuneaMoon, context: Context):
        today_advent_calendar_box = client.database.get_today_advent_calendar_box()
        if not today_advent_calendar_box:
            error_embed = ErrorEmbed(description="Pas de case définie pour aujourd'hui")
            return await context.send(embed=error_embed)
        match today_advent_calendar_box.category:
            case "movie":
                message = f"***\nBien joué ! 🎉🎉🎉***\n\nLe fim à deviner pour le jour {today_advent_calendar_box.day} était bien *{today_advent_calendar_box.description}* !\n\n▶️ le lien sens critique du film : {today_advent_calendar_box.link}"
            case "music":
                message = f"***\nBien joué ! 🎉🎉🎉***\n\nLa musique à deviner pour le jour {today_advent_calendar_box.day} était bien *{today_advent_calendar_box.description}* !\n\n▶️ le lien spotify de la musique : {today_advent_calendar_box.link}"
            case "video_game":
                message = f"***\nBien joué ! 🎉🎉🎉***\n\nLe jeu vidéo à deviner pour le jour {today_advent_calendar_box.day} était bien *{today_advent_calendar_box.description}* !\n\n▶️ le lien steam du jeu vidéo : {today_advent_calendar_box.link}"
            case "_":
                print("error : unvalid category")
                return
        return await context.send(content=message)
