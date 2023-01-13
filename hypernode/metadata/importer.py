import argparse
import csv

from hypernode.common import settings
from hypernode.common.docs import read_doc, write_doc


def parse_args() -> str:
    parser = argparse.ArgumentParser()
    parser.description = "Utility to import metadata from a CSV file into the articles"
    parser.add_argument("file", help="Path to CSV file")

    args = parser.parse_args()
    return args.file


def main():
    file = parse_args()
    with open(file, mode="r") as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        i = 0
        for _, path, title, description in reader:
            if i == 0 or not any([title, description]):
                i += 1
                continue
            path = path.lstrip("/").replace(".html", ".md")
            path = settings.DOCS_DIR / path

            print("Importing metadata for {}".format(path))

            fm, body, _ = read_doc(path)
            fm["myst"] = fm.get("myst", {"html_meta": {}})
            if title:
                fm["myst"]["html_meta"]["title"] = title
            if description:
                fm["myst"]["html_meta"]["description"] = description

            write_doc(path, body, fm)

            i += 1
