import os
from discord.ext import commands, tasks
from instagramconnector import query_instagram


def main():
    bot = commands.Bot(command_prefix='!')

    @tasks.loop(seconds=float(os.environ.get('TIME_INTERVAL') or 600)
                )  # repeat based on variable or after every 10 seconds
    async def myLoop():
        # work
        print('Running Loop')
        query_instagram()

    myLoop.start()

    bot.load_extension("monitorcommands")

    bot.run(os.getenv('TOKEN'))


if __name__ == "__main__":
    if os.environ.get('IG_USERNAME') != None and os.environ.get(
            'WEBHOOK_URL') != None:
        while True:
            main()
    else:
        print('Please configure environment variables properly!')
