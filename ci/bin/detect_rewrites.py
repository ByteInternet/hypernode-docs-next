import argparse
import re
import subprocess
from typing import Tuple

RENAME_PATTERN = re.compile(r"^R[0-9]+")


def parse_args() -> Tuple[str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument("start_commit")
    parser.add_argument("end_commit")

    args = parser.parse_args()

    return args.start_commit, args.end_commit


def main():
    start_commit, end_commit = parse_args()
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
    renamed_files = filter(RENAME_PATTERN.match, output.splitlines())
    renamed_files = map(lambda x: x.split("\t")[1:], renamed_files)
    renamed_markdown_files = filter(lambda x: x[0].endswith(".md"), renamed_files)
    renamed_markdown_files = list(renamed_markdown_files)

    if renamed_markdown_files:
        print("Detected renamed/moved files:")
        print("```")
        for file_from, file_to in renamed_markdown_files:
            print("{} => {}".format(file_from, file_to))
        print("```")
        print("To prevent 404 pages, consider adding the redirects to the new pages:")
        print("```markdown")
        print("---")
        print("redirect_from:")
        for file_from, _ in renamed_markdown_files:
            print("  - {}".format(file_from))
        print("---")
        print("```")


if __name__ == "__main__":
    main()
