# Evidence: Block 3 · Service (block-3)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 5323
- execution id: 20261014.055651.247Z-954e899e

## Stories built
- Implement the Appendix phase 1 block engine and paragraph rendering with HTML escaping. (block-engine) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Block-Engine.md (SP 1846)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- data/logs/test_2026-10-14_020117.log
- mdparser/blocks.py
- mdparser/cli.py
- mdparser/inlines.py
- mdparser/render.py
- tests/test_block_engine.py
- tests/test_blocks.py
- tests/test_executable.py
- tests/test_foundation.py
- tests/test_render.py

## Pre-build acceptance observation
- RED: engine-paragraph-count (FEATURE-Block-Engine.md)
  intent: Blank-line-separated paragraphs render as one p element each.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      paragraphs = ['alpha beta', 'gamma delta', 'epsilon']
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "engine-paragraph-count.py", line 9, in <module>
        assert result.stdout.count("<p>") == len(paragraphs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: engine-multiline-paragraph (FEATURE-Block-Engine.md)
  intent: Consecutive non-blank lines with arbitrary indentation after the first stay in one paragraph.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "engine-multiline-paragraph.py", line 10, in <module>
        assert result.stdout.count("<p>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: engine-blank-lines-ignored (FEATURE-Block-Engine.md)
  intent: Leading, trailing and repeated blank lines produce no extra blocks, and a blank-only document produces no paragraph.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "engine-blank-lines-ignored.py", line 8, in <module>
        assert result.stdout.count("<p>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: engine-html-escaping (FEATURE-Block-Engine.md)
  intent: Special characters in paragraph text are escaped, so only the paragraph tags contribute angle brackets.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "engine-html-escaping.py", line 7, in <module>
        assert result.stdout.count("<") == 2
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: engine-paragraph-count (FEATURE-Block-Engine.md)
  intent: Blank-line-separated paragraphs render as one p element each.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>alpha beta</p>
    <p>gamma delta</p>
    <p>epsilon</p>
- PASS: engine-multiline-paragraph (FEATURE-Block-Engine.md)
  intent: Consecutive non-blank lines with arbitrary indentation after the first stay in one paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>first line
    second line
    third line</p>
- PASS: engine-blank-lines-ignored (FEATURE-Block-Engine.md)
  intent: Leading, trailing and repeated blank lines produce no extra blocks, and a blank-only document produces no paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>content</p>
- PASS: engine-html-escaping (FEATURE-Block-Engine.md)
  intent: Special characters in paragraph text are escaped, so only the paragraph tags contribute angle brackets.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>x &lt; y &gt; z &amp; w</p>

## Build summary
The build directory already has the executable, the `mdparser` skeleton, and placeholder tests from earlier blocks. I'll read the remaining module files before I write anything.Before changing anything, I'll get a baseline test run.Baseline is 47 passing. Now the block engine: a registry of block types, a cursor with tab-stop-aware columns, and the per-line procedure.Next, the renderer (escaping, URL percent-encoding, phase 2 walk), the inline hook, and wiring in the CLI.The earlier placeholder tests assert that nothing renders yet, so they must change with the engine. I'll update those assertions and the no-behavior module list.Now the tests. Block-engine tests read back the tree structure and content; render tests check exact return values.I left a meaningless assertion (`... or True`) in the raw-block test and an awkward double comprehension. Fixing both now.Now the render and inline-hook tests, then the declared acceptance checks transcribed as tests, plus exact end-to-end output checks.Running the full suite through the project's declared runner.All 132 pass. Before reporting, I'll spot-check the executable directly on a few inputs the tests touch only indirectly, and confirm the staged assets are untouched.<blueprint-decisions>
[{"spec":"FEATURE-Block-Engine.md","severity":"Low","subject":"Leading whitespace on paragraph continuation lines","decision":"Stripped at block level when a line joins a paragraph (the Appendix procedure advances past indentation before adding text). Trailing spaces and tabs are stripped from the whole paragraph at close, and interior trailing spaces are kept for later hard-break handling. The spec says only initial and final whitespace is removed, so this is the reading I took. Is that acceptable, or should continuation indentation pass through to the inline hook?"},{"spec":"FEATURE-Block-Engine.md","severity":"Low","subject":"Partially consumed tabs","decision":"Cursor.advance_columns consumes a tab that straddles the target column whole, so the column can overshoot. Partial-tab handling is needed only by block stories that split tabs, such as list item and indented code. Should that story replace this behavior?"},{"spec":"FEATURE-Block-Engine.md","severity":"Low","subject":"Where the inline hook lives","decision":"The hook is parse_inline in mdparser/inlines.py, which returns escape_html(raw). render_document takes it as an argument, so render does not import inlines and the import graph has no cycle. cli wires the two together."}]
</blueprint-decisions>

The block engine and paragraph rendering are implemented, and the project suite passes: 132 tests, up from 47. The four declared acceptance checks pass as transcribed, and the staged `sources/` files are unchanged. I did not run `sources/full_test.sh`, because no criterion in this step invokes it.

**What was built**
- `mdparser/blocks.py`: a `BlockType` record (start, continue, and finalize rules, plus flags for leaf, interruptible, and lazy), a `BlockRegistry`, a `Cursor` with tab-stop-4 column tracking, and a `DocumentParser` implementing the three-step per-line procedure. Start rules are tried before any unmatched block is closed, and lazy continuation is handled. Paragraphs are the only registered text leaf.
- `mdparser/render.py`: `escape_html` (ampersand first, then `<`, `>`, `"`), `percent_encode_url` for the link stories, and the phase 2 walk that renders `<p>…</p>\n` per paragraph.
- `mdparser/inlines.py`: `parse_inline`, the hook, which currently returns the escaped text.
- `mdparser/cli.py`: `render_lines` now parses and renders. Its exit status and error handling are unchanged.

**Existing tests I changed**
Some earlier placeholder tests asserted that nothing renders yet, so they had to change:
- `test_executable.py`: the "runs from another working directory" test and the invalid-UTF-8 test now expect rendered paragraphs. The placeholder render test now checks two paragraphs.
- `test_foundation.py`: `blocks`, `render`, and `inlines` are removed from the no-behavior list.

**New tests**
- `tests/test_blocks.py`: column helpers, the cursor, paragraph rules, registry extensibility, and lazy continuation through a test-only quote container.
- `tests/test_render.py`: escaping, percent-encoding, the phase 2 hook wiring, and the inline hook.
- `tests/test_block_engine.py`: the four declared checks transcribed with their assertions unchanged, plus exact-output checks through the executable.

**Files changed**
- `mdparser/blocks.py`, `mdparser/render.py`, `mdparser/inlines.py`, `mdparser/cli.py`
- `tests/test_executable.py`, `tests/test_foundation.py`
- New: `tests/test_blocks.py`, `tests/test_render.py`, `tests/test_block_engine.py`

I did not commit, per the build rules.

RESULT: SUCCESS

FILES CHANGED:
- mdparser/blocks.py
- mdparser/render.py
- mdparser/inlines.py
- mdparser/cli.py
- tests/test_executable.py
- tests/test_foundation.py
- tests/test_blocks.py
- tests/test_render.py
- tests/test_block_engine.py

SUMMARY:
Implemented the phase 1 block engine with an extensible block-type registry, paragraph and blank-line handling, tab-aware columns, and HTML rendering with escaping. Also added the URL percent-encoding helper for the link stories. Project suite via `bin/test.sh`: 132 passed. Declared checks engine-paragraph-count, engine-multiline-paragraph, engine-blank-lines-ignored, and engine-html-escaping pass. Conformance suite not run: no criterion in this step invokes it. Placeholder tests asserting empty output were updated to the rendered output.

BLOCKERS:
- None.
