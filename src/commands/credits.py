# encode : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import random

from src.core.client import LuneaMoon
from src.core.interaction import Interaction, Context
from src.core.embeds import Embed


class ApplicationCommand(Interaction):

    def __init__(self) -> None:
        self.name = "credits"
        self.description = "credits du bot"

    async def run(self, client, context: Context) -> None:
        face = random.choice(["Pile !", "Face !"])
        embed = Embed().set_description(
            """
            🤖 Bot Alomonia - Un bot open source

Ce bot est développé par _blue_angels et son code source est librement accessible sur GitHub : https://github.com/ghosts-arch/bot-alomonia

📜 Licence MIT

Le bot est distribué sous la licence MIT, ce qui signifie que vous pouvez :
✅ Utiliser le code librement
✅ Modifier le code source
✅ Distribuer des copies du code original ou modifié
✅ Utiliser le projet à des fins commerciales

⚖️ La seule condition est de conserver la notice de copyright et une copie de la licence dans toutes les copies ou portions substantielles du logiciel.

🌟 Le code source est disponible pour tous - n'hésitez pas à contribuer au projet !
"""
        )
        await context.send(embed=embed)
