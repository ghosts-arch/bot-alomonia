import discord

import src.core.client as client
from src.core.embeds import SuccessEmbed, ErrorEmbed
from src.core.ui.buttons import CancelationButton, ConfirmationButton


class DeleteAdventCalendarBoxView(discord.ui.View):
    def __init__(self, advent_calendar_box):
        super().__init__()
        cancel_button = CancelationButton(
            label="Annuler",
            custom_id="cancel_delete_advent_calendar_box",
            callback=self.on_cancel,
        )
        self.add_item(cancel_button)
        confirmation_button = ConfirmationButton(
            label="Supprimer",
            custom_id=f"confirm_delete_rule_{advent_calendar_box.day}",
            callback=self.on_confirm,
        )
        self.add_item(confirmation_button)

    async def on_cancel(self, interaction: discord.Interaction):
        await interaction.response.defer()
        await interaction.delete_original_response()
        await interaction.channel.send(
            embed=ErrorEmbed(description=f"Annulation de la commande ❌")
        )

    async def on_confirm(self, interaction: discord.Interaction[client.LuneaMoon]):
        await interaction.response.defer()
        await interaction.delete_original_response()
        if not interaction.data:
            raise Exception("No data")
        if not interaction.data.get("custom_id"):
            raise Exception("No custom id")
        custom_id = interaction.data.get("custom_id")
        if type(custom_id) != str:
            raise Exception("custom id must be a string")
        box_day = custom_id.split("_")[-1]
        box = interaction.client.database.delete_advent_calendar_box(day=box_day)
        await interaction.channel.send(
            embed=SuccessEmbed(description=f"case suprimée ")
        )
