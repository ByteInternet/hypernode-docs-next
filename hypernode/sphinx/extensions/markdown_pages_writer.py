from pathlib import Path
from typing import TYPE_CHECKING, Dict

from hypernode.sphinx.extensions.markdown_content import convert
from hypernode.sphinx.extensions.markdown_tree import (
    collect_tree,
    site_url_for,
    title_of,
)

if TYPE_CHECKING:
    from sphinx.application import Sphinx

SKIP_DOCS = {"index", "404"}


def write_markdown_pages(app: "Sphinx", exception) -> None:
    env = app.builder.env
    config = app.config

    docnames = collect_tree(env, "index")
    if config.markdown_include_orphans:
        known = set(docnames) | set(SKIP_DOCS)
        docnames.extend(doc for doc in sorted(env.found_docs) if doc not in known)

    titles: Dict[str, str] = {}
    links: Dict[str, str] = {}
    for docname in ["index"] + docnames:
        titles[docname] = title_of(env, docname)
        links[docname] = site_url_for(config, docname)

    # Source image paths (e.g. about-hypernode/billing/_res/cancel.png) map
    # to their published URL (https://docs.hypernode.com/_images/cancel.png).
    image_urls: Dict[str, str] = {}
    for source_key, (_, published_name) in env.images.items():
        image_urls[source_key] = "{}/_images/{}".format(
            (config.html_baseurl or "").rstrip("/"), published_name
        )

    for docname in docnames:
        source_file = Path(app.srcdir) / (docname + ".md")
        if not source_file.exists():
            continue
        output = convert(
            source_file.read_text(encoding="utf-8"),
            docname,
            image_urls,
            titles,
            links,
        )
        output_path = Path(app.outdir) / (docname + ".html.md")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output, encoding="utf-8")


def setup(app: "Sphinx"):
    app.add_config_value("markdown_include_orphans", True, "html")
    app.connect("build-finished", write_markdown_pages)

    return {
        "version": "0.1",
        "parallel_write_safe": True,
    }
