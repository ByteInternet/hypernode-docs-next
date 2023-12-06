import json
import queue
from multiprocessing import Manager
from pathlib import Path
from typing import TYPE_CHECKING

from sphinx.util.logging import getLogger

logger = getLogger(__name__)

if TYPE_CHECKING:
    from sphinx.application import Sphinx

"""
This extension was inspired by sphinx-sitemap, which is a generator
for the sitemap.xml file.
"""


def register_page(app: "Sphinx", pagename: str, templatename, context, doctree):
    env = app.builder.env
    base_url = app.builder.config.html_baseurl
    file_suffix = app.builder.config.html_file_suffix or ".html"

    if pagename == "404":
        return

    link = base_url + pagename + file_suffix
    page_title = context.get("title")
    if page_title:
        env.app.json_sitemap_links.put({"url": link, "title": page_title})  # type: ignore[attr-defined]


def write_sitemap(app: "Sphinx", exception):
    links = []
    while True:
        try:
            links.append(app.env.app.json_sitemap_links.get_nowait())  # type: ignore[attr-defined]
        except queue.Empty:
            break

    encoded = json.dumps(links)
    filename = app.config.json_sitemap_filename
    with open(Path(app.outdir) / filename, "w", encoding="utf-8") as f:
        f.write(encoded)

    logger.info(
        f"json-sitemap: {filename} has been generated",
        type="json-sitemap",
        subtype="information",
    )


def init_page_queue(app: "Sphinx"):
    builder = getattr(app, "builder", None)
    if builder is None:
        return
    builder.env.is_directory_builder = type(builder).__name__ == "DirectoryHTMLBuilder"
    builder.env.app.json_sitemap_links = Manager().Queue()


def setup(app: "Sphinx"):
    app.add_config_value("json_sitemap_filename", default="sitemap.json", rebuild="")
    app.connect("builder-inited", init_page_queue)
    app.connect("html-page-context", register_page)
    app.connect("build-finished", write_sitemap)

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
