import shlex


def parse_match(match, parser):
    args_list = shlex.split(match)
    try:
        args = parser.parse_args(args_list)
    except SystemExit:
        args = False
    return args


def beauty_tasks(tasks):
    output = ''
    for task in tasks:
        output += f"- *{task['name']}*\n"
        if task['description']:
            output += f"   `{task['description']}`\n"

        if task['deadline']:
            output += f"   Limit:{task['deadline']}\n"

        if task['tags']:
            output += f"    tags:{task['tags']}\n"

        if task['members']:
            output += f"    members:{task['members']}\n"
        output += "\n"
    return output


def get_response_from_error(error):
    response, = error.args
    return response
