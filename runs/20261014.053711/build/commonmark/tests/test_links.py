"""Link tests: the look-for-link-or-image procedure, inline and reference forms, and their grammar.

The declared acceptance checks are transcribed from FEATURE-Links.md with their assertions kept as
written. The remaining tests compare the returned HTML string, or the executable's stdout, with its
exact expected value. Reference maps are built per test, so no state is shared between tests.
"""

import subprocess
from pathlib import Path

from mdparser import inlines
from mdparser.refs import ReferenceMap


def run_executable(project_root: Path, data: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [str(project_root / "commonmark")],
        input=data.encode("utf-8"),
        capture_output=True,
        cwd=project_root,
        check=False,
    )


def references_with(*definitions: tuple[str, str, str | None]) -> ReferenceMap:
    """A fresh reference map holding each (label, destination, title) definition."""
    references = ReferenceMap()
    for label, destination, title in definitions:
        references.add(label, destination, title)
    return references


def parse(source: str, references: ReferenceMap | None = None) -> str:
    return inlines.parse_inline(source, references)


# --- Declared acceptance checks (transcribed from FEATURE-Links.md) ---


def test_links_inline_destination_and_title(project_root: Path) -> None:
    """AC links-inline-destination-and-title: an inline link renders one a element with its parts."""
    text = "label"
    dest = "/uri"
    title = "the title"
    source = "[" + text + "](" + dest + ' "' + title + '")\n'
    result = subprocess.run(
        [str(project_root / "commonmark")],
        input=source,
        capture_output=True,
        text=True,
        cwd=project_root,
        check=False,
    )
    print(result.stdout)
    assert result.returncode == 0
    assert result.stdout.count("<a ") == 1
    assert ('href="' + dest + '"') in result.stdout
    assert ('title="' + title + '"') in result.stdout
    assert (">" + text + "</a>") in result.stdout


def test_links_reference_forms(project_root: Path) -> None:
    """AC links-reference-forms: full, collapsed and shortcut references each render one a element."""
    definition = "\n\n[foo]: /url\n"
    for use in ("[text][foo]", "[foo][]", "[foo]"):
        result = subprocess.run(
            [str(project_root / "commonmark")],
            input=(use + definition).encode("utf-8"),
            capture_output=True,
            cwd=project_root,
            check=False,
        )
        print(result.stdout)
        assert result.returncode == 0
        assert result.stdout.decode("utf-8").count("<a ") == 1


def test_links_reference_case_insensitive(project_root: Path) -> None:
    """AC links-reference-case-insensitive: label matching ignores case."""
    result = run_executable(project_root, "[FOO]\n\n[foo]: /url\n")
    stdout = result.stdout.decode("utf-8")
    print(stdout)
    assert result.returncode == 0
    assert stdout.count("<a ") == 1


def test_links_undefined_reference_literal(project_root: Path) -> None:
    """AC links-undefined-reference-literal: a shortcut reference with no definition stays literal."""
    result = run_executable(project_root, "[nothing defined]\n")
    stdout = result.stdout.decode("utf-8")
    print(stdout)
    assert result.returncode == 0
    assert stdout.count("<a ") == 0


def test_links_no_nested_links(project_root: Path) -> None:
    """AC links-no-nested-links: a link inside link text wins and the outer brackets stay literal."""
    result = run_executable(project_root, "[foo [bar](/uri)](/uri)\n")
    stdout = result.stdout.decode("utf-8")
    print(stdout)
    assert result.returncode == 0
    assert stdout.count("<a ") == 1


def test_links_space_before_parenthesis(project_root: Path) -> None:
    """AC links-space-before-parenthesis: whitespace between link text and the parenthesis is no link."""
    result = run_executable(project_root, "[link] (/uri)\n")
    stdout = result.stdout.decode("utf-8")
    print(stdout)
    assert result.returncode == 0
    assert stdout.count("<a ") == 0


# --- Inline form: destination and title grammar ---


def test_inline_link_renders_exact_element() -> None:
    assert parse("[a](/u)") == '<a href="/u">a</a>'


def test_inline_link_destination_is_optional() -> None:
    assert parse("[a]()") == '<a href="">a</a>'


def test_inline_link_title_in_single_quotes() -> None:
    assert parse("[a](/u 'T')") == '<a href="/u" title="T">a</a>'


