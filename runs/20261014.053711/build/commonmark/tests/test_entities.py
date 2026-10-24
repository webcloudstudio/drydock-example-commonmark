"""Entity and numeric character reference tests: named references from the HTML5 table, decimal
and hexadecimal numeric references, U+FFFD replacement, decoded text as plain text, inertness in
code spans, and the shared `unescape_and_decode` helper for destinations, titles and info strings.

Each test compares a returned string, a parsed value, or the executable's stdout bytes with its
exact expected value. The declared acceptance checks are transcribed from FEATURE-Entities.md.
"""

import subprocess
from pathlib import Path

import pytest

from mdparser import entities
from mdparser.entities import match_reference, unescape_and_decode


def run_executable(project_root: Path, data: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [str(project_root / "commonmark")],
        input=data.encode("utf-8"),
        capture_output=True,
        cwd=project_root,
        check=False,
    )


def render(project_root: Path, data: str) -> str:
    result = run_executable(project_root, data)
    assert result.returncode == 0
    return result.stdout.decode("utf-8")


# --- Declared acceptance checks (transcribed from FEATURE-Entities.md) ---


def test_entities_decimal_reference(project_root: Path) -> None:
    """AC entities-decimal-reference: a decimal reference decodes to the character with the bound code point."""
    code_point = 65
    result = run_executable(project_root, "x &#" + str(code_point) + "; y\n")
    assert result.returncode == 0
    assert chr(code_point) in result.stdout.decode("utf-8")
    assert result.stdout.count(b"&#") == 0


def test_entities_hex_reference(project_root: Path) -> None:
    """AC entities-hex-reference: lowercase and uppercase hexadecimal references decode to the same character."""
    code_point = 66
    lower = "&#x" + format(code_point, "x") + ";"
    upper = "&#X" + format(code_point, "X") + ";"
    first = run_executable(project_root, lower + "\n")
    second = run_executable(project_root, upper + "\n")
    assert first.returncode == 0
    assert second.returncode == 0
    assert chr(code_point) in first.stdout.decode("utf-8")
    assert first.stdout == second.stdout


def test_entities_named_ampersand(project_root: Path) -> None:
    """AC entities-named-ampersand: the named ampersand reference round trips to the same escaped form."""
    reference = "&amp;"
    result = run_executable(project_root, "a " + reference + " b\n")
    assert result.returncode == 0
    assert reference in result.stdout.decode("utf-8")
    assert result.stdout.decode("utf-8").count("&amp;") == 1


def test_entities_unknown_stays_literal(project_root: Path) -> None:
    """AC entities-unknown-stays-literal: an unknown entity name is literal text with its ampersand escaped."""
    result = run_executable(project_root, "&MadeUpEntity;\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8").count("&amp;") == 1


def test_entities_nul_reference_replaced(project_root: Path) -> None:
    """AC entities-nul-reference-replaced: the reference for code point zero equals a literal U+FFFD."""
    first = run_executable(project_root, "&#0;\n")
    second = run_executable(project_root, chr(0xFFFD) + "\n")
    assert first.returncode == 0
    assert second.returncode == 0
    assert first.stdout == second.stdout


def test_entities_inert_in_code_span(project_root: Path) -> None:
    """AC entities-inert-in-code-span: a reference inside a code span is not decoded."""
    result = run_executable(project_root, "`&amp;`\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8").count("&amp;amp;") == 1


# --- Named references ---


@pytest.mark.parametrize(
    ("source", "character"),
    [
        ("&amp;", "&"),
        ("&lt;", "<"),
        ("&gt;", ">"),
        ("&quot;", '"'),
        ("&copy;", "©"),
        ("&AElig;", "Æ"),
        ("&nbsp;", " "),
    ],
)
def test_named_reference_decodes_to_its_character(project_root: Path, source: str, character: str) -> None:
    """A recognized named reference yields its character, escaped as text."""
    escaped = {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}.get(character, character)
    assert render(project_root, source + "\n") == f"<p>{escaped}</p>\n"


def test_named_reference_with_two_code_points_emits_both(project_root: Path) -> None:
    """A named entity that decodes to two code points emits both, in order."""
    assert unescape_and_decode("&NotEqualTilde;") == "≂̸"
    assert render(project_root, "&NotEqualTilde;\n") == "<p>≂̸</p>\n"


def test_named_reference_without_semicolon_is_literal(project_root: Path) -> None:
    """A name without its trailing semicolon is not a reference, so the ampersand is escaped."""
    assert render(project_root, "&copy\n") == "<p>&amp;copy</p>\n"


def test_named_reference_lookup_is_case_sensitive(project_root: Path) -> None:
    """`&cOpy;` is not in the table (only `&copy;` is), so it stays literal."""
    assert match_reference("&cOpy;", 0) is None
    assert render(project_root, "&cOpy;\n") == "<p>&amp;cOpy;</p>\n"


def test_unknown_name_returns_no_match() -> None:
    assert match_reference("&MadeUpEntity;", 0) is None


def test_named_reference_returns_value_and_end() -> None:
    assert match_reference("x &copy; y", 2) == ("©", 8)


# --- Decimal references ---


@pytest.mark.parametrize(
    ("source", "character"),
    [
        ("&#65;", "A"),
        ("&#0000065;", "A"),
        ("&#97;", "a"),
        ("&#9731;", "☃"),
    ],
)
def test_decimal_reference_decodes(project_root: Path, source: str, character: str) -> None:
    assert render(project_root, source + "\n") == f"<p>{character}</p>\n"


def test_decimal_reference_accepts_seven_digits_at_most() -> None:
    """A decimal reference of 8 digits is not recognized."""
    assert match_reference("&#00000065;", 0) is None
    assert match_reference("&#0000065;", 0) == ("A", 10)


