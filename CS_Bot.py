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

# class cheat:
#     def __init__(self,ctx):
#         self.ctx = ctx
#     async def showCheatsheet(self):
#         await self.ctx.send("Here is the cheat sheet:")
#         for i in range(1,5):
#             embed = discord.Embed(
#                     colour = discord.Colour.red(),
#                     )
#             embed.set_footer(text="Do .help for a list of commands")
#             embed.set_image(url=constants.stuff["cheatsheet"]["{0}".format(i)])
#             embed.set_author(name=self.ctx.author.name, icon_url=self.ctx.author.avatar_url)
#             await self.ctx.send(embed=embed)
        

@bot.event
async def on_ready():
    print("Bot is online ")

@bot.command()
async def spec (ctx, *args):
    command = specification(ctx, "spec", args[0], args[1])
    try:
        await command.showSpec()
    except:
        embed = discord.Embed(
                colour = discord.Colour.blurple(),
                description = "Invalid command! Please do .help for a list of valid commands.",
                )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@bot.command()
async def cheatsheet(ctx):
    embed = discord.Embed(
                colour = discord.Colour.blurple(),
                description = "Here is the cheatsheet\n https://cdn.discordapp.com/attachments/487334311389954060/642074871039524885/CS_Cheat_Sheet_UPDATED.pdf",
                
                )
    await ctx.send(embed=embed)

    # command = cheat(ctx)
    # try:
    #     await command.showCheatsheet()
    # except:
    #     embed = discord.Embed(
    #             colour = discord.Colour.blurple(),
    #             description = "Invalid command! Please do /help for a list of valid commands.",
    #             )
    #     embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    #     await ctx.send(embed=embed)
    
with open("token.txt","r") as token:
    token=token.read()
    bot.run(token)
