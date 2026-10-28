# FEATURE: Emphasis

| Field | Value |
|-------|-------|
| Version | 20261027 V1 |
| Description | Parse emphasis and strong emphasis using delimiter runs. |
| Depends On | FEATURE-InlineText.md, FEATURE-CodeSpans.md |
| Provides | emphasis parsing |
| Consumes | inline text parsing, code span parsing |

## Purpose and workflow

Extend `commonmark_parser.inlines.parse_inlines(source, references)` to identify runs of `*` and `_` and classify potential openers and closers using the specification's Unicode whitespace and punctuation flanking rules. Apply the underscore restrictions and the rule of three using the original run lengths.

Use the appendix's delimiter-stack process: scan potential closers in input order, search backward for the nearest valid opener above the applicable lower bound, create an emphasis or strong node, consume one or two delimiter characters on each side, and remove intervening delimiters from the stack. Continue with remaining delimiters and retain unmatched characters as text. Preserve the specified nesting and overlap precedence. Code spans bind more tightly; link, image, autolink, and raw HTML precedence is completed when those providers are integrated.

Emphasis nodes have type `em`, strong emphasis nodes have type `strong`, and each exposes ordered `children`. Text children expose `literal`.

The complete Emphasis and strong emphasis corpus section is executed by conformance integration after all interacting inline providers exist.

## Programmatic Acceptance

=== AC emphasis-basic ===
Intent: A matching single delimiter pair produces an emphasis node containing the supplied text.

from commonmark_parser.inlines import parse_inlines

content = "alpha"
nodes = parse_inlines("*" + content + "*", {})
assert len(nodes) == 1
assert nodes[0].type == "em"
assert len(nodes[0].children) == 1
assert nodes[0].children[0].type == "text"
assert nodes[0].children[0].literal == content
=== END AC emphasis-basic ===

=== AC emphasis-strong ===
Intent: A matching double delimiter pair produces a strong node containing the supplied text.

from commonmark_parser.inlines import parse_inlines

content = "beta"
nodes = parse_inlines("**" + content + "**", {})
assert len(nodes) == 1
assert nodes[0].type == "strong"
assert len(nodes[0].children) == 1
assert nodes[0].children[0].literal == content
=== END AC emphasis-strong ===

=== AC emphasis-intraword-underscore ===
Intent: Underscores within a word remain literal rather than creating emphasis.

from commonmark_parser.inlines import parse_inlines

source = "alpha_beta_gamma"
nodes = parse_inlines(source, {})
assert all(node.type == "text" for node in nodes)
assert "".join(node.literal for node in nodes) == source
=== END AC emphasis-intraword-underscore ===

## User Acceptance

- None.

## Guardrails

- Follow the supplied delimiter-stack and precedence rules.
- Preserve supplied conformance assets unchanged.
- Do not invoke the full-suite entry point in this story's checks.
