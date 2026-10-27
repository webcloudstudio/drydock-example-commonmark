from commonmark_parser import parse_blocks, parse_inlines, render_html


def rendered(source: str) -> str:
    return render_html(parse_inlines(parse_blocks(source)))


def test_emphasis_and_strong_emphasis_nest():
    assert rendered("*a **b** c*") == "<p><em>a <strong>b</strong> c</em></p>\n"


def test_unmatched_delimiters_remain_literal():
    assert rendered("a * b ** c") == "<p>a * b ** c</p>\n"


def test_underscore_does_not_open_inside_a_word():
    assert rendered("a_b_c") == "<p>a_b_c</p>\n"


def test_unicode_symbols_count_as_punctuation_for_flanking():
    assert rendered("*$*alpha.") == "<p>*$*alpha.</p>\n"
