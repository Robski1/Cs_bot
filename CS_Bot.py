import discord
from discord.ext.commands import Bot
from discord.ext import commands
from constants import constants
import asyncio
import json
import random
from datetime import datetime, time

bot = commands.Bot(command_prefix = ".", case_insensitive=True)
bot.remove_command("help")

#### SPECIFICATION CLASS ####

class specification:
    def __init__(self, ctx, command, subtopic, index):
        self.ctx = ctx
        self.command = command
        self.subtopic = subtopic
        self.index = index

    async def showSpec(self):
        embed = discord.Embed(
                colour = discord.Colour.teal(),
                description = "Here is part of the specification you have requested:",
                )
        embed.set_footer(text="Do .help for a list of commands")
        embed.set_image(url=constants.stuff[self.command][self.subtopic][self.index])
        embed.set_author(name=self.ctx.author.name, icon_url=self.ctx.author.avatar_url)
        await self.ctx.send(embed=embed)

#### EXAM_QUESTIONS CLASS ####

class Exam_Questions:
    def __init__(self, ctx, topic, number):
        self.ctx = ctx
        self.topic = topic
        self.number = number

    async def ShowQuestion(self):
        embed = discord.Embed(
                colour = discord.Colour.teal(),
                description = "Question:"
                )
        embed.set_footer(text="Do .help for a list of commands")
        embed.set_image(url=constants.stuff["Questions"][self.topic]["Question"][self.number])
        embed.set_author(name=self.ctx.author.name, icon_url=self.ctx.author.avatar_url)
        await self.ctx.send(embed=embed)

        embed = discord.Embed(
                colour = discord.Colour.teal(),
                description = "Answer:\n Click to on link to reveal after attempting question.\n" + constants.stuff["Questions"][self.topic]["Answer"][self.number]
                )
        embed.set_footer(text="Do .help for a list of commands")
        # embed.set_image(url=constants.stuff["Questions"][self.topic]["Answer"][self.number])
        embed.set_author(name=self.ctx.author.name, icon_url=self.ctx.author.avatar_url)
        await self.ctx.send(embed=embed)

#### ERROR MESSAGE ####

async def errorMsg(ctx):
    embed = discord.Embed(
            colour = discord.Colour.red(),
            description = ":no_entry_sign: Invalid command! Please do .help for a list of valid commands.",
            )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

#### ON READY ####

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(".help"))
    print("Bot is online ")

#### SPEC COMMAND ####

@bot.command()
async def spec(ctx, *args):
    try:
        command = specification(ctx, "spec", args[0].lower(), args[1])
        await command.showSpec()
    except:
        return await errorMsg(ctx)

#### QUESTION COMMAND ####

@bot.command()
async def question(ctx, *args):
    try:
        number = str(random.randint(1, (len(constants.stuff["Questions"][args[0].lower()]["Question"]))-1))
        command = Exam_Questions(ctx, args[0].lower(), number)
        await command.ShowQuestion()
    except:
        return await errorMsg(ctx)

#### CHEATSHEET COMMAND ####

@bot.command()
async def cheatsheet(ctx):
    embed = discord.Embed(
            colour = discord.Colour.teal(),
            description = "Here is the cheatsheet: "+constants.stuff["cheatsheet"]["5"],
            )
    await ctx.send(embed=embed)

#### HELP COMMAND ####

