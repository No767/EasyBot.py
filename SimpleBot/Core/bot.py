import logging
import os
import sys
from pathlib import Path
from time import strftime

import discord
from discord.ext import commands

path = Path(__file__).parents[0]
sys.path.append(str(path))

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
    logging.info("Your bot is fully ready!")
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="/help")
    )


def main(token: str):
    """The entrypoint of the bot

    Args:
        token (str): Discord Bot Token
    """
    try:
        cogsList = os.listdir(os.path.join(str(path), "Cogs"))
        for items in cogsList:
            if items.endswith(".py"):
                bot.load_extension(f"Cogs.{items[:-3]}", store=False)
        bot.run(token)
    except KeyboardInterrupt:
        logging.info("Shutting down...")
        sys.exit(0)
