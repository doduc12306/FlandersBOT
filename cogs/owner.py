import aiohttp
import settings.config
import discord

from discord.ext import commands

class Owner():

    def __init__(self, bot):
        self.bot = bot

    # Change the bot's avatar
    @commands.command()
    async def avatar(self, ctx, avatarUrl):
        if ctx.message.author.id == settings.config.OWNERID:
            async with aiohttp.ClientSession() as aioClient:
                async with aioClient.get(avatarUrl) as resp:
                    newAvatar = await resp.read()
                    await self.bot.user.edit(avatar=newAvatar)
                    await ctx.send('Avatar changed!')

    # Change the bot's status/presence
    @commands.command()
    async def status(self, ctx, *, message : str):
        if ctx.message.author.id == settings.config.OWNERID:
            await self.bot.change_presence(game=discord.Game(name=message,
                                                             type=0))

    # Sends a list of the guilds the bot is active in - usable by the bot owner
    @commands.command()
    async def serverlist(self, ctx):
        if ctx.message.author.id == settings.config.OWNERID:
            guildList = ""
            for guild in self.bot.guilds:
                guildList += guild.name + '\n'
            await ctx.author.send(guildList)

    # Shuts the bot down - usable by the bot owner
    @commands.command()
    async def shutdown(self, ctx):
        if ctx.message.author.id == settings.config.OWNERID:
            await self.bot.logout()
            await self.bot.close()

def setup(bot):
    bot.add_cog(Owner(bot))
