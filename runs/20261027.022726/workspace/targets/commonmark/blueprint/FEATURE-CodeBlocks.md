# FEATURE: Code Blocks

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parses indented and fenced code blocks as literal block content. |
| Depends On | FEATURE-ParagraphsAndBreaks.md |
| Provides | code blocks |
| Consumes | paragraph and thematic break blocks |

## Purpose

Recognize indented and fenced code blocks during block parsing and preserve their literal content for HTML rendering.

## Behavior

An indented code block consists of nonblank lines indented at least four columns, with intervening blank lines. Remove four columns of indentation, retain remaining content and interior blank lines, and exclude leading and trailing blank lines. An indented code block cannot interrupt a paragraph.

A fenced code block starts with at least three consecutive backticks or tildes after at most three spaces of indentation. A backtick fence's info string cannot contain backticks. Trim the info string; the examples render its first word as the language class after processing applicable escapes and character references. A closing fence uses the same character, has at least the opening length, allows at most three spaces of indentation, and contains only trailing spaces or tabs. Remove up to the opening indentation from each content line. An unclosed fence ends at the containing block or document end. Fenced blocks can interrupt paragraphs.

Do not parse code content as inline Markdown. Escape literal content appropriately when rendering HTML. The complete code-block sections include interactions with later containers and inline constructs; the later line-break integration exercises those sections after all providers exist.

## Programmatic Acceptance

=== AC indented-code-block ===
Intent: Block parsing removes the required indentation and preserves the literal code content.

from commonmark_parser import parse_blocks

content = "alpha * beta\n"
document = parse_blocks("    " + content)
assert len(document.children) == 1
assert document.children[0].type == "code_block"
assert document.children[0].literal == content
=== END AC indented-code-block ===

=== AC fenced-code-block ===
Intent: Matching fences form a code block whose content remains literal.

from commonmark_parser import parse_blocks

content = "alpha * beta\n"
document = parse_blocks("```\n" + content + "```\n")
assert len(document.children) == 1
assert document.children[0].type == "code_block"
assert document.children[0].literal == content
=== END AC fenced-code-block ===

## User Acceptance

- None.

## Guardrails

- Code block content is literal and is never parsed as inline Markdown.
- Do not modify the supplied conformance assets.
