# FEATURE: Inline Links

| Field       | Value |
|-------------|-------|
| Version     | 20260815 V1 |
| Description | Parse inline, reference, collapsed, and shortcut links together with images. |
| Depends On  | FEATURE-Inline-Emphasis.md, FEATURE-Block-References.md |
| Provides    | links and images with destinations, titles, references, and alt text |
| Consumes    | emphasis inline nodes, code spans, document-wide link reference definition map |

## Workflow

Recognize bracketed link text and image descriptions before resolving inline, full-reference, collapsed-reference, and shortcut forms. Parse balanced destinations, angle-bracket destinations, optional titles, escapes, entities, and permitted line endings.

Resolve labels using the document-wide first-definition map. Prevent nested links while allowing nested images, and construct image alt text from the plain textual content of the description. Preserve literal brackets and source text when a candidate does not satisfy the link grammar.

## Programmatic Acceptance

=== AC inline-links-conformance ===
Intent: The implementation passes the authoritative CommonMark examples for links and images owned by this story.
Suite: scoped

import subprocess

result = subprocess.run(
    [
        "python3",
        "sources/spec_tests.py",
        "--spec", "sources/spec.txt",
        "--program", "./commonmark",
        "--pattern", r"^(Links|Images)$",
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC inline-links-conformance ===

=== AC inline-links-selector ===
Intent: The link and image conformance selector executes the complete owned specification sections successfully.
Suite: scoped

import subprocess

sections = r"^(Links|Images)$"
result = subprocess.run(
    [
        "python3",
        "sources/spec_tests.py",
        "--spec", "sources/spec.txt",
        "--program", "./commonmark",
        "--pattern", sections,
    ],
    capture_output=True,
    text=True,
)
print(result.stdout)
print(result.stderr)
assert result.returncode == 0
=== END AC inline-links-selector ===

## User Acceptance

- None.

## Guardrails

- Do not resolve references before block parsing has collected document-wide definitions.
- Do not permit links nested inside links.
- Preserve image descriptions as plain text for `alt` attributes.
- Do not invoke `full_test.sh` from this story.
