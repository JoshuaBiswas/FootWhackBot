import discord
from os import environ
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('the bot is ready!')    

@client.event
async def on_message(message):
        if message.content.startswith('$go '):
            channel = message.channel
            await channel.send('go fuck yoursefl')
        
        elif message.content.startswith('$'):
            channel = message.channel
            await channel.send('Is this all?')

client.run('.');
