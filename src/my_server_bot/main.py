import os
import sys

import discord
from dotenv import load_dotenv


def main() -> int:
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    intents = discord.Intents.all()
    bot = discord.Bot(intents=intents)

    @bot.event
    async def on_ready():
        args = sys.argv
        activity = discord.Game(name=args[1])
        await bot.change_presence(activity=activity)
        print("ready!")

    @bot.event
    async def on_message(message: discord.Message):
        # メッセージ送信者がBot(自分を含む)だった場合は無視する
        if message.author.bot:
            return

        # 招待コードの場合削除して招待コードチャンネルに再投稿
        if (
            "Steam://" in message.content
            or message.content.isdigit()
            and len(message.content) == 6
        ):
            await repost(message, "招待コード")

        # Steamリンクの場合、削除してSteamリンクチャンネルに再投稿
        if "https://store.steampowered.com/app/" in message.content:
            await repost(message, "steamリンク")

    bot.run(TOKEN)
    return 0


async def repost(message: discord.Message, channelName: str):
    # サーバーでの発言以外は無視する
    guild = message.guild
    if guild == None:
        return

    channel = discord.utils.find(lambda c: c.name == channelName, guild.channels)
    if isinstance(channel, discord.TextChannel):
        await channel.send(message.content)
        await message.delete()
