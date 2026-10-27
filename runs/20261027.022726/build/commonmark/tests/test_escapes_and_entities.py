from commonmark_parser import parse_blocks, parse_inlines, render_html
from commonmark_parser.inline import decode_escapes_and_entities


def test_ascii_punctuation_escape():
    assert decode_escapes_and_entities(r"\*") == "*"


def test_non_punctuation_backslash_remains_literal():
    assert decode_escapes_and_entities(r"\a") == r"\a"


def test_named_reference_requires_semicolon():
    assert decode_escapes_and_entities("&amp; &amp") == "& &amp"


def test_numeric_references_and_invalid_codepoints():
    assert decode_escapes_and_entities("&#65; &#x41; &#0; &#xD800;") == "A A \ufffd \ufffd"


def test_rendered_paragraph_decodes_then_html_escapes():
    document = parse_inlines(parse_blocks(r"A \* &amp; <"))
    assert render_html(document) == "<p>A * &amp; &lt;</p>\n"


def test_code_and_raw_html_keep_literal_content():
    document = parse_blocks("`&amp;`\n\n<div>&amp;</div>\n")
    assert render_html(document) == "<p><code>&amp;amp;</code></p>\n<div>&amp;</div>\n"


def test_code_spans_preserve_entities_escapes_and_escape_html():
    document = parse_inlines(parse_blocks(r"`&amp; \* <tag>`"))
    assert render_html(document) == "<p><code>&amp;amp; \\* &lt;tag&gt;</code></p>\n"


def test_code_span_matches_equal_maximal_backtick_run():
    document = parse_blocks("`` a ` b ``")
    assert render_html(document) == "<p><code>a ` b</code></p>\n"


def test_code_span_normalizes_newlines_and_one_edge_space():
    document = parse_blocks("`  a\nb  `")
    assert render_html(document) == "<p><code> a b </code></p>\n"


def test_unmatched_backtick_runs_remain_literal():
    document = parse_blocks("x `` y ` z")
    assert render_html(document) == "<p>x `` y ` z</p>\n"


def test_readme_describes_standard_streams():
    from pathlib import Path

    content = Path("README.md").read_text(encoding="utf-8")
    assert content.strip()
    assert "./commonmark" in content
    assert "standard input" in content
    assert "standard output" in content
    assert "UTF-8" in content
