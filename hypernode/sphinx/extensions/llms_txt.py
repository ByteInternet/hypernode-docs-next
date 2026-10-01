import re
from typing import List, Tuple

import sphinx.addnodes as addnodes

from hypernode.sphinx.extensions.markdown_tree import site_url_for, title_of

DESCRIPTION = (
    "Documentation for Hypernode: the managed hosting platform for Magento, "
    "Shopware, Laravel and other web applications."
)


def write_llms_txt(app, exception) -> None:
    env = app.builder.env
    config = app.config

    sections, parents = _sections(env)
    in_sections = {docname for _, entries in sections for docname in entries}

    base_url = (config.html_baseurl or "").rstrip("/")
    intro = (
        "Hypernode is a managed hosting platform for webshops and web applications,"
        " maintained by Team.blue. This file is a curated map of the documentation"
        " at {}. Every page is also available as clean markdown by appending"
        " `.html.md` to its URL.".format(base_url if base_url else "this site")
    )
    lines: List[str] = [
        "# Hypernode Documentation",
        "",
        "> " + DESCRIPTION,
        "",
        intro,
        "",
    ]

    for caption, entries in sections:
        lines.append("## " + caption)
        lines.append("")
        lines.extend(_link_list(env, config, entries))
        lines.append("")

    optional = _optional(env, in_sections | set(parents))
    if optional:
        lines.append("## Optional")
        lines.append("")
        lines.extend(_link_list(env, config, optional))
        lines.append("")

    with open(str(app.outdir) + "/llms.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")


def _sections(env) -> Tuple[List[Tuple[str, List[str]]], List[str]]:
    """
    Build H2 sections from the top-level index toctrees. Category pages
    (e.g. hypernode-platform/php) are flattened into their articles; the
    flattened-away pure stub pages are returned separately so they can be
    excluded elsewhere.
    """
    toc = env.tocs.get("index")
    if toc is None:
        return [], []

    sections: List[Tuple[str, List[str]]] = []
    parents: List[str] = []
    for node in toc.findall(addnodes.toctree):
        caption = node.get("caption") or "Documentation"
        entries: List[str] = []
        for _, entry in node.attributes["entries"]:
            if entry == "self":
                continue
            flattened = _flatten(env, entry)
            if entry not in flattened:
                parents.append(entry)
            entries.extend(flattened)
        if entries:
            sections.append((caption, entries))
    return sections, parents


def _flatten(env, docname: str, depth: int = 0) -> List[str]:
    """
    Flatten a category page into its article docnames. Pages with real
    content of their own (chapter landing pages) are kept in the list
    before their children; pure toctree stubs are dropped.
    """
    toc = env.tocs.get(docname)
    if toc is None or depth > 5:
        return [docname]

    child_entries: List[str] = []
    for node in toc.findall(addnodes.toctree):
        for _, entry in node.attributes["entries"]:
            if entry == "self":
                continue
            child_entries.extend(_flatten(env, entry, depth + 1))

    if not child_entries:
        return [docname]
    if _wordcount(env, docname) < 5:
        return child_entries
    return [docname] + child_entries


def _wordcount(env, docname: str) -> int:
    metadata = env.metadata.get(docname, {})
    return metadata.get("wordcount", {}).get("words", 0)


def _link_list(env, config, docnames: List[str]) -> List[str]:
    lines: List[str] = []
    for docname in docnames:
        title = title_of(env, docname)
        url = site_url_for(config, docname)
        summary = _summary(env, docname)
        if summary:
            lines.append("- [{}]({}): {}".format(title, url, summary))
        else:
            lines.append("- [{}]({})".format(title, url))
    return lines


def _summary(env, docname: str) -> str:
    """
    Use the article's meta description (the SEO summary every article has)
    as the link notes in llms.txt; fall back to child titles for category
    pages that end up in the list.
    """
    metadata = env.metadata.get(docname, {})
    description = metadata.get("description")
    if description:
        return _clean_summary(description)

    toc = env.tocs.get(docname)
    if toc is not None:
        children = []
        for node in toc.findall(addnodes.toctree):
            for _, entry in node.attributes["entries"]:
                if entry != "self":
                    children.append(title_of(env, entry))
        if children:
            preview = ", ".join(children[:5])
            if len(children) > 5:
                return "Articles: {}, and more.".format(preview)
            return "Articles: {}.".format(preview)
    return ""


def _clean_summary(description: str) -> str:
    description = re.sub(r"\s+", " ", description).strip()
    description = re.sub(r"\s*\|\s*Hypernode\s*$", "", description)
    return description


def _optional(env, excluded) -> List[str]:
    """
    Pages not reachable from the main navigation end up in Optional.
    Orphaned toctree stubs (nearly empty) and flattened category pages
    are skipped.
    """
    optional: List[str] = []
    for docname in sorted(env.found_docs):
        if docname in ("index", "404") or docname in excluded:
            continue
        metadata = env.metadata.get(docname, {})
        if metadata.get("wordcount", {}).get("words", 0) < 5:
            continue
        optional.append(docname)
    return optional


def setup(app):
    app.connect("build-finished", write_llms_txt)

    return {
        "version": "0.1",
        "parallel_write_safe": True,
    }
