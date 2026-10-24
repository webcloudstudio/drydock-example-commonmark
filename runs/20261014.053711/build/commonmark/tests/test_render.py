"""Renderer and inline hook tests: HTML escaping, URL percent-encoding, the phase 2 walk, and
the inline parser hook. Each test compares a returned string with its exact expected value."""

import pytest

from mdparser import blocks, inlines, render
from mdparser.blocks import DOCUMENT, PARAGRAPH, Block, BlockRegistry, BlockType


def upper_hook(raw: str) -> str:
    return raw.upper()


def render_source(lines: list[str], hook=inlines.parse_inline) -> str:
    return render.render_document(blocks.parse_lines(lines), hook)


# --- HTML escaping ---


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("&", "&amp;"),
        ("<", "&lt;"),
        (">", "&gt;"),
        ('"', "&quot;"),
        ("'", "'"),
        ("plain", "plain"),
        ("", ""),
    ],
)
def test_escape_html_maps_each_special_character(text: str, expected: str) -> None:
    assert render.escape_html(text) == expected


def test_escape_html_does_not_escape_an_ampersand_twice() -> None:
    assert render.escape_html("<&>") == "&lt;&amp;&gt;"


def test_escape_html_leaves_existing_entity_text_as_an_escaped_ampersand() -> None:
    assert render.escape_html("&amp;") == "&amp;amp;"


# --- URL percent-encoding ---


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        ("", ""),
        ("abc", "abc"),
        ("a b", "a%20b"),
        ("é", "%C3%A9"),
        ("😀", "%F0%9F%98%80"),
        ("%20", "%20"),
        ("%zz", "%25zz"),
        ("%", "%25"),
        ("a\"b", "a%22b"),
        ("[x]", "%5Bx%5D"),
        ("http://e.com/a?b=c&d=#e", "http://e.com/a?b=c&d=#e"),
        ("a\\b", "a%5Cb"),
    ],
)
def test_percent_encode_url_encodes_only_what_must_be_encoded(url: str, expected: str) -> None:
    assert render.percent_encode_url(url) == expected


def test_percent_encode_url_is_idempotent() -> None:
    once = render.percent_encode_url("a b é%zz")
    assert render.percent_encode_url(once) == once


# --- Phase 2 walk and paragraph rendering ---


def test_empty_document_renders_nothing() -> None:
    assert render.render_document(Block(DOCUMENT), upper_hook) == ""


def test_one_paragraph_renders_as_one_p_element_with_a_line_ending() -> None:
    assert render_source(["alpha"]) == "<p>alpha</p>\n"


def test_each_paragraph_renders_with_its_own_line_ending() -> None:
    assert render_source(["alpha", "", "beta"]) == "<p>alpha</p>\n<p>beta</p>\n"


def test_paragraph_content_is_escaped_by_the_default_hook() -> None:
    assert render_source(["x < y > z & w"]) == "<p>x &lt; y &gt; z &amp; w</p>\n"


def test_phase_two_calls_the_hook_with_each_paragraphs_raw_content() -> None:
    calls: list[str] = []

    def recording_hook(raw: str) -> str:
        calls.append(raw)
        return raw

    render_source(["one", "two", "", "three"], recording_hook)
    assert calls == ["one\ntwo", "three"]


def test_phase_two_places_the_hook_output_inside_the_paragraph() -> None:
    assert render_source(["abc"], upper_hook) == "<p>ABC</p>\n"


def test_block_without_a_renderer_is_rejected() -> None:
    registry = BlockRegistry(root=DOCUMENT, fallback=PARAGRAPH)
    unknown = BlockType("unknown", continues=lambda block, cursor: False, is_container=False)
    registry.register(unknown)
    root = Block(DOCUMENT)
    root.children.append(Block(unknown))
    with pytest.raises(ValueError):
        render.render_document(root, upper_hook)


# --- Inline parser hook ---


def test_inline_hook_escapes_special_characters() -> None:
    # `<b>` is a raw HTML open tag, so it passes through; the `&` and `"` are still escaped.
    assert inlines.parse_inline("a<b>&\"c\"") == "a<b>&amp;&quot;c&quot;"


def test_inline_hook_returns_empty_text_for_empty_content() -> None:
    assert inlines.parse_inline("") == ""


def test_inline_hook_keeps_ordinary_text_unchanged() -> None:
    assert inlines.parse_inline("plain words, 123") == "plain words, 123"
