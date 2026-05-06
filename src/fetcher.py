import requests

USER_AGENT = "wikiToMd/0.1 (https://github.com/; contact: data@23degrees.io)"


def fetch_article(url: str) -> str:
    """Fetch the raw HTML of a Wikipedia article."""
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    response.raise_for_status()
    return response.text
