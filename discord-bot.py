import os
from discord.ext import commands


TOKEN = '{Token Here}'

client = commands.Bot(command_prefix='.', help_command=None)
os.system('cls')

for filename in os.listdir(r'./commands'):
    if filename.endswith('.py'):
        try:
            client.load_extension(f'commands.{filename[:-3]}')
        except Exception:
            print(f'Module {filename} is having an error....')

client.run(TOKEN)

# Hagery-Ray
