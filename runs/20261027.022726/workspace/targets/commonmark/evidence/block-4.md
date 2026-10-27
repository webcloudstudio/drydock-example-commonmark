# Evidence: Block 4 · Service (block-4)

- block type: block
- date: 2026-10-26
- resulting state: closed/verified
- story points (combined assembled cost): 5456
- execution id: 20261027.023711.000Z-f679c927

## Stories built
- Parse ATX and setext headings. (headings) [story]
- Parse indented and fenced code blocks. (code-blocks) [story]
- Collect document-wide link reference definitions. (references) [story]
- Parse the seven types of HTML blocks. (html-blocks) [story]

## Stacked context
- stack: python_compact.md (SP 601)
- compass: COMPASS.md (SP 512)
- implements: FEATURE-Headings.md (SP 627)
- context: ARCHITECTURE_compact.md (SP 211)
- stack: common_compact.md (SP 1079)
- implements: FEATURE-CodeBlocks.md (SP 667)
- implements: FEATURE-ReferenceDefinitions.md (SP 684)
- implements: FEATURE-HtmlBlocks.md (SP 756)

## Build directory changes
- commonmark_parser/html_blocks.py
- commonmark_parser/model.py
- commonmark_parser/references.py
- commonmark_parser/stages.py
- tests/test_block_features.py
- tests/test_command_line.py
- tests/test_parser_foundation.py

## Pre-build acceptance observation
- RED: atx-heading-block (FEATURE-Headings.md)
  intent: Block parsing records an ATX heading's level and raw content for the inline phase.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      document = Document(children=[Node(type='paragraph', children=[], raw='## alpha')], references={})
    --- drydock: end values ---
    Traceback (most recent call last):
      File "atx-heading-block.py", line 6, in <module>
        assert document.children[0].type == "heading"
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: setext-heading-block (FEATURE-Headings.md)
  intent: A setext underline converts the preceding paragraph into a heading.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      document = Document(children=[Node(type='paragraph', children=[], raw='alpha'), Node(type='thematic_break', children=[], raw='')], references={})
    --- drydock: end values ---
    Traceback (most recent call last):
      File "setext-heading-block.py", line 5, in <module>
        assert len(document.children) == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: indented-code-block (FEATURE-CodeBlocks.md)
  intent: Block parsing removes the required indentation and preserves the literal code content.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      document = Document(children=[Node(type='paragraph', children=[], raw='alpha * beta')], references={})
    --- drydock: end values ---
    Traceback (most recent call last):
      File "indented-code-block.py", line 6, in <module>
        assert document.children[0].type == "code_block"
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: fenced-code-block (FEATURE-CodeBlocks.md)
  intent: Matching fences form a code block whose content remains literal.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      document = Document(children=[Node(type='paragraph', children=[], raw='```\nalpha * beta\n```')], references={})
    --- drydock: end values ---
    Traceback (most recent call last):
      File "fenced-code-block.py", line 6, in <module>
        assert document.children[0].type == "code_block"
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: reference-first-definition (FEATURE-ReferenceDefinitions.md)
  intent: Matching labels share one document-wide entry and the earliest definition wins.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "reference-first-definition.py", line 1, in <module>
        from commonmark_parser.references import collect_definitions
    ModuleNotFoundError: No module named 'commonmark_parser.references'
- RED: reference-remainder (FEATURE-ReferenceDefinitions.md)
  intent: Closing a paragraph removes its initial definition while retaining subsequent paragraph content.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "reference-remainder.py", line 1, in <module>
        from commonmark_parser.references import collect_definitions
    ModuleNotFoundError: No module named 'commonmark_parser.references'
- RED: html-block-termination (FEATURE-HtmlBlocks.md)
  intent: A comment block retains its source through the line containing its end marker and leaves later lines unconsumed.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "html-block-termination.py", line 1, in <module>
        from commonmark_parser.html_blocks import parse_html_block
    ModuleNotFoundError: No module named 'commonmark_parser.html_blocks'
- RED: html-block-paragraph-interruption (FEATURE-HtmlBlocks.md)
  intent: A complete non-block tag cannot interrupt a paragraph but can begin a type 7 HTML block outside one.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "html-block-paragraph-interruption.py", line 1, in <module>
        from commonmark_parser.html_blocks import parse_html_block
    ModuleNotFoundError: No module named 'commonmark_parser.html_blocks'

## Post-build programmatic acceptance
- PASS: atx-heading-block (FEATURE-Headings.md)
  intent: Block parsing records an ATX heading's level and raw content for the inline phase.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: setext-heading-block (FEATURE-Headings.md)
  intent: A setext underline converts the preceding paragraph into a heading.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: indented-code-block (FEATURE-CodeBlocks.md)
  intent: Block parsing removes the required indentation and preserves the literal code content.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: fenced-code-block (FEATURE-CodeBlocks.md)
  intent: Matching fences form a code block whose content remains literal.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: reference-first-definition (FEATURE-ReferenceDefinitions.md)
  intent: Matching labels share one document-wide entry and the earliest definition wins.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: reference-remainder (FEATURE-ReferenceDefinitions.md)
  intent: Closing a paragraph removes its initial definition while retaining subsequent paragraph content.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: html-block-termination (FEATURE-HtmlBlocks.md)
  intent: A comment block retains its source through the line containing its end marker and leaves later lines unconsumed.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: html-block-paragraph-interruption (FEATURE-HtmlBlocks.md)
  intent: A complete non-block tag cannot interrupt a paragraph but can begin a type 7 HTML block outside one.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark_parser/model.py
- commonmark_parser/stages.py
- commonmark_parser/html_blocks.py
- commonmark_parser/references.py
- tests/test_block_features.py
- tests/test_command_line.py
- tests/test_parser_foundation.py

SUMMARY:
Implemented heading, code block, reference definition, and seven type HTML block parsing, with rendering support and focused tests. All 8 declared acceptance assertions passed; `python -m pytest -q` passed (24 tests).

BLOCKERS:
- None.
