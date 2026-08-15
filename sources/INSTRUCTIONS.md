# Build Instructions: CommonMark Parser

Build a CommonMark 0.31.2 parser from the supplied specification. The parser reads Markdown from
standard input and writes HTML to standard output. Do not use a public Markdown implementation.

The deliverable is an executable named `commonmark` at the application root.

`sources/INSTRUCTIONS.md` is imported specification prose. It is not staged into the completed
application. The runtime conformance assets are only `spec.txt`, `spec_tests.py`, `cmark.py`,
`normalize.py`, and `full_test.sh`.

## Run Harness

`sources/full_test.sh` is the single scoring entry point. It is supplied, not authored: it is
staged verbatim into the build directory alongside the other imported assets, and `drydock uat`
runs `sh sources/full_test.sh` from the completed application root and takes its exit code and
output as the score. It runs the complete, unfiltered supplied CommonMark suite against
`./commonmark`.

The interface check is deliberately separate from the conformance run so that a missing
executable and a genuine conformance failure are distinguishable in the evidence.

**The scoring assets are read-only.** `sources/full_test.sh`, `sources/spec_tests.py`,
`sources/cmark.py`, `sources/normalize.py`, and `sources/spec.txt` are hash-verified against the
import and restored before grading, so a modification is reported as tampering rather than
honored. Do not write to them. Build `./commonmark` so that the supplied entry point succeeds;
changing the entry point is not a repair.

Create a concise project `README.md` describing the standard-input/standard-output interface.
README content is not an acceptance criterion and does not require a documentation story.

## Implementation Guidance

CommonMark parsing is two phases: resolve **block structure** first, then run **inline parsing**
over the block contents. Implement in that order.

1. Blocks: paragraphs, thematic breaks, ATX headings, setext headings, indented code, fenced
   code, HTML blocks, link reference definitions, block quotes, then lists — lists are the
   hardest block construct, with lazy continuation, nesting, and tightness.
2. Inlines: backslash escapes, entity and numeric references, code spans, emphasis and strong
   emphasis (the delimiter-run algorithm), links and images, autolinks, raw HTML, hard breaks.

The specification text is normative and contains the algorithms. The "Appendix: A parsing
strategy" section describes the reference implementation's approach; follow it directly rather
than reinventing the rules.

## Acceptance

Parser implementation stories may run `spec_tests.py` with explicit section selectors covering
the story's complete scope. A selector must name headings that own examples, such as `ATX
headings` or `List items`. Chapter headings such as `Leaf blocks`, `Container blocks`, and
`Characters and lines` own no examples; selecting them can exit zero without testing anything.

Create one terminal verification story that:

- depends on every parser implementation story;
- contains the only `Suite: full` acceptance check;
- runs `sh sources/full_test.sh`, prints captured standard output and standard error, and asserts
  only `result.returncode == 0`; and
- carries `Sea Trials: st-001`.

Do not author `full_test.sh`; it is supplied. Do not invoke it from scoped checks. Do not create
file-presence or staged-asset acceptance checks, or additional verification stories.
