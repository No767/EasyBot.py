from discord.commands import slash_command
from discord.ext import commands


class MainTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name="test",
        description="it's just a test command",
        guild_ids=[866199405090308116],
    )
    async def testing(self, ctx):
        await ctx.respond("test")


def setup(bot):
    bot.add_cog(MainTest(bot))