@bot.command()
async def help(ctx, *args):
    if len(args) < 1 or args[0] == "1":
        embed = discord.Embed(
                colour = discord.Colour.blue(),
                description = "<@{0}> We have sent you a list of commands! Please check your DMs.".format(ctx.author.id),
                )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        
        embed = discord.Embed(
                colour = discord.Colour.blue(),
                description = "**Here is a list of all the commands!**\n\n**.spec**\n`EXAMPLE: .spec algorithms 1`\n`Do .help spec to view subcommands in .spec`\n\n**.question**\n`EXAMPLE: .question programming`\n`Do .help question to view subcommands in .question`\n\n**.cheatsheet**\n`See the cheatsheet`\n\n**.help**\n `EXAMPLE: .help question`\n`View help page for the different help commands`",
                )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.author.send(embed=embed)
    
    elif args[0].upper() == "QUESTION":
            if len(args) == 1:
                embed = discord.Embed(
                        colour = discord.Colour.blue(),
                        description = "<@{0}> We have sent you a list of commands! Please check your DMs.".format(ctx.author.id),
                        )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)

                embed = discord.Embed(
                        colour=discord.Colour.blue(),
                        title="The topics are:",
                        description="1) algorithms\n2) programming\n3) data_rep\n4) comp_systems\n5) comp_networks\n6) cyber\n7) ele\n\n`Do .question [topic] to recieve a random question based on the chosen topic`\n"
                )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.author.send(embed=embed)
            else:
                return await errorMsg(ctx)

    elif args[0].upper() == "SPEC":
        if len(args) == 2:
            if args[1].upper() == "ALGORITHMS":
                embed = discord.Embed(
                        colour=discord.Colour.blue(),
                        title="The subcommands for .spec algorithms:",
                        description="**.spec algorithms 1**\tRepresenting algorithms\n**.spec algorithms 2**\tEfficiency of algorithms\n**.spec algorithms 3**\tSearching algorithms\n**.spec algorithms 4**\tSorting algorithms"
                        )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.author.send(embed=embed)
            
            elif args[1].upper() == "PROGRAMMING":
                embed = discord.Embed(
                        colour=discord.Colour.blue(),
                        title="The subcommands for .spec programming:",
                        description="""**.spec programming 1**\tData types\n**.spec programming 2**\tProgramming concepts\n**.spec programming 3**\tArithmetic operations\n**.spec programming 4**\tRelational operations
                                    **.spec programming 5**\tBoolean operations\n**.spec programming 6**\tData structures\n**.spec programming 7**\tInput/output and file handling\n**.spec programming 8**\tString handling operations
                                    **.spec programming 9**\tRandom number generation\n**.spec programming 10**\tSubroutines (procedures/functions)\n**.spec programming 11**\tStructured programming\n**.spec programming 12**\tRobust and secure programming
                                    **.spec programming 13**\tClassifications of programming languages
                                    """
                        )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.author.send(embed=embed)
            
            elif args[1].upper() == "DATA_REP":
                embed = discord.Embed(
                        colour=discord.Colour.blue(),
                        title="The subcommands for .spec data_rep:",
                        description="""**.spec data_rep 1**\tNumber bases\n**.spec data_rep 2**\tConverting between number bases\n**.spec data_rep 3**\tUnits of information\n**.spec data_rep 4**\tBinary arithmetic
                                    **.spec data_rep 5**\tCharacter encoding\n**.spec data_rep 6**\tRepresenting images\n**.spec data_rep 7**\tRepresenting sound\n**.spec data_rep 8**\tData compression
                                    """
                        )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.author.send(embed=embed)

            elif args[1].upper() == "COMP_SYSTEMS":
                embed = discord.Embed(
                        colour=discord.Colour.blue(),
                        title="The subcommands for .spec comp_systems:",
                        description="""**.spec comp_systems 1**\tHardware and software\n**.spec comp_systems 2**\tBoolean logic\n**.spec comp_systems 3**\tSoftware classification\n**.spec comp_systems 4**\tSystem architecture
                                    **.spec comp_systems 5**\tSystem architecture (2)
                                    """
                        )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.author.send(embed=embed)

            elif args[1].upper() == "COMP_NETWORKS":
                embed = discord.Embed(
                        colour=discord.Colour.blue(),
                        title="The subcommands for .spec comp_networks:",
                        description="**.spec comp_networks 1**\tFundamentals of computer networks\n**.spec comp_networks 2**\tFundamentals of computer networks (2)\n**.spec comp_networks 3**\tFundamentals of computer networks (3)"
                        )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.author.send(embed=embed)

            elif args[1].upper() == "CYBER_SECURITY":
                embed = discord.Embed(
                        colour=discord.Colour.blue(),
                        title="The subcommands for .spec cyber_security:",
                        description="**.spec cyber_security 1**\tFundamentals of cyber security"
                        )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.author.send(embed=embed)

            elif args[1].upper() == "CYBER_THREATS":
                embed = discord.Embed(
                        colour=discord.Colour.blue(),
                        title="The subcommands for .spec cyber_threats:",
                        description="**.spec cyber_threats 1**\tCyber security threats\n**.spec cyber_threats 2**\tSocial engineering\n**.spec cyber_threats 3**\tMalicious code\n**.spec cyber_threats 4**\tMethods to detect and prevent cyber security threats"
                                    
                        )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.author.send(embed=embed)

            elif args[1].upper() == "ELE":
                embed = discord.Embed(
                        colour=discord.Colour.blue(),
                        title="The subcommands for .spec data_rep:",
                        description="**.spec ele 1**\tEthical, legal and environmental impacts of digital technology on wider society, including issues of privacy"
                        )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.author.send(embed=embed)

            else:
                return await errorMsg(ctx)
        else:
            if len(args) == 1:
                embed = discord.Embed(
                        colour = discord.Colour.blue(),
                        description = "<@{0}> We have sent you a list of commands! Please check your DMs.".format(ctx.author.id),
                        )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)

                embed = discord.Embed(
                        colour=discord.Colour.blue(),
                        title="The topics are:",
                        description="1) algorithms\n2) programming\n3) data_rep\n4) comp_systems\n5) comp_networks\n6) cyber_security\n7) cyber_threats\n 8) ele\n\n`Do .help spec [topic] to view commands for each topic`\n`EXAMPLE: .help spec algorithms`"
                )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                await ctx.author.send(embed=embed)
            else:
                return await errorMsg(ctx)

    else:
        return await errorMsg(ctx)

