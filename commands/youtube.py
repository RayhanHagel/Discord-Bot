from discord.ext import commands
import urllib.request
import discord
import re
import datetime


class Youtube(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['yt'])
    async def youtube(self, ctx, *, search):
        search = search.replace(' ', '+')
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
        link = re.findall(r"watch\?v=(\S{11})", html.read().decode())

        embed = discord.Embed(title=f':computer:  Top Search Result',
                              url=f'https://www.youtube.com/watch?v={link[0]}',
                              timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_footer(text=f'Youtube')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Youtube(client))

# Hageru-Ray
