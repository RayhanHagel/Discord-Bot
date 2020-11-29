from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from googlesearch import search


class Brainly(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['br'])
    async def brainly(self, ctx, *, target):
        for results in search(target, tld="co.id", num=10, stop=10, pause=2):
            if results.find('brainly') != -1:
                page = requests.get(results)
                soup = BeautifulSoup(page.content, 'html.parser')
                data = soup.find('div', attrs={'class': 'brn-qpage-next-answer-box-content__section'})
                data = data.text.strip()
                await ctx.send(f'{data}')
            else:
                pass


def setup(client):
    client.add_cog(Brainly(client))

# Hageru-Ray
