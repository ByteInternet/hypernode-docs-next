import re
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

from frontmatter import Frontmatter

from hypernode.common.docs import get_all_docs, write_doc

SOURCE_PATTERN = re.compile(r"^<!-- source: (.+) -->$")


def get_source_url(doc: Path) -> Optional[str]:
    result = None
    with open(doc, mode="r", encoding="utf-8") as f:
        for line in f.readlines():
            match = SOURCE_PATTERN.match(line)
            if match:
                result = match[1]
    return result


def set_source_path_redirect(doc: Path, source_path: str) -> None:
    fm = Frontmatter.read_file(doc)
    attributes = fm["attributes"] or {}
    attributes["redirect_from"] = [source_path]

    body = fm["body"]
    if not body:
        with open(doc, mode="r", encoding="utf-8") as f:
            body = f.read()

    write_doc(doc, body, attributes)


def main():
    for doc in get_all_docs():
        source_url = get_source_url(doc)
        if not source_url:
            continue

        path = urlparse(source_url).path
        set_source_path_redirect(doc, path)