def test_inline_link_title_in_parentheses() -> None:
    assert parse("[a](/u (T))") == '<a href="/u" title="T">a</a>'


def test_inline_link_title_escaped_quote_is_unescaped_then_escaped() -> None:
    assert parse('[a](/u "say \\"hi\\"")') == '<a href="/u" title="say &quot;hi&quot;">a</a>'


def test_inline_link_empty_title_is_omitted() -> None:
    assert parse('[a](/u "")') == '<a href="/u">a</a>'


def test_inline_link_angle_destination_allows_spaces() -> None:
    assert parse("[a](<my uri>)") == '<a href="my%20uri">a</a>'


def test_inline_link_angle_destination_rejects_inner_angle() -> None:
    # The `<c>` after the first `<` is a raw HTML tag, so it passes through unescaped.
    assert parse("[a](<b<c>)") == "[a](&lt;b<c>)"


def test_inline_link_balanced_parentheses_in_destination() -> None:
    assert parse("[a](foo(and(bar)))") == '<a href="foo(and(bar))">a</a>'


def test_inline_link_escaped_parentheses_in_destination() -> None:
    assert parse("[a](\\(x\\))") == '<a href="(x)">a</a>'


def test_inline_link_unbalanced_parenthesis_is_no_link() -> None:
    assert parse("[a](foo(bar)") == "[a](foo(bar)"


def test_inline_link_space_in_bare_destination_is_no_link() -> None:
    assert parse("[a](my uri)") == "[a](my uri)"


def test_inline_link_destination_is_percent_encoded() -> None:
    assert parse("[a](/ü)") == '<a href="/%C3%BC">a</a>'


def test_inline_link_destination_keeps_existing_percent_escape() -> None:
    assert parse("[a](/a%20b)") == '<a href="/a%20b">a</a>'


def test_inline_link_destination_entity_is_decoded_then_escaped() -> None:
    assert parse("[a](&amp;x)") == '<a href="&amp;x">a</a>'


def test_inline_link_whitespace_and_one_line_ending_around_parts() -> None:
    assert parse('[a](  /u \n "t"  )') == '<a href="/u" title="t">a</a>'


def test_inline_link_title_needs_whitespace_before_it() -> None:
    # Without whitespace the quotes belong to the bare destination, which percent-encodes them.
    assert parse('[a](/u"t")') == '<a href="/u%22t%22">a</a>'


def test_inline_link_title_quoted_destination_is_destination() -> None:
    assert parse('[a]("b")') == '<a href="%22b%22">a</a>'


def test_inline_link_text_with_balanced_brackets() -> None:
    assert parse("[a [b] c](/u)") == '<a href="/u">a [b] c</a>'


def test_inline_link_text_with_escaped_bracket() -> None:
    assert parse("[a\\]b](/u)") == '<a href="/u">a]b</a>'


def test_inline_link_code_span_binds_tighter_than_bracket() -> None:
    assert parse("[a `]`](/u)") == '<a href="/u">a <code>]</code></a>'


def test_inline_link_text_holds_emphasis() -> None:
    assert parse("[*a*](/u)") == '<a href="/u"><em>a</em></a>'


def test_emphasis_can_wrap_a_link() -> None:
    assert parse("*[a](/u)*") == '<em><a href="/u">a</a></em>'


def test_inline_link_ampersand_in_text_is_escaped() -> None:
    assert parse("[a & b](/u)") == '<a href="/u">a &amp; b</a>'


# --- Reference forms ---


def test_full_reference_uses_its_own_label() -> None:
    references = references_with(("bar", "/url", None))
    assert parse("[foo][bar]", references) == '<a href="/url">foo</a>'


def test_full_reference_with_undefined_label_is_literal() -> None:
    references = references_with(("foo", "/url", None))
    assert parse("[foo][bar]", references) == "[foo][bar]"


def test_shortcut_before_undefined_full_label_is_not_a_link() -> None:
    references = references_with(("foo", "/url", None))
    assert parse("[foo][bar][baz]", references) == "[foo][bar][baz]"


def test_full_reference_then_defined_label_links_the_second_pair() -> None:
    references = references_with(("baz", "/url", None))
    assert parse("[foo][bar][baz]", references) == '[foo]<a href="/url">bar</a>'


def test_collapsed_reference_resolves_text_as_label() -> None:
    references = references_with(("foo", "/url", None))
    assert parse("[foo][]", references) == '<a href="/url">foo</a>'


