# Evidence: Block 10 · Service (block-10)

- block type: block
- date: 2026-10-27
- resulting state: closed/verified
- story points (combined assembled cost): 4675
- execution id: 20261027.213148.636Z-1bae04d1

## Stories built
- Parse emphasis and strong emphasis. (emphasis) [story]
- Parse URI and email autolinks. (autolinks) [story]
- Parse raw inline HTML and hard line breaks. (inline-html-breaks) [story]

## Stacked context
- stack: python_compact.md (SP 654)
- compass: COMPASS.md (SP 548)
- implements: FEATURE-Emphasis.md (SP 747)
- context: ARCHITECTURE_compact.md (SP 304)
- stack: common_compact.md (SP 1079)
- implements: FEATURE-Autolinks.md (SP 568)
- implements: FEATURE-InlineHTMLBreaks.md (SP 581)

## Build directory changes
- commonmark_parser/autolinks.py
- commonmark_parser/inline_html_breaks.py
- commonmark_parser/inlines.py
- tests/test_inline_providers.py

## Pre-build acceptance observation
- RED: emphasis-basic (FEATURE-Emphasis.md)
  intent: A matching single delimiter pair produces an emphasis node containing the supplied text.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      nodes = [Inline(type='text', literal='*alpha*')]
    --- drydock: end values ---
    Traceback (most recent call last):
      File "emphasis-basic.py", line 6, in <module>
        assert nodes[0].type == "em"
               ^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: emphasis-strong (FEATURE-Emphasis.md)
  intent: A matching double delimiter pair produces a strong node containing the supplied text.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      nodes = [Inline(type='text', literal='**beta**')]
    --- drydock: end values ---
    Traceback (most recent call last):
      File "emphasis-strong.py", line 6, in <module>
        assert nodes[0].type == "strong"
               ^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): emphasis-intraword-underscore (FEATURE-Emphasis.md)
  intent: Underscores within a word remain literal rather than creating emphasis.
  return code: 0
- RED: autolinks-uri (FEATURE-Autolinks.md)
  intent: A valid angle-delimited URI becomes a link with the supplied URI as destination and label.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "autolinks-uri.py", line 1, in <module>
        from commonmark_parser.autolinks import parse_autolinks
    ModuleNotFoundError: No module named 'commonmark_parser.autolinks'
- RED: autolinks-email-and-invalid (FEATURE-Autolinks.md)
  intent: An email autolink receives the mail scheme, while an angle-delimited URI containing a space remains text.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "autolinks-email-and-invalid.py", line 1, in <module>
        from commonmark_parser.autolinks import parse_autolinks
    ModuleNotFoundError: No module named 'commonmark_parser.autolinks'
- RED: inline-html-raw (FEATURE-InlineHTMLBreaks.md)
  intent: A valid inline tag is preserved as a raw HTML node with its original spelling.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "inline-html-raw.py", line 1, in <module>
        from commonmark_parser.inline_html_breaks import parse_inline_html_breaks
    ModuleNotFoundError: No module named 'commonmark_parser.inline_html_breaks'
- RED: inline-hard-breaks (FEATURE-InlineHTMLBreaks.md)
  intent: Both specified hard-break forms create a break between text, while a trailing backslash remains text.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "inline-hard-breaks.py", line 1, in <module>
        from commonmark_parser.inline_html_breaks import parse_inline_html_breaks
    ModuleNotFoundError: No module named 'commonmark_parser.inline_html_breaks'

## Post-build programmatic acceptance
- PASS: emphasis-basic (FEATURE-Emphasis.md)
  intent: A matching single delimiter pair produces an emphasis node containing the supplied text.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: emphasis-strong (FEATURE-Emphasis.md)
  intent: A matching double delimiter pair produces a strong node containing the supplied text.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: emphasis-intraword-underscore (FEATURE-Emphasis.md)
  intent: Underscores within a word remain literal rather than creating emphasis.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: autolinks-uri (FEATURE-Autolinks.md)
  intent: A valid angle-delimited URI becomes a link with the supplied URI as destination and label.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: autolinks-email-and-invalid (FEATURE-Autolinks.md)
  intent: An email autolink receives the mail scheme, while an angle-delimited URI containing a space remains text.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: inline-html-raw (FEATURE-InlineHTMLBreaks.md)
  intent: A valid inline tag is preserved as a raw HTML node with its original spelling.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: inline-hard-breaks (FEATURE-InlineHTMLBreaks.md)
  intent: Both specified hard-break forms create a break between text, while a trailing backslash remains text.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark_parser/inlines.py
- commonmark_parser/autolinks.py
- commonmark_parser/inline_html_breaks.py
- tests/test_inline_providers.py

SUMMARY:
Added emphasis parsing with Unicode punctuation flanking, URI and email autolink recognition, and inline HTML and hard-break parsing. Added focused provider tests.

Checks run: `pytest -q tests/test_inline_text.py tests/test_inline_providers.py` — 19 passed. `pytest -q` — 56 passed.

BLOCKERS:
- Autolink and raw HTML nodes are exposed by their parsing APIs; HTML serialization is not covered here because the existing renderer is a stub.
