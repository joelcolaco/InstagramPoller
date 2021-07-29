import os
from discord.ext import tasks, commands
from instagramconnector import query_instagram

class MonitorInstagram(commands.Cog):
    def __init__(self):
        self.startMonitor.start()

    def cog_unload(self):
        self.startMonitor.cancel()

    @tasks.loop(seconds=float(os.environ.get('TIME_INTERVAL') or 600))  # repeat based on variable or after every 10 seconds
    async def startMonitor(self):
      # work
      print('Querying Instagram for new data')
      query_instagram()

def setup(bot):
    bot.add_cog(MonitorInstagram())      