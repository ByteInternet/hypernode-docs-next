import os.path
from pathlib import Path
from typing import List, Optional, Tuple

import mdformat
import yaml
from frontmatter import Frontmatter

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


def read_doc(path: Path) -> Tuple[dict, str, str]:
    with open(path, mode="r") as f:
        contents = f.read()
        fm = Frontmatter.read(contents)
        if not fm["attributes"]:
            fm["attributes"] = {}
        if not fm["body"]:
            fm["body"] = contents
        return (
            fm["attributes"],
            fm["body"],
            contents,
        )


def write_doc(path: Path, contents: str, frontmatter: Optional[dict]) -> None:
    if frontmatter:
        fm_yaml = yaml.dump(frontmatter, default_flow_style=False)
        contents = "---\n" + fm_yaml + "---\n\n" + contents

    contents = mdformat.text(contents, extensions=["frontmatter", "myst"])

    with open(path, mode="w", encoding="utf-8") as f:
        f.write(contents)
