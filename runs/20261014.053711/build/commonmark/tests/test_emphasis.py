"""Emphasis tests: delimiter runs, flanking rules, the process-emphasis pairing, and the rule of 3.

The declared acceptance checks are transcribed from FEATURE-Emphasis.md with their assertions kept
as written. The remaining tests compare the executable's stdout bytes or a returned string with its
exact expected value.
"""

import subprocess
from pathlib import Path

from mdparser import inlines


def run_executable(project_root: Path, data: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [str(project_root / "commonmark")],
        input=data.encode("utf-8"),
        capture_output=True,
        cwd=project_root,
        check=False,
    )


# --- Declared acceptance checks (transcribed from FEATURE-Emphasis.md) ---


def test_emphasis_star_and_underscore(project_root: Path) -> None:
    """AC emphasis-star-and-underscore: single star and single underscore wrap a word in one em."""
    word = "wordy"
    for mark in ("*", "_"):
        result = run_executable(project_root, mark + word + mark + "\n")
        stdout = result.stdout.decode("utf-8")
        assert result.returncode == 0
        assert stdout.count("<em>") == 1
        assert stdout.count("<strong>") == 0
        assert word in stdout


def test_emphasis_strong(project_root: Path) -> None:
    """AC emphasis-strong: doubled delimiters produce one strong element."""
    word = "wordy"
    for mark in ("**", "__"):
        result = run_executable(project_root, mark + word + mark + "\n")
        stdout = result.stdout.decode("utf-8")
        assert result.returncode == 0
        assert stdout.count("<strong>") == 1
        assert stdout.count("<em>") == 0


def test_emphasis_intraword_rules(project_root: Path) -> None:
    """AC emphasis-intraword-rules: intraword emphasis works with star but not with underscore."""
    star = run_executable(project_root, "foo*bar*baz\n")
    under = run_executable(project_root, "foo_bar_baz\n")
    assert star.returncode == 0
    assert under.returncode == 0
    assert star.stdout.decode("utf-8").count("<em>") == 1
    assert under.stdout.decode("utf-8").count("<em>") == 0


def test_emphasis_flanking_whitespace(project_root: Path) -> None:
    """AC emphasis-flanking-whitespace: a run next to whitespace does not form emphasis."""
    result = run_executable(project_root, "a * foo bar*\n\nfoo bar *\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8").count("<em>") == 0


def test_emphasis_nesting(project_root: Path) -> None:
    """AC emphasis-nesting: triple delimiters give one em and one strong; nested forms keep both."""
    triple = run_executable(project_root, "***word***\n")
    nested = run_executable(project_root, "*a **b** c*\n")
    assert triple.returncode == 0
    assert nested.returncode == 0
    assert triple.stdout.decode("utf-8").count("<em>") == 1
    assert triple.stdout.decode("utf-8").count("<strong>") == 1
    assert nested.stdout.decode("utf-8").count("<em>") == 1
    assert nested.stdout.decode("utf-8").count("<strong>") == 1


def test_emphasis_code_span_binds_tighter(project_root: Path) -> None:
    """AC emphasis-code-span-binds-tighter: a star inside a code span cannot close emphasis."""
    result = run_executable(project_root, "*foo`*`\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8").count("<em>") == 0
    assert result.stdout.decode("utf-8").count("<code>") == 1


# --- Single and doubled delimiters ---


def test_emphasis_single_star_exact(project_root: Path) -> None:
    """A single star pair wraps its word in one em element."""
    result = run_executable(project_root, "*wordy*\n")
    assert result.stdout.decode("utf-8") == "<p><em>wordy</em></p>\n"


def test_emphasis_single_underscore_exact(project_root: Path) -> None:
    """A single underscore pair wraps its word in one em element."""
    result = run_executable(project_root, "_wordy_\n")
    assert result.stdout.decode("utf-8") == "<p><em>wordy</em></p>\n"


def test_emphasis_double_star_exact(project_root: Path) -> None:
    """A doubled star pair wraps its word in one strong element."""
    result = run_executable(project_root, "**wordy**\n")
    assert result.stdout.decode("utf-8") == "<p><strong>wordy</strong></p>\n"


def test_emphasis_double_underscore_exact(project_root: Path) -> None:
    """A doubled underscore pair wraps its word in one strong element."""
    result = run_executable(project_root, "__wordy__\n")
    assert result.stdout.decode("utf-8") == "<p><strong>wordy</strong></p>\n"


def test_emphasis_triple_exact() -> None:
    """Triple stars give em outside strong, following the length-matching rule."""
    assert inlines.parse_inline("***word***") == "<em><strong>word</strong></em>"


def test_emphasis_triple_then_single_opener() -> None:
    """A triple opener closed by a double run gives strong inside em with the leftover star."""
    assert inlines.parse_inline("***foo**") == "*<strong>foo</strong>"


def test_emphasis_nested_exact() -> None:
    """Strong nested in em keeps the surrounding text."""
    assert inlines.parse_inline("*a **b** c*") == "<em>a <strong>b</strong> c</em>"


def test_emphasis_strong_inside_em_middle() -> None:
    """Strong in the middle of em word."""
    assert inlines.parse_inline("*foo**bar**baz*") == "<em>foo<strong>bar</strong>baz</em>"


def test_emphasis_three_delimiters_middle() -> None:
    """Triple run in the middle of a word gives em around strong."""
    assert inlines.parse_inline("foo***bar***baz") == "foo<em><strong>bar</strong></em>baz"


# --- Unmatched and empty runs stay literal ---


