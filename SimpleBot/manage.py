import asyncio
import os
import pathlib
import uuid
from pathlib import Path

import typer
import yaml
from pyfiglet import Figlet
from rich.console import Console
from rich.table import Table
from SimpleBot_Utils import SBProcManager, SimpleBotUtils

console = Console()

app = typer.Typer()

sbUtils = SimpleBotUtils()
procManager = SBProcManager()

path = Path(__file__).parents[0]
yamlConfig = os.path.join(str(path), "config.yaml")

uriConnection = ""

with open(yamlConfig, "r") as f:
    data = yaml.safe_load(f)
    if data["db"]["db_engine"] == "SQLite3":
        uriConnection = "sqlite+aiosqlite:///bots.db"
    elif data["db"]["db_engine"] == "PostgreSQL":
        uriConnection = f"postgresql+asyncpg://{data['db']['user']}:{data['db']['password']}@{data['db']['ip']}:{data['db']['port']}/{data['db']['database']}"
    elif data["db"]["db_engine"] == "MySQL":
        uriConnection = f"mysql+asyncmy://{data['db']['user']}:{data['db']['password']}@{data['db']['ip']}:{data['db']['port']}/{data['db']['database']}"


def main():
    pass


@app.command()
def info():
    """Prints info"""
    path = Path(__file__).parents[0]
    yamlConfig = os.path.join(str(path), "config.yaml")
    with open(yamlConfig, "r") as file:
        data = yaml.safe_load(file)
        f = Figlet(font="slant")
        print(f.renderText("SimpleBot"))
        console.print(f"Version: {data['version']}")
        console.print(f"Database Engine: {data['db']['db_engine']}")
        console.print("Author: No767")


@app.command()
def add(name: str, token: str):
    """Adds a bot to the DB"""
    botUUID = str(uuid.uuid4())
    asyncio.run(sbUtils.initTables(uri=uriConnection))
    asyncio.run(
        sbUtils.setToken(uuid=botUUID, name=name, token=token, uri=uriConnection)
    )
    print(f"Added {name}")


@app.command()
def delete(name: str):
    """Delets a bot from the DB"""
    mainRes = asyncio.run(sbUtils.obtainBot(name=name, uri=uriConnection))
    try:
        if len(mainRes) == 0:
            raise ValueError
        for items in mainRes:
            mainItems = dict(items)
            asyncio.run(sbUtils.deleteBot(uuid=mainItems["uuid"], uri=uriConnection))
        print(f"{name} has been deleted")
    except ValueError:
        print(
            f"There isn't any entries with the name of {name} in the DB. Please add the bot first."
        )


@app.command()
def update(name: str, token: str):
    """Updates the token for a bot in the DB"""
    mainRes = asyncio.run(sbUtils.obtainBot(name=name, uri=uriConnection))
    try:
        if len(mainRes) == 0:
            raise ValueError
        else:
            for items in mainRes:
                mainItems = dict(items)
                asyncio.run(
                    sbUtils.updateBotToken(
                        uuid=mainItems["uuid"], token=token, uri=uriConnection
                    )
                )
            print(f"{name} has been updated")
    except ValueError:
        print(
            f"There isn't any entries with the name of {name} in the DB. Please add the bot first."
        )


@app.command()
def view_all():
    """Views all of the bots in the DB"""
    mainRes = asyncio.run(sbUtils.obtainAllBots(uri=uriConnection))
    try:
        if len(mainRes) == 0:
            raise ValueError
        else:
            table = Table(title="Bots")
            console = Console()
            table.add_column("Bot Name", justify="center", no_wrap=True)
            table.add_column("Bot Token", justify="center", no_wrap=True)

            for items in mainRes:
                mainItems = dict(items)
                table.add_row(mainItems["name"], mainItems["token"])

            console.print(table)
    except ValueError:
        print("There are no entries in the DB. Please add the bot first.")


@app.command()
def view_one(name: str):
    """Views one of the bots in the DB"""
    mainRes = asyncio.run(sbUtils.obtainBot(name=name, uri=uriConnection))
    try:
        if len(mainRes) == 0:
            raise ValueError
        else:
            table = Table(title="Bot")
            console = Console()
            table.add_column("Bot Name", justify="center", no_wrap=True)
            table.add_column("Bot Token", justify="center", no_wrap=True)

            for items in mainRes:
                mainItems = dict(items)
                table.add_row(mainItems["name"], mainItems["token"])

            console.print(table)
    except ValueError:
        print(
            f"There isn't any entries with the name of {name} in the DB. Please add the bot first."
        )


@app.command()
def start(
    name: str = typer.Argument(
        default=None, help="The name of the bot you wish to start up"
    )
):
    """Starts the bot of your choice"""
    mainRes = asyncio.run(sbUtils.obtainBot(name=name, uri=uriConnection))
    try:
        if len(mainRes) == 0:
            raise ValueError
        else:
            filePath = os.path.exists(
                os.path.join(pathlib.Path(__file__).parents[0], "Logs")
            )
            if filePath is False:
                os.mkdir(os.path.join(pathlib.Path(__file__).parents[0], "Logs"))
            for items in mainRes:
                mainItems = dict(items)
            botToken = mainItems["token"]
            print(f"Booting {name}...")
            procManager.boot(name, botToken)
    except ValueError:
        print(
            f"There are no bots named {name} within the DB. Please add the bot first."
        )


@app.command()
def stop(bot_name: str):
    """Stops the bot"""
    procManager.stop(bot_name)
    print(f"{bot_name} stopped")


if __name__ == "__main__":
    app()
