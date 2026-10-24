# FEATURE: Autolinks

| Field       | Value |
|-------------|-------|
| Version     | 20261014 V1 |
| Description | Parse URI autolinks and email autolinks inside angle brackets into links. |
| Depends On  | FEATURE-Block-Engine.md |
| Provides    | autolink inline construct |
| Consumes    | inline parser hook, URL percent-encoding helper |

## Purpose

Implement the Autolinks section of the spec.

## Rules

- A URI autolink is `<`, a scheme, a colon, zero or more characters other than ASCII control characters, space, `<` and `>`, then `>`. A scheme is 2 to 32 characters: an ASCII letter followed by letters, digits, `+`, `.` or `-`.
- An email autolink is `<`, an address matching the HTML5 email regex given in the spec, then `>`. The href is `mailto:` followed by the address.
- The link text is the address as written, HTML-escaped. The href is percent-encoded for non-ASCII and unsafe characters (for example a backtick or backslash), with `&` escaped as `&amp;`.
- Backslash escapes are inert inside autolinks.
- Anything with a space, an empty body, a one-letter scheme, or no scheme or `@` stays literal text with `<` and `>` escaped.
- Autolinks bind as tightly as code spans and raw HTML; the first one found left to right wins.

## Reads

- Inline text of paragraphs and headings.

## Writes

- Link nodes in the inline tree.

## Programmatic Acceptance

=== AC autolinks-corpus-section ===
Intent: The Autolinks conformance section (19 cases) passes in full.
Suite: scoped
Probe: --dump-tests
Probe Count: lines

import os
import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--program",
        os.getcwd() + "/commonmark",
        "--spec",
        "sources/spec.txt",
        "--pattern",
        "^Autolinks$",
    ],
    capture_output=True,
    text=True,
    env={**os.environ},
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC autolinks-corpus-section ===

=== AC autolinks-uri-roundtrip ===
Intent: A URI autolink renders as one link whose href and text are the supplied URI.

import subprocess

uri = "http://example.org/path"
result = subprocess.run(["./commonmark"], input="<" + uri + ">\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<a ") == 1
assert ('href="' + uri + '"') in result.stdout
assert (">" + uri + "</a>") in result.stdout
=== END AC autolinks-uri-roundtrip ===

=== AC autolinks-email-mailto ===
Intent: An email autolink renders with a mailto href built from the supplied address.

import subprocess

address = "someone@example.org"
result = subprocess.run(["./commonmark"], input="<" + address + ">\n", capture_output=True, text=True)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<a ") == 1
assert ('href="mailto:' + address + '"') in result.stdout
=== END AC autolinks-email-mailto ===

=== AC autolinks-space-not-autolink ===
Intent: A URI containing a space is not an autolink, so no link element is produced.

import subprocess

result = subprocess.run(
    ["./commonmark"], input="<http://example.org/a b>\n", capture_output=True, text=True
)
print(result.stdout)
assert result.returncode == 0
assert result.stdout.count("<a ") == 0
=== END AC autolinks-space-not-autolink ===

## User Acceptance

- None.

## Guardrails

- Backslash escapes must not be processed inside autolinks.
- Bare URLs and bare email addresses without angle brackets must not become links.
- Do not skip, filter or reinterpret corpus examples.
