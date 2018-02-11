from tortoise_bot.commands.help import add_command_help
from tortoise_bot.commands.login import add_commands_login
from tortoise_bot.commands.tags import add_commands_tags
from tortoise_bot.commands.tasks import add_commands_tasks


def add_commands(bot):
    bot = add_command_help(bot)
    bot = add_commands_login(bot)
    bot = add_commands_tags(bot)
    bot = add_commands_tasks(bot)

    return bot
