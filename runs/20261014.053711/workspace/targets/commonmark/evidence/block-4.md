# Evidence: Block 4 · Service (block-4)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 4576
- execution id: 20261014.060217.836Z-1b64b62b

## Stories built
- Parse URI and email autolinks. (autolinks) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Autolinks.md (SP 1381)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/inlines.py
- tests/test_autolinks.py

## Pre-build acceptance observation
- RED: autolinks-corpus-section (FEATURE-Autolinks.md)
  intent: The Autolinks conformance section (19 cases) passes in full.
  return code: 1
  stdout:
    Example 596 (lines 8805-8809) Autolinks
    <http://foo.bar.baz>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="http://foo.bar.baz">http://foo.bar.baz</a></p>
    +<p>&lt;http://foo.bar.baz&gt;</p>
    
    Example 597 (lines 8812-8816) Autolinks
    <https://foo.bar.baz/test?q=hello&id=22&boolean>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="https://foo.bar.baz/test?q=hello&amp;id=22&amp;boolean">https://foo.bar.baz/test?q=hello&amp;id=22&amp;boolean</a></p>
    +<p>&lt;https://foo.bar.baz/test?q=hello&amp;id=22&amp;boolean&gt;</p>
    
    Example 598 (lines 8819-8823) Autolinks
    <irc://foo.bar:2233/baz>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="irc://foo.bar:2233/baz">irc://foo.bar:2233/baz</a></p>
    +<p>&lt;irc://foo.bar:2233/baz&gt;</p>
    
    Example 599 (lines 8828-8832) Autolinks
    <MAILTO:FOO@BAR.BAZ>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="MAILTO:FOO@BAR.BAZ">MAILTO:FOO@BAR.BAZ</a></p>
    +<p>&lt;MAILTO:FOO@BAR.BAZ&gt;</p>
    
    Example 600 (lines 8840-8844) Autolinks
    <a+b+c:d>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="a+b+c:d">a+b+c:d</a></p>
    +<p>&lt;a+b+c:d&gt;</p>
    
    Example 601 (lines 8847-8851) Autolinks
    <made-up-scheme://foo,bar>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="made-up-scheme://foo,bar">made-up-scheme://foo,bar</a></p>
    +<p>&lt;made-up-scheme://foo,bar&gt;</p>
    
    Example 602 (lines 8854-8858) Autolinks
    <https://../>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="https://../">https://../</a></p>
    +<p>&lt;https://../&gt;</p>
    
    Example 603 (lines 8861-8865) Autolinks
    <localhost:5001/foo>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="localhost:5001/foo">localhost:5001/foo</a></p>
    +<p>&lt;localhost:5001/foo&gt;</p>
    
    Example 605 (lines 8879-8883) Autolinks
    <https://example.com/\[\>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="https://example.com/%5C%5B%5C">https://example.com/\[\</a></p>
    +<p>&lt;https://example.com/\[\&gt;</p>
    
    Example 606 (lines 8901-8905) Autolinks
    <foo@bar.example.com>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="mailto:foo@bar.example.com">foo@bar.example.com</a></p>
    +<p>&lt;foo@bar.example.com&gt;</p>
    
    Example 607 (lines 8908-8912) Autolinks
    <foo+special@Bar.baz-bar0.com>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="mailto:foo+special@Bar.baz-bar0.com">foo+special@Bar.baz-bar0.com</a></p>
    +<p>&lt;foo+special@Bar.baz-bar0.com&gt;</p>
    
    Example 608 (lines 8917-8921) Autolinks
    <foo\+@bar.example.com>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;foo+@bar.example.com&gt;</p>
    +<p>&lt;foo\+@bar.example.com&gt;</p>
    
    7 passed, 12 failed, 0 errored, 636 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=7 fail=12 error=0 skip=636 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^Autolinks$'], returncode=12, stdout='Example 596 (lines 8805-8809) Autolinks\n<htt… (+2748 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "autolinks-corpus-section.py", line 22, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: autolinks-uri-roundtrip (FEATURE-Autolinks.md)
  intent: A URI autolink renders as one link whose href and text are the supplied URI.
  return code: 1
  stdout:
    <p>&lt;http://example.org/path&gt;</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>&lt;http://example.org/path&gt;</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "autolinks-uri-roundtrip.py", line 7, in <module>
        assert result.stdout.count("<a ") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: autolinks-email-mailto (FEATURE-Autolinks.md)
  intent: An email autolink renders with a mailto href built from the supplied address.
  return code: 1
  stdout:
    <p>&lt;someone@example.org&gt;</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>&lt;someone@example.org&gt;</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "autolinks-email-mailto.py", line 7, in <module>
        assert result.stdout.count("<a ") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): autolinks-space-not-autolink (FEATURE-Autolinks.md)
  intent: A URI containing a space is not an autolink, so no link element is produced.
  return code: 0
  stdout:
    <p>&lt;http://example.org/a b&gt;</p>

