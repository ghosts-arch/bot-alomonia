from discord import TextStyle, SelectOption
import discord
from discord.ui import Modal, TextInput, Select

from src.core.client import LuneaMoon
from src.core.embeds import SuccessEmbed


class AddAdventCalendarBoxForm(Modal):

    def __init__(self) -> None:
        super().__init__(title="Ajouter une case au calendrier de l'avant")

        self.box_day_input = TextInput(
            label="Jour de la case",
            style=TextStyle.short,
        )

        self.category_input = TextInput(
            label="Catégorie de la case",
            style=TextStyle.short,
            min_length=4,
            max_length=256,
        )

        self.box_music_name_input = TextInput(
            label="Nom de la musique",
            style=TextStyle.short,
            min_length=4,
            max_length=256,
        )

        self.box_clues_input = TextInput(
            label="indices pour deviner la musique",
            style=TextStyle.short,
            min_length=4,
            max_length=256,
        )

        self.box_music_link_input = TextInput(
            label="Lien spotify de la musique",
            style=TextStyle.short,
            min_length=4,
            max_length=256,
        )

        self.add_item(self.box_day_input)
        self.add_item(self.category_input)
        self.add_item(self.box_music_name_input)
        self.add_item(self.box_clues_input)
        self.add_item(self.box_music_link_input)

    async def on_submit(self, interaction: discord.Interaction[LuneaMoon]):
        if not interaction.guild:
            raise Exception("This command can only be used in a guild")
        interaction.client.database.add_advent_calendar_box(
            day=self.box_day_input.value,
            category=self.category_input.value,
            description=self.box_music_name_input.value,
            link=self.box_music_link_input.value,
            clues=self.box_clues_input.value,
        )
        self.stop()
        embed = SuccessEmbed(
            title="La case suivante à été rajoutée",
            description=f"jour : {self.box_day_input.value}\nmusique : {self.box_music_name_input.value}\nindices : {self.box_clues_input.value}\nlien spotify : {self.box_music_link_input.value}",
        )
        await interaction.response.send_message(embed=embed)
