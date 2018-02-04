import shlex


def parse_match(match, parser):
    args_list = shlex.split(match)
    try:
        args = parser.parse_args(args_list)
    except SystemExit:
        args = False
    return args
