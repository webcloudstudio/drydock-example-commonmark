"""Link reference definitions: label normalization, the reference map, extraction at paragraph close,
and the `commonmark` executable's output for definition-only and definition-plus-paragraph input.

The four declared checks from FEATURE-Link-Reference-Definitions.md are transcribed first, with
their assertions unchanged. The remaining tests act on the parser and read the reference map or
the block tree back, or compare the exact stdout bytes the executable hands back.
"""

import subprocess
from pathlib import Path

import pytest

from mdparser import blocks
from mdparser.refs import LinkReference, ReferenceMap, extract_definitions, normalize_label


def run_commonmark(project_root: Path, source: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(project_root / "commonmark")],
        input=source,
        capture_output=True,
        text=True,
        cwd=project_root,
        check=False,
    )


def extract(text: str) -> tuple[str, ReferenceMap]:
    """Run extraction on paragraph text and return the remainder and the map it filled."""
    references = ReferenceMap()
    remainder = extract_definitions(text, references)
    return remainder, references


# --- Declared acceptance checks (transcribed from FEATURE-Link-Reference-Definitions.md) ---


def test_defs_definition_only_renders_nothing(project_root: Path) -> None:
    """A document that is only a definition, with or without a title or angle brackets, renders no paragraph."""
    for source in ['[foo]: /url "title"\n', "[foo]:\n/url\n'title'\n", "[foo]: <>\n"]:
        result = run_commonmark(project_root, source)
        assert result.returncode == 0
        assert result.stdout.count("<p>") == 0


def test_defs_remainder_is_paragraph(project_root: Path) -> None:
    """Text after a definition stays as one paragraph."""
    rest = "remaining text"
    result = run_commonmark(project_root, "[foo]: /url\n" + rest + "\n")
    assert result.returncode == 0
    assert result.stdout.count("<p>") == 1
    assert rest in result.stdout


def test_defs_trailing_text_not_definition(project_root: Path) -> None:
    """Extra text after the title means the line is not a definition, so it stays a paragraph."""
    result = run_commonmark(project_root, '[foo]: /url "title" ok\n')
    assert result.returncode == 0
    assert result.stdout.count("<p>") == 1


def test_defs_cannot_interrupt_paragraph(project_root: Path) -> None:
    """A definition line directly after paragraph text is part of that paragraph."""
    definition = "[bar]: /baz"
    result = run_commonmark(project_root, "Foo\n" + definition + "\n")
    assert result.returncode == 0
    assert result.stdout.count("<p>") == 1
    assert definition in result.stdout


def test_defs_title_with_blank_line(project_root: Path) -> None:
    """A title containing a blank line is not valid, so the two halves become two paragraphs."""
    result = run_commonmark(project_root, "[foo]: /url 'title\n\nwith blank line'\n")
    assert result.returncode == 0
    assert result.stdout.count("<p>") == 2


# --- normalize_label ---


def test_normalize_label_strips_the_brackets() -> None:
    assert normalize_label("[foo]") == "foo"


def test_normalize_label_leaves_an_unbracketed_label_unchanged() -> None:
    assert normalize_label("foo") == "foo"


def test_normalize_label_applies_case_folding() -> None:
    assert normalize_label("[Foo]") == "foo"


def test_normalize_label_folds_sharp_s_to_ss() -> None:
    assert normalize_label("[ẞ]") == normalize_label("[SS]") == "ss"


def test_normalize_label_collapses_internal_whitespace_to_one_space() -> None:
    assert normalize_label("[foo  \t bar\nbaz]") == "foo bar baz"


def test_normalize_label_strips_outer_whitespace() -> None:
    assert normalize_label("[  foo  ]") == "foo"


def test_normalize_label_keeps_internal_punctuation() -> None:
    assert normalize_label("[a-b_c]") == "a-b_c"


# --- ReferenceMap ---


def test_reference_map_starts_empty() -> None:
    assert len(ReferenceMap()) == 0


def test_reference_map_get_returns_none_for_an_absent_label() -> None:
    assert ReferenceMap().get("foo") is None


def test_reference_map_stores_destination_and_title() -> None:
    references = ReferenceMap()
    references.add("[foo]", "/url", "title")
    assert references.get("foo") == LinkReference("/url", "title")


def test_reference_map_stores_an_untitled_definition_with_no_title() -> None:
    references = ReferenceMap()
    references.add("[foo]", "/url")
    assert references.get("foo") == LinkReference("/url", None)


def test_reference_map_matches_on_normalized_labels() -> None:
    references = ReferenceMap()
    references.add("[Foo   Bar]", "/url")
    assert references.get("[foo bar]") == LinkReference("/url", None)


def test_reference_map_first_definition_wins() -> None:
    references = ReferenceMap()
    references.add("[foo]", "/first")
    references.add("[FOO]", "/second")
    assert references.get("foo") == LinkReference("/first", None)
    assert len(references) == 1


