"""Command-line entry point."""

import sys

from . import render


def main() -> int:
    sys.stdout.write(render(sys.stdin.read()))
    return 0
