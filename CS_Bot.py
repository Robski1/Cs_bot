import discord
from discord.ext.commands import Bot
from discord.ext import commands
from constants import constants
import asyncio
import json
bot = commands.Bot(command_prefix = ".")
bot.remove_command("help")

class specification:
    def __init__(self, ctx, command, subtopic, index):
        self.ctx = ctx
        self.command = command
        self.subtopic = subtopic
        self.index = index

    async def showSpec(self):
        embed = discord.Embed(
                colour = discord.Colour.blurple(),
                description = "Here is part of the specification you have requested:",
                )
        embed.set_footer(text="Do .help for a list of commands")
        embed.set_image(url=constants.stuff[self.command][self.subtopic][self.index])
        embed.set_author(name=self.ctx.author.name, icon_url=self.ctx.author.avatar_url)
        await self.ctx.send(embed=embed)

@bot.event
async def on_ready():
    print("Bot is online ")

@bot.command()
async def spec (ctx, *args):
    command = specification(ctx, "spec", args[0], args[1])
    if args[0] == "algorithms":
        if args[1] == "1":
            await command.showSpec()

with open("token.txt","r") as token:
    token=token.read()
    bot.run(token)