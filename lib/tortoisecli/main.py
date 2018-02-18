import asyncio
import logging

from tortoisecli.client import TortoiseClient
from tortoisecli.errors import GetTokenError, ExpectedStatusError
from tortoisecli.parser import get_parser
from tortoisecli.print import beautyPrint
from tortoisecli.tools import parse_data


def main():
    parser = get_parser()

    args = parser.parse_args()
    setup_logging_level(args.verbose)

    data = parse_data(args.data) if "data" in args else None

    loop = asyncio.get_event_loop()
    try:
        if args.username and args.password:
            client = loop.run_until_complete(
                TortoiseClient.create(args.url, args.username, args.password))
        else:
            client = TortoiseClient.create_with_token(args.url, args.token)

        result = loop.run_until_complete(
            client.api_call(args.command, args.resource, data))
    except (GetTokenError, ExpectedStatusError) as e:
        print(e)
        exit(1)

    beautyPrint.print(result, args.resource)


def setup_logging_level(verbose):
    logger = logging.getLogger()
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
