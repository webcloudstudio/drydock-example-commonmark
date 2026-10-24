"""Autolink tests: URI and email autolinks, the rejected forms, backslash handling, and href
encoding, plus the executable's output for a whole document.

Each test compares a returned string or the executable's stdout bytes with its exact expected
value. No test matches a substring of output.
"""

import subprocess
import sys
from pathlib import Path

import pytest

from mdparser import inlines


def run_executable(project_root: Path, data: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [str(project_root / "commonmark")],
        input=data.encode("utf-8"),
        capture_output=True,
        cwd=project_root,
        check=False,
    )


# --- Declared acceptance checks (transcribed from FEATURE-Autolinks.md) ---


def test_autolinks_uri_roundtrip(project_root: Path) -> None:
    """AC autolinks-uri-roundtrip: a URI autolink is one link with the URI as href and text."""
    uri = "http://example.org/path"
    result = run_executable(project_root, "<" + uri + ">\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == f'<p><a href="{uri}">{uri}</a></p>\n'


def test_autolinks_email_mailto(project_root: Path) -> None:
    """AC autolinks-email-mailto: an email autolink renders with a mailto href."""
    address = "someone@example.org"
    result = run_executable(project_root, "<" + address + ">\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == f'<p><a href="mailto:{address}">{address}</a></p>\n'


def test_autolinks_space_not_autolink(project_root: Path) -> None:
    """AC autolinks-space-not-autolink: a URI containing a space is literal text."""
    result = run_executable(project_root, "<http://example.org/a b>\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == "<p>&lt;http://example.org/a b&gt;</p>\n"


def test_autolinks_corpus_section_passes_in_full(project_root: Path) -> None:
    """AC autolinks-corpus-section: the scoped Autolinks conformance section exits 0."""
    result = subprocess.run(
        [
            sys.executable,
            "sources/spec_tests.py",
            "--program",
            str(project_root / "commonmark"),
            "--spec",
            "sources/spec.txt",
            "--pattern",
            "^Autolinks$",
        ],
        capture_output=True,
        cwd=project_root,
        check=False,
    )
    assert result.returncode == 0


# --- URI autolinks ---


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("<http://example.org>", '<a href="http://example.org">http://example.org</a>'),
        ("<ab:x>", '<a href="ab:x">ab:x</a>'),
        ("<a+b+c:d>", '<a href="a+b+c:d">a+b+c:d</a>'),
        ("<a.b-c:d>", '<a href="a.b-c:d">a.b-c:d</a>'),
        ("<MAILTO:FOO@BAR.BAZ>", '<a href="MAILTO:FOO@BAR.BAZ">MAILTO:FOO@BAR.BAZ</a>'),
        ("<localhost:5001/foo>", '<a href="localhost:5001/foo">localhost:5001/foo</a>'),
        ("<https://../>", '<a href="https://../">https://../</a>'),
    ],
)
def test_uri_autolink_renders_the_uri_as_href_and_label(source: str, expected: str) -> None:
    assert inlines.parse_inline(source) == expected


def test_uri_scheme_of_32_characters_is_an_autolink() -> None:
    scheme = "a" + "b" * 31
    uri = scheme + ":x"
    assert inlines.parse_inline("<" + uri + ">") == f'<a href="{uri}">{uri}</a>'


def test_uri_scheme_of_33_characters_is_literal_text() -> None:
    uri = "a" * 33 + ":x"
    assert inlines.parse_inline("<" + uri + ">") == f"&lt;{uri}&gt;"


def test_one_letter_scheme_is_literal_text() -> None:
    assert inlines.parse_inline("<m:abc>") == "&lt;m:abc&gt;"


def test_scheme_starting_with_a_digit_is_literal_text() -> None:
    assert inlines.parse_inline("<1ab:x>") == "&lt;1ab:x&gt;"


def test_uri_query_ampersands_are_escaped_in_href_and_label() -> None:
    assert inlines.parse_inline("<https://e.com/?a=1&b=2>") == (
        '<a href="https://e.com/?a=1&amp;b=2">https://e.com/?a=1&amp;b=2</a>'
    )


def test_uri_non_ascii_characters_are_percent_encoded_in_href_only() -> None:
    assert inlines.parse_inline("<http://e.com/é>") == (
        '<a href="http://e.com/%C3%A9">http://e.com/é</a>'
    )


def test_uri_backtick_is_percent_encoded_in_href_only() -> None:
    assert inlines.parse_inline("<http://e.com/`x>") == (
        '<a href="http://e.com/%60x">http://e.com/`x</a>'
    )


def test_uri_with_an_existing_percent_escape_keeps_it() -> None:
    assert inlines.parse_inline("<http://e.com/a%20b>") == (
        '<a href="http://e.com/a%20b">http://e.com/a%20b</a>'
    )


@pytest.mark.parametrize("control", ["\x01", "\x09", "\x7f"])
def test_uri_containing_an_ascii_control_character_is_literal_text(control: str) -> None:
    assert inlines.parse_inline("<http://e.com/a" + control + "b>") == (
        "&lt;http://e.com/a" + control + "b&gt;"
    )


@pytest.mark.parametrize(
    ("body", "expected"),
    [
        ("http://e.com/a b", "&lt;http://e.com/a b&gt;"),
        # `<a>` is a raw HTML open tag, so only the leading `<` is escaped.
        ("http://e.com/<a", "&lt;http://e.com/<a>"),
    ],
)
def test_uri_body_with_space_or_open_angle_bracket_is_not_an_autolink(
    body: str, expected: str
) -> None:
    assert inlines.parse_inline("<" + body + ">") == expected


def test_uri_body_ending_before_a_close_angle_bracket_is_an_autolink_then_text() -> None:
    assert inlines.parse_inline("<http://e.com/a>b") == (
        '<a href="http://e.com/a">http://e.com/a</a>b'
    )


# --- Email autolinks ---


@pytest.mark.parametrize(
    ("address", "expected_href", "expected_label"),
    [
        ("foo@bar.example.com", "mailto:foo@bar.example.com", "foo@bar.example.com"),
        (
            "foo+special@Bar.baz-bar0.com",
            "mailto:foo+special@Bar.baz-bar0.com",
            "foo+special@Bar.baz-bar0.com",
        ),
        ("a@b", "mailto:a@b", "a@b"),
        (
            "a.b!#$%&'*+/=?^_`{|}~-@x.y",
            "mailto:a.b!#$%25&amp;'*+/=?%5E_%60%7B%7C%7D~-@x.y",
            "a.b!#$%&amp;'*+/=?^_`{|}~-@x.y",
        ),
    ],
)
def test_email_autolink_renders_mailto_href_and_address_label(
    address: str, expected_href: str, expected_label: str
) -> None:
    assert inlines.parse_inline("<" + address + ">") == (
        f'<a href="{expected_href}">{expected_label}</a>'
    )


@pytest.mark.parametrize(
    "address",
    [
        "foo@-bar.com",
        "foo@bar-.com",
        "foo@bar..com",
        "@bar.com",
        "foo@",
        "foo bar@x.com",
        "foo@bär.com",
    ],
)
def test_malformed_email_is_literal_text(address: str) -> None:
    assert inlines.parse_inline("<" + address + ">") == f"&lt;{address}&gt;"


def test_email_label_longer_than_63_characters_in_a_label_is_literal_text() -> None:
    label = "a" * 64
    address = "x@" + label + ".com"
    assert inlines.parse_inline("<" + address + ">") == f"&lt;{address}&gt;"


def test_email_label_of_63_characters_is_an_autolink() -> None:
    label = "a" * 63
    address = "x@" + label + ".com"
    assert inlines.parse_inline("<" + address + ">") == (
        f'<a href="mailto:{address}">{address}</a>'
    )


# --- Rejected forms and backslash handling ---


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("<>", "&lt;&gt;"),
        ("< https://foo.bar >", "&lt; https://foo.bar &gt;"),
        ("<foo.bar.baz>", "&lt;foo.bar.baz&gt;"),
        ("https://example.com", "https://example.com"),
        ("foo@bar.example.com", "foo@bar.example.com"),
    ],
)
def test_text_that_is_not_an_autolink_stays_literal(source: str, expected: str) -> None:
    assert inlines.parse_inline(source) == expected


