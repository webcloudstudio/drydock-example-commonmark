# Evidence: Block 4 · Service (block-4)

- block type: block
- date: 2026-10-27
- resulting state: closed/verified
- story points (combined assembled cost): 6701
- execution id: 20261027.212400.806Z-88e20c49

## Stories built
- Recognize thematic breaks with block precedence. (thematic-breaks) [story]
- Parse indented code blocks. (indented-code) [story]
- Parse ATX headings. (atx-headings) [story]
- Parse raw HTML blocks. (html-blocks) [story]
- Parse fenced code blocks. (fenced-code) [story]
- Collect document-wide link reference definitions. (reference-definitions) [story]

## Stacked context
- stack: python_compact.md (SP 654)
- compass: COMPASS.md (SP 548)
- implements: FEATURE-ThematicBreaks.md (SP 493)
- context: ARCHITECTURE_compact.md (SP 304)
- stack: common_compact.md (SP 1079)
- implements: FEATURE-IndentedCode.md (SP 597)
- implements: FEATURE-ATXHeadings.md (SP 613)
- implements: FEATURE-HTMLBlocks.md (SP 633)
- implements: FEATURE-FencedCode.md (SP 651)
- implements: FEATURE-ReferenceDefinitions.md (SP 738)

## Build directory changes
- commonmark_parser/blocks.py
- commonmark_parser/fenced_code.py
- commonmark_parser/html_blocks.py
- commonmark_parser/indented_code.py
- commonmark_parser/references.py
- tests/test_service_blocks.py

## Pre-build acceptance observation
- RED: thematic-break-recognition (FEATURE-ThematicBreaks.md)
  intent: Matching marker runs form thematic breaks and interrupt an existing paragraph.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      document = Document(children=[Block(kind='paragraph', children=[], literal='alpha\n* * *', level=None)], references={})
    --- drydock: end values ---
    Traceback (most recent call last):
      File "thematic-break-recognition.py", line 5, in <module>
        assert len(document.children) == 2
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): thematic-break-invalid (FEATURE-ThematicBreaks.md)
  intent: A line with mixed markers remains paragraph content instead of forming a thematic break.
  return code: 0
- RED: indented-code-content (FEATURE-IndentedCode.md)
  intent: Four-column indentation is removed while extra indentation and interior blank lines remain literal.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "indented-code-content.py", line 1, in <module>
        from commonmark_parser.indented_code import parse_indented_code
    ModuleNotFoundError: No module named 'commonmark_parser.indented_code'
- RED: indented-code-interruption (FEATURE-IndentedCode.md)
  intent: Indented code does not interrupt an open paragraph and ends before a less-indented nonblank line.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "indented-code-interruption.py", line 1, in <module>
        from commonmark_parser.indented_code import parse_indented_code
    ModuleNotFoundError: No module named 'commonmark_parser.indented_code'
- RED: atx-heading-level (FEATURE-ATXHeadings.md)
  intent: A valid opening run produces the corresponding heading level and retains its content for inline parsing.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      document = Document(children=[Block(kind='paragraph', children=[], literal='### alpha ###', level=None)], references={})
    --- drydock: end values ---
    Traceback (most recent call last):
      File "atx-heading-level.py", line 6, in <module>
        assert document.children[0].kind == "heading"
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: atx-heading-interruption (FEATURE-ATXHeadings.md)
  intent: An ATX heading interrupts a paragraph and a marker without required separating whitespace stays in paragraph content.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      document = Document(children=[Block(kind='paragraph', children=[], literal='alpha\n# beta\n#gamma', level=None)], references={})
    --- drydock: end values ---
    Traceback (most recent call last):
      File "atx-heading-interruption.py", line 7, in <module>
        assert len(document.children) == 3
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: html-block-termination (FEATURE-HTMLBlocks.md)
  intent: A comment block preserves its lines through the line containing its closing marker.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "html-block-termination.py", line 1, in <module>
        from commonmark_parser.html_blocks import parse_html_block
    ModuleNotFoundError: No module named 'commonmark_parser.html_blocks'
