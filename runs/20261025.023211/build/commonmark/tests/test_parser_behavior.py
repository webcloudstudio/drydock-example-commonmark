"""Focused checks for public parser behavior and executable boundaries."""

import subprocess

from commonmark import parse


def test_inline_emphasis_and_code_render_as_html():
    assert parse("A *small* `code` span.\n") == (
        "<p>A <em>small</em> <code>code</code> span.</p>\n"
    )


def test_reference_definition_resolves_across_document():
    assert parse("[label]\n\n[label]: /path \"title\"\n") == (
        '<p><a href="/path" title="title">label</a></p>\n'
    )


def test_executable_rejects_invalid_utf8():
    result = subprocess.run(["./commonmark"], input=b"\xff", capture_output=True)
    assert result.returncode != 0

