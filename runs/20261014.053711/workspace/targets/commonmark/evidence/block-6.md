# Evidence: Block 6 · Service (block-6)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 4814
- execution id: 20261014.060854.186Z-5eadb737

## Stories built
- Parse code spans and establish the inline precedence order. (code-spans) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Code-Spans.md (SP 1620)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/inlines.py
- tests/test_code_spans.py

## Pre-build acceptance observation
- RED: codespans-corpus-sections (FEATURE-Code-Spans.md)
  intent: The Code spans and Inlines conformance sections (23 cases) pass in full.
  return code: 1
  stdout:
    Example 329 (lines 5876-5880) Inlines
    `hi`lo`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>hi</code>lo`</p>
    +<p>`hi`lo`</p>
    
    Example 330 (lines 5908-5912) Code spans
    `foo`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo</code></p>
    +<p>`foo`</p>
    
    Example 331 (lines 5919-5923) Code spans
    `` foo ` bar ``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo ` bar</code></p>
    +<p>`` foo ` bar ``</p>
    
    Example 332 (lines 5929-5933) Code spans
    ` `` `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>``</code></p>
    +<p>` `` `</p>
    
    Example 333 (lines 5937-5941) Code spans
    `  ``  `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code> `` </code></p>
    +<p>` `` `</p>
    
    Example 334 (lines 5946-5950) Code spans
    ` a`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code> a</code></p>
    +<p>` a`</p>
    
    Example 335 (lines 5955-5959) Code spans
    ` b `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code> b </code></p>
    +<p>` b `</p>
    
    Example 336 (lines 5963-5969) Code spans
    ` `
    `  `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code> </code> <code> </code></p>
    +<p>` ` ` `</p>
    
    Example 337 (lines 5974-5982) Code spans
    ``
    foo
    bar  
    baz
    ``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo bar baz</code></p>
    +<p>`` foo bar baz ``</p>
    
    Example 338 (lines 5984-5990) Code spans
    ``
    foo 
    ``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo </code></p>
    +<p>`` foo ``</p>
    
    Example 339 (lines 5995-6000) Code spans
    `foo   bar 
    baz`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo bar baz</code></p>
    +<p>`foo bar baz`</p>
    
    Example 340 (lines 6012-6016) Code spans
    `foo\`bar`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo\</code>bar`</p>
    +<p>`foo`bar`</p>
    
    Example 341 (lines 6023-6027) Code spans
    ``foo`bar``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo`bar</code></p>
    +<p>``foo`bar``</p>
    
    Example 342 (lines 6029-6033) Code spans
    ` foo `` bar `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo `` bar</code></p>
    +<p>` foo `` bar `</p>
    
    Example 343 (lines 6041-6045) Code spans
    *foo`*`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo<code>*</code></p>
    +<p>*foo`*`</p>
    
    Example 344 (lines 6050-6054) Code spans
    [not a `link](/foo`)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[not a <code>link](/foo</code>)</p>
    +<p>[not a `link](/foo`)</p>
    
    Example 345 (lines 6060-6064) Code spans
    `<a href="`">`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>&lt;a href=&quot;</code>&quot;&gt;`</p>
    +<p>`<a href="`">`</p>
    
    Example 347 (lines 6078-6082) Code spans
    `<https://foo.bar.`baz>`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>&lt;https://foo.bar.</code>baz&gt;`</p>
    +<p>`<a href="https://foo.bar.%60baz">https://foo.bar.`baz</a>`</p>
    
    Example 351 (lines 6113-6117) Code spans
    `foo``bar``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>`foo<code>bar</code></p>
    +<p>`foo``bar``</p>
    
    4 passed, 19 failed, 0 errored, 632 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=4 fail=19 error=0 skip=632 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^Code spans$|^Inlines$'], returncode=19, stdout='Example 329 (lines 5876-5880) Inli… (+3144 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "codespans-corpus-sections.py", line 22, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: codespans-simple (FEATURE-Code-Spans.md)
  intent: A single-backtick span renders one code element containing the supplied content.
  return code: 1
  stdout:
    <p>`some code`</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>`some code`</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "codespans-simple.py", line 7, in <module>
        assert result.stdout.count("<code>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: codespans-backtick-length-match (FEATURE-Code-Spans.md)
  intent: A double-backtick span may contain a single backtick, which is kept inside one code element.
  return code: 1
  stdout:
    <p>``a`b``</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>``a`b``</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "codespans-backtick-length-match.py", line 7, in <module>
        assert result.stdout.count("<code>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): codespans-unclosed-literal (FEATURE-Code-Spans.md)
  intent: An unmatched backtick run is literal text and produces no code element.
  return code: 0
  stdout:
    <p>```foo``</p>
- RED: codespans-escapes-inert (FEATURE-Code-Spans.md)
  intent: A backslash inside a code span is kept literally.
  return code: 1
  stdout:
    <p>`[`</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>`[`</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "codespans-escapes-inert.py", line 7, in <module>
        assert result.stdout.count("<code>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: codespans-corpus-sections (FEATURE-Code-Spans.md)
  intent: The Code spans and Inlines conformance sections (23 cases) pass in full.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    23 passed, 0 failed, 0 errored, 632 skipped
- PASS: codespans-simple (FEATURE-Code-Spans.md)
  intent: A single-backtick span renders one code element containing the supplied content.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><code>some code</code></p>
- PASS: codespans-backtick-length-match (FEATURE-Code-Spans.md)
  intent: A double-backtick span may contain a single backtick, which is kept inside one code element.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><code>a`b</code></p>
- PASS: codespans-unclosed-literal (FEATURE-Code-Spans.md)
  intent: An unmatched backtick run is literal text and produces no code element.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>```foo``</p>
- PASS: codespans-escapes-inert (FEATURE-Code-Spans.md)
  intent: A backslash inside a code span is kept literally.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><code>\[</code></p>

## Build summary
Baseline is green (263 passed). Now I'll add the code span construct to the inline scanner.Now the test file, with the four declared acceptance checks transcribed plus the scoped corpus gate and finer coverage.Before running, I re-derived several expected values by hand and found some wrong. Fixing those now so the tests assert the spec behaviour, not my first guesses.Now I'll run the new tests, then the full project suite to check for regressions in the earlier blocks.The implementation is right here and my expectation was wrong: the trailing backtick has no partner, so it stays literal. Correcting the assertion.The scoped gate passes and the full project suite is green. I wrote a scratch log to `/tmp`, which is outside the authorized build directory, so I'm removing it.RESULT: SUCCESS

FILES CHANGED:
- mdparser/inlines.py
- tests/test_code_spans.py

SUMMARY:
- Code spans are added to the inline scanner in `mdparser/inlines.py`. At a backtick, the scanner takes the whole maximal run and looks for the next run of exactly the same length. The content is normalized (line endings become spaces, then one leading and one trailing U+0020 is removed only when the content is not all spaces), HTML-escaped, and rendered as `<code>`. Backslashes and entities stay inert inside the span.
- An unmatched run is emitted as literal escaped text and the whole run is consumed, so a shorter run inside it cannot open a span by mistake.
- Precedence is left to right: the scanner tries code span, autolink and raw HTML at whichever special character comes first, so the first one found wins. A backslash before a backtick still makes that backtick literal.
- `tests/test_code_spans.py` transcribes the four declared acceptance checks plus the scoped corpus gate, and adds unit tests for run matching, normalization, escapes, and precedence against autolinks and raw HTML.

Test results:
- Declared gate, exact invocation `spec_tests.py --pattern '^Code spans$|^Inlines$'`: exit 0, 23 passed, 0 failed, 0 errored, 632 skipped.
- Project suite `pytest -q`: 291 passed (baseline was 263 before this step).
- I did not run the unscoped `sources/full_test.sh`, since this step's criteria only declare the scoped invocation. The Precedence section needs lists and is gated in the lists story.

Choices I made:
- Unmatched backtick runs are consumed as a whole, not one backtick at a time. Reading them one at a time would let a shorter tail of the run open a span wrongly.
- Only the `\n` line separator is handled in code content. `split_lines` already normalizes CR and CRLF, so no other line-ending cases arise here.

Staged assets in `sources/`, the guardrail files, and git history were not touched. Nothing was staged or committed.