def test_decimal_reference_with_no_digits_is_literal(project_root: Path) -> None:
    assert render(project_root, "&#;\n") == "<p>&amp;#;</p>\n"


# --- Hexadecimal references ---


@pytest.mark.parametrize(
    ("source", "character"),
    [
        ("&#x41;", "A"),
        ("&#X41;", "A"),
        ("&#x2603;", "☃"),
        ("&#x1F600;", "\U0001F600"),
    ],
)
def test_hexadecimal_reference_decodes(project_root: Path, source: str, character: str) -> None:
    assert render(project_root, source + "\n") == f"<p>{character}</p>\n"


def test_hexadecimal_reference_accepts_six_digits_at_most() -> None:
    """A hexadecimal reference of 7 digits is not recognized."""
    assert match_reference("&#x0000041;", 0) is None
    assert match_reference("&#x000041;", 0) == ("A", 10)


def test_decimal_digits_are_not_read_as_hexadecimal(project_root: Path) -> None:
    """`&#41;` is decimal 41, the `)` character, not a hexadecimal reference."""
    assert render(project_root, "&#41;\n") == "<p>)</p>\n"


# --- Invalid code points ---


@pytest.mark.parametrize(
    "source",
    [
        "&#0;",
        "&#x0;",
        "&#xD800;",
        "&#xDFFF;",
        "&#55296;",
        "&#x110000;",
        "&#1114112;",
        "&#9999999;",
    ],
)
def test_invalid_code_point_becomes_replacement_character(project_root: Path, source: str) -> None:
    assert render(project_root, source + "\n") == "<p>�</p>\n"


def test_last_valid_code_point_is_kept() -> None:
    assert match_reference("&#x10FFFF;", 0) == ("\U0010FFFF", 10)


def test_first_code_point_after_surrogates_is_kept() -> None:
    assert match_reference("&#xE000;", 0) == ("", 8)


# --- Decoded characters are plain text ---


def test_decoded_asterisks_do_not_open_emphasis(project_root: Path) -> None:
    assert render(project_root, "&#42;foo&#42;\n") == "<p>*foo*</p>\n"


def test_decoded_hash_does_not_start_heading(project_root: Path) -> None:
    assert render(project_root, "&#35; word\n") == "<p># word</p>\n"


def test_decoded_angle_brackets_are_escaped_text(project_root: Path) -> None:
    """A decoded `<` is text and not the start of raw HTML."""
    assert render(project_root, "&lt;b&gt;bold&lt;/b&gt;\n") == "<p>&lt;b&gt;bold&lt;/b&gt;</p>\n"


def test_numeric_angle_bracket_is_escaped_text(project_root: Path) -> None:
    assert render(project_root, "&#60;b&#62;\n") == "<p>&lt;b&gt;</p>\n"


def test_decoded_ampersand_is_not_decoded_again(project_root: Path) -> None:
    """`&amp;amp;` decodes once to `&amp;` text; the second `amp;` is not re-decoded."""
    assert render(project_root, "&amp;amp;\n") == "<p>&amp;amp;</p>\n"


def test_numeric_ampersand_is_escaped(project_root: Path) -> None:
    assert render(project_root, "&#38;\n") == "<p>&amp;</p>\n"


# --- Inertness and ordinary text ---


def test_references_inside_code_span_stay_literal(project_root: Path) -> None:
    assert render(project_root, "`&#65;`\n") == "<p><code>&amp;#65;</code></p>\n"


def test_multiple_references_in_one_paragraph(project_root: Path) -> None:
    assert render(project_root, "&#65;&#66;&#x43;\n") == "<p>ABC</p>\n"


def test_bare_ampersand_is_escaped(project_root: Path) -> None:
    assert render(project_root, "AT&T\n") == "<p>AT&amp;T</p>\n"


def test_ampersand_at_end_of_line_is_escaped(project_root: Path) -> None:
    assert render(project_root, "AT&\n") == "<p>AT&amp;</p>\n"


def test_empty_input_renders_nothing(project_root: Path) -> None:
    result = run_executable(project_root, "")
    assert result.returncode == 0
    assert result.stdout == b""


# --- Shared helper for destinations, titles and info strings ---


def test_helper_decodes_a_reference() -> None:
    assert unescape_and_decode("&#x26;") == "&"


def test_helper_decodes_named_reference() -> None:
    assert unescape_and_decode("a&copy;b") == "a©b"


def test_helper_backslash_then_reference_is_not_decoded() -> None:
    """A backslash escapes the ampersand, so the reference is not read: `\\&amp;` gives `&amp;`."""
    assert unescape_and_decode("\\&amp;") == "&amp;"


def test_helper_reference_then_backslash_escape() -> None:
    assert unescape_and_decode("&#42;\\*") == "**"


def test_helper_keeps_unrecognized_reference() -> None:
    assert unescape_and_decode("&copy") == "&copy"


def test_helper_keeps_backslash_before_non_punctuation() -> None:
    assert unescape_and_decode("\\A&#65;") == "\\AA"


def test_helper_empty_string() -> None:
    assert unescape_and_decode("") == ""


def test_helper_replaces_nul_reference() -> None:
    assert unescape_and_decode("&#0;") == "�"


def test_unescape_still_leaves_references_alone() -> None:
    """The backslash-only helper does not decode references."""
    assert entities.unescape("&amp;\\*") == "&amp;*"


def test_decode_helper_never_returns_a_partial_reference() -> None:
    """Text that looks like a reference but is cut short comes back unchanged."""
    assert unescape_and_decode("&#x41") == "&#x41"
    assert unescape_and_decode("&amp") == "&amp"