def test_collapsed_reference_with_undefined_label_is_literal() -> None:
    references = references_with(("bar", "/url", None))
    assert parse("[foo][]", references) == "[foo][]"


def test_shortcut_reference_resolves_text_as_label() -> None:
    references = references_with(("foo", "/url", None))
    assert parse("[foo]", references) == '<a href="/url">foo</a>'


def test_shortcut_reference_with_undefined_label_is_literal() -> None:
    references = references_with(("foo", "/url", None))
    assert parse("[bar]", references) == "[bar]"


def test_shortcut_reference_followed_by_parenthesis_that_is_no_link() -> None:
    references = references_with(("foo", "/url", None))
    assert parse("[foo](not a link)", references) == '<a href="/url">foo</a>(not a link)'


def test_shortcut_reference_followed_by_blank_brackets_is_still_shortcut() -> None:
    references = references_with(("foo", "/url", None))
    assert parse("[foo][ ]", references) == '<a href="/url">foo</a>[ ]'


def test_reference_takes_definition_title() -> None:
    references = references_with(("foo", "/url", "T"))
    assert parse("[foo]", references) == '<a href="/url" title="T">foo</a>'


def test_reference_label_collapses_whitespace_and_case() -> None:
    references = references_with(("foo bar", "/url", None))
    assert parse("[Foo   BAR]", references) == '<a href="/url">Foo   BAR</a>'


def test_reference_label_of_maximum_length_matches() -> None:
    label = "a" * 999
    references = references_with((label, "/url", None))
    assert parse("[" + label + "]", references) == '<a href="/url">' + label + "</a>"


def test_reference_label_over_maximum_length_is_literal() -> None:
    label = "a" * 1000
    references = references_with((label, "/url", None))
    assert parse("[" + label + "]", references) == "[" + label + "]"


def test_blank_shortcut_text_is_not_a_label() -> None:
    references = references_with((" ", "/url", None))
    assert parse("[ ]", references) == "[ ]"


def test_reference_destination_is_percent_encoded_on_render() -> None:
    references = references_with(("foo", "/ü", None))
    assert parse("[foo]", references) == '<a href="/%C3%BC">foo</a>'


# --- Nesting, deactivation and literal brackets ---


def test_inner_link_wins_and_outer_brackets_stay_literal() -> None:
    assert parse("[foo [bar](/uri)](/uri)") == '[foo <a href="/uri">bar</a>](/uri)'


def test_link_inside_brackets_deactivates_the_outer_opener() -> None:
    references = references_with(("x", "/url", None))
    assert parse("[[x]]", references) == '[<a href="/url">x</a>]'


def test_unmatched_closing_bracket_is_literal() -> None:
    assert parse("a] b") == "a] b"


def test_unmatched_opening_bracket_is_literal() -> None:
    assert parse("a [ b") == "a [ b"


def test_unmatched_opener_is_literal_while_emphasis_pairs_across_it() -> None:
    assert parse("*foo [bar* baz") == "<em>foo [bar</em> baz"


def test_escaped_opening_bracket_does_not_open_a_link() -> None:
    assert parse("\\[a](/u)") == "[a](/u)"


def test_space_before_parenthesis_is_no_link() -> None:
    assert parse("[link] (/uri)") == "[link] (/uri)"


def test_image_construct_is_rendered_as_an_image_not_a_link() -> None:
    assert parse("![foo](/url)") == '<img src="/url" alt="foo" />'


def test_image_opener_does_not_deactivate_earlier_link_openers() -> None:
    assert parse("[a ![b](/i) c](/u)") == '<a href="/u">a <img src="/i" alt="b" /> c</a>'


# --- Executable: definitions reach paragraphs that use them ---


def test_definition_after_use_resolves_through_executable(project_root: Path) -> None:
    result = run_executable(project_root, "[foo]\n\n[foo]: /url\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == '<p><a href="/url">foo</a></p>\n'


def test_definition_title_resolves_through_executable(project_root: Path) -> None:
    result = run_executable(project_root, '[foo]\n\n[foo]: /url "T"\n')
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == '<p><a href="/url" title="T">foo</a></p>\n'


def test_inline_link_through_executable(project_root: Path) -> None:
    result = run_executable(project_root, '[a](/u "t")\n')
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == '<p><a href="/u" title="t">a</a></p>\n'
