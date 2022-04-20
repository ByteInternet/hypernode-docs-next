from argparse import ArgumentParser
from pathlib import Path
from typing import Optional, Tuple


def parse_args(args) -> Tuple[str, Optional[Path], bool, bool]:
    parser = ArgumentParser(description="Download, convert and save documentation page")
    parser.add_argument("url", nargs=1, help="Documentation URL to download")
    parser.add_argument(
        "--output-dir",
        help="Directory to save the page",
        default=None,
    )
    parser.add_argument(
        "-v", "--verbose", help="Be more verbose", action="store_true", default=False
    )
    parser.add_argument(
        "-f",
        "--force",
        help="Overwrite existing file when it exists",
        action="store_true",
        default=False,
    )

    parsed_args = parser.parse_args(args)

    return (
        parsed_args.url[0],
        Path(parsed_args.output_dir) if parsed_args.output_dir else None,
        parsed_args.force,
        parsed_args.verbose,
    )
