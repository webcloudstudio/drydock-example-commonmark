# Evidence: Block 7 · Service (block-7)

- block type: block
- date: 2026-10-26
- resulting state: closed/verified
- story points (combined assembled cost): 3516
- execution id: 20261027.024509.089Z-8c1e4cad

## Stories built
- Parse backslash escapes and character references. (escapes) [story]
- Document the standard-stream command interface. (documentation) [story]

## Stacked context
- stack: python_compact.md (SP 601)
- compass: COMPASS.md (SP 512)
- implements: FEATURE-EscapesAndEntities.md (SP 719)
- context: ARCHITECTURE_compact.md (SP 211)
- stack: common_compact.md (SP 1079)
- implements: FEATURE-Documentation.md (SP 236)

## Build directory changes
- README.md
- commonmark_parser/inline.py
- commonmark_parser/references.py
- commonmark_parser/stages.py
- tests/test_escapes_and_entities.py

## Pre-build acceptance observation
- RED: escaped-punctuation (FEATURE-EscapesAndEntities.md)
  intent: A backslash before ASCII punctuation produces the punctuation supplied in the source.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "escaped-punctuation.py", line 1, in <module>
        from commonmark_parser.inline import decode_escapes_and_entities
    ModuleNotFoundError: No module named 'commonmark_parser.inline'
- RED: unescaped-character (FEATURE-EscapesAndEntities.md)
  intent: A backslash before a non-punctuation character remains literal.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "unescaped-character.py", line 1, in <module>
        from commonmark_parser.inline import decode_escapes_and_entities
    ModuleNotFoundError: No module named 'commonmark_parser.inline'
- RED: numeric-reference (FEATURE-EscapesAndEntities.md)
  intent: A valid numeric character reference resolves to the character represented by its supplied code point.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "numeric-reference.py", line 1, in <module>
        from commonmark_parser.inline import decode_escapes_and_entities
    ModuleNotFoundError: No module named 'commonmark_parser.inline'
- RED: documentation-readable (FEATURE-Documentation.md)
  intent: The application README exists and can be read as nonempty UTF-8 documentation.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      self = PosixPath('README.md')
      mode = 'r'
      buffering = -1
      encoding = 'utf-8'
      errors = None
      newline = None
    --- drydock: end values ---
    Traceback (most recent call last):
      File "documentation-readable.py", line 3, in <module>
        content = Path("README.md").read_text(encoding="utf-8")
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/pathlib.py", line 1027, in read_text
        with self.open(mode='r', encoding=encoding, errors=errors) as f:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/pathlib.py", line 1013, in open
        return io.open(self, mode, buffering, encoding, errors, newline)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'README.md'

## Post-build programmatic acceptance
- PASS: escaped-punctuation (FEATURE-EscapesAndEntities.md)
  intent: A backslash before ASCII punctuation produces the punctuation supplied in the source.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: unescaped-character (FEATURE-EscapesAndEntities.md)
  intent: A backslash before a non-punctuation character remains literal.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: numeric-reference (FEATURE-EscapesAndEntities.md)
  intent: A valid numeric character reference resolves to the character represented by its supplied code point.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: documentation-readable (FEATURE-Documentation.md)
  intent: The application README exists and can be read as nonempty UTF-8 documentation.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- README.md
- commonmark_parser/inline.py
- commonmark_parser/references.py
- commonmark_parser/stages.py
- tests/test_escapes_and_entities.py

SUMMARY:
Added ASCII punctuation escape and HTML5 named/numeric reference decoding, applied decoding to paragraph, heading, fenced-code info, and reference-definition text, and documented the standard-stream CLI. `pytest -q` passed (41 tests); the declared decoder and README assertions passed.

BLOCKERS:
- None