#### TimeLeft till first CS exam   ####

async def timeLeft():
    
    
    await asyncio.sleep(5)
    channel = bot.get_channel(665690248646492191)
    print(channel)
    
    async def dateDiffInSeconds(date1, date2):
        timedelta = date2 - date1
        return timedelta.days * 24 * 3600 + timedelta.seconds

    async def daysHoursMinutesSecondsFromSeconds(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        return (days, hours, minutes, seconds)
    
    hourArr = ['16','17']
    minArr = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']
        
    randHour = random.randint(0,len(hourArr)-1)
    randMin = random.randint(0,len(minArr)-1)
    randTime = hourArr[randHour]+ ':' + minArr[randMin]   
    print(randTime)
    
    msgSent = False
    
    while True:
        
        while not msgSent:
            leaving_date = datetime.strptime('11-05-2020 09:00:00', '%d-%m-%Y %H:%M:%S')
            now =  datetime.now()
            dateFormat = await daysHoursMinutesSecondsFromSeconds(await dateDiffInSeconds(now, leaving_date))

            setTime = str(now)
            setTime = setTime[11:16]

            if setTime == randTime:
                timeLeft = ('@everyone ' + ("%d days, %d hours, %d minutes, %d seconds") % dateFormat)+ ' left till CS Paper 1'
                embed = discord.Embed(
                colour = discord.Colour.red(),
                description = timeLeft,
                )
                await channel.send(embed=embed)
                msgSent = True
            
            await asyncio.sleep(10)


        now = datetime.now()   
        setTime = str(now)
        setTime = setTime[11:16]

        if setTime == '15:30':
            
            randHour = random.randint(0,len(hourArr)-1)
            randMin = random.randint(0,len(minArr)-1)
            randTime = hourArr[randHour]+ ':' + minArr[randMin]  
            print(randTime)
            
            msgSent = False
          
        
        await asyncio.sleep(10)

async def BREXIT():
    brexitTime = '31-01-2020 10:59'
    msgSent = False
    while not msgSent:
        now = datetime.now()
        strTime = str(now)
        noSec = strTime[:16]

        if noSec == brexitTime:
            timeLeft = ('@everyone Brexit has come! renew your visas at https://visas-immigration.service.gov.uk/alt-language-selection-skip-visa'
            embed = discord.Embed(
            colour = discord.Colour.red(),
            description = timeLeft,
            )
            await channel.send(embed=embed)
            msgSent = True
        
        await aysncio.sleep(10)
bot.loop.create_task(timeLeft())
bot.loop.create_task(BREXIT())
#### RUN TOKEN ####

with open("token.txt", "r") as token:
    token = token.read()
    bot.run(token)
