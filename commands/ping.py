import datetime
from discord.ext import commands
import discord


class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['p'])
    async def ping(self, ctx):
        latency = round(self.client.latency * 1000)
        embed = discord.Embed(title=f':heart: {latency} ms\n',
                              timestamp=datetime.datetime.now(datetime.timezone.utc))
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Ping(client))
