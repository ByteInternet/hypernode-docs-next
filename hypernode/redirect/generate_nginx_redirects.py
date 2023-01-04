import os.path
from pathlib import Path
from typing import List

from frontmatter import Frontmatter

from hypernode.common.docs import get_all_docs
from hypernode.common.settings import DOCS_DIR


def get_redirects_from_doc(doc: Path) -> List[str]:
    fm = Frontmatter.read_file(doc)
    attributes = fm["attributes"] or {}
    return attributes.get("redirect_from", [])


def get_path_for_doc(doc: Path) -> str:
    relative_path = Path(os.path.relpath(doc, DOCS_DIR))
    path = "/{}/{}".format(
        relative_path.parent, relative_path.name.replace(".md", ".html")
    )
    path = path.replace("/./", "/")
    path = path.replace("/index.html", "/")
    return path


def main():
    for doc in get_all_docs():
        for redirect in get_redirects_from_doc(doc):
            doc_path = get_path_for_doc(doc)
            print("rewrite ^{}$ {} permanent;".format(redirect, doc_path))