def test_reference_map_contains_checks_the_normalized_label() -> None:
    references = ReferenceMap()
    references.add("[foo]", "/url")
    assert "FOO" in references
    assert "bar" not in references


def test_reference_map_contains_rejects_non_strings() -> None:
    assert 3 not in ReferenceMap()


def test_reference_maps_are_independent() -> None:
    first = ReferenceMap()
    first.add("[foo]", "/url")
    assert len(ReferenceMap()) == 0


# --- Extraction: the definition grammar ---


def test_empty_text_has_no_definitions_and_no_remainder() -> None:
    remainder, references = extract("")
    assert remainder == ""
    assert len(references) == 0


def test_single_definition_consumes_all_text() -> None:
    remainder, references = extract("[foo]: /url")
    assert remainder == ""
    assert references.get("foo") == LinkReference("/url", None)


@pytest.mark.parametrize(
    ("title_source", "title"),
    [
        ('"title"', "title"),
        ("'title'", "title"),
        ("(title)", "title"),
    ],
)
def test_title_may_use_double_single_or_parenthesized_delimiters(title_source: str, title: str) -> None:
    remainder, references = extract(f"[foo]: /url {title_source}")
    assert remainder == ""
    assert references.get("foo") == LinkReference("/url", title)


def test_title_may_span_lines() -> None:
    remainder, references = extract("[foo]: /url 'line one\nline two'")
    assert remainder == ""
    assert references.get("foo") == LinkReference("/url", "line one\nline two")


def test_title_may_follow_the_destination_after_a_line_ending() -> None:
    remainder, references = extract("[foo]:\n/url\n'title'")
    assert remainder == ""
    assert references.get("foo") == LinkReference("/url", "title")


def test_title_on_a_later_line_is_not_taken_when_it_has_trailing_text() -> None:
    remainder, references = extract('[foo]: /url\n"title" ok')
    assert remainder == '"title" ok'
    assert references.get("foo") == LinkReference("/url", None)


def test_a_failed_title_leaves_the_destination_line_as_the_definition() -> None:
    remainder, references = extract("[foo]: /url\n'title\nnot closed")
    assert remainder == "'title\nnot closed"
    assert references.get("foo") == LinkReference("/url", None)


def test_title_must_be_separated_from_the_destination_by_whitespace() -> None:
    remainder, references = extract('[foo]: <>"title"')
    assert remainder == '[foo]: <>"title"'
    assert len(references) == 0


def test_tab_is_accepted_as_separator_before_a_title() -> None:
    remainder, references = extract("[foo]:\t/url\t'title'")
    assert remainder == ""
    assert references.get("foo") == LinkReference("/url", "title")


def test_angle_bracket_destination_may_be_empty() -> None:
    remainder, references = extract("[foo]: <>")
    assert remainder == ""
    assert references.get("foo") == LinkReference("", None)


def test_angle_bracket_destination_may_contain_spaces() -> None:
    _, references = extract("[foo]: <my url>")
    assert references.get("foo") == LinkReference("my url", None)


def test_angle_bracket_destination_cannot_hold_a_line_ending() -> None:
    remainder, references = extract("[foo]: <my\nurl>")
    assert remainder == "[foo]: <my\nurl>"
    assert len(references) == 0


def test_angle_bracket_destination_cannot_hold_an_unescaped_less_than() -> None:
    remainder, references = extract("[foo]: <a<b>")
    assert remainder == "[foo]: <a<b>"
    assert len(references) == 0


def test_angle_bracket_destination_may_hold_an_escaped_less_than() -> None:
    _, references = extract("[foo]: <a\\<b>")
    assert references.get("foo") == LinkReference("a<b", None)


def test_plain_destination_with_balanced_parentheses_is_kept_whole() -> None:
    _, references = extract("[foo]: /url(a)")
    assert references.get("foo") == LinkReference("/url(a)", None)


def test_plain_destination_with_unbalanced_parenthesis_is_not_a_definition() -> None:
    remainder, references = extract("[foo]: /url(a")
    assert remainder == "[foo]: /url(a"
    assert len(references) == 0


def test_plain_destination_with_an_escaped_parenthesis_is_kept() -> None:
    _, references = extract("[foo]: /url\\(a")
    assert references.get("foo") == LinkReference("/url(a", None)


def test_plain_destination_cannot_hold_a_space() -> None:
    remainder, references = extract("[foo]: /a b")
    assert remainder == "[foo]: /a b"
    assert len(references) == 0


def test_plain_destination_is_unescaped() -> None:
    _, references = extract("[foo]: /a\\_b")
    assert references.get("foo") == LinkReference("/a_b", None)


