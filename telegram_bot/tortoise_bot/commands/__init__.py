from tortoise_bot.commands.login import add_commands_login
from tortoise_bot.commands.tasks import add_commands_tasks
from tortoise_bot.commands.tags import add_commands_tags


def add_commands(bot):
    bot = add_commands_login(bot)

    bot = add_commands_tasks(bot)

    bot = add_commands_tags(bot)

    return bot
