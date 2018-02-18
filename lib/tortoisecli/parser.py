import argparse
import os


def get_parser():
    main_parser = argparse.ArgumentParser(prog="tortoisecli")
    main_parser.add_argument(
        "-v", "--verbose", help="verbose mode", action="store_true")

    main_parser.add_argument(
        "--token", help="tortoise API token",
        default=os.environ.get('TORTOISE_TOKEN', None))

    main_parser.add_argument(
        "-u", "--username", help="tortoise username using basic auth")

    main_parser.add_argument(
        "-p", "--password", help="tortoise password using basic auth")

    main_parser.add_argument(
        "--url", help="tortoise API url",
        default=os.environ.get('TORTOISE_URL', "http://127.0.0.1:8000/v1/"))

    subparsers = main_parser.add_subparsers(dest='command')
    subparsers.add_parser("create", help="Create a resource from stdin")
    subparsers.add_parser("get", help="Display one or many resources")
    subparsers.add_parser("edit", help="Edit a resource")
    subparsers.add_parser("delete", help="Delete resources by stdin")

    resources = ["task", "tag", "user"]

    [subparsers.choices[option].add_argument(
        "resource", choices=resources)
        for option in ["create", "get", "edit", "delete"]]

    [subparsers.choices[option].add_argument(
        "--data", help="Json data send in request", default=None)
        for option in ["create", "edit", "delete"]]

    return main_parser
