import os
import re
from logging import getLogger
from pathlib import Path
from posixpath import basename
from textwrap import dedent
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse

import mdformat
import requests
import yaml
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from slugify import slugify

from hypernode.common.logging import configure_logging
from hypernode.downloader.input import parse_args

logger = getLogger(__name__)


class ConvertException(Exception):
    pass


def remove_old_table_of_contents(content: str, replace: bool = False) -> str:
    parsed_lines = []
    stripping_toc = False
    stripping_done = False
    toc_placeholder = "___toc_placeholder___"

    for line in content.splitlines():
        stripped_line = line.strip()

        if stripped_line == "**TABLE OF CONTENTS**" and not stripping_done:
            stripping_toc = True
            parsed_lines.append(toc_placeholder)
            continue

        if stripping_toc:
            if not stripped_line:
                continue
            if (
                stripped_line.startswith("* [")
                or stripped_line.startswith("+ [")
                or stripped_line.startswith("- [")
            ):
                continue
            else:
                stripping_toc = False
                stripping_done = True

        if not stripping_toc:
            parsed_lines.append(line)

    if stripping_toc and not stripping_done:
        raise Exception("Unfinished Table of Contents found!")

    content = "\n".join(parsed_lines)

    if replace:
        # @TODO(timon): this behavior needs a test too, but the feature can probably be disregarded.
        SPHINX_TOC = """
        ```{contents}
        :caption: 'Table of Contents'
        :depth: 3
        :backlinks: none
        ```
        """
        content = content.replace(toc_placeholder, dedent(SPHINX_TOC).lstrip())
    else:
        content = content.replace(toc_placeholder, "")

    return content


def find_output_dir_for_document(filename: str) -> Optional[Path]:
    for root, _, files in os.walk("docs"):
        for file in files:
            if file == filename:
                return Path(root)
    return None


def figure_out_output_dir(filename: str, document: BeautifulSoup) -> Path:
    output_dir = find_output_dir_for_document(filename)
    if output_dir:
        return output_dir

    breadcrumbs = document.find(class_="breadcrumb")
    categories = []
    for crumb in breadcrumbs.findChildren(recursive=False):
        categories.append(slugify(crumb.text.strip()))
    if len(categories) > 2:
        output_dir = Path("docs").joinpath(*categories[2:])
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        return output_dir

    return Path(os.getcwd())


def remove_trailing_whitespace(content: str) -> str:
    TRAILING_WHITESPACE_PATTERIN = re.compile(r"[ \t]+\n")
    return TRAILING_WHITESPACE_PATTERIN.sub("\n", content)


def remove_excess_empty_lines(content: str) -> str:
    DUPLICATE_EMPTY_LINE_PATTERN = re.compile(r"[\n]{3,}")
    return DUPLICATE_EMPTY_LINE_PATTERN.sub("\n\n", content)


def replace_images_with_local_variants(content: str, output_dir: Path) -> str:
    def download_image_cb(match: re.Match) -> str:
        image_url = match.group(1)
        r = urlparse(image_url)
        image_filename = basename(r.path)

        res_dir = output_dir.joinpath("_res")
        filepath = res_dir.joinpath(image_filename)
        markdown_image_url = f"![](_res/{image_filename})"
        if os.path.isfile(filepath):
            return markdown_image_url

        if not os.path.isdir(res_dir):
            os.mkdir(res_dir)

        res_response = requests.get(image_url)
        # @NOTE(timon): Perhaps check mime type?
        with open(filepath, mode="wb") as f:
            f.write(res_response.content)

        return markdown_image_url

    IMAGE_PATTERN = re.compile(r"!\[\]\((.+)\)")
    return IMAGE_PATTERN.sub(download_image_cb, content)


def code_language_callback(element: BeautifulSoup) -> Optional[str]:
    if not element.has_attr("class"):
        return None
    for class_name in element["class"]:
        if class_name.startswith("language-"):
            return class_name.replace("language-", "")
    return None


def fetch_document(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")


def get_document_metadata(document: BeautifulSoup) -> Dict[str, str]:
    result = {}

    ALLOWED_META_NAMES = "description"
    ALLOWED_META_PROPS = ()

    for meta_element in document.find_all("meta"):
        if not meta_element.has_attr("content") or not meta_element["content"]:
            continue

        if meta_element.has_attr("name") and meta_element["name"] in ALLOWED_META_NAMES:
            result[meta_element["name"]] = meta_element["content"]
        elif (
            meta_element.has_attr("property")
            and meta_element["property"] in ALLOWED_META_PROPS
        ):
            result["property={}".format(meta_element["property"])] = meta_element[
                "content"
            ]

    return result


def get_metadata_frontmatter(document: BeautifulSoup) -> str:
    frontmatter_yaml = "\n"

    metadata = get_document_metadata(document)
    if metadata:
        frontmatter = {"myst": {"html_meta": metadata}}
        frontmatter_yaml = yaml.dump(frontmatter, default_flow_style=False)

    return "---\n{}---".format(frontmatter_yaml)


def convert_document(
    document: BeautifulSoup, url: str, output_dir: Optional[Path] = None
) -> Tuple[Path, str]:
    article_heading = document.find(class_="hc-heading").text
    article_body = document.find(id="article-body")

    filename = slugify(article_heading) + ".md"
    if not output_dir:
        output_dir = figure_out_output_dir(filename, document)
    if not os.path.isdir(output_dir):
        raise ConvertException(f"Output directory {output_dir} does not exist!")

    article_body_markdown = md(
        str(article_body),
        code_language_callback=code_language_callback,
        escape_asterisks=False,
        escape_underscores=False,
    )
    article_body_markdown = remove_trailing_whitespace(article_body_markdown)
    article_body_markdown = remove_excess_empty_lines(article_body_markdown)
    article_body_markdown = remove_old_table_of_contents(article_body_markdown)
    article_body_markdown = replace_images_with_local_variants(
        article_body_markdown, output_dir
    )

    document_source_comment = f"<!-- source: {url} -->"
    document_contents = (
        get_metadata_frontmatter(document) + "\n\n"
        f"{document_source_comment}\n\n"
        f"# {article_heading}\n"
        f"{article_body_markdown}"
    )
    document_contents = mdformat.text(
        document_contents, extensions=["frontmatter", "myst"]
    )

    filepath = output_dir.joinpath(filename)

    return (filepath, document_contents)


def get_url_from_document(path: str) -> Optional[str]:
    PATTERN = re.compile(r"<!-- source: (.+) -->")
    with open(path, mode="r", encoding="utf-8") as f:
        m = PATTERN.match(f.readline())
        return m.group(1) if m else None


def main(args: List[str]) -> int:
    document_url_or_path, output_dir, force, verbose = parse_args(args)

    configure_logging(verbose, logger)

    if not document_url_or_path.startswith("http"):
        url = get_url_from_document(document_url_or_path)
        if not url:
            logger.error(
                f"Failed to find source URL in document {document_url_or_path}, exiting."
            )
            return os.EX_USAGE
    else:
        url = document_url_or_path

    document = fetch_document(url)

    try:
        filepath, contents = convert_document(document, url, output_dir=output_dir)
    except ConvertException as e:
        logger.critical(e)
        return os.EX_USAGE

    if os.path.isfile(filepath):
        if force:
            logger.warning(f"Overwriting file {filepath}")
        else:
            logger.error(f"File {filepath} already exists! Exiting")
            return os.EX_USAGE

    with open(filepath, mode="w", encoding="utf-8") as f:
        logger.warning(f"Writing converted doc to {filepath}")
        f.write(contents)

    return os.EX_OK
