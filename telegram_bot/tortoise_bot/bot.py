import os
import aiotg


def create_bot():
    telegram_bot = aiotg.Bot(os.environ["API_TOKEN"])
    telegram_bot.clients = {}
    return telegram_bot
