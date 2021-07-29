import os
from discord.ext import commands


def main():
    bot = commands.Bot(command_prefix='!')
    bot.user_data = []
    bot.load_extension("monitorcommands")
    bot.load_extension("monitorinstagram")
    bot.run(os.getenv('TOKEN'))


if __name__ == "__main__":
    if os.environ.get('IG_USERNAME') != None and os.environ.get(
            'WEBHOOK_URL') != None:
        while True:
            main()
    else:
        print('Please configure environment variables properly!')
