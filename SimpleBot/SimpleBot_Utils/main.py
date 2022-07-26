from sqlalchemy import Column, String, Text, delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class DiscordBots(Base):

    __tablename__ = "discord_bots"

    uuid = Column(String, primary_key=True)
    name = Column(String)
    token = Column(Text)

    def __iter__(self):
        yield "uuid", self.uuid
        yield "name", self.name
        yield "token", self.token

    def __repr__(self):
        return (
            f"DiscordBots(uuid={self.uuid!r}, name={self.name!r}, token={self.token!r})"
        )


class SimpleBotUtils:
    def __init__(self):
        self.self = self

    async def initTables(self, uri: str):
        """Init the DB tables

        Args:
            uri (str): URI of the SQLite3 DB connection
        """
        engine = create_async_engine(uri)
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def setToken(self, uuid: str, name: str, token: str, uri: str):
        """Set's the name and token for the bot

        Args:
            uuid (str): UUID of the bot
            name (str): Name of the bot
            token (str): Discord Bot Token
            uri (str): URI of the SQLite3 DB connection
        """
        engine = create_async_engine(uri)
        async_session = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )
        async with async_session() as session:
            async with session.begin():
                tokenItem = DiscordBots(uuid=uuid, name=name, token=token)
                session.add_all([tokenItem])
                await session.commit()

    async def obtainBot(self, name: str, uri: str):
        """Obtains the info for the bot

        Args:
            name (str): Name of the bot
            uri (str): URI of the SQLite3 DB connection
        """
        engine = create_async_engine(uri)
        async_session = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )
        async with async_session() as session:
            async with session.begin():
                selectItem = select(DiscordBots).filter(DiscordBots.name == name)
                res = await session.execute(selectItem)
                return [row for row in res.scalars()]

    async def obtainAllBots(self, uri: str):
        """Prints out all of the bots in the DB

        Args:
            uri (str): URI of the SQLite3 DB connection
        """
        engine = create_async_engine(uri)
        async_session = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )
        async with async_session() as session:
            async with session.begin():
                selectItem = select(DiscordBots)
                res = await session.execute(selectItem)
                return [row for row in res.scalars()]

    async def deleteBot(self, uuid: str, uri: str):
        """Removes a bot from the DB

        Args:
            uuid (str): Discord Bot UUID
            uri (str): URI of the SQLite3 DB connection
        """
        engine = create_async_engine(uri)
        async_session = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )
        async with async_session() as session:
            async with session.begin():
                deleteItem = delete(DiscordBots).filter(DiscordBots.uuid == uuid)
                await session.execute(deleteItem)
                await session.commit()

    async def updateBotToken(self, uuid: str, token: str, uri: str):
        """Updates a bot's token in the DB

        Args:
            uuid (str): Discord Bot UUID
            token (str): New Discord Bot Token
            uri (str): URI of the SQLite3 DB connection
        """
        engine = create_async_engine(uri)
        async_session = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )
        async with async_session() as session:
            async with session.begin():
                updateItem = update(
                    DiscordBots, values={DiscordBots.token: token}
                ).filter(DiscordBots.uuid == uuid)
                await session.execute(updateItem)
                await session.commit()
