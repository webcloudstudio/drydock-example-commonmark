from commonmark_parser.blocks import parse_blocks


def test_matching_bullets_form_tight_list_with_item_paragraphs():
    document = parse_blocks("- alpha\n- beta\n")
    listing = document.children[0]
    assert len(document.children) == 1
    assert (listing.type, listing.ordered, listing.tight) == ("list", False, True)
    assert [item.type for item in listing.children] == ["item", "item"]
    assert [item.children[0].literal for item in listing.children] == ["alpha", "beta"]


def test_ordered_start_and_blank_line_make_list_loose():
    listing = parse_blocks("4. first\n\n5. second\n").children[0]
    assert (listing.type, listing.ordered, listing.start, listing.tight) == ("list", True, 4, False)
    assert [item.children[0].literal for item in listing.children] == ["first", "second"]


def test_marker_kind_splits_adjacent_lists_and_thematic_break_wins():
    nodes = parse_blocks("- a\n+ b\n\n---\n").children
    assert [node.kind for node in nodes] == ["list", "list", "thematic_break"]
    assert nodes[0].children[0].children[0].literal == "a"
    assert nodes[1].children[0].children[0].literal == "b"


def test_nested_list_and_lazy_continuation_are_kept_in_item():
    listing = parse_blocks("- alpha\n  continuation\n  - nested\n").children[0]
    item = listing.children[0]
    assert item.children[0].literal == "alpha\ncontinuation"
    assert item.children[1].kind == "list"
    assert item.children[1].children[0].children[0].literal == "nested"


def test_nonempty_item_can_start_with_indented_code_and_empty_item_is_retained():
    listing = parse_blocks("-\n-     code\n").children[0]
    assert len(listing.children) == 2
    assert listing.children[0].children == []
    assert listing.children[1].children[0].kind == "indented_code"


def test_list_interrupts_paragraph_only_with_nonempty_marker_and_ordered_one():
    nodes = parse_blocks("alpha\n-\n2. no\n1. yes\n").children
    assert [node.kind for node in nodes] == ["paragraph", "list"]
    assert nodes[0].literal == "alpha\n-\n2. no"
    assert nodes[1].children[0].children[0].literal == "yes"


def test_tab_indented_blank_line_continuation_stays_inside_list_item():
    listing = parse_blocks("- foo\n\n\tbar\n").children[0]
    assert listing.kind == "list"
    assert [child.literal for child in listing.children[0].children] == ["foo", "bar"]


def test_blank_before_outdented_paragraph_does_not_loosen_list():
    document = parse_blocks("- one\n\n two\n")
    listing = document.children[0]
    assert listing.tight is True
    assert [node.kind for node in document.children] == ["list", "paragraph"]


def test_list_code_block_does_not_absorb_less_indented_following_line():
    from commonmark_parser import render

    source = "<table>\n\n  <tr>\n\n    <td>\n      Hi\n    </td>\n\n  </tr>\n\n</table>\n"
    assert render(source) == (
        "<table>\n  <tr>\n<pre><code>&lt;td&gt;\n  Hi\n&lt;/td&gt;\n</code></pre>\n"
        "  </tr>\n</table>\n"
    )


def test_blank_between_items_with_nested_lists_makes_list_loose():
    from commonmark_parser import render

    source = "- a\n  - b\n  - c\n\n- d\n  - e\n  - f\n"
    assert render(source) == (
        "<ul>\n<li><p>a</p>\n<ul>\n<li>b\n</li>\n<li>c\n</li>\n</ul>\n</li>\n"
        "<li><p>d</p>\n<ul>\n<li>e\n</li>\n<li>f\n</li>\n</ul>\n</li>\n</ul>\n"
    )


def test_blank_lines_inside_nested_list_do_not_loosen_parent_items():
    from commonmark_parser import render

    source = "- foo\n  - bar\n    - baz\n\n\n      bim\n"
    assert render(source) == (
        "<ul>\n<li>foo\n<ul>\n<li>bar\n<ul>\n"
        "<li><p>baz</p>\n<p>bim</p>\n</li>\n</ul>\n"
        "</li>\n</ul>\n</li>\n</ul>\n"
    )
