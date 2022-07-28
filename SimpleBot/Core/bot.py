import logging
import os
import pathlib
import sys
from time import strftime

import discord
from discord.ext import commands

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] | %(asctime)s >> %(message)s",
    datefmt="[%m/%d/%Y] [%I:%M:%S %p %Z]",
    handlers=[
        logging.FileHandler(filename=f"./Logs/{strftime('%Y-%m-%d_%H-%M-%S')}.log"),
        logging.StreamHandler(),
    ],
)

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents, help_command=None)


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="/help")
    )


def main(token: str):
    """The entrypoint of the bot

    Args:
        token (str): Discord Bot Token
    """
    try:
        cogs = [
            f"{f[:-3]}"
            for f in os.listdir(os.path.join(pathlib.Path(__file__).parents[0], "Cogs"))
            if f.endswith(".py")
        ]
        for extensions in cogs:
            bot.load_extension(extensions)
        bot.run(token)
    except KeyboardInterrupt:
        logging.info("Shutting down...")
        sys.exit(0)
