from argparse import ArgumentParser


def parse_args(args) -> bool:
    parser = ArgumentParser(description="Download, convert and save documentation page")
    parser.add_argument(
        "-v", "--verbose", help="Be more verbose", action="store_true", default=False
    )

    parsed_args = parser.parse_args(args)

    return parsed_args.verbose
