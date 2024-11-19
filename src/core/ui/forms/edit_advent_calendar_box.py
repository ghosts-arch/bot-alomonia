from discord import TextStyle, SelectOption
import discord
from discord.ui import Modal, TextInput, Select

from src.core.client import LuneaMoon
from src.core.embeds import SuccessEmbed


class EditAdventCalendarBoxForm(Modal):

    def __init__(self, advent_calendar_box) -> None:
        super().__init__(title="Editer une case au calendrier de l'avant")
        self._advent_calendar_box = advent_calendar_box

        self.box_day_input = TextInput(
            label="Jour de la case",
            style=TextStyle.short,
            default=self._advent_calendar_box.day,
        )

        self.category_input = TextInput(
            label="Catégorie de la case",
            style=TextStyle.short,
            min_length=4,
            max_length=256,
            default=self._advent_calendar_box.category,
            placeholder=f"{self._advent_calendar_box.category} (music, video_game, movie)",
        )

        self.box_music_name_input = TextInput(
            label="Nom de la musique",
            style=TextStyle.short,
            min_length=4,
            max_length=256,
            default=self._advent_calendar_box.description,
        )

        self.box_clues_input = TextInput(
            label="indices pour deviner la musique",
            style=TextStyle.short,
            min_length=4,
            max_length=256,
            default=self._advent_calendar_box.clues,
        )

        self.box_music_link_input = TextInput(
            label="Lien spotify de la musique",
            style=TextStyle.short,
            min_length=4,
            max_length=256,
            default=self._advent_calendar_box.link,
        )

        self.add_item(self.box_day_input)
        self.add_item(self.category_input)
        self.add_item(self.box_music_name_input)
        self.add_item(self.box_clues_input)
        self.add_item(self.box_music_link_input)

    async def on_submit(self, interaction: discord.Interaction[LuneaMoon]):
        if not interaction.guild:
            raise Exception("This command can only be used in a guild")
        interaction.client.database.edit_advent_calent_box(
            day=self.box_day_input.value,
            category=self.category_input.value,
            description=self.box_music_name_input.value,
            link=self.box_music_link_input.value,
            clues=self.box_clues_input.value,
        )
        self.stop()
        embed = SuccessEmbed(
            title="La case suivante à été modifiée",
            description=f"jour : {self.box_day_input.value}\nmusique : {self.box_music_name_input.value}\nindices : {self.box_clues_input.value}\nlien spotify : {self.box_music_link_input.value}",
        )
        await interaction.response.send_message(embed=embed)
