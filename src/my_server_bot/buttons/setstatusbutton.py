import discord

from my_server_bot.modal import setstatusmodal


class SetStatusButton(discord.ui.View):
    def __init__(self, bot: discord.Bot) -> None:
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label="BOTステータス変更", style=discord.ButtonStyle.green)
    async def set_status(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ) -> None:
        await interaction.response.send_modal(setstatusmodal.SetStatusModal(self.bot))
