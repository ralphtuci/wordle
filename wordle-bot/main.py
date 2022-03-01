#3/1/2022
#ralph tran


# import libraries
import os
import discord
import replit
import random

import word

# bot token
my_secret = os.environ['TOKEN']

########################################################

# clear console
replit.clear()

# main code

# retrieving word
WORDS = word.makelist()

# sending to discord client
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  
  
    if message.author == client.user:
        return

    if message.content.startswith('$easy'):
        CHOICE = word.getword(1, WORDS)
        await message.channel.send(CHOICE)

    if message.content.startswith('$word'):
        CHOICE = word.getword(2, WORDS)
        await message.channel.send(CHOICE)

    if message.content.startswith('$hard'):
        CHOICE = word.getword(3, WORDS)
        await message.channel.send(CHOICE)

client.run(os.getenv('TOKEN'))


