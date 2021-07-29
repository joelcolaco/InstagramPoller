from discord.ext import commands


class MonitorCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Add an instagram username
    @commands.command()
    async def add(self, ctx, *args):
        for arg in args:
            self.bot.user_data[f'{arg}'] = ""
        await ctx.send(f'Added user(s) {args}')
        await ctx.send(getDictionary(self))

    # Remove an instagram username
    @commands.command()
    async def remove(self, ctx, *args):
        for arg in args:
            try:
                self.bot.user_data.pop(arg)
                await ctx.send(f'Removed user {arg}')
            except Exception as e:
                print(e)
                await ctx.send(f'Failed to remove user {arg}')
        await ctx.send(getDictionary(self))

    # Query List of instagram username
    @commands.command()
    async def query(self, ctx):
        await ctx.send(getDictionary(self))


def getDictionary(self):
    return f'Current users list: {list(self.bot.user_data.keys())}'


def setup(bot):
    bot.add_cog(MonitorCommands(bot))
