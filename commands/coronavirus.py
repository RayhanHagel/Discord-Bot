# Covid Statistics Parser by @Hageru-Ray
from discord.ext import commands
import discord
import requests
from bs4 import BeautifulSoup as bs4


class Coronavirus_Parser(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.url = 'https://www.worldometers.info/coronavirus/'
        self.data = ''
        
        self.date_update = ''
        self.total_cases = ''
        self.total_deaths = ''
        self.total_recovered = ''
        

    def get_status(self):
        check =  self.data.find("span", attrs={"class" : "style4"})
        if check:
            print("Didn't found the specified country, please try again!")
            quit()
        else:
            pass
        
     
    def get_data(self, url):        
        fetch = requests.get(url)
        self.data = bs4(fetch.content, 'html.parser')
        self.get_status()
        
        # Fetch Date Update
        if url == self.url:
            date = self.data.find("div", attrs={"style" : "font-size:13px; color:#999; margin-top:5px; text-align:center"})
        else:
            date = self.data.find("div", attrs={"style" : "font-size:13px; color:#999; text-align:center"})
        
        # Fetch Statistics
        total_statistics = self.data.findAll("div", {"class" : "maincounter-number"})
        for item in range(len(total_statistics)):
            total_statistics[item] = total_statistics[item].text
            total_statistics[item] = total_statistics[item].strip().strip("\n")
        
        # Defining into Class
        self.date_update = date.text[14:]
        self.total_cases = total_statistics[0]
        self.total_deaths = total_statistics[1]
        self.total_recovered = total_statistics[2]

        
    def get_country(self, country=None):
        if country == None or country == 'total':
            self.get_data(self.url)
        else:
            country = country.replace(' ', '-')
            url = self.url + "country/" + country
            self.get_data(url)

        
    @commands.command(aliases=['covid', 'covid19', 'covid-19'])
    async def coronavirus(self, ctx, country=None):        
        embed_one = discord.Embed(title=f'Coronavirus Statistics', description=f'**Fetching...**')
        message = await ctx.send(embed=embed_one)
        
        country = country.lower()
        self.get_country(country)
        
        embed_two = discord.Embed(title=f'Coronavirus Statistics', description=country.upper())
        embed_two.add_field(name='Total Cases', value=self.total_cases, inline=False)
        embed_two.add_field(name='Total Deaths', value=self.total_deaths, inline=False)
        embed_two.add_field(name='Total Recovered', value=self.total_recovered, inline=False)
        embed_two.set_footer(text=f'Last updated {self.date_update}')
        
        await message.edit(embed=embed_two)

def setup(client):
    client.add_cog(Coronavirus_Parser(client))
        
        