"""Bounded verification contracts for the staged conformance harness."""

import subprocess
import sys


LEAF_SCOPE = (
    "^(Thematic breaks|ATX headings|Setext headings|Indented code blocks|"
    "Fenced code blocks|HTML blocks|Link reference definitions|Paragraphs|"
    "Blank lines)$"
)
INLINE_SCOPE = (
    "^(Code spans|Emphasis and strong emphasis|Links|Images|Autolinks|"
    "Raw HTML|Hard line breaks|Soft line breaks)$"
)


def run_scope(pattern: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            "spec_tests.py",
            "--spec",
            "spec.txt",
            "--program",
            "./program",
            "--pattern",
            pattern,
        ],
        capture_output=True,
        text=True,
        check=False,
    )


def test_leaf_conformance_scope() -> None:
    result = run_scope(LEAF_SCOPE)

    print(result.stdout)
    print(result.stderr, file=sys.stderr)
    assert result.returncode == 0


def test_inline_conformance_scope() -> None:
    result = run_scope(INLINE_SCOPE)

    print(result.stdout)
    print(result.stderr, file=sys.stderr)
    assert result.returncode == 0
