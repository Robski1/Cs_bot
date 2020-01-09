import discord
from discord.ext.commands import Bot
from discord.ext import commands
from constants import constants
import asyncio
bot = commands.Bot(command_prefix = ".")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot is online ")






with open("token.txt","r") as token:
    token=token.read()
    bot.run(token)