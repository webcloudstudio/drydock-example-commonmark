from commonmark_parser.inlines import parse_inlines


def test_ascii_punctuation_escape_removes_marker():
    nodes = parse_inlines("\\!", {})
    assert [(node.type, node.literal) for node in nodes] == [("text", "!")]


def test_escaped_emphasis_delimiter_stays_literal():
    nodes = parse_inlines(r"\*not emphasized*", {})
    assert [(node.type, node.literal) for node in nodes] == [
        ("text", "*"), ("text", "not emphasized*")
    ]


def test_non_punctuation_escape_keeps_backslash():
    nodes = parse_inlines("\\a", {})
    assert nodes[0].literal == "\\a"


def test_named_and_numeric_references_decode():
    nodes = parse_inlines("&amp;&#65;&#x1F600;", {})
    assert [(node.type, node.literal) for node in nodes] == [("text", "&A😀")]


def test_unknown_or_unterminated_reference_remains_text():
    nodes = parse_inlines("&notARealEntity &amp", {})
    assert nodes[0].literal == "&notARealEntity &amp"


def test_invalid_numeric_scalar_replaced():
    nodes = parse_inlines("&#0;&#xD800;&#x110000;", {})
    assert nodes[0].literal == "\uFFFD" * 3


def test_soft_break_trims_spaces_on_both_sides():
    nodes = parse_inlines("alpha   \n  beta", {})
    assert [(node.type, node.literal) for node in nodes] == [
        ("text", "alpha"), ("softbreak", ""), ("text", "beta")
    ]


def test_empty_source_has_no_nodes():
    assert parse_inlines("", {}) == []


def test_code_span_preserves_entities_and_backslashes_literally():
    source = r"`literal &amp; \* text`"
    nodes = parse_inlines(source, {})
    assert [(node.type, node.literal) for node in nodes] == [("code", r"literal &amp; \* text")]


def test_code_span_normalizes_line_endings_and_removes_one_paired_space():
    nodes = parse_inlines("` alpha\r\nbeta `", {})
    assert [(node.type, node.literal) for node in nodes] == [("code", "alpha beta")]


def test_code_span_matches_only_equal_length_runs():
    nodes = parse_inlines("``a ` b``", {})
    assert [(node.type, node.literal) for node in nodes] == [("code", "a ` b")]


def test_unmatched_code_span_delimiter_remains_text():
    source = "`unclosed"
    nodes = parse_inlines(source, {})
    assert [(node.type, node.literal) for node in nodes] == [("text", source)]


def test_all_space_code_content_keeps_its_spaces():
    nodes = parse_inlines("`   `", {})
    assert [(node.type, node.literal) for node in nodes] == [("code", "   ")]


def test_code_span_splits_surrounding_text_into_ordered_nodes():
    nodes = parse_inlines("before `code` after", {})
    assert [(node.type, node.literal) for node in nodes] == [
        ("text", "before "), ("code", "code"), ("text", " after")
    ]
