from discord.ext import commands

class MonitorCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.json_users = []

    @commands.command() # this is for making a command
    async def ping(self, ctx):
      await ctx.send(f'Pong! {round(self.bot.latency * 1000)}')

    @commands.command() # Add an instagram username
    async def add(self, ctx, *args):
      for arg in args:
        self.bot.json_users.append(arg)
      await ctx.send(f'Added user(s) {args}')
      await ctx.send(f'Current users list: {self.bot.json_users}')

    @commands.command() # Remove an instagram username
    async def remove(self, ctx, *args):
      for arg in args:
        try:
          self.bot.json_users.remove(arg)
          await ctx.send(f'Removed user {arg}')
        except Exception as e:
          print(e)
          await ctx.send(f'Failed to remove user {arg}')
      await ctx.send(f'Current users list: {self.bot.json_users}')

    @commands.command() # Query List of instagram username
    async def query(self, ctx):
      await ctx.send(f'Current users list: {self.bot.json_users}')

def setup(bot):
    bot.add_cog(MonitorCommands(bot))