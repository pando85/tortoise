import asyncio
import logging

from tortoisecli.client import TortoiseClient
from tortoisecli.tools import parse_data
from tortoisecli.parser import get_parser


def main():
    parser = get_parser()

    args = parser.parse_args()
    setup_logging_level(args.verbose)

    data = parse_data(args.data) if "data" in args else None

    loop = asyncio.get_event_loop()
    if "username" in args and "password" in args:
        client = loop.run_until_complete(
            TortoiseClient.create(args.url, args.username, args.password))
    else:
        client = TortoiseClient.create_with_token(args.url, args.token)

    try:
        task_obj = loop.create_task(
            client.api_call(args.command, args.resource, data))
        loop.run_until_complete(task_obj)
    finally:
        loop.close()


def setup_logging_level(verbose):
    logger = logging.getLogger()
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
