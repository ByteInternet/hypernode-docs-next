import argparse
import re
import subprocess
from typing import Tuple

CHANGED_PATTERN = re.compile(r"^[AM]")


def parse_args() -> Tuple[str, str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument("start_commit")
    parser.add_argument("end_commit")
    parser.add_argument("--base-url", default="")

    args = parser.parse_args()

    return args.start_commit, args.end_commit, args.base_url.rstrip("/")


def main():
    start_commit, end_commit, base_url = parse_args()
    diff_command = [
        "git",
        "diff",
        "--name-status",
        "-M",
        "--stat",
        start_commit,
        end_commit,
    ]
    output = subprocess.check_output(diff_command, encoding="utf-8")
    changed_files = filter(CHANGED_PATTERN.match, output.splitlines())
    changed_files = map(lambda x: x.split("\t")[1], changed_files)
    changed_markdown_files = filter(lambda x: x.endswith(".md"), changed_files)
    changed_markdown_files = list(changed_markdown_files)

    if changed_markdown_files:
        print("Changed pages:")
        for file in changed_markdown_files:
            file = re.sub("^docs/", "", file)
            file = re.sub(".md$", ".html", file)
            print("- " + base_url + "/" + file)


if __name__ == "__main__":
    main()
