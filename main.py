import os
from discord.ext import commands,tasks
from instagramconnector import query_instagram

bot = commands.Bot(command_prefix='!')

@tasks.loop(seconds = 10) # repeat after every 10 seconds
async def myLoop():
    # work
    print('Running Loop')
    query_instagram()

myLoop.start()

bot.load_extension("monitorcommands")

bot.run(os.getenv('TOKEN'))