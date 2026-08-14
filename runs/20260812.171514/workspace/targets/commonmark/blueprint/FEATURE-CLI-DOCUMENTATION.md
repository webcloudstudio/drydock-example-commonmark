# FEATURE: CLI Documentation

| Field       | Value |
|-------------|-------|
| Version     | 20260812 V1 |
| Description | Documents the parser command-line interface and complete conformance verification command. |
| Depends On  | FEATURE-CLI-ENTRYPOINT.md |
| Provides    | README.md |
| Consumes    | parser executable, full_test.sh |

## Documentation

`README.md` is concise and documents:

- that the parser reads Markdown from standard input;
- that it writes rendered HTML to standard output;
- that `sh full_test.sh` runs the complete supplied conformance suite.

## Programmatic Acceptance

=== AC cli-documentation-content ===
Intent: README.md documents the standard-input and standard-output interface.

from pathlib import Path

text = Path("README.md").read_text(encoding="utf-8")
lower = text.lower()
assert "standard input" in lower or "stdin" in lower
assert "standard output" in lower or "stdout" in lower
=== END AC cli-documentation-content ===

=== AC cli-documentation-verification ===
Intent: README.md documents the required complete-suite invocation.

from pathlib import Path

text = Path("README.md").read_text(encoding="utf-8")
assert "sh full_test.sh" in text
=== END AC cli-documentation-verification ===

## User Acceptance

- None.

## Guardrails

- README.md remains concise.
- Documentation does not claim verification through a filtered or hardcoded tally.
