import sys
from datetime import datetime


def notify(message: str) -> None:
    """Print a timestamped progress message to stderr."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}", file=sys.stderr, flush=True)
