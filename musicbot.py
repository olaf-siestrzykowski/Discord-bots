import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
import time

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents, help_command=None)

bot.remove_command('help')


@bot.event
async def on_ready():
    print('Bot is online')


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            print('Loaded: ' + filename)
            await bot.load_extension("cogs." + filename[:-3])
        else:
            print('unable to load extension'+filename)


async def main():
    await load()
    await bot.start(TOKEN)
#bot.run(TOKEN)

asyncio.run(main())