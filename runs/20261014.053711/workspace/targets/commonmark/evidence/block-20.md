# Evidence: Block 20 · Service (block-20)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 5441
- execution id: 20261014.075451.866Z-23e771a2

## Stories built
- Parse setext headings, including multiline content and underline precedence. (setext-headings) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Setext-Headings.md (SP 2267)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/blocks.py
- mdparser/render.py
- tests/test_blocks.py
- tests/test_setext_headings.py

## Pre-build acceptance observation
- RED: setext-both-levels (FEATURE-Setext-Headings.md)
  intent: Equals underlines give h1 and dash underlines give h2.
  return code: 1
  stdout:
    <p>Foo <em>bar</em>
    =========</p>
    
    <p>Foo <em>bar</em></p>
    <hr />
  stderr:
    --- drydock: values at failure ---
      equals = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>Foo <em>bar</em>\n=========</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "setext-both-levels.py", line 9, in <module>
        assert equals.stdout.count("<h1>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: setext-multiline-content (FEATURE-Setext-Headings.md)
  intent: Several paragraph lines before the underline become one heading with no paragraph.
  return code: 1
  stdout:
    <p>Foo
    Bar</p>
    <hr />
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>Foo\nBar</p>\n<hr />\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "setext-multiline-content.py", line 6, in <module>
        assert result.stdout.count("<h2>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: setext-underline-beats-thematic-break (FEATURE-Setext-Headings.md)
  intent: Dashes after paragraph text make a heading, not a thematic break.
  return code: 1
  stdout:
    <p>Foo</p>
    <hr />
    <p>bar</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>Foo</p>\n<hr />\n<p>bar</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "setext-underline-beats-thematic-break.py", line 6, in <module>
        assert result.stdout.count("<h2>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: setext-sequence-with-thematic-breaks (FEATURE-Setext-Headings.md)
  intent: Dashes with no preceding paragraph are thematic breaks, mixed with two setext headings and a paragraph.
  return code: 1
  stdout:
    <hr />
    <p>Foo</p>
    <hr />
    <p>Bar</p>
    <hr />
    <p>Baz</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<hr />\n<p>Foo</p>\n<hr />\n<p>Bar</p>\n<hr />\n<p>Baz</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "setext-sequence-with-thematic-breaks.py", line 6, in <module>
        assert result.stdout.count("<hr />") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): setext-underline-limits (FEATURE-Setext-Headings.md)
  intent: Four spaces of indentation or internal spaces disqualify the underline.
  return code: 0
  stdout:
    <p>Foo
    ---</p>
    
    <p>Foo
    = =</p>
- GREEN (prepassed): setext-not-lazy-in-quote (FEATURE-Setext-Headings.md)
  intent: An unmarked underline after a quote paragraph does not make a heading inside the quote.
  return code: 0
  stdout:
    <blockquote>
    <p>foo
    bar
    ===</p>
    </blockquote>
- GREEN (prepassed): setext-quote-then-thematic-break (FEATURE-Setext-Headings.md)
  intent: Dashes after a quote without a marker are a thematic break outside the quote.
  return code: 0
  stdout:
    <blockquote>
    <p>Foo</p>
    </blockquote>
    <hr />
- GREEN (prepassed): setext-empty-is-paragraph (FEATURE-Setext-Headings.md)
  intent: An underline with no content line is not a heading.
  return code: 0
  stdout:
    <p>====</p>

## Post-build programmatic acceptance
- PASS: setext-both-levels (FEATURE-Setext-Headings.md)
  intent: Equals underlines give h1 and dash underlines give h2.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <h1>Foo <em>bar</em></h1>
    
    <h2>Foo <em>bar</em></h2>
- PASS: setext-multiline-content (FEATURE-Setext-Headings.md)
  intent: Several paragraph lines before the underline become one heading with no paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <h2>Foo
    Bar</h2>
- PASS: setext-underline-beats-thematic-break (FEATURE-Setext-Headings.md)
  intent: Dashes after paragraph text make a heading, not a thematic break.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <h2>Foo</h2>
    <p>bar</p>
- PASS: setext-sequence-with-thematic-breaks (FEATURE-Setext-Headings.md)
  intent: Dashes with no preceding paragraph are thematic breaks, mixed with two setext headings and a paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <hr />
    <h2>Foo</h2>
    <h2>Bar</h2>
    <p>Baz</p>
- PASS: setext-underline-limits (FEATURE-Setext-Headings.md)
  intent: Four spaces of indentation or internal spaces disqualify the underline.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>Foo
    ---</p>
    
    <p>Foo
    = =</p>
- PASS: setext-not-lazy-in-quote (FEATURE-Setext-Headings.md)
  intent: An unmarked underline after a quote paragraph does not make a heading inside the quote.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <blockquote>
    <p>foo
    bar
    ===</p>
    </blockquote>
- PASS: setext-quote-then-thematic-break (FEATURE-Setext-Headings.md)
  intent: Dashes after a quote without a marker are a thematic break outside the quote.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <blockquote>
    <p>Foo</p>
    </blockquote>
    <hr />
- PASS: setext-empty-is-paragraph (FEATURE-Setext-Headings.md)
  intent: An underline with no content line is not a heading.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>====</p>

## Build summary
Baseline is green (991 passed, 1 skipped). Now I'll add the setext rule to the block engine, register it ahead of thematic breaks so dashes after a paragraph win, and render the new block kind.Now the test file: the declared acceptance checks transcribed unchanged, plus block-tree and exact-output tests.Two expectations I wrote need correcting before I run them: a trailing-space hard break *between* heading lines is valid (only the last line's trailing spaces are dropped), and one test name is misleading.Both failures are mistakes in my test expectations, not the engine. `"  \tFoo  "` is four columns of indentation, so it's an indented code block; and paragraph lines drop their leading whitespace, so the content is `Foo\n===`. Fixing the tests:Now the new file, then the whole project suite in the background to check for regressions against the 991-pass baseline.Same mistake again: a space followed by a tab reaches column 4, so it's still indented code. The single-space case is the one I meant to test, so I'll use that.The new file is green (48 passed). Waiting on the full-suite run:The background run started before my last test fix, so the `strips_surrounding` failure there is stale. The real regression is an existing registry-order test in `test_blocks.py`, which pins the start-rule list. Let me look at it.This test pins the old start-rule order. Adding the setext rule ahead of thematic break is an intended change, so I'll update the expectation (it isn't a declared acceptance check) and rename it to match.RESULT: SUCCESS

FILES CHANGED:
- mdparser/blocks.py
- mdparser/render.py
- tests/test_blocks.py
- tests/test_setext_headings.py

SUMMARY:
Setext headings are implemented as a registered block type, `setext_heading`, with a start rule that runs only when the open container is a paragraph.

- **Underline rule:** the line must have at most three columns of indentation, one run of a single `=` or `-`, and only trailing spaces or tabs. Internal spaces disqualify it. `=` gives level 1 and `-` gives level 2.
- **Whole-paragraph content:** the heading content is all paragraph lines joined, with surrounding spaces and tabs stripped. Leading link reference definitions are extracted into the document map first and do not become heading text.
- **Empty guard:** if no text remains after definitions, the rule declines. The underline then stays paragraph text, or becomes a thematic break for dashes.
- **Precedence:** the setext rule is registered before the thematic-break rule, so dashes after paragraph text make a heading.
- **Lazy continuation:** the rule never fires for a lazy line, so `> foo\nbar\n===` stays a paragraph inside the quote.
- **Tree mechanics:** the paragraph's lines are cleared, so it closes empty and leaves the tree. The heading is attached in its place.
- **Rendering:** `render.py` emits `<hN>` for `setext_heading` the same way it does for ATX headings.

Tests:
- `tests/test_setext_headings.py` (new, 48 tests) transcribes the seven declared acceptance checks unchanged and adds block-tree and exact-output tests. It passes 48/48.
- `tests/test_blocks.py`: I updated one existing test that pinned the old start-rule order to include the new rule first, and renamed it to match. This is an intended change, not a weakened assertion.
- Full project suite: 1037 passed, 1 skipped, 2 failed. One failure was the registry-order test I then updated. The other was a bad input in my own new test, which I then fixed. After those edits, the affected files (test_blocks, test_setext_headings, test_thematic_breaks, test_atx_headings, test_block_quotes, test_block_engine) pass 253/253. I did not rerun the entire suite after the last two edits.

Not run: `sources/full_test.sh` and `spec_tests.py`. The setext corpus examples are gated in the lists story, so I did not invoke the staged corpus here. No commits were made.

BLOCKERS:
- none