## Post-build programmatic acceptance
- PASS: autolinks-corpus-section (FEATURE-Autolinks.md)
  intent: The Autolinks conformance section (19 cases) passes in full.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    19 passed, 0 failed, 0 errored, 636 skipped
- PASS: autolinks-uri-roundtrip (FEATURE-Autolinks.md)
  intent: A URI autolink renders as one link whose href and text are the supplied URI.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><a href="http://example.org/path">http://example.org/path</a></p>
- PASS: autolinks-email-mailto (FEATURE-Autolinks.md)
  intent: An email autolink renders with a mailto href built from the supplied address.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><a href="mailto:someone@example.org">someone@example.org</a></p>
- PASS: autolinks-space-not-autolink (FEATURE-Autolinks.md)
  intent: A URI containing a space is not an autolink, so no link element is produced.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>&lt;http://example.org/a b&gt;</p>

## Build summary
All 19 Autolinks examples pass. Now I'll tighten one long docstring and write the project tests, including the declared acceptance checks.Before running, I re-checked some of my hand-written expectations and found errors: the `%`/`^`/`~` encoding in the complicated email href, a body case that is actually a valid autolink, and an email label computed through the code under test. Fixing those now.All 182 tests pass. Checking the working tree for only the intended changes and any over-long lines:RESULT: SUCCESS

FILES CHANGED:
- mdparser/inlines.py
- tests/test_autolinks.py

SUMMARY:
- `parse_inline` now scans left to right. At a `<` it tries a URI autolink (scheme of 2 to 32 characters, then a colon, then a body with no control characters, space, `<` or `>`), then an email autolink (the spec's HTML5 regex, with `mailto:` prepended). Matches become `<a href>` with the href percent-encoded and then HTML-escaped, and the label HTML-escaped. Anything else stays escaped text.
- Backslash escapes are inert inside an autolink because the whole autolink is consumed first. Outside autolinks, a backslash before ASCII punctuation yields that character, so `\<` does not open an autolink.
- Gate: `python3 sources/spec_tests.py --program ./commonmark --spec sources/spec.txt --pattern '^Autolinks$'` gives 19 passed, 0 failed, 0 errored, exit 0.
- Tests: `tests/test_autolinks.py` has the three declared acceptance checks as tests, plus the scoped corpus gate run as a subprocess. Finer tests cover scheme length boundaries (2, 32, 33 characters), email label length (63 and 64), malformed emails, percent-encoding of non-ASCII, backtick and existing `%XX`, control characters, `&` escaping, and left-to-right scanning. Each test compares a return value or stdout bytes exactly.
- `.venv/bin/python -m pytest -q` gives 182 passed. Only `mdparser/inlines.py` changed and the new test file was added; nothing under `sources/` was touched.
- I did not run `sources/full_test.sh`, because this step declares only the scoped gate.

BLOCKERS:
- None.

<blueprint-decisions>
[{"spec":"FEATURE-Autolinks.md","severity":"Low","subject":"Minimal backslash-escape handling in the inline scanner","decision":"The Autolinks section's example `<foo\\+@bar.example.com>` expects the backslash in front of `+` to be removed outside the autolink, and the gate requires that example to pass. I therefore added a minimal rule to the inline scanner: a backslash before ASCII punctuation yields that character. A full backslash-escape story would replace this, and autolink behaviour does not depend on it. Is that acceptable, or should it move to the entities module on replan?"}]
</blueprint-decisions>
