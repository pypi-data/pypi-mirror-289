import sys
import json
import argparse

from nbweb.app import get_content
from nbweb.app import get_rss
from nbweb.app import check_is_supported


def parse_args():
    parser = argparse.ArgumentParser(
        prog="nbweb",
        description="extracts bloat free content",
        epilog="takes in an url and returns clean content",
    )
    parser.add_argument("url", type=str, help="enter an url")
    parser.add_argument(
        "-f",
        "--format",
        choices=["json", "txt"],
        default="json",
        help="choose the output format. default is json",
    )

    parser.add_argument("--supported", action="store_true", help="returns yes if supported else no")

    parser.add_argument(
        "--rss", action="store_true", help="returns the rss information"
    )

    args = parser.parse_args()
    return args


def cli() -> None:
    args = parse_args()

    if args.rss == True:
        content = get_rss(args.url)
    elif args.supported == True:
        content = check_is_supported(args.url)
    else:
        content = get_content(args.url, args.format)
    print(content)


if __name__ == "__main__":
    cli()
