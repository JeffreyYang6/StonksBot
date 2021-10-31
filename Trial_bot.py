import discord
import os
from decouple import config

client = discord.Client()
TOKEN = config('TOKEN')
PREFIX='tb! '

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(PREFIX + 'hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith(PREFIX + 'gb'):
        await message.channel.send('Goodbye!')

client.run(TOKEN)
