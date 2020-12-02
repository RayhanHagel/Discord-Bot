# Player ID Finder by @Hageru-Ray
from discord.ext import commands
import discord
import datetime


class Player_ID(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def id(self, ctx, args=None):
        if args is None:
            embed = discord.Embed(title=f':zap: {ctx.author.name} \n:sparkles: {ctx.author.id} \n',
                                  timestamp=datetime.datetime.now(datetime.timezone.utc))
            await ctx.send(embed=embed, delete_after=10)
        elif args.find("<@!") != -1:
            embed = discord.Embed(title=f':sparkles: {args.replace("<@!", "").replace(">", "")} \n',
                                  timestamp=datetime.datetime.now(datetime.timezone.utc))
            await ctx.send(embed=embed)
        else:
            pass


def setup(client):
    client.add_cog(Player_ID(client))

# Hageru-Ray
