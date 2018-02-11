import aiotg
import argparse

from tortoise_bot.tortoise_client import TortoiseClient, GetTokenError
from tortoise_bot.commands.tools import parse_match, get_response_from_error


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

        try:
            tortoise_client = await TortoiseClient.create(user, password)
            bot.clients.update({telegram_id: tortoise_client})
            chat.send_text('Successfully login!')
        except GetTokenError as error:
            chat.send_text('Login failed!')
            response = get_response_from_error(error)
            response_body = await response.read()
            chat.send_text('Error: \n' + response_body.decode('utf-8'))
        return
    return bot
