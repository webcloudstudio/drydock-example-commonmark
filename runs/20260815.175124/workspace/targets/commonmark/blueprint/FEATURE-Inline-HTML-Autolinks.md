# FEATURE: Inline HTML and Autolinks

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Parse URI and email autolinks and preserve valid inline raw HTML. |
| Depends On  | FEATURE-Inline-Links.md |
| Provides    | URI autolinks, email autolinks, inline raw HTML |
| Consumes    | links and images, emphasis inline nodes, code spans |

## Intent

The inline parser recognizes absolute URI and email autolinks enclosed in angle brackets and preserves valid raw HTML tags, comments, processing instructions, declarations, and CDATA sections. These constructs take precedence over emphasis and link grouping where required by CommonMark 0.31.2.

## Behavior

- Accept URI schemes of two to thirty-two ASCII characters followed by a colon.
- Accept valid HTML5-style email autolinks and render them with `mailto:` destinations.
- Preserve valid HTML tags and attributes without Markdown interpretation inside the tag.
- Preserve comments, processing instructions, declarations, and CDATA sections.
- Reject malformed tags and autolinks as literal text.
- Apply URL escaping to autolink destinations while preserving visible labels.
- Keep code spans, HTML tags, and autolinks ahead of emphasis parsing.

## Programmatic Acceptance

=== AC inline-autolinks ===
Intent: The implementation passes the authoritative CommonMark autolink examples owned by this story.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--spec",
        "sources/spec.txt",
        "--program",
        "./commonmark",
        "--pattern",
        r"^Autolinks$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC inline-autolinks ===

=== AC inline-raw-html ===
Intent: The implementation passes the authoritative CommonMark raw HTML examples owned by this story.
Suite: scoped

import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,
        "sources/spec_tests.py",
        "--spec",
        "sources/spec.txt",
        "--program",
        "./commonmark",
        "--pattern",
        r"^Raw HTML$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
assert result.returncode == 0
=== END AC inline-raw-html ===

## User Acceptance

- None.

## Guardrails

- Do not use a public Markdown implementation.
- Do not parse malformed autolinks or HTML tags as valid structure.
- Do not invoke `full_test.sh` from scoped checks.
