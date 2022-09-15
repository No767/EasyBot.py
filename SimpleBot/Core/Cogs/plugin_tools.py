import random

import discord
from discord.commands import slash_command
from discord.ext import commands


class PluginUtils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="ping", description="Pings the bot")
    async def pingBot(self, ctx):
        await ctx.respond(
            embed=discord.Embed(
                description=f"Ping >> {round(self.bot.latency * 1000)} ms"
            )
        )

    @slash_command(name="invite", description="Makes an invite link for your bot")
    async def inviteBot(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(
                random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            )
        )
        embed.title = f"Invite {self.bot.user.name} to your server"
        embed.description = f"https://discord.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot&permissions=8"
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(PluginUtils(bot))