def test_destination_entity_is_decoded() -> None:
    _, references = extract("[foo]: /a&amp;b")
    assert references.get("foo") == LinkReference("/a&b", None)


def test_title_entity_is_decoded() -> None:
    _, references = extract('[foo]: /u "&quot;x&quot;"')
    assert references.get("foo") == LinkReference("/u", '"x"')


def test_destination_with_no_text_is_not_a_definition() -> None:
    remainder, references = extract("[foo]:")
    assert remainder == "[foo]:"
    assert len(references) == 0


def test_label_with_an_unescaped_bracket_is_not_a_definition() -> None:
    remainder, references = extract("[fo[o]]: /url")
    assert remainder == "[fo[o]]: /url"
    assert len(references) == 0


def test_label_with_an_escaped_bracket_is_a_definition() -> None:
    remainder, references = extract("[fo\\[o]: /url")
    assert remainder == ""
    assert len(references) == 1


@pytest.mark.parametrize("label", ["[]", "[ ]", "[\t\n]"])
def test_label_with_no_non_whitespace_character_is_not_a_definition(label: str) -> None:
    remainder, references = extract(f"{label}: /url")
    assert remainder == f"{label}: /url"
    assert len(references) == 0


def test_label_of_999_characters_is_a_definition() -> None:
    label = "a" * 999
    remainder, references = extract(f"[{label}]: /url")
    assert remainder == ""
    assert references.get(label) == LinkReference("/url", None)


def test_label_of_1000_characters_is_not_a_definition() -> None:
    remainder, references = extract(f"[{'a' * 1000}]: /url")
    assert remainder == f"[{'a' * 1000}]: /url"
    assert len(references) == 0


def test_label_without_a_colon_is_not_a_definition() -> None:
    remainder, references = extract("[foo] /url")
    assert remainder == "[foo] /url"
    assert len(references) == 0


def test_line_after_a_definition_is_extracted_too() -> None:
    remainder, references = extract("[a]: /1\n[b]: /2\ntext")
    assert remainder == "text"
    assert references.get("a") == LinkReference("/1", None)
    assert references.get("b") == LinkReference("/2", None)


def test_first_definition_for_a_normalized_label_wins_within_one_paragraph() -> None:
    remainder, references = extract("[a]: /1\n[A]: /2")
    assert remainder == ""
    assert references.get("a") == LinkReference("/1", None)


def test_text_before_a_definition_stops_extraction() -> None:
    remainder, references = extract("Foo\n[bar]: /baz")
    assert remainder == "Foo\n[bar]: /baz"
    assert len(references) == 0


def test_remainder_keeps_its_own_line_structure() -> None:
    remainder, _ = extract("[foo]: /url\nline one\nline two")
    assert remainder == "line one\nline two"


# --- Extraction through the block tree ---


def test_paragraph_of_only_definitions_leaves_the_tree() -> None:
    root = blocks.parse_lines(["[foo]: /url", "[bar]: /baz"])
    assert root.children == []
    assert root.references is not None
    assert root.references.get("bar") == LinkReference("/baz", None)


def test_paragraph_remainder_becomes_its_content() -> None:
    root = blocks.parse_lines(["[foo]: /url", "remaining text"])
    assert [child.content for child in root.children] == ["remaining text"]
    assert root.references is not None
    assert root.references.get("foo") == LinkReference("/url", None)


def test_definition_after_a_blank_line_starts_a_new_paragraph() -> None:
    root = blocks.parse_lines(["Foo", "", "[bar]: /baz"])
    assert [child.content for child in root.children] == ["Foo"]
    assert root.references is not None
    assert root.references.get("bar") == LinkReference("/baz", None)


def test_definition_line_directly_after_a_paragraph_is_paragraph_text() -> None:
    root = blocks.parse_lines(["Foo", "[bar]: /baz"])
    assert [child.content for child in root.children] == ["Foo\n[bar]: /baz"]
    assert root.references is not None
    assert len(root.references) == 0


def test_each_parse_starts_with_an_empty_reference_map() -> None:
    blocks.parse_lines(["[foo]: /url"])
    root = blocks.parse_lines(["text"])
    assert root.references is not None
    assert len(root.references) == 0


# --- Exact output through the executable ---


def test_definition_only_output_is_empty(project_root: Path) -> None:
    assert run_commonmark(project_root, "[foo]: /url\n").stdout == ""


def test_definition_then_paragraph_output_is_exact(project_root: Path) -> None:
    result = run_commonmark(project_root, "[foo]: /url\nremaining text\n")
    assert result.stdout == "<p>remaining text</p>\n"


def test_paragraph_that_is_not_a_definition_output_is_exact(project_root: Path) -> None:
    result = run_commonmark(project_root, "Foo\n[bar]: /baz\n")
    assert result.stdout == "<p>Foo\n[bar]: /baz</p>\n"
