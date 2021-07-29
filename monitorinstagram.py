import os
from discord.ext import tasks, commands
from instagramconnector import get_instagram_html,webhook,get_last_publication_url


class MonitorInstagram(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.startMonitor.start()

    def cog_unload(self):
        self.startMonitor.cancel()

    # repeat based on variable or after every 10 seconds
    @tasks.loop(seconds=float(os.environ.get('TIME_INTERVAL') or 600))
    async def startMonitor(self):
        print('Querying Instagram for new data')
        for user in self.bot.user_data:
          query_instagram(self, user)

def query_instagram(self, user):
  try:
      INSTAGRAM_USERNAME = user
      html = get_instagram_html(INSTAGRAM_USERNAME)
      if(self.bot.user_data[user] == get_last_publication_url(html)):
          print("No new image to post in discord.")
      else:
          self.bot.user_data[user] = get_last_publication_url(html)
          print("New image to post in discord.")
          webhook(os.environ.get("WEBHOOK_URL"),
                  get_instagram_html(INSTAGRAM_USERNAME))
  except Exception as e:
      print(e)

def setup(bot):
    bot.add_cog(MonitorInstagram(bot))

