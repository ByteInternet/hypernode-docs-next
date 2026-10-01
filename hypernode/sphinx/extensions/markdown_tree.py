from typing import List

import sphinx.addnodes as addnodes


def collect_tree(env, root_docname: str) -> List[str]:
    """
    Collect all docnames reachable from root_docname's toctrees, in
    navigation order. Does not include root_docname itself unless it is
    also referenced from a child toctree (e.g. the site index).
    """
    result: List[str] = []

    def walk(docname: str) -> None:
        toc = env.tocs.get(docname)
        if toc is None:
            return
        for node in toc.findall(addnodes.toctree):
            for _, entry in node.attributes["entries"]:
                if entry in ("self", "*"):
                    continue
                if entry in result:
                    continue
                result.append(entry)
                walk(entry)

    walk(root_docname)
    return result


def title_of(env, docname: str) -> str:
    title = env.titles.get(docname)
    return title.astext().strip() if title else docname


def site_url_for(config, docname: str) -> str:
    base_url = (config.html_baseurl or "").rstrip("/")
    if docname == "index":
        return base_url + "/"
    if docname.endswith("/index"):
        return base_url + "/" + docname[: -len("/index")] + "/"
    return base_url + "/" + docname + ".html"


def image_url_for(images, target: str) -> str:
    """
    Resolve an image reference (e.g. _res/foo.png) to its published URL
    (e.g. https://docs.hypernode.com/_images/foo.png) using the Sphinx
    environment's image collection, falling back to the bare filename.
    """
    from posixpath import basename

    entry = images.get(target)
    if entry:
        # FilenameUniqDict maps source path -> (set of docnames, published name)
        return basename(entry[1])
    return basename(target)
