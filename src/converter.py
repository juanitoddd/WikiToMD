from bs4 import BeautifulSoup, Tag

from .images import extract_image
from .math_notation import extract_latex
from .parser import get_content_root


def to_markdown(soup: BeautifulSoup) -> str:
    """Convert a parsed Wikipedia article tree into Markdown."""
    root = get_content_root(soup)
    return _convert_node(root).strip() + "\n"


SKIP_CLASSES = frozenset({"mw-editsection", "mw-editsection-bracket"})


def _convert_node(node) -> str:
    if isinstance(node, str):
        return node

    if not isinstance(node, Tag):
        return ""

    if SKIP_CLASSES.intersection(node.get("class") or []):
        return ""

    if node.get("role") == "note":
        return ""

    style = (node.get("style") or "").replace(" ", "").lower()
    if "display:none" in style:
        return ""

    name = node.name

    if name == "style":
        return ""

    if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        level = int(name[1])
        return f"\n{'#' * level} {_convert_children(node).strip()}\n\n"

    if name == "p":
        return f"{_convert_children(node).strip()}\n\n"

    if name in {"strong", "b"}:
        return f"**{_convert_children(node).strip()}**"

    if name in {"em", "i"}:
        return f"*{_convert_children(node).strip()}*"

    if name == "a":
        href = node.get("href", "")
        text = _convert_children(node).strip()
        return f"[{text}]({href})" if href else text

    if name == "figure":
        return f"\n{_convert_children(node)}\n\n---\n\n"

    if name == "img":
        md = extract_image(node)
        if node.find_parent("figure"):
            return md
        return f"{md}\n\n---\n\n"

    if name == "math" or (name == "span" and "mwe-math-element" in node.get("class", [])):
        return extract_latex(node)

    if name == "ul":
        return _convert_list(node, ordered=False)

    if name == "ol":
        return _convert_list(node, ordered=True)

    if name == "code":
        return f"`{_convert_children(node)}`"

    if name == "pre":
        return f"\n```\n{_convert_children(node)}\n```\n\n"

    return _convert_children(node)


def _convert_children(node: Tag) -> str:
    return "".join(_convert_node(child) for child in node.children)


def _convert_list(node: Tag, ordered: bool) -> str:
    lines = []
    for i, item in enumerate(node.find_all("li", recursive=False), start=1):
        prefix = f"{i}." if ordered else "-"
        lines.append(f"{prefix} {_convert_children(item).strip()}")
    return "\n".join(lines) + "\n\n"
