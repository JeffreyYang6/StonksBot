import discord
import os
from decouple import config
import requests

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
    
    if message.content.startswith(PREFIX + 'cards'):
        deck = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1').json()
        deck_id = deck['deck_id']
        hand = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2').json()
        await message.channel.send(hand)

client.run(TOKEN)
