import aiotg
import argparse

from tortoise_bot.tortoise_client import TortoiseClient
from tortoise_bot.commands.tools import parse_match


def add_commands_login(bot):
    @bot.command(r"/login\ *(.*)")
    async def login(chat: aiotg.Chat, match):
        parser = argparse.ArgumentParser(
            prog='login', description='login command')
        required_group_parser = parser.add_argument_group('required arguments')
        required_group_parser.add_argument(
            '-u',
            '--username',
            required=True)
        required_group_parser.add_argument(
            '-p',
            '--password',
            required=True)

        args = parse_match(match.group(1), parser)
        if not args:
            chat.send_text(parser.format_help())
            return

        telegram_id = chat.id
        user = args.username
        password = args.password
        tortoise_client = await TortoiseClient.create(user, password)
        bot.clients.update({telegram_id: tortoise_client})
        chat.send_text(bot.clients[telegram_id].token)
        return
    return bot
