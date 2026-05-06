from urllib.parse import urljoin

from bs4 import Tag

WIKIPEDIA_BASE = "https://en.wikipedia.org"


def extract_image(img: Tag) -> str:
    """Convert an <img> tag into Markdown, resolving the image URL."""
    src = img.get("src", "")
    alt = img.get("alt", "")
    if src.startswith("//"):
        src = "https:" + src
    elif src.startswith("/"):
        src = urljoin(WIKIPEDIA_BASE, src)
    return f"![{alt}]({src})"
