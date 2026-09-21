import discord


class SetStatusModal(discord.ui.Modal):
    def __init__(self, bot: discord.Bot, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs, title="ステータスの変更")
        self.bot = bot
        self.add_item(
            discord.ui.InputText(
                label="Status Content",
                style=discord.InputTextStyle.short,
                required=True,
            )
        )

    async def callback(self, interaction: discord.Interaction) -> None:
        content = self.children[0].value
        if content == None:
            await interaction.response.send_message(
                ephemeral=True, content="ステータスが設定されていません"
            )
            return

        activity = discord.Game(name=content)
        await self.bot.change_presence(activity=activity)

        await interaction.response.send_message(
            ephemeral=True, content="ステータスの変更に成功しました"
        )
