import re
from posixpath import normpath
from typing import List, Tuple

FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.DOTALL)
SOURCE_COMMENT_RE = re.compile(r"^<!-- source: .+ -->\s*$", re.MULTILINE)

# Any MyST directive or fenced code block, matched fence-to-fence. The
# info string (rest of the opening fence line) tells them apart: a
# directive starts with "{name}". Backreference (?P=fence) makes nested
# shorter fences inside the body harmless.
FENCE_RE = re.compile(
    r"^(?P<fence>`{3,}|~{3,})(?P<info>[^\n]*)\n(?P<body>.*?)^(?P=fence)[^\n]*$",
    re.DOTALL | re.MULTILINE,
)

DIRECTIVE_LABELS = {
    "note": "Note",
    "tip": "Tip",
    "warning": "Warning",
    "important": "Important",
    "caution": "Caution",
}

LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)")


def convert(source, docname, images, titles, links):
    """
    Convert a MyST source file into LLM-friendly plain markdown:
    strip frontmatter and source comments, turn MyST directives into
    readable markdown, and rewrite internal links to absolute URLs.
    Fenced code blocks are kept verbatim and shielded from rewriting.
    """
    source = FRONTMATTER_RE.sub("", source, count=1)
    source = SOURCE_COMMENT_RE.sub("", source)

    blocks: List[Tuple[str, str]] = []

    def shield(text: str) -> str:
        placeholder = "\x00PROTECTED{}\x00".format(len(blocks))
        blocks.append((placeholder, text))
        return placeholder

    def handle_fence(match) -> str:
        info = match.group("info").strip()
        if not info.startswith("{"):
            return shield(match.group(0))

        name = info[1:].partition("}")[0]
        if name == "toctree":
            return ""

        label = (
            DIRECTIVE_LABELS.get(name) or info[1 + len(name) + 1 :].strip() or "Note"
        )
        body = FENCE_RE.sub(lambda m: shield(m.group(0)), match.group("body"))
        quoted = "\n".join("> " + line for line in body.strip("\n").splitlines())
        return "**{}:**\n\n{}".format(label, quoted)

    source = FENCE_RE.sub(handle_fence, source)
    source = _rewrite_links(source, docname, images, titles, links)

    for placeholder, block in blocks:
        source = source.replace(placeholder, block)

    return source.strip() + "\n"


def _rewrite_links(source, docname, images, titles, links):
    def replace(match):
        bang, text, target = match.group(1), match.group(2), match.group(3)

        if target.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)

        path, _, anchor = target.partition("#")
        anchor = "#" + anchor if anchor else ""

        if not bang:
            stem = path[: -len(".md")] if path.endswith(".md") else path
            for candidate in (stem, stem + ".md"):
                docname_candidate = _resolve_target(docname, candidate)
                if docname_candidate in links:
                    return "[{}]({}{})".format(text, links[docname_candidate], anchor)
            if stem in ("index", "index/index"):
                return "[{}]({})".format(text, links.get("index", path))

        resolved = _resolve_target(docname, path)
        image = images.get(resolved)
        if image is not None:
            return "![{}]({})".format(text, image)

        return match.group(0)

    return LINK_RE.sub(replace, source)


def _resolve_target(docname, target):
    """
    Resolve a relative target like ../php/foo.md against the directory of
    the page containing the link. Returns the normalized path without
    leading slash, or the input unchanged when it cannot be resolved.
    """
    if target.startswith("/"):
        return normpath(target[1:])
    base = docname.rpartition("/")[0]
    if not base or base == docname:
        return normpath(target)
    return normpath("{}/{}".format(base, target))
