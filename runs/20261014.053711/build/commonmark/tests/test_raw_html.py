"""Raw inline HTML tests: open, closing, empty-element and attribute forms, comments, processing
instructions, declarations and CDATA sections, the rejected forms, and backslash inertness.

Each test compares a returned string or the executable's stdout bytes with its exact expected
value. No test matches a substring of output.
"""

import subprocess
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


# --- Declared acceptance checks (transcribed from FEATURE-Raw-HTML.md) ---


def test_rawhtml_open_and_close_tags_pass_through(project_root: Path) -> None:
    """AC rawhtml-open-and-close-tags: open, self-closing and closing tags pass through verbatim."""
    tags = '<a><bab><c2c> <a href="x" data-k=v /> </a></foo >'
    result = run_executable(project_root, "Foo " + tags + "\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == f"<p>Foo {tags}</p>\n"


@pytest.mark.parametrize(
    "fragment",
    ["<!-- a comment -->", "<?php echo $a; ?>", "<!ELEMENT br EMPTY>", "<![CDATA[>&<]]>"],
)
def test_rawhtml_comment_pi_declaration_cdata_pass_through(
    project_root: Path, fragment: str
) -> None:
    """AC rawhtml-comment-pi-declaration-cdata: each construct passes through verbatim."""
    result = run_executable(project_root, "foo " + fragment + " bar\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == f"<p>foo {fragment} bar</p>\n"


def test_rawhtml_illegal_forms_are_escaped(project_root: Path) -> None:
    """AC rawhtml-illegal-forms-escaped: an illegal tag name is escaped text, not raw HTML."""
    result = run_executable(project_root, "<33> <__>\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == "<p>&lt;33&gt; &lt;__&gt;</p>\n"


def test_rawhtml_closing_tag_with_attributes_is_escaped(project_root: Path) -> None:
    """AC rawhtml-closing-tag-with-attributes: a closing tag with attributes is escaped text."""
    result = run_executable(project_root, '</a href="foo">\n')
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == "<p>&lt;/a href=&quot;foo&quot;&gt;</p>\n"


def test_rawhtml_backslash_in_attribute_value_is_inert(project_root: Path) -> None:
    """AC rawhtml-backslash-inert: a backslash inside a tag attribute value is kept as written."""
    tag = '<a href="\\*">'
    result = run_executable(project_root, "foo " + tag + "\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == f"<p>foo {tag}</p>\n"


# --- Open, closing and empty-element tags ---


@pytest.mark.parametrize(
    "tag",
    [
        "<a>",
        "<a/>",
        "<a  />",
        "<b2/>",
        "<a-b c-d>",
        "<a h=x>",
        "<a h='x'>",
        '<a h="x y">',
        "<a b>",
        "<a b c>",
        "<a b = c>",
        "<a _b:c.d-e=1>",
        "<a\nb>",
        "<a  /><b2\ndata=\"foo\" >",
        "<a \n  b=\"c\">",
    ],
)
def test_legal_open_tag_passes_through_unchanged(tag: str) -> None:
    assert inlines.parse_inline(tag) == tag


@pytest.mark.parametrize("tag", ["</a>", "</a >", "</a\n>", "</a\t  >", "</a-b2>"])
def test_legal_closing_tag_passes_through_unchanged(tag: str) -> None:
    assert inlines.parse_inline(tag) == tag


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ('<a b="x"c>', "&lt;a b=&quot;x&quot;c&gt;"),
        ('<a b="unclosed>', "&lt;a b=&quot;unclosed&gt;"),
        ("<a b=>", "&lt;a b=&gt;"),
        ("<a b=x y='z>", "&lt;a b=x y='z&gt;"),
        ('<a b=x"y>', "&lt;a b=x&quot;y&gt;"),
        ("<a=b>", "&lt;a=b&gt;"),
        ("<1a>", "&lt;1a&gt;"),
        ("<-a>", "&lt;-a&gt;"),
        ("<a b=c<d>", "&lt;a b=c<d>"),
        ("<a b=c`>", "&lt;a b=c`&gt;"),
        ("<a\n\nb>", "&lt;a\n\nb&gt;"),
        ("</a/>", "&lt;/a/&gt;"),
        ("</a b>", "&lt;/a b&gt;"),
        ("</>", "&lt;/&gt;"),
        ("<a/ >", "&lt;a/ &gt;"),
        ("<a b c", "&lt;a b c"),
    ],
)
def test_illegal_tag_form_is_escaped_text(source: str, expected: str) -> None:
    assert inlines.parse_inline(source) == expected


def test_attribute_value_containing_a_backslash_is_passed_through() -> None:
    assert inlines.parse_inline('<a href="\\*">') == '<a href="\\*">'


def test_unquoted_attribute_value_containing_a_backslash_is_passed_through() -> None:
    assert inlines.parse_inline("<a b=\\*>") == "<a b=\\*>"


def test_entity_text_in_attribute_value_is_passed_through_unchanged() -> None:
    assert inlines.parse_inline('<a title="&amp;&copy;">') == '<a title="&amp;&copy;">'


def test_quoted_attribute_value_may_span_a_line_ending() -> None:
    assert inlines.parse_inline('<a b="x\ny">') == '<a b="x\ny">'


# --- Comments ---


@pytest.mark.parametrize(
    "comment",
    [
        "<!-->",
        "<!--->",
        "<!---->",
        "<!-- a comment -->",
        "<!-- a -- b -->",
        "<!--\nline one\nline two\n-->",
        "<!-- > -->",
    ],
)
def test_legal_comment_passes_through_unchanged(comment: str) -> None:
    assert inlines.parse_inline(comment) == comment


@pytest.mark.parametrize(
    ("source", "expected"),
    [("<!-- unclosed", "&lt;!-- unclosed"), ("<!--", "&lt;!--"), ("<!---", "&lt;!---")],
)
def test_unclosed_comment_is_escaped_text(source: str, expected: str) -> None:
    assert inlines.parse_inline(source) == expected


# --- Processing instructions ---


@pytest.mark.parametrize("instruction", ["<?php echo $a; ?>", "<??>", "<? x\ny ?>", "<?>?>"])
def test_legal_processing_instruction_passes_through_unchanged(instruction: str) -> None:
    assert inlines.parse_inline(instruction) == instruction


def test_unclosed_processing_instruction_is_escaped_text() -> None:
    assert inlines.parse_inline("<?php echo") == "&lt;?php echo"


# --- Declarations ---


@pytest.mark.parametrize("declaration", ["<!ELEMENT br EMPTY>", "<!DOCTYPE html>", "<!a>"])
def test_legal_declaration_passes_through_unchanged(declaration: str) -> None:
    assert inlines.parse_inline(declaration) == declaration


@pytest.mark.parametrize(
    ("source", "expected"),
    [("<! x>", "&lt;! x&gt;"), ("<!1x>", "&lt;!1x&gt;"), ("<!a", "&lt;!a"), ("<!>", "&lt;!&gt;")],
)
def test_illegal_declaration_is_escaped_text(source: str, expected: str) -> None:
    assert inlines.parse_inline(source) == expected


# --- CDATA sections ---


@pytest.mark.parametrize("section", ["<![CDATA[>&<]]>", "<![CDATA[]]>", "<![CDATA[a\nb]]>"])
def test_legal_cdata_section_passes_through_unchanged(section: str) -> None:
    assert inlines.parse_inline(section) == section


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("<![CDATA[ unclosed", "&lt;![CDATA[ unclosed"),
        ("<![cdata[x]]>", "&lt;![cdata[x]]&gt;"),
    ],
)
def test_illegal_cdata_section_is_escaped_text(source: str, expected: str) -> None:
    assert inlines.parse_inline(source) == expected


# --- Backslash handling and precedence ---


def test_backslash_before_less_than_prevents_a_raw_tag() -> None:
    assert inlines.parse_inline("\\<b>") == "&lt;b&gt;"


def test_raw_tag_text_between_escaped_text_keeps_its_order() -> None:
    assert inlines.parse_inline("AT&T <b>x</b> & <i>") == "AT&amp;T <b>x</b> &amp; <i>"


def test_raw_tag_inside_text_keeps_surrounding_escapes() -> None:
    assert inlines.parse_inline('say "hi" <b class="x">') == 'say &quot;hi&quot; <b class="x">'


def test_two_raw_tags_in_one_line_both_pass_through() -> None:
    assert inlines.parse_inline("<a><b>") == "<a><b>"


def test_a_less_than_sign_that_cannot_open_raw_html_does_not_hide_a_later_tag() -> None:
    assert inlines.parse_inline("<3 <b>") == "&lt;3 <b>"


def test_empty_content_renders_nothing() -> None:
    assert inlines.parse_inline("") == ""
