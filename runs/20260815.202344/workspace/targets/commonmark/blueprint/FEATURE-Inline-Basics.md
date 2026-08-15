# FEATURE: Inline Basics

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Parses CommonMark escapes, entities, code spans, line breaks, and literal text. |
| Depends On  | ARCHITECTURE.md, FEATURE-Block-Leafs.md, FEATURE-Block-Quotes.md, FEATURE-Block-Lists.md |
| Provides    | inline escapes, entity references, code spans, hard breaks, soft breaks |
| Consumes    | executable commonmark, block structure |

## Purpose

Implement the foundational inline constructs used by all later inline features.

## Scope

Support ASCII punctuation backslash escapes, HTML named and numeric character references, U+0000 replacement, code spans with delimiter matching and whitespace normalization, hard breaks from trailing spaces or backslashes, soft breaks, and literal textual content.

Escapes, entities, and line breaks must obey their context restrictions in code spans, code blocks, autolinks, and raw HTML.

## Programmatic Acceptance

=== AC inline-basics-conformance ===
Intent: The implementation passes every supplied conformance example owned by foundational inline parsing.

import subprocess
import sys

pattern = (
    r"^(Backslash escapes|Entity and numeric character references|Code spans|"
    r"Hard line breaks|Soft line breaks|Textual content)$"
)
result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program",
        "./commonmark",
        "--spec",
        "sources/spec.txt",
        "--pattern",
        pattern,
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC inline-basics-conformance ===

=== AC inline-basics-interface ===
Intent: Inline source containing escapes, entities, code, and line breaks is accepted through the executable interface.

import subprocess

source = r"escaped \* text &amp; `code`  " + "\n" + "next\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC inline-basics-interface ===

=== AC inline-basics-unicode-input ===
Intent: UTF-8 inline text is accepted through the executable interface.

import subprocess

source = "Unicode café\n"
result = subprocess.run(
    ["./commonmark"],
    input=source,
    capture_output=True,
    text=True,
    encoding="utf-8",
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC inline-basics-unicode-input ===

## User Acceptance

- None.

## Guardrails

- Do not apply escapes or entity references inside code spans or code blocks.
- Preserve literal text and internal spaces.
- Do not modify supplied conformance assets.