def test_backslash_is_inert_inside_a_uri_autolink() -> None:
    assert inlines.parse_inline("<https://example.com/\\[\\>") == (
        '<a href="https://example.com/%5C%5B%5C">https://example.com/\\[\\</a>'
    )


def test_backslash_in_a_rejected_email_body_is_an_escape_of_the_next_character() -> None:
    assert inlines.parse_inline("<foo\\+@bar.example.com>") == "&lt;foo+@bar.example.com&gt;"


def test_backslash_before_less_than_prevents_an_autolink() -> None:
    assert inlines.parse_inline("\\<http://e.com>") == "&lt;http://e.com&gt;"


def test_backslash_before_ordinary_character_is_kept() -> None:
    assert inlines.parse_inline("a\\b") == "a\\b"


# --- Left-to-right scanning ---


def test_two_autolinks_in_one_line_both_render() -> None:
    assert inlines.parse_inline("<http://a.b> and <c@d.ef>") == (
        '<a href="http://a.b">http://a.b</a> and <a href="mailto:c@d.ef">c@d.ef</a>'
    )


def test_a_less_than_sign_that_cannot_open_an_autolink_does_not_hide_a_later_one() -> None:
    assert inlines.parse_inline("<a:b<http://x.y>") == (
        '&lt;a:b<a href="http://x.y">http://x.y</a>'
    )


def test_empty_content_renders_nothing() -> None:
    assert inlines.parse_inline("") == ""
