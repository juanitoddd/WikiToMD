import argparse
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

from .converter import to_markdown
from .fetcher import fetch_article
from .notifier import notify
from .parser import parse_html


def slug_from_url(url: str) -> str:
    """Extract the article slug from a Wikipedia URL, lowercased."""
    path = urlparse(url).path
    last = path.rstrip("/").rsplit("/", 1)[-1]
    return unquote(last).lower() or "article"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="wikiToMd",
        description="Convert a Wikipedia article URL into Markdown.",
    )
    parser.add_argument("url", help="Wikipedia article URL")
    parser.add_argument(
        "-o", "--output",
        help="Output folder. The file is auto-named from the article slug "
             "(e.g. .../Discrete_logarithm -> discrete_logarithm.md). "
             "Defaults to stdout.",
        default=None,
    )
    args = parser.parse_args(argv)

    notify(f"Fetching {args.url}")
    html = fetch_article(args.url)

    notify("Parsing HTML")
    soup = parse_html(html)

    notify("Converting to Markdown")
    markdown = to_markdown(soup)

    if args.output:
        folder = Path(args.output)
        folder.mkdir(parents=True, exist_ok=True)
        out_path = folder / f"{slug_from_url(args.url)}.md"
        out_path.write_text(markdown, encoding="utf-8")
        notify(f"Wrote {out_path}")
    else:
        sys.stdout.write(markdown)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
