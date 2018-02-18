import argparse


def get_parser():
    main_parser = argparse.ArgumentParser(prog="tortoisecli")
    main_parser.add_argument(
        "-v", "--verbose", help="verbose mode", action="store_true")

    subparsers = main_parser.add_subparsers(dest='command')
    subparsers.add_parser("create", help="Create a resource from stdin")
    subparsers.add_parser("get", help="Display one or many resources")
    subparsers.add_parser("edit", help="Edit a resource")
    subparsers.add_parser("delete", help="Delete resources by stdin")

    resources = ['user', 'task', 'tag']

    [parser.add_argument("resource", choices=resources)
        for parser in subparsers.choices.values()]

    return main_parser