def test_emphasis_unclosed_is_literal() -> None:
    """An opener with no closer is literal text."""
    assert inlines.parse_inline("*foo") == "*foo"


def test_emphasis_empty_double_is_literal() -> None:
    """Two adjacent delimiters with nothing between never form empty emphasis."""
    assert inlines.parse_inline("**") == "**"


def test_emphasis_empty_underscore_pair_is_literal() -> None:
    """A doubled underscore with no content between it is literal text."""
    assert inlines.parse_inline("__") == "__"


def test_emphasis_run_of_four_is_literal() -> None:
    """Four stars with no content are literal text."""
    assert inlines.parse_inline("****") == "****"


def test_emphasis_leftover_is_escaped() -> None:
    """A leftover delimiter run is escaped like any other text."""
    assert inlines.parse_inline("*a<b") == "*a&lt;b"


# --- Flanking rules ---


def test_emphasis_space_after_opener_is_literal() -> None:
    """A star followed by a space cannot open."""
    assert inlines.parse_inline("* foo*") == "* foo*"


def test_emphasis_space_before_closer_is_literal() -> None:
    """A star preceded by a space cannot close."""
    assert inlines.parse_inline("*foo *") == "*foo *"


def test_emphasis_unicode_space_after_opener_is_literal() -> None:
    """A no-break space after a star counts as Unicode whitespace, so the star cannot open."""
    assert inlines.parse_inline("* foo*") == "* foo*"


def test_emphasis_punctuation_edges_open_and_close() -> None:
    """Punctuation at both edges is allowed when the run is preceded by whitespace or start."""
    assert inlines.parse_inline('*"foo"*') == "<em>&quot;foo&quot;</em>"


def test_emphasis_underscore_inside_word_does_not_open() -> None:
    """An underscore run with alphanumerics on both sides is both-flanking and cannot open."""
    assert inlines.parse_inline("foo_bar_") == "foo_bar_"


def test_emphasis_underscore_after_punctuation_opens() -> None:
    """An underscore preceded by punctuation may open even when it is also right-flanking."""
    assert inlines.parse_inline('"_foo_"') == "&quot;<em>foo</em>&quot;"


def test_emphasis_escaped_star_does_not_open() -> None:
    """A backslash-escaped star is text and is not a delimiter."""
    assert inlines.parse_inline("\\*foo*") == "*foo*"


def test_emphasis_entity_star_does_not_open() -> None:
    """A decoded character reference for a star is text and is not a delimiter."""
    assert inlines.parse_inline("&#42;foo*") == "*foo*"


# --- Process-emphasis pairing and the rule of 3 ---


def test_emphasis_rule_of_three_skips_pair() -> None:
    """Both-flanking runs whose lengths sum to a multiple of 3 do not pair (rule of 3)."""
    assert inlines.parse_inline("*foo**bar*") == "<em>foo**bar</em>"


def test_emphasis_rule_of_three_double_then_single() -> None:
    """A double opener with a single closer sums to 3, so no pair forms."""
    assert inlines.parse_inline("**foo*bar*") == "**foo<em>bar</em>"


def test_emphasis_rule_of_three_multiples_pair() -> None:
    """Runs of length 3 and 3 may pair even though their lengths sum to a multiple of 3."""
    assert inlines.parse_inline("***foo***") == "<em><strong>foo</strong></em>"


def test_emphasis_closer_pairs_with_nearest_opener() -> None:
    """The inner closer pairs with the nearest opener; the outer closer pairs with the first."""
    assert inlines.parse_inline("*a *b* c*") == "<em>a <em>b</em> c</em>"


def test_emphasis_star_closer_pairs_across_text() -> None:
    """A star closer may pair with an opener several words back."""
    assert inlines.parse_inline("*one two three*") == "<em>one two three</em>"


def test_emphasis_consumes_one_character_each() -> None:
    """A regular pair consumes one character from each side."""
    assert inlines.parse_inline("**a*") == "*<em>a</em>"


def test_emphasis_multiple_pairs_in_one_paragraph() -> None:
    """Two separate pairs in one paragraph each produce their own element."""
    assert inlines.parse_inline("*a* and *b*") == "<em>a</em> and <em>b</em>"


def test_emphasis_inside_code_span_is_not_delimiter() -> None:
    """A star inside a code span is code text and does not take part in emphasis."""
    assert inlines.parse_inline("`*a*`") == "<code>*a*</code>"


def test_emphasis_wraps_raw_html() -> None:
    """Emphasis may wrap a raw HTML tag, which stays as written."""
    assert inlines.parse_inline("*<b>*") == "<em><b></em>"


# --- Executable, end to end ---


def test_emphasis_paragraphs_are_independent(project_root: Path) -> None:
    """Delimiter stacks do not carry across paragraphs, so an opener cannot pair across them."""
    result = run_executable(project_root, "*a\n\nb*\n")
    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == "<p>*a</p>\n<p>b*</p>\n"


def test_emphasis_flanking_exact(project_root: Path) -> None:
    """Whitespace-flanked runs in two paragraphs stay literal, with exact output."""
    result = run_executable(project_root, "a * foo bar*\n\nfoo bar *\n")
    assert result.stdout.decode("utf-8") == "<p>a * foo bar*</p>\n<p>foo bar *</p>\n"


def test_emphasis_code_span_binds_tighter_exact(project_root: Path) -> None:
    """A star inside a code span cannot close emphasis: exact output."""
    result = run_executable(project_root, "*foo`*`\n")
    assert result.stdout.decode("utf-8") == "<p>*foo<code>*</code></p>\n"
