# Evidence: Block 6 · Service (block-6)

- block type: block
- date: 2026-10-27
- resulting state: closed/verified
- story points (combined assembled cost): 3522
- execution id: 20261027.212732.438Z-fe4fa9c3

## Stories built
- Parse block quote containers. (block-quotes) [story]

## Stacked context
- stack: python_compact.md (SP 654)
- compass: COMPASS.md (SP 548)
- implements: FEATURE-BlockQuotes.md (SP 878)
- context: ARCHITECTURE_compact.md (SP 304)
- stack: common_compact.md (SP 1079)

## Build directory changes
- commonmark_parser/blocks.py
- tests/test_block_quotes.py

## Pre-build acceptance observation
- RED: block-quote-lazy (FEATURE-BlockQuotes.md)
  intent: A marked paragraph and its unmarked continuation belong to the same quote and retain their source text.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      quote = Block(kind='paragraph', children=[], literal='> alpha\ncontinuation', level=None, info='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "block-quote-lazy.py", line 8, in <module>
        assert quote.type == "block_quote"
               ^^^^^^^^^^
    AttributeError: 'Block' object has no attribute 'type'
- RED: block-quote-nesting (FEATURE-BlockQuotes.md)
  intent: Nested quote markers produce nested containers, and an unmarked blank line ends the quote.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      outer = Block(kind='paragraph', children=[], literal='> > inside', level=None, info='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "block-quote-nesting.py", line 8, in <module>
        assert outer.type == "block_quote"
               ^^^^^^^^^^
    AttributeError: 'Block' object has no attribute 'type'

## Post-build programmatic acceptance
- PASS: block-quote-lazy (FEATURE-BlockQuotes.md)
  intent: A marked paragraph and its unmarked continuation belong to the same quote and retain their source text.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: block-quote-nesting (FEATURE-BlockQuotes.md)
  intent: Nested quote markers produce nested containers, and an unmarked blank line ends the quote.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark_parser/blocks.py
- tests/test_block_quotes.py

SUMMARY:
Added recursive block quote parsing with nested containers, lazy paragraph continuation, explicit blank lines, and document-wide reference collection. Added a `type` alias for block nodes while preserving the existing `kind` interface.

Ran `pytest -q tests/test_block_quotes.py tests/test_paragraphs.py tests/test_service_blocks.py tests/test_setext.py`: 26 passed. The full-suite entry point was not run.

BLOCKERS:
- None
