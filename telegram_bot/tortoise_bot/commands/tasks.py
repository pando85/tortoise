import aiotg
import argparse
import yaml

from tortoise_bot.commands.tools import parse_match


def add_commands_tasks(bot):
    @bot.command(r"/tasks get\ *(.*)")
    async def get_tasks(chat: aiotg.Chat, match):
        tasks = await bot.clients[chat.id].get_tasks()
        tasks_filtered = [
            {k: v for k, v in task.items() if v}
            for task in tasks]
        tasks_yml = yaml.dump(tasks_filtered, default_flow_style=False)
        if tasks:
            return chat.send_text(tasks_yml)
        return

    @bot.command(r"/tasks add\ *(.*)")
    async def create_task(chat: aiotg.Chat, match):
        parser = argparse.ArgumentParser(
            prog='tasks add', description='Command to create new tasks')
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

    return bot
