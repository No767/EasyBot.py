import logging
import sys
import time

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] | %(asctime)s >> %(message)s",
    datefmt="[%m/%d/%Y] [%I:%M:%S %p %Z]",
)


def main(token):
    try:
        while True:
            time.sleep(3)
            print(token)
    except KeyboardInterrupt:
        print("Shutting down...")
        sys.exit(0)
    # intents = discord.Intents.default()
    # intents.members = True
    # bot = commands.Bot(command_prefix=".", intents=intents, help_command=None)
    # bot.run()
