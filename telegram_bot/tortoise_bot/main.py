import os


from tortoise_bot.bot import create_bot
from tortoise_bot.commands import add_commands


def main():
    bot = create_bot()
    bot = add_commands(bot)
    bot.run(debug=os.getenv('DEBUG', False), reload=False)
