from discord.ext import commands
import discord
import datetime
import wikipediaapi


class Wikipedia(commands.Cog):

    def __init__(self, client):
        self.client = client
 
    @commands.command()
    async def wiki(self, ctx, *, search):
        wiki = wikipediaapi.Wikipedia('en')
        page = wiki.page(search)
        dot = page.summary.find('\n')
        
        embed = discord.Embed(title=page.title.capitalize(),
                              url=page.fullurl,
                              description=page.summary[0:dot].replace(page.title, f'**{page.title}**').replace(page.title.lower(), f'**{page.title.lower()}**'),
                              timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_footer(text=f'Wikipedia Article')
        await ctx.send(embed=embed)
        
        
def setup(client):
    client.add_cog(Wikipedia(client))

# Hageru-Ray
