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
words = word.makelist()

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
        await message.channel.send("||" + word.geteasy(words) + "||")

    if message.content.startswith('$word'):
        await message.channel.send("||" + word.getword(words) + "||")

    if message.content.startswith('$hard'):
        await message.channel.send("||" + word.gethard(words) + "||")

    if message.content.startswith('$ex'):
        await message.channel.send("||" + word.getex(words) +   "||")


client.run(os.getenv('TOKEN'))