- RED: html-block-paragraph (FEATURE-HTMLBlocks.md)
  intent: A standalone custom tag cannot interrupt a paragraph, while a block-level tag can and ends before a blank line.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "html-block-paragraph.py", line 1, in <module>
        from commonmark_parser.html_blocks import parse_html_block
    ModuleNotFoundError: No module named 'commonmark_parser.html_blocks'
- RED: fenced-code-matching (FEATURE-FencedCode.md)
  intent: A fence closes only with a sufficiently long matching delimiter and preserves intervening literal content.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "fenced-code-matching.py", line 1, in <module>
        from commonmark_parser.fenced_code import parse_fenced_code
    ModuleNotFoundError: No module named 'commonmark_parser.fenced_code'
- RED: fenced-code-unclosed (FEATURE-FencedCode.md)
  intent: An unclosed fence consumes the remaining input and removes the opening indentation from content.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "fenced-code-unclosed.py", line 1, in <module>
        from commonmark_parser.fenced_code import parse_fenced_code
    ModuleNotFoundError: No module named 'commonmark_parser.fenced_code'
- RED: references-first-definition (FEATURE-ReferenceDefinitions.md)
  intent: Definitions are removed from paragraph content, labels match case insensitively, and the first matching definition wins.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "references-first-definition.py", line 1, in <module>
        from commonmark_parser.references import extract_definitions
    ModuleNotFoundError: No module named 'commonmark_parser.references'
- RED: references-remainder (FEATURE-ReferenceDefinitions.md)
  intent: A valid leading definition leaves subsequent paragraph text intact, while a malformed definition remains visible.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "references-remainder.py", line 1, in <module>
        from commonmark_parser.references import extract_definitions
    ModuleNotFoundError: No module named 'commonmark_parser.references'

## Post-build programmatic acceptance
- PASS: thematic-break-recognition (FEATURE-ThematicBreaks.md)
  intent: Matching marker runs form thematic breaks and interrupt an existing paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: thematic-break-invalid (FEATURE-ThematicBreaks.md)
  intent: A line with mixed markers remains paragraph content instead of forming a thematic break.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: indented-code-content (FEATURE-IndentedCode.md)
  intent: Four-column indentation is removed while extra indentation and interior blank lines remain literal.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: indented-code-interruption (FEATURE-IndentedCode.md)
  intent: Indented code does not interrupt an open paragraph and ends before a less-indented nonblank line.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: atx-heading-level (FEATURE-ATXHeadings.md)
  intent: A valid opening run produces the corresponding heading level and retains its content for inline parsing.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: atx-heading-interruption (FEATURE-ATXHeadings.md)
  intent: An ATX heading interrupts a paragraph and a marker without required separating whitespace stays in paragraph content.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: html-block-termination (FEATURE-HTMLBlocks.md)
  intent: A comment block preserves its lines through the line containing its closing marker.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: html-block-paragraph (FEATURE-HTMLBlocks.md)
  intent: A standalone custom tag cannot interrupt a paragraph, while a block-level tag can and ends before a blank line.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: fenced-code-matching (FEATURE-FencedCode.md)
  intent: A fence closes only with a sufficiently long matching delimiter and preserves intervening literal content.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: fenced-code-unclosed (FEATURE-FencedCode.md)
  intent: An unclosed fence consumes the remaining input and removes the opening indentation from content.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: references-first-definition (FEATURE-ReferenceDefinitions.md)
  intent: Definitions are removed from paragraph content, labels match case insensitively, and the first matching definition wins.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: references-remainder (FEATURE-ReferenceDefinitions.md)
  intent: A valid leading definition leaves subsequent paragraph text intact, while a malformed definition remains visible.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
Implemented thematic breaks, indented and fenced code blocks, ATX headings, raw HTML blocks, and document-wide reference definitions.

`python -m pytest -q` passed: 19 tests. The staged full conformance suite was not run.

RESULT: SUCCESS

FILES CHANGED:
- commonmark_parser/blocks.py
- commonmark_parser/fenced_code.py
- commonmark_parser/html_blocks.py
- commonmark_parser/indented_code.py
- commonmark_parser/references.py
- tests/test_service_blocks.py

SUMMARY:
Added the specified block parsers and reference collection, with focused tests for their public interfaces and block integration.

BLOCKERS:
- None
