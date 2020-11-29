
from discord.ext import commands
import requests
import json
import discord


API_KEY = '{PARSEHUB_API_KEY}'
PROJECT_TOKEN = '{PARSEHUB_PROJECT_TOKEN}'


class Parser_Frame:    
    def __init__(self, key, token):
        self.token = token
        self.parameter = {"api_key": key}
        self.response = self.get_response()
    
    def get_response(self):
        parsehub = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.token}/last_ready_run/data', params=self.parameter)
        data = json.loads(parsehub.text)
        return data

    def get_total_cases(self):
        data = self.get_response()['total']
        for content in data:
            if content['name'] == "Coronavirus Cases:":
                return content['value']
    
    def get_total_deaths(self):
        data = self.get_response()['total']
        for content in data:
            if content['name'] == "Deaths:":
                return content['value']

    def get_total_recovered(self):
        data = self.get_response()['total']
        for content in data:
            if content['name'] == 'Recovered:':
                return content['value']
            
    def get_country_data(self, country):
        response = self.get_response()['country']
        for content in response:
            if content['name'].lower() == country.lower():
                return content
    
    def get_date(self):
        response = self.get_response()['date']
        return response[14:]
    
Parser = Parser_Frame(API_KEY, PROJECT_TOKEN)


class Coronavirus_Parser(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    
    @commands.command(aliases=['covid19'])
    async def covid(self, ctx, country='total'):
        country = country.lower()
        
        if country == 'total':
            cases = Parser.get_total_cases()
            deaths = Parser.get_total_deaths()
            recovered = Parser.get_total_recovered()
            
            embed = discord.Embed(title=f'Total Coronavirus Statistics',
                                  url = 'https://www.worldometers.info/coronavirus/')
            
            embed.set_footer(text=Parser.get_date())
            embed.add_field(name='Cases', value=cases, inline=False)
            embed.add_field(name='Deaths', value=deaths, inline=False)
            embed.add_field(name='Recovered', value=recovered, inline=False)

            message = await ctx.send(embed=embed)
            
        else:
            name = Parser.get_country_data(country)['name']
            cases = Parser.get_country_data(country)['total_cases']
            deaths = Parser.get_country_data(country)['total_deaths']
            recovered = Parser.get_country_data(country)['total_recovered']
            active = Parser.get_country_data(country)['active_cases']
            
            embed = discord.Embed(title=f'Coronavirus Statistics',
                                  url = f'https://www.worldometers.info/coronavirus/country/{country}/')
            
            embed.set_footer(text=Parser.get_date())
            embed.add_field(name='Country', value=name, inline=False)
            embed.add_field(name='Cases', value=cases, inline=False)
            embed.add_field(name='Deaths', value=deaths, inline=False)
            
            embed.add_field(name='Recovered', value=recovered, inline=False)
            embed.add_field(name='Active Cases', value=active, inline=False)
            
            message = await ctx.send(embed=embed)
    
def setup(client):
    client.add_cog(Coronavirus_Parser(client))

# Hageru-Ray
