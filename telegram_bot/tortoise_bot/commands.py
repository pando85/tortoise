import aiotg
import argparse
import json
import shlex
import yaml

from tortoise_bot.tortoise_client import TortoiseClient


def parse_match(match, parser):
    args_list = shlex.split(match)
    try:
        args = parser.parse_args(args_list)
    except SystemExit:
        args = False
    return args


def add_commands(bot):
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

    @bot.command(r"/tasks\ *(.*)")
    async def get_tasks(chat: aiotg.Chat, match):
        tasks = await bot.clients[chat.id].get_tasks()
        tasks_filtered = [
            {k: v for k, v in task.items() if v}
            for task in tasks]
        tasks_yml = yaml.dump(tasks_filtered, default_flow_style=False)
        if tasks:
            return chat.send_text(tasks_yml)
        return

    @bot.command(r"/create task\ *(.*)")
    async def create_task(chat: aiotg.Chat, match):
        parser = argparse.ArgumentParser(
            prog='create task', description='create task command')
        required_group_parser = parser.add_argument_group('required arguments')
        required_group_parser.add_argument(
            '-t',
            '--title',
            required=True)
        parser.add_argument(
            '-d',
            '--description')
        parser.add_argument(
            '--deadline')
        parser.add_argument(
            '-m',
            '--members')
        parser.add_argument(
            '--tags')

        args = parse_match(match.group(1), parser)
        if not args:
            chat.send_text(parser.format_help())
            return
        task = {}
        task.update({'title': args.title})
        if args.description:
            task.update({'description': args.description})
        if args.deadline:
            task.update({'deadline': args.deadline})
        if args.members:
            task.update({'members': args.members})
        if args.tags:
            task.update({'tags': args.tags})
        response = await bot.clients[chat.id].create_task(task)
        if response.status == 201:
            chat.send_text('Task created!')
        if response.status == 400:
            chat.send_text('Task already exist.')
        return

    @bot.command(r"/tags\ *(.*)")
    async def get_tags(chat: aiotg.Chat, match):
        tags = await bot.clients[chat.id].get_tags()
        print(tags)
        tags_yml = yaml.dump(tags, default_flow_style=False)
        if tags:
            return chat.send_text(tags_yml)
        return

    @bot.command(r"/create tags\ *(.*)")
    async def create_tags(chat: aiotg.Chat, match):
        parser = argparse.ArgumentParser(
            prog='create tags', description='create tag command')
        parser.add_argument(
            'tags', metavar='TAG', type=str, nargs='+', help='create tags')
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
