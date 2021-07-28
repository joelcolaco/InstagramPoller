from discord.ext import commands

class MonitorCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() # this is for making a command
    async def ping(self, ctx):
      await ctx.send(f'Pong! {round(self.bot.latency * 1000)}')

def setup(bot):
    bot.add_cog(MonitorCommands(bot))