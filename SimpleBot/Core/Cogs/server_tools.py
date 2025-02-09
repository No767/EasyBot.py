import discord
from discord.commands import Option, SlashCommandGroup
from discord.ext import commands


class ServerUtils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    info = SlashCommandGroup("info", "Info about servers, etc")

    @info.command(name="server")
    async def serverInfo(self, ctx):
        """Provides information about the server"""
        embed = discord.Embed()
        embed.title = ctx.guild.name
        embed.description = ctx.guild.description
        embed.add_field(
            name="Created At (UTC)",
            value=ctx.guild.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            inline=True,
        )
        embed.add_field(
            name="Categories",
            value=[item.name for item in ctx.guild.categories],
            inline=True,
        )
        embed.add_field(
            name="Number of Text Channels",
            value=len(ctx.guild.text_channels),
            inline=True,
        )
        embed.add_field(
            name="Number of Voice Channels",
            value=len(ctx.guild.voice_channels),
            inline=True,
        )
        embed.add_field(
            name="Forum Channels",
            value=[item.name for item in ctx.guild.forum_channels],
            inline=True,
        )
        embed.add_field(name="Server Features", value=ctx.guild.features, inline=True)
        embed.add_field(name="Member Count", value=ctx.guild.member_count, inline=True)
        embed.add_field(name="Server Owner", value=ctx.guild.owner.name, inline=True)
        embed.add_field(
            name="Roles", value=[item.name for item in ctx.guild.roles][1:], inline=True
        )
        embed.set_thumbnail(url=ctx.guild.icon.url)
        await ctx.respond(embed=embed)

    @info.command(name="user")
    async def getUserInfo(
        self, ctx, *, user: Option(discord.Member, "The user to get the info of")
    ):
        """Gets info about the requested user"""
        embed = discord.Embed()
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.title = user.display_name
        embed.add_field(
            name="On Nitro Since (UTC)",
            value=user.premium_since.strftime("%Y-%m-%d %H:%M:%S")
            if user.premium_since is not None
            else None,
            inline=True,
        )
        embed.add_field(
            name="Account Creation Date (UTC)",
            value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            inline=True,
        )
        embed.add_field(
            name="Server Join Date (UTC)",
            value=user.joined_at.strftime("%Y-%m-%d %H:%M:%S")
            if user.joined_at is not None
            else None,
            inline=True,
        )
        embed.add_field(
            name="Timeout Since",
            value=user.communication_disabled_until.strftime("%Y-%m-%d %H:%M:%S")
            if user.communication_disabled_until is not None
            else None,
            inline=True,
        )
        embed.add_field(
            name="Roles",
            value=str([roleName.name for roleName in user.roles][1:]).replace("'", ""),
            inline=True,
        )
        embed.add_field(name="Desktop Status", value=user.desktop_status, inline=True)
        embed.add_field(name="Web Status", value=user.web_status, inline=True)
        embed.add_field(name="On Mobile?", value=user.is_on_mobile(), inline=True)
        embed.add_field(name="Bot?", value=user.bot, inline=True)
        embed.add_field(name="Top Role", value=user.top_role.name, inline=True)
        embed.add_field(
            name="Mutual Guilds",
            value=str([guilds.name for guilds in user.mutual_guilds]).replace("'", ""),
            inline=True,
        )
        embed.add_field(name="Guild Nickname", value=user.nick, inline=True)
        embed.add_field(name="On Timeout?", value=user.timed_out, inline=True)
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(ServerUtils(bot))
