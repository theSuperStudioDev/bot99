import discord
from discord.ext import commands

# Set your bot's token here
TOKEN = 'MTA2Mzk5ODEzMTIxNTI5MDM4OA.G4IM4i.dzcvnmtZvq49Tw2DLR0DCDLJ226j7XZjj0Jtis'

# Set the command prefix
bot = commands.Bot(command_prefix='!')

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Hello
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

# Run the bot
bot.run(TOKEN)
