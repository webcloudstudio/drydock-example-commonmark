# FEATURE: HTML Blocks

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Recognize and preserve CommonMark HTML blocks. |
| Depends On | FEATURE-ParagraphsAndBreaks.md |
| Provides | HTML blocks |
| Consumes | paragraph and thematic break blocks |

## Purpose and behavior

The block parser recognizes HTML blocks after at most three spaces of indentation. It preserves their source lines as raw HTML without inline parsing. A block ends at the end of its containing block or document if its specific end condition is not reached.

Recognize the seven types defined in `sources/spec.txt`, “HTML blocks”:

1. A `pre`, `script`, `style`, or `textarea` opening begins a block ending on a line containing any of their closing tags, case-insensitively.
2. `<!--` begins a block ending on a line containing `-->`.
3. `<?` begins a block ending on a line containing `?>`.
4. `<!` followed by an ASCII letter begins a block ending on a line containing `>`.
5. `<![CDATA[` begins a block ending on a line containing `]]>`.
6. A specified block-level HTML tag begins a block ending before a blank line.
7. A complete open or closing tag on a line by itself begins a block ending before a blank line.

Types 1–6 can interrupt paragraphs; type 7 cannot. A start and end condition can occur on the same line, and the entire ending line belongs to the block. HTML inside an open block does not change its termination rule.

Expose `parse_html_block(lines, paragraph_open=False)` from `commonmark_parser.html_blocks`. It accepts a sequence of source lines and returns either `None` when no block starts or a pair `(consumed, raw)` containing the number of lines consumed and their unchanged concatenated text. The caller supplies only lines within the current container.

Cross-feature examples involving later inline constructs remain covered when those constructs are integrated.

## Programmatic Acceptance

=== AC html-block-termination ===
Intent: A comment block retains its source through the line containing its end marker and leaves later lines unconsumed.

from commonmark_parser.html_blocks import parse_html_block

lines = ["<!-- start\n", "\n", "end --> trailing\n", "after\n"]
consumed, raw = parse_html_block(lines)
assert consumed == 3
assert raw == "".join(lines[:consumed])
=== END AC html-block-termination ===

=== AC html-block-paragraph-interruption ===
Intent: A complete non-block tag cannot interrupt a paragraph but can begin a type 7 HTML block outside one.

from commonmark_parser.html_blocks import parse_html_block

lines = ["<custom>\n", "content\n", "\n"]
assert parse_html_block(lines, paragraph_open=True) is None
consumed, raw = parse_html_block(lines, paragraph_open=False)
assert consumed == 2
assert raw == "".join(lines[:consumed])
=== END AC html-block-paragraph-interruption ===

## User Acceptance

- None.

## Guardrails

- Do not modify the supplied specification or conformance assets.
- Preserve raw HTML rather than interpreting its contents as Markdown.
