from discord.commands import slash_command
from discord.ext import commands


class MainTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name="maintest",
        description="it's just a test command",
    )
    async def testing(self, ctx):
        await ctx.respond("test")


def setup(bot):
    bot.add_cog(MainTest(bot))
