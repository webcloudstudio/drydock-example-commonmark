"""Process-boundary tests for the cmark executable."""

import subprocess


def run_cmark(markdown: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["./cmark"],
        input=markdown,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )


def test_cli_stdin_stdout() -> None:
    result = run_cmark("# Hello\n\nworld\n")

    assert result.returncode == 0
    assert result.stdout == "<h1>Hello</h1>\n<p>world</p>\n"


def test_cli_accepts_utf8() -> None:
    result = run_cmark("café\n")

    assert result.returncode == 0
    assert result.stdout == "<p>café</p>\n"


def test_cli_success_contract() -> None:
    result = run_cmark("plain text\n")

    assert result.returncode == 0
    assert result.stdout == "<p>plain text</p>\n"
    assert result.stderr == ""


def test_cli_stdout_integrity() -> None:
    result = run_cmark("a\n\nb\n")

    assert result.returncode == 0
    assert result.stdout == "<p>a</p>\n<p>b</p>\n"


def test_cli_rejects_invalid_utf8_without_stdout() -> None:
    result = subprocess.run(
        ["./cmark"],
        input=b"\xff",
        capture_output=True,
        check=False,
    )

    assert result.returncode != 0
    assert result.stdout == b""
    assert result.stderr != b""
