import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from cogs import music_cog, help_cog
import asyncio
import time

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

bot.remove_command('help')


@bot.command()
async def load_extensions(filename):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            print(f'Loaded: {filename}')
            time.sleep(0.2)
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start('TOKEN')


asyncio.run(main())
