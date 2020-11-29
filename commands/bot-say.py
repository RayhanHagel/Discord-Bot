from discord.ext import commands
import discord


class Say(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def say(self, ctx, *, message):
        embed = discord.Embed(title=f':loudspeaker:  {message}')
        embed.set_footer(text="Command invoked by {}".format(ctx.message.author.name))
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Say(client))
