import os.path
from pathlib import Path
from typing import List

from hypernode.common.settings import DOCS_DIR


def get_all_docs() -> List[Path]:
    result = []
    for root, dirs, files in os.walk(DOCS_DIR):
        if "/_build" in root or "/_res" in root:
            continue

        markdown_files = filter(lambda f: f.endswith(".md"), files)
        for file in markdown_files:
            result.append(Path(root) / file)
    return result
