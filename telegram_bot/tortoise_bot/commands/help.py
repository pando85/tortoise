import aiotg


def add_command_help(bot):
    @bot.command(r"/help\ *(.*)")
    async def print_help(chat: aiotg.Chat, match):
        help_message = 'Commands: \n'
        help_message += '/login \n'
        help_message += '/help \n'
        help_message += '/tags add \n'
        help_message += '/tags get \n'
        help_message += '/tasks add \n'
        help_message += '/tasks get \n'
        return chat.send_text(help_message)

    return bot
