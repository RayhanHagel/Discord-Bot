from discord.ext import commands
import discord
import datetime
import os


class Load(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def load(self, ctx):
        if ctx.author.id == 345576668020080640:
            for filename in os.listdir(r'./commands'):
                if filename.endswith('.py'):
                    try:
                        self.client.load_extension(f'commands.{filename[:-3]}')
                    except Exception:
                        continue
            embed = discord.Embed(title=f':lock:  Done loading modules ...',
                                  timestamp=datetime.datetime.now(datetime.timezone.utc))
            await ctx.send(embed=embed)
        else:
            pass

    @commands.command()
    async def reload(self, ctx):
        if ctx.author.id == 345576668020080640:
            for filename in os.listdir(r'./commands'):
                if filename.endswith('.py'):
                    self.client.unload_extension(f'commands.{filename[:-3]}')
                    try:
                        self.client.load_extension(f'commands.{filename[:-3]}')
                    except Exception:
                        continue
            embed = discord.Embed(title=f':lock:  Done reloading modules ...',
                                  timestamp=datetime.datetime.now(datetime.timezone.utc))
            await ctx.send(embed=embed)
        else:
            pass

def setup(client):
    client.add_cog(Load(client))
    
# Hageru-Ray
