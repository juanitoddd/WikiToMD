from bs4 import BeautifulSoup


def parse_html(html: str) -> BeautifulSoup:
    """Parse raw HTML into a BeautifulSoup tree."""
    return BeautifulSoup(html, "html.parser")


def get_content_root(soup: BeautifulSoup) -> BeautifulSoup:
    """Return the main article content node, falling back to the full tree."""
    return soup.find("div", {"id": "mw-content-text"}) or soup
