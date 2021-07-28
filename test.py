import os
import discord
from discord.ext import tasks

client = discord.Client()

@tasks.loop(seconds = 10) # repeat after every 10 seconds
async def myLoop():
    # work
    print('Running Loop')

myLoop.start()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))