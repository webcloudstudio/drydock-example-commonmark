"""Standard input/output command-line interface."""

import sys

from .parser import parse


def main() -> int:
    """Read UTF-8 Markdown from stdin and write rendered HTML to stdout."""
    source = sys.stdin.buffer.read().decode("utf-8")
    sys.stdout.write(parse(source))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
