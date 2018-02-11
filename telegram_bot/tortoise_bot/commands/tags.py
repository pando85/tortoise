import aiotg
import argparse
import yaml

from tortoise_bot.commands.tools import parse_match


def get_get_tags_parser():
    parser = argparse.ArgumentParser(
        prog='tasks get', description='Command to get tags')
    return parser


def get_add_tags_parser():
    parser = argparse.ArgumentParser(
        prog='tags add', description='Command to create new tag')
    parser.add_argument(
        'tags', metavar='TAG', type=str, nargs='+',
        help='new tags to create separated by spaces')
    return parser


def add_commands_tags(bot):
    @bot.command(r"/tags get\ *(.*)")
    async def get_tags(chat: aiotg.Chat, match):
        parser = get_get_tags_parser()
        args = parse_match(match.group(1), parser)
        if not args:
            chat.send_text(parser.format_help())
            return
        tags = await bot.clients[chat.id].get_tags()
        tags_yml = yaml.dump(tags, default_flow_style=False)
        if tags:
            return chat.send_text(tags_yml)
        return

    @bot.command(r"/tags add\ *(.*)")
    async def add_tags(chat: aiotg.Chat, match):
        parser = get_add_tags_parser()
        args = parse_match(match.group(1), parser)
        if not args:
            chat.send_text(parser.format_help())
            return

        for tag in args.tags:
            response = await bot.clients[chat.id].create_tag({"name": tag})
            if response.status == 201:
                chat.send_text('Tag created!')
            if response.status == 400:
                chat.send_text('Tag already exist.')
        return
    return bot
